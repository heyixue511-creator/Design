or otherwise changing the chain at run-time. You can combine this with subclassing to specialize handlers statically.

3. Receipt isn’t guaranteed. Since a request has no explicit receiver, there’s no guarantee it’ll be handled—the request can fall off the end of the chain without ever being handled. A request can also go unhandled when the chain is not configured properly.

## Implementation

Here are implementation issues to consider in Chain of Responsibility:

1. Implementing the successor chain. There are two possible ways to implement the successor chain:

(a) Define new links (usually in the Handler, but ConcreteHandlers could define them instead).

(b) Use existing links.

Our examples so far define new links, but often you can use existing object references to form the successor chain. For example, parent references in a partwhole hierarchy can define a part’s successor. A widget structure might already have such links. Composite (163) discusses parent references in more detail.

Using existing links works well when the links support the chain you need. It saves you from defining links explicitly, and it saves space. But if the structure doesn’t reflect the chain of responsibility your application requires, then you’ll have to define redundant links.

2. Connecting successors. If there are no preexisting references for defining a chain, then you’ll have to introduce them yourself. In that case, the Handler not only defines the interface for the requests but usually maintains the successor as well. That lets the handler provide a default implementation of HandleRequest that forwards the request to the successor (if any). If a ConcreteHandler subclass isn’t interested in the request, it doesn’t have to override the forwarding operation, since its default implementation forwards unconditionally.

Here’s a HelpHandler base class that maintains a successor link:

class HelpHandler {   
public:   
HelpHandler(HelpHandler\*s): \_successor(s){ }   
virtual void HandleHelp();   
private:   
HelpHandler\*\_successor;   
);   
void HelpHandler::HandleHelp () {   
if(\_successor) {   
\_successor->HandleHelp();   
  
一

3 . Representing requests. Different options are available for representing requests. In the simplest form, the request is a hard-coded operation invocation, as in the case of HandleHelp. This is convenient and safe, but you can forward only the fixed set of requests that the Handler class defines.

An alternative is to use a single handler function that takes a request code (e.g., an integer constant or a string) as parameter. This supports an open-ended set of requests. The only requirement is that the sender and receiver agree on how the request should be encoded.

This approach is more flexible, but it requires conditional statements for dispatching the request based on its code. Moreover, there’s no type-safe way to pass parameters, so they must be packed and unpacked manually. Obviously this is less safe than invoking an operation directly.

To address the parameter-passing problem, we can use separate request objects that bundle request parameters. A Request class can represent requests explicitly, and new kinds of requests can be defined by subclassing. Subclasses can define different parameters. Handlers must know the kind of request (that is, which Request subclass they’re using) to access these parameters.

To identify the request, Request can define an accessor function that returns an identifier for the class. Alternatively, the receiver can use run-time type information if the implementation languages supports it.

Here is a sketch of a dispatch function that uses request objects to identify requests. A GetKind operation defined in the base Request class identifies the kind of request:

void Handler::HandleRequest (Request\*theRequest) {   
switch (theRequest->GetKind()){   
case Help:   
// cast argument to appropriate type   
HandleHelp((HelpRequest\*) theRequest);   
break;   
case Print:   
HandlePrint((PrintRequest\*)theRequest);   
break;   
default:   
break;

Subclasses can extend the dispatch by overriding HandleRequest. The subclass handles only the requests in which it’s interested; other requests are forwarded to the parent class. In this way, subclasses effectively extend (rather than override) the HandleRequest operation. For example, here’s how an ExtendedHandler subclass extends Handler’s version of HandleRequest:

class ExtendedHandler : public Handler {   
public:   
virtual void HandleRequest(Request\* theRequest);   
void ExtendedHandler::HandleRequest (Request\* theRequest) {   
switch(theRequest->GetKind()) {   
case Preview:   
// handle the Preview request   
break;   
default:   
// let Handler handle other requests   
Handler::HandleRequest(theRequest);

4 . Automatic forwarding in Smalltalk. You can use the doesNotUnderstand mechanism in Smalltalk to forward requests. Messages that have no corresponding methods are trapped in the implementation of doesNotUnderstand, which can be overridden to forward the message to an object’s successor. Thus it isn’t necessary to implement forwarding manually; the class handles only the request in which it’s interested, and it relies on doesNotUnderstand to forward all others.

## Sample Code

The following example illustrates how a chain of responsibility can handle requests for an on-line help system like the one described earlier. The help request is an explicit operation. We’ll use existing parent references in the widget hierarchy to propagate requests between widgets in the chain, and we’ll define a reference in the Handler class to propagate help requests between nonwidgets in the chain.

The HelpHandler class defines the interface for handling help requests. It maintains a help topic (which is empty by default) and keeps a reference to its successor on the chain of help handlers. The key operation is HandleHelp, which subclasses override. HasHelp is a convenience operation for checking whether there is an associated help topic.

typedef int Topic;   
const Topic NO HELP TOPIC = -1;   
class HelpHandler {   
public:   
HelpHandler(HelpHandler\* = 0, Topic = NO\_HELP\_TOPIC);   
virtual bool HasHelp();   
virtual void SetHandler(HelpHandler\*, Topic);   
virtual void HandleHelp();   
private:   
HelpHandler\* \_successor;   
Topic \_topic;   
};   
HelpHandler::HelpHandler(   
HelpHandler\* h, Topic t   
) : \_successor(h), \_topic(t)( }   
bool HelpHandler::HasHelp(){   
return \_topic!= NO\_HELP\_TOPIC;   
void HelpHandler::HandleHelp() (   
if (\_successor != 0) {   
\_successor->HandleHelp();   
  
}

All widgets are subclasses of the Widget abstract class. Widget is a subclass of HelpHandler, since all user interface elements can have help associated with them. (We could have used a mixin-based implementation just as well.)

class Widget : public HelpHandler {   
protected:   
Widget(Widget\*parent. Topic t = NO\_HELP\_TOPIC);   
private:   
Widget\* \_parent;   
};   
Widget::Widget (Widget\* w, Topic t) : HelpHandler(w, t) {   
parent = w;   
}

In our example, a button is the first handler on the chain. The Button class is a subclass of Widget. The Button constructor takes two parameters: a reference to its enclosing widget and the help topic.

class Button : public Widget {   
public:   
Button(Widget\* d, Topic t = NO\_HELP\_TOPIC);   
virtual void HandleHelp();   
//Widgetoperationsthat Button overrides...   
);

Button’s version of HandleHelp first tests to see if there is a help topic for buttons. If the developer hasn’t defined one, then the request gets forwarded to the successor using the HandleHelp operation in HelpHandler. If there is a help topic, then the button displays it, and the search ends.

Button::Button (Widget\* h, Topic t) : Widget(h, t) ( }   
void Button::HandleHelp () {   
if (HasHelp()) {   
// offer help on the button   
} else {   
HelpHandler::HandleHelp();

Dialog implements a similar scheme, except that its successor is not a widget but any help handler. In our application this successor will be an instance of Application.

class Dialog : public Widget {   
public:   
Dialog(HelpHandler\* h, Topic t= NO\_HELP\_TOPIC);   
virtual void HandleHelp();   
//Widget operations that Dialog overrides...   
Dialog::Dialog (HelpHandler\* h, Topic t) : Widget(0) {   
SetHandler(h, t);   
void Dialog::HandleHelp () {   
if (HasHelp()) {   
// offer help on the dialog   
} else {   
HelpHandler::HandleHelp();

At the end of the chain is an instance of Application. The application is not a widget, s o Application is subclassed directly from HelpHandler. When a help request