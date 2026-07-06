class Visitor {   
public:   
void VisitMyType(MyType\*);   
void VisitYourType(YourType\*);   
};

MyType and YourType do not have to be related through inheritance at all.

5. Accumulating state. Visitors can accumulate state as they visit each element in the object structure. Without a visitor, this state would be passed as extra arguments to the operations that perform the traversal, or they might appear as global variables.

6. Breaking encapsulation. Visitor’s approach assumes that the ConcreteElement interface is powerful enough to let visitors do their job. As a result, the pattern often forces you to provide public operations that access an element’s internal state, which may compromise its encapsulation.

## Implementation

Each object structure will have an associated Visitor class. This abstract visitor class declares a VisitConcreteElement operation for each class of ConcreteElement defining the object structure. Each Visit operation on the Visitor declares its argument to be a particular ConcreteElement, allowing the Visitor to access the interface of the ConcreteElement directly. Concrete Visitor classes override each Visit operation to implement visitor-specific behavior for the corresponding ConcreteElement class.

The Visitor class would be declared like this in C++:

class Visitor {   
public:   
virtual void VisitElementA(ElementA\*);   
virtual void VisitElementB(ElementB\*);   
//and so on forother concreteelements   
protected:   
Visitor();

Each class of ConcreteElement implements an Accept operation that calls the matching Visit. . . operation on the visitor for that ConcreteElement. Thus the operation that ends up getting called depends on both the class of the element and the class of the visitor.<sup>10</sup>

The concrete elements are declared as

class Element {   
public:   
virtualElement();   
virtualvoid Accept(Visitor&) = 0;   
protected:   
Element ();   
class ElementA : public Element {   
public:   
ElementA();   
virtual void Accept(Visitor& v) {v.VisitElementA(this); )   
class ElementB : public Element {   
public:   
ElementB();   
virtual void Accept(Visitor& v){v.VisitElementB(this);}

A CompositeElement class might implement Accept like this:

class CompositeElement : public Element{   
public:   
virtual void Accept(Visitor&);   
private:   
List<Element\*>\*\_children;   
void CompositeElement::Accept (Visitor& v) {   
ListIterator<Element\*> i(\_children);   
for (i.First(); !i.IsDone(); i.Next()) {   
i.CurrentItem()->Accept (v);   
v.VisitCompositeElement(this);

Here are two other implementation issues that arise when you apply the Visitor pattern:

1 . Double dispatch. Effectively, the Visitor pattern lets you add operations to classes without changing them. Visitor achieves this by using a technique called double-dispatch. It’s a well-known technique. In fact, some programming languages support it directly (CLOS, for example). Languages like C++ and Smalltalk support single-dispatch.

In single-dispatch languages, two criteria determine which operation will fulfill a request: the name of the request and the type of receiver. For example, the operation that a GenerateCode request will call depends on the type of node object you ask. In C++, calling GenerateCode on an instance of VariableRefNode will call

VariableRefNode::GenerateCode (which generates code for a variable reference). C a l l i n g GenerateCode on an AssignmentNode will call AssignmentNode::GenerateCode (which will generate code for an assignment). The operation that gets executed depends both on the kind of request and the type of the receiver.

“Double-dispatch” simply means the operation that gets executed depends on the kind of request and the types of two receivers. Accept is a double-dispatch operation. Its meaning depends on two types: the Visitor’s and the Element’s. Double-dispatching lets visitors request different operations on each class of element.<sup>11</sup>

This is the key to the Visitor pattern: The operation that gets executed depends on both the type of Visitor and the type of Element it visits. Instead of binding operations statically into the Element interface, you can consolidate the operations in a Visitor and use Accept to do the binding at run-time. Extending the Element interface amounts to defining one new Visitor subclass rather than many new Element subclasses.

2. Who is responsible for traversing the object structure? A visitor must visit each element of the object structure. The question is, how does it get there? We can put responsibility for traversal in any of three places: in the object structure, in the visitor, or in a separate iterator object (see Iterator (257)).

Often the object structure is responsible for iteration. A collection will simply iterate over its elements, calling the Accept operation on each. A composite will commonly traverse itself by having each Accept operation traverse the element’s children and call Accept on each of them recursively.

Another solution is to use an iterator to visit the elements. In C++, you could use either an internal or external iterator, depending on what is available and what is most efficient. In Smalltalk, you usually use an internal iterator using do: and a block. Since internal iterators are implemented by the object structure, using an internal iterator is a lot like making the object structure responsible for iteration. The main difference is that an internal iterator will not cause double-dispatching—it will call an operation on the visitor with an element as an argument as opposed to calling an operation on the element with the visitor as an argument. But it’s easy to use the Visitor pattern with an internal iterator if the operation on the visitor simply calls the operation on the element without recursing.

You could even put the traversal algorithm in the visitor, although you’ll end up duplicating the traversal code in each ConcreteVisitor for each aggregate ConcreteElement. The main reason to put the traversal strategy in the visitor is to implement a particularly complex traversal, one that depends on the results of the operations on the object structure. We’ll give an example of such a case in the Sample Code.

## Sample Code

Because visitors are usually associated with composites, we’ll use the Equipment classes defined in the Sample Code of Composite (163) to illustrate the Visitor pattern. We will use Visitor to define operations for computing the inventory of materials and the total cost for a piece of equipment. The Equipment classes are so simple that using Visitor isn’t really necessary, but they make it easy to see what’s involved in implementing the pattern.

Here again is the Equipment class from Composite (163). We’ve augmented it with an Accept operation to let it work with a visitor.

class Equipment {   
public:   
virtual\~Equipment();   
const char\* Name() { return \_name; }   
virtual Watt Power();   
virtual Currency NetPrice();   
virtual Currency DiscountPrice();   
virtual void Accept(EquipmentVisitor&);   
protected:   
Equipment(const char\*);   
private:   
const char\* \_name;

The Equipment operations return the attributes of a piece of equipment, such as its power consumption and cost. Subclasses redefine these operations appropriately for specific types of equipment (e.g., a chassis, drives, and planar boards).

The abstract class for all visitors of equipment has a virtual function for each subclass of equipment, as shown next. All of the virtual functions do nothing by default.

class EquipmentVisitor {   
public:   
virtual \~EquipmentVisitor();   
virtual void VisitFloppyDisk(FloppyDisk\*);   
virtual voidVisitCard(Card\*);   
virtual void VisitChassis(Chassis\*);   
virtual void VisitBus(Bus\*);   
// and so on for other concrete subclasses of Equipment   
protected:   
Equipmentvisitor();

Equipment subclasses define Accept in basically the same way: It calls the EquipmentVisitor operation that corresponds to the class that received the Accept request, like this:

void FloppyDisk::Accept(EquipmentVisitor& visitor){   
visitor.VisitFloppyDisk(this);

Equipment that contains other equipment (in particular, subclasses of CompositeEquipment in the Composite pattern) implements Accept by iterating over its children and calling Accept on each of them. Then it calls the Visit operation as usual. For example, Chassis::Accept could traverse all the parts in the chassis as follows:

void Chassis::Accept(EquipmentVisitor& visitor) {   
for(   
ListIterator<Equipment\*> i(\_parts);   
!i.IsDone();   
i.Next()   
i.CurrentItem()->Accept(visitor);   
}   
visitor.VisitChassis(this);   
}

Subclasses of EquipmentVisitor define particular algorithms over the equipment structure. The PricingVisitor computes the cost of the equipment structure. It computes the net price of all simple equipment (e.g., floppies) and the discount price of all composite equipment (e.g., chassis and buses).

class PricingVisitor : public EquipmentVisitor {   
public:   
PricingVisitor();   
Currency& GetTotalPrice();   
virtual void VisitFloppyDisk(FloppyDisk\*);   
virtual void VisitCard(Card\*);   
virtual void VisitChassis(Chassis\*);   
virtual void VisitBus(Bus\*);   
private:   
Currency \_total;   
};   
void PricingVisitor::VisitFloppyDisk (FloppyDisk\* e) {   
\_total += e->NetPrice();   
)   
void PricingVisitor::VisitChassis (Chassis\* e) {   
\_total += e->DiscountPrice();   
}

PricingVisitor will compute the total cost of all nodes in the equipment structure. Note that PricingVisitor chooses the appropriate pricing policy for a class of equipment by dispatching to the corresponding member function. What’s more, we can change the pricing policy of an equipment structure just by changing the PricingVisitor class.

We can define a visitor for computing inventory like this:

class InventoryVisitor: public EquipmentVisitor {   
public:   
InventoryVisitor();   
Inventory& GetInventory();   
virtual void VisitFloppyDisk(FloppyDisk\*);   
virtual void VisitCard(Card\*);   
virtual void VisitChassis(Chassis\*);   
virtual void VisitBus(Bus\*);   
private:   
Inventory \_inventory;

The InventoryVisitor accumulates the totals for each type of equipment in the object structure. InventoryVisitor uses an Inventory class that defines an interface for adding equipment (which we won’t bother defining here).

void InventoryVisitor::VisitFloppyDisk(FloppyDisk\* e) {   
\_inventory.Accumulate(e);

void InventoryVisitor::VisitChassis (Chassis\* e){   
\_inventory.Accumulate(e);

Here’s how we can use an InventoryVisitor on an equipment structure:

Equipment\* component;   
InventoryVisitor visitor;

component->Accept(visitor);   
cout << "Inventory"   
<< component->Name()   
<< visitor.GetInventory();

Now we’ll show how to implement the Smalltalk example from the Interpreter pattern (see page 248) with the Visitor pattern. Like the previous example, this one is so small that Visitor probably won’t buy us much, but it provides a good illustration of how to use the pattern. Further, it illustrates a situation in which iteration is the visitor’s responsibility.

The object structure (regular expressions) is made of four classes, and all of them have an accept: method that takes the visitor as an argument. In class SequenceExpression, the accept: method is

accept: aVisitor   
aVisitor visitSequence: self

In class RepeatExpression, the accept: method sends the visitRepeat: message. In c l a s s AlternationExpression, it sends the visitAlternation: message. In class LiteralExpression, it sends the visitLiteral: message.

The four classes also must have accessing functions that the visitor can use. For SequenceExpression these are expressionl and expression2; for AlternationExpression these are alternativel and alternative2; for RepeatExpression it is repetition; and for LiteralExpression these are components.

The ConcreteVisitor class is REMatchingVisitor. It is responsible for the traversal because its traversal algorithm is irregular. The biggest irregularity is that a RepeatExpression will repeatedly traverse its component. The class REMatchingVisitor has an instance variable inputState. Its methods are essentially the same as the match: methods of the expression classes in the Interpreter pattern except they replace the argument named inputState with the expression node being matched. However, they still return the set of streams that the expression would match to identify the current state.