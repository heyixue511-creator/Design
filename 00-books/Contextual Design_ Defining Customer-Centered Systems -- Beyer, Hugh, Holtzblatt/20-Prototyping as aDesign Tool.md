# Prototyping as a Design Tool

17

Te call this a customer-centered process, but it's been quite a few chapters since talking to customers was the main activity (not counting any customers on the design team). The activities covered in the last few parts have focused on the customer—understanding how they work as individuals and the common structure of their work, visioning new ways for them to work, and designing those ways into a software system. These activities keep the customer's work practice coherent and use customer data as the final arbiter. And the consolidated models and vision suggest holes in the team's knowledge of the customer, which they fill through additional interviews. But it's now time to get direct customer feedback again.

One of the difficulties with explaining any process is that each part of the process must be described in turn, and the explanation itself takes up time. The description unrolls the process and lays it out, making it possible to see and examine each part, but also making the process appear more sequential than it is. In fact, the period from the beginning of consolidation to the first pro-

The goal: continuous iteration and extension

totype interview should be no more than a month, even for complex systems, and the team gathers additional data to fill gaps in their understanding and inform the vision during this time. For smaller projects, this period may be as short as a week or two. The point we have now reached in the process is the norm for a design team: with a base understanding of their customers and a target vision for their design, they extend and iterate their design with customer feedback. Iterating with prototypes is a design tool ensuring that the team builds the right system, that the structure fits the user's work, that the

The customer is the final arbiter of the design

detailed structure internal to a focus area works, and that the user interface is usable and reveals the structure clearly. Teams that get bogged down in design are usually those that have lost touch with their customers—that aren't going back out to interview or test prototypes on a regular basis.

The most basic attribute of a customer-centered process is that the customers are the final arbiters of what works and what doesn't. When

you create a design, captured in a User Environment diagram, that design is really a claim about what will work for the user. The claim is that this particular system simplifies the user's work, overcomes pain, or otherwise improves their work practice. So, how do

we test this claim? How do we find out where the design falls short and how to improve it? How do we communicate the design to users in a form that they can respond to—in a form that helps people see the consequences of different design decisions and react to them clearly?

## THE DIFFICULTY OF COMMUNICATING A DESIGN

Most of the approaches commonly used to communicate a new design downplay the difficulty of communicating a design. Think

Demos and specifications can't evoke work practice about it—it's a conceptual nightmare. Consider presenting a demo of the proposed new system to potential customers in a conference room: they must view the product's user interfaċe, understand from the interface and the verbal description what the

product does and how it is structured, apply that implicit structure to their own work practice (which is also unarticulated, as we established in Chapter 2), envision how their work practice will be restructured in the presence of the new system, imagine themselves living in this new way, and decide whether they like it. Then, if they don't, they have to imagine some better way to work, transform it into implications for the design, and express those implications clearly to the designers. The task is overwhelming. It's no wonder most people complain about an icon that confuses them, comment on the color, and ask about one or two key features they care about.

Requirements specifications fare no better. Most are text; most break the system down into categories that relate to the system, not the

user (all reliability requirements together, for example). Even when the first level of organization is by UI component, their textual and list-based nature tends to present features in isolation. It's hard even for designers to see how a feature relates to other parts of the design; internal users reading the requirements for sign-off find it even harder. Requirements

specifications are less approachable than a demo and make it no easier to imagine the impact that the proposed system will have on users' work. They may have their place in specifying exactly what's in the system, but they aren't a good way to communicate a design.

Talking to the customers with models has a similar set of drawbacks. Process models or object models introduce a new language,

which must be learned and understood by the users if they are to participate in the discussion at all. The models represent either facts about their work or the new system. But their work is unarticulated, and the models represent it in a strange and unfamiliar language that offers no touchstones to their experience.

Models introduce a new language for customers to translate

In Contextual Design, we don't even try to talk to customers with our work models, unless we're building systems for an internal business partner, and they have an interest in representing their own work practice explicitly. Then the work models become a tool for the whole department to think about how they work and maintain an ongoing conversation about how they might improve it. When customers think models are a tool for them to manage their business, they can learn to use them in the way that designers use them; otherwise it's too hard for them to see how they map to reality.

Other forms of communication such as use cases and scenarios attempt to communicate more of the context of use. These methods tell stories of how people will work in the new system, so they communicate better than a model or specification. However, each scenario can only tell one story out of the many the system must support. And they all suffer from the same basic drawback: most customers have only an unarticulated knowledge of their own work and cannot check a proposed design against their own experience unaided. They can react to such a story at the level of “I hate that" or “I love that," so scenarios can help test the marketing pitch. They'll help answer the question, "What matters to the customer?" but not "How should the system be structured for them?" To provide that level of feedback, customers need not just an artifact but an event, a process that will allow them to live out their own work in the new system and articulate the issues they identify.' Without such a process, it doesn't matter how many signatures are on the requirements document—there's no guarantee that the specified system will solve any real problems.

## INCLUDING CUSTOMERS IN THE DESIGN PROCESS

The problem for this point in the design process is to get feedback from customers on the detailed structure of the proposed system——on

whether the system work model fits. Getting good feedback from customers is made more complicated because we don't just want “yes" or “no" answers. We want to explore possibilities and create new alternatives. In fact, we want to co-design the system with the users. In Part 1, the question was how to make the customers the best masters of apprentices possible; now the question is how to make them the best co-designers. We'll draw heavily on the same principles that drove Contextual Inquiry for the answer.

The team's design needs testing with customers who haven't been members of the team. The obstacles to making these customers codesigners are real and have to be faced head-on: First, no one articulates their own work practice as an ordinary thing. It would be nice if the users could give three concrete reasons why a design should be changed; usually they can only say that the design just feels wrong. The design process needs to create a way of interacting that helps them articulate the issues. Second, customers have not spent time studying all the users of the proposed system. (Even when customers are on the team, we interview them and follow them around to help them articulate how they work.) What this means is that any customer testing a prototype can only respond to it from their own point of view. Third, customers aren't technologists— they don't know the range of possibilities that technology could support. They may be either unrealistic or excessively cautious as a result. And they don't know what it takes to make a design hang together. And why should they, after all? It's their job to do their job, not design systems. (For a discussion of these issues and a range of techniques for overcoming them, see Wixon and Ramey [1996].)

And yet it's absolutely critical that these customers, immersed and steeped in their own work, be made a powerful partner with the design team, so they have real influence over the design. It's the customers who will have to live with the new system. If it's an internal system, they have a right to say how the work they do will change. If it's a commercial product, it won't be bought if it doesn't meet people's real needs. And unless it works well for customers, both internal and commercial systems will fail. So the challenge for design is to include them in the process to iterate, refine, and extend the initial design concept put together by the team.

The starting point is an initial design concept. Any prototyping process starts from an initial prototype, which designer and user refine.

It's always easier to renovate an existing design than to start from a totally blank slate. But because prototyping is iterative, it's hard to make fundamental changes to the initial concept, so you want to be sure the first cut addresses the right issues. It's also easier to renovate if you're starting with something reasonably close to what you want. Parts 1-5 were about how to get to a good starting point—all the effort that went into understanding the customer's work and needs ensures that vour initial design is addressing the right problems and has a reasonable structure. Now, we need to get the details right.

## USING PAPER PROTOTYPES TO DRIVE DESIGN

In Contextual Design, we borrow the idea of rough mock-ups from Participatory Design by introducing very rough prototypes in paper to start the co-designing with users. The goal of the prototype is not to

## Paper invites conversation about structure

provide a demo; prototypes are a prop in a contextual interview, enabling the user to play out the experience of living with the new system. By acting out their real work in the prototype, customers can make their unarticulated knowledge explicit. Fleshing out the prototype with the customers' own data and work situations gives them the touchstones they need to put them in the experience of doing the work. And their interaction with the designer/interviewer lets them explore different technical possibilities. The designer knows technology and provides options, which the user considers, matches to their experience of the moment, and discusses why one alternative fits and another doesn't. It's another application of Contextual Inquiry—using the prototype in the real work context keeps the discussion grounded, the partnership leads to co-design, together customer and designer interpret work issues, and the prototype gives them focus.

Prototypes act as a language for communicating between user and designer. Instead of introducing a new language, a prototype builds on users' own experience using computers. A prototype enables them to interact with the proposed system as they would with any system and to respond in a language that is immediately relevant to them."I think this should happen when I click here," they say,

unaware that they have just redesigned a focus area on the User Environment Designbut the designer can tell because they can see how the comment relates to structure and can investigate the issue if it challenges the design.

To look at structure, the first prototypes are always paper. Paper is eminently practical and meets the primary need: it makes it possible

to express the structure of the system and makes it hard to overfocus on user interface detail. When a window is drawn by hand, it's pretty clear that icon design, precise layout, and fancy direct manipulation are not the important points. When users interact with paper, they aren't distracted by fancy user interfaces; they have to focus on structure. Even house architects, who aren't constrained by writing code, prefer to communicate their first ideas to clients as sketches rather than finished drawings. (See “Readings and Resources" for a range of approaches to paper prototyping.)

## PROTOTYPING AND USABILITY TESTS

The goals of prototyping in Contextual Design are very different from the goals of a traditional usability test, and the two techniques complement each other. Usability tests typically seek to measure users’ performance on set tasks to ensure they can be done reasonably efficiently. The techniques are different because the goals are different and the kind of information being elicited is different. Usability tests tune a user interface at the tail end of design, to clean up any rough edges or unnecessary difficulty in understanding or interacting with the interface. It's not a goal of traditional usability tests to discover a better system structure or to discover that this isn't an important task at all. In fact, these issues get in the way—usability professionals are constantly frustrated at being asked to fix major structural problems through last-minute Band-Aids. By the tail end of design, it's simply too late to decide that your system addresses the wrong problem. Recognizing this, usability professionals are moving to be involved earlier in the life cycle and are using more contextual techniques in which the user does their own work task. The more they do this, the more they get involved in the design of the whole system, not just the final tailoring.

The very nature of a paper prototype invites change. When the user gets to a window in the prototype and says, “But now I need to

do this," it's easy to add the function right on the window. It's easy to invite users into a discussion of what they need, why they need it, and which of several alternatives would better meet their need. It's easy to move into co-design of the system. The user

Hand-drawn paper prototypes invite change

is discussing his or her own work, in the context of doing it, and manipulating the system interfaces that will help to do it. A running prototype couldn't be changed immediately to track the conversation. Interviewer and user would have to talk about design alternatives with no support, or by sketching them—on paper.

We've discussed the advantages of understanding work for deciding what to build, but there's a whole layer of detailed requirements that users simply can't communicate except when they're working

with an actual design. It's natural to develop requirements in layers, just as an architect works out the overall layout of the house before deciding where the closets go. The vision was the first layer of design, defining the overall corporate response. We worked out the details of the vision in storyboards,

Rough prototypes focus detailed requirements gathering

![](images/7a7e83948b5e6dedbc9c0d00b58565358214efa8c824fb2cb3b7d48c6e4a6352.jpg)  
FIGuRE 17.1 A proposed UI for ordering supplies.

but we needed additional data (the consolidated sequences and issues from the models) to build them. The User Environment Design pulled together the parts of the system into a single diagram to work out their relationships. But now we need an additional level of detailed customer data to work out exactly what will happen in each focus area.

A first level of requirement might be, "The ordering system should make it possible to batch orders from several people." But a complete

Prototypes make it possible to test work practice that doesn't yet exist

specification would give intricate detail: “Orders from several people will be organized in rows, grouped by person or item ordered, with who requested the item, the item description, and price visible on the screen, and movement from order to order will be supported by the TAB key..."(Figure 17.1). Ignoring the difficulty of communicating this much detail precisely, how are the designers to get these details right? How can they determine exactly what information the user needs to see? If it's a new system (the customers currently don't batch orders from different people), they can't use existing work practice as a guide. Customers can't tell them what they will need in a system that they haven't experienced. The only way to get this level of specification right is to work it out in the context of the specific design. Prototyping in paper lets the team complete the detailed design without committing anything to code.

Then, once designer and user are working together on a new system prototype, it becomes possible to take the next step in design.

When a system is entirely new, putting it in place will change the user's world in unpredictable ways. Not until users have worked with the system and understood the possibilities it creates can they start to restructure their world around it. Movies are not filmed theater—but until people had experience

with the new medium, they could not see how to move beyond theater. Word processing is not typing—but the first editor was jokingly called the “Expensive Typewriter" by its creators because they weren't sure they had created anything really new. Not until word processors were part of the workplace could anyone see how profoundly they would change work and redefine the role of professionals and secretaries along the way. Until spreadsheets were in use, no one could tell that they would become an important way to present data and that formatting would matter. As people take advantage of new systems, they change their work practice in ways the designers may not foresee. If designers can find out about this emergent work practice before the design is complete, they can support it directly. Lotus 1-2-3 became successful by recognizing the emergent work practice that VisiCalc did not support. Recognize the emergent work practice yourself, before your competition does, and you can leapfrog a whole generation of products. Interviews with paper prototypes are the first step toward seeing these issues.

The first round of interviews reveals the basic structure of work and needs for the new system. The new system is designed in response

to the current work structure. But working through a prototype of the new system, pretending to do real work, and discussing the interaction of the system with the work reveals issues that would otherwise remain invisible. Together, user and designer can

The trick: using real work pushes co-design

explore how the system will impact the work and how work is likely to change in the future as a result. There's a chance of designing the system to account for these changes.

Co-design over a prototype builds trust with customers

## PROTOTYPING AS A COMMUNICATION TOOL

In Chapters 2 and 5, we discussed the need to build a partnership with the customer organization. especially for IT departments. What's been missing until now has been concrete activities that build day-today communication and trust. What's needed is not just a formal agreement on deliverables but the sense among the customers that the development organization understands their problems and will produce useful software

The continual involvement of users is an important way to achieve this trust. Prototype interviews excite and interest users—they

can see progress, they can talk directly to developers, and they can see how their responses shape the design. It's immediately clear that the design team is listening. This can cause its own problems—one team had to ensure everyone in their customer department was interviewed to handle the interest

and excitement—but surely these are better problems to have than mistrust and contempt. The interest and involvement generated by the sessions leads to easier acceptance and adoption of the system when it comes time to roll it out. And for commercial products, it's a good way to find out if a design works and if it generates excitement among the people who try it. It's also a great sales point for commercial product developers to work out the design with their users—after one set of interviews, one customer had their internal company newsletter do a piece on how well their vendor was listening. Another customer, when asked, said they would pay three times the price marketing thought was possible because they understood the potential impact on work practice.

The prototyping process not only brings the users into the design process, but it changes the design process itself. The customers,

remember, are the final arbiters in a customercentered process. But that's not an achievable goal unless bringing them into the process is fast and easy. We regularly mock up a design alternative in paper on one day and test it with users on the next. We have results and are ready to rethink the design within two days. It's possible to go through multiple iterations, trying out many different ideas, in the course of a week. 'There's no time for people to get overly invested in one design alternative and no reason to argue for any length of time over two alternatives. It's almost always faster to take the alternatives to users and try them out. Most arguments in a design team come about because the team really doesn't have the data to make an informed decision. Paper prototyping reduces the cost of getting data so low that the team can depend on having it and makes getting data so fast that no one has time to get overly invested in a feature. (Moll-Carrillo et al. [1995] and Lundell and Anderson [1995] offer case histories of this kind of rapid iteration.)

## From Structure to 18 User Interface

paper prototype tests the structure captured in a User Environment Design by talking to users through the medium of a user interface. Because the initial intent of the prototype is to test structure, the UI should be a fair representation of the underlying structure. Making the translation from User Environment Design to user interface is a necessary part of the prototyping process.

We'll discuss how to map from User Environment Design to UI in this chapter, but we will not try to cover how to design a good UI. Creating a good UI is its own design problem and is covered extensively in other books. What we care about is that the interface presents the User Environment Design cleanly, so we don't fragment the work in building the UI and we provide a fair test of the structure. The UI should hang together as an interface, conform to any guidelines for the UI platform, and be a fairly straightforward translation of the User Environment Design. The team may choose to put some extra effort into designing the interface, so they can test some of their UI ideas as well. But a clean presentation of the structure is the first priority.

## USING THE USER ENVIRONMENT DESIGN TO DRIVE THE UI

The User Environment Design is the user interface designer's specification. It tells the UI designer how to organize the interface, what functions should be available, and where to put the functions. But it leaves open how the interface should work—the underlying user interface paradigm, the interaction style, and the appearance. When the first prototypes are built, the User Environment Design may also

The UED is the UI designer's specification

leave open low-level design details, such as exact content and order of fields in a list. It's best to work out these details directly with the user in front of a prototype. UI designers use the User Environment Design as a guide and also draw on the work models

to inform their design. The affinity collects issues, including issues with using tools; the physical model shows what's placed where and suggests what should be most accessible and apparent in the UI; and artifact models show the conceptual structure and intents that should be reflected (but not slavishly followed) in the UI. Storyboards not only collect UI ideas for different system components, but give UI designers a sequence of work steps to test their design against.

Like any good specification, the User Environment Design does not determine how to design the user interface. It leaves even the choice of technology open, whether command line, character-cell, windows and mice, or something else. The hardware platform, operating system, and UI technology determine UI style; the User Environment Design defines the structure and function to implement. It's up to the UI designer to make creative use of the technology to get the UI out of the user's way so they can focus on work, not the tool. Then the prototyping interview will test not only the system structure but the first level of the UI, too.

## MAPPING TO A WINDOWING UI

Here's an example of how a User Environment Design might turn into a user interface. The “Select base configuration" focus area in Figure 18.1 specifies that the user should be able to see, sort, and choose from a list of configurations and get details on a configuration in the list. It also says there should be a close link to the “Find configuration" focus area, which allows for creating a new list of configurations that match a specified criteria. This pair of focus areas could be realized on any base platform, but Figure 18.2 shows a windowing implementation, and Table 18.1 shows the appropriate mapping.

Every user interface technology offers a unique set of advantages and drawbacks. One of the challenges of UI design is to overcome the particular drawbacks of a platform. Windowing interfaces offer the possibility of great transparency because all options and changes are visible at once——but some aspects of the interface are cumbersome. The design in Figure 18.2 goes to some effort to make it as easy as possible to select a single configuration by name. The user clicks on the button that brings up a dialog box, types the name, and hits RETURN without even having to wait for the window to draw on the screen, in a good implementation. Nevertheless, the nature of a windows interface is that a window has to come up to present the text entry field, and anytime a windowing UI does this, it will disrupt work. (Some products find creative ways around the problem—MS Word 5 on the Mac would steal part of the horizontal scroll bar for text entry. This bent the UI style rules, but minimized disruption to the work flow.)

![](images/a0873e33f0d0af0bccc49d61c803df5bc1655942c36ba6383e12da8598bd9579.jpg)  
FIGuRE 18.1 Part of the User Environment Design supporting configuration management, first introduced in Chapter 16.

![](images/c649153093a16e842a4eb0c119fb47748d9fd895dac64e842f383807484c8844.jpg)  
FIGuRE 18.2 A windowing implementation of the configuration management User Environment.

![](images/9760c1aa8792b62ea21199c0141f69f43fda15b62436760ca88f2cc4ebbc72ed.jpg)  
TABLE 18.1 Mapping to a windowing UI.

Designing the UI introduces new functions that are specific to manipulating the UI and so don't appear on the User Environment Design. Selecting a configuration and sorting the list are required by the User Environment Design and are handled in the UI by the standard mechanisms of double-clicking to select and (the somewhat less standard) clicking on column heads to specify sort order. But “scroll up," "scroll down," and “select" aren't User Environment functions at all—they are just ways of manipulating the UI and are not fundamental to the work the system supports. They should be designed to stay out of the user's way.

Most focus areas end up being windows in a windowing UI, but that's not the only way to do it. The User Environment Design only

specifies that the function in a focus area be presented as a coherent chunk: that can be done by putting the function in a pane or segmenting a larger window in some other way. Some successful products (Claris Emailer or M.Y.O.B.) make the most important focus areas tabs in a tabbed dialog box and put secondary focus areas in windows accessible from the different tabs (Figure 18.3). Tabs in dialog boxes are problematic because each tab creates its own focus area whether you want it to or not, but when a tab is intended to act like a focus area, the interface can work well.

## MAPPING TO A COMMAND-LINE UI

We presented the mapping to the windowing interface first because it's most direct. But the same User Environment Design can be implemented in other user interface styles. As an example of a very different style, Figure 18.4 shows how a command-line interface might represent the same User Environment Design.

This mapping of a User Environment Design to a command line shows another way to deliver the basic intent of the specification (Table 18.2). Here, the “Select base configuration" focus area is a subsystem. By relisting the configurations automatically after each command that affects the current list, the design ensures that the user always knows what is going on and fills the requirement of the “see current list" automatic function. But it's more cumbersome than the windowing implementation.

![](images/7a7fc09ce614821cb7c0f363e3430ab59430b1fcd475aefa1448b15f404fec81.jpg)

![](images/263920468366394c9e2ccc2c5922a0485fd47fc3d1e0a780d8072c01a4aa892b.jpg)  
FiGuRE 18.3 Claris Emailer and M.Y.O.B., two products that use tabs or tablike buttons to organize access to their primary focus areas.

<table><tr><td>CM&gt; SELECT</td><td>BASE CONFIGURATION</td></tr><tr><td>1。 CONFIG1 8-AUG-96 2。</td><td>JOHN SMITH</td></tr><tr><td>CONFIG2 7-AUG-96</td><td>JANE DOE</td></tr><tr><td>3。 CONFIG3 6-AUG-96</td><td>SAM SPENCE</td></tr><tr><td>SELECT CONFIGURATION&gt;</td><td>SELECT 2</td></tr><tr><td>CONFIGURATION CONFIG2 CM&gt;</td><td>SELECTED</td></tr></table>

FIGuRE 18.4 A command-line implementation of the configuration management User Environment.

<table><tr><td>USER ENVIRONMENT COMPONENT</td><td>COMMAND-LINE EQUIVALENT</td></tr><tr><td>Select base configuration (focus area)</td><td>SELECT BASE CONFIGURATION putS user into a mode that allows searching and specifying a base configuration.</td></tr><tr><td>View recent configurations (automatic function)</td><td>SELECT BASE CONFIGURATION respOnds by listing the 10 most recent configurations immediately. This fulfills the requirements for an automatic function, allowing the user to select from the list</td></tr><tr><td>Enter and choose configuration name (link)</td><td>SELECT BASE CONFIGURATION &lt;NAME&gt; identifies the desired configuration by name. The intent of this function as defined by the User Environment Design is to make it as fast as possible to choose a configuration when the name is known. Command lines excel at this</td></tr><tr><td>Choose configuration (link)</td><td>SELECT &lt;N&gt; and SELECT &lt;NAME&gt; let the user choose a configuration from the current list either by ordinal number in the list or by name.</td></tr><tr><td>Sort by name or date (function)</td><td>SORT BY [REVERSE] {NAME | DATE} allows the user to choose a sort order for the list, sorting in either forward or reverse order, by name or date. The command-line system responds by relisting the current selected</td></tr><tr><td>Find configuration (double link)</td><td>FIND [CONFIGURATIONS] WITH [NAME = &lt;PATTERN&gt;] . . . chooses a set of configurations to view based on criteria</td></tr></table>

TABLE 18.2 Mapping to a command line.

![](images/289016821a16a077187257edf63e119e05c44910f712ae265d822c2a8d26659e.jpg)  
TABLE 18.2 continued

The two forms of the “select base configuration" function—with and without a configuration name—provide an economical way to select a specific configuration quickly or begin a search for the right configuration. This overloading of the command is appropriate to command-line interfaces, and the possibility of such overloading is one reason why command lines can be terse and direct. Windows interfaces have no equivalent—we

saw above how the windowing design had to separate the two functions and pop up a text entry window to do the same thing.

The command line is at a disadvantage in dealing with the list of configurations. You can't point and click in a command line, so how will selection be supported? This design numbers the list and allows choosing both by number (for brevity) and by name (to support recall). These are appropriate options for a command-line user interface style. They don't appear on the User Environment Design because they address issues unique to this UI design. Similarly, the user interface designer will have to decide what to do when the list is too long (over 10 or so). Should the list just scroll? Should there be another layer of function to display the list a screenful at a time? These are questions about working with the constraints of this particular user interface and are decided at this level.

## MAPPING TO UI CONTROLS

When mapping function in the User Environment Design to controls in a windowing UI, there remains the question of how to decide what

kind of control to use. The different options for making a function available in a windowing user interface are not equivalent. Functions can be implemented through a pull-down menu, a button, direct manipulation, or a command key. Which mechanism will work best for a particular function

depends on the nature of the function with respect to the work of the focus area. Who the user is, what role they are playing, and what influences them in the cultural model will all affect what makes an acceptable influence. Doctors and medical technicians both update patient records—but doctors are more pressed for time and will tolerate less complexity from their computer systems. The UI for a system supporting both would have to work for both user populations. It's up to the UI designer to understand the work context and map the function in a style that supports the intent of the focus area and fits with the people who will use it. UI designers have a number of options for presenting a function, none mutually exclusive. Some distinctions between ways of presenting functions can be useful:

In your face: A button, whether on a toolbar or directly on a window, is in your face. It's always present and it always takes up screen real estate (unless you allow the user to redefine the interface by reconfiguring toolbars). They're easy to find because they give a direct visual clue to their existence. In Chapter 15, we discussed core functions, the functions that are central to the work of a focus area. It's often a good idea to implement core functions with mechanisms that put the function in the user's face. Making these functions easy to find and access is worth the drawback of using up screen real estate on them. Also look at the physical model to see what users chose to put in front of them—those things represent the concerns users care about, so functions related to those concerns are good candidates for putting in the user's face.

In your fingers: A command key is the fastest and least distracting way to invoke a function for expert users. Even multiple keys can be struck like one if they're familiar enough. Moving the hand to the mouse, positioning it over the right button, clicking, and returning the hand to the keyboard is always a greater distraction than typing CTRL-B. But a command key is entirely invisible; all but the most common will be used only by power users. When mapping critical functions, frequent functions, or functions that are available across many focus areas, command keys are appropriate. They're also appropriate when the function needs to fit seamlessly into the work flow when users are concentrating on the work in front of them and want to invoke the function without thinking about it. CTRL-B for "Bold" is a great command key—it's consistent across every tool that edits text and it doesn't interrupt the user's thought.

Direct manipulation: Direct manipulation is as invisible as a command key. But direct manipulation functions suggest themselves through the physical metaphor of a windowing user interface. Users think they can drag around icons on the desktop, so it's natural to move files by dragging them between folders. The physical and artifact models will suggest what things are moved around, their structure, and operations on them. Direct manipulation works well when it maps obviously to the physical metaphor and it provides a convenient way to access the function. The work objects in each focus area are natural candidates for manipulable objects in the interface; functions that interact with them are good candidates for direct manipulation.

Available when needed: Pull-down menus make a whole additional range of function available. This function is neither totally available, like the in-your-face function, nor is it totally hidden. It's like the artifacts on the physical model that are moved away behind the user. It's a reasonable choice for the function you need for completeness, but which isn't core to the work of the focus area. The work models—especially models of workplaces and artifacts—will suggest what can be put out of the way or out of sight. Functions related to these or similar objects can be put out of the way on menus. In the User Environment Design, functions that address the same intent within a focus area are clustered together——it makes sense to put them on the same toolbar or same pull-down menu.

In a dialog: Finally, some functions need additional information from the user, so the UI designer has to invent a way to get it. The easiest wav is usually through a dialog box. It's safe to assume that a dialog box that does not represent a focus area always disrupts work to some degree—look at how inserting a page break from the "Break . . ." dialog box in MS Word 6 disrupts the flow of work in a way that having "Page Break” directly on the menu did not. Once a dialog box has too

many controls, it creates the experience of a new focus area by sheer complexity. Experienced users may learn to ignore irrelevant parts of the box-as 90% of users ignore 90% of the print dialog box 99% of the time—but others will have to stop and parse the information in the box. That makes dealing

Good UI design lets the user focus on an activity in a single place

with the box its own type of work and therefore its own focus area. Taking another example from Word, look at the difference between creating a table from the toolbar button and creating a table from the table dialog box. The button fits directly into the flow of editing—it's appropriate when the user is just inserting a table as part of the flow of editing. The separate dialog requires that you read, understand, and manipulate a new interface. It's appropriate when the user is thinking about the structure and appearance of the table as a design problem. For the cleanest mapping, try to keep all functions in the focus area's window. Avoid dialog boxes that don't map to focus areas.

## A PROCESS TO DESIGN THE UI

Getting the UI right is an important part of the design process. Good user interface designers experience the User Environment Design as giving them freedom. Rather than being asked to reinvent the product in the user interface, they are given a clear specification for what goes into the design. The specification is full of hints and implications— automatic functions, potential focus areas, and double links all suggest user interface options that will implement the intent of the designers. But the specification does not overspecify the user interface. It leaves a broad field open for creativity. Even if the UI designer is on the team, separating the User Environment Design allows them to concentrate on structure, then focus on UI as its own task.

Whatever approach is used to design the UI, it builds on the information in the User Environment Design and work models. A few principles help UI design fit it into the overall Contextual Design process.

Follow a defined process: It's possible to approach the Ul design task much like visioning—sketch several alternative approaches to the

UI, evaluate them with positives and negatives, and synthesize a single UI theme from the best of the alternatives. Just as the vision captured a single, comprehensive response to the work situation, a UI vision captures a unified response to the User Environment Design. It ties the system together at the UI level. However you approach UI design, take advantage of the affinity and models—review them for issues and concepts to inform the UI.

Base your design on the work models: The consolidated work models help guide UI design. The flow model shows the different roles and individuals that use the system; consistency and common mechanisms are most important for those parts of the system that support the same role and individuals. The artifact models show how people break up the work into chunks—design the UI to fit those chunks to make it more comprehensible. Sequences show how one step and task follows on another—running them through the UI reveals problems in interacting with the system. The cultural model shows how the users think of themselves—use color, packaging, and style to match your users' self-image. The vision shows how the system hangs together, and the storyboards walk through specific sequences of use. The UI designer can take advantage of them all.

Keep conversations separate: Remember that every new step in a design process sheds light and uncovers flaws in the previous step. As soon as the UI designers try to make a focus area real in an interface that works, they'll discover missing functions and structures that simply can't be made to work. At this point, separating conversations becomes critical: knowing whether the point under discussion hinges on UI, system work model, or customers' work practice and sticking to it makes all the difference to resolving disagreements amicably. By this point in the design process, a good Contextual Design team will automatically identify the conversation they are in and go stand in front of that model.

When working on the UI reveals a problem in the User Environment Design, the team decides whether to go back and fix it or not. If it's just a question of a missing function, and adding the function in no way changes the purpose or scope of the focus area, it's easy to note it and go on. But you may find that the basic structure of the User Environment Design doesn't work. You may find that adding the function changes the scope of the focus area beyond its current definition. In these cases it's best to go back and rethink the User Environment

Design. Use the physical props to help you here. Your sketch of the user interface holds the user interface design conversation, and your

User Environment model holds that conversation. Move between the two physically as you discuss the different issues, and you'll focus your team better on the question at hand. (Constantine [1994b] discusses how to support movement between phases in the development process.)

The User Environment Design and storyboards are the primary guide in working out the UI—the User Environment because it gives the structure to make it real and the storyboards because they capture alternative UI ideas and show sequential histories of use. Other models give additional guidance in working out the details of the user interface. When it's done, the result is an interface that presents a coherent system work model to the user and is ready to be mocked up in paper.