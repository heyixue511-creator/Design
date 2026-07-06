## Known Uses

Both ET++ [WGM88] and the THINK C class library [Sym93b] use director-like objects in dialogs as mediators between widgets.

The application architecture of Smalltalk/V for Windows is based on a mediator structure [LaL94]. In that environment, an application consists of a Window containing a set of panes. The library contains several predefined Pane objects; examples include TextPane, ListBox, Button, and so on. These panes can be used without subclassing. An application developer only subclasses from ViewManager, a class that’s responsible for doing inter-pane coordination. ViewManager is the Mediator, and each pane only knows its view manager, which is considered the “owner” of the pane. Panes don’t refer to each other directly.

The following object diagram shows a snapshot of an application at run-time:

![](images/e6285f617f1d81fe14c20122791c926eab66c79a2baae520cb700b04a900dfbe.jpg)

Smalltalk/V uses an event mechanism for Pane-ViewManager communication. A pane generates an event when it wants to get information from the mediator or when it wants to inform the mediator that something significant happened. An event defines a symbol (e.g., #select) that identifies the event. To handle the event, the view manager registers a method selector with the pane. This selector is the event’s handler; it will be invoked whenever the event occurs.

The following code excerpt shows how a ListPane object gets created inside a ViewManager subclass and how ViewManager registers an event handler for the #select event:

selfaddSubpane: (ListPane new   
paneName:'myListPane';   
owner: self;   
when:#select perform: #listSelect:).

Another application of the Mediator pattern is in coordinating complex updates. An example is the ChangeManager class mentioned in Observer (293). Change-Manager mediates between subjects and observers to avoid redundant updates. When an object changes, it notifies the ChangeManager, which in turn coordinates the update by notifying the object’s dependents.

A similar application appears in the Unidraw drawing framework [VL90] and uses a class called CSolver to enforce connectivity constraints between “connectors.” Objects in graphical editors can appear to stick to one another in different ways. Connectors are useful in applications that maintain connectivity automatically, like diagram editors and circuit design systems. CSolver is a mediator between connectors. It solves the connectivity constraints and updates the connectors’ positions to reflect them.

## Related Patterns

Facade (185) differs from Mediator in that it abstracts a subsystem of objects to provide a more convenient interface. Its protocol is unidirectional; that is, Facade objects make requests of the subsystem classes but not vice versa. In contrast, Mediator enables cooperative behavior that colleague objects don’t or can’t provide, and the protocol is multidirectional.

Colleagues can communicate with the mediator using the Observer (293) pattern.

## Object Behavioral: Memento

## Intent

Without violating encapsulation, capture and externalize an object’s internal state so that the object can be restored to this state later.

## Also Known As

Token

## Motivation

Sometimes it’s necessary to record the internal state of an object. This is required when implementing checkpoints and undo mechanisms that let users back out of tentative operations or recover from errors. You must save state information somewhere so that you can restore objects to their previous states. But objects normally encapsulate some or all of their state, making it inaccessible to other objects and impossible to save externally. Exposing this state would violate encapsulation, which can compromise the application’s reliability and extensibility.

Consider for example a graphical editor that supports connectivity between objects. A user can connect two rectangles with a line, and the rectangles stay connected when the user moves either of them. The editor ensures that the line stretches to maintain the connection.

![](images/f4ff2dfd0df8aa71b7809d6c823e435b5ee1fa785305deec9d4aab75de0c2141.jpg)

A well-known way to maintain connectivity relationships between objects is with a constraint-solving system. We can encapsulate this functionality in a ConstraintSolver object. ConstraintSolver records connections as they are made and generates mathematical equations that describe them. It solves these equations whenever the user makes a connection or otherwise modifies the diagram. Constraint-Solver uses the results of its calculations to rearrange the graphics so that they maintain the proper connections.

Supporting undo in this application isn’t as easy as it may seem. An obvious way to undo a move operation is to store the original distance moved and move the object back an equivalent distance. However, this does not guarantee all objects will appear where they did before. Suppose there is some slack in the connection. In that case, simply moving the rectangle back to its original location won’t necessarily achieve the desired effect.

![](images/63218606012ac776b6e0803bbf35cec0c97801a604a6c6cdd279aa47accfa894.jpg)

In general, the ConstraintSolver’s public interface might be insufficient to allow precise reversal of its effects on other objects. The undo mechanism must work more closely with ConstraintSolver to reestablish previous state, but we should also avoid exposing the ConstraintSolver’s internals to the undo mechanism.

We can solve this problem with the Memento pattern. A memento is an object that stores a snapshot of the internal state of another object—the memento’s originator. The undo mechanism will request a memento from the originator when it needs to checkpoint the originator’s state. The originator initializes the memento with information that characterizes its current state. Only the originator can store and retrieve information from the memento—the memento is “opaque” to other objects.

In the graphical editor example just discussed, the ConstraintSolver can act as an originator. The following sequence of events characterizes the undo process:

1. The editor requests a memento from the ConstraintSolver as a side-effect of the move operation.

2 . The ConstraintSolver creates and returns a memento, an instance of a class SolverState in this case. A SolverState memento contains data structures that describe the current state of the ConstraintSolver’s internal equations and variables.

3 . Later when the user undoes the move operation, the editor gives the SolverState back to the ConstraintSolver.

4. Based on the information in the SolverState, the ConstraintSolver changes its internal structures to return its equations and variables to their exact previous state.

This arrangement lets the ConstraintSolver entrust other objects with the information it needs to revert to a previous state without exposing its internal structure and representations.

## Applicability

Use the Memento pattern when

• a snapshot of (some portion of) an object’s state must be saved so that it can be restored to that state later, and

• a direct interface to obtaining the state would expose implementation details and break the object’s encapsulation.

## Structure

![](images/b3a79f6a1af0ad8e05953a244123eb3e2ae5e9d44f846a91a7364dba0b7f23dd.jpg)