class Singleton {   
public:   
static void Register(const char\* name, Singleton\*);   
static Singleton\* Instance();   
protected:   
static Singleton\* Lookup(constchar\*name);   
private:   
static Singleton\* \_instance;   
static List<NameSingletonPair>\*\_registry;   
);

Register registers the Singleton instance under the given name. To keep the registry simple, we’ll have it store a list of NameSingletonPair objects. Each NameSingletonPair maps a name to a singleton. The Lookup operation finds a singleton given its name. We’ll assume that an environment variable specifies the name of the singleton desired.

Singleton\* Singleton::Instance () {   
if (\_instance == 0) {   
const char\* singletonName = getenv("SINGLETON");   
// user or environment supplies this at startup   
\_instance = Lookup(singletonName);   
// Lookup returns 0 if there's no such singleton   
return \_instance;   
}

Where do Singleton classes register themselves? One possibility is in their constructor. For example, a MySingleton subclass could do the following:

MySingleton::MySingleton() {   
Singleton::Register("MySingleton", this);   
}

Of course, the constructor won’t get called unless someone instantiates the class, which echoes the problem the Singleton pattern is trying to solve! We can get around this problem in C++ by defining a static instance of MySingleton. For example, we can define

## static MySingleton theSingleton;

in the file that contains MySingleton’s implementation.

No longer is the Singleton class responsible for creating the singleton. Instead, its primary responsibility is to make the singleton object of choice accessible in the system. The static object approach still has a potential drawback—namely that instances of all possible Singleton subclasses must be created, or else they won’t get registered.

## Sample Code

Suppose we define a MazeFactory class for building mazes as described on page 92. MazeFactory defines an interface for building different parts of a maze. Subclasses can redefine the operations to return instances of specialized product classes, like BombedWall objects instead of plain Wall objects.

What’s relevant here is that the Maze application needs only one instance of a maze factory, and that instance should be available to code that builds any part of the maze. This is where the Singleton pattern comes in. By making the MazeFactory a singleton, we make the maze object globally accessible without resorting to global variables.

For simplicity, let’s assume we’ll never subclass MazeFactory. (We’ll consider the alternative in a moment.) We make it a Singleton class in C++ by adding a static Instance operation and a static \_instance member to hold the one and only instance. We must also protect the constructor to prevent accidental instantiation, which might lead to more than one instance.

class MazeFactory {   
public:   
static MazeFactory\* Instance();   
// existing interface goes here   
protected:   
MazeFactory();   
private:   
staticMazeFactory\*\_instance;

The corresponding implementation is

MazeFactory\* MazeFactory::\_instance = 0;   
MazeFactory\* MazeFactory::Instance(){   
if (\_instance == 0) {   
\_instance = new MazeFactory;   
return\_instance;   
}

Now let’s consider what happens when there are subclasses of MazeFactory, and the application must decide which one to use. We’ll select the kind of maze through an environment variable and add code that instantiates the proper MazeFactory subclass based on the environment variable’s value. The Instance operation is a good place to put this code, because it already instantiates MazeFactory:

MazeFactory\* MazeFactory::Instance () {   
if (\_instance == 0) (   
const char\* mazeStyle = getenv("MAZESTYLE");   
if (strcmp(mazeStyle, "bombed") == 0) {   
\_instance = new BombedMazeFactory;   
} else if (strcmp(mazeStyle, "enchanted") == 0) {   
\_instance = new EnchantedMazeFactory;   
//... other possible subclasses   
} else { // default   
\_instance = new MazeFactory;   
return \_instance;

Note that Instance must be modified whenever you define a new subclass of MazeFactory. That might not be a problem in this application, but it might be for abstract factories defined in a framework.

A possible solution would be to use the registry approach described in the Implementation section. Dynamic linking could be useful here as well—it would keep the application from having to load all the subclasses that are not used.

## Known Uses

An example of the Singleton pattern in Smalltalk-80 [Par90] is the set of changes to the code, which is ChangeSet current. A more subtle example is the relationship between classes and their metaclasses. A metaclass is the class of a class, and each metaclass has one instance. Metaclasses do not have names (except indirectly through their sole instance), but they keep track of their sole instance and will not normally create another.

The Interviews user interface toolkit [LCI<sup>+</sup>92] uses the Singleton pattern to access the unique instance of its Session and WidgetKit classes, among others. Session defines the application’s main event dispatch loop, stores the user’s database of stylistic preferences, and manages connections to one or more physical displays. WidgetKit is an Abstract Factory (87) for defining the look and feel of user interface widgets. The WidgetKit::instance() operation determines the particular WidgetKit subclass that’s instantiated based on an environment variable that Session defines. A similar operation on Session determines whether monochrome or color displays are supported and configures the singleton Session instance accordingly.

## Related Patterns

Many patterns can be implemented using the Singleton pattern. See Abstract Factory (87), Builder (97), and Prototype (117).

## Discussion of Creational Patterns

There are two common ways to parameterize a system by the classes of objects it creates. One way is to subclass the class that creates the objects; this corresponds to using the Factory Method (107) pattern. The main drawback of this approach is that it can require creating a new subclass just to change the class of the product. Such changes can cascade. For example, when the product creator is itself created by a factory method, then you have to override its creator as well.

The other way to parameterize a system relies more on object composition: Define an object that’s responsible for knowing the class of the product objects, and make it a parameter of the system. This is a key aspect of the Abstract Factory (87), Builder (97), and Prototype (117) patterns. All three involve creating a new “factory object” whose responsibility is to create product objects. Abstract Factory has the factory object producing objects of several classes. Builder has the factory object building a complex product incrementally using a correspondingly complex protocol. Prototype has the factory object building a product by copying a prototype object. In this case, the factory object and the prototype are the same object, because the prototype is responsible for returning the product.

Consider the drawing editor framework described in the Prototype pattern. There are several ways to parameterize a GraphicTool by the class of product:

• By applying the Factory Method pattern, a subclass of GraphicTool will be created for each subclass of Graphic in the palette. GraphicTool will have a NewGraphic operation that each GraphicTool subclass will redefine.

• By applying the Abstract Factory pattern, there will be a class hierarchy of GraphicsFactories, one for each Graphic subclass. Each factory creates just one product in this case: CircleFactory will create Circles, LineFactory will create Lines, and so on. A GraphicTool will be parameterized with a factory for creating the appropriate kind of Graphics.

• By applying the Prototype pattern, each subclass of Graphics will implement the Clone operation, and a GraphicTool will be parameterized with a prototype of the Graphic it creates.

Which pattern is best depends on many factors. In our drawing editor framework, the Factory Method pattern is easiest to use at first. It’s easy to define a new subclass of

GraphicTool, and the instances of GraphicTool are created only when the palette is defined. The main disadvantage here is that GraphicTool subclasses proliferate, and none of them does very much.

Abstract Factory doesn’t offer much of an improvement, because it requires an equally large GraphicsFactory class hierarchy. Abstract Factory would be preferable to Factory Method only if there were already a GraphicsFactory class hierarchy—either because the compiler provides it automatically (as in Smalltalk or Objective C) or because it’s needed in another part of the system.

Overall, the Prototype pattern is probably the best for the drawing editor framework, because it only requires implementing a Clone operation on each Graphics class. That reduces the number of classes, and Clone can be used for purposes other than pure instantiation (e.g., a Duplicate menu operation).

Factory Method makes a design more customizable and only a little more complicated. Other design patterns require new classes, whereas Factory Method only requires a new operation. People often use Factory Method as the standard way to create objects, but it isn’t necessary when the class that’s instantiated never changes or when instantiation takes place in an operation that subclasses can easily override, such as an initialization operation.

Designs that use Abstract Factory, Prototype, or Builder are even more flexible than those that use Factory Method, but they’re also more complex. Often, designs start out using Factory Method and evolve toward the other creational patterns as the designer discovers where more flexibility is needed. Knowing many design patterns gives you more choices when trading off one design criterion against another.