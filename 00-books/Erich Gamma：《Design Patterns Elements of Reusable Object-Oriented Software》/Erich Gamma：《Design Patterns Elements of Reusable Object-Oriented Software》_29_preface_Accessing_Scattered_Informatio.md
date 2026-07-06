# Accessing Scattered Information / Encapsulating Access and Traversal / Iterator Class and Subclasses / Figure 2.13: Iterator class and subclasses

> Section: preface | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

## Accessing Scattered Information

Many kinds of analysis require examining the text character by character. The text we need to analyze is scattered throughout a hierarchical structure of glyph objects. To examine text in such a structure, we need an access mechanism that has knowledge about the data structures in which objects are stored. Some glyphs might store their children in linked lists, others might use arrays, and still others might use more esoteric data structures. Our access mechanism must be able to handle all of these possibilities.

An added complication is that different analyses access information in different ways. Most analyses will traverse the text from beginning to end. But some do the opposite—a reverse search, for example, needs to progress through the text backward rather than forward. Evaluating algebraic expressions could require an inorder traversal.

So our access mechanism must accommodate differing data structures, and we must support different kinds of traversals, such as preorder, postorder, and inorder.

## Encapsulating Access and Traversal

Right now our glyph interface uses an integer index to let clients refer to children. Although that might be reasonable for glyph classes that store their children in an array, it may be inefficient for glyphs that use a linked list. An important role of the glyph abstraction is to hide the data structure in which children are stored. That way we can change the data structure a glyph class uses without affecting other classes.

Therefore only the glyph can know the data structure it uses. A corollary is that the glyph interface shouldn’t be biased toward one data structure or another. It shouldn’t be better suited to arrays than to linked lists, for example, as it is now.

We can solve this problem and support several different kinds of traversals at the same time. We can put multiple access and traversal capabilities directly in the glyph classes and provide a way to choose among them, perhaps by supplying an enumerated constant as a parameter. The classes pass this parameter around during a traversal to ensure they’re all doing the same kind of traversal. They have to pass around any information they’ve accumulated during traversal.

We might add the following abstract operations to Glyph’s interface to support this approach:

void First(Traversal kind)   
void Next()   
bool IsDone()   
Glyph\* GetCurrent()   
void Insert(Glyph\*)

Operations First, Next, and IsDone control the traversal. First initializes the traversal. It takes the kind of traversal as a parameter of type Traversal, an enumerated constant with values such as CHILDREN (to traverse the glyph’s immediate children only), PREORDER (to traverse the entire structure in preorder), POSTORDER, and INORDER. Next advances to the next glyph in the traversal, and IsDone reports whether the traversal is over or not. GetCurrent replaces the Child operation; it accesses the current glyph in the traversal. Insert replaces the old operation; it inserts the given glyph at the current position.

An analysis would use the following C++ code to do a preorder traversal of a glyph structure rooted at g:

Glyph\* g;   
for (g->First(PREORDER); !g->IsDone(); g->Next()) {   
Glyph\* current = g->GetCurrent ();   
// dosome analysis

Notice that we’ve banished the integer index from the glyph interface. There’s no longer anything that biases the interface toward one kind of collection or another. We’ve also saved clients from having to implement common kinds of traversals themselves.

But this approach still has problems. For one thing, it can’t support new traversals without either extending the set of enumerated values or adding new operations. Say we wanted to have a variation on preorder traversal that automatically skips non-textual glyphs. We’d have to change the Traversal enumeration to include something like TEXTUAL\_PREORDER.

We’d like to avoid changing existing declarations. Putting the traversal mechanism entirely in the Glyph class hierarchy makes it hard to modify or extend without changing lots of classes. It’s also difficult to reuse the mechanism to traverse other kinds of object structures. And we can’t have more than one traversal in progress on a structure.

Once again, a better solution is to encapsulate the concept that varies, in this case the access and traversal mechanisms. We can introduce a class of objects called iterators whose sole purpose is to define different sets of these mechanisms. We can use inheritance to let us access different data structures uniformly and support new kinds of traversals as well. And we won’t have to change glyph interfaces or disturb existing glyph implementations to do it.

## Iterator Class and Subclasses

We’ll use an abstract class called Iterator to define a general interface for access and traversal. Concrete subclasses like ArrayIterator and ListIterator implement the interface to provide access to arrays and lists, while PreorderIterator, PostorderIterator, and the like implement different traversals on specific structures. Each Iterator subclass has a reference to the structure it traverses. Subclass instances are initialized with this reference when they are created. Figure 2.13 illustrates the Iterator class along with several subclasses. Notice that we’ve added a CreateIterator abstract operation to the Glyph class interface to support iterators.

## Figure 2.13: Iterator class and subclasses

![](images/dcd24716dfcfc08e8a1915d4110bc37a1036d9464adeb6439748ac107a1b985a.jpg)

The Iterator interface provides operations First, Next, and IsDone for controlling the traversal. The ListIterator class implements First to point to the first element in the list, and Next advances the iterator to the next item in the list. IsDone returns whether or not the list pointer points beyond the last element in the list. CurrentItem dereferences the iterator to return the glyph it points to. An ArrayIterator class would do similar things but on an array of glyphs.

Now we can access the children of a glyph structure without knowing its representation:

Glyph\* g;   
Iterator<Glyph\*>\* i = g->CreateIterator();   
for(i->First(); !i->IsDone(); i->Next()){   
Glyph\*child = i->CurrentItem();   
// do something with current child

CreateIterator returns a NullIterator instance by default. A NullIterator is a degenerate iterator for glyphs that have no children, that is, leaf glyphs. NullIterator’s IsDone operation always returns true.

A glyph subclass that has children will override CreateIterator to return an instance of a different Iterator subclass. Which subclass depends on the structure that stores the children. If the Row subclass of Glyph stores its children in a list \_children, then its CreateIterator operation would look like this:

Iterator<Glyph\*>\* Row::CreateIterator () {   
return new ListIterator<Glyph\*>(\_children);

Iterators for preorder and inorder traversals implement their traversals in terms of glyph-specific iterators. The iterators for these traversals are supplied the root glyph in the structure they traverse. They call CreateIterator on the glyphs in the structure and use a stack to keep track of the resulting iterators.

For example, class PreorderIterator gets the iterator from the root glyph, initializes it to point to its first element, and then pushes it onto the stack:

void PreorderIterator::First () {   
Iterator<Glyph\*>\*i= \_root->CreateIterator();   
if (i) {   
i->First();   
\_iterators.RemoveAll();   
\_iterators.Push(i);

CurrentItem would simply call CurrentItem on the iterator at the top of the stack:

Glyph\* PreorderIterator::CurrentItem () const {   
return   
\_iterators.Size() > 0?   
\_iterators.Top()->CurrentItem(): 0;   
}

The Next operation gets the top iterator on the stack and asks its current item to create an iterator, in an effort to descend the glyph structure as far as possible (this is a preorder traversal, after all). Next sets the new iterator to the first item in the traversal and pushes it on the stack. Then Next tests the latest iterator; if its IsDone operation returns true, then we’ve finished traversing the current subtree (or leaf) in the traversal. In that case, Next pops the top iterator off the stack and repeats this process until it finds the next incomplete traversal, if there is one; if not, then we have finished traversing the structure.

void PreorderIterator::Next (){   
Iterator<Glyph\*>\* i =   
\_iterators.Top()->CurrentItem()->CreateIterator();   
i->First();   
\_iterators.Push(i);   
while(   
\_iterators.Size() >0&& \_iterators.Top()->IsDone()   
delete \_iterators.Pop();   
\_iterators.Top()->Next();   
}

Notice how the Iterator class hierarchy lets us add new kinds of traversals without modifying glyph classes—we simply subclass Iterator and add a new traversal as we have with PreorderIterator. Glyph subclasses use the same interface to give clients access to their children without revealing the underlying data structure they use to store them. Because iterators store their own copy of the state of a traversal, we can carry on multiple traversals simultaneously, even on the same structure. And though our traversals have been over glyph structures in this example, there’s no reason we can’t parameterize a class like PreorderIterator by the type of object in the structure. We’d use templates to do that in C++. Then we can reuse the machinery in PreorderIterator to traverse other structures.

