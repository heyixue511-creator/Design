# Chapter 2

# Design Pattern Languages

“Every place is given its character by certain patterns of events that keep on happening there. These patterns of events are always interlocked with certain geometric patterns in the space.

—Christopher Alexander, "The Timeless Way of Building

## 2.1 Pattern Languages in Architecture

During the renaissance age, architecture, like many other sciences and arts, experienced one of its prime ages. A major key for this revolution was the fact that “master builders" of that time were beginning to systematically collect, document, and structure architectural design knowledge [de Haas, 1999]. A particularly prominent example was master builder Francesco di Giorgio (1439–1501),who led such an effort in Siena.The central ingredient of his documents (see Fig. 2.1) was the sketch of a successful design solution, supported bytextual explanations, which essentiallyled to a new literary form, the first “design pattern".

![](images/dcd3c0006ead7fbdb9cac66c990ba932cca051b47690acb27bbdb1d717604677.jpg)  
Figure 2.1:A page from Tratato I (Francesco diGiorgio, 1480), with constructions for various application domains as well as building and usage iņformation [de Haas, 1999].

In line with this general idea, and out of dissatisfaction with modern urban architecture, a newtheory of architecture, building and planning was proposed by architect Christopher Alexander in the 1970s, centred around the idea of pattern languages.

The discussion of Alexander's concept of patterns in architecture below may seem very detailed.Many central concepts and properties of patterns, however, are introduced in this section, and will be used in the subsequent definitions of pattern languages in HCI and other domains.

## The pattern idea in architecture

In the first volume of his central work,TheTimeless Way of Building [Alexander, 1979], architect Christopher Alexander argues that buildings and towns that people enjoy livingin have a certain, timeless QualityWithout a Namethat cannot be reduced to a single dimension. Instead, the design of these environments has succeeded in supporting the patterns of events that frequently happen there, by implementing a number ofaccording geometric patterns, or relationships between their spatial constituents:

“A building or town is given its character, essentially, by those events that keeponhappening there most often."

[Alexander, 1979, pp. 65–66]

Good spatial patterns within buildings and towns are mostly created not by architects, butrather by the inhabitants themselves. Those environment"users", therefore, have a number of design patterns in their heads — often without being able to name them explicitly—which they use to create such suitable environments for themselves.

These patterns generally solve a problem of conflicting "forces", or interests. For example, people inside a room are naturally drawn towards the light, and to the window, but they also like to sit down after a while.If a room has only seating in its middle, these forces cannot be resolved. The solution is to build a WINDOW PLACE, some kind of seating, into the window area that allows people to sit very close or inside the window [Alexander et al.,1977, p. 833]. Of course, these forces can also be of a social, economic, natural,or physical nature.

These patterns have become lost in contemporary society: inhabitants have stopped devising their own environments, andthis task has been passed on to dedicated architects and builders. However, these professionals are no longer personally or otherwise closely connected to the future inhabitants of their designs and artefacts. The resulting designs cannot support the users' patterns of habits, tasks, and events in an idealway.

Patterns are for To recreate this shared knowledge of appropriate and good   
users design solutions for buildings, towns, and construction, Alexander describes how these patterns can be made explicit, noted down, tested, and graduallyimproved. The goal is to re-enable inhabitants to participate in the design of their environments. This is strikingly similar to the idea of participatory design, which aims to actively involve end users in allstages of the software development cycle.   
Patterns form a Patterns are not isolated: they refer to other, smaller-scale   
language patterns for the solution they describe, and they can only be used in a certain type of context, which is the result of applying larger-scale patterns. This links patterns together to form a hierarchical pattern language for the design of a certain building, and further to a language for the design of a whole town.

When this pattern language is shared and used by a whole community, suitable patterns can be applied at all levels of design, from town planning to the rebuildingof a single room in a building. Alexander considers design and building not a process in which preformed parts are combined, but rather an unfolding process in which space is differentiated to create a complex solution.

By applying a sequence of such patterns, entire buildings and towns are gradually created. They are iteratively magnified, fixed, and improved by a process of piecemeal growth, againapplying patterns to change existingbuildings and neighbourhoods, whichslowly generates the aforementioned timeless quality in an environment. In fact, Alexander sees his formulated patterns only as a means to remind people of important issuesin environmental design; once understood,the patterns have fulfilled their purpose and are, in the long run, no longer needed as a formal framework:

"Indeed this ageless character has nothing, in the end, to do with languages. The language, and the processes which stemfrom it, merely release the fundamental order which is native to us. They do not teach us, they only remind us of what we know already[.. .]."

[Alexander, 1979,p. 531]

Until this end goal has been reached, however, pattern languages, then, aim to provide laymen with a vocabulary that helps them to express their ideas and designs, and discuss them with others. This work essentially carries this idea over from architecture to user interface design, and to the application domain, leading to an interdisciplinarydesign process where the interface is not designed just by HCI professionals, but by application domain experts and software designers as well—who can be considered “laymen" in terms of user interface design.

## Architectural pattern examples

The second volume of Alexander's series, A Pattern Language: Towns, Buildings, Construction [Alexander et al., 1977]is an example of his approach. It presents 253 design patterns of "user-friendly" solutions to recurring problems in urban architecture. They range from large-scale iSSueS (COMMUNITYOF7000,IDENTIFIABLENEIGHBOUR-HOOD), via smaller-scale patterns (PROMENADE, STREET CAFE) down to patterns for the design of single buildings (CASCADE OF ROOFS, INTIMACY GRADIENT, SITTING WALL). In [Alexander et al., 1988],the architect uses his pattern language to define a new planning process for the University of Oregon as an example.

The best way to understand what a pattern in the Alexandrian meaning is supposed to be, is to look at some examples from his original collection. The following pages show two sample patterns from [Alexander et al., 1977], STREET CAFE and SITTINGWALL.Take a moment to read through these two patterns, and note how they convey their ideas by combining a very structured representation with good readability.

## 88 STREET CAFE\*\*

![](images/e0c1fd0745d26ba6e4b71ef9b14aa73385f55dac760aeb5b3ee1d97d57568ee0.jpg)

. . . neighborhoods aredefinedby IDENTIFIABLE NEIGHBOR-Hood (14); their natural points of focus are given by ActiviTy NODES (3O) and sMALL PUBLIC sQUARES (6I). This pattern, and the ones which follow it, give the neighborhood and its points of focus, their identity.

## ÷÷÷

The street cafe provides a unique setting, special to cities: a place where people can sit lazily, legitimately, be on view, and watch the world go by.

The most humane cities are always full of street cafes. Let us try to understand the experience which makes these places so attractive.

We know that people enjoy mixing in public, in parks, squares, along promenades and avenues, in street cafes. The preconditions seem to be: the setting gives you the right to be there, by custom; there are a few things to do that are part of the scene, almost ritual: reading the newspaper, strolling, nursing a beer, playing catch; and people feel safe enough to relax, nod at each other, perhaps even meet. A good cafe terrace meets these conditions. But it has in addition, special qualities ofits own: a person may sit there for hours—in public! Strolling, a person must keep up a pace; loitering is only for a few minutes. You can sit still in a park, but there is not the volume of people passing, it is more a private, peaceful experience. And sitting at home on one's porch is again different: it is far more protected; and there is not the mix of people passing by. But on the cafe terrace, you can sit still, relax, and be very public. As an experience it has special possibilities;"perhaps the next person. . ."; it is a risky place.

It is this experience that the street cafe supports. And it is one of the attractions of cities, for only in cities do we have the concentration of people required to bring it off. But this experience need not be confined to the special, extraordinary parts of town. In European cities and towns, there is a street cafe in every neighborhood—they are as ordinary as gas stations are in the United

## TOWNS

States, And the existence of such places provides social glue for the community. They become like clubs—people tend to return to their favorite, the faces become familiar. When there is a successful cafe within walking distance of your home, in the neighborhood, so much the better. It helps enormously to increase the identity of a neighborhood. It is one of the few settings where a newcomer to the neighborhood can start learning the ropes and meeting the people who have been there many years. The ingredients of a successful street cafe seem to be: 1. There is an established local clientele. That is, by name, location, and staff, the cafe is very much anchored in the neighborhood in which it is situated. 2. In addition to the terrace which is open to the street, the cafe contains several other spaces: with games, fire, soft chairs, newspapers. . . . This allows a variety of people to start using it, according to slightly different social styles. 3. The cafe serves simple food and drinks—some alcoholic drinks, but it is not a bar. It is a place where you are as likely to go in the morning, to start the day, as in the evening, for a nightcap. When these conditions are present, and the cafe takes hold, it offers something unique to the lives of the people who use it: it offers a setting for discussions of great spirit—talks, two-bit lectures, half-public, half-private, learning, exchange of thought. When we worked for the University of Oregon, we compared the importanceof such discussion in cafes and cafe-like places, with the instruction students receive in the classroom. We interviewed 30 students to measure the extent that shops and cafes contributed to their intellectual and emotional growth at the University. We found that "talking with a small group of students in a coffee shop" and "discussion over a glass of beer" scored as high and higher than"examinations" and"laboratory study." Apparently the informal activities of shops and cafes contribute as much to the growth of students, as the more formal educational activities. We believe this phenomenon is general. The quality that we tried to capture in these interviews, and which is present in a neighborhood cafe, is essential to all neighborhoods—not only student neighborhoods. It is part of their life-blood.

## 88 STREET CAFE

Therefore:

Encourage localcafes to spring up in each neighborhood. Make them intimate places, with several rooms, open to a busy path, where people can sit with coffee or a drink and watch the world go by. Build the front of the cafe so that a set of tables stretch out of the cafe, right into the street.

![](images/86a2c7e2434a8593f77f163d2b03b7581bdbf3cc1d192a81469d31294adf16e5.jpg)  
Build a wide, substantial opening between the terrace and the indoors—OPENING TO THE sTREET (165); make the terrace double as A PLACE To wAIT (15o) for nearby bus stops and offices; both indoors and on the terrace use a great variety of different kinds of chairs and tables—DIFFERENT CHAIRs (251); and give the terrace some low definition at the street edge if it is in danger of being interrupted by street action—sTair sEATs (125), SITrING WALL (243), perhaps a CANVAS ROOF (244). For the shape of the building, the terrace, and the surroundings, begin with BUILDING COMPLEX (95). . . .

## 243 SITTING WALL\*\*

![](images/492e4bcb69174178ce7f1b97d991b6dcac8e8d935df233822d16987fbb6df10b.jpg)

. . . if all is well, the outdoor areas are largely made up of positive spaces—PosITIvE oUTDooR sPACEs (106); in some fashion you have marked boundaries between gardens and streets, between terraces and gardens, between outdoor rooms and terraces, between play areas and gardens-GREEN sTREETs (51), PEDESTRIAN STREET (IOO), HALF-HIDDEN GARDEN (III), HIERARCHY OF OPEN SPACE (114), PATH SHAPE (12I), ACTIVITY POCKETS (124), PRIVATE TERRACE ON THE STREET (14O), OUTDOOR ROOM (163), OPENING TO THE STREET (165), GALLERY SUR-ROUND (166), GARDEN GROWING WILD (172). With this pattern, you can help these natural boundaries take on their proper character, by building walls, just low enough to sit on, and high enough to mark the boundaries.

If you have also marked the places where it makes sense to build seats—SEAT SPOTs (241), FRONT DOOR BENCH (242)—yOu can kill two birds with one stone by using the walls as seats which help enclose the outdoor space wherever its positive character is weakest.

## ÷

In many places walls and fences between outdoor spaces are too high; but no boundary at all does injustice to the subtlety of the divisions between the spaces.

Consider, for example, a garden on a quiet street. At least somewhere along the edge between the two there is a need for a seam, a place which unites the two, but does so without breaking down the fact that they are separate places. If there is a high wall or a hedge, then the people in the garden have no way of being connected to the street; the people in the street have no way of being connected to the garden. But if there is no barrier at all-then the division between the two is hard to maintain. Stray dogs can wander in and out at will; it is even uncomfortable to sit in the garden, because it is essentially like sitting in the street.

## CONSTRUCTION

The problem can only be solved by a kind of barrier which junctions as a barrier which separates, and as a seam which joins, at the same time.

A low wall or balustrade, just at the right height for sitting, is perfect. It creates a barrier which separates. But because it invites people to sit on it—invites them to sit first with their legs on one side, then with their legs on top, then to swivel round still further to the other side, or to sit astride it—it also functions as a seam, which makes a positive connection between the two places.

Examples: A low wall with the children's sandbox on one side, circulation path on the other; low wall at the front of the garden, connecting the house to the public path; a sitting wall that is a retaining wall, with plants on one side, where people can sit close to the flowers and eat their lunch.

## Ruskin describes a sitting wall he experienced:

Last summer I was lodging for a little while in a cottage in the country, and in front of my low window there were, first, some beds of daisies, then a row of gooseberry and currant bushes, and then a low wall about three feet above the ground, covered with stonecress. Outside, a corn-field, with its green ears glistening in the sun, and a field path through it, just past the garden gate. From my window I could see every peasant of the village who passed that way, with basket on arm for market, or spade on shoulder for field. When I was inclined for society, I could lean over my wall, and talk fo anybody; when I was inclined for science, I could botanize all along the top of my wall—there were four species of stone-cress alone growing on it; and when I was inclined for exercise, I could jump over my wall, backwards and forwards. That's the sort of fence to have in a Christian country; not a thing which you can't walk inside of without making yourself look like a wild beast, nor look at out of your window in the morning without expecting to see somebody impaled upon it in the night. (John Ruskin, The Two Paths, New York: Everyman's Library, 1907, p. 203.)

## Therefore:

Surround any natural outdoor area, and make minor boundaries between outdoor areas with low walls, about 16 inches high, and wide enough to sit on, at least 12 inches wide.

243 SITTING WALL

![](images/406a8d99db473849e109b53adb4e9fa80f3a0fd194ba25ec057f653915cbb8ef.jpg)  
÷÷÷

Place the walls to coincide with natural seat spots, so that extra benches are not necessary—sEAT spoTs (241); make them of brick or tile, if possible—soFT TILE AND BRICK (248) ; if they separate two areas of slightly different height, pierce them with holes to make them balustrades—oRNAMENT (249). Where they are in the sun, and can be large enough, plant flowers in them or against them—RAIsED FLoWERs (245). . . .

## 3 larger parts

## The structure of patterns

A central property of patternsthat becomes visible when studying the above examples is their uniform structure and format. Each of Alexander's patterns consists of the same components, presented in the same sequence and form [Alexander et al., 1977, p. x]:

• the name of the pattern,

• a ranking of its validity,

• a picture as an example of its application,

• the context in which it is to be used,

• a short problem statement,

• a more detailed problem description with empirical background,

• the central solution of the pattern,

• a diagram illustrating the solution,

• and finally references to smaller patterns.

Name, ranking, picture, and context create the introductory part of each pattern. Problem statement, problem description, solution and diagram form its central part, and the references are its closing part. These major parts of each pattern are divided in the text as well, bylines of three asterisks.

The name of a pattern, such as SITTING WALL, is an essential component: it has to convey the idea of the pattern in one or a few words, to make it easy to remember and refer to when thinking about or discussing design solutions.

The name is followed by a ranking of zero, one, or two asterisks, which indicate the degree of confidence that the authors hadin the pattern. No asterisk means that there are certainly ways of solving the problem different from the was described in the pattern: the solution given is more of an example, and the true invariant of the pattern still has to be found.

One asterisk means that the authorsbelieve that some progress has been made towards finding an invariant pattern,but the user is nevertheless encouraged to carefully look for alternative solutions to the problemat hand.

Patterns with two asterisks, finally, are believed to describe a true invariant: the authors are very confident that it is not possible to solve the statedproblem withoutshaping the environment in a way that somehow follows the given solution. The patterns shown above are allfrom thislast group.

Directly after the heading, a picture gives an example of the pattern applied. It is usually a photograph of an environment that represents a good exampleof the idea of the pattern. Our examples include photographs of a typical STREET CAFE, and a typical SITTINGWALL.

The context explains which larger-scale patterns this specific pattern helps to implement. This links the pattern to other patterns of a higher level. For example, the STREET CAFE is used to further elaborate the larger-scale pattern of an IDENTIFIABLENEIGHBOURHOOD.

Three asterisks now mark the beginning of the central part of each pattern.

Next, a short problem statement summarizes the general situation that the pattern addresses. The problem statement of the SITTING WALL pattern, for example, shows that this pattern addresses the conflict between the necessity to divide open spaces, and the disconnecting nature of high walls.

A more extensive problem description follows that gives empirical background information on the pattern. It often states the problem using the concept of competing "forces" described earlier. In the SITTING WALL example, these forces are to build higher walls, and to build lower or no walls. The goal of the pattern is to resolve, or balance, these forces optimally in the given context:

"As an element in the world, each pattern is a relationship between a certain context, a certain system of forces which occurs repeatedly in that context, and a certain spatial configuration which allows these forces to resolve themselves.

As an element of language, a pattern is an instruction, which shows how this spatial configuration can be used, over and over again, to resolve the given system of forces, wherever the context makes it relevant."

[Alexander, 1979, p. 247]

The problem description also discusses existing solutions.

The next and central component of each pattern is a statement that distils, from those examples, a general solution to the problem at hand. It is a clear, but generic, set of instructions that can be applied in varying situations.

The solution is visualized, and made easier to grasp and remember, with a simple diagram of its central idea. It sketches the solution and its major constituents graphically. Since every pattern is supposed to describe a spatial configuration to solve a certain problem, sketching a pattern must always be possible:

“If you can't draw a diagram of it, it isn't a pattern."

[Alexander, 1979, p. 267]

Three more asterisks mark the end of the central part of the pattern, and are followed by its lastcomponent,the references, which point the reader to smaller patterns. These are other patterns that the author recommends in order to implement and further"unfold"the solution ofthe current pattern. The STREET CAFE pattern, for example, suggests to use a SITTING WALL to separate the terrace from the street.

## Implicit Structuring Through Typography

Alexander's patterns do not contain explicit text tags for each part of each pattern: there is no label saying “Context:", or "Solution:". Though this mayseem at first asif this structuringis missing, looking at the patternsmore closely reveals that this structural information is communicated implicitly, using very rigid rules of typography. The most important rules are:

• Each pattern contains the same parts, in the same order: it starts with a name, followed by ranking, opening picture, context, etc., up to the lastpart of each pattern, its references.

•Each pattern part is always typeset or rendered in the same way: the name in small capitals, the problem and solution in bold face as separate paragraphs, the diagram as a hand-drawn sketch, etc.

•Special words or signs are used to further distinguish each pattern part: the context begins with aninitial ellipsis (...), which also ends the references, the solution is introduced with the word"Therefore:"on a separate line, and three asterisks open and close the pattern"body" between context and references.

This implicit structuring makes it unnecessary to clutter the text with distracting, repetitive, and typographically unaesthetic labels. At the same time, it is still possible to determine immediately, for example, that a paragraph in bold face following the word "Therefore" must be the solution part of a pattern.

Closer examination shows that, in Alexander's pattern language, not every reference to a smaller-scale pattern is reflected in a corresponding backward link in the context section of that pattern. The graph of links that point downwards in the hierarchy is different from thegraph of those that point upwards. However,it mustbe stressed that

Alexandrian patterns are, above all, a didactic medium for human readers, even (and especially) for non-architects. To Alexander, this quality has priority over a mathematically "correct" representation. It also must not be lost in a more formal representation.

Interestingly, Alexander's ideas were not always received well by his colleagues. One reason for this is that Alexander's concepts empowered the inhabitants, supplying them with more ways to influence the building process, and taking much of that power out of the hands of the professional. Obviously, this idea was not very popular among architects.

## 2.2 Pattern Languages in Software Engineering

In 1987, software engineering picked up the idea of using pattern languages from architecture to express design experience. At the OOPSLA conference on object-orientation, Beck and Cunningham [1987]reported on an experiment where application domain experts without prior Smalltalk experience quite successfully designed their own Smalltalk user interfaces. These users had been introduced tobasic Smalltalk UI concepts using a pattern language of just five basic patterns. One of these patterns, COLLECT LOW-LEVEL PROTOCOL, is given below in abbreviated form:

"Once you have initially decomposed a system into objects [Objects from the User's World] and refined the objects [Engines and Holders] you need to begin collecting useful functionality that doesn't particularly fit into any single object. Oftenmany objectsneed to communicate with low-level (bit- or byte-oriented) parts of the system.For example, external files can have complex or highlyencoded formats that requiresubstantialbyte or even bitmanipulation tointerpret. Collectallnecessary protocolfor decoding file formats or any other particular low-level task into an object specifically designed for the purpose. Do so evenif you might otherwise spread it around several other objects. Once you have done this you are ready to begin testing and refining your objects [Elegance through Debugging]."

[Beck and Cunningham, 1987]

Due to its more technical terms, this pattern is not quite as easy to understand as a typical pattern from Alexander's collection. Nevertheless, itis interesting to note that this first software pattern experiment actually dealt with user interface design, and user participation. It was therefore still relatively close to the original goals of the pattern approach.

The OOPSLA workshop starteda vivid exchange about software design patterns. An influential collection of patterns for object-oriented software design was published by the“Gang of Four" [Gamma et al., 1995]. Although it is generally regarded as the archetype of a software patterns book, it does not entirelyfulfil the demands of a pattern language as intended by Alexander: the collection, and the linking between the individualpatterns, is not complete enough to be a language. Furthermore, many patterns do not represent the knowledge andconcepts of good objectoriented design as gained by expertise, but rather workarounds to implement object-oriented concepts despite the shortcomings of today's programming languages, such as C++. But above all, they are not written with the idea of empowering users to participate in the design process in mind. Typical patterns from the collection dedicate over fifty percent of their text to implementation details and sample code listings. A professional programmer can learn a lot from these patterns to improve his program design and implementation skills, but they are not intended for a more general audience.

However, many other researchers have developed ideas about how to adopt the pattern principle for software engineering, and the annual Pattern Languages of Programming (PLoP) conferences [Coplien and Schmidt, 1995, Vlissides et al., 1996, Martin et al.,1998, Harrison et al.,1999] have succeeded in establishing an entirely new and useful forum to exchange proven, generalized solutions to recurring software design problems among professionals.

The field of human-computer interaction, however, is hardly touched upon in this series, with only a few notable exceptions:

Riehle and Züllighoven [1995] describe a pattern language for their "tools and materials" design metaphor. Their abstract patterns, or design metaphors, describe a quite humancentred, task-orientedconceptof HCI design,although theirconcrete design patterns arefirmly rooted in the more technical approach of Gamma et al. [1995].

Rossi etal. [1996] present two design patterns to model navigation in hypermedia systems. NAVIGATION STRAT-EGY decouples link activation from computing the link target. NAVIGATION OBSERVER simplifies navigation history management by separatingthe objects recordingnavigationfrom the actual contents. The work has been continued in [Rossi et al., 1997]. The problems that those patterns address, however, are again very much in the software engineering domain.

The third volumeofthis series is the first one to explicitly contain a part on user interface patterns. However, the introduction to this part voices an interesting concern that HCI issues might have been overlooked by the community before:

"This part contains only one chapter,which is remarkable and puzzling. In a field that has brought us patterns such asObserver, Model-View-Controller, Taskmaster, and so forth, we would have expected this type of pattern to flourish. Aren't there any more user interface patterns to be found? Have we really exhausted this field?Perhaps this is an indication that this field needs more work, and many patterns are still waiting to be discovered."[Martin et al., 1998, p. 345]

The language presented in that volume [Bradac and Fletcher, 1998] helps with constructing forms-based user interfaces. As with the other HCI-oriented PLoP pattern languages, it instructs a developer how to implement a certain type of interface in an elegant and efficient way. It does not give instructions to a user interface designer (or even somebody from another domain) regarding which types or combinations of user interface components should be used for which tasks. Similar work has been carried out by Nanard et al. [1998], who use design patterns and"constructive templates" to capture structures and components for reuse in hypermedia design and development.

In all, the overall format of a pattern has not changed very much from Alexander et al. [1977] to, for example, Gamma et al. [1995]. Name, context, problem, solution, examples, diagrams, and cross-references arestill the essential constituents of each pattern. The goals have, however, changed in an important way, without many noticing:

Software design patterns are considered a useful language for communication among software designers, and a practical vehicle for introducing less experienced designers into the field. The idea of end users designing their own (software) architectures has not been takenover. On the one hand, this makes sense, because people do not live as intensely "in" their software applications as they live in their environments. On the otherhand, though, a good chance to push the concepts of participatorydesign and work ethics forward by introducing patterns has not been taken advantage of. Alexander summarizes this in his keynote speech at OOPSLA'96:

"Now, my understandingof what you are doing with patterns.. . It is a kind of a neat format, and that is fine. The pattern language that we began did have other features, andI don't know whether those have translated into your discipline. I mean, there was at root behind the wholething a continuous mode ofpreoccupation with under what circumstances is the environment good. In our field that means something."

[Alexander, 1996]

## 2.3 Pattern Languages in HCI

This section summarizes most previous research that has been carried out in the field of pattern languages for human-computer interaction. It serves as an overview of the state of the art in this area.

## Early pattern references in HCI

In the academic and professional field of HCI, the idea of design patterns has received much less attention than in software engineering. Nevertheless, Alexander's pattern approach has been referenced by HCI research earlier than one would expect—earlier, actually, thanits first widely known appearance in software engineering at the OOPSLA 1987 conference [Beck and Cunningham, 1987].

Probably the earliest HCI-oriented reference to Alexander's pattern idea can be found in Norman and Draper's seminal book on user-centred system design [Norman and Draper, 1986].Shortly afterwards, in his text on the design of everyday products [Norman,1988], which is also a standard work among user interface researchers and practitioners, Norman explains that he was influenced particularly by Alexander's work:

"All of Alexander's works describe [a] process of evolution, and his books on architectural design are influential. [...] I findthe works fascinating to skim, frustrating to read, and difficult to put into practice, but his descriptions of the structure of homes and villages are very good."

[Norman, 1988, p. 229]

Another classic HCI text, Apple Computer's Macintosh Human Interface Guidelines, quotes Alexander's work asseminal in the field of environmental design in itslist of recommended reading for user interface designers [Apple Computer, 1992, p. 338].

In a more educational context, Barfield et al. [1994] describe how they used the pattern approach in their interaction design curriculum at the Utrecht School of Arts.The authors argue that computer users work as active agents inside evolving information ecologies, andthat many of the systems they use work not in isolation, but as parts of larger networks. This establishes important links from HCI design to architecture and urban design. In both architecture and HCI, the central issues in the relation between user and environment, whether physical or virtual, are:

• how users experience an environment,

how an environment influences individual behaviour,

• how single environments integrate into the larger context, and

• how these smaller and larger environments develop and change over time.

Barfield et al. state that, as for architecture (see p.11), the important thing in a user interface is not its form, but what happens inside it. Patterns refer to relationships between physical elements and the events that happen there. Interface designers, like urban architects, strive to create environments that establish certain behavioural patterns with a positive effectonto thosepeople “inside" these environments. The"Quality Without a Name" that Alexander demands ofgood, "timeless"architecture is comparable to user interface qualities such as “transparent" and “natural".

In their curriculum, Barfield et al. establish patterns, like Alexander, as three-part rules with context, forces, and configuration. Most userinterface"guidelines" function like patterns, and the pattern form can be used to phrase guidelines in a consistent format that leaves room for subtleties; for example, "When users have to wait for a certain periodof time (context), this can befrustrating because we don't know what's going on (forces), so be sure to provide feedback on the system's progress (abstract configuration)." [Barfield et al., 1994, p.72].

They also point out, however, that interaction design is quite different from architecture in one important way: time is an essential component. Interaction is much more dynamic, and contextand system of forces often change during the course of interaction.

Nevertheless, a trioof interaction design courses in their curriculum is based successfully on the pattern concept. Students do exercises such as findinginteraction designs withandwithout the "qualitywithout a name", defining patterns based on their observations, and transforming interface guidelines into patterns.

In all, these references, especially the work by Barfield et al. [1994], show that the importance of the "quality without a name", and the influence of design decisions on the users' experience of their environment, is even more evident in interaction design than in software engineering, which justifies the following statement:

The notion of design patterns, as it was intended in architecture, carries over more naturally to user interface design than it does to software design.

## Recent research efforts

Since1997, the subject of pattern languages in HCI has begun to be addressed more intensively. From a workshop at CHI'97, the largestannual HCI conference, Bayle et al. [1998] report that the ideas about adopting the pattern concept for HCI are still very varied.Even the notion of a “pattern" is being used in two senses: as design pattern in the sense of the present text, butalso as activity pattern that simply describes an existing situation as it is, without claiming that it has any special quality or value to be reused and preserved. The latter definition makes sense especially when describing organizational patterns that capture structures and workflows in an organization. Accordingly, it identifies many different ways of using patterns in HCI [Bayle et al., 1998]:

Capture and Description: describe key characteristics of a situation or event in a context-sensitive way;

Generalization:generalize across varying situations, yet retain a certain concreteness;

Prescription: give prescriptive guidelines for common problems in HCI (or organizational) design;

Rhetoric: create the vocabulary for a lingua franca, a common language, between designers and users; or

Prediction: judge potential consequences of design changes to an existing system or environment, by following ramifications through the pattern network.

The patterns described by the workshop follow the idea of activity patterns and address solutions observed at the conference location. They include, for example:

ADMINISTRATIVE NEXUS IN THE EDDY. This pattern describes the problem of locatingthe conference office. Forces include the necessity to be near the loci of most frequent or severe problems, but also to be not so prominent as to attract casual, non-crucial requests. The solution observed is to place it near the conference area, but far enough away that it is not noticed by people unless they are looking for it. An example of this was the CHI'97 conference office.

CLARIFICATION GRAFFITI. This pattern describes the problem that signs are often meaningless to users because of the different perspective and context of sign designer and user. Forces include the necessity to create aesthetically pleasing signs in advance, but also to experience the actual context when the sign is in use in order to make it meaningful to readers. The solution is that users often add their own notes to existingsignsin order to make them more understandable for fellow users. An example at the conference was a printed sign "Message Board on Ballroom Level",which someone had clarified with a handwritten note"(go up one floor)."

The second example especially shows the workshop's tendency toward activity patterns: the pattern describes a solution that is not one to strive for in future designs; rather, it tells the designer what real-worldbehaviour to expect and take into account when creating similar signs. The pattern could be applied in two ways: either by trying to make sure that signs are meaningful in their final context, thereby eliminating the use of clarification graffiti; or by accepting that it will always be impossible to phrase signs optimally until they are put into use, and consciously permitting for on-site clarification graffiti, for example by leaving space on signs for additional directions, etc.

One of the workshop organizers has subsequently refined these ideas [Erickson, 1998]. Erickson aims to use patterns as a way to describe workplaces, and provide a “what-if” mechanism to reflect about design options. Thisshould make it easier for stakeholders (the various groups engaged in interdisciplinary design, including potential users) to identify important recurringdesign problems and solutions. Patterns can enable stakeholders to talk about and participate in design, and allow for the creation of shared, social artefacts that these stakeholders can use.Ultimately, interaction pattern languages can be alingua franca, legitimizing and empowering “users", and also increasing accessibility of research results.

Thus, Erickson's notion ofInteraction Design Patterns primarily refers to human-human, not human-computer interaction. In [Erickson, 1998], he is quite clear about the fact that his major interest in patterns is not to capture known design solutions in a general way,to support training and discussion within a design organization, or to achieve the "Quality Without a Name". Nevertheless, he recognizes the idea that other research efforts are lookingat the pattern idea for those reasons andconsequentially applying them touser interface design and implementation. As a consequence,he has established the first Interaction Patterns Home Page [H:Erickson98], a very useful collection of publications and pattern collections in human-human and human-computer interaction.

A number of concrete pattern collections for interaction design have been suggested. Currently, the language by Tidwell [1998] is the most comprehensive effort in this field. It addresses the general problem of designing an interactive software artefact, deliberately leaving aside implementation issues for specific user interface technologies, although these are mentioned in the examples section of each pattern.

The language goes beyond pattern efforts in the software community such as the collection by Gamma et al. [1995], and is closer to the Alexandrian ideas of a pattern language, in that it represents timeless principles of good interaction design in a hierarchically structured,interlinked set of patterns that are intended to guide the designer at various levels of abstraction throughout the design process.

According to Tidwell, the success of pattern approaches in architecture and software design calls for an application of the idea to user interface design. Tidwell argues that patterns are a good form to express design guidelines. Typical GUI (Graphical User Interface) style guides are useful to ensure a common look and feel across multiple applications built with a certain user interface toolkit, but they are too much tied tothis toolkit, which makes them transient: as soon as the underlying toolkit changes (for example, from Windows 3.1 to Windows 95), their rules become hard to apply, and seem out of date. Moreover, such style guides limit interface design alternatives to those that are supported by the present toolkit, and they do not help the designer to balance multiple high-level design principles in a particular situation. User tests, on the other hand, are useful and necessary throughout the design cycle, but patterns can support the creative process of devising a design in the first place, or of improving a solution after problems were found.

Tidwell sees several benefits that patterns may bring to the individual user interface designer, and to the user interface design community as a whole:

• Patterns can capture the collective wisdom of experienced designers in HCI and related design fields.

• They can supply a common language to the community.

•They allow the designer to think "outside" the toolkit at hand.

• Whereas today, many excellent user interface prototypes never gain wide acceptance, patterns could help to extract the timeless characteristics of these widgets and solutions, and pass them on to the community.

• They may serve as a starting point when implementing new interface toolkits.

• Some patterns may even be encoded in software.

The language in [Tidwell, 1998] consists of more than fifty patterns, plus several more that have not been writtenin detail yet. The patterns are grouped into different problem subdomains with a varying level of detail, and they mostly address either a question of how to present content, or an issue of how to make actions available.

Alternatives for the basic shape of the content are described by patterns such as the linear and mostlyverbalNARRA-TIVE form, the HIGH-DENSITY INFORMATION DISPLAYof maps, tables, and charts, and the STATUSDISPLAYfound in many electrical appliances.

The next set of patterns deals with the basic shape of actions, and includes patterns suchasthe fill-in FORM,the CONTROL PANEL,for example of a TV remote control, the WYSIWYGEDITOR as found in word processors, the COM-POSED COMMAND used in command-line interfaces such as the UNIX shell, and the online SOCIAL SPACEof newsgroups and chat rooms.

These patterns define the overall appearance and behaviour of the artefact. Subsequently, possible ways to unfoldcontent and actions before theuserare discussed in patterns such as highly interactive, self-paced NAVIGA-BLE SPACES, the tree-like HIERARCHICAL SET display, or the technique that the POINTER SHOWSAFFORDANCE.

A separate set of patterns describes how the system relates to the user's attention (sOVEREIGN POSTURE,HELPER POSTURE, BACKGROUND POSTURE),while others deal with questions of the layout of working areas (CENTRAL,TILED, STACK, or PILE OF WORKING SURFACES) or navigation (GO BACK ONE STEP, GO BACK TO A SAFE PLACE).

The patterns reach down to low-level details such as specific forms of data entry (SLIDING SCALE) and display (PROGRESS INDICATOR), and also deal with questions of customizing and other forms of user support (USER's AN-NOTATIONS, GOOD DEFAULTS).

The following is an example from Tidwell's pattern language.

## GO BACK TO A SAFE PLACE

## Examples:

• The "Home" button on a Web browser

• Turning back to the beginning of a chapter in a physical book or magazine

•The "Revert" feature on some computer applications

Context: The artefact allows a user to move through spaces (as in NAVIGABLE SPACES), or steps (as in STEP-BY-STEP INSTRUCTIONS), or a linear NARRATIVE, or discrete states; the artefact also has one or more checkpoints in that set of spaces.

Problem: How can the artefact make navigation easy, convenient, and psychologically safe for the user?

## Forces:

• A user that explores a complex artefact, or tries many state-changing operations, may literally get lost.

• A user may forget where they were, if they stop using the artefact while they're in the middle of something and don't get back to it for a while.

• If the user gets into a space or a state that they don't want to be in, they willwant to get out of it in a safe and predictable way.

• The user is more likely to explore an artefact if they are assured that they can easily get out of an undesired state or space; that assurance engenders a feeling of security.

• Backtracking outof a long navigation path can be very tedious.

Solution: Provide a way to go back to a checkpoint of the user's choice. That checkpoint may be a home page, a saved file or state, the logical beginningof a section of narrative ora set of steps. Ideally, it could be whatever state or space a user chooses to declare as a checkpoint.

![](images/c731831ad46098117b5988d03c5bbbf4411708c1cde5e2d82446b9e4eefe2cfd.jpg)

![](images/b49effff87cc0f79766718ae389d4cd2bf51205f0d651e02b964c0d2aaf302ad.jpg)  
Resulting Context: GO BACK ONE STEP is a natural adjunct to this pattern, and is often found along with it. For non-Narrative use, INTERACTION HISTORY is useful too, almost to the point of making GO BACK TO A SAFE PLACE unnecessary: it may actually help a"lost" user figure out where they are,for instance, or remind an interrupted user of where they are and what they've done.

Tidwell's pattern collection is currently the most promising effort to create an HCI pattern language. While it has a few weaknesses (severalof its patterns have not been detailed yet, the pattern format is not always keptconsistent, and the collection has not been updated in recent months),it has already served as a frequently quoted example of what an HCI pattern language could look like.

The first workshop in which the pattern communities from software engineering and HCI got into direct contact took place at ChiliPLoP'99, one of the three annual conferences in the PLoP conference series.

As a first result, the workshop turned out an initial definition of what interactionpatterns are. This definition was arrived at after much discussion, but it also foundbroad approval by the other pattern people at the conference:

"An Interaction Pattern Language generates space/time interaction designs that create a system imageclose to the user's mentalmodel of the task at hand,to make the human-computer interface as transparent as possible."

[Borchers, 2000a]

The definition was intentionally not expressed to describe what a single interaction pattern is, as the linking between patterns is generally considered at least as important as the individual patterns themselves (see, for example, [Borchers, 2000a] for James Coplien's views on this).

Another important detailofthe definition is that it talks about space/time interaction designs. This is to stress the temporaldimension of HCI design,aspreviously described (see p. 28): Alexander's patterns almost exclusively deal with spatial configurations. Human-Computer Interaction, on theother hand,has totake into account that the user interface of aninteractive computersystem is a dynamic environment that will usually change its appearance and behaviour substantially over the course of an interaction.

The term "transparency" is an approximation of Alexander's "Quality Without a Name"for human-computer interfaces (see p. 28). The definition also aims at putting the user's task into the focus of attention, following the principles of user-centred design.

The second important result of the workshop is an initial taxonomy of interaction design patterns. It distinguishes three main dimensions along which interaction patterns can be classified meaningfully (see Fig.2.4).

The most important dimension is level ofabstraction: Interaction design patterns can address very large-scale issues that comprise a user's complete task, they can address smaller-scale, slightly more concrete topics that describe the style of a certain part of the interaction (such as a

BROwSER style), or they can deal with low-level questions of user interface design that lookat individual user interface objects (whether virtual or physical).

The inclusion of a fourth layer, "technology", to distinguish the actual input andoutput hardware considerations, was rejected as the distinction from software objects did not seem useful enough.

The second fundamental dimension is function: patterns can be classified into those that address mainly questions of (visual, auditory, etc.) perception (interface output), and those that deal with interfaceinput, or, more specifically, manipulation of some kind of application data, or navigation through the system.

The distinction between navigation andmanipulation may seem too software-centred, but this reflects the engineeringoriented nature of the workshop.

The third dimension is physical dimension: some patterns will address questions of spatiallayout, while others deal with issues of sequence (discrete series of events, e.g. a sequence of dialogues), or with continuous time (such as a design pattern about using animation techniques in the user interface).

The taxonomy was evaluated by trying to classify patterns from the workshop according to it.

For example, the pattern INCREMENTAL REVEALING from the workshop captures the idea that a user interface for non-expert users should initially appear relatively simple and easy to grasp, and that the system should only reveal additional "depth" (contents or features) when the user becomes active and looks for it. The pattern is described in more detail in [Borchers, 1999]

This pattern lies at a high level of abstraction: it addresses how the complete task of theuser is dealt with. Its function lies mainly in perception, as it suggests how much information to display or otherwise output to the user.Its physical dimension is sequence, as it deals with the distribution of this information over a sequence of user events, e.g. subsequent screens of an information system.

![](images/de2aa94e9dba57163cd72e1db3858b9413e946cfbd84675034901638bfc83ebd.jpg)  
Figure 2.4: A taxonomy of human-computer interaction design patterns. [Borchers, 2000a]

Theworkshop also applied the concept of a Writers' Workshop to the interaction patterns submitted, and the entire workshop was considered very successful by participants and outsiders. Nevertheless, it also made clear that the software engineering patterns community requires more input from other disciplines such as HCI.

The results from this Workshop on Interaction Patterns are described in more detail in [Borchers, 2000a]1.

At the INTERACT'99 conference on Human-Computer Interaction, the next major workshop on the subject was coorganized by the author. It builton the previous findings, and delivered several new results:

The workshop agreedon a"user-centred" definition that describes HCI Pattern Languages bydefiningwhatthey can be used for.

"The goals of an HCI Pattern Language are to share successful HCI design solutions among HCIprofessionals, and to provide a common language for HCI design to anyone involved in the design, development, evaluation, or use of interactive systems."

[Borchers et al., 2001]

Several organizing principles for HCI design patterns were conceived and elaboratedin more detail. An important point is that the ultimategoal of any organizing principle is to support an iterative design process, with the connections in the patterns hierarchy always leading the designer to the next logical step to consider.

The first principle classifies patterns according to scale, similarly to Alexander's sorting hierarchy.It has to take into account,though, that the dynamics of user interfaces require incorporating time as well as space into such a classification. The resulting categories were:

• Society (beyond systems)

• Multiple Users

SocialPosition

• System

• Application

•UI structure (Dialogue)

• Components (containers, windows, layout)

• Primitives (buttons and other simple widgets)

• Physical properties

An interesting observation is that the real world of technology changes fastest in the middle area of this scale, between system and components.Since patterns are by definition supposed to capture some timeless quality, it may be particularly difficult to write genuine patterns for this area. At the same time, many existing guidelines — and many of the submitted patterns—address exactly this middle level, which may render them obsolete rather quickly.

Another possible organizing principle that the workshop developed is to follow the HCI design process, leading from analysis- to structure-oriented patterns:

• The highest level is culture and society, followed by environment and role of the user

• The next levels are use and navigation (incorporating affordances and, for example, issues of safety versus exploration)

• After those analysis-oriented levels, structural levels follow

• As an example, tasks can be further classified into retrieval, monitoring, proactive and reactive controlling, construction (writing a document), transactions, modifications (changing contents or structure), calculation, workflow, and communication.

The patterns submitted to that workshop can be sorted according to the above organizing principle of scale:

• An example of patterns at the Multiple Users level is Lyn Pemberton's LETPEOPLE OVERHEAR,which addresses issues of cooperative work.

•Patterns at theSystem level include Ger Koelman's EXPLORABLE INTERFACE and Jan Borchers'INCRE-MENTAL REVEALING, which both dealwith the overall impression that a system conveys.

•Patterns that deal with how to design individual applications include Lyn Pemberton's JUST THEUSUAL about application vocabulary and Peter Windsor's SITUATION DISPLAYandWORK QUEUEpatterns for overall appearance for a certain type of applications.

• Most of our patterns addressed the Dialogue level, such as David England's AVATARJOINING for temporal UI aspects of virtual worlds, Diane Love's selection patterns CHOICE OF SUBLIST FROM A LARGE LIST and CONFIGURING ORDERED SLOTS IN HARDWARE, and Fernando Lyardet et al.'s IN-FORMATIONON DEMAND, BEHAVIOURANTICIPA-TION, INFORMATION-INTERACTION DECOUPLING, and BEHAVIOURAL GROUPING patterns for navigation. RichardGriffiths'GIVEA WARNING also falls into this category.

• Patterns describing solutions at the Components level include Barbara Mirel's INFORMATION FLOW FOR PRECISION for data visualisation and Janet Louise Wesson's List Selection pattern.

• The level of Primitives is covered by patterns such as Martin Hitz's SELECTIONITERATOR, which also contains implementation recommendations.

• The Physical Properties level contains patterns such as John Thomas'SUPPORT THE HANDS WITH SPECIAL-IZED TOOLS.

•Some patterns do not address design issues of interactive systems, but rather aspects of the software development process such systems require, and therefore do not fall easily into the above categorization. Examples include Michael Mahemoff'sONLINE REPOS-ITORY for developing internationalizedsoftware.

As an example, the workshop agreed on a definition of a "typical" HCI design pattern, DESCRIPTIONAT YOURFIN-GERTIPS. It captures the idea of adding temporary information to objects in the user interface to deliver short explanations without permanently cluttering the interface space.

DESCRIPTION AT YOUR FINGERTIPS  
![](images/a920cef14673e9c8ac37f2e026d1c8ae695a4b42a146ac3f4fb596f0086d83ed.jpg)

You are putting interactive objects on a dynamic medium such as a screen and you want to provide various levels of context sensitive help supporting uninterruptable tasks.

Extensive explanations tend to clutter the interface but users may need such help. They do not want to leave the context of their current task, and experts may not want to see the help at all.

In the Mac OS®, a small balloon of textual help appears when the user turns on this feature and moves the mouse over an object. In Windows Tool Tips, the same happens if the mouse hovers over an object. In Netscape, the URL of alinkis displayed in a fixed position atthe bottom of the screen if the cursoris moved over it. In a voice mailbox, options are explained if the user waits for a while.

Therefore: Provide a short description of the object either close to it or in a fixed position. Let users turn it on and off or only provide it on some explicit user action (e.g. hovering).

Alternative representation:

![](images/37087a66c0916d1d4c71d2fc06c22e47db03e1c42ca1528bd7ae13152ac8bc79.jpg)

You can use three-state buttons to implement descriptions like this. Longer explanations can go into on-line help, possibly delivered via an intelligent agent, or in the manual.

The overall structure follows the Alexandrian format quite closely. It is amended by an alternative, pseudo-code representation of the concept that is more suitable to represent the pattern dynamics over time.

A similar pattern has been described by Tidwell [1998] under the name SHORT DESCRIPTION.

## 2.4 Pattern Languages in Other Disciplines

One of the claims of this text is that the pattern approach can also be used to model design-like knowledge from the application domain ofa software project. To show that it makes sense to look at domains other than architecture, software engineering, and HCI, several examples of pattern approaches for diverse domains are described below.

The large appeal of the pattern concept may partly be due to the fact that, according to cognitive theory, patterns might be a particularly effective way to organize complex information in general [Barsalou,1992].

This idea of creating a vocabulary implements the wellknown results from psychological research about verbal recoding: "When there is a story or an argument or an idea that we want to remember [... ], we make a verbal description of the event and then remember our verbalization" [Miller, 1956]. The idea can be recalled when its short name is remembered.

Casaday [1997] suggests applying the idea of pattern-based design to the creation of usable interactive systems. He argues that patterns in a broader sense can be found in architecture, organizational behaviour(archetypes), history of science (paradigms), military theory, studies of mythology (archetypes), and even basic text writing(templates). In fact, the software engineering PLoP community even has created a pattern language for the process of writing patterns [Meszaros and Doble, 1998].

Several others have noticed the potential of pattern languages for interdisciplinary design. Denningand Dargan [1996], for example,in their theory of action-centred design, suggest a technique called Pattern Mapping as a basis for cross-disciplinary software design. Referring to Alexander's work, they claim that patterns could constitute a design language for communication between software engineers and users, just as Alexander's pattern language does between builder and inhabitant.

Granlund and Lafrenière [1999b] use patterns in their pattern-supported approach (PSA) to describe business domains, processes, and tasks, in order to aid early system definition andconceptual design. The authors also note the interdisciplinary value of patterns as a communications medium, and the ability of patterns to capture knowledge from previous projects. The business domain and process patterns are intentionally not patterns inthe Alexandrian sense; they do not include asection describing a solution to a problem that they discuss. Consequently, the pattern format used is not uniform. In contrast to Alexander, the patterns are relativelyshort and not as elaborate.

Their approach served as common ground for a workshop on user interface patterns at the 1999 Usability Professionals' Association (UPA) Conference. The major results of this workshop [Granlund and Lafrenière, 1999a] are summarized below:

•A distinction between Alexandrian design patterns, andinformation patterns was introduced. The latter describe information about user, context, and task, and lack the problem and solution parts.

•The need for conceptual design patterns, "blueprint patterns" for the overall conceptual design, was expressed to avoid concentrating on individual parts of a system design.

•The problem of finding the right balance between too generic and too domain-specific patterns was also addressed: for example, patterns describing tasks could be divided into a generic part with “framingforces", pointing to general conceptual design patterns, and a domain-specific part including forces, consequences, and examples that only apply to a concrete domain.

•Finally, a major point stressed by the workshop is that the process of creating and using patterns must not become too mechanistic and complex. Otherwise, the inherent ease-of-use of good patterns would be lost.

Most of the events mentioned above have been collected on the HCI Patterns Home Page [H:Borchers99].

## 2.5 A Comparison of Central Pattern Collections

While numerous other projects applying the pattern concept to new domains exist, this chapter comprehensively covered the important fields for the present work, especially the area of human-computer interaction.

Alexander, Gamma, and Tidwell

To summarize, here is a table comparing the most notable pattern collections in the various fields discussed above.

<table><tr><td rowspan=1 colspan=1>Patterncollection</td><td rowspan=1 colspan=1>Domain</td><td rowspan=1 colspan=1>Components</td><td rowspan=1 colspan=1>Format</td><td rowspan=1 colspan=1>Uniformity</td></tr><tr><td rowspan=1 colspan=1>Alexanderet al. [1977]</td><td rowspan=1 colspan=1>architecture</td><td rowspan=1 colspan=1>name, ranking, picture, context,problem statement, problemdescription with forces andexamples, solution, diagram,references</td><td rowspan=1 colspan=1>structuredtext, photosanddiagrams</td><td rowspan=1 colspan=1>++</td></tr><tr><td rowspan=1 colspan=1>Gamma et al.[1995]</td><td rowspan=1 colspan=1>softwaredevelopment</td><td rowspan=1 colspan=1>name, classification, intent,aliases, motivation,applicability, structure,participants, collaborations,consequences, implementation,sample code, known uses,related patterns</td><td rowspan=1 colspan=1>structuredtext,diagramsand sourcecode</td><td rowspan=1 colspan=1>++</td></tr><tr><td rowspan=1 colspan=1>Tidwell[1998]</td><td rowspan=1 colspan=1>user interfacedesign</td><td rowspan=1 colspan=1>name, examples, context,problem, forces, solution,diagram (sometimes), resultingcontext, notes</td><td rowspan=1 colspan=1>structuredtext andbullet lists,somediagrams</td><td rowspan=1 colspan=1>+</td></tr></table>

Figure 2.5: Comparing major pattern languages from different domains.

Comparing the central pattern components and their format across different domains shows that there is indeed a high level of agreement on how a pattern language should be structured. This result will be used in the following chapter to define a domain-independent formal model of pattern languages, leading to the central idea of this work, an interdisciplinary pattern framework for the design of interactive systems.

The comparison also reveals that the selected language for HCI patterns is less uniform in its structure than the examples from the other domain. This is true for most existing HCI pattern efforts, and indicates that the concept of patterns is not yet as mature in HCI as in the other disciplines.

## 2.6 Requirements for an Interdisciplinary Pattern Language Framework

With the state of the art in pattern languages in HCI and other disciplines in place, it is time to pose a number of requirements that an interdisciplinary framework based upon pattern languages should fulfil.

Cross-discipline readability. The frameworkshouldlead to patterns that are written in a style readable for people from other professions. Those people may be involved in the design process, where their studying the patterns can improve the outcome of a current project, or they may have learning demands. This generally means writing prose instead of shorthand bullet lists, using a minimum of cryptic jargon, and providing understandable examples for nonprofessionals.

## Domain-independent, uniform, well-defined format.

The framework should define a consistent overall format for all pattern languages that are created, independent of the domain they address (such as HCI, software engineering, or application domain). Only minor adjustments (such as example media type) should be necessary to cater for the specific needs of each discipline. This format should be specified in a formal way to avoid ambiguous interpretation. (This does not imply that the patterns are written as formulae—see the readability requirement.)

Empirical evidence. The framework should define examples in a pattern as containing published empirical evidence of the validity of the solution where possible.

Domain-appropriate, design-supporting hierarchy. The arrangement that the framework imposes on patterns within each language should lead to a hierarchy that guides a “designer" in the respective domain along the design process in a top-down, unfolding fashion. The arrangement criterion will therefore depend heavily on the domain.

Design dimension coverage. The framework should allow the pattern languages to cover all dimensions, including spatial or temporal configuration, that are relevant to each discipline.

Lifecycle integration. A framework proposing pattern languages as a major work document for interactive system design needs to specify a way in which the languages are to be integrated into a software development lifecycle.

Alexander's collection, while fulfilling the requirements of readability and uniform format, do not always give empirical evidence for pattern validity. Their spatial hierarchy is adequate for architecture, though not for other domains, and it does not cover temporal aspects of the artefacts designed.It does, however, offer a good explanation of a design process that uses those patterns.

The collection by Gamma et al. does not fulfil the readability requirement (it is aimedonly at developers), but it also has a very uniform format, andgives good empirical evidence. There is, however, not a very supportive hierarchy of the patterns, although they are linked to each other. Using various diagram types, it covers spatial and temporal aspects of a design, but its integration into the lifecycle is not defined; it is rather regarded as a repository to be studied and then used in whatever process model is being used for development.

The collection by Tidwell is quite readable for outsiders, although the format is not quite as uniform, and not all patterns are as elaborate and complete as desired in the above definition. It usually gives empirical evidence, and uses a hierarchy that aligns well with a typical top-down user interface design process. Time and space are covered in the patterns. The use of the language is discussed briefly in the introduction to the collection.

None of the above collections gives a formal definition of pattern structure, nor do they address more than their own single domain.

The following chapter will present an interdisciplinary pattern-based framework forinteraction design that aims to fulfil these requirements.

This Page Intentionally Left Blank