• there are many dependencies between clients and the implementation classes of an abstraction. Introduce a facade to decouple the subsystem from clients and other subsystems, thereby promoting subsystem independence and portability.

• you want to layer your subsystems. Use a facade to define an entry point to each subsystem level. If subsystems are dependent, then you can simplify the dependencies between them by making them communicate with each other solely through their facades.

## Structure

![](images/9858c694151664f59e46eefe99597a7e3a7e65733b61a6b6888336c7f83981d8.jpg)

## Participants

• Facade (Compiler)

– knows which subsystem classes are responsible for a request.

– delegates client requests to appropriate subsystem objects.

• subsystem classes (Scanner, Parser, ProgramNode, etc.)

– implement subsystem functionality.

– handle work assigned by the Facade object.

– have no knowledge of the facade; that is, they keep no references to it.

## Collaborations

• Clients communicate with the subsystem by sending requests to Facade, which forwards them to the appropriate subsystem object(s). Although the subsystem objects perform the actual work, the facade may have to do work of its own to translate its interface to subsystem interfaces.

• Clients that use the facade don’t have to access its subsystem objects directly.

## Consequences

The Facade pattern offers the following benefits:

1. It shields clients from subsystem components, thereby reducing the number of objects that clients deal with and making the subsystem easier to use.

2 . It promotes weak coupling between the subsystem and its clients. Often the components in a subsystem are strongly coupled. Weak coupling lets you vary the components of the subsystem without affecting its clients. Facades help layer a system and the dependencies between objects. They can eliminate complex or circular dependencies. This can be an important consequence when the client and the subsystem are implemented independently.

Reducing compilation dependencies is vital in large software systems. You want to save time by minimizing recompilation when subsystem classes change. Reducing compilation dependencies with facades can limit the re-compilation needed for a small change in an important subsystem. A facade can also simplify porting systems to other platforms, because it’s less likely that building one subsystem requires building all others.

3. It doesn’t prevent applications from using subsystem classes if they need to. Thus you can choose between ease of use and generality.

## Implementation

Consider the following issues when implementing a facade:

1 . Reducing client-subsystem coupling. The coupling between clients and the subsystem can be reduced even further by making Facade an abstract class with concrete subclasses for different implementations of a subsystem. Then clients can communicate with the subsystem through the interface of the abstract Facade class. This abstract coupling keeps clients from knowing which implementation of a subsystem is used.

An alternative to subclassing is to configure a Facade object with different subsystem objects. To customize the facade, simply replace one or more of its subsystem objects.

2. Public versus private subsystem classes. A subsystem is analogous to a class in that both have interfaces, and both encapsulate something—a class encapsulates state and operations, while a subsystem encapsulates classes. And just as it’s useful to think of the public and private interface of a class, we can think of the public and private interface of a subsystem.

The public interface to a subsystem consists of classes that all clients can access; the private interface is just for subsystem extenders. The Facade class is part of the public interface, of course, but it’s not the only part. Other subsystem classes are usually public as well. For example, the classes Parser and Scanner in the compiler subsystem are part of the public interface.

Making subsystem classes private would be useful, but few object-oriented languages support it. Both C++ and Smalltalk traditionally have had a global name space for classes. Recently, however, the C++ standardization committee added name spaces to the language [Str94], which will let you expose just the public subsystem classes.

## Sample Code

Let’s take a closer look at how to put a facade on a compiler subsystem.

The compiler subsystem defines a BytecodeStream class that implements a stream of Bytecode objects. A Bytecode object encapsulates a bytecode, which can specify machine instructions. The subsystem also defines a Token class for objects that encapsulate tokens in the programming language.

The Scanner class takes a stream of characters and produces a stream of tokens, one token at a time.

class Scanner {   
public:   
Scanner(istream&);   
virtual\~Scanner();   
virtual Token& Scan();   
private:   
istream& \_inputStream;   
);

The class Parser uses a ProgramNodeBuilder to construct a parse tree from a Scanner’s tokens.

class Parser {   
public:   
Parser();   
virtual \~Parser();   
virtualvoidParse(Scanner&, ProgramNodeBuilder&);   
);

Parser calls back on ProgramNodeBuilder to build the parse tree incrementally. These classes interact according to the Builder (97) pattern.

ass ProgramNodeBuilder{   
blic:   
ProgramNodeBuilder();   
virtualProgramNode\* NewVariable(   
const char\*variableName   
) const;   
virtual ProgramNode\* NewAssignment(   
ProgramNode\* variable, ProgramNode\* expression   
) const;   
virtualProgramNode\* NewReturnStatement(   
ProgramNode\*value   
) const;   
virtualProgramNode\* NewCondition(   
ProgramNode\*condition,   
ProgramNode\*truePart,ProgramNode\*falsePart   
) const;   
ProgramNode\*GetRootNode();   
private:   
ProgramNode\* \_node;

The parse tree is made up of instances of ProgramNode subclasses such as StatementNode, ExpressionNode, and so forth. The ProgramNode hierarchy is an example of the Composite (163) pattern. ProgramNode defines an interface for manipulating the program node and its children, if any.

class ProgramNode {   
public:   
// program node manipulation   
virtual void GetSourcePosition(int& line, int& index);   
// child manipulation   
virtual void Add(ProgramNode\*);   
virtualvoid Remove(ProgramNode\*);   
virtualvoid Traverse(CodeGenerator&);   
protected:   
ProgramNode();   
);

The Traverse operation takes a CodeGenerator object. ProgramNode subclasses use this object to generate machine code in the form of Bytecode objects on a BytecodeStream. The class CodeGenerator is a visitor (see Visitor (331)).

class CodeGenerator {   
public:   
virtual void Visit(StatementNode\*);   
virtualvoid Visit(ExpressionNode\*);   
protected:   
CodeGenerator(BytecodeStream&);   
protected:   
BytecodeStream&\_output;   
};

CodeGenerator has subclasses, for example, StackMachineCodeGenerator and RISCCodeGenerator, that generate machine code for different hardware architectures.

Each subclass of ProgramNode implements Traverse to call Traverse on its child ProgramNode objects. In turn, each child does the same for its children, and so on recursively. For example, ExpressionNode defines Traverse as follows:

void ExpressionNode::Traverse (CodeGenerator& cg) (   
cg.Visit(this);   
ListIterator<ProgramNode\*> i(\_children);   
for (i.First(); !i.IsDone(); i.Next()) {   
i.CurrentItem()->Traverse(cg);

The classes we’ve discussed so far make up the compiler subsystem. Now we’ll introduce a Compiler class, a facade that puts all these pieces together. Compiler provides a simple interface for compiling source and generating code for a particular machine.

class Compiler {   
public:   
Compiler();   
virtualvoid Compile(istream&,BytecodeStream&);   
void Compiler::Compile (   
istream&input, BytecodeStream& output   
Scanner scanner(input);   
ProgramNodeBuilder builder;   
Parser parser;   
parser.Parse(scanner,builder);   
RISCCodeGeneratorgenerator(output);   
ProgramNode\*parseTree = builder.GetRootNode();   
parseTree->Traverse(generator);   
)