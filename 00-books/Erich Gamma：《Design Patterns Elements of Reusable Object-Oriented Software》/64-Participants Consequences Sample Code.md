## Participants

• Memento (SolverState)

– stores internal state of the Originator object. The memento may store as much or as little of the originator’s internal state as necessary at its originator’s discretion.

– protects against access by objects other than the originator. Mementos have effectively two interfaces. Caretaker sees a narrow interface to the Memento—it can only pass the memento to other objects. Originator, in contrast, sees a wide interface, one that lets it access all the data necessary to restore itself to its previous state. Ideally, only the originator that produced the memento would be permitted to access the memento’s internal state.

• Originator (ConstraintSolver)

– creates a memento containing a snapshot of its current internal state.

– uses the memento to restore its internal state.

• Caretaker (undo mechanism)

– is responsible for the memento’s safekeeping.

– never operates on or examines the contents of a memento.

## Collaborations

• A caretaker requests a memento from an originator, holds it for a time, and passes it back to the originator, as the following interaction diagram illustrates:

![](images/8fa8e0e9b433c4783e0536c434282a77e42379fe34fb1cebfef91a0967197f2d.jpg)

Sometimes the caretaker won’t pass the memento back to the originator, because the originator might never need to revert to an earlier state.

• Mementos are passive. Only the originator that created a memento will assign or retrieve its state.

## Consequences

The Memento pattern has several consequences:

1. Preserving encapsulation boundaries. Memento avoids exposing information that only an originator should manage but that must be stored nevertheless outside the originator. The pattern shields other objects from potentially complex Originator internals, thereby preserving encapsulation boundaries.

2. It simplifies Originator. In other encapsulation-preserving designs, Originator keeps the versions of internal state that clients have requested. That puts all the storage management burden on Originator. Having clients manage the state they ask for simplifies Originator and keeps clients from having to notify originators when they’re done.

3 . Using mementos might be expensive. Mementos might incur considerable overhead if Originator must copy large amounts of information to store in the memento or if clients create and return mementos to the originator often enough. Unless encapsulating and restoring Originator state is cheap, the pattern might not be appropriate. See the discussion of incrementality in the Implementation section.

4. Defining narrow and wide interfaces. It may be difficult in some languages to ensure that only the originator can access the memento’s state.

5. Hidden costs in caring for mementos. A caretaker is responsible for deleting the mementos it cares for. However, the caretaker has no idea how much state is in the memento. Hence an otherwise lightweight caretaker might incur large storage costs when it stores mementos.

## Implementation

Here are two issues to consider when implementing the Memento pattern:

1. Language support. Mementos have two interfaces: a wide one for originators and a narrow one for other objects. Ideally the implementation language will support two levels of static protection. C++ lets you do this by making the Originator a friend of Memento and making Memento’s wide interface private. Only the narrow interface should be declared public. For example:

class State;   
class Originator {   
public:   
Memento\*CreateMemento();   
void SetMemento(const Memento\*);   
private:   
State\*\_state; // internal data structures   
class Memento {   
public:   
// narrow public interface   
virtual"Memento();   
private:   
// private members accessible onlyto Originator   
friend class Originator;   
Memento();   
void SetState(State\*);   
State\*GetState();   
private:   
State\* \_state;

2. Storing incremental changes. When mementos get created and passed back to their originator in a predictable sequence, then Memento can save just the incremental change to the originator’s internal state.

For example, undoable commands in a history list can use mementos to ensure that commands are restored to their exact state when they’re undone (see Command (233)). The history list defines a specific order in which commands can be undone and redone. That means mementos can store just the incremental change that a command makes rather than the full state of every object they affect. In the Motivation example given earlier, the constraint solver can store only those internal structures that change to keep the line connecting the rectangles, as opposed to storing the absolute positions of these objects.

## Sample Code

The C++ code given here illustrates the ConstraintSolver example discussed earlier. We use MoveCommand objects (see Command (233)) to (un)do the translation of a graphical object from one position to another. The graphical editor calls the command’s Execute operation to move a graphical object and Unexecute to undo the move. The command stores its target, the distance moved, and an instance of

ConstraintSolverMemento, a memento containing state from the constraint solver.

class Graphic;   
// base class for graphicalobjects in the graphical editor   
class MoveCommand{   
public:   
MoveCommand(Graphic\* target, const Point& delta);   
void Execute();   
void Unexecute();   
private:   
ConstraintSclverMemento\*\_state;   
Point \_delta;   
Graphic\* \_target;

The connection constraints are established by the class ConstraintSolver. Its key member function is Solve, which solves the constraints registered with the AddConstraint operation. To support undo, ConstraintSolver’s state can be externalized with CreateMemento into a ConstraintSolverMemento instance. The constraint solver can be returned to a previous state by calling SetMemento. ConstraintSolver is a Singleton (127).

```javascript
class ConstraintSolver {
public:
static ConstraintSolver* Instance();
void Solve();
voidAddConstraint(
Graphic*startConnection, Graphic*endConnection
) ;
void RemoveConstraint(
Graphic*startConnection, Graphic*endConnection
ConstraintSolverMemento*CreateMemento();
void SetMemento(ConstraintSolverMemento*);
private:
//nontrivial state and operationsfor enforcing
//connectivity semantics
);
class ConstraintSolverMemento{
public:
virtual~ConstraintSolverMemento();
private:
friend class ConstraintSolver;
ConstraintSolverMemento();
//private constraint solver state
ven these interfaces, we can implement MoveCommand memb
```