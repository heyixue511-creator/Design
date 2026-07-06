# Foundation Classes / C.1 List / Construction, Destruction, Initialization, and Assignment / List(long size) / List(List&) / \~List() / List& operator=(const List&) / Accessing / Adding / Removing / Stack Interface / void Push(const Item&) / Item& Pop() / C.2 Iterator / virtual void First() / virtual void Next() / virtual bool IsDone() const / virtual Item CurrentItem() const / C.3 ListIterator / C.4 Point / typedef float Coord; / C.5 Rect

> Section: body | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

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
List (List&);   
"List();   
List& operator=(const List&);   
long Count() const;   
Item& Get(long index) const;   
Item& First() const;   
Item& Last() const;   
bool Includes(const Item&) const;   
void Append(const Item&);   
void Prepend(const Item&);   
void Remove(const Item&);   
void RemoveLast();   
void RemoveFirst();   
void RemoveAll();   
Item& Top()const;   
void Push(const Item&);   
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
virtual void First() = 0;   
virtual void Next() = 0;   
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

template <class Item>   
class ListIterator : public Iterator<Item> {   
public:   
ListIterator(const List<Item>\* aList);   
virtual void First();   
virtual void Next();   
virtual bool IsDone() const;   
virtual Item CurrentItem() const;   
};

## C.4 Point

Point represents a point in a two-dimensional Cartesian coordinate space. Point supports some minimal vector arithmetic. The coordinates of a Point are defined as

## typedef float Coord;

Point’s operations are self-explanatory.

class Point {  
public:  
static const Point Zero;  
Point(Coord x = 0.0, Coord y = 0.0);  
Coord x() const; void x(Coordx);  
Coord Y() const; void Y(Coord y);  
friend Point operator+(const Point&, const Point&);  
friend Point operator-(constPoint&, const Point&);  
friend Point operator\*(const Point&, const Point&);  
friend Point operator/(const Point&, const Point&);  
Point& operator+=(const Point&);  
Point& operator-=(const Point&);  
Point& operator\*=(constPoint&);  
Point& operator/=(const Point&);  
Point operator-();  
friend bool operator==(const Point&, const Point&);  
friend bool operator!=(const Point&, const Point&);  
friend ostream& operator<<(ostream&, const Point&);  
friend istream& operator>>(istream&, Point&);

The static member Zero represents Point (0, 0).

## C.5 Rect

Rect represents an axis-aligned rectangle. A Rect is defined by an origin point and

an extent (that is, width and height). The Rect operations are self-explanatory.

class Rect {  
public:  
static const Rect Zero;  
Rect(Coord x, Coord y, Coord w, Coord h);  
Rect(constPoint& origin, const Point& extent);  
Coord Width() const; void Width(Coord);  
Coord Height() const; void Height(Coord);  
Coord Left() const; void Left(Coord);  
Coord Bottom() const; void Bottom(Coord);  
Point& Origin() const; void Origin(const Point&);  
Point& Extent() const; void Extent(const Point&);  
void MoveTo(const Point&);  
void MoveBy(const Point&);  
bool IsEmpty()const;  
bool Contains(const Point&)const;  
};

The static member Zero is equivalent to the rectangle

Rect(Point(0, 0), Point(0, 0));

