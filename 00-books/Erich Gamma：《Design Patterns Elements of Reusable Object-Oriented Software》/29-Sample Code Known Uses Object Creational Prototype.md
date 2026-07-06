## Sample Code

The function CreateMaze (page 84) builds and returns a maze. One problem with this function is that it hard-codes the classes of maze, rooms, doors, and walls. We’ll introduce factory methods to let subclasses choose these components.

First we’ll define factory methods in MazeGame for creating the maze, room, wall, and door objects:

class MazeGame {   
public:   
Maze\* CreateMaze();   
// factory methods:   
virtual Maze\* MakeMaze() const   
{ return new Maze; }   
virtual Room\* MakeRoom(int n) const   
{ return new Room(n); }   
virtual Wall\* MakeWall() const   
{ return new Wall; }   
virtualDoor\* MakeDoor(Room\* r1, Room\* r2) const   
{ return new Door(r1, r2); }

Each factory method returns a maze component of a given type. MazeGame provides default implementations that return the simplest kinds of maze, rooms, walls, and doors.

Now we can rewrite CreateMaze to use these factory methods:

Maze\* MazeGame::CreateMaze (){   
Maze\* aMaze= MakeMaze();   
Room\* r1 = MakeRoom(1);   
Room\*r2 = MakeRoom(2);   
Door\*theDoor = MakeDoor(r1, r2);   
aMaze->AddRoom(r1);   
aMaze->AddRoom(r2);   
r1->SetSide(North, MakeWall());   
r1->SetSide(East, theDcor);   
r1->SetSide(South, MakeWall());   
r1->SetSide(West, MakeWall());   
r2->SetSide(North, MakeWall());   
r2->SetSide(East, MakeWall());   
r2->SetSide(South, MakeWall());   
r2->SetSide(West, theDoor);   
return aMaze;

Different games can subclass MazeGame to specialize parts of the maze. MazeGame subclasses can redefine some or all of the factory methods to specify variations in products. For example, a BombedMazeGame can redefine the Room and Wall products to return the bombed varieties:

class BombedMazeGame : public MazeGame {   
public:   
BombedMazeGame();   
virtualWall\* MakeWall()const   
{ return new BombedWall; }   
virtual Room\* MakeRoom(int n) const   
{return new RoomWithABomb(n); }   
};

An EnchantedMazeGame variant might be defined like this:

class EnchantedMazeGame: public MazeGame {   
public:   
EnchantedMazeGame();   
virtual Room\*MakeRoom(int n)const   
{ return new EnchantedRoom(n, CastSpell()); }   
virtual Door\* MakeDoor(Room\* rl, Room\* r2) const   
{ return new DoorNeedingSpell(r1, r2); }   
protected:   
Spell\* CastSpell() const;   
);

## Known Uses

Factory methods pervade toolkits and frameworks. The preceding document example is a typical use in MacApp and ET++ [WGM88]. The manipulator example is from Unidraw.

Class View in the Smalltalk-80 Model/View/Controller framework has a method defaultController that creates a controller, and this might appear to be a factory method [Par90]. But subclasses of View specify the class of their default controller by defining defaultControllerClass, which returns the class from which default-Controller creates instances. So defaultControllerClass is the real factory method, that is, the method that subclasses should override.

A more esoteric example in Smalltalk-80 is the factory method parserClass defined by Behavior (a superclass of all objects representing classes). This enables a class to use a customized parser for its source code. For example, a client can define a class SQLParser to analyze the source code of a class with embedded SQL statements. The Behavior class implements parserClass to return the standard Smalltalk Parser class. A class that includes embedded SQL statements overrides this method (as a class method) and returns the SQLParser class.

The Orbix ORB system from IONA Technologies [ION94] uses Factory Method to generate an appropriate type of proxy (see Proxy (207)) when an object requests a reference to a remote object. Factory Method makes it easy to replace the default proxy with one that uses client-side caching, for example.

## Related Patterns

Abstract Factory (87) is often implemented with factory methods. The Motivation example in the Abstract Factory pattern illustrates Factory Method as well.

Factory methods are usually called within Template Methods (325). In the document

example above, NewDocument is a template method.

Prototypes (117) don’t require subclassing Creator. However, they often require an Initialize operation on the Product class. Creator uses Initialize to initialize the object. Factory Method doesn’t require such an operation.

## Object Creational: Prototype

## Intent

Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

## Motivation

You could build an editor for music scores by customizing a general framework for graphical editors and adding new objects that represent notes, rests, and staves. The editor framework may have a palette of tools for adding these music objects to the score. The palette would also include tools for selecting, moving, and otherwise manipulating music objects. Users will click on the quarter-note tool and use it to add quarter notes to the score. Or they can use the move tool to move a note up or down on the staff, thereby changing its pitch.

Let’s assume the framework provides an abstract Graphic class for graphical components, like notes and staves. Moreover, it’ll provide an abstract Tool class for defining tools like those in the palette. The framework also predefines a GraphicTool subclass for tools that create instances of graphical objects and add them to the document.

But GraphicTool presents a problem to the framework designer. The classes for notes and staves are specific to our application, but the GraphicTool class belongs to the framework. GraphicTool doesn’t know how to create instances of our music classes to add to the score. We could subclass GraphicTool for each kind of music object, but that would produce lots of subclasses that differ only in the kind of music object they instantiate. We know object composition is a flexible alternative to subclassing. The question is, how can the framework use it to parameterize instances of GraphicTool by the class of Graphic they’re supposed to create?

The solution lies in making GraphicTool create a new Graphic by copying or “cloning” an instance of a Graphic subclass. We call this instance a prototype. GraphicTool is parameterized by the prototype it should clone and add to the document. If all Graphic subclasses support a Clone operation, then the GraphicTool can clone any kind of Graphic.