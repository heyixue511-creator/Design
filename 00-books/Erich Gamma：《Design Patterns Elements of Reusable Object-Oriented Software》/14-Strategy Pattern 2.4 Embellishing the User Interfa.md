![](images/32c7803ad046e6c59437626b4dc1d6cb67951ff8b6fce727ce1bd08364347571.jpg)

Each Compositor subclass can implement a different linebreaking algorithm. For example, a SimpleCompositor might do a quick pass without regard for such esoterica as the document’s “color.” Good color means having an even distribution of text and whitespace. A TeXCompositor would implement the full $\mathrm { T _ { E } X }$ algorithm [Knu84], which takes things like color into account in exchange for longer formatting times.

The Compositor-Composition class split ensures a strong separation between code that supports the document’s physical structure and the code for different formatting algorithms. We can add new Compositor subclasses without touching the glyph classes, and vice versa. In fact, we can change the linebreaking algorithm at run-time by adding a single SetCompositor operation to Composition’s basic glyph interface.

## Strategy Pattern

Encapsulating an algorithm in an object is the intent of the Strategy (315) pattern. The key participants in the pattern are Strategy objects (which encapsulate different algorithms) and the context in which they operate. Compositors are strategies; they encapsulate different formatting algorithms. A composition is the context for a compositor strategy.

The key to applying the Strategy pattern is designing interfaces for the strategy and its context that are general enough to support a range of algorithms. You shouldn’t have to change the strategy or context interface to support a new algorithm. In our example, the basic Glyph interface’s support for child access, insertion, and removal is general enough to let Compositor subclasses change the document’s physical structure, regardless of the algorithm they use to do it. Likewise, the Compositor interface gives compositions whatever they need to initiate formatting.

## 2.4 Embellishing the User Interface

We consider two embellishments in Lexi’s user interface. The first adds a border around the text editing area to demarcate the page of text. The second adds scroll bars that let the user view different parts of the page. To make it easy to add and remove these embellishments (especially at run-time), we shouldn’t use inheritance to add them to the user interface. We achieve the most flexibility if other user interface objects don’t even know the embellishments are there. That will let us add and remove the embellishments without changing other classes.

## Transparent Enclosure

From a programming point of view, embellishing the user interface involves extending existing code. Using inheritance to do such extension precludes rearranging embellishments at run-time, but an equally serious problem is the explosion of classes that can result from an inheritance-based approach.

We could add a border to Composition by subclassing it to yield a BorderedComposition class. Or we could add a scrolling interface in the same way to yield a Scrollable-Composition. If we want both scroll bars and a border, we might produce a Bordered-ScrollableComposition, and so forth. In the extreme, we end up with a class for every possible combination of embellishments, a solution that quickly becomes unworkable as the variety of embellishments grows.

Object composition offers a potentially more workable and flexible extension mechanism. But what objects do we compose? Since we know we’re embellishing an existing glyph, we could make the embellishment itself an object (say, an instance of class Border). That gives us two candidates for composition, the glyph and the border. The next step is to decide who composes whom. We could have the border contain the glyph, which makes sense given that the border will surround the glyph on the screen. Or we could do the opposite—put the border into the glyph—but then we must make modifications to the corresponding Glyph subclass to make it aware of the border. Our first choice, composing the glyph in the border, keeps the border-drawing code entirely in the Border class, leaving other classes alone.

What does the Border class look like? The fact that borders have an appearance suggests they should actually be glyphs; that is, Border should be a subclass of Glyph. But there’s a more compelling reason for doing this: Clients shouldn’t care whether glyphs have borders or not. They should treat glyphs uniformly. When clients tell a plain, unbordered glyph to draw itself, it should do so without embellishment. If that glyph is composed in a border, clients shouldn’t have to treat the border containing the glyph any differently; they just tell it to draw itself as they told the plain glyph before. This implies that the Border interface matches the Glyph interface. We subclass Border from Glyph to guarantee this relationship.

All this leads us to the concept of transparent enclosure, which combines the notions of (1) single-child (or single-component) composition and (2) compatible interfaces. Clients generally can’t tell whether they’re dealing with the component or its enclosure (i.e., the child’s parent), especially if the enclosure simply delegates all its operations to its component. But the enclosure can also augment the component’s behavior by doing work of its own before and/or after delegating an operation. The enclosure can also effectively add state to the component. We’ll see how next.

## Monoglyph

We can apply the concept of transparent enclosure to all glyphs that embellish other glyphs. To make this concept concrete, we’ll define a subclass of Glyph called MonoGlyph to serve as an abstract class for “embellishment glyphs,” like Border (see Figure 2.7). MonoGlyph stores a reference to a component and forwards all requests to it.

Figure 2.7: MonoGlyph class relationships  
![](images/5fea5c50a45a8631e77d8e6caadcf91a9e9f9f2007625817d30412b32de99f00.jpg)

That makes MonoGlyph totally transparent to clients by default. For example, MonoGlyph implements the Draw operation like this:

void MonoGlyph::Draw (Window\* w) {   
\_component->Draw(w);

MonoGlyph subclasses reimplement at least one of these forwarding operations. Border::Draw, for instance, first invokes the parent class operation MonoGlyph::Draw on the component to let the component do its part—that is, draw everything but the border. Then Border::Draw draws the border by calling a private operation called DrawBorder, the details of which we’ll omit:

void Border::Draw (Window\* w) (   
MonoGlyph::Draw(w);   
DrawBorder(w);

Notice how Border::Draw effectively extends the parent class operation to draw the border. This is in contrast to merely replacing the parent class operation, which would omit the call to MonoGlyph::Draw.

Another MonoGlyph subclass appears in Figure 2.7. Scroller is a MonoGlyph that draws its component in different locations based on the positions of two scroll bars, which it adds as embellishments. When Scroller draws its component, it tells the graphics system to clip to its bounds. Clipping parts of the component that are scrolled out of view keeps them from appearing on the screen.

Now we have all the pieces we need to add a border and a scrolling interface to Lexi’s text editing area. We compose the existing Composition instance in a Scroller instance to add the scrolling interface, and we compose that in a Border instance. The resulting object structure appears in Figure 2.8.

Figure 2.8: Embellished object structure  
![](images/3b9d95ffc09fd52cbe3981b7f344430e7d889d61bb9af67498d9795544ffc7b0.jpg)  
Note that we can reverse the order of composition, putting the bordered composition