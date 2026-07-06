There are more sophisticated ways to select the factory at run-time. For example, you could maintain a registry that maps strings to factory objects. That lets you register instances of new factory subclasses without modifying existing code, as the preceding approach requires. And you don’t have to link all platform-specific factories into the application. That’s important, because it might not be possible to link a MotifFactory on a platform that doesn’t support Motif.

But the point is that once we’ve configured the application with the right factory object, its look and feel is set from then on. If we change our minds, we can reinitialize guiFactory with a factory for a different look and feel and then reconstruct the interface. Regardless of how and when we decide to initialize guiFactory, we know that once we do, the application can create the appropriate look and feel without modification.

## Abstract Factory Pattern

Factories and products are the key participants in the Abstract Factory (87) pattern. This pattern captures how to create families of related product objects without instantiating classes directly. It’s most appropriate when the number and general kinds of product objects stay constant, and there are differences in specific product families. We choose between families by instantiating a particular concrete factory and using it consistently to create products thereafter. We can also swap entire families of products by replacing the concrete factory with an instance of a different one. The Abstract Factory pattern’s emphasis on families of products distinguishes it from other creational patterns, which involve only one kind of product object.

## 2.6 Supporting Multiple Window Systems

Look and feel is just one of many portability issues. Another is the windowing environment in which Lexi runs. A platform’s window system creates the illusion of multiple overlapping windows on a bitmapped display. It manages screen space for windows and routes input to them from the keyboard and mouse. Several important and largely incompatible window systems exist today (e.g., Macintosh, Presentation Manager, Windows, X). We’d like Lexi to run on as many of them as possible for exactly the same reasons we support multiple look-and-feel standards.

## Can We Use an Abstract Factory?

At first glance this may look like another opportunity to apply the Abstract Factory pattern. But the constraints for window system portability differ significantly from those for look-and-feel independence.

In applying the Abstract Factory pattern, we assumed we would define the concrete widget glyph classes for each look-and-feel standard. That meant we could derive each concrete product for a particular standard (e.g., MotifScrollBar and MacScrollBar) from an abstract product class (e.g., ScrollBar). But suppose we already have several class hierarchies from different vendors, one for each look-and-feel standard. Of course, it’s highly unlikely these hierarchies are compatible in any way. Hence we won’t have a common abstract product class for each kind of widget (ScrollBar, Button, Menu, etc.)— and the Abstract Factory pattern won’t work without those crucial classes. We have to make the different widget hierarchies adhere to a common set of abstract product interfaces. Only then could we declare the Create. . . operations properly in our abstract factory’s interface.

We solved this problem for widgets by developing our own abstract and concrete product classes. Now we’re faced with a similar problem when we try to make Lexi work on existing window systems; namely, different window systems have incompatible programming interfaces. Things are a bit tougher this time, though, because we can’t afford to implement our own nonstandard window system.

But there’s a saving grace. Like look-and-feel standards, window system interfaces aren’t radically different from one another, because all window systems do generally the same thing. We need a uniform set of windowing abstractions that lets us take different window system implementations and slide any one of them under a common interface.

## Encapsulating Implementation Dependencies

In Section 2.2 we introduced a Window class for displaying a glyph or glyph structure on the display. We didn’t specify the window system that this object worked with, because the truth is that it doesn’t come from any particular window system. The Window class encapsulates the things windows tend to do across window systems:

• They provide operations for drawing basic geometric shapes.

• They can iconify and de-iconify themselves.

• They can resize themselves.

• They can (re)draw their contents on demand, for example, when they are deiconified or when an overlapped and obscured portion of their screen space is exposed.

The Window class must span the functionality of windows from different window systems. Let’s consider two extreme philosophies:

1 . Intersection of functionality. The Window class interface provides only functionality that’s common to all window systems. The problem with this approach is that our Window interface winds up being only as powerful as the least capable window system. We can’t take advantage of more advanced features even if most (but not all) window systems support them.

2. Union of functionality. Create an interface that incorporates the capabilities of all existing systems. The trouble here is that the resulting interface may well be huge and incoherent. Besides, we’ll have to change it (and Lexi, which depends on it) anytime a vendor revises its window system interface.

Neither extreme is a viable solution, so our design will fall somewhere between the two. The Window class will provide a convenient interface that supports the most popular windowing features. Because Lexi will deal with this class directly, the Window class must also support the things Lexi knows about, namely, glyphs. That means Window’s interface must include a basic set of graphics operations that lets glyphs draw themselves in the window. Table 2.3 gives a sampling of the operations in the Window class interface.

Table 2.3: Window class interface
<table><tr><td rowspan=1 colspan=1>Responsibility</td><td rowspan=1 colspan=1>Operations</td></tr><tr><td rowspan=1 colspan=1>window management</td><td rowspan=1 colspan=1>virtual void Redraw()virtual void Raise()virtual void Lower()virtual void Iconify()virtual void Deiconify()...</td></tr><tr><td rowspan=1 colspan=1>graphics</td><td rowspan=1 colspan=1>virtual void DrawLine(...)virtual void DrawRect(...)virtual void DrawPolygon(...)virtual void DrawText(...)</td></tr></table>

Window is an abstract class. Concrete subclasses of Window support the different kinds of windows that users deal with. For example, application windows, icons, and warning dialogs are all windows, but they have somewhat different behaviors. So we can define subclasses like ApplicationWindow, Icon Window, and DialogWindow to capture these differences. The resulting class hierarchy gives applications like Lexi a uniform and intuitive windowing abstraction, one that doesn’t depend on any particular vendor’s window system:

![](images/f3ac3f905f01e15e6752d957acc2adfbdb506b13a13b7663404761a2c9147e20.jpg)

Now that we’ve defined a window interface for Lexi to work with, where does the real platform-specific window come in? If we’re not implementing our own window system, then at some point our window abstraction must be implemented in terms of what the target window system provides. So where does that implementation live?

One approach is to implement multiple versions of the Window class and its subclasses, one version for each windowing platform. We’d have to choose the version to use when we build Lexi for a given platform. But imagine the maintenance headaches we’d have keeping track of multiple classes, all named “Window” but each implemented on a different window system. Alternatively, we could create implementation-specific subclasses of each class in the Window hierarchy—and end up with another subclass explosion problem like the one we had trying to add embellishments. Both of these alternatives have another drawback: Neither gives us the flexibility to change the window system we use after we’ve compiled the program. So we’ll have to keep several different executables around as well.

Neither alternative is very appealing, but what else can we do? The same thing we did for formatting and embellishment, namely, encapsulate the concept that varies. What varies in this case is the window system implementation. If we encapsulate a window system’s functionality in an object, then we can implement our Window class and subclasses in terms of that object’s interface. Moreover, if that interface can serve all the window systems we’re interested in, then we won’t have to change Window or any of its subclasses to support different window systems. We can configure window objects to the window system we want simply by passing them the right window system-encapsulating object. We can even configure the window at run-time.

## Window and WindowImp

We’ll define a separate WindowImp class hierarchy in which to hide different