is localized in one class, it can be changed or replaced by extending or replacing that class.

Here’s how the FontDialogDirector abstraction can be integrated into a class library:

![](images/f0856d7cadcbbd96944a1565d6bfb72802059d017013afe051f9323e520a1437.jpg)

DialogDirector is an abstract class that defines the overall behavior of a dialog. Clients call the ShowDialog operation to display the dialog on the screen. CreateWidgets is an abstract operation for creating the widgets of a dialog. WidgetChanged is another abstract operation; widgets call it to inform their director that they have changed. DialogDirector subclasses override CreateWidgets to create the proper widgets, and they override WidgetChanged to handle the changes.

## Applicability

Use the Mediator pattern when

• a set of objects communicate in well-defined but complex ways. The resulting interdependencies are unstructured and difficult to understand.

• reusing an object is difficult because it refers to and communicates with many other objects.

• a behavior that’s distributed between several classes should be customizable without a lot of subclassing.

## Structure

![](images/e3384d6df8828de702e5ffb687d0ef718d1ad3e6803fe30da98f7c2e7f307a5f.jpg)  
A typical object structure might look like this:

![](images/9cbd204f6ecbec78629a8ce606b74899ad7a0b31585d31fd2168e3481397c623.jpg)

## Participants

• Mediator (DialogDirector)

– defines an interface for communicating with Colleague objects.

• ConcreteMediator (FontDialogDirector)

– implements cooperative behavior by coordinating Colleague objects.

– knows and maintains its colleagues.

• Colleague classes (ListBox, EntryField)

– each Colleague class knows its Mediator object.

– each colleague communicates with its mediator whenever it would have otherwise communicated with another colleague.

## Collaborations

• Colleagues send and receive requests from a Mediator object. The mediator implements the cooperative behavior by routing requests between the appropriate colleague(s).

## Consequences

The Mediator pattern has the following benefits and drawbacks:

1. It limits subclassing. A mediator localizes behavior that otherwise would be distributed among several objects. Changing this behavior requires subclassing Mediator only; Colleague classes can be reused as is.

2 . It decouples colleagues. A mediator promotes loose coupling between colleagues. You can vary and reuse Colleague and Mediator classes independently.

3. It simplifies object protocols. A mediator replaces many-to-many interactions with one-to-many interactions between the mediator and its colleagues. One-to-many relationships are easier to understand, maintain, and extend.

4. It abstracts how objects cooperate. Making mediation an independent concept and encapsulating it in an object lets you focus on how objects interact apart from their individual behavior. That can help clarify how objects interact in a system.

5 . It centralizes control. The Mediator pattern trades complexity of interaction for complexity in the mediator. Because a mediator encapsulates protocols, it can become more complex than any individual colleague. This can make the mediator itself a monolith that’s hard to maintain.

## Implementation

The following implementation issues are relevant to the Mediator pattern:

1. Omitting the abstract Mediator class. There’s no need to define an abstract Mediator class when colleagues work with only one mediator. The abstract coupling that the Mediator class provides lets colleagues work with different Mediator subclasses, and vice versa.

2 . Colleague-Mediator communication. Colleagues have to communicate with their mediator when an event of interest occurs. One approach is to implement the Mediator as an Observer using the Observer (293) pattern. Colleague classes act as Subjects, sending notifications to the mediator whenever they change state. The mediator responds by propagating the effects of the change to other colleagues.

Another approach defines a specialized notification interface in Mediator that lets colleagues be more direct in their communication. Smalltalk/V for Windows uses a form of delegation: When communicating with the mediator, a colleague passes itself as an argument, allowing the mediator to identify the sender. The Sample Code uses this approach, and the Smalltalk/V implementation is discussed further in the Known Uses.

## Sample Code

We’ll use a DialogDirector to implement the font dialog box shown in the Motivation. The abstract class DialogDirector defines the interface for directors.

class DialogDirector {   
public:   
virtual \~DialogDirector();   
virtual void ShowDialog();   
virtual void WidgetChanged(Widget\*) =0;   
protected:   
DialogDirector();   
virtual void CreateWidgets() =0;   
};

Widget is the abstract base class for widgets. A widget knows its director.

class Widget {   
public:   
Widget(DialogDirector\*);   
virtual voidChanged();   
virtual void HandleMouse(MouseEvent& event);   
private:   
DialogDirector\*\_director;

Changed calls the director’s WidgetChanged operation. Widgets call WidgetChanged on their director to inform it of a significant event.

void Widget::Changed () {   
\_director->WidgetChanged(this);

Subclasses of DialogDirector override WidgetChanged to affect the appropriate widgets. The widget passes a reference to itself as an argument to WidgetChanged to let the director identify the widget that changed. DialogDirector subclasses redefine the CreateWidgets pure virtual to construct the widgets in the dialog.

The ListBox, EntryField, and Button are subclasses of Widget for specialized user interface elements. ListBox provides a GetSelection operation to get the current selection, and EntryField’s SetText operation puts new text into the field.

class ListBox : public Widget {   
public:   
ListBox(DialogDirector\*);   
virtual const char\* GetSelection();   
virtual void SetList(List<char\*>\*listItems);   
virtual void HandleMouse(MouseEvent& event);   
class EntryField : public Widget{   
public:   
EntryField(DialogDirector\*);   
virtual void SetText(const char\*text);   
virtual const char\* GetText();   
virtual void HandleMouse(MouseEvent&event);

Button is a simple widget that calls Changed whenever it’s pressed. This gets done in its implementation of HandleMouse:

class Button : public Widget {   
public:   
Button(DialogDirector\*);   
virtualvoid SetText(const char\* text);   
virtualvoid HandleMouse(MouseEvent& event);   
void Button::HandleMouse(MouseEvent& event){   
Changed();

T h e FontDialogDirector class mediates between widgets in the dialog box. FontDialogDirector is a subclass of DialogDirector:

class FontDialogDirector : public DialogDirector {   
public:   
FontDialogDirector();   
virtual "FontDialogDirector();   
virtual void WidgetChanged(Widget\*);   
protected:   
virtual void CreateWidgets();   
private:   
Button\*\_ok;   
Button\* \_cancel;   
ListBox\* \_fontList;   
EntryField\*\_fontName;   
};

FontDialogDirector keeps track of the widgets it displays. It redefines CreateWidgets to create the widgets and initialize its references to them:

void FontDialogDirector::CreateWidgets () {   
\_ok = new Button(this);   
\_cancel = new Button(this);   
\_fontList = new ListBox(this);   
\_fontName = new EntryField(this);   
// fill the listBox with the available font names   
// assemble the widgetsin the dialog   
}   
WidgetChanged ensures that the widgets work together properly:   
void FontDialogDirector::WidgetChanged (   
Widget\* theChangedWidget   
if(theChangedWidget == \_fontList) {   
\_fontName->SetText(\_fontList->GetSelection());   
} else if (theChangedWidget == \_ok) {   
//apply font change and dismiss dialog   
} else if (theChangedWidget == \_cancel) {   
//dismissdialog

The complexity of WidgetChanged increases proportionally with the complexity of the dialog. Large dialogs are undesirable for other reasons, of course, but mediator complexity might mitigate the pattern’s benefits in other applications.