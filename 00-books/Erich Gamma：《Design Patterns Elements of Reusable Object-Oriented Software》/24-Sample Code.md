this:

make: partName   
^(partCatalogat: partName)new

3 . Defining extensible factories. AbstractFactory usually defines a different operation for each kind of product it can produce. The kinds of products are encoded in the operation signatures. Adding a new kind of product requires changing the AbstractFactory interface and all the classes that depend on it.

A more flexible but less safe design is to add a parameter to operations that create objects. This parameter specifies the kind of object to be created. It could be a class identifier, an integer, a string, or anything else that identifies the kind of product. In fact with this approach, AbstractFactory only needs a single “Make” operation with a parameter indicating the kind of object to create. This is the technique used in the Prototype- and the class-based abstract factories discussed earlier.

This variation is easier to use in a dynamically typed language like Smalltalk than in a statically typed language like C++. You can use it in C++ only when all objects have the same abstract base class or when the product objects can be safely coerced to the correct type by the client that requested them. The implementation section of Factory Method (107) shows how to implement such parameterized operations in C++.

But even when no coercion is needed, an inherent problem remains: All products are returned to the client with the same abstract interface as given by the return type. The client will not be able to differentiate or make safe assumptions about the class of a product. If clients need to perform subclass-specific operations, they won’t be accessible through the abstract interface. Although the client could perform a downcast (e.g., with dynamic\_cast in C++), that’s not always feasible or safe, because the downcast can fail. This is the classic trade-off for a highly flexible and extensible interface.

## Sample Code

We’ll apply the Abstract Factory pattern to creating the mazes we discussed at the beginning of this chapter.

Class MazeFactory can create components of mazes. It builds rooms, walls, and doors between rooms. It might be used by a program that reads plans for mazes from a file and builds the corresponding maze. Or it might be used by a program that builds mazes randomly. Programs that build mazes take a MazeFactory as an argument so that the programmer can specify the classes of rooms, walls, and doors to construct.

class MazeFactory {   
public:   
MazeFactory();   
virtual Maze\* MakeMaze() const   
{ return new Maze; }   
virtual Wall\* MakeWall() const   
{ return new Wall; }   
virtual Room\* MakeRoom(int n)const   
{ return new Room(n);}   
virtual Door\* MakeDoor(Room\* rl, Room\* r2) const   
{ return new Door(r1, r2);}   
);

Recall that the member function CreateMaze (page 84) builds a small maze consisting of two rooms with a door between them. CreateMaze hard-codes the class names, making it difficult to create mazes with different components.

Here’s a version of CreateMaze that remedies that shortcoming by taking a MazeFactory as a parameter:

Maze\* MazeGame::CreateMaze (MazeFactory& factory){   
Maze\* aMaze = factory.MakeMaze();   
Room\* r1 = factory.MakeRoom(1);   
Room\* r2 = factory.MakeRoom(2);   
Door\* aDoor = factory.MakeDoor(rl, r2);   
aMaze->AddRoom(r1);   
aMaze->AddRoom(r2);   
r1->SetSide(North,factory.MakeWall());   
r1->SetSide(East, aDoor);   
r1->SetSide(South, factory.MakeWall());   
r1->SetSide(West,factory.MakeWall());   
r2->SetSide(North,factory.Makewall());   
r2->SetSide(East,factory.MakeWall());   
r2->SetSide(South,factory.MakeWall());   
r2->SetSide(West,aDoor);   
return aMaze;

We can create EnchantedMazeFactory, a factory for enchanted mazes, by subclassing MazeFactory. EnchantedMazeFactory will override different member functions and return different subclasses of Room, Wall, etc.

class EnchantedMazeFactory : public MazeFactory {   
public:   
EnchantedMazeFactory();   
virtual Room\* MakeRoom(int n) const   
( return new EnchantedRoom(n, CastSpell()); }   
virtual Door\* MakeDoor(Room\*r1, Room\* r2) const   
{ return new DoorNeedingSpell(r1, r2);}   
protected:   
Spell\* CastSpell() const;

Now suppose we want to make a maze game in which a room can have a bomb set in it. If the bomb goes off, it will damage the walls (at least). We can make a subclass of Room keep track of whether the room has a bomb in it and whether the bomb has gone off. We’ll also need a subclass of Wall to keep track of the damage done to the wall. We’ll call these classes RoomWithABomb and BombedWall.

The last class we’ll define is BombedMazeFactory, a subclass of MazeFactory that ensures walls are of class BombedWall and rooms are of class RoomWithABomb. BombedMazeFactory only needs to override two functions:

Wall\*BombedMazeFactory::MakeWall()const {   
returnnew BombedWall;   
Room\*BombedMazeFactory::MakeRoom(int n)const{   
return new RoomWithABomb(n);

To build a simple maze that can contain bombs, we simply call CreateMaze with a BombedMazeFactory.

MazeGamegame;   
BombedMazeFactoryfactory;

game.CreateMaze(factory);

CreateMaze can take an instance of EnchantedMazeFactory just as well to build enchanted mazes.

Notice that the MazeFactory is just a collection of factory methods. This is the most common way to implement the Abstract Factory pattern. Also note that MazeFactory is not an abstract class; thus it acts as both the AbstractFactory and the ConcreteFactory. This is another common implementation for simple applications of the Abstract Factory pattern. Because the MazeFactory is a concrete class consisting entirely of factory methods, it’s easy to make a new MazeFactory by making a subclass and overriding the operations that need to change.

CreateMaze used the SetSide operation on rooms to specify their sides. If it creates rooms with a BombedMazeFactory, then the maze will be made up of RoomWithABomb objects with BombedWall sides. If RoomWithABomb had to access a subclass-specific member of BombedWall, then it would have to cast a reference to its walls from Wall\* to BombedWall\*. This downcasting is safe as long as the argument is in fact a BombedWall, which is guaranteed to be true if walls are built solely with a BombedMazeFactory.

Dynamically typed languages such as Smalltalk don’t require downcasting, of course, but they might produce run-time errors if they encounter a Wall where they expect a subclass of Wall. Using Abstract Factory to build walls helps prevent these run-time errors by ensuring that only certain kinds of walls can be created.

Let’s consider a Smalltalk version of MazeFactory, one with a single make operation that takes the kind of object to make as a parameter. Moreover, the concrete factory stores the classes of the products it creates.

First, we’ll write an equivalent of CreateMaze in Smalltalk:

createMaze: aFactory   
room1 room2 aDoor   
room1 := (aFactory make: #room) number: 1.   
room2:= (aFactory make: #room)number: 2.   
aDoor := (aFactory make: #door) from: room1 to: room2.   
room1 atSide: #north put: (aFactory make: #wall).   
room1 atSide: #east put: aDoor.   
room1 atSide: #south put: (aFactory make: #wall).   
room1 atSide: #west put: (aFactory make: #wall).   
room2 atSide: #north put: (aFactory make: #wall).   
room2 atSide: #east put: (aFactory make: #wall).   
room2 atSide: #south put: (aFactory make: #wall).   
room2 atSide: #west put: aDoor.   
Maze new addRoom: rooml; addRoom: room2; yourself

As we discussed in the Implementation section, MazeFactory needs only a single instance variable partCatalog to provide a dictionary whose key is the class of the component. Also recall how we implemented the make: method:

make: partName   
^(partCatalog at: partName) new

Now we can create a MazeFactory and use it to implement createMaze. We’ll create the factory using a method createMazeFactory of class MazeGame.

createMazeFactory   
(MazeFactory new   
addPart: Wall named: #wall;   
addPart: Room named: #room;   
addPart: Door named: #door;   
yourself)