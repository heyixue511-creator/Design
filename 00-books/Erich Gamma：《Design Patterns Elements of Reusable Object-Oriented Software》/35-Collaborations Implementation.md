– defines the domain-specific interface that Client uses.

• Client (DrawingEditor)

– collaborates with objects conforming to the Target interface.

• Adaptee (TextView)

– defines an existing interface that needs adapting.

• Adapter (TextShape)

– adapts the interface of Adaptee to the Target interface.

## Collaborations

• Clients call operations on an Adapter instance. In turn, the adapter calls Adaptee operations that carry out the request.

## Consequences

Class and object adapters have different trade-offs. A class adapter

• adapts Adaptee to Target by committing to a concrete Adaptee class. As a consequence, a class adapter won’t work when we want to adapt a class and all its subclasses.

• lets Adapter override some of Adaptee’s behavior, since Adapter is a subclass of Adaptee.

• introduces only one object, and no additional pointer indirection is needed to get to the adaptee.

An object adapter

• lets a single Adapter work with many Adaptees—that is, the Adaptee itself and all of its subclasses (if any). The Adapter can also add functionality to all Adaptees at once.

• makes it harder to override Adaptee behavior. It will require subclassing Adaptee and making Adapter refer to the subclass rather than the Adaptee itself.

Here are other issues to consider when using the Adapter pattern:

1. How much adapting does Adapter do? Adapters vary in the amount of work they do to adapt Adaptee to the Target interface. There is a spectrum of possible work, from simple interface conversion—for example, changing the names of operations—to supporting an entirely different set of operations. The amount of work

Adapter does depends on how similar the Target interface is to Adaptee’s.

2 . Pluggable adapters. A class is more reusable when you minimize the assumptions other classes must make to use it. By building interface adaptation into a class, you eliminate the assumption that other classes see the same interface. Put another way, interface adaptation lets us incorporate our class into existing systems that might expect different interfaces to the class. Object-Works\Smalltalk [Par90] uses the term pluggable adapter to describe classes with built-in interface adaptation.

Consider a TreeDisplay widget that can display tree structures graphically. If this were a special-purpose widget for use in just one application, then we might require the objects that it displays to have a specific interface; that is, all must descend from a Tree abstract class. But if we wanted to make TreeDisplay more reusable (say we wanted to make it part of a toolkit of useful widgets), then that requirement would be unreasonable. Applications will define their own classes for tree structures. They shouldn’t be forced to use our Tree abstract class. Different tree structures will have different interfaces.

In a directory hierarchy, for example, children might be accessed with a GetSubdirectories operation, whereas in an inheritance hierarchy, the corresponding operation might be called GetSubclasses. A reusable TreeDisplay widget must be able to display both kinds of hierarchies even if they use different interfaces. In other words, the TreeDisplay should have interface adaptation built into it.

We’ll look at different ways to build interface adaptation into classes in the Implementation section.

3. Using two-way adapters to provide transparency. A potential problem with adapters is that they aren’t transparent to all clients. An adapted object no longer conforms to the Adaptee interface, so it can’t be used as is wherever an Adaptee object can. Two-way adapters can provide such transparency. Specifically, they’re useful when two different clients need to view an object differently.

Consider the two-way adapter that integrates Unidraw, a graphical editor framework [VL90], and QOCA, a constraint-solving toolkit [HHMV92]. Both systems have classes that represent variables explicitly: Unidraw has State Variable, and QOCA has ConstraintVariable. To make Unidraw work with QOCA, ConstraintVariable must be adapted to State Variable; to let QOCA propagate solutions to Unidraw, State Variable must be adapted to ConstraintVariable.

![](images/d14df736169279aad04a2d379bf0b8c2dda852090e8c78fee41dd0df29cde1d5.jpg)

The solution involves a two-way class adapter ConstraintStateVariable, a subclass of both State Variable and ConstraintVariable, that adapts the two interfaces to each other. Multiple inheritance is a viable solution in this case because the interfaces of the adapted classes are substantially different. The two-way class adapter conforms to both of the adapted classes and can work in either system.

## Implementation

Although the implementation of Adapter is usually straightforward, here are some issues to keep in mind:

1 . Implementing class adapters in C++. In a C++ implementation of a class adapter, Adapter would inherit publicly from Target and privately from Adaptee. Thus Adapter would be a subtype of Target but not of Adaptee.

2. Pluggable adapters. Let’s look at three ways to implement pluggable adapters for the TreeDisplay widget described earlier, which can lay out and display a hierarchical structure automatically.

The first step, which is common to all three of the implementations discussed here, is to find a “narrow” interface for Adaptee, that is, the smallest subset of operations that lets us do the adaptation. A narrow interface consisting of only a couple of operations is easier to adapt than an interface with dozens of operations. For TreeDisplay, the adaptee is any hierarchical structure. A minimalist interface might include two operations, one that defines how to present a node in the hierarchical structure graphically, and another that retrieves the node’s children.

The narrow interface leads to three implementation approaches:

(a) Using abstract operations. Define corresponding abstract operations for the narrow Adaptee interface in the TreeDisplay class. Subclasses must implement the abstract operations and adapt the hierarchically structured object. For example, a DirectoryTreeDisplay subclass will implement these operations by accessing the directory structure.

![](images/34276e53fcfeaa2a1bb06a289fb51fce9eabb69365113faf156e3239bbaa78f9.jpg)  
DirectoryTreeDisplay specializes the narrow interface so that it can display directory structures made up of FileSystemEntity objects.

(b) Using delegate objects. In this approach, TreeDisplay forwards requests for accessing the hierarchical structure to a delegate object. TreeDisplay can use a different adaptation strategy by substituting a different delegate.

For example, suppose there exists a DirectoryBrowser that uses a Tree-Display. DirectoryBrowser might make a good delegate for adapting TreeDisplay to the hierarchical directory structure. In dynamically typed languages like Smalltalk or Objective C, this approach only requires an interface for registering the delegate with the adapter. Then TreeDisplay simply forwards the requests to the delegate. NEXTSTEP [Add94] uses this approach heavily to reduce subclassing.

Statically typed languages like C++ require an explicit interface definition for the delegate. We can specify such an interface by putting the narrow interface that TreeDisplay requires into an abstract TreeAccessorDelegate class. Then we can mix this interface into the delegate of our choice—DirectoryBrowser in this case—using inheritance. We use single inheritance if the DirectoryBrowser has no existing parent class, multiple inheritance if it does. Mixing classes together like this is easier than introducing a new TreeDisplay subclass and implementing its operations individually.

![](images/cea03a51313420de66cd475792912ab19d4fd1411c6f37353d9685e8df68a652.jpg)