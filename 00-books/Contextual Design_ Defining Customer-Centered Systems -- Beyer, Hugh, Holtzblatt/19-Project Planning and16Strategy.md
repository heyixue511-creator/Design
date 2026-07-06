# Project Planning and 16 Strategy

ecause the User Environment diagram shows all parts of the system in relationship to each other, it's a basis for planning as well as a basis for design. Most systems are large enough that they need a team of people to build them and have to be delivered over a series of releases. Most systems don't stand alone; they work together with other systems to support a whole job or business process. It's this collection of systems that taken together must support a coherent work practice. And software development organizations don't care only about individual applications or products—they're often looking for ways to tie their different systems together into a unified strategy for supporting their target market or business. Such a strategy makes the corporate response we discussed in Part 4 possible.

The challenge for project management is to define releases that keep the user's work coherent and can be implemented by the people available in reasonable time. Planning coherent releases can take advantage of the User Environment diagram as a representation of the systems, their parts, and their relationships. The User Environment diagram guides planning by breaking the design into natural components, relevant to the cus-

Management challenge: dene releases that keep user work coherent

tomer, that can be considered independently. Whether these components represent a small part of a single product or a complete application in their own right, the User Environment diagram shows what's going on in that component and how it relates to the rest of the system. Based on this, a team can organize and plan their development strategy.

## PLANNING A SERIES OF RELEASES

The usual situation with a systems development effort is to envision a larger and more complete system than can easily be delivered in a single engineering cycle. Whether it's a product for sale or an internal system, customers typically don't want to wait years to see the first version. By then, they'll have taken their business to other vendors, or their business will have changed so much that the system will no longer be useful to them anyway. It's not even good engineering to spend years producing the maximal solution—any system will miss the mark to some degree. The sooner there's a version out there, the sooner the team can correct their mistakes and build on the new work practice that customers will invent around the new system.

It's important to envision the bigger picture. It gives you a goal to strive for, a direction to your development. But use the larger vision to

define a series of releases, each leading you closer to the vision and each deliverable in a reasonable time frame. Many organizations aim to have the first release out in under a year, even for significant projects. This release sets the customers' first impression of the system and organization that delivered it. The

system should make a splash in the market or make a significant contribution to the customers' business. But it also needs to hang together as a coherent way of working. Every function interacts with other functions in the design—it's a waste to do large amounts of work to ship a function and none to ship the other functions. that make it useful. The last-minute sessions to decide exactly what will make it into a particular version are the most painful. What's the criteria for choosing what to cut? The last feedback from a user group? The most recent customer to call an account representative on the carpet? Whoever shouts loudest on the engineering team? Teams need a process for deciding what functions are most important for the work of the customer and how to deliver them in chunks that keep the work coherent.

When delivering to an internal client, basing development plans on a long-range vision creates the possibility of integrating the development schedule with the organization's business plans. Each piece of the User Environment Design suggests new roles and new ways of working—as each piece is implemented, the organization can put the process changes in place needed to take advantage of that piece. Keeping the business reorganization and system delivery synchronized keeps the process under control.

When delivering a product to a market, creating a larger vision and delivering to it over a series of releases means you have a coherent market message. Reveal the vision as your strategic direction, and then each release is not only useful in its own right but is also another down payment toward your commitment. Instead of selling individual features, you can sell product directions that address problems people experience in their work. Everyone—marketing, sales, services, and development—can push their work in this common direction.

Focus areas and the clusters of focus areas that together address a common intent are one way of looking at how the functions of a sys-

tem group into subsets that can usefully be shipped together. In Figure 16.1, the "Select base configuration” and “Find configurations"” focus areas together let the user view, search for, and select a configuration to use as the starting point for any changes. These two focus areas work as a unit. It wouldn't

make sense to ship one without the other. However, the system could ship without both—developers would then have to type the name of the base configuration directly. This might be reasonable for a first cut at the system.

Another way to prioritize the system is to deliver coherent support for a role, responsibility, or task. The first responsibility of a configuration management system is to support developing code, so the marketing team might decide that the first release has to support developers. “Modify product" is the core focus area for developers, so it had better be included. A minimal release would include just enough other focus areas and functions to support making a change: choosing a base configuration to modify, choosing the specific “parts" to edit, making changes and testing them, and finally packaging up all modifications into a single “change," which is put back in the system.

Once they make the decision what to include in the system, the team makes a shipping User Environment Design showing just those focus areas and functions that are intended to be part of this release (Figure 16.2). This shipping design, when all focus areas and functions are fully specified, forms the core of the software specification for this release. By extracting the subset they intend to ship and representing it

![](images/d4e35fd81063f644d04955e374e45eab090181813ea6d411e0cd6dd2f028cbb1.jpg)

cam cine a e ce chae re ne che  unt chaqnse ne ne ehi ie ar e ie ne tiy

oper cwoenthde ee oeeone aeee eoe m onod (ae aeoe o s eoe e e a eoese o eedaos rese e c e eds   eo, a e eshae

as a User Environment diagram, the team can see whether that subset stands on its own as a self-contained system supporting coherent work. They can validate it, run scenarios through it, prototype it, and test it with users. They can find out both whether it works as a coherent system and whether it works as an interesting release—whether it provides enough to make customers interested in adopting it.

Reviewing the User Environment Design in Figure 16.2 suggests that a cut supporting only development provides only minimal support for one role—hardly a competitive product, and with no extra features for product differentiation. So marketing might decide that supporting the Gatekeeper is a requirement for a viable product. It's a fundamental responsibility of the Gatekeeper's role to review a configuration and decide whether it's good. So there's no point in shipping any of the focus areas supporting the Gatekeeper if the system doesn't include “Qualify configuration." It won't be used by Gatekeepers if it doesn't support that part of the role.

It may not take all the functions of a focus area to support a role.

Only some of the functions of "Modify configuration" are needed by developers, so if they are the targeted users for a first cut of the system, the other functions could be left out. When a role is the target for a release, looking across focus areas for the core function to support that role reveals what's most

important to include.

Finally, because the decision of what to cut is an engineering tradeoff that has to account for implementation difficulty, the team can consider alternative presentations of a function or focus area in the UI. The UI can make the function easy or complicated to implement. For those functions core to a focus area or to a role, it may be worth designing a sophisticated UI that makes the operation of the function smooth and easy. But for less central functions that are nonetheless needed to support the work, a bare-bones implementation may be sufficient.

All these ways of looking at how to prioritize a release depend on understanding what the core innovation of the new system is. What is the

one key change in people's work practice that the system introduces? Don't look for a feature; look for the key way in which the system makes work different. Look for the key differentiator your product offers over the competition or the core way your system helps your customers advance their business goals. Once you've identified the key differentiator, ask, What's the minimum subset of the system necessary to introduce that change? The User Environment Design helps to maximize the impact of a new system by showing what part of the system will implement the core innovation coherently. Then you can build on that to support more of the work, more completely.

![](images/e3e7bcb7c21c70df827daaef7658cb1e0631478c9e9ebab6a0d636ea41234d56.jpg)  
FiGuRE 16.2 A shipping User Environment Design: a subset of the configuration management User Environment Design supporting developers.

## PARTITIONING A SYSTEM FOR IMPLEMENTATION

Real systems are built by more than one person—by teams working together. If dividing up the system is to be useful, every developer must be free to focus on his or her own part. But any requirements document has holes—developers in front of their machines at 2:00 in the morning will have to make decisions that affect the user. With the User Environment Design, those decisions can be made with the knowledge of how it affects the overall design and other design teams. The User Environment Design organizes requirements to show how the system is structured for the customer. But the User Environment Design also helps manage a project by showing how it can be split up for implementation by teams or individuals working in parallel.

The concepts of the User Environment diagram can help a team keep the coherence of user work during implementation. Assign work purely based on technology or implementation considerations, and each developer may not have a coherent piece of the work to code. That will lead developers to lose the focus on the customer. They can't see how the work is supposed to hang together, so they have no way of knowing if a decision they make disrupts the flow of work or supports it. Each focus area represents a coherent concern. It makes sense to assign whole focus areas together, or sets of focus areas addressing a role or task, so that developers can see one complete piece of the whole. If the User Environment Design can be broken into components, as above, whole components can be assigned together. People can think about and design these coherent units as a piece because they hang together in the system and in the work (Figure 16.3).

An implementation subteam needs a coherent part of the system to design, and focus areas provide such an organizing theme. But a large system will have multiple subteams, and some may be organized around components of the implementation such as common objects or technology components (e.g., the interface to a database). Organizing a project for delivery is a balance between keeping the user's work in the system coherent and keeping the implementation coherent.

For any system to work, the teams focused on implementation components need to understand how they relate to user-visible behav-

ior. A team implementing a reusable component to embed video clips in mail messages, for example, would have to understand how the activities of reading and sending mail are structured so that the reusable component can fit into the work smoothly.

The UED reveals reusable components

It would be important to them to see as many different situations of use as possible, to understand the requirements on the component and how to make it a seamless part of the host system. A team implementing a reusable component to support an underlying database link would need to know what kinds of demands the systems might make on that link.

The User Environment Design reveals how reusable components relate to the system work model and shows who needs to work with whom. A team building an object class to implement a work object from the User Environment Design needs to work with the teams building the focus areas where that work object is used. The teams working on focus areas need to manipulate the objects and have a stake in the design of the class. In the UI, the object is a visible screen artifact and should appear consistently in all parts of the system. The User Environment Design flags all the players who need to be concerned about these elements so they can agree. In this way the whole team—even those working on internals—stays grounded in the user's work. And the User Environment Design provides a map of which development teams need to work together.

Links between focus areas assigned to different subteams show points of integration. A link shows that one part of the product needs to provide access to another part and that the work flows from one part to the other. The parts need to connect technically, so some kind of call or invocation mechanism needs to be provided. This might be through the underlying platform (moving a mouse from one window

![](images/b1d85e80b12b2fb62760d0079d6dd59e7508fc9ce4b0a3f08401cca914130771.jpg)  
FIGuRE 16.3 The configuration management User Environment Design annotated to show implementation details. The different patterns and shading show how the focus areas have been assigned to implementation teams: one team has the Developer's parts, another has the Gatekeeper's, and a third has all the "Find/View result" linked focus areas. Because these focus areas all present the same interaction style, it made sense for one team to implement them all.

![](images/ed493d3d9a99fbb45bab23722fae7e7b934f3368ec979900d760b8e1485f292d.jpg)

The User Environment Design has also been annotated to show internal application programming interfaces (APIs) that the different implementation teams have to agree on. There will be a standard Query API, for example, that will be consistent across the "View/Find" focus area pairs. This Query API will be used whenever a part of the system wants to present an interface that allows the user to search for and choose an element to work on. Similarly, the User Environment Design shows external APIs that the team has to conform to—the Mail and Edit APIs.

to another), by using standard application integration mechanisms (OLE or CORBA), or through special APIs. But not only do the soft-

Use the UED to help coordinate implementation teams

ware components need to access each other, but the user needs to feel like it's one consistent system. It's important that the system have a consistent appearance and behavior across the focus areas that are linked and used by the same people.

The User Environment Design helps keep teams from becoming myopic and overfocusing on one situation. The "Modify configura-

Use the UED to help developers see their part in the whole

tion" focus area is used both by Developers and Gatekeepers. If it were given to the subteam implementing the Developer's part of the system, they could easily overemphasize the Developer as their user. The User Environment Design reminds them they support two roles, two kinds of tasks, achieving

two separate intents.

UI implementation considerations may also guide the assignment to teams. If several focus areas need a particular technology—such as natural language query mechanisms in “Find configurations" and “Find parts"—it's natural to assign all these focus areas to the same subteam so they can work out the solution once and apply it everywhere needed.

By showing the structure of the system, the User Environment Design provides a map to the implementation. Just as electricians can use a floor plan to talk to carpenters about how to locate the holes inside the walls so that the users can get their outlets where they want them, so the User Environment supports a conversation between the parts of an implementation team about how to deliver the system. It splits up the implementation into coherent units, shows how they relate to each other, and shows how teams focused on internals need to coordinate with the rest of the project. (Hsia et al. [1996] suggests another approach to sectioning a system for delivery.)

## COORDINATING A PRODUCT STRATEGY

More and more, both internal organizations and software product companies are shipping sets of applications, each supporting a different aspect of the user's work. More and more, these organizations are looking to tie these point solutions together, so they provide seamless support to the work while still being packaged as separate products. Or they're looking to support a new market or process that they've never addressed before and will need to address with a suite of cooperating applications. This is hard to do, especially when starting from multiple existing applications. It's difficult to put the essentials of each application out next to the others to see how they could relate.

A large User Environment model can show how a set of existing applications combine to support the user's work. Extract such a model

as a reverse User Environment Design going application by application. It's usually not necessary to do a full model——representing focus areas, purposes, and flows (as in Figure 14.5) is enough to see the structure without getting overwhelmed. Use a validation walkthrough of the resulting model to look

A reverse UED ties existing unintegrated systems together

for all the ways your current product set fails to deliver a coherent system work model: all the missing links between components, duplicated functions, missing functions, and inconsistencies. Then collect data on the systems in use to see how the work hangs together in practice. Identify changes to the User Environment model that address the problems. Use the structural principles for a User Environment Design to guide these changes, and use the work models to see where the current design falls down and how to fix it. When you have a new User Environment Design, showing how your existing suite should be modifed to provide a coherent solution, you’re ready to decide how to change the applications.

The links between each part of this new design show integration points, where the applications need to share data or support the user's

transition from one kind of work to another. The work objects that appear in different parts of the User Environment Design show key points for data integration across the different systems—these are the objects that will need common definitions, com-

The UED reveals points of integration

mon storage, and common UI. Each project can define a plan for moving to the design specified by the User Environment over one or more releases. Build a shipping User Environment Design showing the first release for all projects, and you'll be able to keep them synchronized.

Building a systems strategy when there are no existing applications is actually easier. You can design the overall system directly, from storyboards, like a single system with a wide scope. Then use the User Environment Design to identify good places to partition the system into applications. Each application should support a coherent part of the work or role and have clean interfaces with the rest of the system. Once you've partitioned the system, the links across partitions and common work objects identify integration points.

IT shops can use the User Environment Design to identify not only the parts they will build, but also the parts they want to buy from ven-

dors. The User Environment defines requirements for the acquisition, showing what it must do, how it must be structured, and how it must fit with the other IT systems. IT development teams have done this—in one case, they designed their desired solution

directly from a vision and storyboards, representing it in a User Environment Design. Then they brought vendors in, showed them the User Environment Design, and invited them to bid on delivering it using their products. The vendors had to prove they could customize their system to support the structure and functions specified in the User Environment Design. They chose the vendor who was most successful at showing that, with reasonable modifications, they could support most of the design the team had specified.

The User Environment is a model that enables the project teams to talk to each other about where system boundaries should lie, how

to create the bridges between systems necessary to support the work, and how to assign and reuse implementations of common system functions. Teams use their User Environment Designs as an artifact to talk over in coming to an agreement on the relationship between groups. In one case, two teams laid out their respective User Environment Designs to support their discussions and ended by canceling one of the projects—the diagrams had made the overlap so obvious that they couldn't justify the existence of both.

## DRIVING CONCURRENT IMPLEMENTATION

The User Environment Design defines the structure of a part of the overall vision—the part that is instantiated in software (and possibly some hardware). It provides the next level of detail about the vision by working out the system work model for the vision. Just as the vision guides different groups in creating a single corporate response, the User Environment Design guides different groups in delivering parts of the system and associated processes in parallel, yet in coordination:

Planning process: The User Environment Design represents the system work model and can be used to support planning business processes. Once you've worked out the coherent units of work in focus areas, you've also laid out coherent chunks for a business process. Defining the process and defining the User Environment Design go hand in hand. You can walk through the new process to see how it's supported in the system. Out of this, identify problems with the system or process, what training needs to be developed, and how to introduce the new way of working to minimize disruption.

Implementation: The User Environment Design specifies behavior without specifying the user interaction mechanisms. An implementation based on the User Environment Design will be free of bias toward one UI over another. When the UI is designed, it can be hooked to the underlying implementation so that there's a clean separation between the UI-specific code and the code that implements behavior—a cleanly layered implementation. The basic function of the system is defined in the functions and objects of the focus areas. As an additional guide to the implementation, annotate the User Environment Design with implementation constraints—for example, the required speed of following a link or the constraints on size or access time of a focus area.

Documentation: The User Environment Design specifies the function of the system so documentation can start to describe what it does. Furthermore, the specification of coherent focus areas, each with a defined purpose in supporting the work, gives documentation writers a clear structure and motivation to communicate. The User Environment Design reveals opportunities for additional user services, such as help desk support, training seminars, and follow-on consulting, and provides the information needed to plan them.

Test plans: The combination of storyboards and User Environment Design provides the information necessary to start test plans. The storyboards show how the system should work; the User Environment Design provides the formal definition of the functions. It's straightforward to build a test plan that checks these statements of the plan against the actual system.

Because the User Environment Design is focused on the system work modelthe system as experienced by the user—it gives a way to

structure and think about the system that keeps the system work model coherent. The chunks of the User Environment Design map to chunks that designers need to think about and design as a unit. As such, it's a natural structure for presenting system requirements. Implementation has its own coherence, which will

come later and which may be represented in an object model. But the structure of an implementation is less useful for planning a customercentered project than the structure of the system work model. Thinking about the system work model—the User Environment Design—ensures that the parts of the system and the components that are delivered are coherent from the user's point of view. That's the key value of the User Environment diagram in planning: it ensures you don't lose coherence for the user in the turmoil of getting to the implementation.

## MARDELL'S STORY

In the early days of WordPerfect, the founders of the company worked in the same building as their users. It wasn't a problem to stay close to their customers. But as the company grew, developers lost that immediate connection. So the company decided to put together a strategic effort to decide on the direction of the WordPerfect product and recover that immediate sense of the customer.

We put together a team of four or five developers, a marketing person, a documentation writer, a UI designer, and a usability specialist. This was simply not done in the company at the time—design was driven by engineering, with marketing getting involved later.

We used the complete Contextual Design process in this team to build a picture of our market and design new product directions to address the market better.

The new designs we came up with were well received in the company, but suggested changes beyond WordPerfect itself. So we split into two teams: one focused on broad strategic issues across the product set, and one focused on improvements to WordPerfect. This required both teams to refocus and redefine their mission.

I led the team focused on WordPerfect. We found that the most important parts of the process for us were interviewing, sequence model analysis, visioning, and paper prototyping. The strategic team continued to use the User Environment Design to show the company's different products and how they related to each other. But we had the strategic direction from the first round: we were focused on developing one product and concentrated on one focus area, WordPerfect's editing window. We didn't need the User Environment Design for that.

As we worked with the process, we recognized that it was a backbone for understanding the customer that could incorporate different activities. We started to use it less rigidly than we had. We decided we weren't creative enough and started to incorporate other techniques to expand the possibilities in our visioning. We found that our customer insight helped us make better use of enhancement requests in our customer feedback database because we understood more of the context of a request. We did a teardown of the current WordPerfect product and competitors to find places for improvement. And we analyzed other kinds of products for ideas as well.

Early on, we had a choice whether to focus on short-term improvements or long-term new directions. Since we did have critics in the early days, we decided we had to show concrete results. We developed specific ideas, prototyped them in paper and in code, and got them into WordPerfect 6.1. When these features were the ones reviewers and customers picked out as being the important innovations of the product, our credibility went way up.

Though we conceived of our ideas as integrated product directions addressing whole themes in the customer's work, we found it easiest to communicate them to developers as features. We would select features to push out together, to address some aspect of the customer's work. We did a lot of one-on-one work with developers, showing them prototypes of a new idea and taking them along on customer visits. (We’ve tried to make sure every developer goes on at least one customer visit.) We transfer ownership of the idea to the developer—they get credit for refining it and making it real.

WordPerfect's been sold now——several times—but that was an amazing team, and the ideas we developed are still important to the product.

![](images/5ab883ce39d635b154e4702a39cd1e801ae209bdbc43b81353f3cce923936e9b.jpg)