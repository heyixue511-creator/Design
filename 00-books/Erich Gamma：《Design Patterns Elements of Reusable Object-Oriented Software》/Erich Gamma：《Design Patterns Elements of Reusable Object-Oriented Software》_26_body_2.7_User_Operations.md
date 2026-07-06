# 2.7 User Operations

> Section: body | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

## 2.7 User Operations

Some of Lexi’s functionality is available through the document’s WYSIWYG representation. You enter and delete text, move the insertion point, and select ranges of text by pointing, clicking, and typing directly in the document. Other functionality is accessed indirectly through user operations in Lexi’s pull-down menus, buttons, and keyboard accelerators. The functionality includes operations for

• creating a new document,

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

