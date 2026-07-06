# Can We Use an Abstract Factory? / Encapsulating Implementation Dependencies / Window and WindowImp / WindowImp Subclasses / Configuring Windows with WindowImps / Bridge Pattern

> Section: preface | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

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

![](images/fd74dfc2ad4a11e88e50bf81431cd4575a7cf82360036a99af52f120c139953e.jpg)

Now that we’ve defined a window interface for Lexi to work with, where does the real platform-specific window come in? If we’re not implementing our own window system, then at some point our window abstraction must be implemented in terms of what the target window system provides. So where does that implementation live?

One approach is to implement multiple versions of the Window class and its subclasses, one version for each windowing platform. We’d have to choose the version to use when we build Lexi for a given platform. But imagine the maintenance headaches we’d have keeping track of multiple classes, all named “Window” but each implemented on a different window system. Alternatively, we could create implementation-specific subclasses of each class in the Window hierarchy—and end up with another subclass explosion problem like the one we had trying to add embellishments. Both of these alternatives have another drawback: Neither gives us the flexibility to change the window system we use after we’ve compiled the program. So we’ll have to keep several different executables around as well.

Neither alternative is very appealing, but what else can we do? The same thing we did for formatting and embellishment, namely, encapsulate the concept that varies. What varies in this case is the window system implementation. If we encapsulate a window system’s functionality in an object, then we can implement our Window class and subclasses in terms of that object’s interface. Moreover, if that interface can serve all the window systems we’re interested in, then we won’t have to change Window or any of its subclasses to support different window systems. We can configure window objects to the window system we want simply by passing them the right window system-encapsulating object. We can even configure the window at run-time.

## Window and WindowImp

We’ll define a separate WindowImp class hierarchy in which to hide different window system implementations. WindowImp is an abstract class for objects that encapsulate window system-dependent code. To make Lexi work on a particular window system, we configure each window object with an instance of a WindowImp subclass for that system. The following diagram shows the relationship between the Window and WindowImp hierarchies:

![](images/8774f7d098fccc4be4db309d15b98cd0bd9f2fba62c947137c086794753ae97c.jpg)

By hiding the implementations in WindowImp classes, we avoid polluting the Window classes with window system dependencies, which keeps the Window class hierarchy comparatively small and stable. Meanwhile we can easily extend the implementation hierarchy to support new window systems.

## WindowImp Subclasses

Subclasses of WindowImp convert requests into window system-specific operations. Consider the example we used in Section 2.2. We defined the Rectangle::Draw in terms of the DrawRect operation on the Window instance:

void Rectangle::Draw (Window\* w) {   
w->DrawRect(\_x0, \_y0, \_x1, \_y1);

The default implementation of DrawRect uses the abstract operation for drawing rectangles declared by WindowImp:

void Window::DrawRect (   
Coord x0, Coord y0, Coord x1, Coord y1   
\_imp->DeviceRect(x0,y0,x1, y1);

where \_imp is a member variable of Window that stores the WindowImp with which the Window is configured. The window implementation is defined by the instance of the

WindowImp subclass that \_imp points to. For an XWindowImp (that is, a WindowImp subclass for the X Window System), the DeviceRect’s implementation might look like

void XWindowImp::DeviceRect (   
Coord x0, Coord y0,Coord x1, Coord y1   
int x = round(min(x0, x1));   
int y = round(min(y0, y1));   
int w = round(abs(x0 - x1));   
int h = round(abs(y0 - y1));   
xDrawRectangle(\_dpy, \_winid, \_gc, x, y, w, h);

DeviceRect is defined like this because XDrawRectangle (the X interface for drawing a rectangle) defines a rectangle in terms of its lower left corner, its width, and its height. DeviceRect must compute these values from those supplied. First it ascertains the lower left corner (since (x0, y0) might be any one of the rectangle’s four corners) and then calculates the width and height.

PMWindowImp (a subclass of WindowImp for Presentation Manager) would define DeviceRect differently:

void PMWindowImp::DeviceRect (   
Coord x0, Coord y0, Coord x1, Coord y1   
Coord left = min(x0, x1);   
Coord right = max(x0, x1);   
Coord bottom = min(y0, y1);   
Coord top = max(y0, y1);   
PPOINTL point [4];   
point[0].x = left; point[0].y = top;   
point[1].x = right; point [1].y = top;   
point[2].x = right; point [2].y = bottom;   
point[3].x = left; point[3].y = bottom;   
if (   
(GpiBeginPath(\_hps, 1L) == false) 11   
(GpiSetCurrentPosition(\_hps, &point[3])==false)11   
(GpiPolyLine(\_hps, 4L, point) ==GPI\_ERROR)I1   
(GpiEndPath(\_hps)== false)   
// report error   
} else {   
GpiStrokePath(\_hps, 1L, 0L);   
}

Why is this so different from the X version? Well, PM doesn’t have an operation for drawing rectangles explicitly as X does. Instead, PM has a more general interface for specifying vertices of multisegment shapes (called a path) and for outlining or filling the area they enclose.

PM’s implementation of DeviceRect is obviously quite different from X’s, but that doesn’t matter. WindowImp hides variations in window system interfaces behind a potentially large but stable interface. That lets Window subclass writers focus on the window abstraction and not on window system details. It also lets us add support for new window systems without disturbing the Window classes.

## Configuring Windows with WindowImps

A key issue we haven’t addressed is how a window gets configured with the proper WindowImp subclass in the first place. Stated another way, when does \_imp get initialized, and who knows what window system (and consequently which WindowImp subclass) is in use? The window will need some kind of WindowImp before it can do anything interesting.

There are several possibilities, but we’ll focus on one that uses the Abstract Factory (87) pattern. We can define an abstract factory class WindowSystemFactory that provides an interface for creating different kinds of window system-dependent implementation objects:

class WindowSystemFactory {   
public:   
virtual WindowImp\*CreateWindowImp() = 0;   
virtual ColorImp\* CreateColorImp() = 0;   
virtual FontImp\* CreateFontImp()= 0;   
//a"Create..."operation for all window system resources

Now we can define a concrete factory for each window system:

class PMWindowSystemFactory: public WindowSystemFactory{   
virtual WindowImp\*CreateWindowImp()   
{ return new PMWindowImp; }   
class XWindowSystemFactory : public WindowSystemFactory {   
virtual WindowImp\* CreateWindowImp()   
{ return new XWindowImp; }

The Window base class constructor can use the WindowSystemFactory interface to initialize the \_imp member with the WindowImp that’s right for the window system:

Window::Window () {   
\_imp = windowSystemFactory->CreateWindowImp();

T h e windowSystemFactory variable is a well-known instance of a WindowSystemFactory subclass, akin to the well-known guiFactory variable defining the look and feel. The windowSystemFactory variable can be initialized in the same way.

## Bridge Pattern

The WindowImp class defines an interface to common window system facilities, but its design is driven by different constraints than Window’s interface. Application programmers won’t deal with WindowImp’s interface directly; they only deal with Window objects. So WindowImp’s interface needn’t match the application programmer’s view of the world, as was our concern in the design of the Window class hierarchy and interface. WindowImp’s interface can more closely reflect what window systems actually provide, warts and all. It can be biased toward either an intersection or a union of functionality approach, whichever suits the target window systems best.

The important thing to realize is that Window’s interface caters to the applications programmer, while WindowImp caters to window systems. Separating windowing functionality into Window and WindowImp hierarchies lets us implement and specialize these interfaces independently. Objects from these hierarchies cooperate to let Lexi work without modification on multiple window systems.

The relationship between Window and WindowImp is an example of the Bridge (151) pattern. The intent behind Bridge is to allow separate class hierarchies to work together even as they evolve independently. Our design criteria led us to create two separate class hierarchies, one that supports the logical notion of windows, and another for capturing different implementations of windows. The Bridge pattern lets us maintain and enhance our logical windowing abstractions without touching window system-dependent code, and vice versa.

