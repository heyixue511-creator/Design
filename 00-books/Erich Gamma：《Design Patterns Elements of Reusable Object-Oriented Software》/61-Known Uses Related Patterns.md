template <classItem>   
void FilteringListTraverser<Item>::Traverse (){   
boolresult= false;   
for(   
\_iterator.First();   
!\_iterator.IsDone();   
\_iterator.Next()   
if(TestItem(\_iterator.CurrentItem())){   
result =ProcessItem(\_iterator.CurrentItem());   
if (result == false) {   
break;   
1   
}   
return result;

A variant of this class could define Traverse to return if at least one item satisfies the test.<sup>6</sup>

## Known Uses

Iterators are common in object-oriented systems. Most collection class libraries offer iterators in one form or another.

Here’s an example from the Booch components [Boo94], a popular collection class library. It provides both a fixed size (bounded) and dynamically growing (unbounded) implementation of a queue. The queue interface is defined by an abstract Queue class. To support polymorphic iteration over the different queue implementations, the queue iterator is implemented in the terms of the abstract Queue class interface. This variation has the advantage that you don’t need a factory method to ask the queue implementations for their appropriate iterator. However, it requires the interface of the abstract Queue class to be powerful enough to implement the iterator efficiently.

Iterators don’t have to be defined as explicitly in Smalltalk. The standard collection classes (Bag, Set, Dictionary, OrderedCollection, String, etc.) define an internal iterator method do:, which takes a block (i.e., closure) as an argument. Each element in the collection is bound to the local variable in the block; then the block is executed. Smalltalk also includes a set of Stream classes that support an iterator-like interface. ReadStream is essentially an Iterator, and it can act as an external iterator for all the sequential collections. There are no standard external iterators for nonsequential collections such as Set and Dictionary.

Polymorphic iterators and the cleanup Proxy described earlier are provided by the ET++ container classes [WGM88]. The Unidraw graphical editing framework classes

use cursor-based iterators [VL90].

ObjectWindows 2.0 [Bor94] provides a class hierarchy of iterators for containers. You can iterate over different container types in the same way. The ObjectWindow iteration syntax relies on overloading the postincrement operator ++ to advance the iteration.

## Related Patterns

Composite (163): Iterators are often applied to recursive structures such as Composites.

Factory Method (107): Polymorphic iterators rely on factory methods to instantiate the appropriate Iterator subclass.

Memento (283) is often used in conjunction with the Iterator pattern. An iterator can use a memento to capture the state of an iteration. The iterator stores the memento internally.

## Object Behavioral: Mediator

## Intent

Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.

## Motivation

Object-oriented design encourages the distribution of behavior among objects. Such distribution can result in an object structure with many connections between objects; in the worst case, every object ends up knowing about every other.

Though partitioning a system into many objects generally enhances reusability, proliferating interconnections tend to reduce it again. Lots of interconnections make it less likely that an object can work without the support of others—the system acts as though it were monolithic. Moreover, it can be difficult to change the system’s behavior in any significant way, since behavior is distributed among many objects. As a result, you may be forced to define many subclasses to customize the system’s behavior.

As an example, consider the implementation of dialog boxes in a graphical user interface. A dialog box uses a window to present a collection of widgets such as buttons,

menus, and entry fields, as shown here:

![](images/00cf4919094882b45a9d5a4f06100c9f686a2e5e0b42301ae65ce3219d721f37.jpg)

Often there are dependencies between the widgets in the dialog. For example, a button gets disabled when a certain entry field is empty. Selecting an entry in a list of choices called a list box might change the contents of an entry field. Conversely, typing text into the entry field might automatically select one or more corresponding entries in the list box. Once text appears in the entry field, other buttons may become enabled that let the user do something with the text, such as changing or deleting the thing to which it refers.

Different dialog boxes will have different dependencies between widgets. So even though dialogs display the same kinds of widgets, they can’t simply reuse stock widget classes; they have to be customized to reflect dialog-specific dependencies. Customizing them individually by subclassing will be tedious, since many classes are involved.

You can avoid these problems by encapsulating collective behavior in a separate mediator object. A mediator is responsible for controlling and coordinating the interactions of a group of objects. The mediator serves as an intermediary that keeps objects in the group from referring to each other explicitly. The objects only know the mediator, thereby reducing the number of interconnections.

For example, FontDialogDirector can be the mediator between the widgets in a dialog box. A FontDialogDirector object knows the widgets in a dialog and coordinates their interaction. It acts as a hub of communication for widgets:

![](images/8ac306877f106f0b5f79322e2d56a57caf0190aef3fcdf2cc63ba344b1abff62.jpg)

The following interaction diagram illustrates how the objects cooperate to handle a change in a list box’s selection:

![](images/a12223fcda7aa7a9fddec5b9d7c7dbfa8ec936c69e5fe43ff3355b8370981626.jpg)

Here’s the succession of events by which a list box’s selection passes to an entry field:

1. The list box tells its director that it’s changed.

2. The director gets the selection from the list box.

3. The director passes the selection to the entry field.

4. Now that the entry field contains some text, the director enables button(s) for initiating an action (e.g., “demibold,” “oblique”).

Note how the director mediates between the list box and the entry field. Widgets communicate with each other only indirectly, through the director. They don’t have to know about each other; all they know is the director. Furthermore, because the behavior