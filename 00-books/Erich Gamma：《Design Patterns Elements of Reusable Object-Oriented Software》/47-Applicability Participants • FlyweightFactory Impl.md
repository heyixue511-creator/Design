The class structure for these objects is shown next. Glyph is the abstract class for graphical objects, some of which may be flyweights. Operations that may depend on extrinsic state have it passed to them as a parameter. For example, Draw and Intersects must know which context the glyph is in before they can do their job.

![](images/cc494a3325a8356e6a20d640c116a7fc387bfa2193ec9b1030faf6c0f04e7cd0.jpg)

A flyweight representing the letter “a” only stores the corresponding character code; it doesn’t need to store its location or font. Clients supply the context-dependent information that the flyweight needs to draw itself. For example, a Row glyph knows where its children should draw themselves so that they are tiled horizontally. Thus it can pass each child its location in the draw request.

Because the number of different character objects is far less than the number of characters in the document, the total number of objects is substantially less than what a naive implementation would use. A document in which all characters appear in the same font and color will allocate on the order of 100 character objects (roughly the size of the ASCII character set) regardless of the document’s length. And since most documents use no more than 10 different font-color combinations, this number won’t grow appreciably in practice. An object abstraction thus becomes practical for individual characters.

## Applicability

The Flyweight pattern’s effectiveness depends heavily on how and where it’s used. Apply the Flyweight pattern when all of the following are true:

• An application uses a large number of objects.

• Storage costs are high because of the sheer quantity of objects.

• Most object state can be made extrinsic.

• Many groups of objects may be replaced by relatively few shared objects once extrinsic state is removed.

• The application doesn’t depend on object identity. Since flyweight objects may be shared, identity tests will return true for conceptually distinct objects.

![](images/5f7a6f2658baab9c6b394055920705e18912fb7c5f09aa30542425327756d0e0.jpg)

The following object diagram shows how flyweights are shared:

![](images/3b7f8ec80fb687d77596154f1e9738e3444009b7809197d5b894daaede0cc193.jpg)

## Participants

• Flyweight (Glyph)

– declares an interface through which flyweights can receive and act on extrinsic state.

## • ConcreteFlyweight (Character)

– implements the Flyweight interface and adds storage for intrinsic state, if any. A ConcreteFlyweight object must be sharable. Any state it stores must be intrinsic; that is, it must be independent of the ConcreteFlyweight object’s context.

## • UnsharedConcreteFlyweight (Row, Column)

– not all Flyweight subclasses need to be shared. The Flyweight interface

enables sharing; it doesn’t enforce it. It’s common for UnsharedConcreteFlyweight objects to have ConcreteFlyweight objects as children at some level in the flyweight object structure (as the Row and Column classes have).

## • FlyweightFactory

– creates and manages flyweight objects.

– ensures that flyweights are shared properly. When a client requests a flyweight, the FlyweightFactory object supplies an existing instance or creates one, if none exists.

## • Client

– maintains a reference to flyweight(s).

– computes or stores the extrinsic state of flyweight(s).

## Collaborations

• State that a flyweight needs to function must be characterized as either intrinsic or extrinsic. Intrinsic state is stored in the ConcreteFlyweight object; extrinsic state is stored or computed by Client objects. Clients pass this state to the flyweight when they invoke its operations.

• Clients should not instantiate ConcreteFlyweights directly. Clients must obtain ConcreteFlyweight objects exclusively from the FlyweightFactory object to ensure they are shared properly.

## Consequences

Flyweights may introduce run-time costs associated with transferring, finding, and/or computing extrinsic state, especially if it was formerly stored as intrinsic state. However, such costs are offset by space savings, which increase as more flyweights are shared.

Storage savings are a function of several factors:

• the reduction in the total number of instances that comes from sharing

• the amount of intrinsic state per object

• whether extrinsic state is computed or stored.

The more flyweights are shared, the greater the storage savings. The savings increase with the amount of shared state. The greatest savings occur when the objects use substantial quantities of both intrinsic and extrinsic state, and the extrinsic state can be computed rather than stored. Then you save on storage in two ways: Sharing reduces the cost of intrinsic state, and you trade extrinsic state for computation time.

The Flyweight pattern is often combined with the Composite (163) pattern to represent a hierarchical structure as a graph with shared leaf nodes. A consequence of sharing is that flyweight leaf nodes cannot store a pointer to their parent. Rather, the parent pointer is passed to the flyweight as part of its extrinsic state. This has a major impact on how the objects in the hierarchy communicate with each other.

## Implementation

Consider the following issues when implementing the Flyweight pattern:

1. Removing extrinsic state. The pattern’s applicability is determined largely by how easy it is to identify extrinsic state and remove it from shared objects. Removing extrinsic state won’t help reduce storage costs if there are as many different kinds of extrinsic state as there are objects before sharing. Ideally, extrinsic state can be computed from a separate object structure, one with far smaller storage requirements.

In our document editor, for example, we can store a map of typographic information in a separate structure rather than store the font and type style with each character object. The map keeps track of runs of characters with the same typographic attributes. When a character draws itself, it receives its typographic attributes as a side-effect of the draw traversal. Because documents normally use just a few different fonts and styles, storing this information externally to each character object is far more efficient than storing it internally.

2 . Managing shared objects. Because objects are shared, clients shouldn’t instantiate them directly. FlyweightFactory lets clients locate a particular flyweight. FlyweightFactory objects often use an associative store to let clients look up flyweights of interest. For example, the flyweight factory in the document editor example can keep a table of flyweights indexed by character codes. The manager returns the proper flyweight given its code, creating the flyweight if it does not already exist.

Sharability also implies some form of reference counting or garbage collection to reclaim a flyweight’s storage when it’s no longer needed. However, neither is necessary if the number of flyweights is fixed and small (e.g., flyweights for the ASCII character set). In that case, the flyweights are worth keeping around permanently.

## Sample Code

Returning to our document formatter example, we can define a Glyph base class for flyweight graphical objects. Logically, glyphs are Composites (see Composite (163)) that have graphical attributes and can draw themselves. Here we focus on just the font attribute, but the same approach can be used for any other graphical attributes a glyph might have.

class Glyph {   
public:   
virtual"Glyph();   
virtual void Draw(Window\*, GlyphContext&);   
virtualvoid SetFont(Font\*, GlyphContext&);   
virtualFont\* GetFont(GlyphContext&);   
virtual void First(GlyphContext&);   
virtual void Next(GlyphContext&);   
virtual bool IsDone(GlyphContext&);   
virtual Glyph\* Current(GlyphContext&);   
virtual void Insert(Glyph\*, GlyphContext&);   
virtual void Remove(GlyphContext&);   
protected:   
Glyph();

The Character subclass just stores a character code:

class Character : public Glyph {   
public:   
Character(char);   
virtualvoid Draw(Window\*, GlyphContext&);   
private:   
char \_charcode;   
};

To keep from allocating space for a font attribute in every glyph, we’ll store the attribute extrinsically in a GlyphContext object. GlyphContext acts as a repository of extrinsic state. It maintains a compact mapping between a glyph and its font (and any other graphical attributes it might have) in different contexts. Any operation that needs to know the glyph’s font in a given context will have a GlyphContext instance passed to it as a parameter. The operation can then query the GlyphContext for the font in that context. The context depends on the glyph’s location in the glyph structure. Therefore Glyph’s child iteration and manipulation operations must update the GlyphContext whenever they’re used.

class GlyphContext {   
public:   
GlyphContext();   
virtual\~GlyphContext();   
virtual void Next(int step = 1);   
virtualvoid Insert(int quantity = 1);   
virtualFont\* GetFont();   
virtualvoid SetFont (Font\*, int span= 1);   
private:   
int \_index;   
BTree\* \_fonts;   
};

GlyphContext must be kept informed of the current position in the glyph structure during traversal. GlyphContext::Next increments \_index as the traversal proceeds. Glyph subclasses that have children (e.g., Row and Column) must implement Next so that it calls GlyphContext::Next at each point in the traversal.

GlyphContext::GetFont uses the index as a key into a BTree structure that stores the glyph-to-font mapping. Each node in the tree is labeled with the length of the string for which it gives font information. Leaves in the tree point to a font, while interior nodes break the string into substrings, one for each child.

Consider the following excerpt from a glyph composition:

2 3 4 5 B -1 2- 9 10 1 12\_ 13 14 15\_16 y. 19-19\_   
0 b e C t 0 r i e n t e d p r 0 g   
5-00 99 100. 101 102 103 104 105 100 107 108 109 110 111112 113   
1   
p e 0 p e e x p e C t t 0 C h   
29920020120020204 205 206 207 208 200. 21021.212 213 314. 216. 216, 217   
I   
a n i t e r a t 0 r F O c a ni

The BTree structure for font information might look like

![](images/c8ebafec058c9f95c12e023596786d2133ec2024f2cb498bb8ab2f4a604e15e8.jpg)

Interior nodes define ranges of glyph indices. BTree is updated in response to font changes and whenever glyphs are added to or removed from the glyph structure. For example, assuming we’re at index 102 in the traversal, the following code sets the font of each character in the word “expect” to that of the surrounding text (that is, times12, an instance of Font for 12-point Times Roman):

GlyphContext gc;   
Font\* times12 =new Font("Times-Roman-12");   
Font\* timesItalic12 = new Font("Times-Italic-12");   
gc.SetFont(times12, 6);

The new BTree structure (with changes shown in black) looks like

![](images/daccd1a6bd76bf93b89ae89f965c46536fb72391bb667b04f8ca6010e4a4bafd.jpg)

Suppose we add the word “don’t” (including a trailing space) in 12-point Times Italic before “expect.” The following code informs the gc of this event, assuming it is still at index 102:

gc.Insert(6);   
gc.SetFont(timesItalic12,6);

The BTree structure becomes

![](images/f3ec089460a7cfed076c3e1b64f8b9da92ee7f7fb72ef9fc3526f7218d9ebec5.jpg)

When the GlyphContext is queried for the font of the current glyph, it descends the BTree, adding up indices as it goes until it finds the font for the current index. Because the frequency of font changes is relatively low, the tree stays small relative to the size of the glyph structure. This keeps storage costs down without an inordinate increase in lookup time.<sup>3</sup>

The last object we need is a FlyweightFactory that creates glyphs and ensures they’re shared properly. Class GlyphFactory instantiates Character and other kinds of glyphs. We only share Character objects; composite glyphs are far less plentiful, and their important state (i.e., their children) is intrinsic anyway.

const int NCHARCODES=128;   
class GlyphFactory {   
public:   
GlyphFactory();   
virtual "GlyphFactory();   
virtualCharacter\* CreateCharacter(char);   
virtual Row\*CreateRow();   
virtual Column\*CreateColumn();   
private:   
Character\* \_character[NCHARCODES];   
}:

The \_character array contains pointers to Character glyphs indexed by character code. The array is initialized to zero in the constructor.