# Abstracting Object Creation / Factories and Product Classes / ScrollBar\* sb = new MotifScrollBar; / GUIFactory\* guiFactory = new MotifFactory; / Abstract Factory Pattern

> Section: preface | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

## Abstracting Object Creation

Everything we see and interact with in Lexi’s user interface is a glyph composed in other, invisible glyphs like Row and Column. The invisible glyphs compose visible ones like Button and Character and lay them out properly. Style guides have much to say about the look and feel of so-called “widgets,” another term for visible glyphs like buttons, scroll bars, and menus that act as controlling elements in a user interface. Widgets might use simpler glyphs such as characters, circles, rectangles, and polygons to present data.

We’ll assume we have two sets of widget glyph classes with which to implement multiple look-and-feel standards:

1 . A set of abstract Glyph subclasses for each category of widget glyph. For example, an abstract class ScrollBar will augment the basic glyph interface to add general scrolling operations; Button is an abstract class that adds button-oriented operations; and so on.

2. A set of concrete subclasses for each abstract subclass that implement different look-and-feel standards. For example, ScrollBar might have Motif ScrollBar and PMScrollBar subclasses that implement Motif and Presentation Manager-style scroll bars, respectively.

Lexi must distinguish between widget glyphs for different look-and-feel styles. For example, when Lexi needs to put a button in its interface, it must instantiate a Glyph subclass for the right style of button (MotifButton, PMButton, MacButton, etc.).

It’s clear that Lexi’s implementation can’t do this directly, say, using a constructor call in C++. That would hard-code the button of a particular style, making it impossible to select the style at run-time. We’d also have to track down and change every such constructor call to port Lexi to another platform. And buttons are only one of a variety of widgets in Lexi’s user interface. Littering our code with constructor calls to specific look-and-feel classes yields a maintenance nightmare—miss just one, and you could end up with a Motif menu in the middle of your Mac application.

Lexi needs a way to determine the look-and-feel standard that’s being targeted in order to create the appropriate widgets. Not only must we avoid making explicit constructor calls; we must also be able to replace an entire widget set easily. We can achieve both by abstracting the process of object creation. An example will illustrate what we mean.

## Factories and Product Classes

Normally we might create an instance of a Motif scroll bar glyph with the following C++ code:

## ScrollBar\* sb = new MotifScrollBar;

This is the kind of code to avoid if you want to minimize Lexi’s look-and-feel dependencies. But suppose we initialize sb as follows:

$$
\mathrm { S c r o l l B a r ^ { * } \ s b = g u i F a c t o r y { \mathrm { - } } C r e a t e S c r o l l B a r ( ) ; }
$$

where guiFactory is an instance of a MotifFactory class. CreateScrollBar returns a new instance of the proper ScrollBar subclass for the look and feel desired, Motif in this case. As far as clients are concerned, the effect is the same as calling the MotifScrollBar constructor directly. But there’s a crucial difference: There’s no longer anything in the code that mentions Motif by name. The guiFactory object abstracts the process of creating not just Motif scroll bars but scroll bars for any look-and-feel standard. And guiFactory isn’t limited to producing scroll bars. It can manufacture a full range of widget glyphs, including scroll bars, buttons, entry fields, menus, and so forth.

All this is possible because MotifFactory is a subclass of GUIFactory, an abstract class that defines a general interface for creating widget glyphs. It includes operations l i ke CreateScrollBar and CreateButton for instantiating different kinds of widget glyphs. Subclasses of GUIFactory implement these operations to return glyphs such as MotifScrollBar and PMButton that implement a particular look and feel. Figure 2.9 shows the resulting class hierarchy for guiFactory objects.

Figure 2.9: GUIFactory class hierarchy  
![](images/f70e845a38deabdcfeba1b36af7aa8dc3a9777431c5d7bd7aafcea06cdf664fc.jpg)  
We say that factories create product objects. Moreover, the products that a factory

produces are related to one another; in this case, the products are all widgets for the same look and feel. Figure 2.10 shows some of the product classes needed to make factories work for widget glyphs.

Figure 2.10: Abstract product classes and concrete subclasses  
![](images/fb512e7a9208703402b53a2683172a1f1fc7203e619e60caf63db191b278d1eb.jpg)

The last question we have to answer is, Where does the GUIFactory instance come from? The answer is, Anywhere that’s convenient. The variable guiFactory could be a global, a static member of a well-known class, or even a local variable if the entire user interface is created within one class or function. There’s even a design pattern, Singleton (127), for managing well-known, one-of-a-kind objects like this. The important thing, though, is to initialize guiFactory at a point in the program before it’s ever used to create widgets but after it’s clear which look and feel is desired.

If the look and feel is known at compile-time, then guiFactory can be initialized with a simple assignment of a new factory instance at the beginning of the program:

## GUIFactory\* guiFactory = new MotifFactory;

If the user can specify the look and feel with a string name at startup time, then the code to create the factory might be

GUIFactory\* guiFactory;   
constchar\*styleName = getenv("LOOK\_AND\_FEEL");   
// user or environment supplies this at startup   
if(strcmp(styleName, "Motif") ==0) {   
guiFactory= new MotifFactory:   
) else if (strcmp(styleName, "Presentation\_Manager") == 0) {   
guiFactory= newPMFactory;   
} else {   
guiFactory= new DefaultGUIFactory;

There are more sophisticated ways to select the factory at run-time. For example, you could maintain a registry that maps strings to factory objects. That lets you register instances of new factory subclasses without modifying existing code, as the preceding approach requires. And you don’t have to link all platform-specific factories into the application. That’s important, because it might not be possible to link a MotifFactory on a platform that doesn’t support Motif.

But the point is that once we’ve configured the application with the right factory object, its look and feel is set from then on. If we change our minds, we can reinitialize guiFactory with a factory for a different look and feel and then reconstruct the interface. Regardless of how and when we decide to initialize guiFactory, we know that once we do, the application can create the appropriate look and feel without modification.

## Abstract Factory Pattern

Factories and products are the key participants in the Abstract Factory (87) pattern. This pattern captures how to create families of related product objects without instantiating classes directly. It’s most appropriate when the number and general kinds of product objects stay constant, and there are differences in specific product families. We choose between families by instantiating a particular concrete factory and using it consistently to create products thereafter. We can also swap entire families of products by replacing the concrete factory with an instance of a different one. The Abstract Factory pattern’s emphasis on families of products distinguishes it from other creational patterns, which involve only one kind of product object.

