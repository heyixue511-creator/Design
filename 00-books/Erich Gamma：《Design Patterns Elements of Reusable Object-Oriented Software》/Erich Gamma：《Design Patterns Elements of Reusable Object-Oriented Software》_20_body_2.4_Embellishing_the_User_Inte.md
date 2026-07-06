# 2.4 Embellishing the User Interface

> Section: body | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

## 2.4 Embellishing the User Interface

We consider two embellishments in Lexi’s user interface. The first adds a border around the text editing area to demarcate the page of text. The second adds scroll bars that let the user view different parts of the page. To make it easy to add and remove these embellishments (especially at run-time), we shouldn’t use inheritance to add them to the user interface. We achieve the most flexibility if other user interface objects don’t even know the embellishments are there. That will let us add and remove the embellishments without changing other classes.

