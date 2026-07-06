# System Design

14

re've understood the user's model of work, we've captured it in work models, we've envisioned new ways for people to work— but so what? How does this help us with software design? Way back in Chapter 1, we discussed the idea of a system work model, the approach to doing work that's built into every system. The vision of Chapter 13 defines a new way of working, with many delivery mechanisms. IT shops can define new roles and procedures in concert with the business partner; commercial product developers can define services and training. But in this book we're focused on software and hardware systems, which embody the desired system work model. How do you make the transition from the vision and storyboards to a system design that delivers on their promise? In Contextual Design, we introduce a new modeling technique to reveal the system work model and show how all the parts of the system relate to each other in the user's experience.

## KEEPING THE USER'S WORK COHERENT

The challenge is to keep the system work model coherent, so that it supports the users and fits with their expectations while extending and transforming their work practice as prescribed by the vision, Coherence isn't just about consistency of the user interface—a coherent system keeps the user's work orderly and natural. When a presentation tool won't let its users change slide notes and slide contents at the same time, making them jump

Design challenge: to keep work coherent by keeping the system coherent

back and forth between views, it breaks up the work. When a word processor provides three successive cascading dialog boxes to choose a bullet, it turns a minor function into a whole task, complicating the work. When an email system lets users search the address book by providing a simple text entry field that filters the address book names but uses a separate query window to search the "sent mail" folder (Figure 14.1), it provides inconsistent structures for doing similar work. When the system work model is coherent, it keeps the user's work coherent; when it fragments, it's the user's work that is disrupted.

Keeping the system model coherent is hard enough when it's one user doing a single task. It's even worse in real systems, which support multiple people playing multiple roles, across departments or the whole business, while using several systems. One user we talked to was verifying information given to her by another department. The information on the form was accessed by several different applications. By the time she was done, she had used 11 screens in four applications to check a single form. Another user wanted to see what drugs a person was taking while recording a clinical event. His information was online, but he had to leave the application he was using and get into an entirely separate one to get at drug records. In both cases, the users had multiple systems, each designed to solve a single problem. These systems didn't address the user's whole job and didn't attempt to make the work fit

together across the different departments or tools. When work practice is too large and complex to see, or it's too hard to address all at once, it's easier to write simple systems that address single problems. But then the systems chop up the work and leave it up to the user to put it back together by taking extra steps or doing additional work on the side.

From the developer's side, the picture is no easier. Software development organizations start projects to address specific problems, and only later do they realize that the systems don't hang together and don't build up into a coherent solution. This leads to conflicts down the road:

You've put a personal organizer in your product? But we're chartered to build the company's solution for personal organizers! And why does the operating system have a to-do list?

We started 10 years ago with a basic system. But we've added on so much that now we have over 50 applications and no clear idea how they fit together. I'm not even sure we know where all the duplications are.

![](images/d5dfab11371ecf4e434d85f3d8f78f1d55f92ce094945c145ff03cc292f86a43.jpg)  
FıGuRE 14.1 Claris Emailer: Two ways of finding: one with a query dialog box, one with a filter.

We do charting. We don't do data reduction—that's the database's job. I know you can't currently do the data reduction you need to do to use our charts, but that's the database's problem.

How can an organization figure out where the boundaries between applications should be, so that every work task is addressed once and once only, and no part of the work falls through the cracks? In the end, the system work model that matters is the one supported by all the applications together—how can an organization see it, design it, and deliver it?

## BREAKING UP THE PROBLEM BREAKS UP THE WORK

One solution to handling the complexity of work is to choose to address only a small part of the problem. As we've seen, that tends to break up the work for the customer. Addressing the whole of the work coherently means building a bigger system or tying together multiple small systems seamlessly (an even harder problem). As the size of the system or systems goes up, keeping the systems themselves and the work practice they support coherent gets harder and harder. A small system can be designed and built by one person—keeping it coherent isn't so difficult. But it takes multiple people working in parallel just to get all the details of a larger system worked out.

A common solution is to anoint an “architect" or architect team with the responsibility of tracking the whole system and catching any

discrepancies. The work itself is done by carving the system up into pieces, assigning pieces to individuals, and letting them work out the details. But as we discussed when introducing work moels in Chapter 5, as soon as any system grows beyond the very simple, it's just too hard to balance all the factors without some external representation to manipulate. Furthermore, in a large system, too many different people and groups are building too many parts—it's too hard to keep track of all the relationships. As soon as several people get involved in the design, they need an external representation to focus their discussion and capture their agreements. It's no longer enough for the whole design to stay in one person's head.

Passing out pieces for people to develop independently throws the whole design out of balance unless everyone really knows the whole design and how their part fits. Give one person a single part to design and build, and what should be a minor feature can turn into a whole miniapplication (Figure 14.2). Designers find it hard not to treat their assigned part of the system as the most important—not only is their ego involved, but it is the most important part for them. It's no wonder so many small features turn into a larger and more complicated design than necessary.

It's no wonder that designers create a dialog box that is almost like the one their neighbor designed, but with the one or two extra features they can't do without. It's no wonder that what started as a simple dialog starts to feel like a small application. Dividing the system up among team members tends to pull the design apart—it's up to the design process to provide mechanisms that keep it whole.

## A SYSTEM HAS ITS OWN COHERENCE

While storyboards capture a coherent story of a single task, each storyboard can only follow that one thread. A full system supports many different tasks and roles. Storyboards work out system implications sequentially, by considering what happens in order to perform a task. But the system needs to hang together with its own organization and structure. That organization and structure has to be designed as a whole if the system is to be coherent.

It's as if the stories of use are patns across a university quad, each one wearing out the grass a little along that path. Then the grounds-

keepers look at the paths all together and decide that here, where two paths run almost together, they can be merged and paved; and there, where four cross, there might be a little courtyard with benches. The people making the paths are following their everyday life activities without thinking particularly

Good design for individual work tasks is not enough

about where they walk but following the best path for them; the groundskeepers are withdrawing from day-to-day events to see the implications on the whole “system."1 And once the groundskeepers put new physical structures in place, people discover new possibilities and build on them—perhaps the courtyard becomes a favorite spot for street musicians. When structure is well designed, it's flexible enough to support additional uses, unforeseen by the designers.

![](images/f9703433cf7b45a7ec1d057cbf65916d7c9ec3342acafe021d40898a06430f35.jpg)  
F1GuRE 14.2 Apple's LaserWriter 8.4.1 print dialog—what happens when printing becomes an application. How many different dialogs are really needed to print  file?

In the same way, designing a system based solely on storyboards— or use cases—would optimize each sequence of use at the expense of the system as a whole. Tell the story of nine different users, each with different printing needs, and each dialog in Figure 14.2 might make sense on its own. It's only when they are seen together that it's clear the interface is overcomplicated. Walk two separate cases for filtering address books and filtering sent mail, and each interface in Figure 14.1 makes sense. It's only when put together in the context of a system that they become inconsistent.

Good design tends to alternate berween sequential and structural thinking. The initial quad design was a structure, designed as a consis-

tent whole and put in place to be used by many people many ways. The actual use by any person is sequential: they came in here, crossed to there, sat on the grass after that, and left over there. Each individual sequence of use hangs together for that person. The next step of design switches back to structure. The groundskeepers looked at all the patterns of use

together (as recorded by worn grass) and redesigned the structure to better fit its use. This step of seeing all the parts of a system as they relate to each other is an intrinsic part of systems design. Seeing and balancing the parts of a system against each other goes beyond a pure task-oriented approach by introducing a focus on the structure of the system itself.

## THE STRUCTURE OF A SYSTEM

A courtyard's easy enough to see and design. How can the design process make it equally easy to see the structure of a complex system? What is the structure of a system that designers need to see and manipulate, and how does it relate to the structure of work?

Consider a user reading mail: First she scans her new messages looking for something important. She doesn't care to see the whole content of every message—that would be a distraction. She just wants to know who it's from and the subject line to decide what to read first. Then she decides on one to read, and suddenly

The structure of a system determines how well it supports work

Good design process alternates between sequential cases and structural models

she needs a new context for doing this new activity. She no longer needs to see all her messages, but she does need to see the whole content of this one. Her intent changes—she's not wondering what important messages she might have been sent anymore, she's reading to find out what this one message says. Accordingly, her tools change instead of seeing and scrolling over message headers, she's reading through message content.

Our user situated herself in a place in the product that suited the needs of the activity she was engaged in and stayed there a while,

scanning messages with the tools provided. Then, when her activity and needs changed, she moved to a different part of the product where she could do the different kind of work associated with the new activity. The structure of the system consists of the places in the product where she can work, the func-

tions that support work in each place, and the links that allow her to move from one place to another. The places do not impose any one sequence of use. Like the areas within a quad, they all exist together, offering the possibility of any number of different uses. But the structure they offer may make work convenient and easy to do or make it difficult. Customer-centered design seeks to build a structure into the system that supports the user's natural movement through her work and is flexible enough to enable the invention of new ways of working. Seeing this structure and reworking it to fit the user better is equivalent to the gardener restructuring a quad to better fit its usage. That's what designing the system work model is all about.

Designing the system work model as a whole runs counter to the engineering principle that every part should be self-contained so that changes to any part are isolated to that part. That's one reason for thinking of the implementation in terms of opaque modules or objects. But some approaches to design that work well for engineering the implementation get in the way when designing the system work model. Suppose Joe invents a way for users to scan and search without entering a query and uses it in the piece he was assigned. There's no way to keep users from expecting this approach throughout the system because the parts aren't isolated in the users' experience. Having encountered the mechanism in one part, users expect to find it in every similar situation. So keeping the design coherent means that after a part changes, the designers must step back, look across the whole system, and see what impact that change has on the rest of the system. The system work model is a single whole—every part exists in relationship to every other part, and a change to one may ripple throughout the system.

## DESIGNING STRUCTURE PRECEDES UI DESIGN

Designing the system work model to fit the user is a problem of structuring the system well, not of designing the user interface or implementation. User interface and implementation are the next layers of detail in the design process. When the makers of PowerPoint decided to make one view, and only one, that edits the contents and layout of a slide, they made a decision about the structure of their product. By implication, they made an assumption about the structure of users' work—that it is reasonable to concentrate all slide changes in this one view. In the same way, when they decided not to give control over flying bullets for on-screen presentations from this view, they decided that was a function that did not need to be part of this work. These are structural decisions—they decide what the system should do and how it should be organized, but say nothing about how it should look or be implemented (Constantine 1994a).

Structural decisions of this sort precede decisions about the user interface. It doesn't make sense to design screen layouts until you've decided what function the screen should implement. It would be as though an architect started design by choosing rugs and materials for the countertops. They don't; they start with rough sketches that they work up into a floor plan. The floor plan captures the right level of detail for talking about the struc-

Use a language of structure to maintain a focus on structure

ture of a house—it shows the parts and their relationships without showing how the house is decorated. The user interface of a system is equivalent to the decoration of a house. It matters, but if the structure is wrong, no user interface can fix the problems.

In our initial design teams, we found that team members tended to slide into conversations about the UI before they were ready before they had agreed on base structure. They were like architects who could only communicate by drawing pictures of the proposed house. "We want this function in this window," one would say, sketching a row of buttons. "The style guide says those should go on a pull-down menu," another would reply. "Do you really want to use that word?" a third would ask. When the very language suggests that the user interface is the topic of conversation, it's hard not to be distracted by it. But how could we represent the system work model directly, free of any UI implications?

The pattern of working we found in software—working in a place, moving to a new location, and doing a new kind of work in that place—is not unique to working in a system. In fact, it's very like living in a house (Winograd 1996). To start dinner, a person goes to the kitchen, where the tools for cooking are located (knives, bowls, stove). A drawer sticks, and he decides to take it to the workshop and plane it down while the water boils. He moves with the drawer to another place, which has the different set of tools useful for minor carpentry, and works on the drawer there. Then he goes back to finish dinner. A house consists of places to do things, functions or tools that help do things, and access allowing people to move between places. The parallels between living and working in software and in houses suggest that studying the role of a floor plan might shed light on the appropriate representation of a system work model.

A floor plan occupies a unique role in the design of a house (Figure 14.3). It's less physical than an elevation, which shows a view of the house as though you were looking at it (an elevation is more like a UI picture). It doesn't show wall color or how the house is finished (which would also be more like a UI). Yet it's not at the nuts-and-bolts level of a construction diagram, which might show how to put a wall together but doesn't show anything

the homeowner can relate to. The floor plan selects a few of the most salient aspects of a house as it supports living and represents them: the spaces in the house, their sizes and relationships to each other, the things in each space that support the kind of living done there (stoves, refrigerators), and the access between spaces.

As a diagram, a floor plan supports a conversation about how well a design supports a particular style of life, and allows the architect to compare that with the life the house's prospective owners want to have. Architects can walk stories of living through the floor plan to see how well it fits the homeowners. Is a room too small for the way the owners want to use it? Is it too hard to get from one room to another? Is there a lot of dead space devoted to halls or intermediate areas? The floor plan lays out all the parts of a house, letting the architect walk different cases and scenarios through it. Rules of thumb, such as constraints on minimum clearances, layouts that work well, and the limitations of construction materials, ensure that the resulting design is usable and implementable. Of course, once the house is built, meals may be eaten in the kitchen, and the dining room may become a music room. A good structure will permit different uses, which the architect never designed explicitly.

![](images/0dcd4f1457217332f27fabc7bea2cdbe8b3b3d115cd59b370ba60eec5f37dcdf.jpg)  
FiGuRE 14.3 A floor plan. Notice how the important distinctions are immediately apparent—the relative size of the spaces and the access between them. Details that are unimportant for understanding the structure of the house—rugs, wall surfaces—are absent or inconspicuous. (Even the tile around the woodstove affects access because people will walk around it.) But the drawing does tie to the users' experience of moving through a house. It also puts construction details in context the dark squares in the walls indicate supporting posts, and the numbers in circles key this diagram to cross sections showing wall construction. This is what we are missing in software design—a single representation that shows how all the parts of the system relate in the users' experience and how they relate to the implementation.

## THE USER ENVIRONMENT DESIGN

Contextual Design represents the system work model in a new modeling technique, the User Environment Design (UED). The User Environ-

ment Design plays the same role in Contextual Design that the floor plan plays in house design. Just as a floor plan represents the key distinctions for supporting living, the User Environment Design represents the key distinctions for supporting work practice with software systems. Like the floor plan, the

representation shows all the parts of a system that the user knows or cares about, what aspects of work each part supports, and how the parts of the system relate to each other (see Figure 14.4 for an example). Like the floor plan, it ignores UI details to reveal the underlying structure, uncluttered by surface appearance or by implementation details. In fact, the User Environment Design has no representation for these details, so it's hard for a conversation focused on a User Environment Design to go into details too soon. (In this way, it fills the need for a blueprint for software design identified by Denning and Dargan [1996].)

The User Environment formalism highlights the key concepts for designing a system work model. Focus areas show the coherent places in the system that support doing an activity in the work. They're the "rooms" of the system. Like rooms in the real world, they should support the activities that happen in them well. They should provide the function that's needed to do that work, and only the function that's needed. They should contain, organize, and present the objects that users need to work on. And like rooms in the real world, they are connected—the arrows between focus areas show how the user can move from place to place as their work requires it. Like paths traversing a quad, a new User Environment Design is built from storyboards, collecting the different stories of use into one structure supporting them all. User Environment Designs can also be built to represent existing systems, revealing their structure and highlighting problems (Figure 14.5).

![](images/863f6c8879c503598e6f90205bf3609cb7858bea9b23b254844e0266d68cc047.jpg)  
F1Gu RE 14.4 A User Environment Design for a part of a mail system. Each box represents a "focus area," a place in the system. These are like rooms in a house, which permit the user to focus on one particular activity. The purpose statement describes the work the focus area supports. Functions, which enable the user to do work, are listed in the focus area, as are the work objects that the user works on there. The arrows between focus areas are links and show how the user can move through the system.

This form of User Environment diagram is on its way to becoming a specification for the system. Each focus area collects and describes the functions provided the user in that focus area. The focus areas act like checklists, allowing designers to review the function in each place and verify that all the function is needed there and that all needed function is available.

![](images/ac1b8aaab3cf3da5f745c547b06e729b2ad7dc45f60970af8b037cb7bbe7c67c.jpg)

ad se  es  ( aoe s sseioke. shoesewe e (e e ) aee  e eie, e e s a-wninm a  ons t   ot nne rse s e  o a o  aaio n ae s si ui l! op ne ro s  w e s o  r e   a at wos e e n ness ees ne ne o oo e -ee aee eodns (aeoio e oe) see so o aes cs ocl. ane ss w i  a ov. aeei e oe moe woe , on ec mae mveced uavi  ear r i r ai reai s  rar se pern  ptahe rvve sos o o coon a o os s as scwho (Onse es Sas croi nes es seaaes (es) es ndes Beyor e s s s ose dos o e do se ct s  ars as s so  s ,e as emp. o   t        she

Because focus areas are the most visible concept captured by a User Environment model, the model helps designers organize the sys-

tem so it fits the work. Do users spend time scanning their mail messages, choosing which ones to look at? Then it makes sense to create a distinct part of the system that helps them do that. After choosing a message, do they then concentrate just on that message and what it's about? Then seeing other messages is a distraction, so it makes sense to provide a separate area to focus on a single message. What's involved in reading a message? If

The UED reveals structure

users often want the sender in their address book, adding the name to the address book should be a function available in that place. If users never scanned messages, but simply worked through them one by one, there would be no need for a separate

place to see all messages. If they needed to see what messages preceded and followed the message they were reading, the place to read should be integrated with the place to scan messages. (In a bulletin board, where messages are captured in threads of connected conversations, readers do want to see the context of messages, and products often do connect the two places.) The structure of the system must be designed to fit the structure of the work, and the User Environment model makes the system structure explicit.

## REPRESENTING THE SYSTEM WORK MODEL

Capturing and representing the system work model in a User Environment diagram gives designers a way to see the whole system and keeps design at the right level.² A user interface would be too detailed—it invites the team to get caught up in issues of layout and appearance that can be put off until later, after the base structure is in place. Data flow diagrams show movement and transformation of data intrinsic to the work, not the structure of the system that the user experiences. Structure charts show the components of the system at a higher level of detail than code, but are focused on the structure of the implementation, which is not experienced by the user directly. The same is true for object models: an object hierarchy provides a way to see and structure the implementation, not the user's experience.

Of course, people claim object models can represent anything, and it's true that an object model can represent the parts of a system

design. But to be a good design and thinking tool, a model should evoke the thing being designed, making the right issues explicit and concrete. Designers manipulating the model need to feel like they are manipulating the real thing. An object model could

A good model evokes the reality it represents

capture the data in an architect's floor plan——but no architects using such a model would ever feel like they were manipulating space, as they do when they manipulate a floor plan. If the model is too far from the actual design issues, people using it have to make a translation in their heads. So it's not good enough to be able to make a mapping from a modeling technique to the issues for the system work model—a new model is needed to represent the user's experience. An effective model will influence designers' thinking by making the relevant issues jump out, just as work models influence what interviewers see in the workplace.

Such a model won't supplant object-oriented design, of course. In an object-oriented design, the object model keeps the implementation consistent—in the object model, developers bring functions from different use cases together into a single object class. They identify the reusable parts that different system components can use. But that's at the implementation level—the object model represents the different parts of the code, invisible to the user. The structure of the system as the user experiences it needs to be kept coherent as well.

## THE USER ENVIRONMENT FORMALISM IN THE DESIGN PROCESS

The User Environment Design occupies a place in the design process between storyboards on the one hand, and user interface design and

object analysis on the other. It makes the discussion of the system work model tangible by providing a physical representation. In this way it helps to separate the conversation about the system work model from the redesigned work process (represented in storyboards), from the system appearance (represented

Explicit models help keep design conversations separate

## TASK-ORIENTED OR OBJECT-ORIENTED?

Is designing with storyboards and User Environment Design task-oriented or objectoriented? On the one hand, it's clearly not object-oriented because the User Environment Design does not focus on identifying common objects as its primary feature. Its most salient concepts are coherent activities—the focus areas—and flow between them. Yet it's clearly not task-oriented either. A User Environment Design prescribes no order, as storyboards do. It shows the parts of the system and their relationships independent of time. Many different stories of use can be walked through a User Environment Design to see how well it supports them just as many different stories of individual actions can take place in a house.

In fact, even in pure object-oriented design from use cases, object modeling does not stand on its own. The purpose of a use case is to tell a coherent story of how the users will work and the system will meet their needs (Jacobson et al. 1992). From this, object modelers can extract the objects and their behaviors. But neither use case nor object model provide a good representation of the system work model. The use case is task-oriented, telling one story of use, for one task, but it doesn't provide a coherent view of the system. The object model gives a coherent view of the system, but not the system the user experiences. Instead, it's a view of the system the developers will implement. It's not customer-centered because it's not focused on keeping the user's work coherent—and rightfully so, since it's an implementation tool. It is supposed to keep the implementation coherent—elegant, evolvable, extensible, and maintainable.

This is true even of so-called object-oriented user interfaces. These reveal to the user only a small proportion of the objects and behaviors of a full object model for the system. Objectoriented user interfaces achieve consistency by presenting objects as identifiable screen artifacts with consistent behavior. But what objects should the system present? How should they be organized? And what behaviors should they have? These are the questions answered by the system work model.

The basic question is, How do designers decide what the objects and behaviors should be to support the user? That's the question answered by the User Environment Design. Rather than base object definitions on use cases, the User Environment Design introduces a coherent model of the system that can be designed, structured, and corrected before object definition starts. In the end, it's neither task-oriented nor object-oriented. By focusing on the structure of work in the system, it's work-oriented and that's what makes it powerful. (Rosson and Carroll [1995] suggest another approach to integrating object-oriented and task-oriented system views.)

by the user interface), and from the internal system structure (represented by the object model). When each conversation has its own physical representation, the design discussion is easier to have. Is the team arguing about how to change the user's work? Then they're standing in front of a storyboard, changing it to reflect their thinking. Are they arguing about how to organize the system to support that work? Then they are modifying the User Environment Design. Are they arguing about appearance and layout? Then they're changing parts of the user interface. Everyone can tell which issues to pay attention to because that's the model the team is updating.

User Environment Designs support the natural alternation between sequential and structural thinking. Storyboards and use cases are

sequential; they tell a single series of events in order. The vision, User Environment Design, and object model are structural; they show all parts of the system and how they interrelate, though they focus on new work practice, the system work model, and internal structure, respectively. Each sequential step follows a story of use to work out the details of the

Alternating between sequential and structural thinking drives design details

preceding structure and uncover problems with it, so storyboards help the team work out the details of a vision, and use cases help work out the details of a User Environment Design. Each structural step pulls together the implications of different stories into a coherent system. The designers step back to see how each sequence affects the structure as a whole. So the User Environment Design integrates one system out of multiple storyboards, and the object model integrates one model out of multiple use cases. When a single structure is created, it can be checked for accuracy and completeness—the functions of a User Environment Design and behavior of an object can be reviewed and anything missing added. This continuous process of working out details, integrating, and checking ensures the integrity of the resulting system. Each transformation acts like a structured walkthrough, forcing the team to review all parts of the system from a different perspective (Figure 14.6).

The User Environment Design is created first to support design. It enables the design team to keep the system coherent. But because it

represents the structure of the system as the user experiences it, it supports customer-centered project planning. Grouping focus areas that address specific roles identifies subsets of the whole design that sup-

The UED aids planning

port a coherent part of the work and could be delivered together. Identifying focus areas that are closely associated with each other reveals a subset that is appropriate for assignment to an implementation team. Building up a User Environment Design to include external and third-party products creates a strategic design showing what corporate partnerships to create. Building a reverse User Environment model of existing systems identifies duplicated function and holes in the suite. By representing the parts of the system from the point of view of the user's work, engineers can see how their work relates to each other and to the user. And that keeps the whole development process coherent.

![](images/d07681fb75d1f6eb0fc8e04fd94b17e1656d30b114232ec8d5ef0d62eaa5051a.jpg)  
FIGuRE 14.6 The progression from design to development. This diagram shows the process of going from work models through systems design to implementation design. It shows the alternation between sequential, story-based thinking and structural, model-based thinking intrinsic to design. The stories build a structure that can be checked for coherence and completeness; the structure drives lower-level stories specifying more detail. Working out the stories reveals holes in the structure defined previously, and putting together the structure reveals inconsistencies in the stories. The stories show a particular instance of using the system; the structure shows how the system can support multiple stories. Contextual Design alternates between the two, providing physical representations all along the way.

One of the challenges of any design process is to keep the design coherent—to maintain the design team's ability to comprehend and operate at the level of the whole system while working on a part. Contextual Design continually returns to a coherent representation that pulls all the detail together. The consolidated work models show the whole customer work, structured and represented along each of the five dimensions. The User Environment model shows the whole system as experienced by the user, with all the parts and their relationships, independent of UI or implementation. The object model shows the whole

implementation architecture and how it is organized. Each of these representations is focused on the appropriate issues for its place in the design process, but each represents the whole system coherently. The User Environment Design responds to the work models on one side and drives the object

model, the user interface, and project planning on the other. It's the pivot between customer work and system implementation, making sure that the work as it happens in the system hangs together.

15

he goal of the User Environment Design is to present structural issues, making the key considerations salient for keeping the user's   
work coherent. IT keeps the design team focused on the customer by   
giving a physical representation to the structure of work that the pro  
posed system will enable for its users. To be a good tool for accomplish  
ing this task, the User Environment formalism organizes the presenta  
tion of the system into a structure that supports a natural flow of work.

We saw in the previous chapter that work consists of coherent activities. Each activity is oriented toward accomplishing some intent, requires a certain set of actions to accomplish, and is naturally connected to other activities that the user might choose to switch to, given what they are trying to achieve. By their structure, systems create places that can support an activity if they have the right organization and make the right functions available. The system work model fits the user when it matches the structure of activities and actions that the user needs to accomplish.

Just as any house has a floor plan, no matter how it was designed, any system has a User Environment model implicit within it. Any system can be analyzed, and its underlying User Environment model revealed. We introduced the User Environment Design informally in the previous chapter and showed some models taken from com-

Every system has a UED

mercial products. To introduce the parts of the User Environment formalism and their definitions, we'll walk through the analysis of another commercial product, Microsoft PowerPoint. As we go, we will show each part of the User Environment formalism and how they build up to a complete model.

![](images/ddf481ff4dd98a13332c81acc4b1a95f67cde2b8efbaf911a1b263d5be619ac2.jpg)  
FiGuRE 1 5.1 The main screen of Microsoft PowerPoint and the focus area that represents it. This window creates a place in the system in which to focus on creating, viewing, and changing the content of individual slides. This place is represented on the right, with the work that is done there summarized in the statement of purpose. Functions are available through different mechanisms—toolbar buttons, pulldown menus, the keyboard, and direct manipulation. In the focus area, we show only the functions, with no indication of how they are accessed. As is usual in a model built to analyze an existing product, the functions are high level (“add shape" rather than listing all the different shapes), and the model lists only the primary function in support of the purpose. A model built to design a new product would list every function and every shape designers intend to implement.

Figure 15.1 shows the main window of PowerPoint, a tool for making slide presentations. This window provides a place for creating and editing the content of slides. In the User Environment Design we represent places as focus areas, where you focus on doing a certain kind of work. Every focus area has a purpose, a succinct statement of the work the focus area supports. If you can't write a single sentence that describes the purpose of the focus area because there are so many different functions doing different things, it's likely that the system is poorly structured. Use the purpose statement to describe everything the focus area does.

This window provides functions that enable doing work in the place—to put rectangles, text boxes, and other slide objects on the slide, color and rotate them, and manipulate them in other ways. Functions are made available through menus, toolbars, keyboard com-

mands, and by direct manipulation. These are alternative UI mechanisms for performing a function; some functions can be accessed all three ways (e.g., to save the presentation, choose “Save" under the "File" menu, click the disk icon on the toolbar, or type CTRL-S). Which mechanism the designers chose to implement for a function matters—a poor UI or

inconvenient access to a function gets in the user's way—but it doesn't change the purpose of the place or the work done there. The UI mechanisms and screen layout are as much a distraction to understanding system structure as rug color would be on a floor plan. So we list the functions once on the right, with no indication of how they are accessed.

The “Edit slide" window also makes available the things the user needs to work on to edit a slide—the slide itself and also text boxes, shapes, lines, and clip art. These objects are collected and organized in the place appropriate for the job at hand—in this case, laid out on the screen to reveal the design of the slide. The focus area captures these work objects as an important part of the definition of the focus area. Later, when the object model is developed, they will be harvested as starting points for the objects.

Some of the function in this window leads to other places. Selecting the small icon at the bottom changes to the slide sorter view. This

changes the view and the function available——it is no longer possible to create and edit the content of slides here. Instead, the slide sorter supports viewing a whole presentation in order, changing the order of slides, and controlling the transition from slide to slide. Because the work that can be done is different,

the slide sorter supports a new activity in a new place, and we represent it with a new focus area. The function that switched from one to the other is a link, shown on the User Environment Design as an arrow (Figure 15.2). You'd expect to find links between focus areas whenever the user might need to switch between the activities they support.

This much of the User Environment formalism will represent 90% of most products. However, there are some additional cases, the

Links between focus areas enable a shift in attention to another activity

![](images/47dbf48954da5b69da681c15cc556348c6c5b11e6637b07e5f08afb5a90efd89.jpg)  
FIGuRE 15.2 Links between focus areas. These three focus areas support distinct but related activities. They declare that when a user is worrying about the detailed content of one slide, she is not concerned with the overall structure of the presentation. Conversely, if she is worrying about the overall presentation, she needs to see and recognize slide content, but doesn't need to change it there; she's willing to switch back to the “Edit slide" focus area and lose the context of the whole presentation. This works reasonably well, but on the other side users do need to change slide notes and slide content together. When developing a slide, we have found that users naturally develop notes and slide content in parallel, moving information from the notes to the slide and back as the idea of what is presented shifts. The division of the work in the current design does not support a fluid movement between notes and slide content. The User Environment model above shows the connections and reveals the issue.

most important of which is the double link. When the user needs to do the work of one focus area in the context of another, we show a double link between the two focus areas. The spell checker is clearly a separate focus area from the main slide show—in this focus area, you think about spelling and dictionaries, not about the overall layout and content of your slide. But on the other hand, it's also closely linked to the “Edit slide" focus area: when you move to the next spelling error, the main window switches to display the slide with the error on it and attempts to position the slide so the error is visible. So we represent the spell checker as a double link to the “Edit slide" focus area (Figure 15.3). This indicates that the two cooperate to support the work, that the user needs to know where they are on the slide while checking spelling and needs to switch back and forth rapidly between the two. (When errors are marked as you type, the function has been merged into one focus area.)

![](images/8a6c19533e4cb28056591bbabe25fc41ff0ff0db8596b5140d8b5b69fad5de6b.jpg)  
FiGuRE 15.3 A double link between focus areas. The double link indicates that the work done in the second focus area, spell checking, needs the context of the main focus area and that the user will switch back and forth between the two. Designing the user interface for this is a challenge because the user needs to switch between focus areas without losing her context in either.

This is a partial reverse User Environment model of PowerPoint, showing the primary parts of the formalism and what they represent in a real product. (See “User Environment Formalism" for a complete definition of the formalism.) Each box or focus area represents a coherent place to do work. The links between places show how the system supports the flow of activities but doesn't prescribe any particular order of work. The double-linked focus areas in Figure 15.3 show how the spell checker is related to the slide view; it says nothing about when the spell checker is run.

## USER ENVIRONMENT FORMALISM

## Focus area

A focus area collects functions and work objects into a coherent place in the system to support a particular type of work. A function should be necessary to do the work, not to manipulate the UI:

—Supports performing a coherent part of the work

—Named with a simple active phrase

—Lists functions that are needed to do the work

—Lists the work objects that the user needs to perform the work

—Numbered for unambiguous references to the focus area

## Purpose

Short description of what the focus area does in supporting the work

## Functions

Functions are described on the UED with a short phrase. They are written up online with a description of their behavior and justification.

• Functions invoked by the user to do work

o Functions that are automatically invoked by the system as necessary. The user knows these functions exist, but does not invoke them explicitly.

(name) Function clusters that appear in multiple focus areas. This is shorthand for listing all the functions in the cluster. The function cluster name appears between parentheses and is separately defined once to apply to all focus areas.

## Links

Links and double links to other focus areas:

V Functions that support links between focus areas. An arrow between focus areas represents the link. The function name may not be the same as the destination focus area name, in which case the name or number of the destination focus area should be given in parentheses.

» Functions that support double links between focus areas. A double line between focus areas represents the double link.

## Work objects

The things the user sees and manipulates in the focus area

## Constraints

Implementation constraints on the focus area: speed, reliability, availability, form factor (for hardware), etc.

## Issues

Open design issues associated with this focus area, UI ideas, implementation concerns, and quality requirements

## Hidden focus areas

Conceptual units of work done by the system that the user knows and cares about, but doesn't have to interact with. Often they automate work that used to be done by a person. Represented as boxes formed of dotted lines, connected to other focus areas with dotted lines.

## External focus areas

Conceptual units of work delivered by other teams. External focus areas show how your system works with others to provide coherent support to the customer.

## THE REVERSE USER

## ENVIRONMENT DESIGN

There are two ways to take advantage of the User Environment Design. One is while designing a new system: seeing the structure ensures that the system stays simple and close to the user's needs and helps a team plan how to deliver. We'll show how to do that below. The other is to do what we did with PowerPoint—build a reverse User Environment Design to represent a product that already exists.

Building a reverse User Environment Design has a number of uses: to analyze a competitive product, to reveal the structure of mul-

tiple systems that need to be integrated, or to represent an existing system version so it can be extended in a new version. Building a reverse User Environment model of an existing system reveals its underlying work model. It reveals what users can think about and do together in the system, and assump-

A reverse UED shows your implicit existing system work model

tions built into the system about how users work. In the PowerPoint example above, PowerPoint supports changes to notes and changes to the slide content in separate focus areas. This implies that creating notes is an unrelated activity to creating slide content. It doesn't really matter whether the system's designers intended that consciously; that's what's built into the system.

Building a reverse User Environment model can be the first step in designing the next version of an existing system. It's easy for systems to get more unstructured over time—what started out as a reasonable and elegant design turns into a rat's nest of features and connections with no clear structure. Before adding new function, build a reverse User Environment model to see structural issues in the existing system. Modify the design to capture decisions about what to fix. Then you can make storyboards to capture new work practice for the next version to support, and you can use the process we describe below to roll them into the User Environment Design. In this way, you can add function without losing the system's overall design coherence.

When one developer was introduced to the User Environment Design, he started laughing hysterically, then grabbed a piece of paper and started sketching boxes and arrows on it. "I just figured out why users hate our system," he said. "This is what it looks like." He showed us the diagram he had drawn:

![](images/f0da751187d34d680beb035f71f8cbf3abf76df7d86789b984df710d447f782d.jpg)

"See? They have to go all the way back up to this top box and then down again to do anything.'

Using the reverse User Environment Design to see the structure of competitive products can make it clear to a team what the grounds for

competition are. For example, most presentation packages have essentially the same structure at the User Environment level. The three focus areas of outliner, slide sorter, and slide editor are very common. The grounds for competition in presentation packages is at the level of detailed function and UI;

the first product to shift the ground through a fundamental improvement in structure or UI paradigm will gain a substantial competitive advantage. Conversely, QuickMail Pro's market message (from their marketing literature) is that it offers a base structure different from that of other mail products: "The 'All-in-One’Message window lets you simultaneously view your incoming messages, create and send new messages, and file or sort existing messages." Instead of providing separate focus areas for the in-box, sent messages, and filed messages, it's got one focus area for all three. This will only work if the work practice of users naturally mixes these different activities; otherwise it will be confusing.

The reverse User Environment Design is a good way to step back from a system and get insight into it. Surprising numbers of systems have

the hierarchical structure that the engineer recognized in the story above. But the reverse User Environment Design may also reveal the values and assumptions about the work practice built into the existing products. When these are explicit, the team can compare them to the work models representing real customers and decide whether the assumptions built into the

Discussion during a reverse UED reveals designers' values and assumptions

current systems work for the market or organization. For example, one team developing a collaborative work tool that allowed anyone to drop in on any conversation realized they were promoting a value of open communication to an extent that might stifle the use of their system.

The reverse User Environment Design gives a team a way to see what the users experience as they move through a system. It's a valuable tool in its own right. But the User Environment Design is also central to designing new systems.

## BUILDING THE USER ENVIRONMENT FROM STORYBOARDS

In the design of a new system, storyboarding drives the design of the

User Environment. We discussed in the last chapter how design alternates between sequential thinking and structural thinking. Storyboards are sequential and run a single thread; the User Environment Design is structural and reveals how all the threads fit together coherently. Storyboards give a lot of

A good structure suggests and supports unforeseen ways of working

information about a part of the system in the context of a specific use—how that part of the system supports one work task. The User Environment Design lets a team build the single coherent structure that supports multiple different tasks performed by different roles. It's a framework, a structure for doing work that is not constrained to the particular storyboards used to build it. Users will invent new ways to do their work based on the structure in the User Environment Design, if it's designed well

Separating storyboards from the User Environment Design (and from subsequent user interface design) helps a team separate different kinds of design thought. Storyboards support following a single story of use: "I'm a user sorting my mail. How do I approach it? What do I do?" This is one approach to designing a system. It ensures that the system hangs together from the point of moving through a task, but it tends to hide the relationship to any other tasks the user might do. The User En-

vironment Design supports structural thinking: "W'hat's really going on in this place? Is it supporting a single, coherent activity? Does it provide everything the user needs to do that activity?" With two diagrams, each focused on supporting one kind of thinking well, the conversations can be separated for the team, making them clearer and easier to have.

The User Environment Design is built from storyboards one at a time. Each storyboard contains implications for place, functions, and links in the User Environment Design. After the implications of each storyboard have been incorporated, the team steps back and looks over the whole User Environment Design with an eye to maintaining coherence. They identify focus areas that overlap in purpose and merge them, clean out focus areas that have accumulated extraneous functions, and reorganize the structure so that every focus area has a clear purpose and appropriate links to the rest of the system. (Constantine [1995b] describes building systems from a “use context model," a similar process.)

A team pulls structural implications out of a storyboard by walking through it cell by cell. Each cell may suggest a new focus area, function, or link in the emerging User Environment Design. Storyboards are pictorial and help a team recall the context and the implications of each cell for the design better than a scenario or other textual description. The team discusses these implications and revises or extends the User Environment Design to capture their decisions.

The sketches that are part of storyboards give designers a way to think in the language most natural to them, while still staying out of the low-level details for as long as possible. The User Environment formalism is a direct representation of the issues for structuring the user's experience of the system. But we've found that teams coming up to speed on the User Environment formalism don't find this new representation a natural form for thinking. They do better thinking and designing in UI

Moving between storyboards and the UED helps designers see structure in the UI

sketches, capturing them in the storyboard, and then pulling out the implications for the User Environment. The more they go back and forth between User Environment Design and user interface, the more they start to see the design implications from the User Environment diagram directly, and the more it will work for them not only as a seeing and checking tool, but as a design tool.

Here's how the process works in practice. The storyboard in Figure 15.4 shows the first steps of a user getting help in a new work redesign. The vision implies a mix of hardware and software to implement: the phones are altered to have a “help" button, and the phone system is tied into the computer system so that the call is associated with the office and user where the phone is located. When the call is routed, the first-line helper's phone rings, and at the same time this information is displayed on her screen.

Because the system is a mix of hardware and software, some focus areas in this User Environment represent physical hardware places as well as software screens. In this way the User Environment diagram can be extended to represent the total system delivered to the user: hardware, software, documentation, and other systems. (It won't, of course, represent other aspects of the corporate response such as marketing or services.) The phone acts as a place to do work in an office: the work it

The UED can   
represent hardware and software that the user interacts with

supports is communicating with others. The help button adds a function to the place: get quick help on system problems. So the implication of the first cell of the storyboard is a new function on an existing hardware focus area in the user's office (Figure 15.5).

![](images/5edce50593de11ed130f4520cf2bbc7e2931ae1c238a2e5710c77d6570765212.jpg)  
FIGuRE 15.4 Storyboard for getting help from system management.

The next cell shows how the system acts when the help button is pushed. It's necessary for working out what the system will do, but it

The UED shows only what users care about or interact with

isn't part of either the user's experience or the firstline helper's experience; it's entirely behind the scenes. In the next cell, the result of these behindthe-scenes actions is to display information on the first-line helper's screen and ring the telephone. So these actions flesh out the definition of the “help" function; they don't lead to a new focus area (Figure 15.6).

![](images/0d6cece98f54e07a360d7779e135c6c6c104c266f08b50cd9676aebf2e0fdf0a.jpg)  
FIGURE 15.5 A focus area representing new functions on the user's phone.

![](images/8be26b1bcfd7581a27cdc9f824813456ae611d03077deffd9b5f212d2299fdec.jpg)  
FIGuRE 15.6 Function added to an existing focus area.

When the screen comes up on the helper's workstation, it creates a new focus area showing the information necessary to work on the user's problem. The information about the user, his system, and any history is displayed immediately, without any explicit request on the part of the helper. This is represented as an automatic function. We choose a name for the focus area that is terse and describes the primary work it supports: in this case, "Work on user's request" captures the essence of what the place is for (Figure 15.7).

![](images/361e053356fc5720a3f0a115792cc0f950dfd8258c64da1e790cf92261f2ce92.jpg)  
FiGuRE 15.7 Two focus areas connected by a hidden link. Each focus area collects the functions out of all storyboards needed to support the work of that place. They begin to act as a system specification, organized into clusters that support a coherent work activity.

The link between the phone and the new focus area is not an explicit link; neither the user nor the helper move between the phone and the "Work on user's request" focus area. The communication between the two is in the behind-the-scenes work. We show this on the User Environment as a dashed line, showing how the system supports communication between the focus areas.

The storyboard defines additional functions needed by the helper in this place: the ability to turn on and off time charges, assign ownership of problems, and record solutions. We write these functions right into the place. And we add the objects the user works on in this place to the focus area also—the problem report and the user information. Later, when it comes time to build the object model, the functions will define the behavior these

Objects in a focus area reveal the things the user works on

objects must support by specifying what to write into the use cases that drive object modeling.

The next storyboard step has the helper looking at detailed system history. At this point, she's not thinking about the overall problem and system anymore; she's thinking about what has happened on the system that might tie into current behavior, either to support or suggest hypotheses. This is a different kind of work from the initial, direct discussion with the user about their problem. The system support for it is quite different—this part of the system is organized around browsing, free-form searching, and locating pieces of history by association. All this implies a new focus area, “See system's history," which is linked to "Work on user's request." Links are like other functions in that the user has to take an explicit action to follow the link; they're different in that the effect they have is to move the user to a new focus area. We find it useful to collect the links together in the User Environment Design so people can see the connections all together.

This decision about when to create a new focus area is critical to the User Environment Design. Focus areas support one part of the

work and are organized to support it well. Whenever the user is doing a new kind of work, worrying about a different set of concerns, or engaged in a different style of thought, it implies a new focus area. This generally means that the user should work in any focus area for some amount of time, just as

people expect to spend time in a room. It's hard for people to shift their attention from one kind of work to another frequently—the system should not force such a shift unless the work demands it.

When rolling storyboards into the User Environment Design, it's the work the storyboard represents that defines the focus areas in the User Environment. The designers of the storyboard were thinking in the UI and may have created subwindows or dialog boxes, but if they don't support a different kind of work, the system doesn't need new focus areas. Conversely, if the storyboard mixes unrelated work in one interface, it implies several focus areas in the User Environment Design. This is the time to clean that up.

The process of generating a User Environment Design from a storyboard continues in this manner, using the discussion of each cell in the storyboard to identify and capture new focus areas and extend existing focus areas (Figure 15.8). But the User Environment is the structure that supports all stories.

After doing the first storyboard, roll in additional storyboards in the same way.

The first cell of the storyboard in Figure 15.9 identifies a place in the system we haven't seen before—a place for seeing all the work assigned to the user. We add it to the User Environment Design. Then the next step defines a place for seeing an existing problem. But when we look at the User Environment Design we already have, we see that "Work on user's request" already allows us to see and work on a problem. Should this cell reuse that focus area or create a new one? This is a question about the appropriate system structure for the work

The new storyboard suggests a new way of thinking about the system structure. The first storyboard created one place from which to manage all the work of dealing with a problem. That place acted like a control panel or command center, providing access to all the different tools that might help resolve the problem:

2. Work on user's request See, work on, and track user's problem

5. Diagnosis tool Access ailing system with special diagnosis tool

The new storyboard suggests a different approach. Instead of a single command center, the new storyboard breaks out the passive work of seeing the description of the problem and any work done on it to date and documenting any new actions. By breaking the act of working on the problem into a separate cell with a separate UI sketch, the storyboard suggests that access to tools be part of a second focus area:

2. See trouble ticket See description of problem and history of work done to date

3. Act on ailing system Access tools to work on ailing system

5. Diagnosis tool Access ailing system with special diagnosis tool

![](images/5537ebe88b49b9db49537880142079f4807e6f6b6220ad4d428fa17d8e05bce6.jpg)

![](images/4c0255766a643a2ebb113b2ba8ac91fced2e8cc981f1212dd41c291eda3189f0.jpg)  
FiGuRE 15.9 A second storyboard, in which the system manager starts from a list of assigned tasks instead of starting by answering the phone.

These are different options for structuring the system. Up to this point, neither option has been given careful thought. The designers did what made sense for each storyboard without careful consideration of the implications for the system. Now that the two storyboards are coming together in the User Environment Design, the team can have the conversation about which structure would be best for the work as they have observed it. Should a trouble ticket be like a form, capturing the whole history of the work that has been done on this problem? That would be a close duplication of a paper ticket, an essentially passive holder of information. Or should a trouble ticket be an active working place bringing together the knowledge and context of the problem with the tools needed to work on it? The User Environment Design helps the team have this conversation with the aid of sketches like Figure 15.9. By removing UI details from the conversation, the User Environment diagram keeps the conversation focused on structure.

In the actual case, the design team decided on the first of the two options and prototyped it with the helpers. The helpers liked having a single command center for dealing with problems but went further: they wanted the interaction with their tools to happen in the same place. And they didn't need to see all the details of the user in that place. The User Environment Design implied by these changes keeps a place to work on the user's

Different storyboards suggest alternate structures to reconcile in the UED

request, but it integrates the tool results into that place through a linked focus area. And the detailed information about the user is moved into a separate focus area, accessible, but out of the way:

<table><tr><td>7. See user details See detailed information about this user</td><td>2. Work on user&#x27;s request See, work on, and track user&#x27;s problem</td><td>6. See tool result See the results of actions using the different tools in the context</td></tr></table>

The concepts provided by the User Environment diagram make this discussion easier to have. They focus on the critical question for this level of design: what are the places the system will create, and what work will they support? The different diagrams above support a discussion about what structure fits the user's work best, disregarding UI considerations.

Similarly, these discussions precede any object modeling for the system implementation. If objects were derived directly from the storyboards, there would be no opportunity for this level of structural thinking. Each of the different options above suggests different technical challenges, a different set of use cases, and a different object model. In particular, the third option suggests a use case describing how invoking a diagnostic tool causes that tool to run on the appropriate system and show its results right in the “Work on user's request" place.

Different UEDs imply different object models

Neither of the other two options suggest that use case. By designing the structure of the system work model first, the User Environment Design helps stabilize the design before object modeling starts and limits the amount of rework needed afterwards.

## DEVELOPING SPECIFICATIONS

When you have to work within a software process that expects a software specification, the User Environment Design can take you much of the way. The User Environment Design defines how the new system will behave and organizes its function in a way that makes sense for the user. Based on this, you can drive the different parts of the specification. A typical specification might have the following parts:

Overview: The first part would give an overview of the whole system, its goals, and its basic structure. This is illustrated with a high-level User Environment model—titles, purposes, and links only, as in Figure 14.5. This section introduces the reader to the system and orients them to the parts of the system, showing how the different parts support users' roles and tasks.

Supporting data: This section summarizes the customer data on which the system design is based. It shows key sections of the affinity and consolidated models, reviews the roles that the system primarily supports, names the primary influences that drove the design direction, and summarizes the structure of consolidated sequences for key tasks. Particularly when customer-centered design is new to an organization, it's important to emphasize how a design is built on and responds to concrete customer data.

Functional requirements: This is the basic definition of what the system does. It's organized by focus area. Each section introduces the focus area and describes the work done there. For each function, it names the function and provides a full description of the function's behavior. In this way, it avoids presenting long lists of functions with no organized intent instead, it's clear how the functions toge.her support particular activities. Objects manipulated in the focus area are named, and constraints and issues are listed. Where the specification includes user interface designs, they are described with the focus area definition

Nonfunctional requirements: Additional requirements on the system-performance. reliability, maintainability, evolvability, platforms supported, and so on-are listed in their own section. These are collected from the affinity and extended while building the User Environment Design but aren't associated with any particular focus area. They are kept on the side for inclusion in the specification later.

Objects: The objects manipulated in the different focus areas are listed with the focus areas but described once, here. The meaning and usage of the objects across all focus areas are described. This will act as a starting point for later object modeling. Use cases will describe the detailed behavior of the system, and out of that, the behavior of each object can be defined, and additional implementation objects identified.

External interfaces: External interfaces to the system are described. We'll show in the next chapter how links between focus areas can define interfaces between one system and another. In this part of the specification, these interfaces are collected and described.

It's easy to integrate detailed requirements tracing into this structure when your organization requires it. In each function definition, list the storyboard cells that used that function. Document each storyboard and record the consolidated sequence that you used to define it. List any additional data you used—sections of the affinity, role definitions, or other pieces of consolidated models. Document each consolidated model online, and link it to the individual models from which it was built. Do this, and you'll be able to take any function and walk the steps backwards to the actual customer data that suggested the design of that function.

## DEFINING A SYSTEM WITH THE USER ENVIRONMENT DESIGN

The User Environment Design keeps the user's work coherent by holding the whole definition of a focus area in one place. If you have no physical representation, it's too hard to look across a whole system and decide if the parts of it are coherent and where a new function should go. But when the system is concrete in a diagram, it's not hard to scan the purpose and existing function to find the right place for a new extension. When a focus area gets too complex, it's straightforward to review it and related focus areas. What roles does the focus area support? What tasks? For each role, is the focus area reasonable? What's really needed? Using questions like these, designers can rebalance the focus areas and clean up the design.

Within each focus area, the list of functions, links, and constraints summarizes what can happen in that place. As a list, it supports checking the completeness of the focus area—it's easy to scan and check against the issues raised by models and storyboards. Keeping the UI sketches from the different storyboard cells that contributed to a focus area gives additional context: they show what the designers were thinking about when they developed the place. Because they are sketches, they are more concrete, helping designers envision what a system based on this User Environment Design might look like. And

## The UED works against proliferation of dialog boxes

![](images/24aba0d4dbc6e2ff94ed2987b51e11899fddde0fb1bcfcdc8b6344947ea0d01d.jpg)  
FiGuRE 1 5.10 When a focus area leads to one other focus area, which leads to one other after that, you have a "leggy" User Environment structure. The user will have to go through multiple layers of windows to accomplish a function. This is the structure for defining the bullets in a bulleted list in Microsoft Word. How many different ways are there to choose a bullet? And how many different focus areas do you have to go through before you can choose one? In this case, the focus areas are created by dialog boxes; each dialog box creates its own concern by offering a different interface and different function that the user has to parse and understand. Not every dialog box would be represented as a focus area. Microsoft Word's “Zoom” dialog box is simpler and would be considered part of its parent focus area.

they give UI designers a starting point for designing the presentation of the focus area.

Thinking in terms of focus areas and links tends to keep the basic work of the focus area in the focus area, rather than spreading it over

several. Thinking in terms of today's user interfaces allows—or encourages——spreading the function across windows, panes, dialog boxes, tabbed dialogs, and other gewgaws. Look at the way MS Word uses three layers of dialog box to specify bullets (Figure 15.10). Thinking in the UI raises worries about con-

straints of screen real estate and problems of specifying every detail of a function; it's easy to punt and decide to put the function in a dialog box. Thinking in the User Environment Design takes away that excuse—if the function is part of the work of a focus area, it goes into the focus area.

Later, when it's time for the UI designer to create a user interface, the User Environment Design will have collected all the different functions from all storyboards and organized them into coherent areas, each focused on one kind of work. It's up to the UI designer to figure out creative ways of making the function available in one coherent place in the interface. This gives the UI designer the most flexibility to be creative—deciding to split a focus area because it will be too hard to design the UI prejudges what the UI design will be able to do.

The sketches from the storyboards offer suggestions for the UI design and show the concepts the storyboard designers intended to reveal. But the UI designer has to decide, for all the storyboards collected into this place, and for all the roles and tasks the place might support, what is the UI appearance that will support the work best. In the above example, the “Work on user's request" focus area has to let the first-line helper see what

The UI designer makes function accessible for all users and tasks

work has been done on a problem and also support the system manager doing the work on the user's system. The User Environment Design specified that they could both take advantage of the one focus area; now the UI design has to support both roles. The first-line helper has an irate user on the phone; he needs a clear and direct interface. But he does want to see the whole history of the problem. The system manager wants powerful access to all the tools, but if that access is provided, she can benefit from the clear and direct interface the first-line helper needs. The UI designer has to consider both roles when designing the presentation and access mechanisms.

This is the ongoing process of extending a design: create a storyboard to work out the implications of a new component to the user's work practice, then roll it into the User Environment Design to see how the system structure can support the work practice you've designed. Storyboards keep the work coherent; the User Environment Design keeps the system coherent. Additional storyboards build up the User Environment Design into a structure that responds to all the multiple tasks and roles the system must support. The resulting User Environment Design shows all the parts together, how they relate, and how they overlap.

## DEVELOPING THE OBJECT MODEL

The next task facing the team after developing the User Environment Design (and checking it with users, which we discuss in the next part) is to start the design of the implementation. This is what use cases and object modeling are all about. We will not treat object modeling in depth, but the design work done in storyboards and User Environment Design gives the team the basis they need to design the implementation quickly.

The usual method is to start with use cases and define classes and class hierarchies from them. Going from use case to object model is another example of switching between sequential and structural thinking; the use cases are a story of use, the object model is structural, and (if used) object interaction diagrams are a story again. But, as practiced in the industry, use cases may be very high level, showing a whole task in the work, or low level, showing the accomplishing of a smaller function. And it's always an issue to decide what ought to be specified by the use case anyway.

When building on a Contextual Design project, we incorporate use cases at two points. First, storyboards act like high-level use cases. They show how real users interact with the system to get tasks done. At this level, the storyboard is well grounded in a consolidated sequence and the vision, so there are clear criteria for what should be included. But the storyboard format is more appropriate to this high level of design. Their pictorial nature makes it easy to scan and see the emerging design. And, while use cases include preconditions, postconditions, and exceptions, we've not found it necessary to specify these at this high level.

The User Environment Design provides a high-level structural thinking step that responds to the storyboards. Change the structure or function at this level, and the object model for the implementation will change; merge two focus areas and expand the function of a work object in the User Environment Design, and the corresponding implementation object will take on new responsibilities

Later, object modeling captures these implications by switching back to sequence-based thinking in low-level use cases. At this level, each use case tells the story of how one function or closely related group of functions operates. The use case is based on storyboards and User Environment Design: the storyboard defines what the user will do, while the User Environment Design defines the function. The use case works out precisely what happens when the user operates these functions, how the system responds, and how the system internals make the designed response possible. They reveal flaws in what went before and drive the next step. Use cases bridge the gap from design of the system work model to design of the implementation.

Similarly, the design team derives events and triggers driving the implementation from the User Environment Design. Whether initiated by the user invoking a function or initiated by the system as indicated by automatic functions, the User Environment Design defines the events that the implementation needs to handle.

Building the User Environment Design as an intermediate step between storyboards and use cases helps ensure that the structure built into the use cases holds together for the user. Until the User Environment structure is stable, there isn't a design to build use cases on—changes at the User Environment level will change what happens in the use cases. Without an explicit representation such as this, the only way to work out structural issues is in the implementation and the UI. The more we can reveal, identify, address, and test these issues with users before starting implementation design, the faster implementation design and coding will go. □

## USER ENVIRONMENT DESIGN

## WALKTHROUGHS

The walkthrough is the final step of building a User Environment Design, and it should never be skipped. It's always done before going on to design a UI or test the design with users. The User Environment Design walkthrough uses principles of good system structure to check the design. Even a careful team will, as they roll more and more storyboards into the design, start to destructure it. A focus area that started out clean will accumulate function until the original purpose gets blurred. Perhaps any individual function could be justified, but taken together they suggest a different work focus that should be separated out. Two focus areas that started clearly distinct will, as function is added to each, start to overlap to the point that the distinction is no longer clear. The team needs the walkthrough as a chance to withdraw from the design, take stock of it, and reorganize what has started to get messy.

You'll see another level of structure when you walk through your design. The design itself suggests new possibilities when you pause to inquire into it. A set of focus areas taken together may imply support for a whole task or role; three focus areas might be consolidated into one addressing the fundamental task more directly; or functions in several focus areas suggest an activity that could be supported directly in its own focus area. It's this step of rationalizing the design against the work that will lead to a solid, flexible base structure that supports many different uses.

Walking the User Environment Design also gets the team into position for the next phase of design. It ensures that the whole team is clear on what they intend by the design and how they think it will work. It identifies test cases—conditions or design elements that become a focus to test with users in prototypes. In this way it becomes the first step toward iterating the design with users.

![](images/9127dbf2fad50c00fe5c02914f5264209c92bab4a5842c8a4b0750f5a496d5ff.jpg)  
FiGuRE 15.11 When a focus area contains no function, only links to other places, you've got a hallway. Here in Peapod are three hallways in succession (1, 16, and 17) before the user can get to doing anything real. System designers frequently create places that have no purpose except to organize access to other places. They are like hallways in a house, where no actual living is done but doors open onto other rooms. Hallways are necessary in houses because of the physical constraints in laying out a house, but in a software system every place can support real work. This kind of structure is often an indication that the designer is carrying over old ways of thinking from non-GUI systems.

## PROBING USER ENVIRONMENT DESIGN STRUCTURE

The questions to ask when checking a User Environment Design are similar to those that drove building it:

Are focus areas coherent? Does each focus area support one activity within the overall task? Is that represented by the title and purpose statement? Be suspicious of any focus area that has no purpose. It's often because the team isn't clear on what the purpose is.

Do focus areas support real work? Look for focus areas that are really glorified dialog boxes—they've turned a simple command into a whole subtask (see Figure 15.10). Look for focus areas that group related functions, but that don't support something you might work on. Look for focus areas that don't support a coherent work task, but instead only reveal the data associated with an object in the system.

Are functions correct? Look for functions that are not in direct support of the focus area's purpose. Do they imply a separate activity that should be separated into another focus area?

Are focus areas distinct? Collect the focus areas that support the same part of the work—the same activity, task, or role—and compare them. Are they clearly distinct? Do they, taken together, provide coherent support for this part of the work? Can they be recombined to give a cleaner set of distinctions for doing the work?

Do links make sense? Do they support the work task as you know it from the consolidated and redesigned models? Certain patterns of links and focus areas always indicate trouble (see Figures 15.10 through 15.12). Do any of these patterns appear, and do they indicate problems in the design? (Incidentally, notice the simplified form of focus area used in Figure 15.10, with only title and purpose. This is a useful way to highlight structural issues.)

Is the work supported? Finally, use the consolidated models to refresh your memory, and look at the User Environment Design from the point of view of the different roles and tasks. Does the design work for each different kind of user? Does it account for the issues they care about? Run actual sequences through the model, asking how this user would have done this task given the new system. See if you can make it break down.

Using a walkthrough this way pulls the User Environment Design back together into a structure that makes the user's work coherent. Like a groundskeeper rethinking path layouts, the walkthrough gives you a chance to step back from your design. Check it for fit against the user, for missing parts, and for internal balance. Clean up the structure, and then you can either test it with users or extend it with more storyboards. Or, better yet, do both in parallel—the sooner you get feedback from real users on their design, the better off you are.

<table><tr><td>1. Main menu See what I can do 1111ks &gt; Shop 15. Tips for moms and dads Read atces from M Working Mothes maq/ne , New on Peapod 16. Peapod Pantry Jomn a community of stoppers 1nks ,See shopping tips . sce teape arsle K 17. Recipe aisle See difterent kinds of teaipes avatlable 1 Lilik; · Reape of the month , tost teape, Found reapes Wute the Peapod . Pantry</td></tr></table>

eachs occs orea. hao o e o oe uoh e ek e e  e weo Usnearn  ns ond s S s sn neenn pan thit e s  t  is a tnr  s he sos sy urtr ouy o uy osi o u y o sns tee wie e ssae we ei is ee wi gier ros ie e e e me e  oet oe otyt ht e  ee re oeoe aoe soe ee vy, proh at ssoons uots sos puts s uohe Jrhis xe Ssze sre sas ss ses exe seaa

arnla s hc has ys) niot ro pa at soe ss o  o r roohte thed  ho es e h e  ke e s es ce Turess u w ee s es s  sos oe nt eins aik n suocy or a u) uoy ers ur urons sks s-ue e oue stuee so ee ie uoped e e ucs tuuel EUuidns bpornd ein, Sns ro n Dvoings FIle sre   s  e  rser