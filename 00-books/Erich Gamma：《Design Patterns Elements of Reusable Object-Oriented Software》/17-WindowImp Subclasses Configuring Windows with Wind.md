window system implementations. WindowImp is an abstract class for objects that encapsulate window system-dependent code. To make Lexi work on a particular window system, we configure each window object with an instance of a WindowImp subclass for that system. The following diagram shows the relationship between the Window and WindowImp hierarchies:

![](images/61ce37e415832d77eba92dcfef512bfea2d6873f93a3423c99473fa2e3cfb9dc.jpg)

By hiding the implementations in WindowImp classes, we avoid polluting the Window classes with window system dependencies, which keeps the Window class hierarchy comparatively small and stable. Meanwhile we can easily extend the implementation hierarchy to support new window systems.

## WindowImp Subclasses

Subclasses of WindowImp convert requests into window system-specific operations. Consider the example we used in Section 2.2. We defined the Rectangle::Draw in terms of the DrawRect operation on the Window instance:

void Rectangle::Draw (Window\* w) {   
w->DrawRect(\_x0, \_y0, \_x1, \_y1);

The default implementation of DrawRect uses the abstract operation for drawing rectangles declared by WindowImp:

void Window::DrawRect (   
Coord x0, Coord y0, Coord x1, Coord y1   
\_imp->DeviceRect(x0,y0,x1,y1);

where \_imp is a member variable of Window that stores the WindowImp with which the Window is configured. The window implementation is defined by the instance of the

WindowImp subclass that \_imp points to. For an XWindowImp (that is, a WindowImp subclass for the X Window System), the DeviceRect’s implementation might look like

void XWindowImp::DeviceRect(   
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
point[3].x = left; point[3].y= bottom;   
if (   
(GpiBeginPath(\_hps, 1L) == false) 11   
(GpiSetCurrentPosition(\_hps,&point[3])==false)11   
(GpiPolyLine(\_hps, 4L, point) ==GPI\_ERROR)I1   
(GpiEndPath(\_hps)== false)   
// report error   
} else {   
GpiStrokePath(\_hps, 1L, OL);   
}

Why is this so different from the X version? Well, PM doesn’t have an operation for drawing rectangles explicitly as X does. Instead, PM has a more general interface for specifying vertices of multisegment shapes (called a path) and for outlining or filling the area they enclose.

PM’s implementation of DeviceRect is obviously quite different from X’s, but that doesn’t matter. WindowImp hides variations in window system interfaces behind a potentially large but stable interface. That lets Window subclass writers focus on the window abstraction and not on window system details. It also lets us add support for new window systems without disturbing the Window classes.

## Configuring Windows with WindowImps

A key issue we haven’t addressed is how a window gets configured with the proper WindowImp subclass in the first place. Stated another way, when does \_imp get initialized, and who knows what window system (and consequently which WindowImp subclass) is in use? The window will need some kind of WindowImp before it can do anything interesting.

There are several possibilities, but we’ll focus on one that uses the Abstract Factory (87) pattern. We can define an abstract factory class WindowSystemFactory that provides an interface for creating different kinds of window system-dependent implementation objects:

class WindowSystemFactory {   
public:   
virtualWindowImp\*CreateWindowImp() = 0;   
virtual ColorImp\* CreateColorImp() = 0;   
virtual FontImp\* CreateFontImp()= 0;   
//a"Create..."operation for all window system resources

Now we can define a concrete factory for each window system:

class PMWindowSystemFactory: public WindowSystemFactory{   
virtual WindowImp\*CreateWindowImp()   
{ return new PMWindowImp;}   
class XWindowSystemFactory : public WindowSystemFactory {   
virtual WindowImp\* CreateWindowImp()   
{ return new XWindowImp; }

The Window base class constructor can use the WindowSystemFactory interface to initialize the \_imp member with the WindowImp that’s right for the window system:

Window::Window () {   
\_imp= windowSystemFactory->CreateWindowImp();

T h e windowSystemFactory variable is a well-known instance of a WindowSystemFactory subclass, akin to the well-known guiFactory variable defining the look and feel. The windowSystemFactory variable can be initialized in the same way.

## Bridge Pattern

The WindowImp class defines an interface to common window system facilities, but its design is driven by different constraints than Window’s interface. Application programmers won’t deal with WindowImp’s interface directly; they only deal with Window objects. So WindowImp’s interface needn’t match the application programmer’s view of the world, as was our concern in the design of the Window class hierarchy and interface. WindowImp’s interface can more closely reflect what window systems actually provide, warts and all. It can be biased toward either an intersection or a union of functionality approach, whichever suits the target window systems best.

The important thing to realize is that Window’s interface caters to the applications programmer, while WindowImp caters to window systems. Separating windowing functionality into Window and WindowImp hierarchies lets us implement and specialize these interfaces independently. Objects from these hierarchies cooperate to let Lexi work without modification on multiple window systems.

The relationship between Window and WindowImp is an example of the Bridge (151) pattern. The intent behind Bridge is to allow separate class hierarchies to work together even as they evolve independently. Our design criteria led us to create two separate class hierarchies, one that supports the logical notion of windows, and another for capturing different implementations of windows. The Bridge pattern lets us maintain and enhance our logical windowing abstractions without touching window system-dependent code, and vice versa.

## 2.7 User Operations

Some of Lexi’s functionality is available through the document’s WYSIWYG representation. You enter and delete text, move the insertion point, and select ranges of text by pointing, clicking, and typing directly in the document. Other functionality is accessed indirectly through user operations in Lexi’s pull-down menus, buttons, and keyboard accelerators. The functionality includes operations for

• creating a new document,