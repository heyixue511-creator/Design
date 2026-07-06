PETERDENNING and

PAMELADARGAN

# Action-Centered Design

The standard engineering design process produces a   
fundamental blindness to the domains of action in which the customers of software systems live and work. The connection   
between measurable aspects of the software and the satisfaction of those customers is, at best, tenuous. We propose a broader   
interpretation of design that is based on observing the repetitive actions of people in a domain and connecting those actionprocesses to supportive software technologies

Peter Denning has led a distinguished career in the computer-science profession. In addition to holding several promirient teaching and research-management posts, he has been the president of the Association for Computing Machinery (ACM), the head of the ACM Publications Board, and Editor-in-Chief of the Communications, ACM's most widely read publication. He has spearheaded national computing curriculum taskforces, including one that produced a milestone document on principles for revising the computer-science curriculum, known widely as the “Denning report" (Denning et al., 1989).

From this background, we might expect his perspective to be close to the conventional wisdom of computer science, and his advice about design to be tied closely to the methods and slogans of software engineering. But the chapter included here reflects a different direction one that brings to the center people and their practices, rather than the technologies of computing.

Working with Pamela Dargan, an experienced software designer as well, Denning set out to find out how successful software designers had managed to create software that users found usable and well suited to their needs. Denning and Dargan did not simply study the systems; they asked the systems'designers and developers what had led to achieving a good design. As Denning and Dargan report, the answers were surprisingly consistent—and were surprisingly far from the conventional wisdom on software engineering.

— Terry Winograd

![](images/3fb9993d49ae6742fcd4d84418faf29cd907eb1fd8dc1fdc79dbac71805763c9.jpg)

HE SOFTWARE LANDSCAPE is a mixed field of successes and failures. Along with notably successful software packages for every task   
from payroll to party invitations, we find notable failures, some of   
them spectacular. As one measure, a 1979 U.S. Government Ac  
counting Office review of nine software projects for the Department of   
Defense showed that about 2 percent of the allocated funds was spent   
on software that was delivered and in use; about 25 percent was spent on   
software that was never delivered; and about 50 percent was spent on

software that was delivered, but was never used (Neumann, 1995). This example may represent an extreme case, but everyone in the software industry knows that such problems are widespread and are of large magnitude. Software engineering—a discipline invented in the 1960s to address the so-called software crisishas unwittingly created an illusion that a rigorous process of transforming requirements into systems is the key to reliable design. With this illusion comes a false sense of security that the solution to the crisis is at hand—and that we will obtain it faster by throwing more research dollars at the problem.

The shortcoming is not due to a lack of effort or intelligence among software practitioners. The problem is of a different kind: The standard engineering design process produces a fundamental blindness to the domains of action in which the customers of software systems live and work. The connection between measurable aspects of the software and the satisfaction of those customers is, at best, tenuous We propose a broader interpretation of design that is based on observing the repetitive actions of people in a domain and connecting those action-processes to supportive software technologies. We call this activity action-centered design, and we propose it as the basis of a discipline of software architecture.

## Approaches to Software Design

Various English dictionaries that we have consulted list no fewer than 10 different senses of the verb design. The primary meaning is “to make or conceive a plan." Software design is concerned with the form and function of a software system and with the structure of the process that produces that system. Two principal approaches are practiced. Software engineering, which dates to the mid 1960s, is based in the engineering tradition, where design is seen as a formal process of defining specifications and deriving a system from them. Humancentered design is more recent, dating to the late 1980s. In this approach, designers immerse themselves in the everyday routines and concerns of their customers. These approaches have complementary strengths and weaknesses. We believe that the two can be brought together into a new disciplinc: software architecture. The central practice of software architecturc, action-centered design, produces maps that serve as blueprints, uniting system-oriented engineers and customer-oriented designers.

Let us begin with software engineering. Software engineers believe that most of their work lies in the process that generates a system having the form and function specified by the customer. They refer to this process as the software-lifecycle model. The most common varieties of the softwarc-lifecycle model are the waterfall model (Figure 6.1) and the spiral model (Figurc 6.2). Vivid descriptions of how this process is organized can be found in the works of Andriole and Freeman (1993), Bochm (1976), DeGrace and Hulet-Stahl (1990), and Dijkstra (1989).

Unlike other engineers, however, software engineers have not achieved success in the engineering design process. They have not devcloped a systematic method of producing software that is easy to use, rcliable, and dependable: They have not developed a discipline of software production.

Many explanations have been proposed for this anomaly. The most popular ones posit the notion that software is complex and violates the continuity laws that pervade most engineering disciplines—changing a single bit in a program can produce drastic changes in behavior. In this view, software is seen as a radical novelty, for which our customary engineering analogies are misleading (see Dijkstra, 1989; Parnas, 1985). However comforting they might be, none of these explanations has produced a practical means for systematically producing usable, dependable software.

The engineering design process operates from three assumptions:

1. The result of the design is a product (artifact, machine, or system).

2. The product is derived from specifications given by the customer. In principle, with enough knowledge and computing power, this derivation could be mcchanized.

3. Once the customer and designer have agreed on the specifications, there is little need for contact between them until delivery.

The software crisis is usually seen as a breakdown in the application of this methodology, especially due to faulty input in the form of incomplete or incorrect specifications.

![](images/d0df2142a747088504fb93a9a85346d3f950a776364aa286dd7517bd8c08daea.jpg)  
FIGURE 6.1 The Waterfall Model of Software Development The traditional waterfall model emphasizes the structured relationships between adjacent stages in an idealized process that moves from abstraction to implementation. It does not take into account the realities of iterative design, such as the prototyping cycle described by Schrage in Chapter 10. (Source: Adapted from Barry Boehm, “A spiral model of software development and enhancement," IEEE Computer 21:2 (May 1988), p. 62. Copyright © 1988 IEEE. Reprinted with permission.)

![](images/b61ba34c9681a09cde105b31ff672a2dbc4f7943927d75ce8e330ca7d008b87e.jpg)  
FiGURE 6.2 The Spiral Model The spiral model improves on the waterfall model of Figure 6.1 by emphasizing the iterative nature of the design process. It introduces a cycle of iterative prototyping, but it is still designer and product centered, rather than user and action centered. (Source: Adapted from Barry Boehm, “A spiral model of software development and enhancement," IEEE Computer 21:2 (May 1988), p. 64. Copyright © 1988 IEEE. Reprinted with permission.)

The school of human-centered design emerged in Europe in reaction to the shortcomings of product-centered design as practiced in the standard engincering design process (Floyd et al., 1992). One approach to human-centered design (see Kuhn's description in Chapter 14) focuses on workers using computer-based systems in industrial settings, emphasizing the role of human judgment and experience in work. Another approach focuses on the interaction and coordination among people and organizations, arguing that the software crisis is fundamentally a failure of customer satisfaction (Denning, 1992a).

The standard engineering design process offers little to connect the actions of designers with the concerns of users; the interaction between these two groups is limited to the requirements and specifications documents and to the final signoff. Donald Norman (1993) argues that the product-centered design process focuses primarily on the machine and its efficiency, expecting humans to adapt. In contrast, he says, the human-centered design process leaves to humans the actions that humans do well, such as empathizing, perceiving, understanding, solving problems, listening for concerns, fulfilling commitments, satisfying other people, and serving interests. It leaves to machines what humans do not do well, such as performing repetitive actions without error, searching large data sets, and carrying out accurate calculations.

Human-centered design of computer systems is based on understanding the domain of work or play in which people are engaged and in which they interact with computers, and programming computers to facilitate human action. Anthropologists play a significant role in this work. Human-centered design operates from three assumptions:

1. The result of a good design is a satisfied customer.

2. The process of design is a collaboration between designers and customers. The design evolves and adapts to their changing concerns, and the process produces a specification as an important byproduct.

3. The customer and designer are in constant communication during the entire process.

## A New Interpretation of Design

A discipline of software design must train its practitioners to be skilled observers of the domain of action in which a particular community of people engage, so that the designers can produce software that assists people in performing those actions more effectively. The phrase domain of action is meant to be broad; it includes specialized domains, such as medicine, law, banking, and sports, as well as general domains such as work, career, entertainment, education, finance, law, family, health, world, dignity, and spirituality. Software engineers must reframe design from a process of deriving a software system from specifications to a process of supporting standard practices in a domain, through software that enables more effective action.

The assessment of whether software is useful, reliable, and dependable is made by the people who act in a domain. By focusing on a system and its specifications, the traditional engineering process loses sight of those people—of their common concerns and of their actions. The process cannot offer a grounded assessment of quality, because many of the factors influencing quality are not observable in the software itself (Denning, 1992a). Human-centered design, at least, does not lose sight of the community. As presently constituted, however, human-centered design lacks formalisms and is not capable of making connections systematically between user concerns and the structure of software.

There is an increasing number of software engineers today who are using object-oriented design as a way to frame the requirements-analysis stage of the engineering design process, and are using object-oriented programming as an approach to implementation. Having observed this trend, we asked a number of prominent software engineers this question: "What is the concern that makes people find object-oriented programming so attractive?" Their answers were instructive. Most saw object-oriented programming as another fad, rather than as the silver bullet that will end the software crisis. Most thought that object-oriented programming appeals to some intuitive sense about how the software will be used, and thereby reduces the apparent complexity of the software.

We then asked the designers of the following award-winning software packages, “What does it mean for a design to be intuitive and judged as complexity-reducing?"

• Quicken (by Intuit): A personal financial-accounting system (see Profile 13)

MectingMaker (by On Technologies) and Synchronize (by Crosswind Technologies): Systems for scheduling meetings and managing calendars in groups

• Topic (by Verity): A system for retrieving documents from a database based on their text content

• Macintosh user interface (by Apple Computer) (see Profile 4)

We asked the designers of these software packages what they had done to achieve a good design. There was a surprising level of unanimity in their answers:

Pick a domain in which many people are involved and that is a constant source of breakdowns for them. (For example, the designer of Quicken chose personal finance.)

Study the nature of the actions that people take in that domain, especially of repetitive actions. What do they complain about most? What new actions would they like to perform next? (In personal finance, the repetitive actions include writing checks and balancing the checkbook; the most common complaints include errors in arithmetic and discrepancies between bank statements and personal balance sheets; and the most-sought new action is to generate reports automatically for income-tax purposes.)

Define software routines that imitate familiar patterns of action. Users will have little to learn to get started, because the software merely helps them do what they find obvious. Include functions that permit actions that most users have wished they could do, but could not do manually. (In personal finance, these functions include presenting screen images of template checks, allowing electronic payments, and providing a database that records transactions by income-tax type.)

Deploy prototypes early in selected customer domains. Observe how people react and what kinds of breakdowns they experience. Because the customers frequently shift concerns, especially after they are seasoned users, the software designer must have means of observing shifting concerns and of taking these shifts into account in the next version of the design. Thus, there are beta-test sites, individual follow-up sessions, hot lines, highly attentive technical and customer support staff, suggestion boxes, bug advisories, and the like. It is of central importance to stay in communication with customcrs (sec Chapter 13 for an account of how Intuit creates and maintains customer communication).

All the designers said that they did not pay much attention to standard software-cngineering methodology. Several said that the internal structure of their code is ugly and is not well modularized. When fixing bugs, they made patches; when the system got too patchy, they declared the next version and redesigned the software completely.

One way to summarize these findings is this: Software systems have customers. Quality means customer satisfaction. Customers are more likely to be satisfied by software that is transparent in their domain of work, because it allows them to perform familiar actions without distraction, and to perform new actions that previously they could only imagine. Customer satisfaction is not static: Customers change expectations, and software must evolve to track their shifting expectations.

We also reviewed the published papers of people who had designed software systems that were given the Best System award by the Association for Computing Machinery (ACM). We found a similar set of concerns expressed here, even though the initial users of these systems were typically technical specialists (see Denning and Dargan, 1994).

## Pattern Mapping as a Basis for a Discipline of Design

A discipline of software design should be capable of training its practitioners so that they can systematically fulfill promises to build and instali software systems that are judged useful and dependable by their customers. The key to transforming software design and engineering into a customer-centered discipline is the development of a method of mapping from human actions to software functions in a way that is intelligible to clients, designers, and engineers simultaneously.

The field of architecture is rich in useful analogies and practices. Architect Christopher Alexander (1979) says that the job of an architect is to give expression to the patterns in the use of space that permit the building's occupants to carry out their daily actions effectively. He says that surprisingly few patterns are needed to describe and generate

In any public place where people loiter, add a few steps at the edge where stairs come down or where there is a change of level. Make these raised areas immediately accessible from below, so that people may congregate and sit to watch the goings-on.

![](images/84ab758e107aa07cd4a5c70501ecbdc25999d09b726966cc4984dd913902d012.jpg)  
Give the stair seats the same orientation as SEAT SPOTS (241). Make the steps out of wood or tile or brick so that they wear with time, and show the marks of feet, and are soft to the touch for people sitting on them—SOFT TILE AND BRICK (248); and make the steps connect directly to surrounding buildings—CONNECTION TO THE EARTH (168)....  
FiGuRE 6.3 Element of a Pattern Language An architectural pattern language, as described by Alexander, consists of a vocabulary of design patterns, each of which links an observation about the human uses of a structure with a sketch and a guideline for building.(From Christopher Alexander, A Pattern Language, 1977, NY: Oxford University Press. Reprinted with permission.)

buildings—a dozen or so suffice for a typical home, and three or four dozen serve for a typical office. The immense variety of buildings arises from the infinite number of ways that these basic patterns can be combined. Alexander says that these patterns are not objects, such as bricks, beams, boards, floors, or ceilings, but instead are relationships among simpler patterns and the environment. An example of a simple architectural pattern is shown in Figure 6.3.

When everyone involved knows the pattern language of the building, Alexander says, it is easy for the builders to construct an edifice that is harmonious with the lives and work of the building's users. The patterns constitute a kind of design language for communication between builder and inhabitant (see Rheinfrank and Evenson's discussion of design languages in Chapter 4).

The architect's blueprint is a map (actually, an interrelated set of maps) that expresses the patterns and their relationships, and that provides a common language across architect, builder, and clicnt. Although Coplien and Schmidt (1995) have proposed a set of patterns for software construction, the fields of software design and engineering have no generally accepted method of mapping that is analogous to the blueprint—no agreement on the basic patterns of human action that will be composed in a software system. Although we do not yet have a formal method to construct such maps, we do know what we would want from them. The maps would provide ways

To convey the patterns of action of the domain in which the software will be used, in terms of its basic distinctions, repetitive processes, standards of assessment, strategies, tools, breakdowns, and driving concerns

To connect the linguistic structure of the domain to the software structures that will support the patterns, and to guide software engineers in implementing those structures

• To provide a basis for measuring the effectiveness of the implemented system in practice

The domain actors would find the map a useful depiction of how they work; the software producers would find it useful to configure client-server networks, databases, and applications to support the actors' work; and observers would use it to guide measurements.

These maps go beyond the standard elements of computer code or program specifications. They represent the domain of action, rather than just the system being built. These maps should cover a number of basic patterns.

A set of linguistic distinctions (verbs, nouns, jargon, etc.), around which people in the domain organize their actions (in personal finance, these distinctions include checks, ledgers, banks, bank accounts, bank statements, merchants, bills, fund transfers, deposits, credits, and interest)

• A set of speech acts by which domain participants declare and report states of affairs, initiate actions, signify completions, and coordinate with other people (in personal finance, these acts include pay, deposit, withdraw, transfer funds, reconciliation successful, prepare tax report, and cancel payment)

A sct of standard practices (recurrent actions, organizational processes, roles, standards of assessment) performed by members of the domain (in personal finance, these practices include paying monthly bills, reconciling the ledger, putting money into savings, preparing quarterly tax summaries, maintaining positive balances in accounts, earning good interest, having a minimum liquidity level, having a maximum debt level, and getting a credit rating)

A set of ready-to-hand tools and equipment that people use to perform actions; a tool is ready to hand if the person using it does so with skill and without conscious thought (in personal finance, these tools include pens, calculators, checkbooks, databases, tax forms, and monthly reports)

A set of breakdowns, which are interruptions of standard practices and progress caused by tools breaking, people failing to complete agreements, external circumstances, and so on (in personal finance, these breakdowns include errors in writing or coding checks, missing payments, discrepancies between ledger and bank statement, lost deposits, errors in credit reports, lost checks, inability to compile tax data, unresponsive customer-service departments, and broken modems)

A set of ongoing concerns of the people in the domain—common missions, interests, and fears (in personal finance, these concerns include a working banking system, good credit rating, liquidity, low debt, steady income, accurate tax data, good return on investment, and fear of tax audit)

This overall framework is sometimes called the ontology of the domain (see Winograd and Flores, 1987). Put simply, an ontology is a conceptual framework for interpreting the world in terms of recurrent actions. Building an ontology of the domain in which software will be used, representing it as a pattern language in a standard notation, and coordinating the work of builders are the central activities of a software architect. These skills are analogous to the architect's skills in creating sketches and blueprints, in using them to coordinate builders, and in using them to help clients assess the results. We call the practice of these skills action-centered design.

## Business-Process Maps

The important aspects of action-centered design are its emphases on spcech acts, on the use of language, and on repetitive actions. This perspective is a distinct departure from the traditional functional analysis of a domain, which describes the domain as a process network—a network of interconnected input-output functions that operate on physical or information objects. Speech acts such as “I request,"“I promise,"“I have completed the task," and“I am satisfied"are important because they are the motivating force for action. Without them, no task would be declared, initiated, or completed, and no one would know whether anyone else was satisfied.

Human beings engage in repetitive processes in which they coordinate action by standard speech acts. Repetitive processes that become mindless routines are ripe for automation. The skilled designer knows how to observe the repetitive processes by watching what people say to one another (verbally, in writing, electronically, via body language, or through other communications media), and then to offer tools that allow people to complete their repetitive processes faster or more reliably.

The notation of business-process maps (see Profile 6) appears to be well suited as a starting point for maps of repetitive coordination processes (Medina-Mora et al, 1993; Denning, 1992b). This notation needs to be extended to show how a process network is triggered by people acting in their coordination processes. The software system would implement the clients, servers, networks, operating systems, and applications needed to perform the tasks and to transfer data and signals among them. It would also detect people's speech acts, and would use them to trigger functions in the software system.

We propose an interpretation of design that is

• Focused primarily on satisfying the customer, rather than on satisfying the system's specifications

• Grounded in a language-action perspective (Winograd, 1987), rather than in a system-dataflow-network perspective

Based on observations of concerns, breakdowns, standard practices, institutions, and recurring actions, and on production of means to connect those observations with software structures

Action-centered design consists of observing the ontology of a domain, then constructing a workflow map, a process map, and the connections between them. The maps can be used by the software architect to review with the client how the system will satisfy each concern, and to coordinate the implementation of the system with the software engineers. The rudiments of this process can be seen in the examples of the successful software packages and systems that we studied, and in the statements of their designers.

Note that we are not advocating that anyone abandon processnetwork diagrams and other formalisms of software engineering. We are advocating that designers learn to look much more broadly, rigorously observing the domain of action and then coupling software tools with actions that people perform and assessments that people make.

We propose this interpretation not as a final answer, but as a preliminary step—an opening for a new direction in software design.

## Suggested Readings

Christopher Alexander. A Pattern Language. New York: Oxford University Press, 1977.

Christopher Alexander. The Timeless Way of Building. New York: Oxford University Press, 1979.

James Coplien and Douglas Schmidt. Pattern Languages of Program Design. Reading, MA: Addison-Wesley, 1995.

Peter DeGrace and Leslie Hulet-Stahl. Wicked Problems, Righteous Solutions: ACatalogue of Modern Software Engineering Paradigms. New York: Yourdon/Prentice-Hall, 1990.

Peter Denning and Pamela Dargan. A discipline of software architecture. interactions 1:1 (January, 1994), 55–65.

## About the Authors

![](images/11038a2efe533a45f426a562fb336e57eeff8b6cc13bb40492dbb65750c060b9.jpg)

Peter Denning is Chair of the Computer Science Department and Associate Dean for Computing in the School of Information Technology and Engineering at George Mason University. As chair of the publications board of the Association for Computing Machinery, he led the development of a far-reaching electronic publishing plan and of new copyright policies for cyberspace.

![](images/d734279faa15485f74007cad3d3d12f23af2c3e0349613b6efdfc5c40f07a0ac.jpg)

Pamela A. Dargan is a Senior Software Engineer for a nonprofit company in Washington, D.C. that provides consulting services to the government. She has been involved in all aspects of software development for nearly two decades, and currently designs open system architectures for large government software acquisitions.