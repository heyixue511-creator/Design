contains a dog—no matter where the instance appears in the tree.

## Sample Code

Here are two examples. The first is a complete example in Smalltalk for checking whether a sequence matches a regular expression. The second is a C++ program for evaluating Boolean expressions.

The regular expression matcher tests whether a string is in the language defined by the regular expression. The regular expression is defined by the following grammar:

expression ::= literalalternation sequencerepetition   
'('expression')   
alternation ::= expression '' expression   
sequence ::= expression '&' expression   
repetition ::= expression'repeat'   
literal ::= ′a′ | ′b′ | ′c′ | …. { ′a′ | ′b′ | ′c′ | . }\*

This grammar is a slight modification of the Motivation example. We changed the concrete syntax of regular expressions a little, because symbol "\*" can’t be a postfix operation in Smalltalk. So we use repeat instead. For example, the regular expression

(('dog ' | 'cat ') repeat & 'weather')

matches the input string "dog dog cat weather".

To implement the matcher, we define the five classes described on page 243. The class SequenceExpression has instance variables expression1 and expression2 for its children in the abstract syntax tree. AlternationExpression stores its alternatives in the instance variables alternativel and alternative2, while RepetitionExpression holds the expression it repeats in its repetition instance variable. LiteralExpression has a components instance variable that holds a list of objects (probably characters). These represent the literal string that must match the input sequence.

The match: operation implements an interpreter for the regular expression. Each of the classes defining the abstract syntax tree implements this operation. It takes inputState as an argument representing the current state of the matching process, having read part of the input string.

This current state is characterized by a set of input streams representing the set of inputs that the regular expression could have accepted so far. (This is roughly equivalent to recording all states that the equivalent finite state automata would be in, having recognized the input stream to this point).

The current state is most important to the repeat operation. For example, if the regular expression were

## 'a' repeat

then the interpreter could match "a", "aa", "aaa", and so on. If it were

## 'a' repeat & 'be'

then it could match "abc", "aabc", "aaabc", and so on. But if the regular expression were

## 'a' repeat & 'abc'

then matching the input "aabc" against the subexpression "'a' repeat" would yield two input streams, one having matched one character of the input, and the other having matched two characters. Only the stream that has accepted one character will match the remaining "abc".

Now we consider the definitions of match: for each class defining the regular expression. The definition for SequenceExpression matches each of its subexpressions in sequence. Usually it will eliminate input streams from its inputState.

match:inputState   
expression2match:(expressionl match: inputState).

An AlternationExpression will return a state that consists of the union of states from either alternative. The definition of match: for AlternationExpression is

match: inputState   
finalState I   
finalState:=alternativel match: inputState.   
finalstate addAll: (alternative2 match: inputState).   
^finalState

The match: operation for RepetitionExpression tries to find as many states that could match as possible:

match:inputState   
aState finalstate |   
aState := inputState.   
finalState :=inputState copy.   
[aState isEmpty]   
whileFalse:   
[aState:=repetition match: aState.   
finalstate addAll: aState].   
finalState

Its output state usually contains more states than its input state, because a RepetitionExpression can match one, two, or many occurrences of repetition on the input state. The output states represent all these possibilities, allowing subsequent elements of the regular expression to decide which state is the correct one.

Finally, the definition of match: for LiteralExpression tries to match its components against each possible input stream. It keeps only those input streams that have a match:

match: inputState   
finalState tStream   
finalState := Set new.   
inputState   
do:   
[:stream | tStream := stream copy.   
(tStream nextAvailable:   
components size   
) = components   
ifTrue: [finalState add: tStream]   
1.   
finalState

The nextAvailable: message advances the input stream. This is the only match: operation that advances the stream. Notice how the state that’s returned contains a copy of the input stream, thereby ensuring that matching a literal never changes the input stream. This is important because each alternative of an AlternationExpression should see identical copies of the input stream.

Now that we’ve defined the classes that make up an abstract syntax tree, we can describe how to build it. Rather than write a parser for regular expressions, we’ll define some operations on the RegularExpression classes so that evaluating a Smalltalk expression will produce an abstract syntax tree for the corresponding regular expression. That lets us use the built-in Smalltalk compiler as if it were a parser for regular expressions.

To build the abstract syntax tree, we’ll need to define "|", "repeat", and "&" as operations on RegularExpression. These operations are defined in class RegularExpression like this:

& aNode   
SequenceExpression new   
expression1: self expression2: aNode asRExp   
repeat   
RepetitionExpression new repetition:self   
|aNode   
AlternationExpression new   
alternativel: self alternative2: aNode asRExp   
asRExp   
self

T h e asRExp operation will convert literals into RegularExpressions. These operations are defined in class String:

& aNode   
SequenceExpression new   
expressionl: self asRExp expression2: aNode asRExp   
repeat   
RepetitionExpression new repetition: self   
| aNode   
AlternationExpression new   
alternativel: self asRExp alternative2: aNode asRExp   
asRExp   
LiteralExpression new components: self

If we defined these operations higher up in the class hierarchy (Sequenceable-Collection in Smalltalk-80, IndexedCollection in Smalltalk/V), then they would also be defined for classes such as Array and OrderedCollection. This would let regular expressions match sequences of any kind of object.

The second example is a system for manipulating and evaluating Boolean expressions implemented in C++. The terminal symbols in this language are Boolean variables, that is, the constants true and false. Nonterminal symbols represent expressions containing the operators and, or, and not. The grammar is defined as follows<sup>1</sup>:

BooleanExp ::= VariableExp | Constant | OrExp| AndExp | NotExp|   
'(′BooleanExp')'   
AndExp ::= BooleanExp 'and' BooleanExp   
OrExp ::= BooleanExp'or' BooleanExp   
NotExp ::='not' BooleanExp   
Constant::= 'true' 'false'   
VariableExp ::= ′A'| 'B′ | ... | ′x′ |′Y' | ′z

We define two operations on Boolean expressions. The first, Evaluate, evaluates a Boolean expression in a context that assigns a true or false value to each variable. The second operation, Replace, produces a new Boolean expression by replacing a variable with an expression. Replace shows how the Interpreter pattern can be used for more than just evaluating expressions. In this case, it manipulates the expression itself.

We give details of just the BooleanExp, VariableExp, and AndExp classes here. Classes OrExp and NotExp are similar to AndExp. The Constant class represents the Boolean constants.

BooleanExp defines the interface for all classes that define a Boolean expression:

class BooleanExp {   
public:   
BooleanExp();   
virtual \~BooleanExp();   
virtual bool Evaluate(Context&) = 0;   
virtual BooleanExp\* Replace(const char\*, BooleanExp&) =0;   
virtual BooleanExp\* Copy() const = 0;   
};

The class Context defines a mapping from variables to Boolean values, which we represent with the C++ constants true and false. Context has the following interface:

class Context {   
public:   
bool Lookup(const char\*) const;   
voidAssign(VariableExp\*, bool);   
);   
A VariableExp represents a named variable:   
class VariableExp : public BooleanExp {   
public:   
VariableExp(const char\*);   
virtual \~VariableExp();   
virtual bool Evaluate(Context&);   
virtual BooleanExp\* Replace(const char\*, BooleanExp&);   
virtual BooleanExp\* Copy() const;   
private:   
char\* \_name;   
);   
The constructor takes the variable’s name as an argument:   
VariableExp::VariableExp(const char\* name) {   
\_name = strdup(name);   
}   
Evaluating a variable returns its value in the current context.   
bool VariableExp::Evaluate (Context& aContext) {   
return aContext.Lookup(\_name);   
}   
Copying a variable returns a new VariableExp:   
BooleanExp\* VariableExp::Copy()const{   
return new VariableExp(\_name);   
}

To replace a variable with an expression, we check to see if the variable has the same name as the one it is passed as an argument:

BooleanExp\* VariableExp::Replace (   
const char\* name, BooleanExp& exp   
if (strcmp(name, \_name) == 0) {   
return exp.Copy();   
} else {   
return new VariableExp(\_name);   
}

A n AndExp represents an expression made by ANDing two Boolean expressions together.

class AndExp : public BooleanExp {   
public:   
AndExp(BooleanExp\*,BooleanExp\*);   
virtual\~AndExp();   
virtual bool Evaluate(Context&);   
virtual BooleanExp\*Replace(const char\*, BooleanExp&);   
virtualBooleanExp\* Copy() const;   
private:   
BooleanExp\* \_operand1;   
BooleanExp\*\_operand2;   
};   
AndExp::AndExp (BooleanExp\* op1, BooleanExp\* op2) {   
\_operand1 = opl;   
\_operand2 = op2;   
1

Evaluating an AndExp evaluates its operands and returns the logical “and” of the results.

bool AndExp::Evaluate (Context& aContext) {   
return   
\_operand1->Evaluate(aContext) &&   
\_operand2->Evaluate(aContext);   
}

A n AndExp implements Copy and Replace by making recursive calls on its operands:

BooleanExp\* AndExp::Copy () const {   
return   
new AndExp(\_operand1->Copy(), \_operand2->Copy());   
一   
BooleanExp\* AndExp::Replace (const char\* name, BooleanExp& exp)   
return   
new AndExp(   
\_operand1->Replace(name,exp),   
\_operand2->Replace(name,exp)

Now we can define the Boolean expression

(true and x) or (y and (not x))

and evaluate it for a given assignment of true or false to the variables x and y:

BooleanExp\* expression;   
Context context;   
VariableExp\* x = new VariableExp("x");   
VariableExp\* y = new VariableExp("Y");   
expression = new OrExp(   
new AndExp(new Constant(true), x),   
new AndExp(y, new NotExp(x))   
);   
context.Assign(x, false);   
context.Assign(y, true);   
bool result = expression->Evaluate(context);

The expression evaluates to true for this assignment to x and y. We can evaluate the expression with a different assignment to the variables simply by changing the context.

Finally, we can replace the variable y with a new expression and then reevaluate it:

VariableExp\* z = new VariableExp("Z");   
NotExp not\_z(z);

BooleanExp\* replacement = expression->Replace("Y", not\_z);

context.Assign(z, true);

result = replacement->Evaluate(context);

This example illustrates an important point about the Interpreter pattern: many kinds of operations can “interpret” a sentence. Of the three operations defined for BooleanExp, Evaluate fits our idea of what an interpreter should do most closely—that is, it interprets a program or expression and returns a simple result.