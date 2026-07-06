specific code to the node classes. The Visitor pattern encapsulates the operations for each compilation phase in a Visitor associated with that phase.

![](images/0ac54e907ac34e49b3390aefae257dddbc96a73f53b59324f3c3589c975f79dd.jpg)  
With the Visitor pattern, you define two class hierarchies: one for the elements being operated on (the Node hierarchy) and one for the visitors that define operations on the elements (the NodeVisitor hierarchy). You create a new operation by adding a new subclass to the visitor class hierarchy. As long as the grammar that the compiler accepts doesn’t change (that is, we don’t have to add new Node subclasses), we can add new functionality simply by defining new NodeVisitor subclasses.

## Applicability

Use the Visitor pattern when

• an object structure contains many classes of objects with differing interfaces, and you want to perform operations on these objects that depend on their concrete classes.

• many distinct and unrelated operations need to be performed on objects in an object structure, and you want to avoid “polluting” their classes with these operations. Visitor lets you keep related operations together by defining them in one class. When the object structure is shared by many applications, use Visitor to put operations in just those applications that need them.

• the classes defining the object structure rarely change, but you often want to define new operations over the structure. Changing the object structure classes requires redefining the interface to all visitors, which is potentially costly. If the object structure classes change often, then it’s probably better to define the operations in those classes.

## Structure

![](images/66ff4e6740e083d01b1ead00dab4cfb555009e9a0b646f8a7521da708a4c16d3.jpg)

## Participants

## • Visitor (NodeVisitor)

– declares a Visit operation for each class of ConcreteElement in the object structure. The operation’s name and signature identifies the class that sends the Visit request to the visitor. That lets the visitor determine the concrete class of the element being visited. Then the visitor can access the element directly through its particular interface.

• Concrete Visitor (TypeCheckingVisitor)

– implements each operation declared by Visitor. Each operation implements a fragment of the algorithm defined for the corresponding class of object in the structure. ConcreteVisitor provides the context for the algorithm and stores its local state. This state often accumulates results during the traversal of the structure.

• Element (Node)

– defines an Accept operation that takes a visitor as an argument.

• ConcreteElement (AssignmentNode, VariableRefNode)

– implements an Accept operation that takes a visitor as an argument.

• ObjectStructure (Program)

– can enumerate its elements.

– may provide a high-level interface to allow the visitor to visit its elements.

– may either be a composite (see Composite (163)) or a collection such as a list or a set.

## Collaborations

• A client that uses the Visitor pattern must create a ConcreteVisitor object and then traverse the object structure, visiting each element with the visitor.

• When an element is visited, it calls the Visitor operation that corresponds to its class. The element supplies itself as an argument to this operation to let the visitor access its state, if necessary.

The following interaction diagram illustrates the collaborations between an object structure, a visitor, and two elements:

![](images/69b0470c1b9a69d74554c7b6d6f30d8eeda4f5518fb0796d887bab7b0df65ecd.jpg)

## Consequences

Some of the benefits and liabilities of the Visitor pattern are as follows:

1 . Visitor makes adding new operations easy. Visitors make it easy to add operations that depend on the components of complex objects. You can define a new operation over an object structure simply by adding a new visitor. In contrast, if you spread functionality over many classes, then you must change each class to define a new operation.

2. A visitor gathers related operations and separates unrelated ones. Related behavior isn’t spread over the classes defining the object structure; it’s localized in a visitor. Unrelated sets of behavior are partitioned in their own visitor subclasses. That simplifies both the classes defining the elements and the algorithms defined in the visitors. Any algorithm-specific data structures can be hidden in the visitor.

3. Adding new ConcreteElement classes is hard. The Visitor pattern makes it hard to add new subclasses of Element. Each new ConcreteElement gives rise to a new abstract operation on Visitor and a corresponding implementation in every ConcreteVisitor class. Sometimes a default implementation can be provided in Visitor that can be inherited by most of the ConcreteVisitors, but this is the exception rather than the rule.

So the key consideration in applying the Visitor pattern is whether you are mostly likely to change the algorithm applied over an object structure or the classes of objects that make up the structure. The Visitor class hierarchy can be difficult to maintain when new ConcreteElement classes are added frequently. In such cases, it’s probably easier just to define operations on the classes that make up the structure. If the Element class hierarchy is stable, but you are continually adding operations or changing algorithms, then the Visitor pattern will help you manage the changes.

4. Visiting across class hierarchies. An iterator (see Iterator (257)) can visit the objects in a structure as it traverses them by calling their operations. But an iterator can’t work across object structures with different types of elements. For example, the Iterator interface defined on page 263 can access only objects of type Item:

template <class Item>  
class Iterator {  
Item CurrentItem() const;  
};

This implies that all elements the iterator can visit have a common parent class Item.

Visitor does not have this restriction. It can visit objects that don’t have a common parent class. You can add any type of object to a Visitor interface. For example, in