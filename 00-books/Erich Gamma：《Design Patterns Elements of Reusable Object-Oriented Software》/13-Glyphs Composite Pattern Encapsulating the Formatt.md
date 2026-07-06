This approach has two important implications. The first is obvious: The objects need corresponding classes. The second implication, which maybe less obvious, is that these classes must have compatible interfaces, because we want to treat the objects uniformly. The way to make interfaces compatible in a language like C++ is to relate the classes through inheritance.

## Glyphs

We’ll define a Glyph abstract class for all objects that can appear in a document structure.<sup>3</sup> Its subclasses define both primitive graphical elements (like characters and images) and structural elements (like rows and columns). Figure 2.4 depicts a representative part of the Glyph class hierarchy, and Table 2.1 presents the basic glyph interface in more detail using C++ notation.

Figure 2.4: Partial Glyph class hierarchy  
![](images/736fa2c01af890a3cee9cbb0dfdee185ae099c6b12f6994af33f2576ae58c23d.jpg)

Table 2.1: Basic glyph interface
<table><tr><td>Responsibility</td><td>Operations</td></tr><tr><td>appearance</td><td>virtual void Draw(Window*) virtual</td></tr><tr><td>hit detection</td><td>void Bounds (Rect&amp;) Intersects(const Point&amp;)</td></tr><tr><td rowspan="4">structure</td><td>virtual bool virtual</td></tr><tr><td>void Insert(Glyph*, int) voidRemove(Glyph*)</td></tr><tr><td>virtual virtual Glyph* Child(int)</td></tr><tr><td>virtualGlyph* Parent()</td></tr></table>

Glyphs have three basic responsibilities. They know (1) how to draw themselves, (2) what space they occupy, and (3) their children and parent.

Glyph subclasses redefine the Draw operation to render themselves onto a window. They are passed a reference to a Window object in the call to Draw. The Window class defines graphics operations for rendering text and basic shapes in a window on the screen. A Rectangle subclass of Glyph might redefine Draw as follows:

void Rectangle::Draw (Window\* w) {   
w->DrawRect(\_x0, \_y0, \_x1, y1);

where \_x0, \_y0, \_x1, and \_y1 are data members of Rectangle that define two opposing corners of the rectangle. DrawRect is the Window operation that makes the rectangle appear on the screen.

A parent glyph often needs to know how much space a child glyph occupies, for example, to arrange it and other glyphs in a line so that none overlaps (as shown in Figure 2.2). The Bounds operation returns the rectangular area that the glyph occupies. It returns the opposite corners of the smallest rectangle that contains the glyph. Glyph subclasses redefine this operation to return the rectangular area in which they draw.

T he Intersects operation returns whether a specified point intersects the glyph. Whenever the user clicks somewhere in the document, Lexi calls this operation to determine which glyph or glyph structure is under the mouse. The Rectangle class redefines this operation to compute the intersection of the rectangle and the given point.

Because glyphs can have children, we need a common interface to add, remove, and access those children. For example, a Row’s children are the glyphs it arranges into a row. The Insert operation inserts a glyph at a position specified by an integer index.<sup>5</sup> The Remove operation removes a specified glyph if it is indeed a child.

The Child operation returns the child (if any) at the given index. Glyphs like Row that can have children should use Child internally instead of accessing the child data structure directly. That way you won’t have to modify operations like Draw that iterate through the children when you change the data structure from, say, an array to a linked list. Similarly, Parent provides a standard interface to the glyph’s parent, if any. Glyphs in Lexi store a reference to their parent, and their Parent operation simply returns this reference.

## Composite Pattern

Recursive composition is good for more than just documents. We can use it to represent any potentially complex, hierarchical structure. The Composite (163) pattern captures the essence of recursive composition in object-oriented terms. Now would be a good time to turn to that pattern and study it, referring back to this scenario as needed.

## 2.3 Formatting

We’ve settled on a way to represent the document’s physical structure. Next, we need to figure out how to construct a particular physical structure, one that corresponds to a properly formatted document. Representation and formatting are distinct: The ability to capture the document’s physical structure doesn’t tell us how to arrive at a particular structure. This responsibility rests mostly on Lexi. It must break text into lines, lines into columns, and so on, taking into account the user’s higher-level desires. For example, the user might want to vary margin widths, indentation, and tabulation; single or double space; and probably many other formatting constraints.<sup>6</sup> Lexi’s formatting algorithm must take all of these into account.

By the way, we’ll restrict “formatting” to mean breaking a collection of glyphs into lines. In fact, we’ll use the terms “formatting” and “linebreaking” interchangeably. The techniques we’ll discuss apply equally well to breaking lines into columns and to breaking columns into pages.

## Encapsulating the Formatting Algorithm

The formatting process, with all its constraints and details, isn’t easy to automate. There are many approaches to the problem, and people have come up with a variety of formatting algorithms with different strengths and weaknesses. Because Lexi is a WYSIWYG editor, an important trade-off to consider is the balance between formatting quality and formatting speed. We want generally good response from the editor without sacrificing how good the document looks. This trade-off is subject to many factors, not all of which can be ascertained at compile-time. For example, the user might tolerate slightly slower response in exchange for better formatting. That trade-off might make an entirely different formatting algorithm more appropriate than the current one. Another, more implementation-driven trade-off balances formatting speed and storage requirements: It may be possible to decrease formatting time by caching more information.

Because formatting algorithms tend to be complex, it’s also desirable to keep them well-contained or—better yet—completely independent of the document structure. Ideally we could add a new kind of Glyph subclass without regard to the formatting algorithm. Conversely, adding a new formatting algorithm shouldn’t require modifying existing glyphs.

These characteristics suggest we should design Lexi so that it’s easy to change the formatting algorithm at least at compile-time, if not at run-time as well. We can isolate the algorithm and make it easily replaceable at the same time by encapsulating it in an object. More specifically, we’ll define a separate class hierarchy for objects that encapsulate formatting algorithms. The root of the hierarchy will define an interface that supports a wide range of formatting algorithms, and each subclass will implement the interface to carry out a particular algorithm. Then we can introduce a Glyph subclass that will structure its children automatically using a given algorithm object.

## Compositor and Composition

We’ll define a Compositor class for objects that can encapsulate a formatting algorithm. The interface (Table 2.2) lets the compositor know what glyphs to format and when to do the formatting. The glyphs it formats are the children of a special Glyph subclass called Composition. A composition gets an instance of a Compositor subclass (specialized for a particular linebreaking algorithm) when it is created, and it tells the compositor to Compose its glyphs when necessary, for example, when the user changes a document. Figure 2.5 depicts the relationships between the Composition and Compositor classes.

Table 2.2: Basic compositor interface
<table><tr><td rowspan=1 colspan=1>Responsibility</td><td rowspan=1 colspan=1>Operations</td></tr><tr><td rowspan=1 colspan=1>what to format</td><td rowspan=1 colspan=1>void SetComposition(Composition*)</td></tr><tr><td rowspan=1 colspan=1>when to format</td><td rowspan=1 colspan=1>virtual void Compose()</td></tr></table>

Figure 2.5: Composition and Compositor class relationships  
![](images/e8ed28a3c2ab0da14a658892287acec316c04cd062e96bc118c4b46dfb23fc27.jpg)

An unformatted Composition object contains only the visible glyphs that make up the document’s basic content. It doesn’t contain glyphs that determine the document’s physical structure, such as Row and Column. The composition is in this state just after it’s created and initialized with the glyphs it should format. When the composition needs formatting, it calls its compositor’s Compose operation. The compositor in turn iterates through the composition’s children and inserts new Row and Column glyphs according to its linebreaking algorithm.<sup>7</sup> Figure 2.6 shows the resulting object structure. Glyphs that the compositor created and inserted into the object structure appear with gray backgrounds in the figure.

Figure 2.6: Object structure reflecting compositor-directed linebreaking