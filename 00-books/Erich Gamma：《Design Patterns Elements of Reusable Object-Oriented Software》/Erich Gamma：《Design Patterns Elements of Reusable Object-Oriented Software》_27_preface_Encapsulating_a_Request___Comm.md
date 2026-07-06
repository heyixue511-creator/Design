# Encapsulating a Request / Command Class and Subclasses / Figure 2.11: Partial Command class hierarchy / Undoability / Command History / Command Pattern

> Section: preface | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

## Encapsulating a Request

From our perspective as designers, a pull-down menu is just another kind of glyph that contains other glyphs. What distinguishes pull-down menus from other glyphs that have children is that most glyphs in menus do some work in response to an up-click.

Let’s assume that these work-performing glyphs are instances of a Glyph subclass called MenuItem and that they do their work in response to a request from a client.<sup>9</sup> Carrying out the request might involve an operation on one object, or many operations on many objects, or something in between.

We could define a subclass of MenuItem for every user operation and then hard-code each subclass to carry out the request. But that’s not really right; we don’t need a subclass of MenuItem for each request any more than we need a subclass for each text string in a pull-down menu. Moreover, this approach couples the request to a particular user interface, making it hard to fulfill the request through a different user interface.

To illustrate, suppose you could advance to the last page in the document both through a MenuItem in a pull-down menu and by pressing a page icon at the bottom of Lexi’s interface (which might be more convenient for short documents). If we associate the request with a MenuItem through inheritance, then we must do the same for the page icon and any other kind of widget that might issue such a request. That can give rise to a number of classes approaching the product of the number of widget types and the number of requests.

What’s missing is a mechanism that lets us parameterize menu items by the request they should fulfill. That way we avoid a proliferation of subclasses and allow for greater flexibility at run-time. We could parameterize MenuItem with a function to call, but that’s not a complete solution for at least three reasons:

1. It doesn’t address the undo/redo problem.

2. It’s hard to associate state with a function. For example, a function that changes the font needs to know which font.

3. Functions are hard to extend, and it’s hard to reuse parts of them.

These reasons suggest that we should parameterize MenuItems with an object, not a function. Then we can use inheritance to extend and reuse the request’s implementation. We also have a place to store state and implement undo/redo functionality. Here we have another example of encapsulating the concept that varies, in this case a request. We’ll encapsulate each request in a command object.

## Command Class and Subclasses

First we define a Command abstract class to provide an interface for issuing a request. The basic interface consists of a single abstract operation called “Execute.” Subclasses of Command implement Execute in different ways to fulfill different requests. Some subclasses may delegate part or all of the work to other objects. Other subclasses may be in a position to fulfill the request entirely on their own (see Figure 2.11). To the requester, however, a Command object is a Command object—they are treated uniformly.

## Figure 2.11: Partial Command class hierarchy

![](images/2534bb93f6f193343d2ab0bf1a5a69e66c36642903d2b0e7d3bf2ff05cfca3e5.jpg)

Now MenuItem can store a Command object that encapsulates a request (Figure 2.12). We give each menu item object an instance of the Command subclass that’s suitable for that menu item, just as we specify the text to appear in the menu item. When a user chooses a particular menu item, the MenuItem simply calls Execute on its Command object to carry out the request. Note that buttons and other widgets can use commands in the same way menu items do.

Figure 2.12: MenuItem-Command relationship  
![](images/5859445ccb8e2b4b626432abca9deb08ebef152c3703eeb42246b1bf3c484d48.jpg)

## Undoability

Undo/redo is an important capability in interactive applications. To undo and redo commands, we add an Unexecute operation to Command’s interface. Unexecute reverses the effects of a preceding Execute operation using whatever undo information Execute stored. In the case of a FontCommand, for example, the Execute operation would store the range of text affected by the font change along with the original font(s). FontCommand’s Unexecute operation would restore the range of text to its original font(s).

Sometimes undoability must be determined at run-time. A request to change the font of a selection does nothing if the text already appears in that font. Suppose the user selects some text and then requests a spurious font change. What should be the result of a subsequent undo request? Should a meaningless change cause the undo request to do something equally meaningless? Probably not. If the user repeats the spurious font change several times, he shouldn’t have to perform exactly the same number of undo operations to get back to the last meaningful operation. If the net effect of executing a command was nothing, then there’s no need for a corresponding undo request.

So to determine if a command is undoable, we add an abstract Reversible operation to the Command interface. Reversible returns a Boolean value. Subclasses can redefine this operation to return true or false based on run-time criteria.

## Command History

The final step in supporting arbitrary-level undo and redo is to define a command history, or list of commands that have been executed (or unexecuted, if some commands have been undone). Conceptually, the command history looks like this:

![](images/f013d3f39398b7bd8488f6400ef7cc06d242f1ea1a5fcd3fef3bb95a30203553.jpg)

Each circle represents a Command object. In this case the user has issued four commands. The leftmost command was issued first, followed by the second-leftmost, and so on until the most recently issued command, which is rightmost. The line marked “present” keeps track of the most recently executed (and unexecuted) command.

To undo the last command, we simply call Unexecute on the most recent command:

![](images/dc618bff6106b317d451b89dcc7e764d1744170917152a7e958b8abac80d303d.jpg)

After unexecuting the command, we move the “present” line one command to the left. If the user chooses undo again, the next-most recently issued command will be undone in the same way, and we’re left in the state depicted here:

![](images/887ed72d87b567270e9cd9b5d150b10c7f275d95fda792562cc8a4b54b65c780.jpg)

You can see that by simply repeating this procedure we get multiple levels of undo. The number of levels is limited only by the length of the command history.

To redo a command that’s just been undone, we do the same thing in reverse. Commands to the right of the present line are commands that may be redone in the future. To redo the last undone command, we call Execute on the command to the right of the present line:

![](images/0cbcab4a4c4422a7e93d0a847ba03611a0ff1cc9f68e4269ac9519091e1715e2.jpg)

Then we advance the present line so that a subsequent redo will call redo on the following command in the future.

![](images/a3e2de34427ba20a52f7698875d002ce0dc304bf136aaca0c75dc29674419a8f.jpg)

Of course, if the subsequent operation is not another redo but an undo, then the command to the left of the present line will be undone. Thus the user can effectively go back and forth in time as needed to recover from errors.

## Command Pattern

Lexi’s commands are an application of the Command (233) pattern, which describes how to encapsulate a request. The Command pattern prescribes a uniform interface for issuing requests that lets you configure clients to handle different requests. The interface shields clients from the request’s implementation. A command may delegate all, part, or none of the request’s implementation to other objects. This is perfect for applications like Lexi that must provide centralized access to functionality scattered throughout the application. The pattern also discusses undo and redo mechanisms built on the basic

Command interface.

