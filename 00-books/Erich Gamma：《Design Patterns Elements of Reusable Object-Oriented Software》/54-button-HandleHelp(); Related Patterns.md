propagates to this level, the application can supply information on the application in general, or it can offer a list of different help topics:

class Application : public HelpHandler {   
public:   
Application(Topic t) : HelpHandler(0, t){}   
virtualvoid HandleHelp();   
//application-specific operations...   
void Application::HandleHelp () {   
// show a list of help topics

The following code creates and connects these objects. Here the dialog concerns printing, and so the objects have printing-related topics assigned.

constTopic PRINT\_TOPIC = 1;   
const Topic PAPER\_ORIENTATION\_TOPIC = 2;   
constTopic APPLICATION\_TOPIC = 3;   
Application\* application = new Application(APPLICATION\_TOPIC);   
Dialog\*dialog = new Dialog(application, PRINT\_TOPIC);   
Button\* button = new Button(dialog, PAPER\_ORIENTATION\_TOPIC);

We can invoke the help request by calling HandleHelp on any object on the chain. To start the search at the button object, just call HandleHelp on it:

## button->HandleHelp();

In this case, the button will handle the request immediately. Note that any HelpHandler class could be made the successor of Dialog. Moreover, its successor could be changed dynamically. So no matter where a dialog is used, you’ll get the proper context-dependent help information for it.

## Known Uses

Several class libraries use the Chain of Responsibility pattern to handle user events. They use different names for the Handler class, but the idea is the same: When the user clicks the mouse or presses a key, an event gets generated and passed along the chain. MacApp [App89] and ET++ [WGM88] call it “Event-Handler,” Symantec’s TCL library [Sym93b] calls it “Bureaucrat,” and NeXT’s AppKit [Add94] uses the name “Responder.”

The Unidraw framework for graphical editors defines Command objects that encapsulate requests to Component and Component View objects [VL90]. Commands are requests in the sense that a component or component view may interpret a command to perform an operation. This corresponds to the “requests as objects” approach described in Implementation. Components and component views may be structured hierarchically. A component or a component view may forward command interpretation to its parent, which may in turn forward it to its parent, and so on, thereby forming a chain of responsibility.

ET++ uses Chain of Responsibility to handle graphical update. A graphical object calls the InvalidateRect operation whenever it must update a part of its appearance. A graphical object can’t handle InvalidateRect by itself, because it doesn’t know enough about its context. For example, a graphical object can be enclosed in objects like Scrollers or Zoomers that transform its coordinate system. That means the object might be scrolled or zoomed so that it’s partially out of view. Therefore the default implementation of InvalidateRect forwards the request to the enclosing container object. The last object in the forwarding chain is a Window instance. By the time Window receives the request, the invalidation rectangle is guaranteed to be transformed properly. The Window handles InvalidateRect by notifying the window system interface and requesting an update.

## Related Patterns

Chain of Responsibility is often applied in conjunction with Composite (163). There, a component’s parent can act as its successor.

## Object Behavioral: Command

## Intent

Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

## Also Known As

Action, Transaction

## Motivation

Sometimes it’s necessary to issue requests to objects without knowing anything about the operation being requested or the receiver of the request. For example, user interface toolkits include objects like buttons and menus that carry out a request in response to user input. But the toolkit can’t implement the request explicitly in the button or menu, because only applications that use the toolkit know what should be done on which object. As toolkit designers we have no way of knowing the receiver of the request or the operations that will carry it out.

The Command pattern lets toolkit objects make requests of unspecified application objects by turning the request itself into an object. This object can be stored and passed around like other objects. The key to this pattern is an abstract Command class, which declares an interface for executing operations. In the simplest form this interface includes an abstract Execute operation. Concrete Command subclasses specify a receiver-action pair by storing the receiver as an instance variable and by implementing Execute to invoke the request. The receiver has the knowledge required to carry out the request.

![](images/3fa3e98e69eb5ed7dd2c297ba68b34cae54817c611867b29aae0c26a23fd26ec.jpg)

Menus can be implemented easily with Command objects. Each choice in a Menu is an instance of a Menultem class. An Application class creates these menus and their menu items along with the rest of the user interface. The Application class also keeps track of Document objects that a user has opened.

The application configures each Menultem with an instance of a concrete Command subclass. When the user selects a Menultem, the Menultem calls Execute on its command, and Execute carries out the operation. Menultems don’t know which subclass of Command they use. Command subclasses store the receiver of the request and invoke one or more operations on the receiver.

For example, PasteCommand supports pasting text from the clipboard into a Document. PasteCommand’s receiver is the Document object it is supplied upon instantiation. The Execute operation invokes Paste on the receiving Document.

![](images/cdfff36a40d38e18d5f0825f90559aed4c2d10e5e3f8a2e1ff0858000915daed.jpg)

OpenCommand’s Execute operation is different: it prompts the user for a document name, creates a corresponding Document object, adds the document to the receiving application, and opens the document.

![](images/9c966562630b3242972317c954d32e4a7a1217942c604757e8eadc44d2ed38f6.jpg)  
Sometimes a Menultem needs to execute a sequence of commands. For example, a Menultem for centering a page at normal size could be constructed from a CenterDocumentCommand object and a NormalSizeCommand object. Because it’s common to string commands together in this way, we can define a MacroCommand class to allow a Menultem to execute an open-ended number of commands.

MacroCommand is a concrete Command subclass that simply executes a sequence of Commands. MacroCommand has no explicit receiver, because the commands it sequences define their own receiver.

![](images/07f2d349233aee00965a7099d3b0bb3a71162ceb6594ff98e7ffa57cd696a754.jpg)  
In each of these examples, notice how the Command pattern decouples the object that invokes the operation from the one having the knowledge to perform it. This gives us a lot of flexibility in designing our user interface. An application can provide both a menu and a push button interface to a feature just by making the menu and the push button share an instance of the same concrete Command subclass. We can replace commands dynamically, which would be useful for implementing context-sensitive menus. We can also support command scripting by composing commands into larger ones. All of this is possible because the object that issues a request only needs to know how to issue it; it