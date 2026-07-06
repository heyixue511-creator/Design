# Recursive Composition / Glyphs / Composite Pattern

> Section: preface | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

## Recursive Composition

A common way to represent hierarchically structured information is through a technique called recursive composition, which entails building increasingly complex elements out of simpler ones. Recursive composition gives us a way to compose a document out of simple graphical elements. As a first step, we can tile a set of characters and graphics from left to right to form a line in the document. Then multiple lines can be arranged to form a column, multiple columns can form a page, and so on (see Figure 2.2).

Figure 2.2: Recursive composition of text and graphics

![](images/fb9f1c66147ca20deffb97ec9b301eb477b6f5164a314a8e65d02b7c5531259b.jpg)  
We can represent this physical structure by devoting an object to each important element. That includes not just the visible elements like the characters and graphics but the invisible, structural elements as well—the lines and the column. The result is the object structure shown in Figure 2.3.

Figure 2.3: Object structure for recursive composition of text and graphics  
![](images/d91700ca3a2191fbfd4cad90e3e24fc2487865736b27825fe620b9d849f1a21e.jpg)  
By using an object for each character and graphical element in the document, we promote flexibility at the finest levels of Lexi’s design. We can treat text and graphics uniformly with respect to how they are drawn, formatted, and embedded within each other. We can extend Lexi to support new character sets without disturbing other functionality. Lexi’s object structure mimics the document’s physical structure.

This approach has two important implications. The first is obvious: The objects need corresponding classes. The second implication, which maybe less obvious, is that these classes must have compatible interfaces, because we want to treat the objects uniformly. The way to make interfaces compatible in a language like C++ is to relate the classes through inheritance.

## Glyphs

We’ll define a Glyph abstract class for all objects that can appear in a document structure.<sup>3</sup> Its subclasses define both primitive graphical elements (like characters and images) and structural elements (like rows and columns). Figure 2.4 depicts a representative part of the Glyph class hierarchy, and Table 2.1 presents the basic glyph interface in more detail using C++ notation.

Figure 2.4: Partial Glyph class hierarchy  
![](images/cf1ee1348dd3e3f42c408bd833f04e453c4c8eecd2f0746ee8e57ed540463b51.jpg)

Table 2.1: Basic glyph interface
<table><tr><td>Responsibility</td><td>Operations</td></tr><tr><td>appearance</td><td>virtual void Draw(Window*) virtual</td></tr><tr><td>hit detection</td><td>void Bounds (Rect&amp;) Intersects(const Point&amp;)</td></tr><tr><td rowspan="4">structure</td><td>virtual bool virtual</td></tr><tr><td>void Insert(Glyph*, int) voidRemove(Glyph*)</td></tr><tr><td>virtual virtual Glyph* Child(int)</td></tr><tr><td>virtualGlyph* Parent()</td></tr></table>

Glyphs have three basic responsibilities. They know (1) how to draw themselves, (2) what space they occupy, and (3) their children and parent.

Glyph subclasses redefine the Draw operation to render themselves onto a window. They are passed a reference to a Window object in the call to Draw. The Window class defines graphics operations for rendering text and basic shapes in a window on the screen. A Rectangle subclass of Glyph might redefine Draw as follows:

void Rectangle::Draw (Window\* w) {   
w->DrawRect(\_x0, \_y0, \_x1, y1)

where \_x0, \_y0, \_x1, and \_y1 are data members of Rectangle that define two opposing corners of the rectangle. DrawRect is the Window operation that makes the rectangle appear on the screen.

A parent glyph often needs to know how much space a child glyph occupies, for example, to arrange it and other glyphs in a line so that none overlaps (as shown in Figure 2.2). The Bounds operation returns the rectangular area that the glyph occupies. It returns the opposite corners of the smallest rectangle that contains the glyph. Glyph subclasses redefine this operation to return the rectangular area in which they draw.

T he Intersects operation returns whether a specified point intersects the glyph. Whenever the user clicks somewhere in the document, Lexi calls this operation to determine which glyph or glyph structure is under the mouse. The Rectangle class redefines this operation to compute the intersection of the rectangle and the given point.

Because glyphs can have children, we need a common interface to add, remove, and access those children. For example, a Row’s children are the glyphs it arranges into a row. The Insert operation inserts a glyph at a position specified by an integer index.<sup>5</sup> The Remove operation removes a specified glyph if it is indeed a child.

The Child operation returns the child (if any) at the given index. Glyphs like Row that can have children should use Child internally instead of accessing the child data structure directly. That way you won’t have to modify operations like Draw that iterate through the children when you change the data structure from, say, an array to a linked list. Similarly, Parent provides a standard interface to the glyph’s parent, if any. Glyphs in Lexi store a reference to their parent, and their Parent operation simply returns this reference.

## Composite Pattern

Recursive composition is good for more than just documents. We can use it to represent any potentially complex, hierarchical structure. The Composite (163) pattern captures the essence of recursive composition in object-oriented terms. Now would be a good time to turn to that pattern and study it, referring back to this scenario as needed.

