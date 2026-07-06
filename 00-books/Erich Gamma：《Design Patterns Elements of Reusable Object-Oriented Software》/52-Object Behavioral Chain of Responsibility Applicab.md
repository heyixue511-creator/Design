its state object changes. Visitor (331) encapsulates behavior that would otherwise be distributed across classes, and Iterator (257) abstracts the way you access and traverse objects in an aggregate.

## Object Behavioral: Chain of Responsibility

## Intent

Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.

## Motivation

Consider a context-sensitive help facility for a graphical user interface. The user can obtain help information on any part of the interface just by clicking on it. The help that’s provided depends on the part of the interface that’s selected and its context; for example, a button widget in a dialog box might have different help information than a similar button in the main window. If no specific help information exists for that part of the interface, then the help system should display a more general help message about the immediate context—the dialog box as a whole, for example.

Hence it’s natural to organize help information according to its generality—from the most specific to the most general. Furthermore, it’s clear that a help request is handled by one of several user interface objects; which one depends on the context and how specific the available help is.

The problem here is that the object that ultimately provides the help isn’t known explicitly to the object (e.g., the button) that initiates the help request. What we need is a way to decouple the button that initiates the help request from the objects that might provide help information. The Chain of Responsibility pattern defines how that happens.

The idea of this pattern is to decouple senders and receivers by giving multiple objects a chance to handle a request. The request gets passed along a chain of objects until one of them handles it.

![](images/2305dbc835e04b886b83d1241eb08c15364ade649396de72bff798f4150810db.jpg)

The first object in the chain receives the request and either handles it or forwards it to the next candidate on the chain, which does likewise. The object that made the request has no explicit knowledge of who will handle it—we say the request has an implicit receiver.

Let’s assume the user clicks for help on a button widget marked “Print.” The button is contained in an instance of PrintDialog, which knows the application object it belongs to (see preceding object diagram). The following interaction diagram illustrates how the help request gets forwarded along the chain:

![](images/e81c0c8f21c92860f7b3c018e786d499d40966f4ec1107ea2386af18d591181b.jpg)

In this case, neither aPrintButton nor aPrintDialog handles the request; it stops at anApplication, which can handle it or ignore it. The client that issued the request has no direct reference to the object that ultimately fulfills it.

To forward the request along the chain, and to ensure receivers remain implicit, each object on the chain shares a common interface for handling requests and for accessing its successor on the chain. For example, the help system might define a HelpHandler class with a corresponding HandleHelp operation. HelpHandler can be the parent class for candidate object classes, or it can be defined as a mixin class. Then classes that want to handle help requests can make HelpHandler a parent:

![](images/6c1ba2130f2fe43390de8d5deb0e7cbbb67716cd1367689e324013b50feebac0.jpg)

The Button, Dialog, and Application classes use HelpHandler operations to handle help requests. HelpHandler’s HandleHelp operation forwards the request to the successor by default. Subclasses can override this operation to provide help under the right circumstances; otherwise they can use the default implementation to forward the request.

## Applicability

Use Chain of Responsibility when

• more than one object may handle a request, and the handler isn’t known a priori. The handler should be ascertained automatically.

• you want to issue a request to one of several objects without specifying the receiver explicitly.

• the set of objects that can handle a request should be specified dynamically.

## Structure

![](images/9a51f2f8594283829efbba9d4a41dfe1cc7036a1ddf0b327e90f6b9f592b9335.jpg)  
A typical object structure might look like this:

![](images/938e2b93b583c27162bec746b06540942b3039452c197879fa7bed914210af0c.jpg)

## Participants

• Handler (HelpHandler)

– defines an interface for handling requests.

– (optional) implements the successor link.

• ConcreteHandler (PrintButton, PrintDialog)

– handles requests it is responsible for.

– can access its successor.

– if the ConcreteHandler can handle the request, it does so; otherwise it forwards the request to its successor.

## • Client

– initiates the request to a ConcreteHandler object on the chain.

## Collaborations

• When a client issues a request, the request propagates along the chain until a ConcreteHandler object takes responsibility for handling it.

## Consequences

Chain of Responsibility has the following benefits and liabilities:

1 . Reduced coupling. The pattern frees an object from knowing which other object handles a request. An object only has to know that a request will be handled “appropriately.” Both the receiver and the sender have no explicit knowledge of each other, and an object in the chain doesn’t have to know about the chain’s structure.

As a result, Chain of Responsibility can simplify object interconnections. Instead of objects maintaining references to all candidate receivers, they keep a single reference to their successor.

2 . Added flexibility in assigning responsibilities to objects. Chain of Responsibility gives you added flexibility in distributing responsibilities among objects. You can add or change responsibilities for handling a request by adding to