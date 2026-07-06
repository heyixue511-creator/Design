![](images/0848bcd498d2ccae0413f24bb55daf5190c67f96d5741bffe705e98c5ca58d92.jpg)

## Participants

• AbstractClass (Application)

– defines abstract primitive operations that concrete subclasses define to implement steps of an algorithm.

– implements a template method defining the skeleton of an algorithm. The template method calls primitive operations as well as operations defined in AbstractClass or those of other objects.

• ConcreteClass (MyApplication)

– implements the primitive operations to carry out subclass-specific steps of the algorithm.

## Collaborations

• ConcreteClass relies on AbstractClass to implement the invariant steps of the algorithm.

## Consequences

Template methods are a fundamental technique for code reuse. They are particularly important in class libraries, because they are the means for factoring out common behavior in library classes.

Template methods lead to an inverted control structure that’s sometimes referred to as “the Hollywood principle,” that is, “Don’t call us, we’ll call you” [Swe85]. This refers to how a parent class calls the operations of a subclass and not the other way around.

Template methods call the following kinds of operations:

• concrete operations (either on the ConcreteClass or on client classes);

• concrete AbstractClass operations (i.e., operations that are generally useful to subclasses);

• primitive operations (i.e., abstract operations);

• factory methods (see Factory Method (107)); and

• hook operations, which provide default behavior that subclasses can extend if necessary. A hook operation often does nothing by default.

It’s important for template methods to specify which operations are hooks (may be overridden) and which are abstract operations (must be overridden). To reuse an abstract class effectively, subclass writers must understand which operations are designed for overriding.

A subclass can extend a parent class operation’s behavior by overriding the operation and calling the parent operation explicitly:

void Derivedclass::Operation (){   
ParentClass::Operation();   
//DerivedClass extended behavior   
)

Unfortunately, it’s easy to forget to call the inherited operation. We can transform such an operation into a template method to give the parent control over how subclasses extend it. The idea is to call a hook operation from a template method in the parent class. Then subclasses can then override this hook operation:

void ParentClass::Operation (){   
//ParentClass behavior   
HookOperation();   
)

HookOperation does nothing in ParentClass:

void ParentClass::HookOperation () {}

Subclasses override HookOperation to extend its behavior:

void DerivedClass::HookOperation () {   
// derivedclass extension   
}

## Implementation

Three implementation issues are worth noting:

1. Using C++ access control. In C++, the primitive operations that a template method calls can be declared protected members. This ensures that they are only called by the template method. Primitive operations that must be overridden are declared pure virtual. The template method itself should not be overridden; therefore you can make the template method a nonvirtual member function.

2 . Minimizing primitive operations. An important goal in designing template methods is to minimize the number of primitive operations that a subclass must override to flesh out the algorithm. The more operations that need overriding, the more tedious things get for clients.

3 . Naming conventions. You can identify the operations that should be overridden by adding a prefix to their names. For example, the MacApp framework for Macintosh applications [App89] prefixes template method names with “Do-”: “DoCreateDocument”, “DoRead”, and so forth.

## Sample Code

The following C++ example shows how a parent class can enforce an invariant for its subclasses. The example comes from NeXT’s AppKit [Add94]. Consider a class View that supports drawing on the screen. View enforces the invariant that its subclasses can draw into a view only after it becomes the “focus,” which requires certain drawing state (for example, colors and fonts) to be set up properly.

We can use a Display template method to set up this state. View defines two concrete operations, SetFocus and ResetFocus, that set up and clean up the drawing state, respectively. View’ s DoDisplay hook operation performs the actual drawing. Display calls SetFocus before DoDisplay to setup the drawing state; Display calls ResetFocus afterwards to release the drawing state.

void View::Display() {   
SetFocus();   
DoDisplay();   
ResetFocus() ;   
}

To maintain the invariant, the View’s clients always call Display, and View subclasses always override DoDisplay.

DoDisplay does nothing in View:

void View::DoDisplay () { }

Subclasses override it to add their specific drawing behavior:

void MyView::DoDisplay () {   
//renderthe view's contents

## Known Uses

Template methods are so fundamental that they can be found in almost every abstract class. Wirfs-Brock et al. [WBWW90, WBJ90] provide a good overview and discussion of template methods.

## Related Patterns

Factory Methods (107) are often called by template methods. In the Motivation example, the factory method DoCreateDocument is called by the template method OpenDocument.

Strategy (315): Template methods use inheritance to vary part of an algorithm. Strategies use delegation to vary the entire algorithm.

## Object Behavioral: Visitor

## Intent

Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.

## Motivation

Consider a compiler that represents programs as abstract syntax trees. It will need to perform operations on abstract syntax trees for “static semantic” analyses like checking that all variables are defined. It will also need to generate code. So it might define operations for type-checking, code optimization, flow analysis, checking for variables being assigned values before they’re used, and so on. Moreover, we could use the abstract syntax trees for pretty-printing, program restructuring, code instrumentation, and computing various metrics of a program.

Most of these operations will need to treat nodes that represent assignment statements differently from nodes that represent variables or arithmetic expressions. Hence there will be one class for assignment statements, another for variable accesses, another for arithmetic expressions, and so on. The set of node classes depends on the language being compiled, of course, but it doesn’t change much for a given language.

![](images/d6005e8703eb8972ebfeea0f37cb6b3a69153d2628c61d04ea29b3aa0dd98c54.jpg)

This diagram shows part of the Node class hierarchy. The problem here is that distributing all these operations across the various node classes leads to a system that’s hard to understand, maintain, and change. It will be confusing to have type-checking code mixed with pretty-printing code or flow analysis code. Moreover, adding a new operation usually requires recompiling all of these classes. It would be better if each new operation could be added separately, and the node classes were independent of the operations that apply to them.

We can have both by packaging related operations from each class in a separate object, called a visitor, and passing it to elements of the abstract syntax tree as it’s traversed. When an element “accepts” the visitor, it sends a request to the visitor that encodes the element’s class. It also includes the element as an argument. The visitor will then execute the operation for that element—the operation that used to be in the class of the element.

For example, a compiler that didn’t use visitors might type-check a procedure by calling the TypeCheck operation on its abstract syntax tree. Each of the nodes would implement TypeCheck by calling TypeCheck on its components (see the preceding class diagram). If the compiler type-checked a procedure using visitors, then it would create a TypeCheckingVisitor object and call the Accept operation on the abstract syntax tree with that object as an argument. Each of the nodes would implement Accept by calling back on the visitor: an assignment node calls VisitAssignment operation on the visitor, while a variable reference calls VisitVariableReference. What used to be the TypeCheck operation in class AssignmentNode is now the VisitAssignment operation on TypeCheckingVisitor.

To make visitors work for more than just type-checking, we need an abstract parent class NodeVisitor for all visitors of an abstract syntax tree. NodeVisitor must declare an operation for each node class. An application that needs to compute program metrics will define new subclasses of NodeVisitor and will no longer need to add application-