• opening, saving, and printing an existing document,

• cutting selected text out of the document and pasting it back in,

• changing the font and style of selected text,

• changing the formatting of text, such as its alignment and justification,

• quitting the application,

• and on and on.

Lexi provides different user interfaces for these operations. But we don’t want to associate a particular user operation with a particular user interface, because we may want multiple user interfaces to the same operation (you can turn the page using either a page button or a menu operation, for example). We may also want to change the interface in the future.

Furthermore, these operations are implemented in many different classes. We as implementors want to access their functionality without creating a lot of dependencies between implementation and user interface classes. Otherwise we’ll end up with a tightly coupled implementation, which will be harder to understand, extend, and maintain.

To further complicate matters, we want Lexi to support undo and redo<sup>8</sup> of most but not all its functionality. Specifically, we want to be able to undo document-modifying operations like delete, with which a user can destroy lots of data inadvertently. But we shouldn’t try to undo an operation like saving a drawing or quitting the application. These operations should have no effect on the undo process. We also don’t want an arbitrary limit on the number of levels of undo and redo.

It’s clear that support for user operations permeates the application. The challenge is to come up with a simple and extensible mechanism that satisfies all of these needs.

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

![](images/677a299aa60f8f48fab85df5106082fffd3c8cfc7588be2e6aaacbfb7c051161.jpg)

Now MenuItem can store a Command object that encapsulates a request (Figure 2.12). We give each menu item object an instance of the Command subclass that’s suitable for that menu item, just as we specify the text to appear in the menu item. When a user chooses a particular menu item, the MenuItem simply calls Execute on its Command object to carry out the request. Note that buttons and other widgets can use commands in the same way menu items do.

Figure 2.12: MenuItem-Command relationship  
![](images/86573ca6ce462079947caab606caedd6ffcdb1ffb996f31f791b24f3a1bdd368.jpg)

## Undoability

Undo/redo is an important capability in interactive applications. To undo and redo commands, we add an Unexecute operation to Command’s interface. Unexecute reverses the effects of a preceding Execute operation using whatever undo information Execute stored. In the case of a FontCommand, for example, the Execute operation would store the range of text affected by the font change along with the original font(s). FontCommand’s Unexecute operation would restore the range of text to its original font(s).

Sometimes undoability must be determined at run-time. A request to change the font of a selection does nothing if the text already appears in that font. Suppose the user selects some text and then requests a spurious font change. What should be the result of a subsequent undo request? Should a meaningless change cause the undo request to do something equally meaningless? Probably not. If the user repeats the spurious font change several times, he shouldn’t have to perform exactly the same number of undo operations to get back to the last meaningful operation. If the net effect of executing a command was nothing, then there’s no need for a corresponding undo request.

So to determine if a command is undoable, we add an abstract Reversible operation to the Command interface. Reversible returns a Boolean value. Subclasses can redefine this operation to return true or false based on run-time criteria.

## Command History

The final step in supporting arbitrary-level undo and redo is to define a command history, or list of commands that have been executed (or unexecuted, if some commands have been undone). Conceptually, the command history looks like this:

![](images/8fd0c50179f549cc85ee5c5339822bd500fec3471900d966b2288977907c7940.jpg)

Each circle represents a Command object. In this case the user has issued four commands. The leftmost command was issued first, followed by the second-leftmost, and so on until the most recently issued command, which is rightmost. The line marked “present” keeps track of the most recently executed (and unexecuted) command.

To undo the last command, we simply call Unexecute on the most recent command:

![](images/662259164e8753efad1f5f0a27736c75a5aa5783106b0eb83d9f9f93fe170d71.jpg)

After unexecuting the command, we move the “present” line one command to the left. If the user chooses undo again, the next-most recently issued command will be undone in the same way, and we’re left in the state depicted here: