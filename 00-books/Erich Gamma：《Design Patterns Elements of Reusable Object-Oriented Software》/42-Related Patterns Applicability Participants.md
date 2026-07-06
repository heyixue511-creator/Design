assignments that change several registers at once.

Another example of this pattern occurs in the financial domain, where a portfolio aggregates individual assets. You can support complex aggregations of assets by implementing a portfolio as a Composite that conforms to the interface of an individual asset [BE93].

The Command (233) pattern describes how Command objects can be composed and sequenced with a MacroCommand Composite class.

## Related Patterns

Often the component-parent link is used for a Chain of Responsibility (223).

Decorator (175) is often used with Composite. When decorators and composites are used together, they will usually have a common parent class. So decorators will have to support the Component interface with operations like Add, Remove, and GetChild.

Flyweight (195) lets you share components, but they can no longer refer to their parents.

Iterator (257) can be used to traverse composites.

Visitor (331) localizes operations and behavior that would otherwise be distributed across Composite and Leaf classes.

## Object Structural: Decorator

## Intent

Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

## Also Known As

Wrapper

## Motivation

Sometimes we want to add responsibilities to individual objects, not to an entire class. A graphical user interface toolkit, for example, should let you add properties like borders or behaviors like scrolling to any user interface component.

One way to add responsibilities is with inheritance. Inheriting a border from another class puts a border around every subclass instance. This is inflexible, however, because the choice of border is made statically. A client can’t control how and when to decorate the component with a border.

A more flexible approach is to enclose the component in another object that adds the border. The enclosing object is called a decorator. The decorator conforms to the interface of the component it decorates so that its presence is transparent to the component’s clients. The decorator forwards requests to the component and may perform additional actions (such as drawing a border) before or after forwarding. Transparency lets you nest decorators recursively, thereby allowing an unlimited number of added responsibilities.

![](images/eb3db0a99a40134fba931ef28c1917213f706008b31f87e85e18e02be48aef96.jpg)

For example, suppose we have a TextView object that displays text in a window. TextView has no scroll bars by default, because we might not always need them. When we do, we can use a ScrollDecorator to add them. Suppose we also want to add a thick black border around the TextView. We can use a BorderDecorator to add this as well. We simply compose the decorators with the TextView to produce the desired result.

The following object diagram shows how to compose a TextView object with BorderDecorator and ScrollDecorator objects to produce a bordered, scrollable text view:

![](images/4d2a946bdb286552f87bbda8f01e4b7b68bef50727214e90416ebecfe435512f.jpg)

The ScrollDecorator and BorderDecorator classes are subclasses of Decorator, an abstract class for visual components that decorate other visual components.

![](images/e51ce602d122aa2bc095c71416989cf8488bab00352ea36bd9bc9aec8d4a0e80.jpg)

VisualComponent is the abstract class for visual objects. It defines their drawing and event handling interface. Note how the Decorator class simply forwards draw requests to its component, and how Decorator subclasses can extend this operation.

Decorator subclasses are free to add operations for specific functionality. For example, ScrollDecorator’s ScrollTo operation lets other objects scroll the interface if they know there happens to be a ScrollDecorator object in the interface. The important aspect of this pattern is that it lets decorators appear anywhere a VisualComponent can. That way clients generally can’t tell the difference between a decorated component and an undecorated one, and so they don’t depend at all on the decoration.

## Applicability

Use Decorator

• to add responsibilities to individual objects dynamically and transparently, that is, without affecting other objects.

• for responsibilities that can be withdrawn.

• when extension by subclassing is impractical. Sometimes a large number of independent extensions are possible and would produce an explosion of subclasses to support every combination. Or a class definition may be hidden or otherwise unavailable for subclassing.

## Structure

![](images/2d5c64677dab34a55c2677e9d070a78efcb33139cb403b0e0e6f17a908ace193.jpg)

## Participants

• Component (VisualComponent)

– defines the interface for objects that can have responsibilities added to them dynamically.

• ConcreteComponent (TextView)

– defines an object to which additional responsibilities can be attached.

## • Decorator

– maintains a reference to a Component object and defines an interface that conforms to Component’s interface.

• ConcreteDecorator (BorderDecorator, ScrollDecorator)

– adds responsibilities to the component.

## Collaborations

• Decorator forwards requests to its Component object. It may optionally perform additional operations before and after forwarding the request.

## Consequences

The Decorator pattern has at least two key benefits and two liabilities:

1 . More flexibility than static inheritance. The Decorator pattern provides a more flexible way to add responsibilities to objects than can be had with static (multiple) inheritance. With decorators, responsibilities can be added and removed at run-time simply by attaching and detaching them. In contrast, inheritance requires creating a new class for each additional responsibility (e.g.,