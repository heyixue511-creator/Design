subject. In that case, a change in two or more subjects might cause redundant updates.   
The DAGChangeManager ensures the observer receives just one update.   
SimpleChangeManager is fine when multiple updates aren’t an issue.

![](images/5d64a6deba0a0186f0a95f909d9a3f2e6dcc8af9b584397d4872c933e756dd0e.jpg)

ChangeManager is an instance of the Mediator (273) pattern. In general there is only one ChangeManager, and it is known globally. The Singleton (127) pattern would be useful here.

9 . Combining the Subject and Observer classes. Class libraries written in languages that lack multiple inheritance (like Smalltalk) generally don’t define separate Subject and Observer classes but combine their interfaces in one class. That lets you define an object that acts as both a subject and an observer without multiple inheritance. In Smalltalk, for example, the Subject and Observer interfaces are defined in the root class Object, making them available to all classes.

## Sample Code

An abstract class defines the Observer interface:

class Observer {   
public:   
virtual "Observer();   
virtual void Update(Subject\*theChangedSubject)= 0;   
protected:   
Observer();   
};

This implementation supports multiple subjects for each observer. The subject passed to the Update operation lets the observer determine which subject changed when it observes more than one.

Similarly, an abstract class defines the Subject interface:

class Subject {   
public:   
virtualSubject();   
virtual void Attach(Observer\*);   
virtual void Detach(Observer\*);   
virtual void Notify();   
protected:   
Subject();   
private:   
List<Observer\*>\*\_observers;   
};   
void Subject::Attach(Observer\* o){   
\_observers->Append(o);   
voidSubject::Detach(Observer\*o){   
\_observers->Remove(o);   
void Subject::Notify () {   
ListIterator<Observer\*>i(\_observers);   
for (i.First(); !i.IsDone(); i.Next()) {   
i.CurrentItem()->Update(this);

ClockTimer is a concrete subject for storing and maintaining the time of day. It notifies its observers every second. ClockTimer provides the interface for retrieving individual time units such as the hour, minute, and second.

class ClockTimer : public Subject {   
public:   
ClockTimer();   
virtualint GetHour();   
virtualint GetMinute();   
virtualint GetSecond();   
void Tick();   
);

The Tick operation gets called by an internal timer at regular intervals to provide an accurate time base. Tick updates the ClockTimer’s internal state and calls Notify to inform observers of the change:

void ClockTimer::Tick () {   
// update internal time-keeping state   
Notify();   
1

Now we can define a class DigitalClock that displays the time. It inherits its graphical functionality from a Widget class provided by a user interface toolkit. The Observer interface is mixed into the DigitalClock interface by inheriting from Observer.

class DigitalClock: public Widget, public Observer {   
public:   
DigitalClock(ClockTimer\*);   
virtual"DigitalClock();   
virtual void Update(Subject\*);   
//overrides Observer operation   
virtual void Draw();   
// overrides Widget operation;   
//defines how to draw the digital clock   
private:   
ClockTimer\*\_subject;   
};   
DigitalClock::DigitalClock (ClockTimer\* s){   
\_subject= s;   
\_subject->Attach(this);   
}   
DigitalClock::"DigitalClock (){   
\_subject->Detach(this);   
}

Before the Update operation draws the clock face, it checks to make sure the notifying subject is the clock’s subject:

void DigitalClock::Update (Subject\* theChangedSubject){   
if (theChangedSubject == \_subject) {   
Draw();   
}   
void DigitalClock::Draw() {   
// get the new values from the subject   
inthour = \_subject->GetHour();   
int minute = \_subject->GetMinute();   
// etc.   
// draw the digitalclock   
3

An AnalogClock class can be defined in the same way.

class AnalogClock : public Widget, public Observer {   
public:   
AnalogClock(ClockTimer\*);   
virtualvoid Update(Subject\*);   
virtualvoid Draw();   
);

The following code creates an AnalogClock and a DigitalClock that always show the same time:

ClockTimer\* timer = new ClockTimer;   
AnalogClock\*analogClock = newAnalogClock(timer);   
DigitalClock\* digitalclock = new DigitalClock(timer);

Whenever the timer ticks, the two clocks will be updated and will redisplay themselves appropriately.

## Known Uses

The first and perhaps best-known example of the Observer pattern appears in Smalltalk Model/View/Controller (MVC), the user interface framework in the Smalltalk environment [KP88]. MVC’s Model class plays the role of Subject, while View is the base class for observers. Smalltalk, ET++ [WGM88], and the THINK class library [Sym93b] provide a general dependency mechanism by putting Subject and Observer interfaces in the parent class for all other classes in the system.

Other user interface toolkits that employ this pattern are Interviews [LVC89], the Andrew Toolkit [P+88], and Unidraw [VL90]. Interviews defines Observer and Observable (for subjects) classes explicitly. Andrew calls them “view” and “data object,” respectively. Unidraw splits graphical editor objects into View (for observers) and Subject parts.

## Related Patterns

Mediator (273): By encapsulating complex update semantics, the ChangeManager acts as mediator between subjects and observers.

Singleton (127): The ChangeManager may use the Singleton pattern to make it unique and globally accessible.

## Object Behavioral: State

## Intent