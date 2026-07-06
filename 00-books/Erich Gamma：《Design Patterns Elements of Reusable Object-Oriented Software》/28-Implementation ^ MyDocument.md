![](images/c5cc06942060fdc657235d50218d6e0f61b22ad01312f5f35da186eccaf3ccb3.jpg)

The Figure class provides a CreateManipulator factory method that lets clients create a Figure’s corresponding Manipulator. Figure subclasses override this method to return an instance of the Manipulator subclass that’s right for them. Alternatively, the Figure class may implement CreateManipulator to return a default Manipulator instance, and Figure subclasses may simply inherit that default. The Figure classes that do so need no corresponding Manipulator subclass—hence the hierarchies are only partially parallel.

Notice how the factory method defines the connection between the two class hierarchies. It localizes knowledge of which classes belong together.

## Implementation

Consider the following issues when applying the Factory Method pattern:

1. Two major varieties. The two main variations of the Factory Method pattern are (1) the case when the Creator class is an abstract class and does not provide an implementation for the factory method it declares, and (2) the case when the Creator is a concrete class and provides a default implementation for the factory method. It’s also possible to have an abstract class that defines a default implementation, but this is less common.

The first case requires subclasses to define an implementation, because there’s no reasonable default. It gets around the dilemma of having to instantiate unforeseeable classes. In the second case, the concrete Creator uses the factory method primarily for flexibility. It’s following a rule that says, “Create objects in a separate operation so that subclasses can override the way they’re created.” This rule ensures that designers of subclasses can change the class of objects their parent class instantiates if necessary.

2 . Parameterized factory methods. Another variation on the pattern lets the factory method create multiple kinds of products. The factory method takes a parameter that identifies the kind of object to create. All objects the factory method creates will share the Product interface. In the Document example, Application might support different kinds of Documents. You pass Create-Document an extra parameter to specify the kind of document to create.

The Unidraw graphical editing framework [VL90] uses this approach for reconstructing objects saved on disk. Unidraw defines a Creator class with a factory method Create that takes a class identifier as an argument. The class identifier specifies the class to instantiate. When Unidraw saves an object to disk, it writes out the class identifier first and then its instance variables. When it reconstructs the object from disk, it reads the class identifier first.

Once the class identifier is read, the framework calls Create, passing the identifier as the parameter. Create looks up the constructor for the corresponding class and uses it to instantiate the object. Last, Create calls the object’s Read operation, which reads the remaining information on the disk and initializes the object’s instance variables.

A parameterized factory method has the following general form, where MyProduct and YourProduct are subclasses of Product:

class Creator {   
public:   
virtual Product\*Create(ProductId);   
Product\* Creator::Create (ProductId id) {   
if(id == MINE) return new MyProduct;   
if(id == YOURS) return new YourProduct;   
// repeat for remaining products...   
return 0;   
}

Overriding a parameterized factory method lets you easily and selectively extend or change the products that a Creator produces. You can introduce new identifiers for new kinds of products, or you can associate existing identifiers with different products.

For example, a subclass MyCreator could swap MyProduct and YourProduct and support a new TheirProduct subclass:

Product\* MyCreator::Create (ProductId id){   
if (id == YOURS) return new MyProduct;   
if (id == MINE) return new YourProduct;   
// N.B.: switchedYOURS and MINE   
if (id == THEIRS) return new TheirProduct;   
return Creator::Create(id); // called if all others fail

Notice that the last thing this operation does is call Create on the parent class.

clientMethod   
document := self documentclass new.   
documentClass   
selfsubclassResponsibility   
In class MyApplication we have   
documentClass

That’s because MyCreator::Create handles only YOURS, MINE, and THEIRS differently than the parent class. It isn’t interested in other classes. Hence MyCreator extends the kinds of products created, and it defers responsibility for creating all but a few products to its parent.

3. Language-specific variants and issues. Different languages lend themselves to other interesting variations and caveats.

Smalltalk programs often use a method that returns the class of the object to be instantiated. A Creator factory method can use this value to create a product, and a ConcreteCreator may store or even compute this value. The result is an even later binding for the type of ConcreteProduct to be instantiated.

A Smalltalk version of the Document example can define a documentClass method on Application. The documentClass method returns the proper Document class for instantiating documents. The implementation of documentClass in MyApplication returns the MyDocument class. Thus in class Application we have

## ^ MyDocument

which returns the class MyDocument to be instantiated to Application.

An even more flexible approach akin to parameterized factory methods is to store the class to be created as a class variable of Application. That way you don’t have to subclass Application to vary the product.

Factory methods in C++ are always virtual functions and are often pure virtual. Just be careful not to call factory methods in the Creator’s constructor—the factory method in the ConcreteCreator won’t be available yet.

You can avoid this by being careful to access products solely through accessor operations that create the product on demand. Instead of creating the concrete product in the constructor, the constructor merely initializes it to 0. The accessor returns the product. But first it checks to make sure the product exists, and if it doesn’t, the accessor creates it. This technique is sometimes called lazy initialization. The following code shows a typical implementation:

class Creator {   
public:   
Product\* GetProduct() ;   
protected:   
virtual Product\*CreateProduct();   
private:   
Product\*\_product;   
};   
Product\*Creator::GetProduct () {   
if (\_product == 0) {   
\_product = CreateProduct();   
return \_product;   
}

4. Using templates to avoid subclassing. As we’ve mentioned, another potential problem with factory methods is that they might force you to subclass just to create the appropriate Product objects. Another way to get around this in C++ is to provide a template subclass of Creator that’s parameterized by the Product class:

class Creator {   
public:   
virtual Product\* CreateProduct() = 0;   
};   
template <class TheProduct>   
class StandardCreator: public Creator {   
public:   
virtual Product\* CreateProduct();   
template <class TheProduct>   
Product\*StandardCreator<TheProduct>::CreateProduct () {   
return new TheProduct;   
}

With this template, the client supplies just the product class—no subclassing of Creator is required.

class MyProduct : public Product {   
public:   
MyProduct ();   
};   
StandardCreator<MyProduct> myCreator;

5. Naming conventions. It’s good practice to use naming conventions that make it clear you’re using factory methods. For example, the MacApp Macintosh application framework [App89] always declares the abstract operation that defines the factory method as Class\* DoMakeClass(), where Class is the Product class.