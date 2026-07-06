design patterns than to formalize it.

From Alexander’s point of view, the patterns in this book do not form a pattern language. Given the variety of software systems that people build, it’s hard to see how we could provide a “complete” set of patterns, one that offers step-by-step instructions for designing an application. We can do that for certain classes of applications, such as report-writing or making a forms-entry system. But our catalog is just a collection of related patterns; we can’t pretend it’s a pattern language.

In fact, we think it’s unlikely that there will ever be a complete pattern language for software. But it’s certainly possible to make one that is more complete. Additions would have to include frameworks and how to use them [Joh92], patterns for user interface design [BJ94], analysis patterns [Coa92], and all the other aspects of developing software. Design patterns are just a part of a larger pattern language for software.

## Patterns in Software

Our first collective experience in the study of software architecture was at an OOPSLA ’91 workshop led by Bruce Anderson. The workshop was dedicated to developing a handbook for software architects. (Judging from this book, we suspect “architecture encyclopedia” will be a more appropriate name than “architecture handbook.”) That first workshop has led to a series of meetings, the most recent of which being the first conference on Pattern Languages of Programs held in August 1994. This has created a community of people interested in documenting software expertise.

Of course, others have had this goal as well. Donald Knuth’s The Art of Computer Programming [Knu73] was one of the first attempts to catalog software knowledge, though he focused on describing algorithms. Even so, the task proved too great to finish. T h e Graphics Gems series [Gla90, Arv91, Kir92] is another catalog of design knowledge, though it too tends to focus on algorithms. The Domain Specific Software Architecture program sponsored by the U.S. Department of Defense [GM92] concentrates on gathering architectural information. The knowledge-based software engineering community tries to represent software-related knowledge in general. There are many other groups with goals at least a little like ours.

James Coplien’s Advanced C++: Programming Styles and Idioms [Cop92] has influenced us, too. The patterns in his book tend to be more C++-specific than our design patterns, and his book contains lots of lower-level patterns as well. But there is some overlap, as we point out in our patterns. Jim has been active in the pattern community. He’s currently working on patterns that describe people’s roles in software development organizations.

There are a lot of other places in which to find descriptions of patterns. Kent Beck was one of the first people in the software community to advocate Christopher Alexander’s work. In 1993 he started writing a column in The Smalltalk Report on Smalltalk patterns. Peter Coad has also been collecting patterns for some time. His paper on patterns seems to us to contain mostly analysis patterns [Coa92]; we haven’t seen his latest patterns, though we know he is still working on them. We’ve heard of several books on patterns that are in the works, but we haven’t seen any of them, either. All we can do is let you know they’re coming. One of these books will be from the Pattern Languages of Programs conference.

## 6.4 An Invitation

What can you do if you are interested in patterns? First, use them and look for other patterns that fit the way you design. A lot of books and articles about patterns will be coming out in the next few years, so there will be plenty of sources for new patterns. Develop your vocabulary of patterns, and use it. Use it when you talk with other people about your designs. Use it when you think and write about them.

Second, be a critical consumer. The design pattern catalog is the result of hard work, not just ours but that of dozens of reviewers who gave us feedback. If you spot a problem or believe more explanation is needed, contact us. The same goes for any other catalog of patterns: Give the authors feedback! One of the great things about patterns is that they move design decisions out of the realm of vague intuition. They let authors be explicit about the trade-offs they make. This makes it easier to see what is wrong with their patterns and to argue with them. Take advantage of that.

Third, look for patterns you use, and write them down. Make them a part of your documentation. Show them to other people. You don’t have to be in a research lab to find patterns. In fact, finding relevant patterns is nearly impossible if you don’t have practical experience. Feel free to write your own catalog of patterns...but make sure someone else helps you beat them into shape!

## 6.5 A Parting Thought

The best designs will use many design patterns that dovetail and intertwine to produce a greater whole. As Christopher Alexander says:

It is possible to make buildings by stringing together patterns, in a rather loose way. A building made like this, is an assembly of patterns. It is not dense. It is not profound. But it is also possible to put patterns together in such a way that many patterns overlap in the same physical space: the building is very dense; it has many meanings captured in a small space; and through this density, it becomes profound.

## Appendix A

## Glossary

abstract class A class whose primary purpose is to define an interface. An abstract class defers some or all of its implementation to subclasses. An abstract class cannot be instantiated.

abstract coupling Given a class A that maintains a reference to an abstract class B, class A is said to be abstractly coupled to B. We call this abstract coupling because A refers to a type of object, not a concrete object.

abstract operation An operation that declares a signature but doesn’t implement it. In C++, an abstract operation corresponds to a pure virtual member function.

acquaintance relationship A class that refers to another class has an acquaintance with that class.

aggregate object An object that’s composed of subobjects. The subobjects are called the aggregate’s parts, and the aggregate is responsible for them.

aggregation relationship The relationship of an aggregate object to its parts. A class defines this relationship for its instances (e.g., aggregate objects).

black-box reuse A style of reuse based on object composition. Composed objects reveal no internal details to each other and are thus analogous to “black boxes.”

class A class defines an object’s interface and implementation. It specifies the object’s internal representation and defines the operations the object can perform.

class diagram A diagram that depicts classes, their internal structure and operations, and the static relationships between them.

class operation An operation targeted to a class and not to an individual object. In C++, class operations are are called static member functions.

concrete class A class having no abstract operations. It can be instantiated.

constructor In C++, an operation that is automatically invoked to initialize new instances.

coupling The degree to which software components depend on each other.

delegation An implementation mechanism in which an object forwards or delegates a request to another object. The delegate carries out the request on behalf of the original object.

design pattern A design pattern systematically names, motivates, and explains a general design that addresses a recurring design problem in object-oriented systems. It describes the problem, the solution, when to apply the solution, and its consequences. It also gives implementation hints and examples. The solution is a general arrangement of objects and classes that solve the problem. The solution is customized and implemented to solve the problem in a particular context.

destructor In C++, an operation that is automatically invoked to finalize an object that is about to be deleted.

dynamic binding The run-time association of a request to an object and one of its operations. In C++, only virtual functions are dynamically bound.

encapsulation The result of hiding a representation and implementation in an object. The representation is not visible and cannot be accessed directly from outside the object. Operations are the only way to access and modify an object’s representation.

framework A set of cooperating classes that makes up a reusable design for a specific class of software. A framework provides architectural guidance by partitioning the design into abstract classes and defining their responsibilities and collaborations. A developer customizes the framework to a particular application by subclassing and composing instances of framework classes.

friend class In C++, a class that has the same access rights to the operations and data of a class as that class itself.

inheritance A relationship that defines one entity in terms of another. Class inheritance defines a new class in terms of one or more parent classes. The new class inherits its interface and implementation from its parents. The new class is called a subclass or (in C++) a derived class. Class inheritance combines interface inheritance and implementation inheritance. Interface inheritance defines a new interface in terms of one or more existing interfaces. Implementation inheritance defines a new implementation in terms of one or more existing implementations.

instance variable A piece of data that defines part of an object’s representation. C++ uses the term data member.

interaction diagram A diagram that shows the flow of requests between objects.

interface The set of all signatures defined by an object’s operations. The interface describes the set of requests to which an object can respond.

metaclass Classes are objects in Smalltalk. A metaclass is the class of a class object.

mixin class A class designed to be combined with other classes through inheritance. Mixin classes are usually abstract.

object A run-time entity that packages both data and the procedures that operate on that data.

object composition Assembling or composing objects to get more complex behavior.

object diagram A diagram that depicts a particular object structure at run-time.

object reference A value that identifies another object.

operation An object’s data can be manipulated only by its operations. An object performs an operation when it receives a request. In C++, operations are called member functions. Smalltalk uses the term method.

overriding Redefining an operation (inherited from a parent class) in a subclass.

parameterized type A type that leaves some constituent types unspecified. The unspecified types are supplied as parameters at the point of use. In C++, parameterized types are called templates.

parent class The class from which another class inherits. Synonyms are superclass (Smalltalk), base class (C++), and ancestor class.

polymorphism The ability to substitute objects of matching interface for one another at run-time.

private inheritance In C++, a class inherited solely for its implementation.

protocol Extends the concept of an interface to include the allowable sequences of requests.

receiver The target object of a request.

request An object performs an operation when it receives a corresponding request from another object. A common synonym for request is message.

signature An operation’s signature defines its name, parameters, and return value.

subclass A class that inherits from another class. In C++, a subclass is called a derived class.

subsystem An independent group of classes that collaborate to fulfill a set of

responsibilities.

subtype A type is a subtype of another if its interface contains the interface of the other type.

supertype The parent type from which a type inherits.

toolkit A collection of classes that provides useful functionality but does not define the design of an application.

type The name of a particular interface.

white-box reuse A style of reuse based on class inheritance. A subclass reuses the interface and implementation of its parent class, but it may have access to otherwise private aspects of its parent.