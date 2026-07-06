## Sample Code

The following code implements two kinds of proxy: the virtual proxy described in the Motivation section, and a proxy implemented with doesNotUnderstand:.<sup>7</sup>

1. A virtual proxy. The Graphic class defines the interface for graphical objects:

class Graphic {   
public:   
virtual\~Graphic();   
virtual void Draw(const Point& at) = 0;   
virtual void HandleMouse(Event& event)= 0;   
virtual const Point& GetExtent() = 0;   
virtual void Load(istream& from) = 0;   
virtual void Save(ostream& to) = 0;   
protected:   
Graphic();   
};

The Image class implements the Graphic interface to display image files. Image overrides HandleMouse to let users resize the image interactively.

class Image : public Graphic (   
public:   
Image(const char\* file); //loads image from afile   
virtual \~Image();   
virtual void Draw(const Point& at);   
virtual voidHandleMouse(Event& event);   
virtual const Point& GetExtent();   
virtual void Load(istream& from);   
virtual void Save(ostream& to);   
private:   
};

ImageProxy has the same interface as Image:

class ImageProxy : public Graphic {   
public:   
ImageProxy(const char\* imageFile);   
virtual\~ImageProxy();   
virtual void Draw(const Point& at);   
virtual void HandleMouse(Event& event);   
virtual const Point& GetExtent();   
virtual void Load(istream& from);   
virtual void Save(ostream& to);   
protected:   
Image\* GetImage();   
private:   
Image\*\_image;   
Point \_extent;   
char\* \_fileName;   
};

The constructor saves a local copy of the name of the file that stores the image, and it initializes \_extent and \_image:

ImageProxy::ImageProxy(constchar\*fileName) {   
\_fileName = strdup(fileName);   
\_extent = Point::Zero; //don't know extent yet   
\_image = 0;   
}

Image\* ImageProxy::GetImage(){   
if (\_image == 0) {   
\_image = new Image(\_fileName);   
}   
return\_image;   
}

The implementation of GetExtent returns the cached extent if possible; otherwise the image is loaded from the file. Draw loads the image, and HandleMouse forwards the event to the real image.

const Point& ImageProxy::GetExtent () {   
if (\_extent == Point::Zero) {   
\_extent =GetImage()->GetExtent();   
  
return\_extent;   
  
void ImageProxy::Draw (const Point& at){   
GetImage()->Draw(at);   
void ImageProxy::HandleMouse (Event& event) {   
GetImage()->HandleMouse(event);   
}

The Save operation saves the cached image extent and the image file name to a stream. Load retrieves this information and initializes the corresponding members.

void ImageProxy::Save (ostream& to) {   
to << \_extent << \_fileName;   
void ImageProxy::Load (istream&from){   
from >> \_extent >> \_fileName;   
}

Finally, suppose we have a class TextDocument that can contain Graphic objects:

class TextDocument {   
public:   
TextDocument ();   
void Insert(Graphic\*);

We can insert an ImageProxy into a text document like this:

TextDocument\* text= new TextDocument;   
text->Insert(newImageProxy("anImageFileName"));

2 . Proxies that use doesNotUnderstand. You can make generic proxies in Smalltalk by defining classes whose superclass is nil<sup>8</sup> and defining the doesNotUnderstand: method to handle messages.

The following method assumes the proxy has a realSubject method that returns its real subject. In the case of ImageProxy, this method would check to see if the the Image had been created, create it if necessary, and finally return it. It uses perform:withArguments: to perform the message being trapped on the real subject.

doesNotUnderstand: aMessage   
self realSubject   
perform:aMessage selector   
withArguments: aMessage arguments

The argument to doesNotUnderstand: is an instance of Message that represents the message not understood by the proxy. So the proxy responds to all messages by making sure that the real subject exists before forwarding the message to it.

One of the advantages of doesNotUnderstand: is it can perform arbitrary processing. For example, we could produce a protection proxy by specifying a set legalMessages of messages to accept and then giving the proxy the following method:

doesNotUnderstand: aMessage   
(legalMessagesincludes: aMessageselector)   
ifTrue: [self realSubject   
perform:aMessage selector   
withArguments: aMessage arguments]   
ifFalse:[self error:'Illegaloperator']

This method checks to see that a message is legal before forwarding it to the real subject. If it isn’t legal, then it will send error: to the proxy, which will result in an infinite loop of errors unless the proxy defines error:. Consequently, the definition of error: should be copied from class Object along with any methods it uses.

## Known Uses

The virtual proxy example in the Motivation section is from the ET++ text building block classes.

NEXTSTEP [Add94] uses proxies (instances of class NXProxy) as local representatives for objects that may be distributed. A server creates proxies for remote objects when clients request them. On receiving a message, the proxy encodes it along with its arguments and then forwards the encoded message to the remote subject. Similarly, the subject encodes any return results and sends them back to the NXProxy object.

McCullough [McC87] discusses using proxies in Smalltalk to access remote objects. Pascoe [Pas86] describes how to provide side-effects on method calls and access control with “Encapsulators.”

## Related Patterns

Adapter (139): An adapter provides a different interface to the object it adapts. In contrast, a proxy provides the same interface as its subject. However, a proxy used for access protection might refuse to perform an operation that the subject will perform, so its interface may be effectively a subset of the subject’s.

Decorator (175): Although decorators can have similar implementations as proxies, decorators have a different purpose. A decorator adds one or more responsibilities to an object, whereas a proxy controls access to an object.

Proxies vary in the degree to which they are implemented like a decorator. A protection proxy might be implemented exactly like a decorator. On the other hand, a remote proxy will not contain a direct reference to its real subject but only an indirect reference, such as “host ID and local address on host.” A virtual proxy will start off with an indirect reference such as a file name but will eventually obtain and use a direct