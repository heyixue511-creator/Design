Unexecute as follows: cute as follows:

void MoveCommand::Execute () {   
ConstraintSolver\* solver = ConstraintSolver::Instance();   
\_state = solver->CreateMemento(); //createa memento   
\_target->Move(\_delta);   
solver->Solve();   
  
void MoveCommand::Unexecute (){   
ConstraintSolver\* solver = ConstraintSolver::Instance();   
\_target->Move(-\_delta);   
solver->SetMemento(\_state);//restore solver state   
solver->Solve();   
}

Execute acquires a ConstraintSolverMemento memento before it moves the graphic. Unexecute moves the graphic back, sets the constraint solver’s state to the previous state, and finally tells the constraint solver to solve the constraints.

## Known Uses

The preceding sample code is based on Unidraw’s support for connectivity through its CSolver class [VL90].

Collections in Dylan [App92] provide an iteration interface that reflects the Memento pattern. Dylan’s collections have the notion of a “state” object, which is a memento that represents the state of the iteration. Each collection can represent the current state of the iteration in any way it chooses; the representation is completely hidden from clients. The Dylan iteration approach might be translated to C++ as follows:

template <class Item>   
class Collection {   
public:   
Collection();   
IterationState\*CreateInitialState();   
void Next(IterationState\*);   
bool IsDone(constIterationState\*) const;   
Item CurrentItem(const IterationState\*) const;   
IterationState\* Copy(const IterationState\*) const;   
void Append(const Item&);   
void Remove(constItem&);

CreatelnitialState returns an initialized IterationState object for the collection. Next advances the state object to the next position in the iteration; it effectively increments the iteration index. IsDone returns true if Next has advanced beyond the last element in the collection. CurrentItem dereferences the state object and returns the element in the collection to which it refers. Copy returns a copy of the given state object. This is useful for marking a point in an iteration.

Given a class ItemType, we can iterate over a collection of its instances as follows<sup>7</sup>:

class ItemType {   
public:   
void Process();   
Collection<ItemType\*>aCollection;   
IterationState\* state;   
state = aCollection.CreateInitialState();   
while(!aCollection.IsDone(state)){   
aCollection.CurrentItem(state)->Process();   
aCollection.Next(state);   
)   
delete state;

The memento-based iteration interface has two interesting benefits:

1. More than one state can work on the same collection. (The same is true of the Iterator (257) pattern.)

2 . It doesn’t require breaking a collection’s encapsulation to support iteration. The memento is only interpreted by the collection itself; no one else has access to it. Other approaches to iteration require breaking encapsulation by making iterator classes friends of their collection classes (see Iterator (257)). The situation is reversed in the memento-based implementation: Collection is a friend of the iteratorState.

The QOCA constraint-solving toolkit stores incremental information in mementos [HHMV92]. Clients can obtain a memento that characterizes the current solution to a system of constraints. The memento contains only those constraint variables that have changed since the last solution. Usually only a small subset of the solver’s variables changes for each new solution. This subset is enough to return the solver to the preceding solution; reverting to earlier solutions requires restoring mementos from the intervening solutions. Hence you can’t set mementos in any order; QOCA relies on a history mechanism to revert to earlier solutions.

## Related Patterns

Command (233): Commands can use mementos to maintain state for undoable

operations.

Iterator (257): Mementos can be used for iteration as described earlier.

## Object Behavioral: Observer

## Intent

Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Also Known As

Dependents, Publish-Subscribe

## Motivation

A common side-effect of partitioning a system into a collection of cooperating classes is the need to maintain consistency between related objects. You don’t want to achieve consistency by making the classes tightly coupled, because that reduces their reusability.

For example, many graphical user interface toolkits separate the presentational aspects of the user interface from the underlying application data [KP88, LVC89, P<sup>+</sup>88, WGM88]. Classes defining application data and presentations can be reused independently. They can work together, too. Both a spreadsheet object and bar chart object can depict information in the same application data object using different presentations. The spreadsheet and the bar chart don’t know about each other, thereby letting you reuse only the one you need. But they behave as though they do. When the user changes the information in the spreadsheet, the bar chart reflects the changes immediately, and vice versa.

![](images/9ef77dc6cf468570b660bb609a892950e73fe96c7ba12cf5d535819e28945df1.jpg)

This behavior implies that the spreadsheet and bar chart are dependent on the data object and therefore should be notified of any change in its state. And there’s no reason to limit the number of dependent objects to two; there may be any number of different user interfaces to the same data.

The Observer pattern describes how to establish these relationships. The key objects in this pattern are subject and observer. A subject may have any number of dependent observers. All observers are notified whenever the subject undergoes a change in state. In response, each observer will query the subject to synchronize its state with the subject’s state.

This kind of interaction is also known as publish-subscribe. The subject is the publisher of notifications. It sends out these notifications without having to know who its observers are. Any number of observers can subscribe to receive notifications.

## Applicability

Use the Observer pattern in any of the following situations:

• When an abstraction has two aspects, one dependent on the other. Encapsulating these aspects in separate objects lets you vary and reuse them independently.

• When a change to one object requires changing others, and you don’t know how many objects need to be changed.

• When an object should be able to notify other objects without making assumptions about who these objects are. In other words, you don’t want these objects tightly coupled.

## Structure