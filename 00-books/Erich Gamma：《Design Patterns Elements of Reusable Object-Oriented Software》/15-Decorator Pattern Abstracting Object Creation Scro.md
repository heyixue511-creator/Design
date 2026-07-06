into the Scroller instance. In that case the border would be scrolled along with the text, which may or may not be desirable. The point is, transparent enclosure makes it easy to experiment with different alternatives, and it keeps clients free of embellishment code.

Note also how the border composes one glyph, not two or more. This is unlike compositions we’ve defined so far, in which parent objects were allowed to have arbitrarily many children. Here, putting a border around something implies that “something” is singular. We could assign a meaning to embellishing more than one object at a time, but then we’d have to mix many kinds of composition in with the notion of embellishment: row embellishment, column embellishment, and so forth. That won’t help us, since we already have classes to do those kinds of compositions. So it’s better to use existing classes for composition and add new classes to embellish the result. Keeping embellishment independent of other kinds of composition both simplifies the embellishment classes and reduces their number. It also keeps us from replicating existing composition functionality.

## Decorator Pattern

The Decorator (175) pattern captures class and object relationships that support embellishment by transparent enclosure. The term “embellishment” actually has broader meaning than what we’ve considered here. In the Decorator pattern, embellishment refers to anything that adds responsibilities to an object. We can think for example of embellishing an abstract syntax tree with semantic actions, a finite state automaton with new transitions, or a network of persistent objects with attribute tags. Decorator generalizes the approach we’ve used in Lexi to make it more widely applicable.

## 2.5 Supporting Multiple Look-and-Feel Standards

Achieving portability across hardware and software platforms is a major problem in system design. Retargeting Lexi to a new platform shouldn’t require a major overhaul, or it wouldn’t be worth retargeting. We should make porting as easy as possible.

One obstacle to portability is the diversity of look-and-feel standards, which are intended to enforce uniformity between applications. These standards define guidelines for how applications appear and react to the user. While existing standards aren’t that different from each other, people certainly won’t confuse one for the other—Motif applications don’t look and feel exactly like their counterparts on other platforms, and vice versa. An application that runs on more than one platform must conform to the user interface style guide on each platform.

Our design goals are to make Lexi conform to multiple existing look-and-feel standards and to make it easy to add support for new standards as they (invariably)

emerge. We also want our design to support the ultimate in flexibility: changing Lexi’s look and feel at run-time.

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
![](images/a2df13cf539ec46f446678ead2d9719cda0d41271ed7187ce2b3ceee6413668f.jpg)  
We say that factories create product objects. Moreover, the products that a factory

produces are related to one another; in this case, the products are all widgets for the same look and feel. Figure 2.10 shows some of the product classes needed to make factories work for widget glyphs.

Figure 2.10: Abstract product classes and concrete subclasses  
![](images/ec1c46dc2c2bc19609a4b3d8ee882f802efe4df4ba03869144abebe993d4ad68.jpg)

The last question we have to answer is, Where does the GUIFactory instance come from? The answer is, Anywhere that’s convenient. The variable guiFactory could be a global, a static member of a well-known class, or even a local variable if the entire user interface is created within one class or function. There’s even a design pattern, Singleton (127), for managing well-known, one-of-a-kind objects like this. The important thing, though, is to initialize guiFactory at a point in the program before it’s ever used to create widgets but after it’s clear which look and feel is desired.

If the look and feel is known at compile-time, then guiFactory can be initialized with a simple assignment of a new factory instance at the beginning of the program:

## GUIFactory\* guiFactory = new MotifFactory;

If the user can specify the look and feel with a string name at startup time, then the code to create the factory might be

GUIFactory\* guiFactory;   
constchar\*styleName= getenv("LOOK\_AND\_FEEL");   
//user or environment suppliesthisat startup   
if(strcmp(styleName, "Motif") ==0) {   
guiFactory= newMotifFactory:   
) else if (strcmp(styleName, "Presentation\_Manager") == 0) {   
guiFactory= newPMFactory;   
} else {   
guiFactory= new DefaultGUIFactory;