(c) Parameterized adapters. The usual way to support pluggable adapters in Smalltalk is to parameterize an adapter with one or more blocks. The block construct supports adaptation without subclassing. A block can adapt a request, and the adapter can store a block for each individual request. In our example, this means TreeDisplay stores one block for converting a node into a GraphicNode and another block for accessing a node’s children.

For example, to create TreeDisplay on a directory hierarchy, we write

directoryDisplay :=   
(TreeDisplay on: treeRoot)   
getChildrenBlock:   
[:node |node getSubdirectories]   
createGraphicNodeBlock:   
[:node|node createGraphicNode]

If you’re building interface adaptation into a class, this approach offers a convenient alternative to subclassing.

## Sample Code

We’ll give a brief sketch of the implementation of class and object adapters for the Motivation example beginning with the classes Shape and TextView.

class Shape {   
public:   
Shape();   
virtual void BoundingBox(   
Point& bottomLeft, Point& topRight   
) const;   
virtual Manipulator\* CreateManipulator()const;   
};

class TextView {   
public:   
TextView();   
void GetOrigin(Coord& x, Coord& y) const;   
void GetExtent (Coord& width, Coord& height)const;   
virtual bool IsEmpty() const;

Shape assumes a bounding box defined by its opposing corners. In contrast, TextView is defined by an origin, height, and width. Shape also defines a CreateManipulator operation for creating a Manipulator object, which knows how to animate a shape when the user manipulates it.<sup>1</sup> TextView has no equivalent operation. The class TextShape is an adapter between these different interfaces.

A class adapter uses multiple inheritance to adapt interfaces. The key to class adapters is to use one inheritance branch to inherit the interface and another branch to inherit the implementation. The usual way to make this distinction in C++ is to inherit the interface publicly and inherit the implementation privately. We’ll use this convention to define the TextShape adapter.

class TextShape : public Shape, private TextView {   
public:   
TextShape();   
virtual void BoundingBox(   
Point& bottomLeft, Point& topRight   
) const;   
virtual bool IsEmpty() const;   
virtual Manipulator\* CreateManipulator() const;

The BoundingBox operation converts TextView’s interface to conform to Shape’s.

void TextShape::BoundingBox (   
Point& bottomLeft, Point& topRight   
) const {   
Coord bottom,left, width, height;   
GetOrigin(bottom, left);   
GetExtent(width, height);   
bottomLeft = Point(bottom, left);   
topRight = Point(bottom + height, left + width);   
}

The IsEmpty operation demonstrates the direct forwarding of requests common in adapter implementations:

bool TextShape::IsEmpty () const {   
return TextView::IsEmpty();

Finally, we define CreateManipulator (which isn’t supported by TextView) from scratch. Assume we’ve already implemented a TextManipulator class that supports manipulation of a TextShape.

Manipulator\* TextShape::CreateManipulator () const {   
return new TextManipulator(this);

The object adapter uses object composition to combine classes with different interfaces. In this approach, the adapter TextShape maintains a pointer to TextView.

class TextShape : public Shape {   
public:   
TextShape(TextView\*);   
virtual void BoundingBox(   
Point& bottomLeft, Point& topRight   
) const;   
virtual bool IsEmpty() const;   
virtual Manipulator\* CreateManipulator() const;   
private:   
TextView\*\_text;

TextShape must initialize the pointer to the TextView instance, and it does so in the constructor. It must also call operations on its TextView object whenever its own operations are called. In this example, assume that the client creates the TextView object and passes it to the TextShape constructor:

TextShape::TextShape (TextView\* t) {   
\_text = t;   
void TextShape::BoundingBox (   
Point& bottomLeft, Point& topRight   
) const (   
Coord bottom, left, width, height;   
\_text->GetOrigin(bottom, left);   
\_text->GetExtent(width,height);   
bottomLeft = Point(bottom,left);   
topRight = Point (bottom + height, left + width);   
bool TextShape::IsEmpty () const {   
return \_text->IsEmpty();

CreateManipulator’s implementation doesn’t change from the class adapter version, since it’s implemented from scratch and doesn’t reuse any existing TextView functionality.

Manipulator\* TextShape::CreateManipulator () const {   
return new TextManipulator(this);   
)

Compare this code to the class adapter case. The object adapter requires a little more effort to write, but it’s more flexible. For example, the object adapter version of TextShape will work equally well with subclasses of TextView—the client simply passes an instance of a TextView subclass to the TextShape constructor.

## Known Uses

The Motivation example comes from ET++Draw, a drawing application based on ET++ [WGM88]. ET++Draw reuses the ET++ classes for text editing by using a TextShape adapter class.

Interviews 2.6 defines an Interactor abstract class for user interface elements such as scroll bars, buttons, and menus [VL88]. It also defines a Graphic abstract class for structured graphic objects such as lines, circles, polygons, and splines. Both Interactors and Graphics have graphical appearances, but they have different interfaces and implementations (they share no common parent class) and are therefore incompatible— you can’t embed a structured graphic object in, say, a dialog box directly.

Instead, Interviews 2.6 defines an object adapter called GraphicBlock, a subclass of Interactor that contains a Graphic instance. The GraphicBlock adapts the interface of the Graphic class to that of Interactor. The GraphicBlock lets a Graphic instance be displayed, scrolled, and zoomed within an Interactor structure.

Pluggable adapters are common in ObjectWorks\Smalltalk [Par90]. Standard Smalltalk defines a ValueModel class for views that display a single value. ValueModel defines a value, value: interface for accessing the value. These are abstract methods. Application writers access the value with more domain-specific names like width and width:, but they shouldn’t have to subclass ValueModel to adapt such applicationspecific names to the ValueModel interface.

Instead, ObjectWorks\Smalltalk includes a subclass of ValueModel called PluggableAdaptor. A PluggableAdaptor object adapts other objects to the ValueModel interface (value, value:). It can be parameterized with blocks for getting and setting the desired value. PluggableAdaptor uses these blocks internally to implement the value, value: interface. PluggableAdaptor also lets you pass in the selector names (e.g., width, width:) directly for syntactic convenience. It converts these selectors into the corresponding blocks automatically.

![](images/b62484fd4b856d7e2525fdd05b6c9db64204f6f4c19afe6f86edb2044c0e3ca6.jpg)

Another example from ObjectWorks\Smalltalk is the TableAdaptor class. A TableAdaptor can adapt a sequence of objects to a tabular presentation. The table displays one object per row. The client parameterizes TableAdaptor with the set of messages that a table can use to get the column values from an object.

Some classes in NeXT’s AppKit [Add94] use delegate objects to perform interface adaptation. An example is the NXBrowser class that can display hierarchical lists of data. NXBrowser uses a delegate object for accessing and adapting the data.

Meyer’s “Marriage of Convenience” [Mey88] is a form of class adapter. Meyer describes how a FixedStack class adapts the implementation of an Array class to the interface of a Stack class. The result is a stack containing a fixed number of entries.