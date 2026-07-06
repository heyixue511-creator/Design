ordering. If Composites represent parse trees, then compound statements can be instances of a Composite whose children must be ordered to reflect the program.

When child ordering is an issue, you must design child access and management interfaces carefully to manage the sequence of children. The Iterator (257) pattern can guide you in this.

7 . Caching to improve performance. If you need to traverse or search compositions frequently, the Composite class can cache traversal or search information about its children. The Composite can cache actual results or just information that lets it short-circuit the traversal or search. For example, the Picture class from the Motivation example could cache the bounding box of its children. During drawing or selection, this cached bounding box lets the Picture avoid drawing or searching when its children aren’t visible in the current window.

Changes to a component will require invalidating the caches of its parents. This works best when components know their parents. So if you’re using caching, you need to define an interface for telling composites that their caches are invalid.

8. Who should delete components? In languages without garbage collection, it’s usually best to make a Composite responsible for deleting its children when it’s destroyed. An exception to this rule is when Leaf objects are immutable and thus can be shared.

9. What’s the best data structure for storing components? Composites may use a variety of data structures to store their children, including linked lists, trees, arrays, and hash tables. The choice of data structure depends (as always) on efficiency. In fact, it isn’t even necessary to use a general-purpose data structure at all. Sometimes composites have a variable for each child, although this requires each subclass of Composite to implement its own management interface. See Interpreter (243) for an example.

## Sample Code

Equipment such as computers and stereo components are often organized into partwhole or containment hierarchies. For example, a chassis can contain drives and planar boards, a bus can contain cards, and a cabinet can contain chassis, buses, and so forth. Such structures can be modeled naturally with the Composite pattern.

Equipment class defines an interface for all equipment in the part-whole hierarchy.

class Equipment {   
public:   
virtual \~Equipment();   
const char\* Name() { return \_name; }   
virtual Watt Power();   
virtual Currency NetPrice();   
virtual Currency DiscountPrice();   
virtual void Add(Equipment\*);   
virtual void Remove(Equipment\*);   
virtual Iterator<Equipment\*>\* CreateIterator();   
protected:   
Equipment(const char\*);   
private:   
const char\*\_name;   
};

Equipment declares operations that return the attributes of a piece of equipment, like its power consumption and cost. Subclasses implement these operations for specific kinds of equipment. Equipment also declares a CreateIterator operation that returns an Iterator (see Appendix C) for accessing its parts. The default implementation for this operation returns a NullIterator, which iterates over the empty set.

Subclasses of Equipment might include Leaf classes that represent disk drives, integrated circuits, and switches:

class FloppyDisk : public Equipment {   
public:   
FloppyDisk(constchar\*);   
virtual \~FloppyDisk();   
virtualWatt Power();   
virtual Currency NetPrice();   
virtual Currency DiscountPrice();   
};

CompositeEquipment is the base class for equipment that contains other equipment. It’s also a subclass of Equipment.

class CompositeEquipment : public Equipment {   
public:   
virtual\~CompositeEquipment();   
virtual Watt Power();   
virtual Currency NetPrice();   
virtual Currency DiscountPrice();   
virtual void Add(Equipment\*);   
virtual void Remove(Equipment\*);   
virtual Iterator<Equipment\*>\*CreateIterator();   
protected:   
CompositeEquipment(constchar\*);   
private:   
List<Equipment\*> \_equipment;   
};

CompositeEquipment defines the operations for accessing and managing subequipment. The operations Add and Remove insert and delete equipment from the list of equipment stored in the \_equipment member. The operation CreateIterator returns an iterator (specifically, an instance of ListIterator) that will traverse this list.

A default implementation of NetPrice might use CreateIterator to sum the net prices of the subequipment<sup>2</sup>:

Currency CompositeEquipment::NetPrice () {   
Iterator<Equipment\*>\*i =CreateIterator();   
Currency total = 0;   
for (i->First(); !i->IsDone(); i->Next()){   
total += i->CurrentItem()->NetPrice();   
delete i;   
return total;   
}

Now we can represent a computer chassis as a subclass of CompositeEquipment called Chassis. Chassis inherits the child-related operations from CompositeEquipment.

class Chassis : public CompositeEquipment {   
public:   
Chassis(const char\*);   
virtual\~Chassis();   
virtual Watt Power();   
virtualCurrency NetPrice();   
virtualCurrency DiscountPrice();   
};

We can define other equipment containers such as Cabinet and Bus in a similar way.

That gives us everything we need to assemble equipment into a (pretty simple) personal computer:

Cabinet\* cabinet = new Cabinet("PC Cabinet");   
Chassis\* chassis= new Chassis("PC Chassis");   
cabinet->Add(chassis);   
Bus\* bus = new Bus("MCA Bus");   
bus->Add(new Card("16Mbs Token Ring"));   
chassis->Add(bus);   
chassis->Add(new FloppyDisk("3.5in Floppy"));   
cout << "The net price is " << chassis->NetPrice() << endl;

## Known Uses

Examples of the Composite pattern can be found in almost all object-oriented systems. The original View class of Smalltalk Model/View/Controller [KP88] was a Composite, and nearly every user interface toolkit or framework has followed in its steps, including ET++ (with its VObjects [WGM88]) and Interviews (Styles [LCI<sup>+</sup>92], Graphics [VL88], and Glyphs [CL90]). It’s interesting to note that the original View of Model/View/Controller had a set of subviews; in other words, View was both the Component class and the Composite class. Release 4.0 of Smalltalk-80 revised Model/View/Controller with a VisualComponent class that has subclasses View and CompositeView.

The RTL Smalltalk compiler framework [JML92] uses the Composite pattern extensively. RTLExpression is a Component class for parse trees. It has subclasses, such as BinaryExpression, that contain child RTLExpression objects. These classes define a composite structure for parse trees. RegisterTransfer is the Component class for a program’s intermediate Single Static Assignment (SSA) form. Leaf subclasses of RegisterTransfer define different static assignments such as

• primitive assignments that perform an operation on two registers and assign the result to a third;

• an assignment with a source register but no destination register, which indicates that the register is used after a routine returns; and

• an assignment with a destination register but no source, which indicates that the register is assigned before the routine starts.

Another subclass, RegisterTransferSet, is a Composite class for representing