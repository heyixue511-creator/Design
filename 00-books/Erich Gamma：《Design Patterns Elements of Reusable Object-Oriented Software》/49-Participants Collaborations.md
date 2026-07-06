![](images/22b65590336e40df09bf098393c3494c3217cf9881edc1b94805882da7454403.jpg)

Here’s a possible object diagram of a proxy structure at run-time:  
![](images/917946ea9b96691d28e69de4665797fb043ca280c6c6cbdf89c02df0796ec2e4.jpg)

## Participants

• Proxy (ImageProxy)

– maintains a reference that lets the proxy access the real subject. Proxy may refer to a Subject if the RealSubject and Subject interfaces are the same.

– provides an interface identical to Subject’s so that a proxy can by substituted for the real subject.

– controls access to the real subject and may be responsible for creating and deleting it.

– other responsibilities depend on the kind of proxy:

• remote proxies are responsible for encoding a request and its arguments and for sending the encoded request to the real subject in a different address space.

• virtual proxies may cache additional information about the real subject so that they can postpone accessing it. For example, the ImageProxy from the Motivation caches the real image’s extent.

• protection proxies check that the caller has the access permissions required to perform a request.

## • Subject (Graphic)

– defines the common interface for RealSubject and Proxy so that a Proxy can be used anywhere a RealSubject is expected.

## • RealSubject (Image)

– defines the real object that the proxy represents.

## Collaborations

• Proxy forwards requests to RealSubject when appropriate, depending on the kind of proxy.

## Consequences

The Proxy pattern introduces a level of indirection when accessing an object. The additional indirection has many uses, depending on the kind of proxy:

1. A remote proxy can hide the fact that an object resides in a different address space.

2 . A virtual proxy can perform optimizations such as creating an object on demand.

3. Both protection proxies and smart references allow additional housekeeping tasks when an object is accessed.

There’s another optimization that the Proxy pattern can hide from the client. It’s called copy-on-write, and it’s related to creation on demand. Copying a large and complicated object can be an expensive operation. If the copy is never modified, then there’s no need to incur this cost. By using a proxy to postpone the copying process, we ensure that we pay the price of copying the object only if it’s modified.

To make copy-on-write work, the subject must be reference counted. Copying the proxy will do nothing more than increment this reference count. Only when the client requests an operation that modifies the subject does the proxy actually copy it. In that case the proxy must also decrement the subject’s reference count. When the reference count goes to zero, the subject gets deleted.

Copy-on-write can reduce the cost of copying heavyweight subjects significantly.

## Implementation

The Proxy pattern can exploit the following language features:

1. Overloading the member access operator in C++. C++ supports overloading operator->, the member access operator. Overloading this operator lets you perform additional work whenever an object is dereferenced. This can be helpful for implementing some kinds of proxy; the proxy behaves just like a pointer.

The following example illustrates how to use this technique to implement a virtual proxy called ImagePtr.

class Image;   
extern Image\* LoadAnImageFile(const char\*);   
// externalfunction

class ImagePtr{   
public:   
ImagePtr(const char\*imageFile);   
virtual \~ImagePtr();   
virtual Image\* operator->();   
virtual Image& operator\*();   
private:   
Image\* LoadImage();   
private:   
Image\*\_image;   
const char\*\_imageFile;   
ImagePtr::ImagePtr (const char\* theImageFile){   
\_imageFile = theImageFile;   
\_image = 0;   
  
Image\* ImagePtr::LoadImage (){   
if (\_image == 0) {   
\_image = LoadAnImageFile(\_imageFile);   
  
retura \_image;   
}

The overloaded -> and \* operators use LoadImage to return \_image to callers (loading it if necessary).

Image\* ImagePtr::operator->() {   
return LoadImage();   
  
Image& ImagePtr::operator\*(){   
return \*LoadImage();   
}

This approach lets you call Image operations through ImagePtr objects without going to the trouble of making the operations part of the ImagePtr interface:

ImagePtr image = ImagePtr("anImageFileName");   
image->Draw(Point(50, 100));   
//(image.operator->())->Draw(Point(50, 100))

Notice how the image proxy acts like a pointer, but it’s not declared to be a pointer to an Image. That means you can’t use it exactly like a real pointer to an Image. Hence clients must treat Image and ImagePtr objects differently in this approach.

Overloading the member access operator isn’t a good solution for every kind of proxy. Some proxies need to know precisely which operation is called, and overloading the member access operator doesn’t work in those cases.

Consider the virtual proxy example in the Motivation. The image should be loaded at a specific time—namely when the Draw operation is called—and not whenever the image is referenced. Overloading the access operator doesn’t allow this distinction. In that case we must manually implement each proxy operation that forwards the request to the subject.

These operations are usually very similar to each other, as the Sample Code demonstrates. Typically all operations verify that the request is legal, that the original object exists, etc., before forwarding the request to the subject. It’s tedious to write this code again and again. So it’s common to use a preprocessor to generate it automatically.

2. Using doesNotUnderstand in Smalltalk. Smalltalk provides a hook that you can use to support automatic forwarding of requests. Smalltalk calls doesNotUnderstand: aMessage when a client sends a message to a receiver that has no corresponding method. The Proxy class can redefine doesNotUnderstand so that the message is forwarded to its subject.

To ensure that a request is forwarded to the subject and not just absorbed by the proxy silently, you can define a Proxy class that doesn’t understand any messages. Smalltalk lets you do this by defining Proxy as a class with no superclass.<sup>6</sup>

The main disadvantage of doesNotUnderstand: is that most Smalltalk systems have a few special messages that are handled directly by the virtual machine, and these do not cause the usual method look-up. The only one that’s usually implemented in Object (and so can affect proxies) is the identity operation ==.

If you’re going to use doesNotUnderstand: to implement Proxy, then you must design around this problem. You can’t expect identity on proxies to mean identity on their real subjects. An added disadvantage is that doesNotUnderstand: was developed for error handling, not for building proxies, and so it’s generally not very fast.

3. Proxy doesn’t always have to know the type of real subject. If a Proxy class can deal with its subject solely through an abstract interface, then there’s no need to make a Proxy class for each RealSubject class; the proxy can deal with all RealSubject classes uniformly. But if Proxies are going to instantiate RealSubjects (such as in a virtual proxy), then they have to know the concrete class.

Another implementation issue involves how to refer to the subject before it’s instantiated. Some proxies have to refer to their subject whether it’s on disk or in memory. That means they must use some form of address space-independent object identifiers. We used a file name for this purpose in the Motivation.