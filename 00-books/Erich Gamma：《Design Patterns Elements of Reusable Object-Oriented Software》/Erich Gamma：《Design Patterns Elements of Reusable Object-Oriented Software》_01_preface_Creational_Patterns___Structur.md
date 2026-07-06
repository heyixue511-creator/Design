# Creational Patterns / Structural Patterns / Behavioral Patterns / Addison-Wesley Professional Computing Series / Design Patterns / Praise for Design Patterns: Elements of Reusable Object-Oriented Software / —Stan Lippman, C++ Report / —Tom DeMarco, IEEE Software / —Sanjiv Gossain, Journal of Object-Oriented Programming / —Larry O’Brien, Software Development / —Steve Bilow, Journal of Object-Oriented Programming

> Section: preface | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

## Creational Patterns

Abstract Factory (87) Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

Builder (97) Separate the construction of a complex object from its representation so that the same construction process can create different representations.

Factory Method (107) Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

Prototype (117) Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

Singleton (127) Ensure a class only has one instance, and provide a global point of access to it.

## Structural Patterns

Adapter (139) Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.

Bridge (151) Decouple an abstraction from its implementation so that the two can vary independently.

Composite (163) Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

Decorator (175) Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

Facade (185) Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

Flyweight (195) Use sharing to support large numbers of fine-grained objects efficiently.

Proxy (207) Provide a surrogate or placeholder for another object to control access to it.

## Behavioral Patterns

Chain of Responsibility (223) Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.

Command (233) Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

Interpreter (243) Given a language, define a represention for its grammar along with an interpreter that uses the representation to interpret sentences in the language.

Iterator (257) Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

Mediator (273) Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.

Memento (283) Without violating encapsulation, capture and externalize an object’s internal state so that the object can be restored to this state later.

Observer (293) Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

State (305) Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.

Strategy (315) Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

Template Method (325) Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.

Visitor (331) Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.

# Addison-Wesley Professional Computing Series

Brian W. Kernighan, Consulting Editor

Matthew H. Austern, Generic Programming and the STL: Using and Extending the C++ Standard Template Library

David R. Butenhof, Programming with POSIX<sup>®</sup> Threads

Brent Callaghan, NFS Illustrated

Tom Cargill, C++ Programming Style

William R. Cheswick/Steven M. Bellovin/Aviel D. Rubin, Firewalls and Internet Security, Second Edition: Repelling the Wily Hacker

David A. Curry, UNIX<sup>®</sup> System Security: A Guide for Users and System Administrators

Stephen C. Dewhurst, C++ Gotchas: Avoiding Common Problems in Coding and Design

Dan Farmer/Wietse Venema, Forensic Discovery

Erich Gamma/Richard Helm/Ralph Johnson/John Vlissides, Design Patterns: Elements of Reusable Object-Oriented Software

Erich Gamma/Richard Helm/Ralph Johnson/John Vlissides, Design Patterns CD: Elements of Reusable Object-Oriented Software

Peter Haggar, Practical Java™ Programming Language Guide

David R. Hanson, C Interfaces and Implementations: Techniques for Creating Reusable Software

Mark Harrison/Michael McLennan, Ef ective Tcl/Tk Programming: Writing Better Programs with Tcl and Tk

Michi Henning/Steve Vinoski, Advanced CORBA<sup>®</sup> Programming with C++

Brian W. Kernighan/Rob Pike, The Practice of Programming

S. Keshav, An Engineering Approach to Computer Networking: ATM Networks, the Internet, and the Telephone Network

John Lakos, Large-Scale C++ Software Design

Scott Meyers, Ef ective C++ CD: 85 Specific Ways to Improve Your Programs and Designs

Scott Meyers, Ef ective C++, Third Edition: 55 Specific Ways to Improve Your

Programs and Designs

Scott Meyers, More Ef ective C++: 35 New Ways to Improve Your Programs and Designs

Scott Meyers, Ef ective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library

Robert B. Murray, C++ Strategies and Tactics

David R. Musser/Gillmer J. Derge/Atul Saini, STL Tutorial and Reference Guide, Second Edition: C++ Programming with the Standard Template Library

John K. Ousterhout, Tel and the Tk Toolkit

Craig Partridge, Gigabit Networking

Radia Perlman, Interconnections, Second Edition: Bridges, Routers, Switches, and Internetworking Protocols

Stephen A. Rago, UNIX<sup>®</sup> System V Network Programming

Eric S. Raymond, The Art of UNIX Programming

Marc J. Rochkind, Advanced UNIX Programming, Second Edition

Curt Schimmel, UNIX<sup>®</sup> Systems for Modern Architectures: Symmetric Multiprocessing and Caching for Kernel Programmers

W. Richard Stevens, TCP/IP Illustrated, Volume 1: The Protocols

W. Richard Stevens, TCP/IP Illustrated, Volume 3: TCP for Transactions, HTTP, NNTP, and the UNIX<sup>®</sup> Domain Protocols

W. Richard Stevens/Bill Fenner/Andrew M. Rudoff, UNIX Network Programming Volume 1, Third Edition: The Sockets Networking API

W. Richard Stevens/Stephen A. Rago, Advanced Programming in the UNIX<sup>®</sup> Environment, Second Edition

W. Richard Stevens/Gary R. Wright, TCP/IP Illustrated Volumes 1-3 Boxed Set

John Viega/Gary McGraw, Building Secure Software: How to Avoid Security Problems the Right Way

Gary R. Wright/W. Richard Stevens, TCP/IP Illustrated, Volume 2: The Implementation

Ruixi Yuan/W. Timothy Strayer, Virtual Private Networks: Technologies and Solutions

Visit www.awprofessional.com/series/professionalcomputing for more

information about these titles.

# Design Patterns

Elements of Reusable Object-Oriented Software

Erich Gamma

Richard Helm

Ralph Johnson

John Vlissides

六ADDISON-WESLEY

Boston • San Francisco • New York • Toronto • Montreal

London • Munich • Paris • Madrid

Capetown • Sidney • Tokyo • Singapore • Mexico City

Material from A Pattern Language: Towns/Buildings/Construction by Christopher Alexander, copyright © 1977 by Christopher Alexander is reprinted by permission of Oxford University Press, Inc.

Many of the designations used by manufacturers and sellers to distinguish their products are claimed as trademarks. Where those designations appear in this book, and we were aware of a trademark claim, the designations have been printed in initial capital letters or in all capitals.

The author and publisher have taken care in the preparation of this book, but make no expressed or implied warranty of any kind and assume no responsibility for errors or omissions. No liability is assumed for incidental or consequential damages in connection with or arising out of the use of the information or programs contained herein.

The publisher offers discounts on this book when ordered in quantity for special sales. For more information, please contact:

Pearson Education Corporate Sales Division

201 W. 103rd Street

Indianapolis, IN 46290

(800) 428-5331

corpsales@pearsoned.com

Visit AW on the Web: www.awprofessional.com

Library of Congress Cataloging-in-Publication Data

Design Patterns : elements of reusable object-oriented software / Erich Gamma ... [et al.].

p. cm.—(Addison-Wesley professional computing series)

Includes bibliographical references and index.

ISBN 0-201-63361-2

1. Object-oriented programming (Computer science) 2. Computer software—Reusability.

I. Gamma, Erich. II. Series.

QA76.64.D47 1994

005.1'2—dc20

94-34264

CIP

Copyright © 1995 by Addison-Wesley

All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form, or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior consent of the publisher. Printed in the United States of America. Published simultaneously in Canada.

Cover art © M.C. Escher/Cordon Art - Baarn - Holland. All rights reserved.

ISBN 0-201-63361-2

Text printed in the United States on recycled paper at Courier Westford in Westford, Massachusetts.

37th Printing March 2009

To Karin

—E.G.

To Sylvie

—R.H.

To Faith

—R.J.

To Dru Ann and Matthew Joshua 24:15b

—J.V.

## Praise for Design Patterns: Elements of Reusable Object-Oriented Software

“This is one of the best written and wonderfully insightful books that I have read in a great long while...this book establishes the legitimacy of patterns in the best way: not by argument but by example.”

## —Stan Lippman, C++ Report

“...this new book by Gamma, Helm, Johnson, and Vlissides promises to have an important and lasting impact on the discipline of software design. Because Design Patterns bills itself as being concerned with object-oriented software alone, I fear that software developers outside the object community may ignore it. This would be a shame. This book has something for everyone who designs software. All software designers use patterns; understanding better the reusable abstractions of our work can only make us better at it.”

## —Tom DeMarco, IEEE Software

“Overall, I think this book represents an extremely valuable and unique contribution to the field because it captures a wealth of object-oriented design experience in a compact and reusable form. This book is certainly one that I shall turn to often in search of powerful object-oriented design ideas; after all, that’s what reuse is all about, isn’t it?”

## —Sanjiv Gossain, Journal of Object-Oriented Programming

“This much-anticipated book lives up to its full year of advance buzz. The metaphor is of an architect’s pattern book filled with time-tested, usable designs. The authors have chosen 23 patterns from decades of object-oriented experience. The brilliance of the book lies in the discipline represented by that number. Give a copy of Design Patterns to every good programmer you know who wants to be better.”

## —Larry O’Brien, Software Development

“The simple fact of the matter is that patterns have the potential to permanently alter the software engineering field, catapulting it into the realm of true elegant design. Of the books to date on this subject, Design Patterns is far and away the best. It is a book to be read, studied, internalized, and loved. The book will forever change the way you view software.”

## —Steve Bilow, Journal of Object-Oriented Programming

“Design Patterns is a powerful book. After a modest investment of time with it, most C++ programmers will be able to start applying its “patterns” to produce better software. This book delivers intellectual leverage: concrete tools that help us think

and express ourselves more effectively. It may fundamentally change the way you think about programming.

—Tom Cargill, C++ Report

