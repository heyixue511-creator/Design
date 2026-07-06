# Transparent Enclosure / Monoglyph / Decorator Pattern

> Section: preface | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

## Transparent Enclosure

From a programming point of view, embellishing the user interface involves extending existing code. Using inheritance to do such extension precludes rearranging embellishments at run-time, but an equally serious problem is the explosion of classes that can result from an inheritance-based approach.

We could add a border to Composition by subclassing it to yield a BorderedComposition class. Or we could add a scrolling interface in the same way to yield a Scrollable-Composition. If we want both scroll bars and a border, we might produce a Bordered-ScrollableComposition, and so forth. In the extreme, we end up with a class for every possible combination of embellishments, a solution that quickly becomes unworkable as the variety of embellishments grows.

Object composition offers a potentially more workable and flexible extension mechanism. But what objects do we compose? Since we know we’re embellishing an existing glyph, we could make the embellishment itself an object (say, an instance of class Border). That gives us two candidates for composition, the glyph and the border. The next step is to decide who composes whom. We could have the border contain the glyph, which makes sense given that the border will surround the glyph on the screen. Or we could do the opposite—put the border into the glyph—but then we must make modifications to the corresponding Glyph subclass to make it aware of the border. Our first choice, composing the glyph in the border, keeps the border-drawing code entirely in the Border class, leaving other classes alone.

What does the Border class look like? The fact that borders have an appearance suggests they should actually be glyphs; that is, Border should be a subclass of Glyph. But there’s a more compelling reason for doing this: Clients shouldn’t care whether glyphs have borders or not. They should treat glyphs uniformly. When clients tell a plain, unbordered glyph to draw itself, it should do so without embellishment. If that glyph is composed in a border, clients shouldn’t have to treat the border containing the glyph any differently; they just tell it to draw itself as they told the plain glyph before. This implies that the Border interface matches the Glyph interface. We subclass Border from Glyph to guarantee this relationship.

All this leads us to the concept of transparent enclosure, which combines the notions of (1) single-child (or single-component) composition and (2) compatible interfaces. Clients generally can’t tell whether they’re dealing with the component or its enclosure (i.e., the child’s parent), especially if the enclosure simply delegates all its operations to its component. But the enclosure can also augment the component’s behavior by doing work of its own before and/or after delegating an operation. The enclosure can also effectively add state to the component. We’ll see how next.

## Monoglyph

We can apply the concept of transparent enclosure to all glyphs that embellish other glyphs. To make this concept concrete, we’ll define a subclass of Glyph called MonoGlyph to serve as an abstract class for “embellishment glyphs,” like Border (see Figure 2.7). MonoGlyph stores a reference to a component and forwards all requests to it.

Figure 2.7: MonoGlyph class relationships  
![](images/96d8d524b94190c1b45677c6be86dca15bd7361f28e504530729208973c05f05.jpg)

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
![](images/7b6701061ded5c3a07c534a8117372e82649cf5a837c8e1785cd9131be585b6f.jpg)  
Note that we can reverse the order of composition, putting the bordered composition

into the Scroller instance. In that case the border would be scrolled along with the text, which may or may not be desirable. The point is, transparent enclosure makes it easy to experiment with different alternatives, and it keeps clients free of embellishment code.

Note also how the border composes one glyph, not two or more. This is unlike compositions we’ve defined so far, in which parent objects were allowed to have arbitrarily many children. Here, putting a border around something implies that “something” is singular. We could assign a meaning to embellishing more than one object at a time, but then we’d have to mix many kinds of composition in with the notion of embellishment: row embellishment, column embellishment, and so forth. That won’t help us, since we already have classes to do those kinds of compositions. So it’s better to use existing classes for composition and add new classes to embellish the result. Keeping embellishment independent of other kinds of composition both simplifies the embellishment classes and reduces their number. It also keeps us from replicating existing composition functionality.

## Decorator Pattern

The Decorator (175) pattern captures class and object relationships that support embellishment by transparent enclosure. The term “embellishment” actually has broader meaning than what we’ve considered here. In the Decorator pattern, embellishment refers to anything that adds responsibilities to an object. We can think for example of embellishing an abstract syntax tree with semantic actions, a finite state automaton with new transitions, or a network of persistent objects with attribute tags. Decorator generalizes the approach we’ve used in Lexi to make it more widely applicable.

