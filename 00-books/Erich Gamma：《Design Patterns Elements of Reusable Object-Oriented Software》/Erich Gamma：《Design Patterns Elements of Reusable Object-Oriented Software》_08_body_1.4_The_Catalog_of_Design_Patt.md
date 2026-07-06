# 1.4 The Catalog of Design Patterns / 1.5 Organizing the Catalog

> Section: body | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

## 1.4 The Catalog of Design Patterns

The catalog beginning on page 79 contains 23 design patterns. Their names and intents are listed next to give you an overview. The number in parentheses after each pattern name gives the page number for the pattern (a convention we follow throughout the book).

Abstract Factory (87) Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

Adapter (139) Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.

Bridge (151) Decouple an abstraction from its implementation so that the two can vary independently.

Builder (97) Separate the construction of a complex object from its representation so that the same construction process can create different

representations.

Chain of Responsibility (223) Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.

Command (233) Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

Composite (163) Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

Decorator (175) Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

Facade (185) Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

Factory Method (107) Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

Flyweight (195) Use sharing to support large numbers of fine-grained objects efficiently.

Interpreter (243) Given a language, define a represention for its grammar along with an interpreter that uses the representation to interpret sentences in the language.

Iterator (257) Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

Mediator (273) Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.

Memento (283) Without violating encapsulation, capture and externalize an object’s internal state so that the object can be restored to this state later.

Observer (293) Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

Prototype (117) Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

Proxy (207) Provide a surrogate or placeholder for another object to control access to it.

Singleton (127) Ensure a class only has one instance, and provide a global point of access to it.

State (305) Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.

Strategy (315) Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

Template Method (325) Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.

Visitor (331) Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.

## 1.5 Organizing the Catalog

Design patterns vary in their granularity and level of abstraction. Because there are many design patterns, we need a way to organize them. This section classifies design patterns so that we can refer to families of related patterns. The classification helps you learn the patterns in the catalog faster, and it can direct efforts to find new patterns as well.

We classify design patterns by two criteria ( Table 1.1). The first criterion, called purpose, reflects what a pattern does. Patterns can have either creational, structural, or behavioral purpose. Creational patterns concern the process of object creation. Structural patterns deal with the composition of classes or objects. Behavioral patterns characterize the ways in which classes or objects interact and distribute responsibility.

Table 1.1: Design pattern space
<table><tr><td rowspan=2 colspan=2></td><td rowspan=1 colspan=3>Purpose</td></tr><tr><td rowspan=1 colspan=1>Creational</td><td rowspan=1 colspan=1>Structural</td><td rowspan=1 colspan=1>Behavioral</td></tr><tr><td rowspan=2 colspan=1>Scope</td><td rowspan=1 colspan=1>Class</td><td rowspan=1 colspan=1>Factory Method (107)</td><td rowspan=1 colspan=1>Adapter (class) (139)</td><td rowspan=1 colspan=1>Interpreter (243)Template Method (325)</td></tr><tr><td rowspan=1 colspan=1>Object</td><td rowspan=1 colspan=1>Abstract Factory (87)Builder (97)Prototype (117)Singleton (127)</td><td rowspan=1 colspan=1>Adapter (object) (139)Bridge (151)Composite (163)Decorator (175)Facade (185)Flyweight (195)Proxy (207)</td><td rowspan=1 colspan=1>Chain of Responsibility (223)Command (233)Iterator (257)Mediator (273)Memento (283)Observer (293)State (305)Strategy (315)Visitor (331)</td></tr></table>

The second criterion, called scope, specifies whether the pattern applies primarily to classes or to objects. Class patterns deal with relationships between classes and their subclasses. These relationships are established through inheritance, so they are static— fixed at compile-time. Object patterns deal with object relationships, which can be changed at run-time and are more dynamic. Almost all patterns use inheritance to some extent. So the only patterns labeled “class patterns” are those that focus on class relationships. Note that most patterns are in the Object scope. Creational class patterns defer some part of object creation to subclasses, while Creational object patterns defer it to another object. The Structural class patterns use inheritance to compose classes, while the Structural object patterns describe ways to assemble objects. The Behavioral class patterns use inheritance to describe algorithms and flow of control, whereas the Behavioral object patterns describe how a group of objects cooperate to perform a task that no single object can carry out alone. There are other ways to organize the patterns. Some patterns are often used together. For example, Composite is often used with Iterator or Visitor. Some patterns are alternatives: Prototype is often an alternative to Abstract Factory. Some patterns result in similar designs even though the patterns have different intents. For example, the structure diagrams of Composite and Decorator are similar. Yet another way to organize design patterns is according to how they reference each other in their “Related Patterns” sections. Figure 1.1 depicts these relationships graphically.

