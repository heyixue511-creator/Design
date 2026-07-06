MITCHELLKAPOR

# A Software Design Manifesto

The most important social evolution within the computing   
professions would be to create a role for the software designer as a   
champion of the user experience....What is design?...It's where you stand with a foot in two worlds—the world of technology and the world of people and human purposes—and you try to bring the two together.

Mitchell Kapor was one of the first people in the microcomputer industry to identify his work as designing software. When he began work on Lotus l-2-3 in the early 1980s, he took on the task of designing the interactions, but he wasn't the programmer. He worked closely with a skilled programmer, Jonathan Sachs, interactively developing the design at all levels of detail—from the broad architecture to the structured organization of the command menus and the naming of the menu items.

He recounts the story of being asked by his son what he did for a living, and of being unable to come up with a good answer—he wasn't a programmer, but he was developing programs. On the other hand, he wasn't a manager, in that he was doing the detailed design work himself, rather than directing other workers. He was doing software design, but he didn't have a label for that kind of work. In his manifesto, which is reproduced here, and in a number of other talks and writings over the past few years, he has eloquently made the case that we need to think of software design as a profession, rather than as a side task of a manager or a programmer.

Kapor delivered his manifesto in 1990 at Esther Dyson's PC forum, a renowned gathering of microcomputer industry leaders. The response ranged from strong enthusiasm to the predictable “Why are you complaining—we're selling lots of software?" It first appeared in print 1 year later (Kapor, 1991) in Dr. Dobbs Journal, one of the oldest and most widely read magazines for microcomputer programmers.

This chapter is the only one in the book that is reprinted from an earlier publication. As a call to arms, it has in important place in helping us to understand the history and context of our field. The points that Kapor made are still as valid today as they were a few years ago, and the themes that he introduced echo throughout this book.

— Terry Winograd

![](images/9369eedabe25b63098b1c33a4aa7db1a91abeedb49fe52910ef9a307e2f29cc7.jpg)

HE GREAT AND RAPID SUCCESS of the personal computer industry over the past decade is not without its unexpected ironies. What   
began as a revolution of individual empowerment has ended with the   
personal computer industry not only joining the computing main-

stream, but in fact defining it. Despite the enormous outward success of personal computers, the daily experience of using computers far too often is still fraught with difficulty, pain, and barriers for most people, which means that the revolution, measured by its original goals, has not as yet succeeded.

Instead we find ourselves in a period of retrenchment and consolidation, in which corporations seek to rationalize their computing investment by standardizing on platforms, applications, and methods of connectivity, rather than striving for a fundamental simplification of the user experience. In fact, the need for extensive help in the installation, configuration, and routine maintenance of system functions continues to make the work of corporate data processing and MIS departments highly meaningful. But no one is speaking for the poor user.

There is a conspiracy of silence on this issue. It's not splashed all over the front pages of the industry trade press, but we all know it's true. Users are largely silent about this. There is no uproar, no outrage. Scratch the surface and you'll find that people are embarrassed to say they find these devices hard to use. They think the fault is their own. So users learn a bare minimum to get by. They underuse the products we work so hard to make and so don't help themselves or us as much as we would like. They're afraid to try anything else. In sum, everyone I know (including me) feels the urge to throw that infuriating machine through the window at least once a week. (And now thanks to recent advances in miniaturization, this is now possible.)

The lack of usability of software and the poor design of programs are the secret shame of the industry. Given a choice, no one would want it to be this way. What is to be done? Computing professionals themselves should take responsibility for creating a positive user experience. Perhaps the most important conceptual move to be taken is to recognize the critical role of design, as a counterpart to programming, in the creation of computer artifacts. And the most important social evolution within the computing professions would be to create a role for the software designer as a champion of the user experience.

By training and inclination, people who develop programs haven't been oriented to design issues. This is not to fault the vital work of programmers. It is simply to say that the perspective and skills that are critical to good design are typically absent from the development process, or, if present, exist only in an underground fashion. We need to take a fresh look at the entire process of creating softwarc—what I call the software design viewpoint. We need to rethink the fundamentals of how software is made.

## The Case for Design

What is design? What makes something a design problem? It's where you stand with a foot in two worlds—the world of technology and the world of people and human purposes—and you try to bring the two together. Consider an example.

Architects, not construction engineers, are the professionals who have overall responsibility for creating buildings. Architecture and engineering are, as disciplines, peers to each other, but in the actual process of designing and implementing the building, the engineers take direction from the architects. The engineers play a vital and crucial role in the process, but they take their essential direction from the design of the building as established by the architect.

When you go to design a house you talk to an architect first, not an engineer. Why is this? Because the criteria for what makes a good building fall substantially outside the domain of what engineering deals with. You want the bedrooms where it will be quiet so people can sleep, and you want the dining room to be near the kitchen. The fact that the kitchen and dining room should be proximate to each other emerges from knowing first, that the purpose of the kitchen is to prepare food and the dining room to consume it, and second, that rooms with related purposes ought to be closely related in space. This is not a fact, nor a technical item of knowledge, but a piece of design wisdom.

Similarly, in computer programs, the selection of the various components and elements of the application must be driven by an appreciation of the overall conditions of use and user needs through a process of intelligent and conscious design. How is this to be done? By software designers.

Design disciplines are concerned with making artifacts for human use. Architects work in the medium of buildings, graphic designers work in paper and other print media, industrial designers on massproduced manufactured goods, and software designers on software. The software designer should be the person with overall responsibility for the conception and realization of the program.

The Roman architecture critic Vitruvius advanced the notion that well-designed buildings were those which exhibited firmness, commodity, and delight.

The same might be said of good software. Firmness: A program should not have any bugs that inhibit its function. Commodity: A program should be suitable for the purposes for which it was intended. Delight: The experience of using the program should be a pleasurable one. Here we have the beginnings of a theory of design for software.

## Software Design Today

Today, the software designer leads a guerrilla existence, formally unrecognized and often unappreciated. There's no spot on the corporate organization chart or career ladder for such an individual. Yet time after time I’ve found people in software development companies who recognize themselves as software designers, even though their employers and colleagues don't yet accord them the professional recognition they seek.

Design is widely regarded by computer scientists as being a proper subpart of computer science itself. Also, engineers would claim design for their own. I would claim that software design needs to be recognized as a profession in its own right, a disciplinary peer to computer science and software engineering, a first-class member of the family of computing disciplines.

One of the main reasons most computer software is so abysmal is that it's not designed at all, but merely engineered. Another reason is that implementors often place more emphasis on a program's internal construction than on its external design, despite the fact that as much as 75 percent of the code in a modern program deals with the interface to the user.

## More Than Interface Design

Software design is not the same as user interface design.

The overall design of a program is to be clearly distinguished from the design of its user interface. If a user interface is designed after the fact, that is like designing an automobile's dashboard after the engine, chassis, and all other components and functions are specified. The separation of the user interface from the overall design process fundamentally disenfranchises designers at the expense of programmers and relegates them to the status of second-class citizens.

The software designer is concerned primarily with the overall conception of the product. Dan Bricklin's invention of the electronic spreadsheet is one of the crowning achievements of software design. It is the metaphor of the spreadsheet itself, its tableau of rows and columns with their precisely interrelated labels, numbers, and formulas—rather than the user interface of VisiCalc—for which he will be remembered. The look and feel of a product is but one part of its design.

## Training Designers

If software design is to be a profession in its own right, then there must be professional training that develops the consciousness and skills central to the profession.

Training in software design is distinguished from computer science, software engineering, and computer programming, in that its principal focus is on the training of professional practitioners whose work it is to create usable computer-based artifacts—that is, software programs. The emphasis on developing this specific professional competency distinguishes software design on the one hand from computer science, which seeks to train scientists in a theoretical discipline, and on the other, from engineering, which focuses almost exclusively on the construction of the internals of computer programs and which, from the design point of view, gives short shrift to consideration of use and users.

In architecture, the study of design begins with the fundamental principles and techniques of architectural representation and composition, which include freehand drawing, constructed drawing, presentation graphics, and visual composition and analysis.

In both architecture and software design it is necessary to provide the professional practitioner with a way to model the final result with far less effort than is required to build the final product. In each case specialized tools and techniques are used. In software design, unfortunately, design tools aren't sufficiently developed to be maximally useful.

Hypercard, for instance, allows the ready simulation of the appearance of a program, but is not effective at modeling the behavior of real-world programs. It captures the surface, but not the semantics. For this, object-oriented approaches will do better, especially when there are plug-in libraries, or components, readily available that perform basic back-end functions. These might not have the performance or capacity of back ends embedded in commercial products, but will be more than adequate for prototyping purposes.

## A Firm Grounding in Technology

Many people who think of themselves as working on the design of software simply lack the technical grounding to be an effective participant in the overall process. Naturally, programmers quickly lose respect for people who fail to understand fundamental technical issues. The answer to this is not to exclude designers from the process, but to make sure that they have a sound mastery of technical fundamentals, so that genuine communication with programmers is possible.

Technology courses for the student designer should deal with the principles and methods of computer program construction. Topics would include computer systems architecture, microprocessor architectures, operating systems, network communications, data structures and algorithms, databases, distributed computing, programming environments, and object-oriented development methodologies.

Designers must have a solid working knowledge of at least one modern programming language (C or Pascal) in addition to exposure to a wide variety of languages and tools, including Forth and Lisp.

## The Software Design Studio

Most important, students learn software design by practicing it. A major component of the professional training, therefore, would consist of design studios in which students carry out directed projects to design parts of actual programs, whole programs, and groups of programs using the tools and techniques of their trade.

Prospective software designers must also master the existing research in the field of human-computer interaction and social science research on the use of the computer in the workplace and in organizations.

A design is realized only in a particular medium. What are the characteristic properties of the medium in which we create software?

Digital media have unique properties that distinguish them from print-based and electronic predecessors. Software designers need to make a systematic study and comparison of different media—print, audiovisual, and digital—examining their properties and affordances with a critical eye to how these properties shape and constrain the artifacts realized in them.

## Design and the Development Process

Designers must study how to integrate software design into the overall software development process—in actual field conditions of teams of programmers, systems architects, and technical management.

In general, the programming and design activities of a project must be closely interrelated. During the course of implementing a design, new information will arise, which many times will change the original design. If design and implementation are in watertight compartments, it can be a recipe for disaster because the natural process of refinement and change is prevented.

The fact that design and implementation are closely related does not mean that they are identical—even if the two tasks are sometimes performed by one and the same person. The technical demands of writing the code are often so strenuous that the programmer can lose perspective on the larger issues affecting the design of the product.

Before you can integrate programming and design, each of the two has to have its own genuine identity.

## A Call to Action

We need to create a professional discipline of software design. We need our own community. Today you can't get a degree in software design, go to a conference on the subject, or subscribe to a journal on the topic. Designers need to be brought onto development teams as peers to programmers. The entire PC community needs to become sensitized to issues of design.

Software designers should be trained more like architects than like computer scientists. Software designers should be technically very well grounded without being measured by their ability to write production-quality code.

In the ycar since I first sounded this call to action, there has been a gratifying response from the computing industry and academic computer science departments. At Stanford University, Computer Science Professor Terry Winograd has been awarded a major National Science Foundation grant to develop and teach the first multicourse curriculum in software design. And in Silicon Valley and elsewhere there is talk of forming a professional organization dedicated to advancing the interests of software design.

## Suggested Readings

Nathaniel Borenstein. Programming as if People Mattered: Friendly Programs, Software Engineering, and Other Noble Delusions. Princeton, NJ: Princeton University Press, 1991.

Paul Heckel. Elements of Friendly Software Design. Berkeley, CA: Sybex, 1994. Bruce Tognazzini. Tog on Software Design. Reading MA: Addison-Wesley, 1995.

## About the Author

![](images/86783c33fcb94dc4b294ad77565491569309ee815ca7bf27125e758f7b8736a0.jpg)

Mitchell Kapor was the founder of Lotus Development Corporation and the designer of the Lotus 1-2-3 spreadsheet. Presently, he is an adjunct professor in the Media Laboratory at MIT, developing courses on software design, and is chair of the advisory board of the Association for Software Design. He is also a cofounder and boardmember of the Electronic Fronticr Foundation.

![](images/29237b13e3e2ca728e1e3557cd67b68b6a7579bc9887b3f495ad2f8c57ca9d06.jpg)

ARCHITECTURE

Mitchell Kapor's Software Design Manifesto (Chapter 1) draws an analogy between software design and architecture. Kapor characterizes software design in terms of the theories of the Roman architect and architectural theorist Vitruvius, who proclaimed that well-designed buildings were those exhibiting the virtues of firmness, commodity, and delight.

Since the manifesto was originally presented, the architecture-software analogy has been repeated many times in the literature on human-computer interaction and software design. We in the software profession may have much to learn from the ancient and rich tradition of architectural practice and architectural theory. At the same time, in drawing such a broad analogy, it is possible to fall into superficiality, finding attractive but misleading guidance. This profile identifies some of the issues that the architectural analogy highlights about software design, relating them to the content of the subsequent chapters.

## Roles in Design and Construction

In trying to understand the boundaries that distinguish software design, software engineering, interaction design, and the many other professional categories in our field, we can draw an analogy to the different roles in creating a building. In the simplest projects, designer, builder, and artisan are one. A single person or a small cooperative group sets out to build a structure. In contrast, developing a large software system,

Profile Authors: Terry Winograd and Philip Tabor like constructing a building, is typically a large undertaking by many people. It calls for a division of labor, ranging from the broad vision of the whole project to the many small components, crafted by individuals or smaller groups. Yet the whole is seen by the user as a unity, rather than as a collection of more or less autonomous elements.

In modern building practice, we see a general division of labor among the architect, the builder (or contractor), and the individual laborers. The architect starts from the look-and-feel end of the problem—Vitruvius' commodity and delight. The engineers and builders are more concerned with the firmness of construction: with issues of economy, safety, and constructability.

As software design continues to mature, perhaps we will see a similar evolution: from the individual artisan-programmer (far from an extinct species today); to a master architect-builder, as described by Frederick Brooks (1995); to a commercial environment that includes software architectural firms that vie for awards for originality and elegance of their designs, but that are not responsible for construction (implementation). Kapor's call for a software-design profession that is distinct from programming suggests this separation of function between design and construction, and Gillian Crampton Smith and Philip Tabor (Chapter 3) describe the role of the artist-designer whose professional grounding is in the artistic, rather than engineering, disciplines.

Is this division of labor appropriate for software, or are design and construction more intimately related? Does a software system require, as Brooks suggests, an overarching master designer who brings a coherent and consistent vision to the vast teams that build the cathedrals and fortresses of the software world? Should programmers have the kinds of legal and licensing requirements that civil engineers do, to assure the public of the firmness of the systems that affect lives (see Neumann, 1995, for a portrayal of computer risks)?

Of course, in the world of buildings, roles are not so neatly divided. The model of architect as distinct from builder is not prevalent in most of the world, and is not even that pervasive in the United States. Most everyday buildings are designed without the involvement of an architectural firm, by people whose training is in enginecring, rather than in architecture. Do-it-yourselfers and small contractors make additions and changes to houses without the benefit of any formal

Profile I: SOFTWARE DESIGN AND ARCHITECTURE

architectural or engineering training—the equivalent of end users or local developers (see Nardi, 1993) modifying the computer-application code. What properties of our software will make it remodeler friendly, while preserving its firmness?

## Design Education

The tradition of teaching in architecture differs from that of teaching in computing. It is grounded in the study of concrete examples and in direct engagement by students in a series of design projects. Budding architects are familiar with the great genres of the past: the Greek temple, the Gothic cathedral, the modern and postmodern skyscraper (Figure 1.1). They are presented with current precedent—previous designs, usually fairly recent, whose analysis and appraisal provide the raw material for theory and future practice. These designs may be classics, but they are not necessarily so: Students—and all practitioners often learn more from disasters.

![](images/a21f18abe11728def46bfe5ceb790c6ce67b509674677e4a475b954f29f0f2a0.jpg)  
FIGURE 1.1 Genres in Architecture The Gothic cathedral is an example of an architectural genre—a social tradition of building that combines form and function in a coherent way across a wide variety of individual buildings. (Source: Courtesy of Corel Corporation.)

Kapor proposes a curriculum with courses such as the History of the Word Processor, just as an architecture student might study the history of the town square. Students would examine the different periods and genres (Figure 1.2), analyzing the development of the timeless concepts and seeing how those concepts have led to implementations in different architectural media (platforms and operating systems). Perhaps it is too early to base a software-design education on classics and precedents, as Kapor suggests; the field is so young, and is changing so rapidly. Or perhaps not, since the design-cycle times are so much shorter than are those of buildings: Students can begin by studying the design languages discussed by John Rheinfrank and Shelley Evenson (Chapter 4) and the emerging genres that carry social meaning, as described by John Seely Brown and Paul Duguid (Chapter 7).

![](images/1c9cb8a0b885eedbc2b8d33154c09dbc5fd8612ef1eb7c59e9ff6b5b3cc23a40.jpg)  
FiGuRE 1.2 Genres in Software  The graphic-interface word processor represents a software genre, with established conventions and styles that cut across the individual products. Elements such as toolbars, rulers, and pulldown menus for styles are as conventional in this genre as are the characteristic arched windows and buttresses of the cathedral. (Source: Microsoft® Word for Macintosh 5.0.)

The second component of architectural education is the studio. Students tackle design projects in an environment where experienced professionals review and critique their work. The spirit of teaching is not “Let me tell you all you need to know about how to design," but rather “Let me help you to understand and improve what you've done." Donald Schön (Chapter 9) has studied this kind of teaching extensively, and describes it as reflection in action. Although studiobased teaching is not a part of traditional engineering and computerscience education, it is a component of newer proposals for human-computer interaction curricula, such as the National Science Foundation study on new directions in human-computer interaction and research (Strong, 1995) and the interdisciplinary student design projects sponsored by Apple, as described in Profile 9.

Architectural education also includes a more traditional body of instruction on the practical issues of building: structures, economics, materials, and the many details of construction. This component is analogous to the current education in software engineering, as distinct from computer science, which focuses on the technical engineering aspects and their theoretical foundations, often to the exclusion of practical concerns of management, economics, and the design process. As Donald Norman demonstrates in his tale of the Macintosh power switch (Chapter 12), all these dimensions can be relevant to the designer in surprising ways.

## Style and Function

Architecture, like fashion, is a public art form. We are constantly exposed to new styles, each of which is a response to what came before. In architecture, a shared style develops over a long time; people know what a church or a house looks like, and each new instance develops a little from its predecessors. Software design, like architecture, is a cultural phenomenon, and therefore is subject to the forces of taiste, fashion, and desire. Software is still much younger and less well devcloped, but we can see the development of styles—the IBM 3270 display mainframe style, the Microsoft style, the Nintendo style—on which a designer can build.

## Theoretical Framework

Just as Vitruvius’ virtues of firmness, commodity, and delight can be mapped onto the software world, it is interesting to examine other conceptual structures that have been applied to architecture as well. For example, a work of architecture can be seen in terms of three interlocking domains: material components, spaces, and experiences. So an architect might conceive of a building primarily as (1) an assembly of walls, floorplates and columns; (2) a cluster of spatial volumes, some squat, some lofty; or (3) a sequence of feelings induced in the user—of welcome, awe, constriction, and release. Renaissance architectural theory tended to focus on the material components of architecture. Twentieth-century Modernism, with its emphasis on abstraction, immateriality, and expression, has stressed architecture's spatial and cxperiential components (widely influential texts were Giedion (1941) and Rasmussen (1959)).

Obvious parallels can be drawn to software, which traditionally has been designed with a focus on the computing itself: algorithmic form, function, and implementation. The software-design field is now turning to understand the nature of the human-computer interactions the metaphorical spaces that people inhabit-and to the experience that software offers the user. Peter Denning and Pamela Dargan (Chapter 6) argue for a shift away from software design that is focused on the computer to software design that begins with the donain of action for the users. Crampton Smith and Tabor emphasize the ways in which interfaces communicate and shape the user's experience, rather than seeing interfaces as representations of underlying function.

Also, in considering the experience of the user as a basis for design, an issue of frequent concern to architects is that their client—the customer whom thev have to satisfy with the design—often is not the cnd user. We are all familiar with buildings that are impressive monuments to the companies that commissioned them, but are inhabitant unfriendly. As Sarah Kuhn points out (Chapter 14), the same phenomenon is frequent in software systems: They are designed to meet needs of the client who commissions them, without being suitably designed in consideration of the end-user experience.

## Beyond the Analogy

Having laid out the many areas of similarity, we could equally well point out substantial differences that distinguish software design from architecture—every comparison could be the starting point for a debate. The point, however, is not whether we can find a fit for every aspect of architecture in our understanding of software design. As with all metaphors and analogies, the value of looking at software design as architecture lies not in finding precise answers, but in raising provocative questions.

## Suggested Readings

Christopher Alexander. Notes on the Synthesis of Form. Cambridge, MA: Harvard University Press, 1964.

Sigfried Giedion. Space, Time, and Architecture: The Growth of a New Tradition. Cambridge, MA: Harvard University Press, 1941.

William J. Mitchell. City of Bits. Cambridge, MA: MIT Press, 1995.

Peter Neumann. Computer-Related Risks. Reading, MA: Addison-Wesley, 1995.

Steen Eiler Rasmussen. Experiencing Architecture (Second United States edition). Cambridge MA: MIT Press, 1959.