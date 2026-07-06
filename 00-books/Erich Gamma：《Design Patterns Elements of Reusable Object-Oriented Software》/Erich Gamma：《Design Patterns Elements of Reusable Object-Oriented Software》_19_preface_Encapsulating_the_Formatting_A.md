# Encapsulating the Formatting Algorithm / Compositor and Composition / Strategy Pattern

> Section: preface | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

## Encapsulating the Formatting Algorithm

The formatting process, with all its constraints and details, isn’t easy to automate. There are many approaches to the problem, and people have come up with a variety of formatting algorithms with different strengths and weaknesses. Because Lexi is a WYSIWYG editor, an important trade-off to consider is the balance between formatting quality and formatting speed. We want generally good response from the editor without sacrificing how good the document looks. This trade-off is subject to many factors, not all of which can be ascertained at compile-time. For example, the user might tolerate slightly slower response in exchange for better formatting. That trade-off might make an entirely different formatting algorithm more appropriate than the current one. Another, more implementation-driven trade-off balances formatting speed and storage requirements: It may be possible to decrease formatting time by caching more information.

Because formatting algorithms tend to be complex, it’s also desirable to keep them well-contained or—better yet—completely independent of the document structure. Ideally we could add a new kind of Glyph subclass without regard to the formatting algorithm. Conversely, adding a new formatting algorithm shouldn’t require modifying existing glyphs.

These characteristics suggest we should design Lexi so that it’s easy to change the formatting algorithm at least at compile-time, if not at run-time as well. We can isolate the algorithm and make it easily replaceable at the same time by encapsulating it in an object. More specifically, we’ll define a separate class hierarchy for objects that encapsulate formatting algorithms. The root of the hierarchy will define an interface that supports a wide range of formatting algorithms, and each subclass will implement the interface to carry out a particular algorithm. Then we can introduce a Glyph subclass that will structure its children automatically using a given algorithm object.

## Compositor and Composition

We’ll define a Compositor class for objects that can encapsulate a formatting algorithm. The interface (Table 2.2) lets the compositor know what glyphs to format and when to do the formatting. The glyphs it formats are the children of a special Glyph subclass called Composition. A composition gets an instance of a Compositor subclass (specialized for a particular linebreaking algorithm) when it is created, and it tells the compositor to Compose its glyphs when necessary, for example, when the user changes a document. Figure 2.5 depicts the relationships between the Composition and Compositor classes.

Table 2.2: Basic compositor interface
<table><tr><td rowspan=1 colspan=1>Responsibility</td><td rowspan=1 colspan=1>Operations</td></tr><tr><td rowspan=1 colspan=1>what to format</td><td rowspan=1 colspan=1>void SetComposition(Composition*)</td></tr><tr><td rowspan=1 colspan=1>when to format</td><td rowspan=1 colspan=1>virtual void Compose()</td></tr></table>

Figure 2.5: Composition and Compositor class relationships  
![](images/5d53b72a913cbb6aa27b020794344a65ae021a677506d99719655ba8b6dcc55a.jpg)

An unformatted Composition object contains only the visible glyphs that make up the document’s basic content. It doesn’t contain glyphs that determine the document’s physical structure, such as Row and Column. The composition is in this state just after it’s created and initialized with the glyphs it should format. When the composition needs formatting, it calls its compositor’s Compose operation. The compositor in turn iterates through the composition’s children and inserts new Row and Column glyphs according to its linebreaking algorithm.<sup>7</sup> Figure 2.6 shows the resulting object structure. Glyphs that the compositor created and inserted into the object structure appear with gray backgrounds in the figure.

Figure 2.6: Object structure reflecting compositor-directed linebreaking

![](images/db250008257ba4de1f03a98d84515864fee498edda0d2a509a8df90e0b668468.jpg)

Each Compositor subclass can implement a different linebreaking algorithm. For example, a SimpleCompositor might do a quick pass without regard for such esoterica as the document’s “color.” Good color means having an even distribution of text and whitespace. A TeXCompositor would implement the full $\mathrm { T _ { E } X }$ algorithm [Knu84], which takes things like color into account in exchange for longer formatting times.

The Compositor-Composition class split ensures a strong separation between code that supports the document’s physical structure and the code for different formatting algorithms. We can add new Compositor subclasses without touching the glyph classes, and vice versa. In fact, we can change the linebreaking algorithm at run-time by adding a single SetCompositor operation to Composition’s basic glyph interface.

## Strategy Pattern

Encapsulating an algorithm in an object is the intent of the Strategy (315) pattern. The key participants in the pattern are Strategy objects (which encapsulate different algorithms) and the context in which they operate. Compositors are strategies; they encapsulate different formatting algorithms. A composition is the context for a compositor strategy.

The key to applying the Strategy pattern is designing interfaces for the strategy and its context that are general enough to support a range of algorithms. You shouldn’t have to change the strategy or context interface to support a new algorithm. In our example, the basic Glyph interface’s support for child access, insertion, and removal is general enough to let Compositor subclasses change the document’s physical structure, regardless of the algorithm they use to do it. Likewise, the Compositor interface gives compositions whatever they need to initiate formatting.

