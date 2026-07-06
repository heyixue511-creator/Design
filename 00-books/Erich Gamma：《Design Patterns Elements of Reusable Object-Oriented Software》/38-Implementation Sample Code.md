The Bridge pattern has the following consequences:

1. Decoupling interface and implementation. An implementation is not bound permanently to an interface. The implementation of an abstraction can be configured at run-time. It’s even possible for an object to change its implementation at run-time.

Decoupling Abstraction and Implementor also eliminates compile-time dependencies on the implementation. Changing an implementation class doesn’t require recompiling the Abstraction class and its clients. This property is essential when you must ensure binary compatibility between different versions of a class library.

Furthermore, this decoupling encourages layering that can lead to a betterstructured system. The high-level part of a system only has to know about Abstraction and Implementor.

2 . Improved extensibility. You can extend the Abstraction and Implementor hierarchies independently.

3 . Hiding implementation details from clients. You can shield clients from implementation details, like the sharing of implementor objects and the accompanying reference count mechanism (if any).

## Implementation

Consider the following implementation issues when applying the Bridge pattern:

1. Only one Implementor. In situations where there’s only one implementation, creating an abstract Implementor class isn’t necessary. This is a degenerate case of the Bridge pattern; there’s a one-to-one relationship between Abstraction and Implementor. Nevertheless, this separation is still useful when a change in the implementation of a class must not affect its existing clients—that is, they shouldn’t have to be recompiled, just relinked.

Carolan [Car89] uses the term “Cheshire Cat” to describe this separation. In C++, the class interface of the Implementor class can be defined in a private header file that isn’t provided to clients. This lets you hide an implementation of a class completely from its clients.

2. Creating the right Implementor object. How, when, and where do you decide which Implementor class to instantiate when there’s more than one?

If Abstraction knows about all ConcreteImplementor classes, then it can instantiate one of them in its constructor; it can decide between them based on parameters passed to its constructor. If, for example, a collection class supports multiple implementations, the decision can be based on the size of the collection. A linked list implementation can be used for small collections and a hash table for larger ones.

Another approach is to choose a default implementation initially and change it later according to usage. For example, if the collection grows bigger than a certain threshold, then it switches its implementation to one that’s more appropriate for a large number of items.

It’s also possible to delegate the decision to another object altogether. In the Window/WindowImp example, we can introduce a factory object (see Abstract Factory (87)) whose sole duty is to encapsulate platform-specifics. The factory knows what kind of WindowImp object to create for the platform in use; a Window simply asks it for a WindowImp, and it returns the right kind. A benefit of this approach is that Abstraction is not coupled directly to any of the Implementor classes.

3. Sharing implementors. Coplien illustrates how the Handle/Body idiom in C++ can be used to share implementations among several objects [Cop92]. The Body stores a reference count that the Handle class increments and decrements. The code for assigning handles with shared bodies has the following general form:

Handle& Handle::operator= (const Handle& other) {   
other.\_body->Ref();   
\_body->Unref();   
if (\_body->RefCount() == 0) {   
delete \_body;   
)   
\_body = other.\_body;   
return \*this;   
}

4 . Using multiple inheritance. You can use multiple inheritance in C++ to combine an interface with its implementation [Mar91]. For example, a class can inherit publicly from Abstraction and privately from a ConcreteImplementor. But because this approach relies on static inheritance, it binds an implementation permanently to its interface. Therefore you can’t implement a true Bridge with multiple inheritance—at least not in C++.

## Sample Code

The following C++ code implements the Window/WindowImp example from the Motivation section. The Window class defines the window abstraction for client applications:

class Window {  
public:  
Window(View\* contents);  
// requests handled by window  
virtual void DrawContents();  
virtual void Open();  
virtual voidClose();  
virtual void Iconify();  
virtual void Deiconify();  
// requests forwarded to implementation  
virtual void SetOrigin(const Point& at);  
virtual void SetExtent(const Point& extent);  
virtual void Raise();  
virtual void Lower();  
virtual void DrawLine(const Point&, const Point&);  
virtual void DrawRect(const Point&, constPoint&);  
virtual void DrawPolygon(const Point[l, int n);  
virtual void DrawText(const char\*, const Point&);  
protected:  
WindowImp\*GetWindowImp();  
View\* GetView();  
private:  
WindowImp\*\_imp;  
View\* \_contents; // the window's contents

Window maintains a reference to a WindowImp, the abstract class that declares an interface to the underlying windowing system.

class WindowImp (   
public:   
virtual void ImpTop() = 0;   
virtual void ImpBottom() = 0;   
virtual void ImpSetExtent(const Point&) = 0;   
virtual void ImpSetOrigin(const Point&) = 0;   
virtual void DeviceRect(Coord, Coord, Coord, Coord) = 0;   
virtual void DeviceText(const char\*, Coord, Coord) = 0;   
virtual void DeviceBitmap(const char\*, Coord, Coord) = 0;   
// lots more functions for drawing on windows...   
protected:   
WindowImp();

Subclasses of Window define the different kinds of windows the application might use, such as application windows, icons, transient windows for dialogs, floating palettes of tools, and so on.

For example, ApplicationWindow will implement DrawContents to draw the View instance it stores:

class ApplicationWindow : public Window {   
public:   
virtual void DrawContents();   
void ApplicationWindow::DrawContents(){   
GetView()->DrawOn(this);

IconWindow stores the name of a bitmap for the icon it displays...

class IconWindow : public Window {   
public:   
virtual void DrawContents();   
private:   
const char\* \_bitmapName;   
);

...and it implements DrawContents to draw the bitmap on the window:

void IconWindow::DrawContents() {   
WindowImp\* imp = GetWindowImp();   
if (imp != 0) (   
imp->DeviceBitmap(\_bitmapName, 0.0,0.0);   
)

Many other variations of Window are possible. A TransientWindow may need to communicate with the window that created it during the dialog; hence it keeps a reference to that window. A PaletteWindow always floats above other windows. An IconDockWindow holds IconWindows and arranges them neatly.

Window operations are defined in terms of the WindowImp interface. For example, DrawRect extracts four coordinates from its two Point parameters before calling the WindowImp operation that draws the rectangle in the window:

void Window::DrawRect (const Point& pl, const Point& p2) {   
WindowImp\* imp = GetWindowImp();   
imp->DeviceRect(p1.X(), p1.Y(), p2.X(), p2.Y());   
1

Concrete subclasses of WindowImp support different window systems. The XWindowImp subclass supports the X Window System:

class XWindowImp : public WindowImp {   
public:   
XwindowImp();   
virtual void DeviceRect(Coord, Coord, Coord, Coord);   
// remainder of public interface...   
private:   
// lots of X window system-specific state, including:   
Display\* \_dpy;   
Drawable \_winid; // window id   
GC \_gc; // window graphic context   
};

For Presentation Manager (PM), we define a PMWindowImp class:

class PMWindowImp : public WindowImp {   
public:   
PMWindowImp();   
virtualvoid DeviceRect(Coord, Coord, Coord, Coord);   
// remainder of public interface...   
private:   
// lots of PM window system-specific state, including:   
HPS \_hps;   
};

These subclasses implement WindowImp operations in terms of window system primitives. For example, DeviceRect is implemented for X as follows:

void XWindowImp::DeviceRect (   
Coord x0, Coord y0, Coord x1, Coord y1   
int x = round(min(x0, x1));   
int y = round(min(y0, y1));   
int w = round(abs(x0 - x1));   
int h = round(abs(y0 - y1));   
xDrawRectangle(\_dpy, \_winid, \_gc, x, y, w, h);   
}

The PM implementation might look like this: