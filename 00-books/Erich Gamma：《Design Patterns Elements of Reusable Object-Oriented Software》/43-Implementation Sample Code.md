BorderedScrollableTextView, BorderedTextView). This gives rise to many classes and increases the complexity of a system. Furthermore, providing different Decorator classes for a specific Component class lets you mix and match responsibilities.

Decorators also make it easy to add a property twice. For example, to give a TextView a double border, simply attach two BorderDecorators. Inheriting from a Border class twice is error-prone at best.

2 . Avoids feature-laden classes high up in the hierarchy. Decorator offers a pay-as-you-go approach to adding responsibilities. Instead of trying to support all foreseeable features in a complex, customizable class, you can define a simple class and add functionality incrementally with Decorator objects. Functionality can be composed from simple pieces. As a result, an application needn’t pay for features it doesn’t use. It’s also easy to define new kinds of Decorators independently from the classes of objects they extend, even for unforeseen extensions. Extending a complex class tends to expose details unrelated to the responsibilities you’re adding.

3 . A decorator and its component aren’t identical. A decorator acts as a transparent enclosure. But from an object identity point of view, a decorated component is not identical to the component itself. Hence you shouldn’t rely on object identity when you use decorators.

4 . Lots of little objects. A design that uses Decorator often results in systems composed of lots of little objects that all look alike. The objects differ only in the way they are interconnected, not in their class or in the value of their variables. Although these systems are easy to customize by those who understand them, they can be hard to learn and debug.

## Implementation

Several issues should be considered when applying the Decorator pattern:

1 . Interface conformance. A decorator object’s interface must conform to the interface of the component it decorates. ConcreteDecorator classes must therefore inherit from a common class (at least in C++).

2. Omitting the abstract Decorator class. There’s no need to define an abstract Decorator class when you only need to add one responsibility. That’s often the case when you’re dealing with an existing class hierarchy rather than designing a new one. In that case, you can merge Decorator’s responsibility for forwarding requests to the component into the ConcreteDecorator.

3. Keeping Component classes lightweight. To ensure a conforming interface, components and decorators must descend from a common Component class. It’s important to keep this common class lightweight; that is, it should focus on defining an interface, not on storing data. The definition of the data representation should be deferred to subclasses; otherwise the complexity of the Component class might make the decorators too heavyweight to use in quantity. Putting a lot of functionality into Component also increases the probability that concrete subclasses will pay for features they don’t need.

4. Changing the skin of an object versus changing its guts. We can think of a decorator as a skin over an object that changes its behavior. An alternative is to change the object’s guts. The Strategy (315) pattern is a good example of a pattern for changing the guts.

Strategies are a better choice in situations where the Component class is intrinsically heavyweight, thereby making the Decorator pattern too costly to apply. In the Strategy pattern, the component forwards some of its behavior to a separate strategy object. The Strategy pattern lets us alter or extend the component’s functionality by replacing the strategy object.

For example, we can support different border styles by having the component defer border-drawing to a separate Border object. The Border object is a Strategy object that encapsulates a border-drawing strategy. By extending the number of strategies from just one to an open-ended list, we achieve the same effect as nesting decorators recursively.

In MacApp 3.0 [App89] and Bedrock [Sym93a], for example, graphical components (called “views”) maintain a list of “adorner” objects that can attach additional adornments like borders to a view component. If a view has any adorners attached, then it gives them a chance to draw additional embellishments. MacApp and Bedrock must use this approach because the View class is heavyweight. It would be too expensive to use a full-fledged View just to add a border.

Since the Decorator pattern only changes a component from the outside, the component doesn’t have to know anything about its decorators; that is, the decorators are transparent to the component:

![](images/1b86edf21808d4751784f6dbf66e2ee75792510d1dc098babc012e9dbdc125a0.jpg)

With strategies, the component itself knows about possible extensions. So it has to reference and maintain the corresponding strategies:

![](images/d8b9aaaac2c878f8d279858ddef2ab14236aa30303680c29a52e9a1fa29df20c.jpg)

The Strategy-based approach might require modifying the component to accommodate new extensions. On the other hand, a strategy can have its own specialized interface, whereas a decorator’s interface must conform to the component’s. A strategy for rendering a border, for example, need only define the interface for rendering a border (DrawBorder, GetWidth, etc.), which means that the strategy can be lightweight even if the Component class is heavyweight.

MacApp and Bedrock use this approach for more than just adorning views. They also use it to augment the event-handling behavior of objects. In both systems, a view maintains a list of “behavior” objects that can modify and intercept events. The view gives each of the registered behavior objects a chance to handle the event before nonregistered behaviors, effectively overriding them. You can decorate a view with special keyboard-handling support, for example, by registering a behavior object that intercepts and handles key events.

## Sample Code

The following code shows how to implement user interface decorators in C++. We’ll assume there’s a Component class called VisualComponent.

class VisualComponent {   
public:   
VisualComponent();   
virtual void Draw();   
virtual void Resize();

We define a subclass of VisualComponent called Decorator, which we’ll subclass to obtain different decorations.

class Decorator : public VisualComponent {   
public:   
Decorator(VisualComponent\*);   
virtual void Draw();   
virtual void Resize();   
private:   
VisualComponent\*\_component;   
};

Decorator decorates the VisualComponent referenced by the \_component instance variable, which is initialized in the constructor. For each operation in VisualComponent’s interface, Decorator defines a default implementation that passes the request on to \_component:

void Decorator::Draw(){   
\_component->Draw();   
  
voidDecorator::Resize(){   
\_component->Resize();   
}

Subclasses of Decorator define specific decorations. For example, the class BorderDecorator adds a border to its enclosing component. BorderDecorator is a subclass of Decorator that overrides the Draw operation to draw the border. BorderDecorator also defines a private DrawBorder helper operation that does the drawing. The subclass inherits all other operation implementations from Decorator.

class BorderDecorator : public Decorator {   
public:   
BorderDecorator(VisualComponent\*,int borderWidth);   
virtual void Draw();   
private:   
void DrawBorder(int);   
private:   
int \_width;   
};   
void BorderDecorator::Draw()(   
Decorator::Draw();   
DrawBorder(\_width);   
}

A similar implementation would follow for ScrollDecorator and DropShadowDecorator, which would add scrolling and drop shadow capabilities to a visual component.