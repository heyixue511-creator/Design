Chapter 3

# An Interdisciplinary Pattern Framework

"These rules, the semiotic language and grammar of the game, represent a kind of highly   
developed secret language, in which several sciences and arts, but mathematics and music (respectively   
musicology) in particular, participate, and which is   
capable of expressing, and relating to each other, the essence and results of nearly all sciences.'

—Hermann Hesse,

"The Glass Bead Game (Magister Ludi)"

This chapter presents the interdisciplinary pattern language framework to capture and express design experience in HCI, software engineering, and the application domain of a software project. The chapter contains a formal hypertext model of design patterns and pattern languages, details the components of each pattern, and discusses how instances of such pattern languages can be used to support design,training, andeducationinthefield of interactive hardware and software systems. For a summary of this approach, see also [Borchers, 2000b].

## 3.1 A Formal Model of Pattern Languages

To define the components of a pattern language regardless ofthe problemdomain it addresses, we first introduce a formal syntactic notation:

1. A pattern language is a directed acyclic graph $P L =$ $( \wp , \Re )$ with nodes $\wp = \left\{ P _ { 1 } , \ldots , P _ { n } \right\}$ and edges $\Re =$ $\{ R _ { 1 } , \ldots , R _ { m } \}$

2. Each node $P \in \wp$ represents a pattern.

3. For two nodes $P , Q \in \wp ,$ we say that Preferences $Q$ if and only if there is a directed edge $R \in \Re$ leading from $P$ to $Q$

4. The set of edges pointing away from a node $P \in \wp$ is called its references, and the set of edges pointing to it is called its context.

5. Each node $ { \mathcal { P } } _ { \mathbf { \Phi } } \in  { \mathcal { P } } _ { \mathbf { \Phi } }$ is itself a set $\begin{array} { r l } { P } & { { } = } \end{array}$ $\{ n , r , i , p , f _ { 1 } \ldots f _ { i } , e _ { 1 } \ldots e _ { j } , s , d , \}$ of a name $^ { n , }$ ranking $\boldsymbol { r } ,$ illustration $i ,$ problem $p$ with forces $f _ { 1 } \ldots f _ { \imath } ,$ examples $e _ { 1 } \ldots e _ { g }$ , the solution $s ,$ and diagram d.

The meaning of the components of this notation is defined next:

• Each pattern in the language describes a commonly encountered design problem, and suggests a solution that has provenuseful in this situation. The pattern language consists of a number of such patterns for a specific design domain, such as urban architecture.

• For any pattern in the language, the context edges leading into it from higher-level patterns represent the design situations in which it can be used, and its reference edges show what lower-level patterns can be applied next, after it has been used. This relationship establishes a hierarchy within thepattern language. It leads the designer from patterns addressing largescale design issues, to patterns about small details.

• The name of a pattern helps to reference it easily, communicate its central idea quickly, and build a vocabulary.

• The ranking shows how valid the pattern author believes this specific pattern is. It helps readers to separate early pattern ideas from trusted and tried,timeless patterns.

• The illustration is used to quickly "sensitize"readers tothe idea of the pattern, even ifthey are not professionals (cf. diagram below). The choice of media is discussed later in this chapter.

•The problem states what the major issue is that the pattern addresses.

The forces further elaborate the problem statement. They are aspects of the design context that need to be optimised. They usually come in pairs that contradict each other.

• The examples show existing,real-worldsituations in which the problem at hand can be (or has been) encountered, and they show how it has been solved, and the forces balanced, in those instances. They are taken from the working practice of the domain that the pattern language addresses.

• The solution generalizes from the examples a proven way to balance the forces at handoptimally for the given design context. It is not prescriptive, but generic so that it can generate a solution when it is applied to concrete problem situations of the form that the context specifies.

•The diagram summarizes the main idea of the pattern in a schematic way, concentrating on its main points and leaving out unnecessary detail. This representation is usually preferred over the illustration format by people from the profession to quickly grasp an idea. Again, the media choice is discussed further below.

This formal definition helps to clarify the structure of patterns and pattern languages, and gives a domainindependent description of the structure of a pattern language. It is also useful as a model to implement computerized tools that support authoring or browsing pattern languages.

For actual presentation, however, patterns are not represented as formulae, but rather as written texts, to make them easy to read and understand even for people from other professions. Each part of a pattern, and its connections to other patterns, are usually presented as several paragraphs in the pattern description (see, for example, Alexander et al. [1977], or the example on pp. 14ff.). Other media, such as images, animations, audio recordings, etc., are used to augment the pattern description as described above.

The actual form and contents of those pattern components are described in more detail, and with examples for each of the three disciplines involved, later in this chapter. But first we need an way to integrate the pattern framework into the software and user interface design process.

## 3.2 Pattern Languages in the Software Lifecycle

Fig. 3.1 shows the general result of the pattern-based approach: three patternlanguages that describe HCI, software design, andapplication domain concepts.

The role of the user interface designer, or human factors expert, becomes that of a relay person, talking on the one hand to the user group to arrive at a user interface design, and communicatingthe resulting requirements to the software engineering group, to help them in creating a software design.

It is remarkable that in traditional projects, those two design products are usually shifted much further to the right:

![](images/8674e33c1a4b4cc96e961b88aa754cc6e8a1f5f8a9bc812c738b8ad7573ec21f.jpg)  
Figure 3.1: Three pattern languages describing application domain, HCI, and software engineering concepts.

software engineers usually create the software design on their own, and often even do the user interface design as part of their job because there is nobody dedicated to this task, and users are hardly involved in the whole process.

The framework suggested in this work shifts those responsibilites further to the left within the diagram: others, especially HCI people, deliver input to the software design, and take over the task of desigining the user interface, with users being able to influence the latter.

Chapter 4 gives an example of this approach. It contains specific instances of the above languages, dealing with the design of interactive exhibits and similar publicaccess systems. Fig. 3.2 shows those three pattern hierarchies schematically, with a few sample patterns representing each language.

To use the pattern language framework in the process of desiging an interactive software system, it is not mandatory to follow a single fixed design method. As Dix et al. [1998, p. 6] point out:

"Probably 90% of the value of any interface design technique is that it forces the designer to remember that someone (andin particular someone else) willuse the system under construction."

![](images/084ee9e7a734ac7650bf59ea209f67d4dc2cd2f2ab914900cf1aaaace8d8dd09.jpg)  
Figure 3.2: Three pattern languages, as they were created for theWorldBeat interactive music exhibit.

However, usability must play a central role in the design process, and this implies thatthe team must consistof members fromdifferent disciplines, including programmers, user interface designers, and end users (see page 3).

The question, then, arises when the pattern concept is to be used within the development process. As with any usability method, there will not be just a single phase of the development cycle dealing with patterns. Instead, patterns will appear at most of the stages of development:

"Software engineering for interactive system design is not simply a matter of adding one more activity that slots in nicely with the existing activities in the life cycle.Rather, it involves techniques which span the entire life cycle."

[Dix et al., 1998, p. 179]

## 3.2.1 The Usability Engineering Lifecycle

To define where pattern languages can be used,we first needa software life cycle model that is gearedtowards usability for interactive system design. The standard waterfall model (see, for example, [Fairley, 1985, p. 38]), originially devised for the design of large time-sharing systems, needs to be extended by a model of the usability engineering process of modern interactive systems. Nielsen [1993, p. 72] proposes the following stages of a usability engineering lifecycle model:

## 1. Know the user

(a)Individual user characteristics

(b) The user's current and desired tasks

(c)Functional analysis

(d) The evolution of the users and the job

2.Competitive analysis

3.Setting usability goals

(a) Financial impact analysis

4. Parallel design

5. Participatory design

6.Coordinated design of the total interface

7. Apply guidelines and heuristic analysis

8. Prototyping

9. Empirical testing

10. Iterative design

(a)Capture design rationale

11. Collect feedback from field use

## 3.2.2 The Pattern Framework in the Lifecyle

The following paragraphs explain how the three pattern languages of HCI, software engineering, and application domain can be incorporated into the above model of a usability engineering lifecycle.

1. Know the user. The use of pattern languages begins in this first phase: it hasto be determined whether the application domain is suitable for expressing its concepts and methods in pattern form. This will be true whenever working in that application domain comprises some sort of creative, designing, or problem-solving activity,because the rules and guidelines that lead people in that application domain in their activitycan be formulated as design patterns with the characteristics explainedat the beginning of this chapter.

In that case, the analysis of the users' current anddesired tasks can use the pattern format to notate those tasks. This can take place in cooperation with the users or domain experts after they have been instructed about the general idea and form of a design pattern. For first-time efforts, those patterns are not required to be perfect in terms of “timeless quality". The pattern format is simply used as a convention for writing down what has to be captured anyway, but with an explicit way of stating forces, alternatives, and connections in those“work patterns".

Another advantage is that this will be the same format in which the HCIand software development patterns are expressed, making all those materials more accessible for the design team, and makingit easier for users to recognize their work patterns in the user interface objects andsequences of the product later on.

2. Competitive analysis. Duringthis phase, existing products in the market are examinedto find different solutions to the problems of the product area, and they can be used to do comparative usability evaluation before the own system is being designed. While the internal software architecture is usually not accessible for such systems, and therefore it would be too early to derive software patterns from this examination, HCIpattern languages cangeneralize successful solutions observed in competing products into a design suggestion for the new system.

3. Setting usability goals. At this point, the different usability aspects are weighed against each other and prioritized. These goals, such as learnability, effiency of use, memorability,and low error rate, become the competing forces in high-level HCI patterns that explainhow those forces work against each other, and how the design team intends to balance them for this project. For example, a system used very intensively by highly trained staff will put the balance between memorability and efficiency of use more towards the latter goal, since users who typically access the system daily are less likely to forget about the program's functions.

4. Parallel design. To explore a larger design space, several initial prototypes of the user interface can be designed by independent teams. In this case, as well as for later stages, general HCI design patterns (possibly written as books by others outside the team) can take over the role of design guidelines, and help to create a common ground, preserving the usability goals from the last phase, between the design teams working in parallel.

5. Participatory Design. Users, also called application domain experts, are usually involved in the design process to criticize prototypes, and participate in design discussions. This is the first time that the interdisciplinary value of pattern languages comes into focus: users participating in the design will find it relatively easy to understandthe pattern language of their domain, which was established in the first phase (they may even have been actively participating in constructing it). Once they are familiar with the general concept of what a pattern is and what it expresses, this knowledge will help them to understand the set of HCI patterns that the user interface design team has collected and which represents their design values, methods, and guidelines. Conversely, the user interface design team can use the application domain pattern language to talk among themselves and to users about issues of the application domain, in a language that users will find resembling their own terminology. A common vocabulary for users and user interface designers emerges from the combination of both languages.

6. Coordinated design of the total interface. Theoverall goal of coordinated design is to ensure consistency of the resulting interface,including consistency with documentation, help systems and tutorials, but also earlier versions of the product and other products within a company.A vocabulary of HCIdesign patterns, especially those that address lower-level, concrete design decisions, can help designers communicate more efficientlyabout their designs, and ensure that the same design concepts are known and respected throughout the interface. Nevertheless, other measures, suchas dictionaries ofterms usedin the user interface,are necessary to support this process ofcoordination.

7. Apply guidelines and heuristic analysis.Styleguides, guidelines, and standards are the forms of expressing HCI design experience that are closest to HCI design patterns. Patterns can improve these forms through their structured inclusion of existing examples and aninsightful explanation not only of the solution, but also of the problem context in which this solution can be used, and the structured way in which individual patterns are integrated into the hierarchical network of a pattern language, similar to the distinctionbetween general, category-specific, and productspecific guidelines [Nielsen, 1993, p. 93]:

"Category-specific guidelines ... are often a product of corporate memory, to the extent that lessons from previous projects are generalized and made available to future projects. ... Product-specific guidelines are often developed as part of individualprojects as project members gain a better understandingfof thespecial usability aspects of their system.Such understanding can be gathered early on through competitive analysis ... , and additional insights typically come from user testing of prototypes of the new system."

8. Prototyping. The traditionalwaterfall model suggests to create actual executable programs only towards the end of the development cycle. Prototypes help to put concrete interfaces into the hands of users much earlier, albeit limited in functionality, scope of features, performance and stability. This aspect of usability engineering is more orientedtowards implementation, and here software design patterns play an important role. If the development group can express their architectural standards, components, and specific project ideas in pattern form,thenthe user interface design group can relate to those concepts more easily, and will better understand the concerns of the development team. For example, the HCI design group could agree to have features in a prototype that are easier to implement without compromising the usefulness of the prototype for testing.

9. Empirical testing. Prototypes, from initial paper mockups to the final system, are tested with potential users to discover design problems. Applicationdomain patterns can be a resource to construct realistic scenarios for testing. Problems discovered can be related toHCI patterns that could be applied to solve those problems. This is discussed in the next paragraph.

10. Iterative design. Based upon user feedback, prototypes are redesigned and improved in an iterative process. Patterns of HCI or softwaredesign experience are important tools to inform the designers about design options at this point, because they are constructive—they suggest how a problem could be solved—, in contrast to general design guidelines, which are mainly descriptive, merely stating desirable general features of a “good" finished interactive system.

Of course, all pattern languages used will and should evolve even duringthe project, to capture the progress in understandingthe problem space and improvingthe design solution. Concrete, successful solutions in the current project can become examples for a given pattern, or warrant the postulation of a new pattern. Subsequent projects will then easily relate to this pattern because it contains examples from a “known"project.

This way, patterns become a very suitable format to capture the design space explored in a project, also called the structural design rationale.This post-hoc rationale is an important form of “corporate memory", as it keeps the lessons learned in a project forfollow-up projects in a readable, accessible form.

Its counterpart, the process design rationale, which documents the good and bad decisions made during design, is less suitable to be documented with patterns since they are defined to capture successful solutions. There is, however, the notion ofanti-patterns, which document particularly bad solutions that people often implement due to lack of better knowledge.Such patterns,while not patterns in the original sense ofthe definition, could document alternatives that were discarded during the design process.

11. Collect feedback from field use. After delivery of a software product, methods such as field tests, follow-up marketingstudies, or analysis of helpline calls can be used to see if reality confirms the usability engineering results. In talking to users, the application domain pattern language again plays an important role as a common vocabulary between UI experts and users, and HCI patterns can help to point designers to alternative solutions when problems arise. At the same time, feedback can be used to strengthen the argument of those patterns that created a successful solution, and to rethink those that led to suboptimal results.

This description has shown how the pattern framework can be introduced into the interactive system design process. Next,the form and contents of the various pattern components will be defined in more detail, but first, we need to deal with the notion of time in patterns.

## 3.3 Time in Patterns

A pattern language is much more than the sum of its individual patterns. The links from patterns addressing largescale design issues down to small-scale design details help the reader and prospective designer to find the next important pattern as she refines her design. In architecture, the resultinghierarchy is quite simply ordered by geometrical size. Patterns dealing with the general layout ofan entire neighbourhood are higher up in the hierarchy than patterns dealing with the question of how to split up an individual house into rooms.

This simple organizing principle ignores one major dimension: time. This works reasonably well for architecture, as the artefacts created (buildings, streets, etc.) do not change themselves substantially over time. Only the events taking place within those environments change over time, and Alexander uses such sequences of events (such as traffic intensity over the course of a day) as a single aspect that influences the design of an environment at the geometric level the pattern addresses.

This approach does not work for HCI, software engineering, and many other application domains, because the artefacts they create do change substantially over time, following the tasks they support. To give a simple example for

HCI: a railway information kiosk changes from a start page, to a page giving train type options and travel time input fields, to another page displaying possible train connections, etc. In other words, we design user interfaces along a time dimension as well as along two(or three) spatial dimensions.

Therefore, the ordering principle of spatial size has to be expanded into an ordering principle of spatial and temporal expansion. One obvious solution is to put time at the top of the hierarchy, according to the large-scale notion of tasks: In HCI, the designer first thinks about what the complete task looks like, what objects and procedures it contains, and how it can be supported by a series of interactions, or dialogues. Then she goes into detail for each of those steps, designing those shorter dialogues, until each step in the dialogue sequence (or rather graph) is designed with its interaction objects, layout, and spatial geometry.

Other ordering principles are possible, for example those that are more oriented toward the design process itself; these issues were discussed in some detail atthe INTER-ACT'99 workshop [Borchers et al., 2001].

However, the structure and components of individual patterns also needs to take the temporal dimension into account. This is discussed in the next section.

## 3.4 Patterns and Their Components in Detail

To ensure that the patterns defined and used within a project actually improve interdisciplinary cooperation, it is important that the characteristics of all patterns follow certain common rules that increase their readability and usefulness for all participants. These characteristics are best explained by looking at the pattern components more closely. For each component, requirements specific to HCI, software engineering, and applicationdomain are also listed.

The Context and References parts are discussed last, since they lead to the question of organizing principles for pattern languages.

For all parts of a pattern, thewritingstyle should avoid genre-specific jargon and notation wherepossible. If they are necessary, for example, to describe details of a solution, then a generally readable alternative representation should also be included, even if it is less precise.

For the same reason—readability—patterns shouldfollow the standard rules of good text design, for example using whole sentences instead of keyword lists.

## 3.4.1 Name

Choosing the right name for a pattern is not a trivial task. The name is often the only thing that is remembered literally about a pattern, and it is the pattern part that is referred to most frequently in discussion. In the approach presented here, it becomes a word in the vocabulary for communication between all people involved in the design process, not only from the same but also from other professions.

Therefore, the name should express the central idea of the pattern—the core of its solution—as clearly as possible. At the same time, it must remain short enough to be easily remembered. Two words are a common length, four words the maximum.

Alexander [1979, p. 267] gives an example of how his group improved a pattern name over several iterations. The pattern suggests to design the space between street and the front door of a house so that a person experiences a change in the environment and atmosphere while entering the house from the street. From an initial name ENTRY PROCESS (muchtoo vague), via HOUSE STREET RELATIONSHIP (not defining therelationship), and FRONT DOOR INDIRECTLY REACHED FROM STREET (still not definingthe place to create), they arrived at a final name that actuallycaptures the idea that a concrete space, the “transition", needs to be created: ENTRANCE TRANSITION.

To be understandable across disciplines, it is generally better not to choose a name that uses terminology of the domain that is meaningless to outsiders. This is especially true for software engineering patterns, but also HCI patterns. Patterns from the application domain, on the other hand, may use terminology from the application domain to give names to patterns, because one of the goals of that pattern language (see above) is to introduce the designers to this terminology.

For an understandable name, it may help to refer to an analogy from common experience to describe the idea for a pattern. If this analogy is too far-fetched, however, it may become meaningless, or different people may re-map it to the actual problem in different ways, its meaning becoming blurred. As an example, van Welie [2000] called an HCI pattern WHAT'S FOR DINNER?, to refer to the idea of always providing a list of available functions in the current interaction context, but its name may not describe the HCI design solution in an entirely clear way.

## 3.4.2 Ranking

A pattern author will never be equally confident about the validity of all patterns in his collection. It is important to convey this personal rating to the reader, as it can help the latter to decide whether to use a pattern with confidence, or whether it may be worth looking for alternative solutions.

Software engineering, HCI, andapplication domain patterns should adopta simple ranking scheme suchas the one using zero, one or two stars used in [Alexander et al., 1977] and explained in more detail on page 18.

## 3.4.3 Illustration

The illustration is the first thing—apart from the name— that a reader encounters when studying a pattern. It has the important function of sensitizing the reader to the problem and solution of the pattern. With the pattern name in mind, the reader should recognize thesituationdepicted in the illustration directly, helping him to understand and appreciate the values of the solution that the pattern describes. It is an especially accessible representation of the pattern idea, even for non-professionals.

The choice of media depends on the domain: in architecture, Alexander used realistic photos of buildingsand places.

In HCI, it may be necessary to include the notion of time into the illustration, because, as outlined above, user interfaces often change substantially over the course of an interaction, and this time-dependent behaviour needs to be expressed as part of those solutions dealing with it.Therefore, an illustration for HCI could simplybe a photo of a user interacting with a system, or a screen shot of a graphical user interface. But where appropriate, it could also be a short movie showing the behaviour of a user interface over time, or a different medium for other types of user interfaces (such as an audio recording of someone using a voicecontrolled menu).

In software engineering, it is difficult to show a "realworld" example of the solution, because the interior design of a software system is not an environment that people from outside the profession will be familiar with. If the language is mainly used as suggested in this framework—to support communicatingtechnical aspects of the software architecture to the user interface designer who has some understanding of the technical issues—, then it may be helpful to show sample diagrams of objects interacting in an existing system, if possible from the application domain of the project at hand. They will be a concrete instantiation of the abstract concept explained in the pattern (and sketched in its diagram section which is discussed below).

Application domain patterns will usually be much easier to depict in an illustration. There are always people living inside this domain—the users—, and their work orother activity practice, and their successfulsolutions to recurring problems, can be captured, for example, by scenario photographs takenon site, or by other representations of the artefacts created. In music, for example, a short audio recording can introduce the concept that a musical design pattern addresses.

## 3.4.4Problem and Forces

It turns out that this part is often the most difficult one to write in a pattern. Expressing exactly what problem a potential pattern solves frequently shows that the problem was not really defined in a sufficiently concrete way. Since patterns should always capture design solutions that balance the various interests in a useful way, it should always be possible to express those conflicting interests as opposing“forces".

The concept of forces is very close to the spatial design solutions of architecture, where one argument, for example, speaks in favour of a higher wall, whereas the other argument supports a lower wall design (see the SITTING WALL pattern on page 16). However, Alexander makes it clear that those forces do not have to be of a purely physical nature. He includes psychological, social,and economical forces in his considerations [Alexander, 1979, pp. 108-110].

This idea of forces can be transferred directly to HCI. Spatial forces are at work in geometrical layout considerations, but other forces come from cognitive psychology (such as Gestalt theory [Köhler, 1930, 1992]),and from social and economical issues.

The software engineering field can express many of its design conflicts as opposing forces as well, as has been shown in the software patterns literature. Those forces will usually be of a technical nature. An example is the tradeoff between memory requirements and execution speed of a software system, but also the tradeoff between initial simplicity and flexibility of a software architecture later on.

The existing efforts that have been presented in section 2.4 to carry the pattern idea over to the application domain often fail at expressing their problems using opposing forces. This usually indicates that the solutions presented are not really design-oriented patterns balancing conflicting design goals, but rather activity patterns that just describeexisting work practice without validating it. This is one of the reasons why the present framework requires that the application domain has to incorporate some kind of creative, problem-solving, or designing work activity.Otherwise it may not be possible to put its concepts into pattern form, and other techniques may be more applicable to model the application domain.

## 3.4.5Examples

The examples are vital to a pattern for two reasons. First, they serve to lead the novice reader towards the general solution of the pattern via a set of concrete, existing instantiations of this solution. Second, they give the professional reader empirical, verifiable evidence of the validity of the pattern.

To make a pattern as understandable as possible, it is better to use an inductive than a deductive style. This means that the concrete examples are presented first, and then generalized into the solution. They should refer to existing systems that are as widely known as possible, and explain how those systems solve the problem described before. Additional illustrations should be used where available.

In HCI, because of its closeness to architecture, it is relatively easy to describe examples that the reader can relate to. For example, to explain the idea of dynamic information appearing close to an object upon request, features of common desktop operating systems, such as Mac OS®Balloon Help,or Microsoft Windows® Tool Tips, can be shown. Since people from outside HCI design have usually interacted with such systems as well, they are usually able to understand those examples and see the common solution in them that leads them to the core of the pattern.

For software engineering, it may be easy to come up with existingsystems that use a certain designsolution, but it will be more difficult to make those examples understandable to people from outside the profession, since architectural details are usually not directly“visible"in an interactive software system, but rather indirectly influence external characteristics such as performance, stability, or flexibility. Nevertheless, as with the opening illustration, it should usually be possible to show examples that are understandable to HCI people with some computing expertise.

In the application domain, the examples are drawn from work practice or artefacts created, and help to underline the importance of the application domain patterns they exemplify to the remaining design team.

## 3.4.6 Solution

This is the central message of each pattern. It takes the lessons to be learned from the examples, and generalizes them into a constructive design recommendation that can be applied in varying situations whenever a problem is encountered as described in the context.

In HCI, those solutions deal with the user interface design of interactive systems. They describe psychological, spatial andtemporal rules and configurationsthatcreate a more intuitive user experience, making the interaction as natural and simple as possible and appropriate for the application domain.

In software engineering, the solutionsgive design recommendationsfor the internals ofthe software system, from global,architectural issues down toimplementation details. They aim at improving the resulting system performance with respect to the tasks it is to support.

In the application domain, the solutiondescribes the way problems are solved in the work practice or other activity that the software system is going to support. They can serve as starting point for the way the software solves those problems, with the possibility of improvingupon those practices through the introduction of the system.

In any case, the solution should be put into a succinct form (usuallynot more than a fewshort sentences). It is something that is often read after glancing at a pattern, to find out what the core message of the pattern is.

## 3.4.7 Diagram

The diagram summarizes the main idea of the pattern in a schematic way, concentrating on its main points and leaving out unnecessary detail. It is more concise and schematic than the illustration.

The medium used depends on the pattern language domain: For architecture, the medium chosen byAlexander is a graphical sketch. In HCI, the graphical sketch can capture spatial designs, and a storyboard sketch can dealwith temporal design aspects.

In software engineering, UML diagrams or even pseudocode may express the pattern idea very precisely, and similar forms are used, for example, in [Gamma et al., 1995]. However, when choosing a notation, it has to be kept in mind that this notation also needs to be sufficiently readable and accessible for readers from outside the profession

In the application domain, the choice depends on the nature of that domain. Most domains have some form of shorthand notation to express their concepts. In music, for example, this shorthand is the musical score notation.

## 3.4.8Context and References

The context, together with the references, represents the added value that turns a loose collection of patterns into a pattern language. Once a reader has decided to apply a pattern, its references should point her toother, "smaller" patterns that can be appliednext to refine the design further. The context is the “inverse function" of the references, and sets the stage for the reader to make it clear when the current pattern can be applied.

The above notion of pattern “size"” as organizing principle works very well in architecture, where patterns can be sorted into a hierarchy according to the size of the space they apply to. A pattern describing how to layout an entire neighbourhood is “larger"than a pattern dealing with the placement of windows in a single room. Alexander used this organizing principle because it reflects the order in which he suggests to carry out the design: initial designs create a broad layout, which is then refined by subsequently applying smaller design patterns.

HCI actually uses a similar design sequence with time as an added dimension, especially when following theideas of user-centreddesign and iterative prototyping as outlined in the usability engineering lifecycle: after taskanalysis, which in the pattern framework creates the application domain pattern language, the user interface is designed in an iterative process. The first designs are crude prototypes, paper sketches, or storyboards that dealwith theoverall structure of the interaction. Only insubsequent iterations, those designs are refined, user interface objects identified, until final prototypes deal with small-scale issues ofgraphical layout etc. (Of course, thisdoes not imply that those small-scale patterns are less important, because the overall "QualityWithout a Name" of the system depends on the successful combination of patterns at all levels.)

In software engineering, the design process is again similar if atop-down process is employed. Inthis case, considerations about the total system architecture lead to questions about groups of interacting components, down to implementation details of individualsoftwareclassesor modules. Of course, this does not mean that no implementation takes place until the end of the design cycle (that would imply going back to the waterfall model). Instead, it indicates that the technicalqualityof the implementation does not need to be optimized for the first softwareprototypes, and that patterns to improve that quality can be applied later in the software development process.

This concludes the pattern-based framework for interaction design. The next chapter shows sample pattern languages from this approach. In particular, the HCI pattern language should be useful to many readers in its own right.

This Page Intentionally Left Blank