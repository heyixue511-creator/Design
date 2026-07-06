taking into account the components’ size and stretchability. It also tries to give an even “color” to the paragraph by minimizing the whitespace between components.

class TexCompositor: public Compositor {   
public:   
TeXCompositor();   
virtual int Compose(   
Coord natural[], Coord stretch[], Coord shrink[],   
int componentCount, int lineWidth, int breaks[]   
};

ArrayCompositor breaks the components into lines at regular intervals.

class ArrayCompositor : public Compositor {   
public:   
ArrayCompositor(int interval);   
virtual int Compose(   
Coord natural[], Coord stretch[], Coord shrink[],   
int componentCount, int lineWidth, int breaks[]

These classes don’t use all the information passed in Compose. SimpleCompositor ignores the stretchability of the components, taking only their natural widths into account. TeXCompositor uses all the information passed to it, whereas ArrayCompositor ignores everything.

To instantiate Composition, you pass it the compositor you want to use:

Composition\* quick = new Composition(new SimpleCompositor);   
Composition\*slick = newComposition(new TexCompositor);   
Composition\*iconic = newComposition(new ArrayCompositor(100));

Compositor’s interface is carefully designed to support all layout algorithms that subclasses might implement. You don’t want to have to change this interface with every new subclass, because that will require changing existing subclasses. In general, the Strategy and Context interfaces determine how well the pattern achieves its intent.

## Known Uses

Both ET++ [WGM88] and Interviews use strategies to encapsulate different linebreaking algorithms as we’ve described.

In the RTL System for compiler code optimization [JML92], strategies define different register allocation schemes (RegisterAllocator) and instruction set scheduling policies (RISCscheduler, CISCscheduler). This provides flexibility in targeting the optimizer for different machine architectures.

The ET++SwapsManager calculation engine framework computes prices for different financial instruments [EG92]. Its key abstractions are Instrument and Yield-Curve. Different instruments are implemented as subclasses of Instrument. Yield-Curve calculates discount factors, which determine the present value of future cash flows. Both of these classes delegate some behavior to Strategy objects. The framework provides a family of ConcreteStrategy classes for generating cash flows, valuing swaps, and calculating discount factors. You can create new calculation engines by configuring Instrument and YieldCurve with the different ConcreteStrategy objects. This approach supports mixing and matching existing Strategy implementations as well as defining new ones.

The Booch components [BV90] use strategies as template arguments. The Booch collection classes support three different kinds of memory allocation strategies: managed (allocation out of a pool), controlled (allocations/deallocations are protected by locks), and unmanaged (the normal memory allocator). These strategies are passed as template arguments to a collection class when it’s instantiated. For example, an UnboundedCollection that uses the unmanaged strategy is instantiated as UnboundedCollection<MyItemType\*, Unmanaged>.

RApp is a system for integrated circuit layout [GA89, AG90]. RApp must lay out and route wires that connect subsystems on the circuit. Routing algorithms in RApp are defined as subclasses of an abstract Router class. Router is a Strategy class.

Borland’s ObjectWindows [Bor94] uses strategies in dialogs boxes to ensure that the user enters valid data. For example, numbers might have to be in a certain range, and a numeric entry field should accept only digits. Validating that a string is correct can require a table look-up.

ObjectWindows uses Validator objects to encapsulate validation strategies. Validators are examples of Strategy objects. Data entry fields delegate the validation strategy to an optional Validator object. The client attaches a validator to a field if validation is required (an example of an optional strategy). When the dialog is closed, the entry fields ask their validators to validate the data. The class library provides validators for common cases, such as a Range Validator for numbers. New client-specific validation strategies can be defined easily by subclassing the Validator class.

## Related Patterns

Flyweight (195): Strategy objects often make good flyweights.

## Class Behavioral: Template Method

## Intent

Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.

## Motivation

Consider an application framework that provides Application and Document classes. The Application class is responsible for opening existing documents stored in an external format, such as a file. A Document object represents the information in a document once it’s read from the file.

Applications built with the framework can subclass Application and Document to suit specific needs. For example, a drawing application defines Draw Application and DrawDocument subclasses; a spreadsheet application defines Spreadsheet-Application and SpreadsheetDocument subclasses.

![](images/9f1071b3aaf101ee431e9867e48b7764035dd304e04fef4463bf2b59e15fb81d.jpg)

The abstract Application class defines the algorithm for opening and reading a document in its OpenDocument operation:

void Application::OpenDocument (const char\* name){   
if(!CanOpenDocument (name)) {   
//cannothandle this document   
return;   
Document\* doc= DoCreateDocument ();   
if (doc) {   
\_docs->AddDocument(doc);   
AboutToOpenDocument (doc);   
doc->Open();   
doc->DoRead();

OpenDocument defines each step for opening a document. It checks if the document can be opened, creates the application-specific Document object, adds it to its set of documents, and reads the Document from a file.

We call OpenDocument a template method. A template method defines an algorithm in terms of abstract operations that subclasses override to provide concrete behavior. Application subclasses define the steps of the algorithm that check if the document can be opened (CanOpenDocument) and that create the Document (DoCreateDocument). Document classes define the step that reads the document (DoRead). The template method also defines an operation that lets Application subclasses know when the document is about to be opened (AboutToOpenDocument), in case they care.

By defining some of the steps of an algorithm using abstract operations, the template method fixes their ordering, but it lets Application and Document subclasses vary those steps to suit their needs.

## Applicability

The Template Method pattern should be used

• to implement the invariant parts of an algorithm once and leave it up to subclasses to implement the behavior that can vary.

• when common behavior among subclasses should be factored and localized in a common class to avoid code duplication. This is a good example of “refactoring to generalize” as described by Opdyke and Johnson [OJ93]. You first identify the differences in the existing code and then separate the differences into new operations. Finally, you replace the differing code with a template method that calls one of these new operations.

• to control subclasses extensions. You can define a template method that calls “hook” operations (see Consequences) at specific points, thereby permitting extensions only at those points.

## Structure