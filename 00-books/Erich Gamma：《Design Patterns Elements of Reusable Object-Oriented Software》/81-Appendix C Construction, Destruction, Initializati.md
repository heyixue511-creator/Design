# Appendix C

## Foundation Classes

This appendix documents the foundation classes we use in the C++ sample code of several design patterns. We’ve intentionally kept the classes simple and minimal. We describe the following classes:

• List, an ordered list of objects.

• Iterator, the interface for accessing an aggregate’s objects in a sequence.

• ListIterator, an iterator for traversing a List.

• Point, a two-dimensional point.

• Rect, an axis-aligned rectangle.

Some newer C++ standard types may not be available on all compilers. In particular, if your compiler doesn’t define bool, then define it manually as

typedef int bool;   
const int true = 1;   
const int false = 0;

## C.1 List

The List class template provides a basic container for storing an ordered list of objects. List stores elements by value, which means it works for built-in types as well as class instances. For example, List<int> declares a list of ints. But most of the patterns use List to store pointers to objects, as in List<Glyph\*>. That way List can be used for heterogeneous lists.

For convenience, List also provides synonyms for stack operations, which make code that uses List for stacks more explicit without defining another class.

template <class Item>   
class List {   
public:   
List(long size = DEFAULT\_LIST\_CAPACITY);   
List(List&);   
"List();   
List& operator=(const List&);   
long Count() const;   
Item& Get(long index) const;   
Item& First() const;   
Item& Last() const;   
bool Includes(const Item&) const;   
void Append(constItem&);   
void Prepend(const Item&);   
void Remove(const Item&);   
void RemoveLast();   
void RemoveFirst();   
void RemoveAll();   
Item& Top() const;   
void Push(constItem&);   
Item& Pop();   
};

The following sections describe these operations in greater detail.

## Construction, Destruction, Initialization, and Assignment

## List(long size)

initializes the list. The size parameter is a hint for the initial number of elements.

## List(List&)

overrides the default copy constructor so that member data are initialized properly.

## \~List()

frees the list’s internal data structures but not the elements in the list. The class is not designed for subclassing; therefore the destructor isn’t virtual.

## List& operator=(const List&)

implements the assignment operation to assign member data properly.

## Accessing

long Count() const returns the number of objects in the list.

Item& Get (long index) const returns the object at the given index.

Item& First() const returns the first object in the list.

Item& Last() const returns the last object in the list.

## Adding

void Append(const Item&) adds the argument to the list, making it the last element.

void Prepend(const Item&) adds the argument to the list, making it the first element.

## Removing

removes the given element from the list. This operation requires that the type of elements in the list supports the == operator for comparison.

## Stack Interface

returns the top element (when the List is viewed as a stack).

## void Push(const Item&)

pushes the element onto the stack.

## Item& Pop()

pops the top element from the stack.

## C.2 Iterator

Iterator is an abstract class that defines a traversal interface for aggregates.

template <class Item>   
class Iterator {   
public:   
virtual void First()= 0;   
virtualvoid Next() = 0;   
virtual bool IsDone() const = 0;   
virtual Item CurrentItem() const = 0;   
protected:   
Iterator();

The operations do the following:

## virtual void First()

positions the iterator to the first object in the aggregate.

## virtual void Next()

positions the iterator to the next object in the sequence.

## virtual bool IsDone() const

returns true when there are no more objects in the sequence.

## virtual Item CurrentItem() const

returns the object at the current position in the sequence.

## C.3 ListIterator

ListIterator implements the Iterator interface to traverse List objects. Its constructor takes a list to traverse as an argument.