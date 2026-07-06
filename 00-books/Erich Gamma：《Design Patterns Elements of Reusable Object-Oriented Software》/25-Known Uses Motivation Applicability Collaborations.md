A BombedMazeFactory or EnchantedMazeFactory is created by associating different classes with the keys. For example, an EnchantedMazeFactory could be created like this:

createMazeFactory   
(MazeFactorynew   
addPart: Wall named: #wall;   
addPart: EnchantedRoom named: #room;   
addPart: DoorNeedingSpell named: #door;   
yourself)

## Known Uses

Interviews uses the “Kit” suffix [Lin92] to denote AbstractFactory classes. It defines WidgetKit and DialogKit abstract factories for generating look-and-feel-specific user interface objects. Interviews also includes a LayoutKit that generates different composition objects depending on the layout desired. For example, a layout that is conceptually horizontal may require different composition objects depending on the document’s orientation (portrait or landscape).

ET++ [WGM88] uses the Abstract Factory pattern to achieve portability across different window systems (X Windows and SunView, for example). The WindowSystem abstract base class defines the interface for creating objects that represent window system resources (MakeWindow, MakeFont, MakeColor, for example). Concrete subclasses implement the interfaces for a specific window system. At run-time, ET++ creates an instance of a concrete WindowSystem subclass that creates concrete system resource objects.

## Related Patterns

AbstractFactory classes are often implemented with factory methods (Factory Method (107)), but they can also be implemented using Prototype (117).

A concrete factory is often a singleton (Singleton (127)).

## Object Creational: Builder

## Intent

Separate the construction of a complex object from its representation so that the same construction process can create different representations.

## Motivation

A reader for the RTF (Rich Text Format) document exchange format should be able to convert RTF to many text formats. The reader might convert RTF documents into plain ASCII text or into a text widget that can be edited interactively. The problem, however, is that the number of possible conversions is open-ended. So it should be easy to add a new conversion without modifying the reader.

A solution is to configure the RTFReader class with a TextConverter object that converts RTF to another textual representation. As the RTFReader parses the RTF document, it uses the TextConverter to perform the conversion. Whenever the RTFReader recognizes an RTF token (either plain text or an RTF control word), it issues a request to the TextConverter to convert the token. TextConverter objects are responsible both for performing the data conversion and for representing the token in a particular format.

Subclasses of TextConverter specialize in different conversions and formats. For example, an ASCIIConverter ignores requests to convert anything except plain text. A TeXConverter, on the other hand, will implement operations for all requests in order to produce a $\mathrm { T _ { E } X }$ representation that captures all the stylistic information in the text. A TextWidgetConverter will produce a complex user interface object that lets the user see and edit the text.

![](images/3b8423477bd883a6238db92ffc384e5b098f9d2bf5d6c4e4a31a0fdffd0d3d26.jpg)

Each kind of converter class takes the mechanism for creating and assembling a complex object and puts it behind an abstract interface. The converter is separate from the reader, which is responsible for parsing an RTF document.

The Builder pattern captures all these relationships. Each converter class is called a builder in the pattern, and the reader is called the director. Applied to this example, the Builder pattern separates the algorithm for interpreting a textual format (that is, the parser for RTF documents) from how a converted format gets created and represented. This lets us reuse the RTFReader’s parsing algorithm to create different text representations from RTF documents—just configure the RTFReader with different subclasses of TextConverter.

## Applicability

Use the Builder pattern when

• the algorithm for creating a complex object should be independent of the parts that make up the object and how they’re assembled.

• the construction process must allow different representations for the object that’s constructed.

## Structure

![](images/95aaaa1f78d6575b097004383c4c2a362db19c9dd198158290f5c8d9c4277451.jpg)

## Participants

• Builder (TextConverter)

– specifies an abstract interface for creating parts of a Product object.

• ConcreteBuilder (ASCIIConverter, TeXConverter, TextWidgetConverter)

– constructs and assembles parts of the product by implementing the Builder interface.

– defines and keeps track of the representation it creates.

– provides an interface for retrieving the product (e.g., GetASCIIText, Get-Text Widget).

• Director (RTFReader)

– constructs an object using the Builder interface.

• Product (ASCIIText, TeXText, TextWidget)

– represents the complex object under construction. ConcreteBuilder builds the product’s internal representation and defines the process by which it’s assembled.

– includes classes that define the constituent parts, including interfaces for assembling the parts into the final result.

## Collaborations

• The client creates the Director object and configures it with the desired Builder object.

• Director notifies the builder whenever a part of the product should be built.

• Builder handles requests from the director and adds parts to the product.

• The client retrieves the product from the builder.

The following interaction diagram illustrates how Builder and Director cooperate with a client.

![](images/e2d4dbbc79ae0748568076f20b1198d98d7f1139bb215a40d1c804e4040fa1c1.jpg)

## Consequences

Here are key consequences of the Builder pattern:

1 . It lets you vary a product’s internal representation. The Builder object provides the director with an abstract interface for constructing the product. The interface lets the builder hide the representation and internal structure of the product. It also hides how the product gets assembled. Because the product is constructed through an abstract interface, all you have to do to change the product’s internal representation is define a new kind of builder.

2 . It isolates code for construction and representation. The Builder pattern improves modularity by encapsulating the way a complex object is constructed and represented. Clients needn’t know anything about the classes that define the product’s internal structure; such classes don’t appear in Builder’s interface.