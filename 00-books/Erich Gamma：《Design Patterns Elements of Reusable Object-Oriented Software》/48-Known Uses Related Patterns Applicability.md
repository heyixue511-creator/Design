GlyphFactory::GlyphFactory () {   
for(int i = 0; i < NCHARCODES; ++i) {   
\_character[i] = 0;   
}   
)

CreateCharacter looks up a character in the character glyph in the array, and it returns the corresponding glyph if it exists. If it doesn’t, then CreateCharacter creates the glyph, puts it in the array, and returns it:

Character\* GlyphFactory::CreateCharacter (char c) {   
if(!\_character[c]) {   
\_character[c]= newCharacter(c);   
  
return \_character[c];

The other operations simply instantiate a new object each time they’re called, since noncharacter glyphs won’t be shared:

Row\* GlyphFactory::CreateRow () {   
return new Row;   
Column\* GlyphFactory::CreateColumn (){   
return new Column;

We could omit these operations and let clients instantiate unshared glyphs directly. However, if we decide to make these glyphs sharable later, we’ll have to change client code that creates them.

## Known Uses

The concept of flyweight objects was first described and explored as a design technique in Interviews 3.0 [CL90]. Its developers built a powerful document editor called Doc as a proof of concept [CL92]. Doc uses glyph objects to represent each character in the document. The editor builds one Glyph instance for each character in a particular style (which defines its graphical attributes); hence a character’s intrinsic state consists of the character code and its style information (an index into a style table).<sup>4</sup> That means only position is extrinsic, making Doc fast. Documents are represented by a class Document, which also acts as the FlyweightFactory. Measurements on Doc have shown that sharing flyweight characters is quite effective. In a typical case, a document containing 180,000 characters required allocation of only 480 character objects.

ET++ [WGM88] uses flyweights to support look-and-feel independence.<sup>5</sup> The lookand-feel standard affects the layout of user interface elements (e.g., scroll bars, buttons, menus—known collectively as “widgets”) and their decorations (e.g., shadows, beveling). A widget delegates all its layout and drawing behavior to a separate Layout object. Changing the Layout object changes the look and feel, even at run-time.

For each widget class there is a corresponding Layout class (e.g., ScrollbarLayout, MenubarLayout, etc.). An obvious problem with this approach is that using separate layout objects doubles the number of user interface objects: For each user interface object there is an additional Layout object. To avoid this overhead, Layout objects are implemented as flyweights. They make good flyweights because they deal mostly with defining behavior, and it’s easy to pass them what little extrinsic state they need to lay out or draw an object.

The Layout objects are created and managed by Look objects. The Look class is an Abstract Factory (87) that retrieves a specific Layout object with operations like GetButtonLayout, GetMenuBarLayout, and so forth. For each look-and-feel standard there is a corresponding Look subclass (e.g., MotifLook, OpenLook) that supplies the appropriate Layout objects.

By the way, Layout objects are essentially strategies (see Strategy (315)). They are an example of a strategy object implemented as a flyweight.

## Related Patterns

The Flyweight pattern is often combined with the Composite (163) pattern to implement a logically hierarchical structure in terms of a directed-acyclic graph with shared leaf nodes.

It’s often best to implement State (305) and Strategy (315) objects as flyweights.

## Object Structural: Proxy

## Intent

Provide a surrogate or placeholder for another object to control access to it.

## Also Known As

Surrogate

## Motivation

One reason for controlling access to an object is to defer the full cost of its creation and initialization until we actually need to use it. Consider a document editor that can embed graphical objects in a document. Some graphical objects, like large raster images, can be expensive to create. But opening a document should be fast, so we should avoid creating all the expensive objects at once when the document is opened. This isn’t necessary anyway, because not all of these objects will be visible in the document at the same time.

These constraints would suggest creating each expensive object on demand, which in this case occurs when an image becomes visible. But what do we put in the document in place of the image? And how can we hide the fact that the image is created on demand so that we don’t complicate the editor’s implementation? This optimization shouldn’t impact the rendering and formatting code, for example.

The solution is to use another object, an image proxy, that acts as a stand-in for the real image. The proxy acts just like the image and takes care of instantiating it when it’s required.

![](images/1ae702a386def50457a3512db5ad004ee80d011ceaf752dcc9d785de43198e31.jpg)

The image proxy creates the real image only when the document editor asks it to display itself by invoking its Draw operation. The proxy forwards subsequent requests directly to the image. It must therefore keep a reference to the image after creating it.

Let’s assume that images are stored in separate files. In this case we can use the file name as the reference to the real object. The proxy also stores its extent, that is, its width and height. The extent lets the proxy respond to requests for its size from the formatter without actually instantiating the image.

The following class diagram illustrates this example in more detail.

![](images/20a964d85464df6304fd6bf908b055daf5d01bc295ec3b73224c5efb055a6032.jpg)  
The document editor accesses embedded images through the interface defined by the

abstract Graphic class. ImageProxy is a class for images that are created on demand. ImageProxy maintains the file name as a reference to the image on disk. The file name is passed as an argument to the ImageProxy constructor.

ImageProxy also stores the bounding box of the image and a reference to the real Image instance. This reference won’t be valid until the proxy instantiates the real image. The Draw operation makes sure the image is instantiated before forwarding it the request. GetExtent forwards the request to the image only if it’s instantiated; otherwise ImageProxy returns the extent it stores.

## Applicability

Proxy is applicable whenever there is a need for a more versatile or sophisticated reference to an object than a simple pointer. Here are several common situations in which the Proxy pattern is applicable:

1. A remote proxy provides a local representative for an object in a different address space. NEXTSTEP [Add94] uses the class NXProxy for this purpose. Coplien [Cop92] calls this kind of proxy an “Ambassador.”

2 . A virtual proxy creates expensive objects on demand. The ImageProxy described in the Motivation is an example of such a proxy.

3. A protection proxy controls access to the original object. Protection proxies are useful when objects should have different access rights. For example, KernelProxies in the Choices operating system [CIRM93] provide protected access to operating system objects.

4 . A smart reference is a replacement for a bare pointer that performs additional actions when an object is accessed. Typical uses include

• counting the number of references to the real object so that it can be freed automatically when there are no more references (also called smart pointers [Ede92]).

• loading a persistent object into memory when it’s first referenced.

• checking that the real object is locked before it’s accessed to ensure that no other object can change it.

## Structure