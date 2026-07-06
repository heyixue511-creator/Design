3. Initializing clones. While some clients are perfectly happy with the clone as is, others will want to initialize some or all of its internal state to values of their choosing. You generally can’t pass these values in the Clone operation, because their number will vary between classes of prototypes. Some prototypes might need multiple initialization parameters; others won’t need any. Passing parameters in the Clone operation precludes a uniform cloning interface.

It might be the case that your prototype classes already define operations for (re)setting key pieces of state. If so, clients may use these operations immediately after cloning. If not, then you may have to introduce an Initialize operation (see the Sample Code section) that takes initialization parameters as arguments and sets the clone’s internal state accordingly. Beware of deep-copying Clone operations—the copies may have to be deleted (either explicitly or within Initialize) before you reinitialize them.

## Sample Code

We’ll define a MazePrototypeFactory subclass of the MazeFactory class (page 92). MazePrototypeFactory will be initialized with prototypes of the objects it will create so that we don’t have to subclass it just to change the classes of walls or rooms it creates.

MazePrototypeFactory augments the MazeFactory interface with a constructor that takes the prototypes as arguments:

class MazePrototypeFactory: public MazeFactory {   
public:   
MazePrototypeFactory(Maze\*, Wall\*, Room\*, Door\*);   
virtual Maze\* MakeMaze()const;   
virtual Room\* MakeRoom(int) const;   
virtual Wall\* MakeWall() const;   
virtual Door\* MakeDoor(Room\*, Room\*) const;   
private:   
Maze\* \_prototypeMaze;   
Room\* \_prototypeRoom;   
Wall\* \_prototypeWall;   
Door\* prototypeDoor;

The new constructor simply initializes its prototypes:

MazePrototypeFactory::MazePrototypeFactory(   
Maze\* m, Wall\* w, Room\* r, Door\* d   
\_prototypeMaze = m;   
\_prototypeWall = w;   
\_prototypeRoom = r;   
\_prototypeDoor = d;

The member functions for creating walls, rooms, and doors are similar: Each clones a prototype and then initializes it. Here are the definitions of MakeWall and MakeDoor:

Wall\* MazePrototypeFactory::MakeWall() const {   
return \_prototypeWall->Clone();   
Door\* MazePrototypeFactory::MakeDoor (Room\* r1, Room \*r2) const {   
Door\* door = \_prototypeDoor->Clone();   
door->Initialize(rl, r2);   
return door;

We can use MazePrototypeFactory to create a prototypical or default maze just by initializing it with prototypes of basic maze components:

MazeGame game;   
MazePrototypeFactory simpleMazeFactory(   
new Maze, new Wall, new Room, new Door   
Maze\* maze = game.CreateMaze(simpleMazeFactory);

To change the type of maze, we initialize MazePrototypeFactory with a different set of prototypes. The following call creates a maze with a BombedDoor and a RoomWithABomb:

MazePrototypeFactory bombedMazeFactory   
new Maze, new Bombedwall,   
new RoomWithABomb, new Door   
);

An object that can be used as a prototype, such as an instance of Wall, must support the Clone operation. It must also have a copy constructor for cloning. It may also need a separate operation for reinitializing internal state. We’ll add the Initialize operation to Door to let clients initialize the clone’s rooms.

Compare the following definition of Door to the one on page 83:

class Door : public MapSite {   
public:   
Door();   
Door(const Door&);   
virtual void Initialize(Room\*, Room\*);   
virtual Door\* Clone() const;   
virtualvoid Enter();   
Room\*OtherSideFrom(Room\*);   
private:   
Room\* \_rooml;   
Room\* \_room2;   
Door::Door (const Door& other) (   
\_rooml= other.\_rooml;   
\_room2=other.\_room2;   
void Door::Initialize (Room\*r1, Room\* r2) {   
\_room1 = r1;   
\_room2 = r2;   
Door\* Door::Clone () const {   
return new Door(\*this);

The BombedWall subclass must override Clone and implement a corresponding copy constructor.

class Bombedwall : public Wall (   
public:   
BombedWall();   
BombedWall(const BombedWall&);   
virtual Wall\* Clone() const;   
bool HasBomb();   
private:   
bool \_bomb;   
BombedWall::BombedWall (const BombedWall& other): Wall(other){   
\_bomb = other. \_bomb;   
Wall\* BombedWall::Clone () const {   
return new BombedWall(\*this);

Although BombedWall::Clone returns a Wall\*, its implementation returns a pointer to a new instance of a subclass, that is, a BombedWall\*. We define Clone like this in the base class to ensure that clients that clone the prototype don’t have to know about their concrete subclasses. Clients should never need to downcast the return value of Clone to the desired type.

In Smalltalk, you can reuse the standard copy method inherited from Object to clone any MapSite. You can use MazeFactory to produce the prototypes you’ll need; for example, you can create a room by supplying the name #room. The MazeFactory has a dictionary that maps names to prototypes. Its make: method looks like this:

make: partName   
(partCatalog at: partName) copy

Given appropriate methods for initializing the MazeFactory with prototypes, you could create a simple maze with the following code:

CreateMaze   
on: (MazeFactory new   
with: Door new named: #door;   
with: Wall new named: #wall;   
with: Room new named: #room;   
yourself)

where the definition of the on: class method for CreateMaze would be

on: aFactory   
room1 room2 I   
rooml := (aFactory make: #rcom) location: 1@1.   
room2:=(aFactory make: #room) location: 2@1.   
door := (aFactory make: #door) from: room1 to: room2.   
room1   
atSide: #north put: (aFactory make: #wall);   
atSide: #east put: door;   
atSide: #south put: (aFactory make: #wall);   
atSide: #west put: (aFactory make: #wall).   
room2   
atSide: #north put: (aFactory make: #wall);   
atSide: #east put: (aFactory make: #wall);   
atSide: #south put: (aFactory make: #wall);   
atSide: #west put: door.   
Maze new   
addRoom: room1;   
addRoom: room2;   
yourself

## Known Uses

Perhaps the first example of the Prototype pattern was in Ivan Sutherland’s Sketchpad system [Sut63]. The first widely known application of the pattern in an object-oriented language was in ThingLab, where users could form a composite object and then promote it to a prototype by installing it in a library of reusable objects [Bor81]. Goldberg and Robson mention prototypes as a pattern [GR83], but Coplien [Cop92] gives a much more complete description. He describes idioms related to the Prototype pattern for C++ and gives many examples and variations.

Etgdb is a debugger front-end based on ET++ that provides a point-and-click