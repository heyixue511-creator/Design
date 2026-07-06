## Contents

Preface   
Foreword   
Guide to Readers   
1 Introduction   
1.1 What Is a Design Pattern?   
1.2 Design Patterns in Smalltalk MVC   
1.3 Describing Design Patterns   
1.4 The Catalog of Design Patterns   
1.5 Organizing the Catalog   
1.6 How Design Patterns Solve Design Problems   
1.7 How to Select a Design Pattern   
1.8 How to Use a Design Pattern   
2 A Case Study: Designing a Document Editor   
2.1 Design Problems   
2.2 Document Structure   
2.3 Formatting   
2.4 Embellishing the User Interface   
2.5 Supporting Multiple Look-and-Feel Standards   
2.6 Supporting Multiple Window Systems   
2.7 User Operations   
2.8 Spelling Checking and Hyphenation   
2.9 Summary   
Design Pattern Catalog   
3 Creational Patterns   
Abstract Factory   
Builder   
Factory Method   
Prototype   
Singleton   
Discussion of Creational Patterns   
4 Structural Patterns   
Adapter   
Bridge   
Composite   
Decorator   
Facade   
Flyweight   
Proxy   
Discussion of Structural Patterns   
5 Behavioral Patterns   
Chain of Responsibility   
Command   
Interpreter   
Iterator   
Mediator   
Memento   
Observer   
State   
Strategy   
Template Method   
Visitor   
Discussion of Behavioral Patterns   
6 Conclusion   
6.1 What to Expect from Design Patterns   
6.2 A Brief History   
6.3 The Pattern Community   
6.4 An Invitation   
6.5 A Parting Thought   
A Glossary   
B Guide to Notation   
B.1 Class Diagram   
B.2 Object Diagram   
B.3 Interaction Diagram   
C Foundation Classes   
C.1 List   
C.2 Iterator   
C.3 ListIterator   
C.4 Point   
C.5 Rect   
Bibliography   
Index

## Preface

This book isn’t an introduction to object-oriented technology or design. Many books already do a good job of that. This book assumes you are reasonably proficient in at least one object-oriented programming language, and you should have some experience in object-oriented design as well. You definitely shouldn’t have to rush to the nearest dictionary the moment we mention “types” and “polymorphism,” or “interface” as opposed to “implementation” inheritance. On the other hand, this isn’t an advanced technical treatise either. It’s a book of design patterns that describes simple and elegant solutions to specific problems in object-oriented software design. Design patterns capture solutions that have developed and evolved over time. Hence they aren’t the designs people tend to generate initially. They reflect untold redesign and recoding as developers have struggled for greater reuse and flexibility in their software. Design patterns capture these solutions in a succinct and easily applied form. The design patterns require neither unusual language features nor amazing programming tricks with which to astound your friends and managers. All can be implemented in standard object-oriented languages, though they might take a little more work than ad hoc solutions. But the extra effort invariably pays dividends in increased flexibility and reusability. Once you understand the design patterns and have had an “Aha!” (and not just a “Huh?”) experience with them, you won’t ever think about object-oriented design in the same way. You’ll have insights that can make your own designs more flexible, modular, reusable, and understandable—which is why you’re interested in object-oriented technology in the first place, right? A word of warning and encouragement: Don’t worry if you don’t understand this book completely on the first reading. We didn’t understand it all on the first writing! Remember that this isn’t a book to read once and put on a shelf. We hope you’ll find yourself referring to it again and again for design insights and for inspiration. This book has had a long gestation. It has seen four countries, three of its authors’ marriages, and the birth of two (unrelated) offspring. Many people have had a part in its development. Special thanks are due Bruce Anderson, Kent Beck, and André Weinand for their inspiration and advice. We also thank those who reviewed drafts of the manuscript: Roger Bielefeld, Grady Booch, Tom Cargill, Marshall Cline, Ralph Hyre, Brian Kernighan, Thomas Laliberty, Mark Lorenz, Arthur Riel, Doug Schmidt, Clovis Tondo, Steve Vinoski, and Rebecca Wirfs-Brock. We are also grateful to the team at Addison-Wesley for their help and patience: Kate Habib, Tiffany Moore, Lisa Raffaele, Pradeepa Siva, and John Wait. Special thanks to Carl Kessler, Danny Sabbah, and Mark Wegman at IBM Research for their unflagging support of this work.

Last but certainly not least, we thank everyone on the Internet and points beyond who commented on versions of the patterns, offered encouraging words, and told us that what we were doing was worthwhile. These people include but are not limited to Jon Avotins, Steve Berczuk, Julian Berdych, Matthias Bohlen, John Brant, Allan Clarke, Paul Chisholm, Jens Coldewey, Dave Collins, Jim Coplien, Don Dwiggins, Gabriele Elia, Doug Felt, Brian Foote, Denis Fortin, Ward Harold, Hermann Hueni, Nayeem Islam, Bikramjit Kalra, Paul Keefer, Thomas Kofler, Doug Lea, Dan LaLiberte, James Long, Ann Louise Luu, Pundi Madhavan, Brian Marick, Robert Martin, Dave McComb, Carl McConnell, Christine Mingins, Hanspeter Mössenböck, Eric Newton, Marianne Ozkan, Roxsan Payette, Larry Podmolik, George Radin, Sita Ramakrishnan, Russ Ramirez, Alexander Ran, Dirk Riehle, Bryan Rosenburg, Aamod Sane, Duri Schmidt, Robert Seidl, Xin Shu, and Bill Walker.

We don’t consider this collection of design patterns complete and static; it’s more a recording of our current thoughts on design. We welcome comments on it, whether criticisms of our examples, references and known uses we’ve missed, or design patterns we should have included. You can write us care of Addison-Wesley, or send electronic mail to design-patterns@cs.uiuc.edu. You can also obtain softcopy for the code in the Sample Code sections by sending the message “send design pattern source” to designpatterns-source@cs.uiuc.edu. And now there’s a Web page at http://stwww.cs.uiuc.edu/users/patterns/DPBook/DPBook.html for late-breaking information and updates.

Mountain View, California E.G.

Montreal, Quebec R.H.

Urbana, Illinois R.J.

Hawthorne, New York J.V.

August 1994