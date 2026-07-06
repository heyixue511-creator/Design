void PMWindowImp::DeviceRect (   
Coord x0, Coord y0, Coord x1, Coord y1   
Coord left = min(x0, x1);   
Coord right = max(x0, x1);   
Coord bottom = min(y0, y1);   
Coord top = max(y0, y1);   
PPOINTL point[4];   
point[0].x = left; point[0].y = top;   
point[1].x = right; point[1].y = top;   
point[2].x = right; point[2].y = bottom;   
point[3].x = left; point[3].y = bottom;   
if (   
(GpiBeginPath(\_hps, 1L) == false)||   
(GpiSetCurrentPosition(\_hps, &point[3]) == false)||   
(GpiPolyLine(\_hps, 4L, point) ==GPI\_ERROR)   
(GpiEndPath(\_hps) == false)   
// report error   
} else {   
GpiStrokePath(\_hps, 1L, 0L);   
}   
一

How does a window obtain an instance of the right WindowImp subclass? We’ll assume Window has that responsibility in this example. Its GetWindowImp operation gets the right instance from an abstract factory (see Abstract Factory (87)) that effectively encapsulates all window system specifics.

WindowImp\* Window::GetWindowImp () {   
if (\_imp == 0) {   
\_imp=WindowSystemFactory::Instance()->MakeWindowImp();   
}   
return \_imp;   
}

WindowSystemFactory::Instance() returns an abstract factory that manufactures all window system-specific objects. For simplicity, we’ve made it a Singleton (127) and have let the Window class access the factory directly.

## Known Uses

The Window example above comes from ET++ [WGM88]. In ET++, WindowImp is called “WindowPort” and has subclasses such as XWindowPort and SunWindowPort. The Window object creates its corresponding Implementor object by requesting it from an abstract factory called “WindowSystem.” WindowSystem provides an interface for creating platform-specific objects such as fonts, cursors, bitmaps, and so forth.

The ET++ Window/WindowPort design extends the Bridge pattern in that the WindowPort also keeps a reference back to the Window. The WindowPort implementor class uses this reference to notify Window about WindowPort-specific events: the arrival of input events, window resizes, etc.

Both Coplien [Cop92] and Stroustrup [Str91] mention Handle classes and give some examples. Their examples emphasize memory management issues like sharing string representations and support for variable-sized objects. Our focus is more on supporting independent extension of both an abstraction and its implementation.

libg++ [Lea88] defines classes that implement common data structures, such as Set, LinkedSet, HashSet, LinkedList, and HashTable. Set is an abstract class that defines a set abstraction, while LinkedList and HashTable are concrete implementors for a linked list and a hash table, respectively. LinkedSet and HashSet are Set implementors that bridge between Set and their concrete counterparts LinkedList and HashTable. This is an example of a degenerate bridge, because there’s no abstract Implementor class.

NeXT’s AppKit [Add94] uses the Bridge pattern in the implementation and display of graphical images. An image can be represented in several different ways. The optimal display of an image depends on the properties of a display device, specifically its color capabilities and its resolution. Without help from AppKit, developers would have to determine which implementation to use under various circumstances in every application.

To relieve developers of this responsibility, AppKit provides an NXImage/NXImageRep bridge. NXImage defines the interface for handling images. The implementation of images is defined in a separate NXImageRep class hierarchy having subclasses such as NXEPSImageRep, NXCachedImageRep, and NXBitMapImageRep. NXImage maintains a reference to one or more NXImageRep objects. If there is more than one image implementation, then NXImage selects the most appropriate one for the current display device. NXImage is even capable of converting one implementation to another if necessary. The interesting aspect of this Bridge variant is that NXImage can store more than one NXImageRep implementation at a time.

## Related Patterns

An Abstract Factory (87) can create and configure a particular Bridge.

The Adapter (139) pattern is geared toward making unrelated classes work together. It is usually applied to systems after they’re designed. Bridge, on the other hand, is used up-front in a design to let abstractions and implementations vary independently.

## Object Structural: Composite

## Intent

Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

## Motivation

Graphics applications like drawing editors and schematic capture systems let users build complex diagrams out of simple components. The user can group components to form larger components, which in turn can be grouped to form still larger components. A simple implementation could define classes for graphical primitives such as Text and Lines plus other classes that act as containers for these primitives.

But there’s a problem with this approach: Code that uses these classes must treat primitive and container objects differently, even if most of the time the user treats them identically. Having to distinguish these objects makes the application more complex. The Composite pattern describes how to use recursive composition so that clients don’t have to make this distinction.

![](images/c634a61139637781b5bb8f9749c856390ad6c8ff686549518c1c0363c35c72f3.jpg)

The key to the Composite pattern is an abstract class that represents both primitives and their containers. For the graphics system, this class is Graphic. Graphic declares operations like Draw that are specific to graphical objects. It also declares operations that all composite objects share, such as operations for accessing and managing its children.

The subclasses Line, Rectangle, and Text (see preceding class diagram) define primitive graphical objects. These classes implement Draw to draw lines, rectangles, and text, respectively. Since primitive graphics have no child graphics, none of these subclasses implements child-related operations.

The Picture class defines an aggregate of Graphic objects. Picture implements Draw to call Draw on its children, and it implements child-related operations accordingly. Because the Picture interface conforms to the Graphic interface, Picture objects can

compose other Pictures recursively.

The following diagram shows a typical composite object structure of recursively composed Graphic objects:

![](images/adb22453983c56a0482cee02a8fab6fdab5d23e238e905639b835edec0473bf0.jpg)

## Applicability

Use the Composite pattern when

• you want to represent part-whole hierarchies of objects.

• you want clients to be able to ignore the difference between compositions of objects and individual objects. Clients will treat all objects in the composite structure uniformly.

## Structure

![](images/35ea86dac96c5a7c8ea84c3418eaa694d3f8c5ee863e3702e37362735910336d.jpg)  
A typical Composite object structure might look like this: