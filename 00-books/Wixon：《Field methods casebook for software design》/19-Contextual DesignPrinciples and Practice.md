# Contextual Design: Principles and Practice

![](images/a048b29c4b24322da4bbd0b1d7a92e5a42d5c7162b1b13b57954639e8b923ef8.jpg)

Karen Holtzblatt

Hugh Beyer

InContext Enterprises, Inc.

## INTRODUCTION

Contextual techniques aim to ground the design process in a solid base of customer data. As an industry, we are still learning how to accommodate to the demands of customer-centered design. A new approach to product design and development requires readjustment from everyone. The pioneers in this area are working out new relationships between the design team and their customers,¹ between designers and developers, between development and marketing, and between development and management. The case studies in this book give examples of handling some of the primary issues.

In this chapter we will describe our experience over the past nine years coaching many different development teams in collecting and using customer data in their projects. Through this process we developed Contextual Design, a structured, step-by-step roadmap to guide a team from initial project set-up and field interviews through design and the transition to implementation. This continual use of the process has forced us to address many of the common issues of collecting, interpreting, and using customer data.

As we describe Contextual Design we reveal the underlying motivations of each part of the process. We show how each part is intended to solve organizational or interpersonal problems, or to support the process of design. This allows us to identify design principles guiding the adaptation of a customer-centered process to the needs of a particular organizational situation. The other chapters of this book describe specific experiences using field research techniques, and provide a rich mine of ideas and descriptions of how these ideas worked in practice. We offer this discussion of Contextual Design as a framework for the whole design process, tying together different techniques into an orderly sequence, and showing some of the issues customer-centered design must address.

## BACKGROUND OF CONTEXTUAL DESIGN

Contextual Design had its roots in a challenge from John Whiteside to his usability team at Digital Equipment Corporation: To develop new techniques that would lead to fundamental changes in products, rather than minor iterations. The usability testing techniques he was using on Digital's products at the time collected feedback on an existing product or prototype, and as is always the case with this kind of testing, tended to produce iterations on the existing theme rather than creating new approaches to the problem.

Karen Holtzblatt responded to this challenge with the recognition that radical corrections to a design can only come from a better understanding of how customers work. The resulting process, which came to be called Contextual Inquiry, drew on several disciplines. Ethnography provided the fundamental method of understanding work practice by living in a culture; psychology supplied techniques to shorten the time needed to study long processes, and an understanding of how to manage the interpersonal dynamics of an interview. The need to see design implications within the constraints of quickly delivering real products dictated the style of interaction in the interview. Holtzblatt worked out these ideas in collaboration with Sandra Jones and through iteration with design teams at Digital. Putting the first field research approach in practice, a new problem emerged: Suddenly engineers had access to huge amounts of data about their customers. This created a need to organize, interpret, share, and represent the data in an external form. As a member of Lou Cohen's quality group, Holtzblatt borrowed the concepts of a cross-functional team and adapted affinity diagrams, one of the "seven new Quality tools" from Japan (Brassard 1989) to collect, organize, and present the major design issues from a set of interviews.

Contextual Inquiry was first named and formalized publicly in a tutorial at the conference on Computer/Human Interaction (CHI) developed by Holtzblatt, Jones, and Steve Knox, with substantial support from John Bennet and Dennis Wixon. Their assistance, and that of the rest of the usability and quality groups, is gratefully acknowledged.

Further work revealed that teams found it difficult to know what specifically to build based on the hierarchical set of issues presented by an affinity. Hugh Beyer, familiar with the use of graphical formalisms from his software engineering background, began to look for more formal representations of the thought steps implicit in representing customer work and system structure. Together, we developed work models as a more natural and coherent representation of customers' work, and introduced work model consolidation to see common patterns across all customers. As we worked with teams, we discovered that they kept getting stuck in user interface (UI) detail when we wanted to talk about the underlying structure of the system. We had no way to discuss this structure except by drawing UIs. Software engineering methods offered different ways of representing a system, but none of them showed system structure as it supports the user (Keller 1992, Seaton 1992), so we developed the User Environment formalism. We were already using paper mockups with Contextual Inquiry to develop the UI, and discovered they were as effective to test structure (Kyng 1988, Ehn 1991; see Muller 1991 for related work). Finally, we found that engineers needed assistance with the transition to implementation. We had already included work objects in the User Environment formalism, so we were able to build on it to make definition of the system object model easy.

This evolution led to the structure of Contextual Design as it is now: Contextual Inquiry to gather field data from customers; interpretation sessions with work modeling in a cross-functional team to understand the data from single interviews; affinity diagrams and work model consolidation to see the scope of issues and the common patterns of work across all customers; redesign to invent how to improve work practice; User Environment design to specify how the system should be structured from the user's point of view and drive object modeling; and paper mockups to test and extend the structure and user interface with users. At each point, we were driven to extend the method by the needs of our teams attempting to ship products. Very little in Contextual Design is totally new. We have adopted and adapted processes developed by others and have formalized practices that existed informally, putting them together into a smooth flow of work to solve the problems of defining systems.

![](images/a273c75524342499372064b5c79a040a81aca7422064a622f273c87b44086b54.jpg)  
FIGURE 17.1 Contextual Design.

The base structure of Contextual Design has stabilized over past three years. However, in the spirit of continuous improvement, not only do we continue to evolve it but every team we work with evolves it as well. Having learned to study work practice, teams apply their knowledge to their own situation, and create new processes and techniques to handle their unique situations. Because it has been taught on its own, Contextual Inquiry is widespread and is being used and evolved independently. We thank all the teams who have worked with us and who, through their questions and commitment, have allowed us to synthesize a coherent approach.

## CREATING THE PROJECT

The first challenge of any customer-centered design project is to define the project so that it is focused on the right problem, includes the right people, and has a clear process to follow. Coming to a complete understanding of the customer, defining a system which solves real work problems, and handling the host organization are all simplified if these tasks are done well

Defining the problem. We find that projects usually start with too narrow a statement of their job. Either they focus on a single tool or task, they assume they will just add some features to what they already have, or they want to exploit a particular technology; but a tool supports some aspect of work, and that work is a small part of the users'whole job. Unless the design team understands the whole job and sees the task the tool or technology supports in the context of its use, they cannot support the job well. They cannot ensure that the tool they create will fit with other tools, systems, or manual processes without causing breakdowns in the work when users have to move into or out of the tool.

Designing well means designing systematically: Seeing the whole work practice of the user, and designing a coherent response that hangs together as a new work practice. This doesn't mean the system has to be huge—only a small part of the new work practice might be automated. However, it does mean that the new system design takes the whole work practice of the user into account. Systemic design not only supports the work better, it leads to innovation. As long as spreadsheets thought they were tools for calculation, they could only supply more math function; once they realized that their numbers had to be presented and used, they started to make formatting and presentation functions available. The first spreadsheets to do this supported more of the work, supported it better, and differentiated themselves from the rest.

We develop this broader focus by working backwards from a team's original problem statement to identify the whole of the users' work practice or job that is affected. Then we ask who else in the customer organization is affected or cares about this job. This is the wider context the team needs to understand to design well. It defines what the team needs to care about and who they should interview to understand the work.

Defining project membership. We borrow from Total Quality Management (TQM) (Demming 1982; Ishikawa 1985) and define a crossfunctional team to design the system. The goal in TQM is to ensure that the product which is designed can be manufactured, tested, marketed, and delivered. Taking these considerations into account during the design of a new manufactured product means that many potential problems that would have to be overcome by these other functions are solved before they ever occur. The involvement of the other functions in the design eases the transition to production-each team member ensures the design accounts for their issues, and can start gearing up even before the last details of the design are finalized.

In the same way, a cross-functional software design team gives responsibility to those who have a stake in the design. The biggest roadblock to rapid development of software systems isn't technical it's coming to a decision on what to build and sticking to that decision. Any time a small group defines a system which others have to live with, they put themselves in the position of having to convince the others that their decisions are right. This is true whether the designers of a commercial system are trying to convince everyone else involved in getting a product out that this is the right thing, or whether the designers of a custom system are trying to convince their clients that they want to use the new system.

Instead of trying to convince them that the design is sound, we put marketing, usability, UI design, test, and customers (for custom systems) on the team with software designers. Each member of the team collects and interprets data and influences the design to account for the issues with which they are familiar. Interacting with the team in face-to-face meetings, they teach other team members their own perspective. The design becomes more marketable, usable, aesthetically and ergonomically pleasing, robust, and useful. Each member of the team can recognize the implications of the design on their own organization, and can prepare their organization accordingly. The result is fewer problems in the design, and more buy-in to the new design.

In our experience, nondesigners do not see the design implications of customer data as readily as those who have been involved in software design, so at least half the team should be designers. And most importantly, all members of the team must have credibility and respect in their own organizations. Everyone must trust that the solutions they come up with are reasonable.

A team size of more than 8–12 people is too difficult to manage, so the team must communicate progress and results to the rest of the organization. Any team needs to capture their work as they go, both to support communication to others and to track their work for themselves and for new team members later. Contextual Design includes points in the process where others can learn what progress has been made and can contribute to the design.

Defining the process. To gain the benefits of cross-functional perspectives, the team needs a clear process that allows them to do real design together: gathering detailed customer data effectively, supporting design conversations and making them concrete, and supporting team design. Without a clear process, the team spends its time working out the process instead of working out the design.

This is difficult—doing actual design together as a team is rare in our industry. It is much more usual to divide a problem up into small parts, give the small parts to individuals to solve, and have them bring their solutions back to the group for review and approval. Any real design is worked out through informal conversations in the hall and in offices. A project leader or architect might attempt to keep all parts of the system coherent by being the conduit between the different project members. Where difficult decisions must be made, one person might be appointed to dictate the answer. There is no sharing of perspectives, and little collaboration among the whole team to guarantee that the system will hang together.

A clear process gives the whole team rules to live by. It provides a well-defined framework for design activities, with principles to guide how to tailor them to each situation. It makes the role of each team member within that framework clear. Each design activity has its own clear task, and a defined way to resolve disputes. It is clear where the data that drives each design activity comes from, and what results are expected from it.

Contextual Design is such a process.

## UNDERSTANDING THE CUSTOMER

The first concern for design is to bring valid, useful data about how people work into the engineering process. Any system controls how people work on a day-to-day basis. Making a system fit well with the work people do requires understanding work at the level of daily action. However, finding out about work at this level of detail is hard. Not only are developers building for customers doing work in which the developers are not expert, but customers themselves have difficulty saying what they do. People are adaptable and resourceful creatures—they invent a thousand work-arounds and quick fixes to problems, and then forget that they invented the work-around. The detail of everyday work becomes second nature and invisible. Customers do not reflect on their work, and cannot describe it in a way useful to designers. An organization might have a defined process, but continuous modification in practice means that the defined process no longer reflects what is really going on. Contextual Inquiry is our approach to getting data on the actual work practice.

## Contextual Inquiry

Contextual Inquiry gathers design data by sending individual designers to watch people do their own jobs, interspersing observation, discussion, and reconstruction of past events (Holtzblatt and Jones 1993). A contextual interview, the most typical way of applying principles of Contextual Inquiry to define the data gathering situation, usually lasts two to three hours. Each aspect of Contextual Inquiry addresses some problem in gathering data.

It's important to watch ongoing work, because it is only while people are actually working that they have access to the details of what they do. Customers commonly say they do a task one way and then, during the interview, do something different. It is common for them to say they spend most of their time on one task, when in fact other tasks consume more time. A person's summary of the experience of months in a statement of what they do is simply not a reliable basis for design. We have found that the only way to ensure that a design team does not solve the wrong problem in the wrong way is to watch the real work as it happens.

Contextual Inquiry uses apprenticeship as a model for the relationship between customer and designer (Beyer 1995). Using this model puts the designer in the customer's world and gives both people a natural guide for how to behave. Once there, designer and customer can jointly build a shared understanding of how the customer works based on the specific actions of that day's work. The apprenticeship model suggests how to run the interview. It precludes taking a list of questions—the apprentice does not know what is important to ask about. It suggests that a one-on-one interview is best—the apprentice needs to build their own understanding, and having several apprentices do this at once adds confusion. The basic inquiry process is described by Holtzblatt and Jones (1993), though it has since been somewhat extended

The apprenticeship model leads to turning control of the interview over to the customer, while at the same time allowing discussion of the work as it unfolds. It is critical to discuss observations and interpretations with the customer during the interview. Designers will go back to the team and make specific design suggestions based on what they learned; however, the most important knowledge is not the specific actions the customer took, but the motive for those actions. If the new system can support the motives more directly, it will improve the customer's work. The only way for the designer to be sure that they understand the motivation correctly is to share their understanding with the customer. Interrupted in the moment of doing the work, the customer can say what is really going on. Without this shared interpretation, the team's design will be based on an interpretation that the designer made up.

Retrospective accounts (detailed reconstructions of past events) uncover more about the work than can be observed in two to three hours. A retrospective account leads the customer through an event in order, using the artifacts constructed in doing the work to help tell the story in detail. When a work process extends across weeks, months, or years, designers can learn about the whole process by retrospective accounts, and by interviewing different customers at different points in the process and performing different roles with respect to the task.

Some decisions of how to put Contextual Inquiry into practice are driven by pragmatic considerations of software development organizations. First, we assume that design teams are building products and systems, not conducting research. It is more important to deliver a useful system quickly than to understand everything possible about how people work. Second, we assume that the system will support more people than a team can reasonably interview given limited time. These considerations influence how Contextual Inquiry is used.

We train and send out designers rather than specialists in work practice, because it is the designers who have to understand the customer in order to design. If only specialists conduct interviews whether they be psychologists, sociologists, or usability professionals— they have to teach the designers what they learned so well that the designers believe it and act out of it automatically. We find that the data gets in the designer's head better if designers and specialists conduct interviews and interpret them together, rather than if specialists conduct all the interviews.

We usually do not recommend videotaping interviews, because the overhead of setting up and running the cameras and reviewing the videotape later is usually not worth the additional level of detail. We use videotape when the problem requires studying work at such a detailed level that there is no other way to capture it; otherwise, audiotape and notes are good enough. Even when we do use videotape, we have the interviewer review the videotape with the customer so they can build a shared interpretation of the customer's work together.

Customer interviews are conducted to discover the common underlying structure of work and the range of variation across all potential users of the system. The best way to collect this base structure and variation is to interview a wide variety of disparate people, rather than studying fewer people in greater depth. Common aspects of work will recur when new people are interviewed, and the tem will see more variation. Even if there are aspects of a customer's work that the interviewer did not understand, it's often better to clarify them by going on to the next customer rather than returning to the same one.

This way of collecting customer information is new, and most organizations do not have the procedures in place to make scheduling these interviews easy. The groups that have the easiest time are those who already create events with individual customers, such as for usability tests or focus groups. There can be internal resistance, too the sales force or marketing department can be suspicious of letting engineers talk directly to customers. But the reactions to the visits are nearly always enthusiastic. Customers feel like they are being listened to for the first time, and the sales force and marketing department soon recognize the benefits. When the customers are internal, they feel like they have control over the new system. Teams developing custom software often do more interviews than are strictly necessary, just to allow everyone to participate.

## The Interpretation Session

As an interviewing process, Contextual Inquiry successfully uncovers data about customers' work in detail. But it's not enough for individual developers to talk to individual customers. Each person on the crossfunctional team needs to learn about every customer. Each person will see something different in every interview, and needs to feed their unique point of view into the design. And each person needs to learn what the other team members see, so they can take on each other's perspective.

Interpretation sessions provide a forum in which everyone can learn about an interview, all relevant data can be captured immediately, and in which everyone has a job to do so that no one's attention wanders. The interviewer acts as informant, recounting the entire story of the interview in order, leaving nothing out. Everyone makes observations, asks questions, and shares insights and ideas for the system design; one team member (acting as recorder) types these points online as independent notes. Simultaneously, other team members draw work models as they hear them in the story. Because we run an interpretation session with four to six people, everyone has a job to keep them involved. When the session is done, all the data has been captured in the form in which it will be used. The captured points and work models will be used by the team to build their consolidated representation of the customer, and are also the medium of communication to anyone who was not present. They make communication to the larger team and to the customer community possible.

We find interpretation sessions to be more effective than reports or individual reviews of the interview for leading the team to meaningful insights. We have to be realistic about what to expect of people. With the best will in the world, people cannot communicate effectively through lengthy written reports—and any complete account of a customer visit will be lengthy. If the interviewer shortens the report by summarizing key findings, no other perspective can be brought to bear on the data—less will be learned from the interview, and there will be less sharing of perspectives across the team. The interpretation sessions produce more insight from each interview, and makes a team of the participants by giving them shared work to do.

## Work Modeling

Before people can communicate knowledge, they need a language. The words of the language must represent the concepts of the knowledge domain—the more specialized the domain, the more specialized the language. The diagramming formalisms of software engineering are graphical languages that use symbols to embody those concepts necessary to understand and communicate different aspects of the software problem (J. Martin 1992). Because a formalism is so limited, it structures thought. It encourages the use of its symbols, and therefore of the concepts those symbols represent.

Work models are diagrams that make work practice concrete. They provide symbols for representing the different aspects of work practice. Created during the interpretation session, they capture the work of specific customers as it is revealed. They record work practice as it was discovered, and support communication about it to others. They manage the complexity of work by defining five different perspectives on the work and providing a coherent model to represent each perspective. They uncover and represent the structure of work of individual users, making it possible to consolidate models across all users to see common structure. These consolidated models form the basis of design. Unlike a list of findings, requirements, or wishes, work models show how all aspects of work relate to each other.

Though we often create new work models to handle specific situations, we find five types of work models to be useful to nearly every problem. We will present each model and discuss the design conversation it supports after consolidation.

Context models. (Figure 17.2) Context models show how organizational culture, policies, and procedures restrict and create expectations about how people work and what they produce. Context work models represent standards, procedures, policies, directives, expectations, feelings, perceptions, and other emotional and cultural influences on how people are willing to work. They show which influences originate from outside the organization, and which are internal to the organization. The context model drives design by showing what changes in culture customers are willing to accept. Where a design enables customers to handle an influence on their work, or enables them to get control of it, it is likely to be accepted. Where a design conflicts with an influence, customers will work around it or will not use the system. Designing with this knowledge lets the team choose how to make the system fit into the work. Developers of internal systems have the additional choice of working with the client to impose new influences on the work (such as cost-consciousness) that are desirable, but not currently present.

![](images/79bec245207a932015484d73547aaf4941a9baf2fc50b1fdea21f488f3ae0310.jpg)  
FIGURE 17.2 Context model.

Physical models. (Figure 17.3) Physical models represent the physical environment as it impacts the work. They show how work is split across sites, buildings, and rooms, and how these spaces relate to each other. They show the organization of work places—the tools, artifacts, and work areas, and their relationships to each other. They show movement between spaces and forms of communication in doing the work, and they show hardware and software where it is used.

![](images/af21726eda4939c62d1c234b38d8b3870b94c5217630e34f447a43ed200a764b.jpg)  
FIGURE 17.3 Physical model.

To the extent that they can, people structure their environment to support the work; then they work around any problems put in their way by limitations in the physical layout, location, hardware configuration, or technology. Physical work models support design both by revealing the constraints imposed by the physical environment, and by revealing the work strategies made manifest in the way the environment is structured and used. The physical model reveals what kind of communication is required, whether the system must support movement, and what platforms the system must support. They reveal the natural organization of work, which might be mimicked or supported in the system.

Flow models. (Figure 17.4) Flow models represent people's responsibilities, communication, and coordination, independent of time. They show what people do, who communicates with each other, what they communicate to each other, and how they communicate. When we consolidate, the flow model shows how the work breaks down into roles, sets of responsibilities, and associated tasks for accomplishing part of the work. Whereas job responsibilities are idiosyncratic to the organization, roles tend to be very consistent from one organization to the next. The flow model shows how people combine roles in performing their jobs.

Flow models drive system design by showing who the users of the system are. Each role represents a coherent set of responsibilities for the system to support. By presenting a wide view of the work, the flow model identifies peripheral roles that might be more directly supported in the future. It identifies roles that are unnecessary to get the actual work done, and which could be eliminated (which usually means removing or automating the tedious parts of a person's job, not the entire job). The flow model determines the communication paths and artifacts the system should support or replace.

Sequence models. (Figure 17.5) Sequence models show the sequence of actions to accomplish a specific task in time. A sequence model can be focused on the coordination of activities across individuals, on the thought steps and strategies of a single individual in doing one activity, or on the steps taken by a person in using a tool to accomplish an activity. They are similar to flow charting and task analysis (Carter 1991). They show the intent, or motive, for the activity and for sets of steps, and they show the trigger (the event that caused the sequence to be initiated).

![](images/75da33e95759d396177cb7ee378774f832486d363c66e40930a88a3f04f663fe.jpg)

U1: Move user to larger disk   
Intent: Give user more disk quota   
Trigger: User requests higher disk quota   
↓   
Requests more quota of customer support   
↓   
Customer support discovers there's no more room on the user's disk   
↓   
Customer support calls U1   
↓   
Intent: Relocate user to a disk with more free   
space without losing any user data   
U1 looks for a scratch disk   
↓   
Initializes and mount scratch disk   
↓   
Creates user directory   
↓   
Moves user's files to the new disk   
↓   
Uses DIR to check that files are there   
↓   
Call user to confirm the user agrees all files are there   
↓   
User checks and confirms   
↓   
Delete user files from the old disk   
↓   
Send mail to system manager to add new disk to regular start-up   
↓   
System manager adds new disk   
↓   
Done

FIGURE 17.5 Sequence model.

Sequences are a detailed map of the work a system must support, improve, or replace. They tie specific steps to the intent of those steps, allowing the design team to see where replacing a step is possible and where the step supports some critical intent. Sequence models reveal strategies to support, ensure that work practice continues to work in the new system, and drive test cases for system design, usability, and system test.

Artifact models. (Figure 17.6) Artifact models reveal the detailed structure of artifacts created and used to support the work. They show the structure, usage, and intent of the artifact. Through their parts and arrangements of parts, they reveal how customers break up the work conceptually and how they use the presentation of the artifact to support its use.

Artifact models guide the creation of new system artifacts. They reveal what is used and what is not used in existing artifacts provided to customers. They indicate what new artifacts might be created in the

## XXXXX Co., Inc.

To: XXXXXXX

From: XXXXXXX

Date: 5/9/92

Subject: Need for larger disk

## Remarks:

What

Rationale

Do you think you could get us that disk drive we talked about? It s clear that as long as this project lasts we re going to be storing more and more data. It s slowing us down to keep going back to you every week. I think we need one of the 1Gig Syquest drives, and we want it on the XXXXXX group cluster. If it s ne

Description

Location Expense

FIGURE 17.6 Artifact model.  
![](images/ee1e246b4049afc3f7838cf507160a0a65f0aa57385eebca4c44b4dc31fa120b.jpg)

informal annotations and additions customers have made, and they indicate the appropriate structure for new artifacts by showing the conceptual structure customers put on the work.

Work models provide a concise way to represent the work of individuals and their organizations. Because each model is tailored to a specific perspective, they guide the team in thinking about the aspect of work they focus on. They provide the concepts necessary to understand how work is structured, and lead the team to see common aspects of work across their customers. They focus the team on the elements of work practice they must support and account for in the system.²

## CONSOLIDATION ACROSS USERS

It is easy to be overwhelmed by the huge amounts of data gathered by contextual techniques. With such a wealth of detail, it is hard to see the common issues and themes across all customers that a new system could address directly. Affinity diagrams and consolidated work models provide a coherent, manageable representation of the market or customer base for a new system.

## Affinity Diagrams

During interpretation sessions, key points, insights, questions, and design ideas are written as separate notes. Each interview usually generates 50-100 such notes, in addition to the work models. Fifteen to twenty interviews (typical for most projects) generate 1000-2000 notes in all. Affinity diagrams provide a technique for organizing and structuring this vast quantity of detail. Affinity diagrams were originally designed to handle 200–500 notes, but we find the process scales up well with more people (we try to get one person for every 100 notes). An affinity is built by putting up notes one at a time (clustering those that go together) that have an “affinity" for each other. The clusters are named, and then they are grouped into higher-level structures. Rather than impose a structure from the beginning, an affinity allows structure to bubble up from the detail. We encourage this by banning familiar categories such as “usability" and "quality," and by giving the groups names that express the user's intent: For example, "Let me browse to learn the structure of the system." In the groupings, the affinity reveals new insights (derived from the data collected from all customers), and lays them out on the wall in a coherent structure.

When done, the whole team walks the affinity to read what each part is about, and brainstorms design ideas for that part. (Anyone else in the organization who wants to influence the design can do this too.) Because the affinity organizes whole sets of issues into larger themes, it naturally pushes ideas that respond to whole themes rather than single features. Each person writes their ideas on Post-its and attaches them directly to the affinity itself. Later, when the team picks up these ideas to develop, they will be directly tied to the customer data that sparked them. People also identify holes (places where the data is weak) in the same way. Identifying holes helps the team plan what data to collect next.

An affinity shows the scope of the issues to address within the defined focus of the team. It captures and structures the team's insight into the customers' work. The cluster names represent these insights and tie them back to individual customer's data through the notes in each cluster. Because the structure is derived from data instead of predefined categories, it drives the creation of new insight into the problem.

## Work Model Consolidation

The affinity organizes and structures customer issues, but it is not a good representation of customer work practice. Its hierarchical, textual organization does not show how the work hangs together coherently. Individual work models do show the work practice of individual customers, but do not reveal common strategies and structures across the market. Designing a system to support the work practice of multiple people depends on understanding the common strategies across customers. Otherwise, the overwhelming tendency is to design for the specific customers interviewed and to create isolated fixes for single problems.

Work model consolidation provides a single synthetic representation of work. Consolidation brings together common aspects of all models of the same type, showing common structure but also capturing key variants. Consolidation is applied to each kind of model individually, resulting in a consolidated flow model, a consolidated context model, a consolidated physical model for sites and work places, and consolidated models for each task represented in the sequences and for each type of artifact.

Work model consolidation reveals structure that is pervasive and consistent across customers. Focusing on the exact job title or the specific steps taken in a tool obscures the consistent structure across users; work models focus on the division of responsibilities into roles, the intent driving work steps, and the strategies to achieve them. By revealing the fundamental structure, work models make it possible to see how that structure recurs in different ways across users.

A description of flow model consolidation will serve to illustrate the method. First, team members pair up and look at each actual model in parallel. For each bubble representing an individual, they identify the key roles that person plays. A role is a collection of responsibilities that go together naturally. (When someone says, "I wear two hats, programmer and analyst" they are describing two of their roles.) They name and list the roles and their responsibilities. When roles have been identified for all individuals on all models, they bring together similar roles from each of the models and name the role. They write a single list of responsibilities, removing duplications but otherwise retaining them all. Then they transfer the lines of communication from the actual models to the consolidated model. When done, the model shows the fundamental division of work into roles and communication between roles across the entire market or organization. A systęm designed to the work described in the consolidate flow model will be useful to everyone, no matter what idiosyncratic assignment of roles to individuals an organization may adopt.

Consolidating other models is conceptually similar. The first step is to look at the parts of each actual model and identify the intents of each part; then the parts with similar intents from the different models are collected. After that, the parts are laid out on the consolidated model in proper relationship to each other.

We frequently encounter skepticism about whether work across a market is so similar structurally that this kind of consolidation is possible; but in any work domain, we find there are only a few different strategies people use to get their work done. Most teams stop seeing new variants after incorporating 10-15 different individual models into their consolidated model. Consolidated work models are a powerful tool for any design team. If the system is for sale to a market, they describe the market at the level of how people work. They define who the customers are, what they do, and what they care about. They show who is affected by the system, who needs to buy into it, and who represents potential markets for related products. If the system is for a single organization, the models show how that organization works, who it depends on, and who its customers are. They show all the inefficiencies in their work and all the opportunities for process redesign. When the team redesigns the work, the models show the impact of their changes and help them anticipate how the new system might break the work. A complete set of consolidated models gives a team a solid base for design, identifying issues and opportunities for the system and ensuring that it does not disrupt work.

![](images/6bd35555df17fbf4abc9b32dea329b7c3c4cd861449dd4d2eab64efcdbc89c2f.jpg)  
Hcnd  dd  ondt.

## The Design Room

With an affinity and a set of consolidated work models, a team really needs a design room. These represent the team's knowledge of the customer on the wall; they don't want to have to unroll all the models and affinity to be able to think. Given the opportunity, the team will continually return to this data throughout the design process. It is common in our meetings for a team member to gesture or walk over to a part of their affinity to support a point they are making. It is hard to achieve this kind of fidelity to the customer when the data about the customer is tucked away, out of sight.

Having the data spread out on the wall is very different from having it online. Online representations are important too, for permanence and to share with remote sites, but a video screen cannot present the breadth of data that a wall can. By its very size, the screen reduces the scope of data that can be considered together in relation to a design. It works against systemic design—broad responses to a whole work problem—and toward single features.

Most of our teams start out complaining that it's impossible to get a dedicated room in their organization. However, it's hardly unreasonable to expect that, if a group of people have real work to do together, they should have a space in which to do it. This means a place where they can work together for days at a time, and where they can leave their work lying around. In the end, somehow, all our teams do manage to create themselves a room. Several have become so attached to working together that when the time comes to code their systems, they bring in their computers and code in the room. There they can reference their customer data, redesigned models, User Environment design, and implementation models.

The design room is an excellent mechanism for communicating progress and insights to the rest of the organization. When designed to communicate, the room is a living record of the design process. A team member or manager who wants to catch up can browse the walls on their own, or another team member can use the walls to tell them what has happened. Teams commonly invite other interested or affected groups to walk the affinity and consolidated models, writing comments and ideas on Post-its and sticking them up. The guests get the benefit of learning the data, the team gets the benefit of their ideas, and everyone feels like they can be part of the conversation. One manager told us he prefers to use the room to find out how the team is doing—he found it more immediate and more real than a status report or presentation.

## SYSTEMIC DESIGN

Working with specific customers gives the team an understanding of the work of those customers. The next challenge is to design a response which transforms work in new and useful ways. This is a new design conversation. Up to now the team has focused on work as it is; now they will design the work as it will be, when the new system is in place. This conversation is inherent in design. Every system changes the work of its users. We prefer to think about and design the effect the system will have explicitly, ensuring that innovations are driven by real customer problems and that they fit into the customers' work context.

We use an explicit visioning step to brainstorm alternative ways to redesign work and systems to support the new work practice. First the team walks the consolidated models and affinity to identify the key issues, roles, and aspects of work to address. They brainstorm alternatives as a group, elaborating each one for five to fifteen minutes. They compare the alternatives using a modified Pugh matrix process (Pugh 1991) to identify the good and bad points of each alternative, and finally merge the best parts of all the alternatives, fixing the problems and building on the good parts. The resulting vision is a signpost for the team, identifying what they are trying to do with their system.

The vision is just a sketch. It contains no details at all—we intentionally focus on the big picture before working out the details of the parts. The next step is to bring the vision down to earth, to say exactly what we will do to implement the vision.

The vision is brought back to reality through redesigned scripts. When the team analyzed a customer's work in terms of work models, they broke it up into five different views of work; a script reunites all these different perspectives to show the new work practice coherently. A script shows the role performing the work step, the work step itself, the changes in the physical environment required for this step, and the concepts or artifacts used in this step. The scripts are driven by redesign of all the consolidated models in light of the vision. So if the vision prescribes how to support a particular role, the team goes to the consolidated flow model, updates the role's responsibilities in light of the vision, and writes the script to ensure that the role can do its tasks. The other consolidated models support redesign similarly.

<table><tr><td>Role</td><td>Step</td><td>Changes to physical environment and technology</td><td>Concepts</td></tr><tr><td>User</td><td>User presses “Help&quot; button on their telephone.</td><td>Telephones with special buttons tied to particu- lar functions.</td><td>Phone is the way to talk to someone; it is integrated into getting help on a problem.</td></tr><tr><td rowspan="4">Help</td><td>Phone rings from user and sees user name and context, on his screen. Context includes system and location</td><td>Telephone tied into system: button dials number and prompts system.</td><td rowspan="4">Problem screen: user name, system, location; current screen. Provides an area to enter comments for self and anyone who looks at this problem.</td></tr><tr><td>First level help adds any additional information they collect and actions taken. Decides he can&#x27;t solve. the problem and presses</td><td>Speaker phones in every office.</td></tr><tr><td>his &quot;HELP” button. Problem logged in system.</td><td>Central database of calls.</td></tr><tr><td>Problem routed to the right responsible person</td><td>Database of experts and what kinds of problems</td></tr><tr><td rowspan="2"></td><td>When answered, shows problem context and any- thing first level help captured. Problem context overlays anything now on screen. (Issue—what if RP not there?)</td><td></td><td></td></tr><tr><td>System starts logging time spent on this problem. Displays time spent on screen so RP can stop it when he switches</td><td></td><td>Same time log as above.</td></tr></table>

FIGURE 17.8 Redesigned script.

Each script corresponds to the consolidated sequences from which it is built. Consolidated sequences define how the key tasks of central roles are performed. They show the key processes and strategies, together with the intents driving each step. Each consolidated sequence drives a redesigned script that shows how that task will be done in the new system. Each step in the consolidated sequence must be accounted for in the redesign; either the step must be supported, the intent of the step must be met in a new way, or the step is obviated because changes to a higher-level intent made this step unnecessary. Multiple scripts taken together drive the system design.

This work redesign step makes the invention of new work practice an explicit, recognized part of system design. Using the consolidated models and affinity as a base promotes systemic thinking, because they present the whole work problem coherently. Visioning promotes divergent thinking—inventing and considering unusual and innovative solutions to the problem, rather than proceeding along traditional lines. The Pugh evaluation process gives the team a way to consider the alternatives as collections of possible ideas, looking for the best aspects of each, rather than choosing a "winner" from a set of designs. And the redesigned scripts tie everything back to reality. Each of these principles—systemic design, divergent thinking, egoless evaluation, and fidelity to the data—is critical to good design, but never more than in this step where the system itself is defined.

## Separating Conversations

Going from consolidation to redesign is a switch between conversations. The team stopped talking about the work as it is done now, and started talking about work as it would be done in the future with the application of technology. The next step in design is another switch in conversations, from redesigned work to the structure of the system that will enable that work. Just as we supported the switch from consolidation to redesign by providing clear physical artifacts that support each conversation and keep them separate, so we will support the switch to system design by providing a new artifact, the User Environment model, to keep that conversation separate.

Design meetings are difficult, contentious, and lack clarity when the team unknowingly mixes conversations. Here's a case study: Joe argues that the mail system should allow people to read and answer other people's mail as their agent. Sue claims that would be a security hole. Joe says no, we could implement a password. Sue points out that we cannot implement anything as secure as the operating system.

In this short interchange, conversations have become completely confusedJoe was making a point about the work, but expressed it by proposing a system feature. Sue reacted to the design idea without recognizing the work conversation at all. Joe responded by fixing the design, at which point Sue went into an implementation conversation. They never even discussed whether the original work redesign idea—allowing people to act as agents for others—was reasonable. Any process that hopes to make face-to-face team design possible must provide a mechanism to untangle conversations.

Using models to separate conversations and make them concrete goes a long way towards clearing up this confusion. Each time a separate conversation is needed, a separate model supports that conversation. The work as it is now is a set of consolidated work models on one part of the wall. The work as redesigned is a set of scripts, on a different part of the wall. The system design will be on yet another part of the wall. Each model defines a place for the appropriate design conversation, and provides a physical prop that focuses the team on the issues for that conversation. Separating conversations is one element among many in providing an effective process for teams to design together. See Holtzblatt's article (Holtzblatt 1994) for a more complete discussion of making team design work.

## User Environment Design

The User Environment model defines how the system is structured to support the work of its users appropriately. It defines the places in the system to support the user's activities, the functions each place provides, the work objects manipulated in each place, and the flow between places to support the flow of work tasks. Just as a floor plan lays out a house, revealing its structure and the relationship of its parts, the User Environment lays out a system design. A floor plan allows the architect to see all the parts of a house and how they relate to each other. A User Environment design allows the team to see all the parts of a system and how they relate. It shows the system as a whole.

The User Environment model is a language for communicating and recording system structure independently of the UI or implementation. Building a User Environment model focuses the team on the appropriate level of detail. It puts off low-level decisions about look and layout until after the fundamental decisions about structure are made. It focuses the team on the structure of the system as experienced by the user, rather than the structure of the implementation. It defines the requirements on the implementation, provides initial objects for the system data model, and defines the structure of the user interface.

<table><tr><td>1. Call for Help</td><td></td><td>2. Work on User&#x27;s Request See, work on, and track user&#x27;s problem.</td><td></td><td>3. See System&#x27;s History</td><td></td><td></td><td></td><td>See the past problems with this system and how they have been resolved. Functions : o See problems on this system, who</td><td></td><td rowspan="3">worked on them, when and how they were resolved • Search for problems of particular type</td></tr><tr><td></td><td>Functions : telephone</td><td colspan="4" rowspan="8">o See history and comments of this problem</td><td rowspan="3"></td><td rowspan="3"></td><td rowspan="3">o See system type, hardware and software installed</td></tr><tr><td>o Transmit user data based on phone&#x27;s association with system &gt; Ask for help Work Objects:</td><td></td><td>o See user name, and system associated with</td></tr><tr><td>Associated system User Constraints : • This is a telephone; must designate a button for help. • Need to integrate</td><td>flow to another place</td><td>&gt; Get guru help</td><td>&gt; See system&#x27;s history • Enter comments on problem or request, including what has been tried • Enter solution to problem</td></tr><tr><td></td><td>function</td><td>o Update probiem history • Assign self as owner next level support)</td><td>• Reassign owner (to specified person or to</td><td></td><td>&gt; Get guru help Work Objects: System</td><td>Problem history</td><td></td><td></td></tr><tr><td></td><td>function</td><td></td><td>assigned) • Mark problem done</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>and phone numbers.</td><td></td><td>automatic</td><td>• Cancel probiem o Log ticket into system (when assigned)</td><td>o Display time spent on problem (when</td><td></td><td></td><td></td><td>Comment</td></tr><tr><td></td><td>database of users, history,</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>• Pause timing Restart timing</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Work Objects:</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>4. Guru Help</td><td></td></tr><tr><td></td><td></td><td></td><td>User</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>System Problem</td><td></td><td></td><td>Tracks and allows user to find</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>problem solutions</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Functions:</td><td></td></tr><tr><td></td><td></td><td></td><td>Owner</td><td></td><td></td><td>• See problem topics</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>• See names of other helpers</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>• Specify type of problem you</td><td></td></tr><tr><td></td><td></td><td></td><td>Issues :</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>What if the help person isn&#x27;t there?</td><td></td><td></td><td>want to find</td><td></td></tr><tr><td></td><td></td><td></td><td>• How do people see all their problems?</td><td></td><td></td><td>• Search</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Roles :</td><td></td><td></td><td>o View search results</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Work Objects:</td><td></td></tr><tr><td></td><td></td><td></td><td>• This place will be used by both first-line</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Problem</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>helper and responsible person.</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>System</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Helper</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>place to do work</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Hci l il il  arign.

Redesigned scripts drive the development of the User Environment design. The team walks each script extracting implications for the system design. They define places in the system to support each work activity, and define system function, work objects, and flow between places. As each redesigned script is fed into the User Environment design, a system structure emerges that supports all the work described in the different scripts. Because it is represented in a single model, the team can ensure that the system structure is coherent and consistent.

The User Environment design supports team discussions about whether the system supports work well—whether it provides the right function and the right organization of function for a smooth flow of work. It allows the team to check the system against the work described in consolidated and redesigned models: whether the system provides adequate support for a role, whether it provides for a particular communication path, whether it inhibits an influence from the context model, and whether it accounts for the constraints of the physical model. Actual and consolidated sequences can be run through the User Environment to ensure that it supports the real work of individual users.

The User Environment model is an ideal method of planning and communication with other design teams. In one company, two teams with overlapping responsibilities had been arguing about who should ship what. They used their User Environment models to describe their own plans, see and resolve the overlapping designs, and reassign parts of the new, coherent design to each team amicably. In another, a team used the User Environment to define the system they wanted and evaluate off-the-shelf software to see which met their needs best. Others have used the User Environment to define whole families of applications and how they should work together. By making the issues of structuring systems for the users explicit, the User Environment model makes all these conversations easier.

## Iteration with Paper Mockups

Once a team has a base User Environment design, development proceeds through rapid iterations with the user. The team moves quickly to test the partial design with paper prototypes. The first goal in prototyping is to test the User Environment design—to see whether the basic structure and function are useful—and to collect detailed data in the area of work the prototype supports. Structure can be tested through simple mockups with almost no UI detail, for example by mapping places in the system to windows and functions to menu items. The team takes the prototypes to the users' workplace and asks them to pretend it is a system and to work with it. Users do not give us their opinion—they simulate doing one of their own tasks using the prototype, so they can react as they would to a real product. Interviewers observe and probe in the same way as a contextual interview. They do not have to tell their users what level of detail to respond to—the roughness of the prototype does that.

Initially the prototypes are very rough, and interviewers encourage users to explore, trying to accomplish a task of their own. When they ask if the system does something, interviewers design on the spot: "Yes. How would you expect it to work? Show me." The user sees that the design is incomplete and open to change, and is drawn into the design conversation. (This requires members of the design team to run the interview, to respond appropriately and to design with the user.) The team soon discovers whether the initial structuring of the work in the User Environment design makes sense. As the User Environment design stabilizes, the focus of the interview shifts to the user interface. The team builds more careful prototypes, and in customer interviews asks users to live with the limitations of the system as designed. Finally, it becomes useful to build and test running prototypes that can evolve into the real system.

Iterating with customers early, before the design is complete, is an effective way to keep the design on track. Any design proceeds best if the large structure is defined before detailed design, because changes in the overall structure will force changes to the detail. This is hard most engineers would rather get all the details right before testing anything. Quick iteration with the user checks the structure before much time has been wasted designing detail that might change. Because some parts of the system will be tested before others, they will be fully designed and more stable, which is also an advantage—it allows development to proceed in stages, taking a chunk of the system at a time.

Frequent iteration keeps the team focused on the customers and their problems, not on each other. The longer the team works on the design without feedback, the more committed they will be to that design, and the more they will resist discovering that it is wrong. Interestingly, iteration with customers also keeps the team creative— when our teams get bogged down, it's usually because they've lost contact with the customer (Beyer 1994). When they mock up the ideas they developed from data and take them out, suddenly they get moving again. We keep prototypes in paper until the level of UI design is so detailed that paper cannot test it. Building prototypes on the computer before this is not only extra work, it's actually counter-productive. Not only do the team members get overinvested in their design, but users invariably respond to details of the look and the layout. If we present a hand-drawn prototype on paper, they respond to the structure and function in the system.

As a design process, Contextual Design is based on a few overriding principles: that customer data is the only sound basis for design; that the cognitive process of design is enabled by supporting systemic thinking and providing concrete models that create clean design conversations; and that the design process must support face-to-face team design and coexist with the host organization. We have used these principles repeatedly throughout Contextual Design to create a process that is effective at designing systems, and that supports the people who must live in it.

## CUSTOMER-CENTERED DESIGN IN THE ORGANIZATION

In this chapter, we've presented a summary of how Contextual Design is structured and why it is structured as it is; but any process needs to be adapted and adjusted to meet the needs of a particular project, and Contextual Design is no exception. In fact, it's been called a backbone for organizing the use of a whole range of techniques for customercentered design. Depending on project goals and context, team membership and application of techniques would change. For example, Contextual Design is not necessarily participatory in the full sense of the term. It does not require that customers be a part of design in the way that Participatory Design specifies. However, Contextual Design can be used to support a Participatory Design project:

1. Define a team consisting of designers and customers, including users of the proposed system.

2. Use Contextual Inquiry to gather information about the work domain. Interview all classes of customers. All members of the team (including customers) conduct interviews. Interview the customers on the team at work if their work needs to be understood.

3. Consolidate work models and build an affinity. Bring in additional customers to help, especially on the affinity. Hold sessions for people in the department to walk the models and comment on them. Use the comments as a focus for future interviews.

4. Brainstorm and redesign with additional customers not on the design team. Envision process changes as well as system behavior. Run several envisioning sessions with different sets of customers. Use the modified Pugh matrix to merge alternatives and build a single vision.

5. Build a User Environment design and mock it up. Test it with customers throughout the organization.

We have followed variants of this outline on several projects with great success. The customers are involved throughout the process, and become enthusiastic supporters of the project. One IT manager even told us how unusual she found it to have her clients eager to have her work with them, instead of viewing her organization as an obstacle.

Anyone introducing any sort of customer-centered design should be aware that success will lead to organizational change. CACM 1995. Organizations are not currently structured to facilitate customer-centered design or to take best advantage of it. As the approach becomes more widespread, the mismatch between the new and old ways of doing business will cause complaints. These complaints reflect real problems, but will tend to go away as the new approach becomes institutionalized and tailored to the culture.

Setting up customer visits is hard. Most organizations have procedures to make field testing easy. Interviews are a far smaller logistical problem, but currently the full burden of arranging them falls on the design team. We need channels supporting this new relationship with the customer, particularly in those organizations developing commercial products.

The new approach to design implies a new relationship between marketing, engineering, and the other organizations that help ship products. People are not yet comfortable with their new roles. Marketing is responsible for bringing their focus on the business to the team, but is not unilaterally deciding on what to build. Engineering brings technology expertise to the room, but they are not unilaterally deciding what to build either.

Teams using the new approaches still have to interact with other teams and managers. who are used to the old ways. When teams are expected to produce working documents as part of design, they still need to create those documents expected by the organization, whether or not they duplicate the team's internal design documents. Our teams have used the User Environment to generate requirements documents, specs, and UI designs in the form expected by their organizations. Over time, statements of"user needs,""requirements,""specifications," and other milestone deliverables may start to conform to the structure the team had to create anyway, as part of design. The overhead of documenting and reporting would then lessen, replaced by processes that record real work as it happens.

After customer-centered design becomes common, but before it becomes institutionalized, bringing new people up to speed is a problem. Training needs to be created for new people and for teams who want to start using the new approach. If they are not trained, teams will tend to call whatever they are doing with the customer“Contextual Inquiry" or "customer-centered design," even if it follows none of the principles.

Customer-centered design is a new approach to designing software, and the processes are still evolving. The specific techniques used at any point are always open to modification and adaptation, just has we have borrowed from many places to create Contextual Design. The definition of the new process will be driven by principles of how to support design well; it will also be driven by the restrictions and requirements of the host organization. All the writers in this book are practicing the fine art of balancing these two sets of requirements. On the one hand, we cannot push the organization so hard that the process falls apart; on the other, we cannot limit what we do so much that the process is not useful. The happy medium is always unclear and constantly shifts as we seek the best process for each situation. We wish the reader well in striking the right balance in their own organizations.

## NOTES

1. Throughout this paper, "user" refers to those who actually interact with a computer system. We use "customer" as a more general term to indicate those who are affected by a system, whether they use it themselves or not. This includes users, managers of users, buyers, those who use a system's results, and those who provide input to a system.

2. For other discussions of representing work, see the September 1995 issue of Communications of the ACM (CACM 1995).

## REFERENCES

"Requirements Gathering, The Human Factor." Communications of the ACM, May, 1995. vol 38, No 5. This is a special issue devoted to

the organizational changes resulting from new customer-centered design practice.

"Representations of Work." Communications of the ACM. 38(9). This is a special issue discussing different approaches towards representing customer work.

Beyer, H. 1994. "Calling Down the Lightning." IEEE Software. September 1994, Vol 11 No 5. p. 106.

Beyer, H. and Holtzblatt, K. 1995. “Apprenticing with the Customer." Communications of the ACM 38(5), 45–52.

Brassard, M. 1989. Memory Jogger Plus. Methuen, MA: GOAL/QPC.

Carter, J., Jr. 1991. "Combining Task Analysis with Software Engineering for Designing Interactive Systems." John Karat (Ed.), Taking Software Design Seriously. NY: Academic Press, p. 209.

Deming, W.E. 1982. Out of the Crisis. Cambridge, MA: Massachusetts Institute of Technology, Center for Advanced Engineering Study.

Ehn, P. and M. Kyng. 1991."Cardboard Computers: Mocking-it-up or Hands-on the Future." J. Greenbaum and M. Kyng (Eds.): Design at Work. Hillsdale, NJ: Lawrence Earlbaum Associates, p. 169.

Keller, M. and Shumate, K. 1992. Software Specification and Design. New York: John Wiley & Sons, Inc.

Kyng, M. "Designing for a Dollar a Day." Proceedings of CSCW'88: Conference of Computer-Supported Cooperative Work (pp. 178-188). New York: Association for Computing Machinery.

Holtzblatt, K. and Jones, S. 1993. "Contextual Inquiry: A Participatory Technique for System Design." Aki Namioka and Doug Schuler (Eds.), Participatory Design: Principles and Practice. Hillsdale, N.J.: Lawrence Earlbaum Associates.

Holtzblatt, K. 1994. "If We're a Team, Why Don't We Act Like One?". Interactions. July 1994, Vol. 1 No. 3, p. 17.

Ishikawa, K. 1985. What is Total Quality Control?. Englewood Cliffs, NJ: Prentice-Hall.

Martin, J. and Odell, J. 1992. Object-Oriented Analysis and Design. Englewood Cliffs, NJ: Prentice-Hall.

Muller, M. 1991. "PICTIVE—An exploration in participatory design." Human Factors in Computing Systems Proceedings of the CHI'91. ACM, 225–231.

Pugh, S. 1991. Total Design. Reading, MA: Addison-Wesley Publishing.

Seaton, P. and Stewart, T. 1992. "Evolving Task Oriented Systems." Human Factors in Computing Systems. Proceedings of the CHI'92. Monterey, California: ACM.

## Index

![](images/83f6c3f20d6c0aadb018169ac59b1a1667bf724731e05dc7ab43c08c1c43cd5b.jpg)

Page references followed by lowercase f indicate illustrations, while references followed by lowercase t indicate material in tables.

## A

action graphs, 103–104   
action research, work-oriented, 286   
affinity diagrams, 302, 303, 318–319 in chromatographic equipment development, 129-130, 131t in clinical workstation design, 239-240 in consumer software design, 216, 220, 222–223, 224, 225 in ultrasound equipment development, 171-172 "walking the wall" of, 240 in WordPerfect design, 202, 206f   
agenda, 131   
aided recall questions, 46   
Allen, C., 291   
ALL-IN-1-Integrated Office System, 58   
Alpine Media, 269   
apprenticeship user-designer model, Contextual Inquiry, 308–309   
Arizona, University of, 1, 2   
artifact models, 317–318   
artifacts, 135, 270-271, 309 consumer software design, 222 ultrasound equipment development, 170,172

with usability roundtables, 257 artifact walk-throughs: Hewlett-Packard family life study, 146,154 Teamlink for Macintosh, 70, 86 ATL Inc., 157–158 ultrasound imaging system development at, 160–175 audio tapes: clinical workstation design, 234 with Contextual Inquiry, 309–310 Hewlett-Packard family life studies, 152 WordPerfect design process, 201 August, J.H., 278

## B

Bauersfield, Kristin, 177   
beta testing, 273   
Beyer, Hugh R., 278, 301, 303   
BJC Health System, 230, 231–232   
Bloomberg, J., 287   
Bodker, S., 289   
Bravo, Ellen, 295   
Brigham Young University, 35, 269   
Brown, Diane S., 157   
bulletin boards, 209   
Butler, Mary Beth, 249   
button bars, 77

## C

cardiology, ultrasound imaging system development, 164, 171   
CARD method, 17, 18–20, 30–32 applying, 21–25 data analysis, 25–29   
Carleton University, 1, 2   
Carlshamre, Pär, 94   
Carr, Rebecca, 17   
case-focused questions, 41–42   
category label questions, 43–44   
category member questions, 44   
chromatographic equipment development, 125, 127–143   
Claris Corporation, 177-178 field techniques application at, 179-195   
client-centered design, 273–276. See also user-centered design   
client-server applications, 114   
clinical workstation, 229-247   
cluster analysis, 192   
codiscovery, 251   
cognitive anthropology, 38–39   
cognitive psychology, 37   
collaborative analysis, 17–18   
Collaborative Analysis of Requirements and Design (CARD), see CARD method   
Collaborative Approach to Usability Engineering, A, 94   
collaborative query clarification, 20   
competition, 145   
competitive benchmarking, 66, 68   
competitive studies, 251   
Computer Human Interaction (CHI) Conference, 194, 303   
Computer Professionals for Social Responsibility (CPSR) Workplace Project, 294–295   
computers, increased use in workplace, 295   
computer support for cooperative work (CSCW), 287   
conceptual design, Delta method, 105-106   
concurrent think aloud questions, 46–47   
condensed ethnographic interviews, 179. 181, 186–187, 188, 190–191, 193   
consolidated models, 319-322 WordPerfect design, 203   
context, 292   
context models, 312–313 clinical workstation design, 237, 239f consumer software design, 222–223 WordPerfect design, 202   
Contextual Inquiry, 278. See also ethnographic interviews/methods; field research affinity diagrams, see affinity diagrams applications: chromatographic equipment development, 125, 127–143 clinical workstation design, 230, 233-243 consumer software design at Microsoft, 216, 217-227 Hewlett-Packard family life study, 146,155 Lotus Development, 250-252 Teamlink for Macintosh, 65 WordPerfect design, 197, 199, 201-205 apprenticeship user-designer model, 308-309 background, 302–304 as "bottom up" approach, 37 defining projects, 304–307 design room, 322–323 lack of timing benchmarks, 246 paper prototyping with, 328–330 as participatory design, 292–294 process of, 308–310 interpretation session, 310-311 work model consolidation, 319–322 work modeling, 311-312 redesigned scripts, 323–325, 324f, 326 systemic design, 323–325 User Environment model, 204–205, 303, 325-328   
contrast questions, 44   
cooperative design, 289–291   
cooperative prototyping, 289, 290   
Corel Corporation, 197 WordPerfect design at, 197–212   
CPSR Workplace project, 294–295   
cross-examination, 47   
cross-functional teams, 302, 305-307 applications: chromatographic equipment development, 125, 126, 127–143 Teamlink for Macintosh development, 60–61, 63 WordPerfect design, 197, 199, 207-209 optimum size, 306–307   
cross-validation, 66   
CSCW (computer support for cooperative work), 287   
customer-centered design, see usercentered design   
customer day, 66   
customer partners, 65   
customer support system, WordPerfect, 198   
customer surveys, see user surveys

## D

data-driven design decisions, 4   
Deal, The, as metaphor, 121, 123   
Delphi, 205   
Delta method, 91-111 development, 92–94 integrating within customer organizations, 97–99 purpose, 94–96 role in design process, 96 theory and practice, 99–110   
Delta Method Handbook, The, 94   
demand pull, 62   
DEMOS project, 286   
design: client-centered, 273–276 data-driven, 4 iterative requirements, 62–63 system-centered: traditional method, 272-273

user-centered, see user-centered design user-friendliness, 146 design metaphors, 62 design reviews, 209 diagnostic radiology workstation, ethnographic task domain investigation, 1-14 Digital Equipment Corporation, 58 Teamlinks for Macintosh development 57-87 directed contrast questions, 44t direct language questions, 41t, 42 directory assistance operators, task analysis, 18–32 domain-specific knowledge, 50 domain-specific language, importance of using, 39, 42, 50, 311 downsizing, 125-126 Dray, Susan M., 145 Dun & Bradstreet Software Services, Inc., 114 dyadic contrast questions, 44t

## E

ease of use, 273   
Ehn, Pelle, 285-286   
Ericsson Infocom Consultants AB, 92   
ethnographic interviews/methods, 36. See also Contextual Inquiry; field research applications: chromatographic equipment development, 132-133 clinical workstation design, 233-235 condensed interviews at Claris, 179–181, 186–187, 188, 190–191, 193 consumer software design, 220-223 Delta method, 91 diagnostic radiology workstation: stream-of-behavior chronicles, 1-14 Hewlett-Packard family life study, 146,149–155   
ethnographic interviews/methods (cont.) mobile sales automation workstation development, 116-117 ultrasound equipment development, 162-168 WordPerfect design process, 201 approaches, 276-279, 287-289 design process relevance, 288 expert knowledge and, 37–38 future trends, 279–280 hierarchical outline, 168, 169f potential errors, 38–39, 50 tacit knowledge, 38, 50 as "top-down" approach, 36–37 work/task analysis strategy, 35, 39-49   
ethnography, 1, 2–3, 35–36, 179–180 challenges, 271–272 overview, 269–272   
European families, 149, 151–152, 154   
example questions, 41t, 42   
expertise, 37, 50   
expert knowledge, 37–38, 50   
expert systems, 36   
extended user interfaces, 95

## F

family life studies, 147–155, 215   
family market, 145   
field research, See also Contextual Inquiry; ethnographic interviews/methods applications: Claris Corporation: condensed-time frame methods, 179-195 consumer software design at Microsoft, 215–227 sales automation workstation, 113-123 Teamlink for Macintosh, 60, 61, 86 ultrasound equipment development, 157, 160–175 Delta method, see Delta method in ethnography, 287   
flow models, 314, 315f

clinical workstation design, 236–239, 238f consolidation, 320 consumer software design, 222–223, 224,225 WordPerfect design, 201–202, 203f focus, 293 focus groups, 198, 274, 288 ultrasound equipment development, 160-161 focus statements, 129–130, 131t Ford, John M., 269 Freelance Graphics, 250 French families, 149, 151 functional departments, shift away from, 126 future workshops, 289

## G

Georgetown University, 1, 2   
George Washington University, 1, 2   
German families, 149, 151–152, 154   
GOMS/CPM modeling, 18, 27, 28f, 30   
Gottesdiener, Ellen, 297   
Graf, Robert C., Ph.D., 113   
grand tour questions, 40–41   
Gronbaek, K., 289   
grounded design, 62   
guided questions, 41

## H

Halgren, Shannon, 177   
Hewlett-Packard, 146 family life studies, 147–155   
hierarchical outline, 168, 169f   
Holtzblatt, Karen, 278, 292, 301, 303   
home market, 145   
Huntwork, Paul K., 57   
hypothetical-interaction language questions, 41, 42

## I

IBM,230 imaging systems, ultrasound, see ultrasound imaging systems

InContext Enterprises, Inc., 301   
information technology sector, 145   
interactive feature conceptualization, 183–184, 191, 193, 194   
interpretation session, Contextual Inquiry, 310–311   
interpreters, 135, 165   
ITYP venture, 92

## J

Joint Application Design (JAD), 278   
Joint Application Development, 297   
Jones, S., 292, 302, 303   
Juhl, Dianne, 215

## K

knowledge-based expert systems, 36   
knowledge work, 29   
knowledge workers, 29–30   
directory assistance operators as, 25   
Knox, Steve, 303   
Kodak, 230   
Kyng, M., 289

## L

liaisons, 208   
lifecycle approaches, 19   
Linköping University, 92   
Lotus 1-2-3, 250   
Lotus Development, 249, 250 Contextual Inquiry at, 250-252 usability roundtables at, 249, 250, 252-267   
Lotus SmartSuite, 250   
low-fidelity prototyping, 251

## M

Make It Fit feature (WordPerfect), 209–210, 212,297   
Management Science America, Inc., 114   
market research departments, 146   
McCormack and Dodge Corporation, 114   
medical imaging systems, ultrasound, see ultrasound imaging systems   
medical market, 157 clinical workstation development, 229-247 radiology workstation task domain investigation, 1-14 ultrasound imaging system development, 160-175   
mental work, 20   
mentors, 208–209   
Microsoft Corporation, 113, 114 consumer software field-oriented design at, 215–227   
mobile sales automation workstation development, 113-123   
mock-up designs, 289, 290   
model sharing, 209   
moderators: focus groups, 274 usability roundtables, 258–259   
Mrazek, Deborah, 145   
Muller, M.J., 17, 18, 278–279   
Muzzy, Douglas W., 57

## N

Namioka, Aki Helen, 283   
native language questions, 41t, 42   
naturalistic observation, 146   
Netscape Corporation, 177   
notes, 310   
Nygaard, Kristen, 285

## 0

objects, see work objects   
observations, 237 naturalistic, 146 passive video observation, 181–182, 187,188,194   
open houses, 209   
organizational games, 289–290   
organizational reengineering, 126

## P

PANDA (Participatory ANalysis, Design, and Assessment), 19 paper prototyping, 328–330

participatory design, 19, 277, 330. See also CARD method; Contextual Inquiry; ethnographic interviews/ methods; PICTIVE method approaches to, 287–294 features, 283–285 history, 285–287 U.S. use of. 294–298   
Participatory Design Conference 1990. 283,294   
partnership, 292–293   
passive video observation, 181–182, 187 188,194   
PerfectOffice 3.0, 210   
personal experience questions, 41, 42   
physical models, 313–314 WordPerfect design, 202, 205f   
physician's clinical workstation, 229-247   
PICTIVE method, 17, 18–19, 20–21, 30–32,278–279 applying, 21–25 data analysis, 25–29   
Pietras, Christine M., 57   
Plastic Interface for Collaborative Technology Initiatives through Video Exploration (PICTIVE), see PICTIVE method   
process knowledge, 38, 45–48   
Product Development Partnerships, 138-139.140   
Project Spectrum, 229–230, 232–235, 246   
protocol analysis, 46   
prototyping: applications: chromatographic equipment development, 130, 133–134 consumer software design, 216–217 Delta method, 91, 108–109 Teamlink for Macintosh, 60, 61, 70, 77-82 WordPerfect design, 205 with Contextual Inquiry, 328–330 cooperative, 289, 290 low-fidelity, 251

rapid, 275 Pugh matrix process, 323, 325

## Q

Quality Function Deployment (QFD), 67   
quantitative research, 61-62   
questionnaires, see user surveys   
questions: think aloud protocol generation, 46–48, 47t work object identification, 41t, 41–43 work object relationships, 43-45, 44t   
QuickTasks feature (WordPerfect), 210

## R

radiology: ultrasound imaging system development, 164, 171 workstation, ethnographic task domain investigation, 1-14   
Ramey, Judith, 1   
Rantzer, Martin, 91   
Rao, Christopher, 283   
rapid application development (RAD), 296-297   
rapid prototyping, 275   
reciprocal evolution, 291-292   
redesigned scripts, 323–325, 324f 326   
redesigned work models, 204, 207f   
requirements document, 231, 241, 243, 244f   
retrospective accounts, 309   
retrospective thinking aloud protocol, 6, 46   
Robinson, Carol, 1   
Rowberg, Alan H., 1   
Rowley, David E., 125

## s

sales automation workstation, 113–123   
SBC Corporation, 230   
Scandinavian Airlines, 286-287   
Scandinavian design, 276–279, 285   
scenario development, 48, 49   
separation of concerns, 63   
sequence models, 314, 316f

clinical workstation design, 236, 237f consumer software design, 222–223 WordPerfect design, 202, 204f   
SIGCHI, 294   
Silver, 297   
simplification bias, 38–39, 50   
SIMULA, 285   
SmartSuite, 250   
socio-tech, 297   
software, for support of ethnographic data analysis, 279–280   
software crisis, 60   
software design, see design   
Special Interest Group for Computer Human Interaction (SIGCHI), 294   
step-wise refinement, 63   
stimulated recall, 6   
stream-of-behavior chronicles, 1-2, 3–4, 5,6-7   
structured outlines, 47   
subject matter experts, 19, 30   
super graphs, Delta method, 104   
Swedish Graphics Union, 286   
Swedish National Board for Industrial and Technical Development, 92   
system-centered design, 272–273   
system definition, Delta method, 100-101

## T

tacit knowledge, 38, 50   
Tahir, Marie, 249   
task analysis, see work/task analysis   
task-related questions, 41   
Teamlinks for Macintosh development, 57-87   
Telia AB, 97   
Telia NM, 97–99   
The Deal, as metaphor, 121, 123   
thinking aloud protocol, 251, 274 concurrent think aloud questions, 46-47 retrospective, 6, 46   
time, as element of study, 170–171   
ToolBook, 205   
top-down development, 63

Total Quality Management (TQM), 305   
training, 142   
translation competence, 39, 50   
Tudor, L.G., 18   
typical questions, 41

## U

ultrasound imaging systems, 157–159 development at ATL Inc., 160–175   
usability engineering, 91   
usability goals, Delta method, 107–108   
usability labs, 274–275   
usability roundtables, 249, 250, 252–260 benefits, 257 case study, 260–267 future developments, 260 limitations, 258–259   
usability testing: Claris Corporation, 178 in consumer software design, 216–217 Delta method, 109-110 mobile sales automation workstation, 114-123   
use questions, 41, 42   
user analysis, Delta method, 101–102   
user-centered design, 2, 62, 330–332 Contextual Inquiry and, 227 Hewlett-Packard, 146-147 move towards, 273–276 ultrasound equipment development, 160-175 work/task analysis, see work/task analysis   
User Environment model, 204–205, 303, 325-328   
user-friendly design, 146   
user interfaces, 94–95   
user profile, clinical workstation design, 237-238   
user surveys, 275–276, 288 Teamlink for Macintosh development, 60,65   
U S West Communications, directory assistance operator task analysis, 18-32   
UTOPIA project, 286

## V

Varian Chromatography systems, 125, 126-127 chromatographic equipment development at, 127–143   
Vector Comparative Analysis (VCA), 63, 66–67,68–69,82   
video logging software, 168   
videotaping: with CARD and PICTIVE method, 24 chromatographic equipment development, 130–133, 135, 139 "surprise attack" approach favored, 130 Contextual Inquiry, 309 Hewlett-Packard family life studies, 151,152 mobile sales automation workstation development, 117, 122 passive observation method at Claris, 181–182, 187, 188, 194 stream-of-behavior chronicles: radiology activities, 1–2, 3–4, 5, 6–7 ultrasound equipment activities, 161, 165–166, 167–168, 173

## W

"walking the wall", of affinity diagrams, 240   
Washington, University of, 1 Medical Center, 5–6   
Washington University School of Medicine, 229–230, 232   
Windows (Microsoft Windows), mobile sales automation workstation development, 113–123   
Wixon, Dennis R., 57, 278   
Wood, Larry E., 35, 269, 297   
WordPerfect, 197–198 user-centered design of, 198–212   
WordPro, 250   
workarounds, 172, 293   
worker empowerment, 297   
workflow automation, 77   
workflow models, see flow models   
work models, 311–312. See also specific work models; work/task analysis consolidation, 203, 319–322 development, 45 validating, 48-49   
work objects: identification, 35 identification questions, 40–43, 41t, 50 knowledge, 38 relationship questions, 43–45, 50   
work-oriented action research, 286   
Workplace project (CPSR), 294–295   
work-related language, importance of using, 39, 42, 50, 311   
workstation design: clinical, 229–247 diagnostic radiology, 1–14 mobile sales automation, 113–123   
work/task analysis: Delta method, 101–104 directory assistance operators, 18–32 ethnographic interview strategy for, 35,39–49 mobile sales automation workstation, 117-119 underestimating expertise complexity, 37