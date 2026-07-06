operation.

Now we can traverse the glyph structure, calling CheckMe on each glyph with the spelling checker as an argument. This effectively identifies each glyph to the SpellingChecker and prompts the checker to do the next increment in the spelling check.

SpellingChecker spellingChecker;   
Composition\*c;   
Glyph\*g;   
PreorderIterator i(c);   
for (i.First(); !i.IsDone(); i.Next()){   
g = i.CurrentItem();   
g->CheckMe(spellingChecker);

The following interaction diagram illustrates how Character glyphs and the SpellingChecker object work together:

![](images/62c631d124df2d6ba4e70962d8fe86b6a5309141b0f31c487fbdfe80c429a103.jpg)

This approach works for finding spelling errors, but how does it help us support multiple kinds of analysis? It looks like we have to add an operation like CheckMe(SpellingChecker&) to Glyph and its subclasses whenever we add a new kind of analysis. That’s true if we insist on an independent class for every analysis. But there’s no reason why we can’t give all analysis classes the same interface. Doing so lets us use them polymorphically. That means we can replace analysis-specific operations like CheckMe(SpellingChecker&) with an analysis-independent operation that takes a more general parameter.

## Visitor Class and Subclasses

We’ll use the term visitor to refer generally to classes of objects that “visit” other objects during a traversal and do something appropriate.<sup>12</sup> In this case we can define a Visitor class that defines an abstract interface for visiting glyphs in a structure.

class Visitor (   
public:   
virtual void VisitCharacter(Character\*) { }   
virtual void VisitRow(Row\*){ }   
virtual void VisitImage(Image\*) { }   
// ... and so forth

Concrete subclasses of Visitor perform different analyses. For example, we could have a SpellingCheckingVisitor subclass for checking spelling, and a HyphenationVisitor subclass for hyphenation. SpellingCheckingVisitor would be implemented exactly as we implemented SpellingChecker above, except the operation names would reflect the more general Visitor interface. For example, CheckCharacter would be called VisitCharacter.

Since CheckMe isn’t appropriate for visitors that don’t check anything, we’ll give it a more general name: Accept. Its argument must also change to take a Visitor&, reflecting the fact that it can accept any visitor. Now adding a new analysis requires just defining a new subclass of Visitor—we don’t have to touch any of the glyph classes. We support all future analyses by adding this one operation to Glyph and its subclasses.

We’ve already seen how spelling checking works. We use a similar approach in HyphenationVisitor to accumulate text. But once HyphenationVisitor’s VisitCharacter operation has assembled an entire word, it works a little differently. Instead of checking the word for misspelling, it applies a hyphenation algorithm to determine the potential hyphenation points in the word, if any. Then at each hyphenation point, it inserts a discretionary glyph into the composition. Discretionary glyphs are instances of Discretionary, a subclass of Glyph.

A discretionary glyph has one of two possible appearances depending on whether or not it is the last character on a line. If it’s the last character, then the discretionary looks like a hyphen; if it’s not at the end of a line, then the discretionary has no appearance whatsoever. The discretionary checks its parent (a Row object) to see if it is the last child. The discretionary makes this check whenever it’s called on to draw itself or calculate its boundaries. The formatting strategy treats discretionaries the same as whitespace, making them candidates for ending a line. The following diagram shows how an embedded discretionary can appear.

![](images/daa769199e6448091719b653a96716e38dc7a034ee216334b6dce3d39ce404fd.jpg)

## Visitor Pattern

What we’ve described here is an application of the Visitor (331) pattern. The Visitor class and its subclasses described earlier are the key participants in the pattern. The Visitor pattern captures the technique we’ve used to allow an open-ended number of analyses of glyph structures without having to change the glyph classes themselves. Another nice feature of visitors is that they can be applied not just to composites like our glyph structures but to any object structure. That includes sets, lists, even directed-acyclic graphs. Furthermore, the classes that a visitor can visit needn’t be related to each other through a common parent class. That means visitors can work across class hierarchies.

An important question to ask yourself before applying the Visitor pattern is, Which class hierarchies change most often? The pattern is most suitable when you want to be able to do a variety of different things to objects that have a stable class structure. Adding a new kind of visitor requires no change to that class structure, which is especially important when the class structure is large. But whenever you add a subclass to the structure, you’ll also have to update all your visitor interfaces to include a Visit... operation for that subclass. In our example that means adding a new Glyph subclass called Foo will require changing Visitor and all its subclasses to include a VisitFoo operation. But given our design constraints, we’re much more likely to add a new kind of analysis to Lexi than a new kind of Glyph. So the Visitor pattern is well-suited to our needs.

## 2.9 Summary

We’ve applied eight different patterns to Lexi’s design:

1. Composite (163) to represent the document’s physical structure,

2. Strategy (315) to allow different formatting algorithms,

3. Decorator (175) for embellishing the user interface,

4. Abstract Factory (87) for supporting multiple look-and-feel standards,

5. Bridge (151) to allow multiple windowing platforms,

6. Command (233) for undoable user operations,

7. Iterator (257) for accessing and traversing object structures, and

8 . Visitor (331) for allowing an open-ended number of analytical capabilities without complicating the document structure’s implementation.

None of these design issues is limited to document editing applications like Lexi. Indeed, most nontrivial applications will have occasion to use many of these patterns, though perhaps to do different things. A financial analysis application might use Composite to define investment portfolios made up of subportfolios and accounts of different sorts. A compiler might use the Strategy pattern to allow different register allocation schemes for different target machines. Applications with a graphical user interface will probably apply at least Decorator and Command just as we have here.

While we’ve covered several major problems in Lexi’s design, there are lots of others we haven’t discussed. Then again, this book describes more than just the eight patterns we’ve used here. So as you study the remaining patterns, think about how you might use each one in Lexi. Or better yet, think about using them in your own designs!

Design Pattern Catalog