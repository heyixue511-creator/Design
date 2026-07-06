require arguments, we can use C++ templates to avoid creating a Command subclass for every kind of action and receiver. We show how to do this in the Sample Code section.

## Sample Code

The C++ code shown here sketches the implementation of the Command classes in the Motivation section. We’ll define OpenCommand, PasteCommand, and MacroCommand. First the abstract Command class:

class Command {   
public:   
virtual \~Command();   
virtual void Execute() = 0;   
protected:   
Command();   
);

OpenCommand opens a document whose name is supplied by the user. An OpenCommand must be passed an Application object in its constructor. AskUser is an implementation routine that prompts the user for the name of the document to open.

class OpenCommand : public Command {   
public:   
OpenCommand(Application\*);   
virtual void Execute();   
protected:   
virtual const char\* AskUser();   
private:   
Application\*\_application;   
char\*response;   
OpenCommand::OpenCommand (Application\* a){   
\_application = a;   
void OpenCommand::Execute () {   
const char\* name = AskUser();   
if (name != 0) {   
Document\* document = new Document (name);   
\_application->Add(document);   
document->Open();   
}

A PasteCommand must be passed a Document object as its receiver. The receiver is given as a parameter to PasteCommand’s constructor.

class PasteCommand : public Command {   
public:   
PasteCommand(Document\*);   
virtual void Execute();   
private:   
Document\* \_document;   
};   
PasteCommand::PasteCommand (Document\* doc){   
\_document = doc;   
)   
void PasteCommand::Execute () {   
\_document->Paste();   
}

For simple commands that aren’t undoable and don’t require arguments, we can use a class template to parameterize the command’s receiver. We’ll define a template subclass SimpleCommand for such commands. SimpleCommand is parameterized by the Receiver type and maintains a binding between a receiver object and an action stored as a pointer to a member function.

template <class Receiver>   
class SimpleCommand : public Command {   
public:   
typedef void (Receiver::\*Action)();   
SimpleCommand(Receiver\*r, Action a):   
\_receiver(r), \_action(a) {}   
virtual void Execute();   
private:   
Action \_action;   
Receiver\* \_receiver;   
);

The constructor stores the receiver and the action in the corresponding instance variables. Execute simply applies the action to the receiver.

template <class Receiver>   
voidSimpleCommand<Receiver>::Execute()(   
(\_receiver->\*\_action)();   
}

To create a command that calls Action on an instance of class MyClass, a client simply writes

MyClass\* receiver = new MyClass;   
Command\* aCommand =   
new SimpleCommand<MyClass>(receiver,&MyClass::Action);   
aCommand->Execute();

Keep in mind that this solution only works for simple commands. More complex commands that keep track of not only their receivers but also arguments and/or undo state require a Command subclass.

A MacroCommand manages a sequence of subcommands and provides operations for adding and removing subcommands. No explicit receiver is required, because the subcommands already define their receiver.

class MacroCommand : public Command {   
public:   
MacroCommand();   
virtual\~MacroCommand();   
virtual void Add(Command\*);   
virtual void Remove(Command\*);   
virtual void Execute();   
private:   
List<Command\*>\*\_cmds;   
);

The key to the MacroCommand is its Execute member function. This traverses all the subcommands and performs Execute on each of them.

void MacroCommand::Execute () {   
ListIterator<Command\*>i(\_cmds);   
for (i.First(); !i.IsDone(); i,Next()){   
Command\* c = i.CurrentItem();   
c->Execute();   
)

Note that should the MacroCommand implement an Unexecute operation, then its subcommands must be unexecuted in reverse order relative to Execute’s implementation.

Finally, MacroCommand must provide operations to manage its subcommands. The MacroCommand is also responsible for deleting its subcommands.

void MacroCommand::Add(Command\* c){   
\_cmds->Append(c);   
void MacroCommand::Remove (Command\*c) {   
\_cmds->Remove(c);   
}

## Known Uses

Perhaps the first example of the Command pattern appears in a paper by Lieberman [Lie85]. MacApp [App89] popularized the notion of commands for implementing undoable operations. ET++ [WGM88], Interviews [LCI<sup>+</sup>92], and Unidraw [VL90] also define classes that follow the Command pattern. Interviews defines an Action abstract class that provides command functionality. It also defines an ActionCallback template, parameterized by action method, that can instantiate command subclasses automatically.

The THINK class library [Sym93b] also uses commands to support undoable actions. Commands in THINK are called “Tasks.” Task objects are passed along a Chain of Responsibility (223) for consumption.

Unidraw’s command objects are unique in that they can behave like messages. A Unidraw command may be sent to another object for interpretation, and the result of the interpration varies with the receiving object. Moreover, the receiver may delegate the interpretation to another object, typically the receiver’s parent in a larger structure as in a Chain of Responsibility. The receiver of a Unidraw command is thus computed rather than stored. Unidraw’s interpretation mechanism depends on run-time type information.

Coplien describes how to implement functors, objects that are functions, in C++ [Cop92]. He achieves a degree of transparency in their use by overloading the function call operator (operator()). The Command pattern is different; its focus is on maintaining a binding between a receiver and a function (i.e., action), not just maintaining a function.

## Related Patterns

A Composite (163) can be used to implement MacroCommands.

A Memento (283) can keep state the command requires to undo its effect.

A command that must be copied before being placed on the history list acts as a Prototype (117).

## Ciass Behavioral: Interpreter

## Intent

Given a language, define a represention for its grammar along with an interpreter that uses the representation to interpret sentences in the language.

## Motivation

If a particular kind of problem occurs often enough, then it might be worthwhile to express instances of the problem as sentences in a simple language. Then you can build an interpreter that solves the problem by interpreting these sentences.

For example, searching for strings that match a pattern is a common problem. Regular expressions are a standard language for specifying patterns of strings. Rather than building custom algorithms to match each pattern against strings, search algorithms could interpret a regular expression that specifies a set of strings to match.

The Interpreter pattern describes how to define a grammar for simple languages, represent sentences in the language, and interpret these sentences. In this example, the pattern describes how to define a grammar for regular expressions, represent a particular regular expression, and how to interpret that regular expression.

Suppose the following grammar defines the regular expressions:

expression ::= literal | alternation | sequencerepetition   
'('expression')'   
alternation ::= expression''expression   
sequence ::= expression'&' expression   
repetition ::= expression'\*.   
literal ::= ′a′| ′b′ | ′c′| .. {′a′|′b′ | ′c′| …. }\*

The symbol expression is the start symbol, and literal is a terminal symbol defining simple words

The Interpreter pattern uses a class to represent each grammar rule. Symbols on the right-hand side of the rule are instance variables of these classes. The grammar above is represented by five classes: an abstract class RegularExpression and its four subclasses LiteralExpression, AlternationExpression, SequenceExpression, and RepetitionExpression. The last three classes define variables that hold subexpressions.

![](images/f5aad069129d0311e0588f5d2fd2024a392e92575f9c154f02d890f207c8db8a.jpg)

Every regular expression defined by this grammar is represented by an abstract syntax tree made up of instances of these classes. For example, the abstract syntax tree