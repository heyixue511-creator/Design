void TCPClosed::ActiveOpen (TCPConnection\* t)(   
// send SYN, receive SYN, ACK, etc.   
ChangeState(t, TCPEstablished::Instance());   
void TCPClosed::PassiveOpen (TCPConnection\*t){   
ChangeState(t, TCPListen::Instance());   
void TCPEstablished::Close (TCPConnection\* t){   
// send FIN, receive ACK of FIN   
ChangeState(t, TCPListen::Instance());   
}   
void TCPEstablished::Transmit (   
TCPConnection\*t,TCPOctetStream\*o   
t->ProcessOctet(o);   
void TCPListen::Send (TCPConnection\* t){   
// send SYN, receive SYN, ACK, etc.   
ChangeState(t, TCPEstablished::Instance());

After performing state-specific work, these operations call the ChangeState operation to change the state of the TCPConnection. TCPConnection itself doesn’t know a thing about the TCP connection protocol; it’s the TCPState subclasses that define each state transition and action in TCP.

## Known Uses

Johnson and Zweig [JZ91] characterize the State pattern and its application to TCP connection protocols.

Most popular interactive drawing programs provide “tools” for performing operations by direct manipulation. For example, a line-drawing tool lets a user click and drag to create a new line. A selection tool lets the user select shapes. There’s usually a palette of such tools to choose from. The user thinks of this activity as picking up a tool and wielding it, but in reality the editor’s behavior changes with the current tool: When a drawing tool is active we create shapes; when the selection tool is active we select shapes; and so forth. We can use the State pattern to change the editor’s behavior depending on the current tool.

We can define an abstract Tool class from which to define subclasses that implement tool-specific behavior. The drawing editor maintains a current Tool object and delegates requests to it. It replaces this object when the user chooses a new tool, causing the behavior of the drawing editor to change accordingly.

This technique is used in both the HotDraw [Joh92] and Unidraw [VL90] drawing editor frameworks. It allows clients to define new kinds of tools easily. In HotDraw, the DrawingController class forwards the requests to the current Tool object. In Unidraw, the corresponding classes are Viewer and Tool. The following class diagram sketches the Tool and DrawingController interfaces:

![](images/25f0f575a68ce1a7b8a3efa829643d1885dceb519021cd7281debdef1b8e383b.jpg)

Coplien’s Envelope-Letter idiom [Cop92] is related to State. Envelope-Letter is a technique for changing an object’s class at run-time. The State pattern is more specific, focusing on how to deal with an object whose behavior depends on its state.

## Related Patterns

The Flyweight (195) pattern explains when and how State objects can be shared.

State objects are often Singletons (127).

## Object Behavioral: Strategy

## Intent

Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

## Also Known As

Policy

## Motivation

Many algorithms exist for breaking a stream of text into lines. Hard-wiring all such algorithms into the classes that require them isn’t desirable for several reasons:

• Clients that need linebreaking get more complex if they include the linebreaking code. That makes clients bigger and harder to maintain, especially if they support multiple linebreaking algorithms.

• Different algorithms will be appropriate at different times. We don’t want to support multiple linebreaking algorithms if we don’t use them all.

• It’s difficult to add new algorithms and vary existing ones when linebreaking is an integral part of a client.

We can avoid these problems by defining classes that encapsulate different linebreaking algorithms. An algorithm that’s encapsulated in this way is called a strategy.

![](images/997892f41f0f59ab1c14802b860b12ca798f170849309f781605d1c661c2e163.jpg)

Suppose a Composition class is responsible for maintaining and updating the linebreaks of text displayed in a text viewer. Linebreaking strategies aren’t implemented by the class Composition. Instead, they are implemented separately by subclasses of the abstract Compositor class. Compositor subclasses implement different strategies:

• SimpleCompositor implements a simple strategy that determines linebreaks one at a time.

• TeXCompositor implements the $\mathrm { T _ { E } X }$ algorithm for finding linebreaks. This strategy tries to optimize linebreaks globally, that is, one paragraph at a time.

• ArrayCompositor implements a strategy that selects breaks so that each row has a fixed number of items. It’s useful for breaking a collection of icons into rows, for example.

A Composition maintains a reference to a Compositor object. Whenever a Composition reformats its text, it forwards this responsibility to its Compositor object. The client of Composition specifies which Compositor should be used by installing the Compositor it desires into the Composition.

## Applicability

Use the Strategy pattern when

• many related classes differ only in their behavior. Strategies provide a way to configure a class with one of many behaviors.

• you need different variants of an algorithm. For example, you might define algorithms reflecting different space/time trade-offs. Strategies can be used when these variants are implemented as a class hierarchy of algorithms [HO87].

• an algorithm uses data that clients shouldn’t know about. Use the Strategy pattern to avoid exposing complex, algorithm-specific data structures.

• a class defines many behaviors, and these appear as multiple conditional statements in its operations. Instead of many conditionals, move related conditional branches into their own Strategy class.

## Structure

![](images/3f973a03e7d1e09f19ebd52c3b80a4c1473f0ea9c0685217aee35e0e8d080054.jpg)

## Participants

• Strategy (Compositor)

– declares an interface common to all supported algorithms. Context uses this interface to call the algorithm defined by a ConcreteStrategy.

• ConcreteStrategy (SimpleCompositor, TeXCompositor, ArrayCompositor)

– implements the algorithm using the Strategy interface.

• Context (Composition)

– is configured with a ConcreteStrategy object.

– maintains a reference to a Strategy object.

– may define an interface that lets Strategy access its data.

## Collaborations

• Strategy and Context interact to implement the chosen algorithm. A context may