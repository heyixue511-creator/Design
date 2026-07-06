# Using Data to Drive Design

12

Te've defined a new process step, work redesign, and we've located it in the systems engineering process. It's the job of the work redesign step to invent the new work practice that a corporation will deliver by building systems, offering services, and redesigning procedures. Invention of work practice is based on a foundation of customer data, driven by knowledge of the different available technology and how to apply it to the design problem.

There are all kinds of technology a team might take advantage of—hardware, software, delivery mechanisms, service possibilities, and

process design, to name just a few. But there's one critical kind of technology that a team must have yet is not commonly available. The team's primary task is to design work practice—which means that knowing how to manipulate work practice is a central skill for the team. The “technology” of work practice—

The critical team skill: how to see and design work practice

how to see issues in the data, how to think about redesigning work to address the issues, different process options for redesigning work and their benefits and drawbacks—these are necessary skills for a design team. Yet they are skills most teams don't have.

There are two ways to learn how to see work structure. One is inquiry into the consolidated models. Inside each work model are hid-

den issues and insights that will inform the design process, but it takes knowledge and inquiry into the models to pull the issues out. The second way to see work structure is to look at work that has the same structure or pattern as the work you’re studying, but that is more familiar or transparent. By using this

See work structure in consolidated models and metaphors

work like a metaphor, drawing parallels between it and the work you care about, you see issues and structure you might not think about otherwise.

What follows suggests some ways to look at consolidated models and see the issues they suggest. Then we'll discuss metaphors and how to use them. These ideas will get you started thinking about how the work models might suggest design possibilities.

## THE CONSOLIDATED FLOW MODEL

The consolidated flow model ties together much of the critical information about the customer. It's your best starting point for understanding work practice and driving design. The flow model shows the roles people play and how they map to individuals; looking at the roles, and the flows that support them, reveals communication patterns and problems in the work.

Every mapping of roles to individuals raises unique problems. When too many roles are assigned to one person, that person is over-

Look at how roles map to people and organizations whelmed and unable to focus on one thing. When they are split up among many people, then those people have to coordinate to get the job done. Departments often oscillate between these extremes: overcentralization causes a bottleneck so they diver-

sify, then when they realize that diversification caused communication problems, they recentralize. But any arrangement of roles creates its attendant problems. It's our goal to build the solution to the problems into the work process rather than search for the perfect role structure that solves all problems.

With that introduction, let's look at some of the issues associated with roles and mapping them to individuals. To facilitate discussion, we'll give each issue a snappy tag and then discuss its implications.

## ROLE SWITCHING

Everyone plays more than one role. Each role is a coherent set of tasks and responsibilities that hang together organically. Switching roles is like switching hats; it means putting aside an entire way of thinking and set of concerns, and taking up another. Sometimes the new role just continues the work, as when a developer who does her own testing starts testing a module. But sometimes the new role is an interruption, in which case the whole context of the interrupted task has to be stashed away to be recovered later, and a new context brought out to worry about. Every transition between roles is an opportunity to forget something, to allow an issue to fall through the cracks.

![](images/8b8b601b6adb9fb4922b11401ae0e402a3ddd44780f023cd97934947472e658b.jpg)  
FiGuRE 12.1 Two roles played by a scientist (the two roles are shaded alike, indicating that the same person plays both). Switching between roles is part of the scientist's life, but do the tools support putting down one role and taking up another?

Consider the scientist who also develops methods: formal procedures for doing an experiment (Figure 12.1). He's in the middle of

defining a method when a test run completes. This forces a switch from the Method Developer role to the Experimenter role. He may choose to analyze the results immediately or save them for later, but he must at least clean up after the test. He has to save everything about the method to one side in such a way that he can resume the work later.

Role switching creates opportunity for something to fall through the cracks

Role switching suggests issues a system could overcome. Do people have to reenter the same information in each of their different roles? If the roles are played by more than one person, redundant data entry is wasteful, but if the same person reenters the same data, it's exasperating. A scientist who creates a method shouldn't have to reenter information about the method in order to use it. Can systems share data to eliminate reentry?

Do the systems in place support the movement from role to role? Are they completely disjoint systems, so switching roles means starting up an entirely new interface? Are some roles not supported at all, so users are cast back on their own resources for part of the job? The developer who finds herself having to switch back to the command line and homegrown scripts to run tests won't think she has a complete development environment. Look for ways to integrate systems so they provide seamless support for the work.

And do the systems support putting a role aside and coming back to it later by saving the context of the task? Do the systems allow the task to be inter-

rupted? What context does the user need saved? Saving context doesn't have to be complicated—Microsoft Word saves your last position in a document so you can pick up right where you left off.

HINTS

Eliminate redundant data entry

• Support movement from role to role

• Support consistent interfaces for the different roles

• Save state to support interruptions

## ROLE STRAIN

When people play too many roles, they get overwhelmed. They are trying to wear too many hats, each of which has its own imperatives, its own concerns, and its own demands. There are just too many roles to switch between. Any small business person is plagued with this problem, as are secretaries. Dual-income families have it in spades. The constant switching increases the demand on the person and increases the chances that they'll lose track of things. Furthermore, the roles themselves may call for different skills or meeting different goals.

The person who has the primary responsibility for running a household provides the classic example of role strain (Figure 12.2). Each different role has its own needs and tasks, its own demands on time and concentration. But when there are so many, the people are always juggling them, trying to give enough time to each that nothing important falls through the cracks.

When you see people under role strain, look for ways to alleviate it. Are there roles that could be totally automated, or substantially supported? Online shopping eliminates the Shopper role, reducing the number of roles people have to juggle. Failing that, can you keep much of the information needed by a role in the system, so people don't have to rely on their own organization? If you capture the issues a Worry Keeper tracks, and remind him of things he might forget, it will be easier to play that role. Or it may be possible to move a responsibility or a whole role to another person. In this way, the advent of word processing moved most

![](images/c0d29e51f700ff75a44f05c5a366cc5219c0f757166a02e8b455a2d3771c849c.jpg)  
-ie  e ae ye haed she e e  5oa euus-

of the document production role from secretaries to professionals, giving the professionals more control and reducing the cycles of passing the document back for correction.

## HINTS

• Automate or eliminate roles

• Support and organize roles

• Move responsibilities or roles to other people

## ROLE SHARING

When multiple people with different job responsibilities all play a role, they are role sharing. Doctors, nurses, and technicians may all take

samples from a patient (Figure 12.3), but they'll do it differently. Doctors draw samples in the context of a patient consultation; lab technicians don't have any other contact with the patient. The different people have very different skills and expectations: doctors assume their time is at a premium and have no

patience for dealing with computers, but it's the lab technician's job to make sure all data is entered and is correct. And the context of use is different: doctors will do the work in a consulting room, while lab technicians often have stations set up especially for taking samples.

So how should the system respond? Recognize the different needs and characteristics of the different users. Even though it's one role and

one task, don't assume one interface will fit all users. Design for the most demanding user, and create a system that is cleaner for everyone. Doctors may not be willing to put up with a complicated interface, but an interface that works for them may be an improvement for other types of users as well. Doctors may need a portable system with pen input that they can take with them on their rounds. Technicians may be able to use a desktop interface and may be willing to do keyboard entry. But they'll need the system to integrate with the rest of their work, including sending the sample to the lab for test. Also, look to see whether all users need the same information. The doctors may need less detail than the tech, even though they may share data in the underlying system.

![](images/74679a4f456d4c2c5fe9edfb13102ae6587892cdcae3ac97325daa1c5a62b318.jpg)  
FiGuRE 12.3 A role annotated to show how individuals play the role. The shade shows that nurses play the role, the pattern shows that technicians do, and the dark outline shows that doctors play the role.

HINTS

• Tailor the interface style to the user

• Tailor the data presented to the user

• Share data internally across the types of user

• Fit with the rest of the roles each type of user plays

## ROLE ISOLATION

Any of the above problems may be resolved by separating roles cleanly among individuals. But that just raises a new set of issues. Each role has a coherent job to focus on, but it needs to hand off work to other roles and communicate the context of the work—the roles depend on each other to get the job done. When people don't do a job, they don’t know what's involved in doing it or why it's hard, and they often end up blaming the people responsible for it for not doing it well. It's like a manufacturing line—everyone understands their own part of the job and blames the other parts for not producing the materials or using the results properly.

Division of labor doesn't eliminate the need to coordinate

![](images/37e22fad39f333aebf0670da92d1786c5206038d937256fc7ede38de9fbb910f.jpg)  
FIGuRE 12.4 Shopping as a role isolated from the Head Chef. The Head Chef or Cook knows what the meal is and what ingredients will work. The Shopper only knows what they've been asked to buy. So if the list doesn't specify the exact brand and size, or if the Shopper can't get the exact item and has to substitute, they don't get the right thing.

Sending someone else to do your shopping invariably creates role isolation (Figure 12.4). If the store didn't have something on your list,

your shopper has to choose whether.to substitute something else or come back with nothing. How can they decide which to do? They'll only know which to do if they know what you want the items for and how they fit together. Otherwise, they'll come back with half a meal. So each role has to have enough of

the whole work context so they can really do their tasks on their own.

When roles get too isolated, and it becomes clear that communication is a major problem, organizations sometimes create liaison roles

The system's job is to carry context between roles

whose sole job is to maintain communication. A typical situation for IT departments is to have the business customer communicate requirements through a customer representative, the person on the customer side chartered to say what they need (Figure 12.5).

![](images/8c0d27428152379952db2c05f00687dcc266032177c5958db18eb1774b8d67f8.jpg)  
FiGuRE 12.5 Role isolation at work. Two new roles have been created to manage the communication between the business and the developer.

These requirements are communicated to an analyst, the person on the IT side chartered to find out what customers need, so the developers can build it. These intermediary roles exist only as an attempt to overcome role isolation.

Deal with role isolation by addressing the communication problem. Can you capture and communicate state by introducing a new artifact, or by automating and improving an existing one? Can you show each of the different roles exactly what they need to do their part of the job—so the Head Chef sees “cream cheese," but the Shopper sees “1 Philadelphia Cream Cheese, 8 oz. block"? Can you coordinate the handoff process so that the communication from one role to another doesn't look like passing an artifact only, but allows for a conversation around it? Can you show the context of a communication, so the Shopper finds out which ingredients all go together? Where intermediary roles have been created, can you facilitate their communication, or should their responsibilities be folded back into the primary roles on either side?

## HINTS

• Communicate the whole context between roles

Support communication between roles

• Present only the information each role needs

• Automate or eliminate unnecessary liaison roles

## PROCESS FIXES

When you're an IT department working with internal users, there's a wider range of fixes available to you. In partnership with the business,

Redesign the work by changing role structure directly

you can redefine job responsibilities, reassign roles to different people, put new procedures in place. If you decide to eliminate a role, you can do so by automating everything it does, but you can also simply reassign its responsibilities to other roles or introduce new procedures to make it unnecessary.

One company completely rethought the purpose of its purchasing department. The department's primary role was the Shopper, placing orders for people and paying bills—and making it more difficult and slower to buy things. In fact, much of their work was clerical and added no value. They decided they wanted to give up the Shopper role entirely, returning it to each individual department. They would restrict themselves to the Finder role, helping people locate and set up relationships with vendors for the things they needed. Integrate process fixes such as these into your system response—your system won't just support the work as it is, it will support the system as you and your business partner redesign it. Include the people responsible for looking at your business process on the design team so they are included in the discussions and you have the benefit of their expertise.

## HINTS

• Design the organization as part of designing the work

• Consider process and procedure changes

• Consider defining new roles and job responsibilities

• Include business process designers on the team

## TARGET THE CUSTOMER

Once you've looked at the flow in detail in all these different ways, step back and scan across the whole model. Ask: Where is the center of the work? All aspects of work are there for a purpose. What's core to that purpose? An analytical lab's sole purpose is to get its clients the answers to specific questions about the materials being tested. Everything else an analytical lab does is in support of that. So the Experimenter role is centralbut if there was a way to run experiments automatically, even that role could be dispensed with. Every role is a means to an end. Look for the fundamental intent and seek ways to address it more directly.

If you're a commercial product developer, this central role is the key leverage point for your market message. Even if you're actually

selling a product to support another role, you'll want to show the benefit of the product for the Experimenter. If the lab can't get the procedures done fast enough because it takes too long to wash the glassware, emphasize how your glassware washer

Find the key roles to leverage the market

will improve the Experimenter's life. Even if they don't make the buy decision, they will make recommendations, and their problems become the lab's problems.

Look across the model to see what roles you address in your current product set. What other roles do they touch? What other roles are played by the same people? Those roles are natural to address in future products. Use the flow model to plan how you'll address the whole market.

## PITFALLS

Your last inquiry is a sanity check. What will you mess up if you do the things you plan? By automating a role, have you broken a com-

munication path that the role maintained? By shifting a role to another person, did you create role strain for them? Is there a natural separation of roles that you should maintain, such as the separation between writer and editor? By separating roles, did

Caution: don't create new problems with your fxes

you create role isolation that you will have to overcome with additional tools? Remember that every division of roles creates its own set of problems. Make sure you cover the mapping of roles to people that

Choose the culture to build into your system

occur in the market, and make sure your redesign addresses the new problems it will create.

## THE CONSOLIDATED CULTURAL MODEL

The cultural model reveals values, standards, constraints, the emotional and power relationships between people and groups, and how they all intermix, conflicting and supporting each other (Figure 12.6). Because it concentrates on feelings, the cultural model contributes very little structural information to the design. What it does is give lots of guidance on what matters to address and what constraints to respect. It reveals the hot points, the interpersonal and process problems that people really care about fixing.

The information provided by the cultural model suggests a couple of different design options. Some influences are constraints you cannot

change. These will affect how any product is accepted; a good design should conform to the constraint. Some influences reveal problems in the cultural climate that a system might overcome or ameliorate. $\mathrm { O r } ,$ if the influence is a good thing, the design can

actively encourage and support it. Finally, when an important value seems to be missing from the workplace, the design can seek to introduce a new value as part of the new work practice.

## INTERPERSONAL GIVE-AND-TAKE

If the flow shows the communication between people, the cultural model shows the emotional aspect of the relationship. The different ways that people attempt to impose their will on others and get resistance are captured on this model. Relationships in which the power is unequal reveal this power imbalance in the language and type of influences (Figure 12.7). Look for irritation or subversion in the influences; these will indicate where people are rubbing each other the wrong way. "I'll find a way around the rules" indicates people aren't happy with the way the rules have been set. Look for people fighting over turf: "I manage databases. Don't touch them.""I only work on hardware problems."

Positive influences show where people join forces to get things done, or where a group value shows up in the way the work is done. Look for the positive values: "It's my job to fix your problem no matter who's at fault." "We cover for each other." Look for ways to support these positive values.

Redesign to reduce interpersonal friction

Look at what's creating friction to see how to alleviate it. Is it caused by role isolation, such as the isolation between system management and users? Then increasing communication between the groups may be the answer. Or maybe it would be better to design systems that meet everyone's requirements. If you can ship a system that does what users want and is still easy to manage, part of the friction will go away. Look also for pervasive influences coming from the company or professional culture. These influences will be the hardest to work around—find a way to live with or support them.

HINTS

• Alleviate role isolation

• Increase communication

• Address the immediate complaint

## PERVASIVE VALUES

Formal policy set by the organization and the organization's implicit values constrain what people do, how they act, and even how they think. The values that an organization makes real in its culture determine what people care about and what motivates them. Some values are driven by the organization. They constrain people in the organization, defining what they care about and think they are up to as a group. Other values are driven by groups and individuals, and either reinforce the organization's values or push back against them.

Pervasive values may show up as a single influence that runs into multiple bubbles, but they may also appear as multiple influences that together point to larger attitudes and mind-sets.

When the organization pushes the value “keep careful equipment records" on the system managers, this is part of a constellation of values having to do with being a careful, managed organization that is in control

Choose whether to support or alter customer values

![](images/94996e489894874f0fd547539887d47df7c6cf846aea622fcde25d82ec8698bd.jpg)

Ioses e e sees oe se oe oe e y usenm Ios e e se o ee 'e e e e ten sernd ree e ee rrose eesoshy or reoin rei an. -thal e e keos s ose qeodse e e HSe e on simqoe dre oe ruroealse puae dpe ui  suoeod uins muee re eu ue-ile   ere is ee onnde

succsstiul mnqe i e  m  w w e ma n  s o n trogee ss e yae Sne ens e e e ynae min e r e    e e e e sresrk a-a n es ns s o ns omd o ns mn ne thinss es adxe o ia es os n. nn s snm a s Ss (st) s  aa wen usesn e g n yog sm sns  hk o oicas amre e oee e e ree e e oire e ionisde

oceeen es Sns  a  n snt. bda u dy sy qo ds a er  t word pne Ss sss  i, uaas asns o uern

the sai aior ofe a e a oe e  s s a-n. arecretese e o eus oe e uuqee, se suraitce ples seetsre e err  ee r pet n watent. heq nis dm o e o   nd  ne tfypes e e aeee yee e aee sye  oors Cae eq e e eeesreoees oes see ree rekeeend The ar oae a e  dser hhe

![](images/0656b3a4e47d45c0402db8e33e7210e973838301612393d8b7d586655b52284c.jpg)  
FIGuRE 12.7 Showing the nature of a relationship: the use and subversion of power between system managers and users.

of how it does things and documents actions thoroughly (Figure 12.8). But individuals or groups may push back. "It's easier to throw equipment away than keep careful records" indicates both a willingness to counter the corporate direction and a willingness to spend money. These attitudes will show up in other values and in concrete behavior.

Dealing with pervasive values usually means deciding whether to work with them or against them. To work with a value, introduce systems that make it easier to achieve—perhaps an automated tracking system will make it easy to keep records without requiring major overhead. Look at the flow model to see what roles the value touches and where systems might make a difference. Work against a value when you decide it's counterproductive. So you might decide that your organization is too willing to spend money. Then introduce systems that expose how much people are spending and when; make the budget visible and show how much is left against each budget item. Be aware when you're bucking the culture that this may make your system less attractive—you'll need a good story for why it's better to use the system anyway or else it will have to be so subtle that no one minds.

Values and policies you decide to accept join another category: the absolute constraints you can't or won't do anything about. If the FDA (Food and Drug Administration) regulates your industry and failing an FDA inspection will cause your stock price to drop, there's no way to get rid of the value "We document our procedures every way we can for the FDA." If the whole corporation is organized around "Shipping hardware is how we make money," trying to focus on software will always be hard. Make sure your system promotes, or at least won't interfere with, these absolute constraints.

![](images/607b778cfae60290dde552b3ed1aaa3057ada6a4fe9d084116175adfa13950a1.jpg)  
FiGuRE 12.8 Identifying policy and values. They will show up on the cultural model, but watch what happens to them. Do they get picked up and carried through into all parts of the organization, or are they subverted?

HINTS

• Make positive values and absolute constraints easier to achieve

• Make negative values harder to achieve

• Oppose negative values by introducing counterbalancing positive values

## PUBLIC RELATIONS

The cultural model, more than any other, tells a team what their customers care about (Figure 12.9). It reveals the key issues that should be the focus of the team's efforts. So the cultural model can be a focus

![](images/eb33f7a1b3ab9a1fff40fcb89d0e800f3085b0867dac3f50047c773bf567150d.jpg)

ior r r srs y arn   s   tnt -ue e y  smn mnss de  se  miurd ties od oe uus  on ss o e ns sho rcasphs ae o asre .. 'ns ia is o nca on hre ios aee oe mes e .  r  nt nuhnr i r urie e numr er hmor rs -ntiere esoe oe  se e ee uidq ie e e nuesiitr

desiae wss ee wgk wyaes wne sr has oe a ae e e   e k e cs liakess Senmg yo m e o ok S e es so ymns choe sioe oe soe e ie ie moe e nee oel

beie ne Sn ne pdnrs e o sotnd ee ie ihn manneme ss e e sse e ns aemene Fiesas a da u l s. da utmm

Finaskys e  ey e sys o e stem inasys e ee desaey e sys o e stem Img nn) rune n ir : s smeon  rmn ort es Sns seor raoie os om sre eoid Srieu e o tms mn ns   s uis ens ung s ns uk ug -dns ss sns hns n s son hon ouit anuore, n oe e oe Sos sois e s sosn n thes ,eee. (oe o oes e eaes (es so ,) uee es e meky o oae hue . suese oay s u os s ry hoep iee scts e ezenc mse e mih se nse-

manr  an s. sr ar n or aeaty

for discussing how your team wants to appear to the customer—what message you want to give. You can write yourselves onto the cultural model (if you're not there already) and draw an influence to the customer population. What do you want that influence to say? Do you want to be the “We are your reliable protection against FDA audits" people? Or do you want to be the "We let you get your work done despite all those bothersome requirements" people? What's the message that will sell to the population?

A convenient way to capture this direction is a team slogan—a single, simple statement of the team's mission they can use to keep themselves focused. In one case, the marketing manager looked at a cultural model and said: "Look there— what all these influences are saying is that our customers need flexibility in expanding their systems. They aren't going to plan ahead and they can't. What they really need is fast response. If we could turn

around their order in 48 hours, they'd buy from us without thinking." "Turn around an order in 48 hours" became a slogan for the team—it emphasized a simple, achievable system characteristic, important to their customers, that they could focus on. The slogan becomes a rallying point, a way of choosing between options to advance the team's primary goal. Use the cultural model to define a slogan that fits your customer's desires and who your team wants to be.

## PROCESS FIXES

It's easier to affect corporate culture when you can change management structure and process. Management can deal with interpersonal friction by introducing better communication channels of all sorts, from new systems to brown-bag lunches. They can introduce new values not only by ensuring that the systems enforce values, but also by changing management tone and procedures. Defining new cultural influences can be a task for the whole organization, of which the automated systems are just one part.

When you're building a system for an internal client, the customer

Change processes of internal organizations directly

can be on the design team, and they'll see possibilities in the data beyond system delivery. In one team, a manager in the client organization sat in front of the cultural model for a good five minutes, then jumped up and said: "But this is wrong! We want everyone in our organization to be conscious that the day-to-day decisions they make directly affect how long it takes to ship product. That's not here at all!"

It wasn't there, of course, because that value wasn't real in the organization—no one was acting out of it. The manager drew a new influence in to represent the new value he wanted to instill. It's part of a manager's job to monitor and manage the values of an organization, so it was natural for him to see the omission and to think he could do something about it.

## PITFALLS

The primary danger with the cultural model is that you'll try to lead the customers where they don't want to go. Are you really supporting

the issues they care about? If you're introducing a new value, do you have evidence that anyone cares about that value? The success of the first notes products were limited because they were pushing open, flat access to information on organizations that were, at the time, hierarchical and closed. Only

Don't try to take   
customers where they don't   
want to go

when the notes products started to include controls over the access to information did they become successful. Make sure the changes you introduce will cause someone in the customer population to sit up and take notice—otherwise, you aren't giving customers a reason to adopt your system.

## THE CONSOLIDATED PHYSICAL MODEL

The physical model's primary message is about how physical space constrains what you can do. The world of walls and buildings is hard to change. Within the walls, however, there is room for adapting the physical environment to the needs of the work. People lay things out to meet their needs, define spaces to support the work they do, and otherwise make the physical environment work for them. The physical model shows both the constraints imposed by the environment and the structure people create within those constraints to get their work done (Figure 12.10).

![](images/fd019ecf996eebc1c3d5f621ee9c7eb567312ba837fd3e67d0293e624ef2ff3a.jpg)

timmes. fe e e he ete e o sht e et e k ee ki ael mouien mers a t, e e e tes thal ee e e eol re e e seel eate n aes alec q suez e eds eue suos e es

rats ettes trs s ees  ess os. caoeerd s o ns mtags ns ans ncams -ecomr s esis sye o se ae seem esis Sye yiesystel ee e e  rsuoee eoel ree e soteoe esds mna se e rne e agee rrae ss e stec oihioe l rin s y e  rs sri riss uc ie e  de ms e e e se oe msse en

Iodse ie soe e kie o arse e e e

wom ents. mm  m e ms es s. Mme a he Iis s a asd na  ma ons-

anaae mae rme om man e i oer hs ee  oe o ea oice o thes se, ue sees e es eo e e yre e eom haoe ne soo o oa ne hoay o ne ho e hnol sit l mane at t e osn ne mane mss hheds e e  e se s eh iee ee  ese si e

## THE REALITY CHECK

The first message of the model is to make it inescapable what the customers' physical world is like. If the work is spread out over several buildings, then expect communication to be a problem. Look for existing communication mechanisms: Are people networked? Is everyone networked? What other communication mechanisms exist? Maybe people communicate primarily by yelling to each other. At one site the user talked to the wall and the wall answered back-the partitions were so thin that workers could collaborate even though they couldn't see each other. Is the space noisy or quiet? How many people will be disrupted if the system starts beeping?

The physical model may reveal intents that augment those on other models and may reveal issues that are reflected in other models.

The physical model may reveal that your customers walk around a lot; check the cultural model to see if this is a positive value you should encourage ("We know everyone and are always on the spot to help") or an annoyance you should alleviate (“Every phone call means another interruption and another hike"). The physical model may reveal that supplies from different vendors are kept entirely separately; this will explain why the sequence model for working with vendors shows that people work with only one vendor at a time. In this way, the physical model contributes to your understanding of what's important to the work, as well as helping you get real about the constraints your system must live under.

Design your system to deal with the constraints the physical environment imposes. Allow for the way people move around in doing the work—we've seen people call from a field site back to their main office in another town, asking their coworkers to log them out so they can log in remotely and get their work done. Let mechanisms that work be. If people communicate effectively by yelling to each other, they probably don't need email very much. And don't forget the other side: take advantage of the hardware that is in place. If most of your users already have two monitors, why not use them?

## HINTS

• Don't depend on what's not there

• Account for movement and multiple locations

• Overcome communication problems

• Take advantage of what is there

## WORK STRUCTURE MADE REAL

Where people can change the physical world to match their work, they build into the physical structures concrete representations of the work

structure. Designers can learn the structure of work by analyzing the physical structures people create, just as archeologists learn about cultures by analyzing garbage dumps. When the consolidated model shows a“current work" pile, this is a concrete representation

Fit with the way people organize their work

of how people organize their days. A room dedicated to disposing of hazardous materials indicates that how disposal happens is an important concern. Each place—whether a pile, a corner, or a whole room—is a clustering that supports one particular work intent. That intent is real to the users and could be real in the system you deliver.

Then the relationship of artifacts and clusters to the user shows what matters in the detailed doing of the work. What's in front of the user, within arm's reach? These are the artifacts that the user chose to have “in their face"—they are the critical things to have handy. What's behind the user, pushed out of the way? These need to be accessible, but they don't need to be immediately to hand. If the user is technical and much of their work is online, look at the screen and how it's laid out—it will capture much of the organization of work.

Look at the structure built into the physical world for clues into how to build the system. When the structure exists because users made it that way (the physical environment didn't force it to be that way), it's a structure that matters to users in organizing their work. Build that structure into the system and you'll support the work better. When people create a “current work" pile, it says that the primary organization is “what I am working on now"—not by project. If you design a system that organizes work only by project folder, it will fight the way people think about their work. Look at placement to determine the detailed structure of the system. An artifact that is pushed out of the user's way probably shouldn't be the most prominent thing in the system, but things kept at hand can be easily accessible in the system.

HINTS

• Build conceptual structures into the system

• Match the intent of the place, not the detailed appearance

• Make the things in the user's face easily accessible

• Put things placed behind the user out of the user's way

## MOVEMENT AND ACCESS

The pattern of movement of people and artifacts through the physical environment provides another layer of insight. The flow of an artifact through a person's office shows the important stages of working on it and indicates what stages an automated system should support. The movement of people through space shows important relationships in the physical environment—so frequent movement between the different system consoles in a lab indicates that the work is on all the systems together, not on each system individually.

Finally, the relationship between spaces reveals distinctions and intents. When home offices are repeatedly located up or down a flight of stairs from the rest of the house, it indicates that separating home office activities from household activities matters. When conference rooms are located around the entrance to the site, and none are found near offices, it indicates that meetings are thought to be how you work with clients, not how you work

with each other. The arrangement of space indicates its usage, and its usage suggests attitudes, values, or intents that matter for your design. If it's a problem that workplaces are far away, look for ways to bring that work closer through automation.

Movement in the physical world indicates how to structure a system. The steps people take to work on an artifact reveal stages of work. Look at the sequence model to see the work structure, and build a system that matches that structure or redesigns it. If two kinds of work are kept separate in the real world, maintain that separation in the virtual world—people won't want to mix them. Use the arrangement of the real world to find out what matters. But make sure you match the intent, not only the actual arrangement. Putting the office up or down a flight of stairs indicates this is separate work that wants to be physically separate, whereas the separation between phone and Rolodex is only a reflection of physical limitations.

HINTS

• Match or improve the flow of artifacts

• Maintain conceptual separation between parts of the work

• Support the intents implicit in the arrangement of space

## PARTIAL AUTOMATION

It's hardly ever possible to put everything online. People increasingly use email, but paper mail still exists. So even if email is easier to file and track, it hasn't gotten rid of paper filing—what it's done is to introduce a new layer in addition to paper filing.

In the system you build, consider whether you've automated everything about a job or whether customers still need paper. When you build an automated ordering system, will people still print and file a paper version so they can track what they've ordered? When you automate scientific methods, will scientists still have to print them to meet FDA requirements? When you make lab orders electronic, do requesters still have to print the order and attach

Work with paper—it's not going away

it to the sample? Make sure you've either covered the whole job or that you dovetail with the paper documentation that is still necessary.

## HINTS

• Address all intents of the paper system

• Provide complete coverage in the online system

• Help keep online and paper in sync if paper is still needed

## PROCESS FIXES

If you own the physical environment, you have the option of changing it. You can move people and equipment around to make places that

## IT: consider moving walls and restructuring space

support a single intent in the work. You can hook all the people who need to communicate into the same network. You can reorganize offices to better support movement through them. You can give everyone PDAs and install wireless networks. These changes in

the physical environment can be part of the overall response, supporting and supported by the systems you put in place. Planning the rollout so that changes to the physical environment are synchronized with process changes is part of designing the corporate response.

## PITFALLS

The easiest way to mess up the physical environment is to not take it seriously. If people don't have printers by their desks, don't build a

Don't ignore the reality of the environment

system that requires frequent trips to the printer. If your users walk around all the time and like it, don't try to tie them to a desk by giving them a product that only runs on a desktop. Check the cultural model to see if they like walking around. Check the

flow to see what communication is enabled. The physical model is your guide to what's real—let it drive what you can do in your system. But don't get too literal either. Try to achieve the users' intent, rather than matching the current environment's limitations.

## CONSOLIDATED SEQUENCE MODELS

Sequence models make the detailed structure of a work task explicit. They show how the task is broken into activities, the intents that people are trying to accomplish in doing the task, the different strategies people use, and the individual steps that make up the task. Sequences are your best guide to structuring a system to match and extend the way people approach a task (Figure 12.11).

<table><tr><td rowspan=1 colspan=4>FIXING A PROBLEM</td></tr><tr><td rowspan=6 colspan=2>Set up to tackle              • Set up place and context to tackleproblem                        problem• Orient self to problem situation</td><td rowspan=1 colspan=2>Go to the place where problem can besolved</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Get more information on problem</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>Look at system to see problem incontext</td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>Think about who is expert in thisdomain</td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=3 colspan=1>Search for cause</td><td rowspan=1 colspan=1>• Identify cause of problem</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Search for problem cause by hand</td></tr><tr><td rowspan=2 colspan=1> Eliminate repetitive tasks</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Create and run specialized procedureto search for cause of problem</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Identify cause of problem</td></tr><tr><td rowspan=8 colspan=3>Fix problem• Minimize disruption of users&#x27; work• Move substitute HW into place sousers can keep working</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>See who will be affected by work ondisk</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Warn users of work to be done</td></tr><tr><td rowspan=1 colspan=1>Wait for users to get off disk</td></tr><tr><td rowspan=1 colspan=1>Dismount disk</td></tr><tr><td rowspan=1 colspan=1>Find scratch disk or new disk</td></tr><tr><td rowspan=1 colspan=1>Mount new disk for use in fix</td></tr><tr><td rowspan=1 colspan=4>1</td></tr></table>

FiGuRE 12.11 A consolidated sequence model showing how system managers solve problems. This is a partial model. but shows some of the major activities and intents in the problem-solving task. The sequence suggests both what issues a design might address as well as how it should be structured to support the user well.

Looking down the set of activities reveals an initial set of concerns a design might address. The very first activity is "Set up to tackle problem." How could a design support getting set up? Currently, system managers have to go to the place where the problem is. Looking at the intents reveals that "setting up" means both going to the right place and getting information and context about the problem. A system that could both provide remote manipulation and reveal what's going on at the failing system might address the whole activity.

In a later activity. "Escalate problem." the system manager coordinates with backup expert help. There are two strategies: one to work on the problem together and the other to hand over responsibility for the problem. Each strategy needs to be allowed for in a system. The system could focus on supporting collaboration between the system manager and the backup help with groupware-style tools so the two can see what each other is doing. Or, the system could support handing off problems. simplifying the process by passing context and history to the new owner automatically: Or the system could do both. The fow and cultural models will offer additional insight as to which solution would be most valued by the customer population.

<table><tr><td rowspan=1 colspan=5>FIXING A PROBLEM</td></tr><tr><td rowspan=10 colspan=4>Fix problem continued      • Move substitute HW into place sousers can keep working continued</td><td rowspan=1 colspan=1>Create directories if necessary</td></tr><tr><td rowspan=1 colspan=1>Copy files to their right places</td></tr><tr><td rowspan=1 colspan=1>Mount new disk publicly if it ispermanent</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>If other problem: process crashes, fixinappropriate message on VTX, createprint queue, install SW</td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>Attempt fix</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>Use documentation to help do task</td></tr><tr><td rowspan=3 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>Determine if fix worked; if worked, goto &quot;Document solution&quot;</td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Didn&#x27;t work, try to figure out why</td></tr><tr><td></td><td></td><td rowspan=2 colspan=1>• Get help, either keepingresponsibility or passing it on</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Can&#x27;t figure out problem or not my jobto fix problem; call on experts</td></tr><tr><td></td><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>If trying to fix on phone:</td></tr><tr><td></td><td></td><td rowspan=2 colspan=1>• Apply advice from expert to solveproblem</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Decide on fix on phone (go to&quot;Attempt fix&quot;)</td></tr><tr><td></td><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>If expert needs to see actual system:</td></tr><tr><td></td><td></td><td rowspan=2 colspan=1>• Make it possible for expert to solveproblem</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>Give information for expert to lookat problem</td></tr><tr><td></td><td></td><td rowspan=1 colspan=1></td></tr><tr><td></td><td></td><td rowspan=3 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Check site documentation of setupto determine how to identify failingHW</td></tr><tr><td></td><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Give experts information necessaryto locate HW</td></tr><tr><td></td><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Wait ștrategy 1: partner in fix</td></tr><tr><td></td><td></td><td rowspan=1 colspan=1>• Save time and boredom, and</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>Look for problem in parallel toexperts (go to &quot;Search for cause&quot;)</td></tr><tr><td></td><td></td><td rowspan=2 colspan=2>maintain responsibility for thesolution</td><td rowspan=1 colspan=1></td></tr><tr><td></td><td></td><td rowspan=1 colspan=1>Wait strategy 2: give responsibilityto expert</td></tr><tr><td></td><td></td><td rowspan=1 colspan=2>• Save time by passing responsibilityand doing something else</td><td rowspan=1 colspan=1>Do something else while theyhandle it</td></tr><tr><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>Document solution</td></tr><tr><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>Document solution and actions taken</td></tr></table>

<table><tr><td>FIXING A PROBLEM</td><td></td><td></td></tr><tr><td rowspan="6">Document actions continued</td><td>• Make sure affected people hear directly</td><td rowspan="3">Notify important people directly</td></tr><tr><td>• Make self a person to clients</td></tr><tr><td>Make sure problem doesn&#x27;t happen again</td></tr><tr><td>• Keep from creating future problems</td><td>Clean up—get rid of temporary files</td></tr><tr><td rowspan="3">• Make sure full process works</td><td>Notify owners of other parts of the process to do their part</td></tr><tr><td>Done with documenting</td></tr><tr><td>Done</td></tr></table>

FIGURE 12.11 continued

## WHAT THE USER IS UP TO

Every consolidated sequence has a primary intent—-the reason why the task was worth doing in the first place. In the end, no individual sequence step matters. You can change, eliminate, or automate steps at will as long as you continue to support the user's intent. There are multiple levels of intent: a system manager's intent in responding to a call is to resolve whatever problem the user is having. But behind that, he intends to demonstrate that his organization has the systems under control. And behind that, he wants to show that he delivers real value to the corporation and should continue to be funded. Each level is broader and addresses more wide-reaching issues than the one before.

Every consolidated sequence has numerous subintents that are accomplished along the way. A subintent allows the user to achieve

the primary intent—if you redesign the sequence, you may make some subintents irrelevant. That's okay because they are only a way to achieve a more fundamental intent. One team discovered that part of keeping records of lab procedures was to reduce

A system has to allow for all the users' intents

graphs produced by lab equipment by 50% on the copier so scientists could paste them into lab notebooks. Through the development of an electronic lab notebook, the team eliminated the intent of pasting a paper graph into a paper notebook. They simplified the work to the point that the intent was no longer relevant.

Secondary intents are achieved in the process of performing a sequence. Unlike subintents, they are important in their own right if you get rid of the whole sequence, you'll still have to find users a way to achieve these secondary intents. So system managers may depend on users asking them for an IP address to find out what new systems are being added and what's on those systems. No matter what happens to IP address assignment, system managers will always want to know about new systems.

The first design question to ask of a sequence is whether the primary intent needs to be met at all. If the intent of the whole sequence is to assign an IP address and you can automate the whole process (or introduce a network that doesn't require unique address assignment), then you've rendered the sequence unnecessary—you've simplified the job. But before you can eliminate the whole sequence, check all the individual intents that the user accomplishes along the way. Don't worry about the subintents—if you eliminate the need for the task, they become unnecessary. But if you eliminate the sequence, you must find another way for the customers to accomplish secondary intents or your system will fail. If you eliminate IP address assignment as a task, system managers will need another way to find out about new systems.

If you choose to keep the sequence, every intent is an opportunity for redesign. Each intent indicates something that matters to the

work. If you can provide a way to achieve it more directly, you can simplify the work. When changing the steps for accomplishing an intent, treat it just as you treat the overall intent of the sequence: look at the part of the sequence you are designing away, and make sure your customers can still accomplish all

the intents that matter to them.

Get behind the specific actions to understand what the user cares about. One design team was looking at the low-level interaction of users with a word processor. Analyzing the sequences of interaction revealed constant repositioning of the cursor. Users would click one character off their intended target, or lose track of where the cursor was, or be unsure where it would end up if they clicked on different places in their document. One user kept hitting the right and left arrows in quick succession. “He's just twiddling his fingers," said one engineer, and that's a natural reaction if you're not used to looking at pattern.

But other engineers on the team were used to looking at pattern, and what they saw was a recurring theme—positioning the cursor was a low-level but constant irritation and an impediment to getting work done. And this itself was part of an overarching theme of glitches and problems in the low-level interaction with the system. The team adopted a design direction of cleaning out all these glitches to make the interface disappear as a problem, including better ways to provide feedback on where the cursor was.

HINTS

• Render the primary intent irrelevant

• Support the primary intent a new way

• Account for all secondary intents

• Redesign to support achieving subintents

## HOW USERS APPROACH A TASK

Where customers use different strategies to accomplish work tasks, the consolidated sequence models show what those strategies are. Each strategy indicates a different approach to the work, driven by different circumstances or values. The different strategies may be adopted by different roles, driven by different work styles, and may reflect different intents.

Your system needs to recognize the strategies and support them, or introduce a new way of working that supplants one or more of the

strategies in use. If you choose the latter option, account for the underlying characteristics driving customers to choose the strategy you are eliminating. You might decide that system managers who continue to work on a problem after turning it over

Support the strategies you know people use

to their backup experts are wasting their time. But they may do this to save face—to prove that even though they had to ask for help, they are still experts and have just as good a chance of finding the problem as the people they called in. They may do this because they really want to have someone to talk to about the problem while they work on it. Or they may just be bothered by the problem and want to find out what the answer is. In these cases you won't be able to keep people from hunting for the solution on their own. You'd do better to recognize and allow for it.

## HINTS

• Identify and support strategies

• Don't eliminate strategies unless you can account for the circumstances where people choose them

## UNNECESSARY STEPS

After you've decided that your system must support the sequence, it is your guide to the structure of the task. Look at the steps of the sequence to reveal the issues for your design. Are there wasted steps? Are there steps you could eliminate? What role could automation have in simplifying the work?

The major activities in the consolidated sequence show the coherent units of work the system must support. Use them to guide the dif-

## Eliminate and simplify steps

ferent things your system must do and how they must be arranged to support the work. Look at the transition between activities. Is there a transition between roles as well? How will your system manage the handoff? Does the new activity imply moving to a new physical place? What needs to be taken to this place, and how does the customer make the transition? What, in general, disrupts the transition between activities, and how will you manage it?

Look at the steps themselves. Can you simplify them? Where the customer currently takes several steps, can you automate them down to one? Where a step is currently difficult, can you make it easy? Where is the pain, and where is the tedium? Look for ways in which technology can streamline the work, but make sure you don't have to add steps elsewhere (in setup, or loading information to use later) to eliminate them here.

## HINTS

• Eliminate steps

• Automate steps

• Eliminate breakdowns

• Facilitate the transition between roles

• Don't create work no one wants to do

• Achieve intents directly

## WHAT GETS THEM STARTED

The triggers show how to alert the user that something needs to be done. Pay attention to the style of the trigger. Is it noisy or quiet? Is it

appropriate to the work being triggered? Does it work, or is it a nuisance? Choose whether to duplicate the trigger in your system, if it works, or to replace it with a trigger that works better. Look at the difference between users—the designer who

can't stand to have the mail icon blink in the menu bar versus the writer who has a dialog box come up to announce each new mail message. Look at how too many triggers defeats the purpose, as when system managers learn to ignore alarms because there are so many and so many are irrelevant. Choose a way to trigger users that works given who they are.

## HINTS

• Provide triggers for work tasks

• Match style of trigger to appropriate kind of interruption and the user

## PROCESS FIXES

When the work is internal, the sequence model captures the work procedure to redesign. Designing a new way of working means, among other things, redesigning the sequence model so it represents the new procedures. The organization can put these procedures in place directly. It's a typical failing of business process reengineering projects to overlook the secondary intents that are accomplished by the current process—failing to recognize them, the reengineered process doesn't cover everything that needs to be done, causing people

Introduce new procedures to improve the work

extra work. By analyzing the existing process in this way, you increase the likelihood that you'll recognize and support all the intents that a work process must support. (We'll discuss prototyping new systems and process fixes in Part 6.)

## PITFALLS

Certain problems are typical when automating and eliminating steps. We've mentioned failing to account for secondary intents—make sure

Reveal the workings of automation to gain user trust

all intents are accounted for when you redesign. But when you automate a set of steps, be aware that users won't trust that you did it right—at least not right away. They're going to want to see what you did until they are confident you won't mess up. Developers used to insist on seeing the machine code pro-

duced by their compilers—but as compilers have become standard and dependable, the need to see the machine code went away.

Also watch out for the amount of extra work your automation introduces. Have you simplified many steps at the cost of vast amounts of setup and customization? Will the user have to set up the system like it is a separate task? If so, will any real users do this? And look at the amount of work it takes to interface with and maintain the system. Have you introduced a new role, that of the system babysitter, or feeder? If so, will your users be willing to adopt those roles?

## CONSOLIDATED ARTIFACT MODELS

Artifact models show the common structure and intents of the different artifacts used in the work. They are important for showing both the detailed conceptual structure underlying a task and how that plays out when it's made real in the artifact.

## WHY IT MATTERS

Just as sequences exist for a reason, artifacts exist for a reason: they enable customers to accomplish something they care about. There will be one or more intents for the whole artifact, and then each of the parts may suggest additional intents.

Look for ways to achieve the intents more directly in the system you design. When you see a report passed back with notes and ques-

tions scribbled in the margins, you know it supports discussion, not just reporting. Consider supporting the communication directly through email and bulletin boards. But make sure you support all the intents—you have to support them all before you can get rid of the artifact. If you put an existing

artifact online, pay special attention to the informal uses of the existing artifact—if you make it impossible to dog-ear corners, scribble notes in margins, or tear off bits to pin to the wall, you won't support the work.

HINTS

• Support the intent more directly

• Support intents indicated by informal usage

• Account for all intents

## WHAT IT SAYS

An artifact presents information. Look at the data on an artifact for insight about the work. Does a purchase request form provide a field for justifying a purchase, but not for the cost of the item to be bought? That suggests that cost consciousness is not part of the environment. Who uses the information? Does the artifact pass information between people? Does it present the same information to every person, regardless of their role or what they care about, cluttering up the interface with irrelevant information? Is the artifact acting as the communication mechanism between two roles, to pass the context of a work task?

Consolidated artifacts collapse the history of use across all the actual events captured by individual artifacts. As a result, the artifact shows the scope of all the different usages, collecting data, intents, and concepts into one place. In this way the artifact shows the range of variation your design must account for and collects all the intents that matter to the work. It makes sure your design covers all the bases (Figure 12.12).

Beware: an online artifact can render informal usages impossible

![](images/3c749cd267c275897edcf020caa623cf20160ab61f6c7e66acbbdcf016c42438.jpg)

FiGuRE 12.12 A consolidated artifact. This model shows the parts of a purchase request as they might matter to the developers of an ordering system. It shows the parts, but also their intent and how they are used. An automated ordering system would have to support the intents implied by each part.

The model reveals that there are two primary intents to the purchase request artifact: first to justify the need for the item so the requester might actually get it, and second to communicate exactly what to get and where to put it. Automating purchase requests depends on understanding and responding to both intents. However, the description of what to buy is often informal. People assume knowledge of standard configurations and what has been bought before

The model shows the parts that a purchase request should have, including where to put the item, where to buy it, and sometimes the exact model number to buy. A purchase request that matched a company's formal organization——where the purchasing department decides where to buy things—would not fit the need people feel to say exactly what they want and who should supply it.

Look for opportunities to put artifacts online. If the artifact helps two roles communicate (like a form), can you automate them entirely?

Forms tend to capture all the data that anyone might ever need, which means that everyone sees all the data. When the form is used by different people for different parts of a job, the result can be overwhelmingly complex. When you automate the artifact, can

Artifacts should provide only the data people need

you collect all the data in one place, but provide to the different roles only the data they need, so that no one is distracted by irrelevant information? Can you provide information automatically (such as cost center on a purchase request) that is needed by some people but is not important to the requester? And what's the communication the artifact supports? If that communication is discussion, not just data or context, can you support it with communication tools?

HINTS

• Provide data automatically

• Share context between roles directly

• Support communication implied by the artifact

## HOW IT CHUNKS

A consolidated artifact holds distinctions that are indicated by the structure of the artifact. Unlike the distinctions represented by a sequence or physical model, these are extremely particular to the work the artifact supports. An artifact model won't tell you what you should build; but once you have decided that this artifact is important to your proposed solution, it will give you the detailed structure you need to guide the design.

Each grouping of information on the artifact represents a chunk for your system to consider. A form might include routing informa-

tion that an online version might automate away-— but you must make sure that the automated form supports the same kind of routing that the paper form supports (unless you're redesigning that, too). Conversely, our calendar model showed the distinction between meetings and reminders. It showed

The structure of the artifact reveals distinctions for the system

that notes are associated with specific days. Distinctions like these must be carried over into the new design if it is to work well.

## Don't just duplicate an artifact online

## HINTS

• Use the structure of the artifact to guide the structure of the system

• Maintain the distinctions that matter to users

## WHAT IT LOOKS LIKE

Artifacts don't consist only of structure and content. They also have a representation, an appearance, which is designed to support the work

the artifact is used in. Look at how presentation is used to further the intent of the artifact—or how it gets in the way. When a part is made to stand out, it's intended to catch the eye—how will the analogous artifact in your new system catch the eye? Look at the different ways of making a part stand out. Do they represent different intents, or are they different ways of achieving the same intent? Is standing out the only intent, or are there secondary intents to consider, just as a newspaper headline both stands out and reflects the overall look and tone of the newspaper?

Take presentation seriously. It's often treated as secondary, but people work hard to make the things they use look right for the work.

## HINTS

• Determine the intent of the presentation details

•Mimic the intent of presentation details, not the details themselves

## PITFALLS

Artifacts, because they are real, suggest that every part is needed and every part is relevant. Look beyond the artifact itself to see what's useful. Are all parts of a form used? Is any part of the form used, or is the real communication written in longhand over the top? Even if the data is used, does everyone need it, or would it be better to give different roles their unique views? And make sure that an online version of the artifact doesn't break it up too much. If every part of the artifact maps to a different dialog box, it will be hard to see all the information together.

## USING METAPHORS

We discussed metaphors briefly in Chapter 4 as a way to think about work structure while setting focus for a project. As you study the work, you may find that these or other metaphors continue to be useful and enlightening. If so, consider redesigning the work explicitly by following the structure of the metaphorical work domain (Kensing and Madsen 1991).

For example, anytime the work you are supporting involves making things—software development is a prime example—housing con-

struction is an interesting metaphor. As a team, draw a flow model of the roles in building a house. Look at the architect's relationship to the homeowner on one side and the primary contractor on the other. How does he or she mediate between the two? How does the architect communicate with the homeowner, and what representations show the homeowners

what they will get? Where does the architect's responsibility leave off and the contractor's take over? Look at the emotional tone of the relationships. Architects and contractors frequently argue over what to build and how to build it—contractors have to work out the details of the architect's specifications in lumber and concrete.

Then use these questions to drive how you restructure the actual work you are supporting. Where is the architect role in software devel-

opment? Do “software architects" play the same role as building architects? Do they create the same sense of partnership with the customer? How would you redefine the software architect role to incorporate more of the user focus of a housing architect? What tools do architects use in working out designs and in

Metaphors break you out of the weeds of your own focus

managing their relationships with client and builder? Could the intent of these tools be carried over into a system for software architects? Architects use a wide variety of props to help communicate with clients—floor plans, elevations or front views, perspective views, and complete three-dimensional models of the proposed house on its site. Do software architects have the same range of representations available to them? Could you create similar representations to improve the communication between software designers and users? Should software architects record their agreement with customers in a contract similar to that used by architects?

This inquiry just scratches the surface of the home building metaphor—you'd also want to look at the relationship between architect and contractor, and between contractor and subcontractors, to begin with—but it gives some sense of how to use the metaphor to drive your thinking. You may find that you need to understand the metaphorical work practice better to use it well. (How do architects and contractors really work together on a day-to-day basis?) If it's worth it, do some interviews in the metaphorical work domain; otherwise, find a more familiar metaphor.

Look for work domains that parallel the domain you're designing for. One team supporting home finances decided the roles were like

the pilot and navigator on a plane: one person did the day-to-day work of keeping the finances on course, while the other got involved when deciding how, over the longer term, to get where they wanted to go. Another team decided that the order process

in their company was like asking someone else to shop for you in a household. All the problems they saw in the interactions with the purchasing department mirrored the problems of getting someone else to understand what you want. Recognizing such a metaphor gives you a handle on how to support the work in new ways.

## USING MODELS FOR DESIGN

These discussions of work models and parallel work practice should give you a guide in thinking about the implications of existing work practice for design. The models lay out different aspects of work in front of you so you don't have to hold it all in your head; doing the inquiry into one model after another helps you synthesize across the models, see overarching issues and pattern, and begin to put common solutions together. Discussing the models and possible metaphors in the team leads to shared understanding and perspectives. Through these discussions, teams start thinking about the design response, not just by responding to specific work problems with specific features, but by responding to the whole work situation with a coherent system. By the time they get to actually designing, the team is so steeped in the data that they can't help but respond to it.

Through these activities and discussions, the team together works down the chain of reasoning from the facts in the work models, through interpretations, implications for the design, and finally specific design ideas. We'll present an orderly process for doing this in the next chapter.

## Design from Data 13

oing from customer data to a design requires a creative leap, a I leap from what matters to what to do about it. Customer data never dictates exactly what to design. Any set of facts can be taken multiple ways, used to inform different kinds of decisions. A product designer looking at a salesman's role might see how to provide information and tracking tools appropriate to life on the road. The division manager might see the frustrations and constraints of the job and how to alleviate them through training and communication sessions with individual salespeople. Upper management might see the constraints imposed by the organizational structure and how the sales role and relationship of sales to the rest of the organization might be redefined to make them more successful. Each different point of view reveals a different set of issues and different solutions.

The range of solutions a design team considers depends on who is on the team and the perspectives they take—the skills and knowledge they have available to them, the charter they think they have from management, and their shared assumptions about what they are up to as a design team (Gomaa 1983). Teams can't invent solutions that they don't have the knowledge to create, don't feel they have permission to carry out, or don't see as being their job. Shrink-wrap software developers

Teams can't invent solutions that they don't have the knowledge to create

won't think of restructuring the organization as part of their design— but even a team chartered to reengineer a business process won't think of restructuring the organization if they don't have the skill to see and design process and if they don't have the backing of management. A cross-functional team makes the widest possible set of skills and perspectives available, and increases the range of solutions they can consider. But that solution creates its own problem: team members tend to pull in different directions, with individual members emphasizing the issues and ideas they see. It's up to the design process to unite the team behind a single corporate response. (See Kelley and Hartfield [1996] for further discussion of using multiple points of view to drive invention.)

Getting the team to be creative is tricky. We want the team to think widely, "out of the box." Yet it's in an engineer's nature to im-

Evaluation stifles creativity mediately do a feasibility estimate of any idea they hear of or invent. That's why they respond so frequently, "We can't do that." Until the entire design for doing it is worked out, the idea does not seem doable. Then the same engineer who said it was impossible Friday will come in Monday morning and announce that it's done. It's not possible to be creative when every idea gets immediately put to the test and a truly creative idea may well require a substantial time to investigate whether it can be done or not. We often find that the idea we thought was a pipe dream when it was first mentioned turns out to be easy when the implementation is designed. So there's no advantage to filtering ideas early.

On the other hand, part of being free to think widely is to feel secure that you won't be committed to implementing the things you

think up. We encourage people to think broad, wide, and radical first, without worrying about how to implement their ideas or fit them with existing products. Once you've had the radical idea, you can reduce it to its core intent, decide what's important about it in supporting customers, and scale it back to what's practical in limited time. Following invention, the process provides many evaluation steps within the team and with customers to ensure that the design works for the customer and can be implemented by the people in your organization. Knowing these steps are coming frees the team to step outside the bounds of what they know to be safe.

In Contextual Design, a team walks through a series of activities intended to get them over the hump of having a broad understanding of their customers' work practice but no agreed solution, to a clear sense of what problems to address and an innovative design to address them. Contextual Design provides a set of steps, linked together into a process, that move the team to a concrete representation of their shared direction, or vision:

Walking the data: to see the different aspects of work and synthesize them mentally

Visioning: to invent multiple possible responses to the data

Evaluation and integration: to develop a single corporate response

Concurrent action: to move all parts of the organization forward in parallel

## WALKING THE DATA

The first activities are designed to explore the data and its implications for the design. At this point we aren't looking for specific design solutions; we just want to enable team members to think about the data in detail and explore all the different ways they might respond to it. Just as we set focus before going on an interview so people know what to look at, we use these activities to set the team's focus for design so they know what to build. When the customer data is understood and internalized, team members will find it natural to design solutions that respond to the primary issues it raises.

The first activity for immersing yourself in the data is to read the affinity from end to end—what we call “walking the wall." Walking

the affinity right before visioning ensures that the customer issues are fresh in the designers' minds— that the solutions they invent will be grounded in the customers' work practice. Then when they review each other's ideas and see how other people are reacting to the data, they start to build a shared

Anyone who visions must be steeped in the customer data

sense of how to respond. We discussed the detailed process of walking an affinity in Chapter 10—everyone who will be involved in the visioning session walks the affinity this way before visioning.

After walking the affinity, the team uses the consolidated work models to do the same kind of thinking as the affinity on the different perspectives on work. Each model represents a different point of view, a different dimension of work practice. When people walk one after another, they naturally synthesize all the different dimensions into a single three-dimensional picture of the customer. The previous chapter discussed in detail the kind of issues the team might consider for each type of model; designers do this individually or in small groups, discussing the model and how they should respond as a team. Each model will generate a set of goals: values to encourage; negative feelings to eliminate; roles and activities to support, combine, or eliminate; and so forth.

Once individuals or small groups have discussed each model, they share their discussions with the rest of the design team, and the team marks parts of the model that they want to support or eliminate. At this initial stage when the team is still deciding on a design direction, they are more interested in the "what matters" type of issue than the structural issues. So they look at flow and cultural models in detail; they look at constraints and primary intents on the physical; and they look at intents, activities, and strategies of high-level structure in the sequence and artifact models. As they read and discuss each model, issues from the other models and from the affinity are naturally incorporated into their discussion. What started as point solutions to individual problems weave together into a synthetic response to the whole work problem.

Walking the affinity diagram and work models focuses the team on specific aspects of work they want to respond to. The team can have an

explicit and public conversation, recording the issues right on the affinity and models. You can include others in the discussions by allowing them to participate in reading and responding to the models. And they ground your vision for redesign in real work issues.

After walking the affinity and each model, crystallize your thinking by making a list of the most important issues from that model. This gives you a single, crisp statement of the issues that you can return to as a reminder of your focus for the vision. When the lists are made, the team is primed to start the vision.

## PRIMING THE BRAIN

Before starting with the visioning, the team brainstorms two lists, with no evaluation or filtering, that will be fodder for the vision itself:

Technology: Any design response uses technology to solve work problems. To bring the technology they have available to mind, teams list all the technology they might draw on. This list incorporates the mundane (networks, World Wide Web), specialized technology unique to the company (artificial agents, CAD diagramming),

Lists bring possibilities to mind

and implementation approaches that the team might otherwise not think of (process design, business partnerships). Anyone on the team who doesn't know about any of these possibilities can learn about them at this point.

Starting points: Discussing the work inevitably involves discussing how the team might respond to it. These initial discussions are starting points for the vision. In this list, we capture some of the most important starting points that people don't want to forget: design ideas that have captured the imagination of team members, a slogan that the team wants to commit to, or a metaphor for what the work could be like. "Put the system manager's whole job on a PDA." “Ordering should be one-stop shopping." “The lab should be like Federal Express tracking packages—you always know the state of every experiment." “Do shopping like bumper cars." Each of these ideas is a seed, a starting point for the team to elaborate into a whole approach to a design problem.

## CREATING A VISION

We call our visioning process a grounded brainstorm—“brainstorm" because ideas are not evaluated as they are generated and “grounded"

because ideas are driven by the customer's work practice. A visioning session gives a team the chance to choose a starting point and spin it out into a story about the new work practice transformed by technology. The story describes the brave new world

Choose a seed to start

the vision

the team envisions—without committing them to actually building it. (Greenbaum and Kyng [1991] describes a variety of approaches to inventing new work practices.)

In the visioning session, one person (the “pen") stands at a flip chart, drawing the ideas as participants throw them out. The pen has two roles: encourage people to talk, but also fit their ideas into the vision as it is developing. Unlike a normal brainstorm, where each idea is independent, a vision session starts with one of the ideas from the list of starting points and incorporates each idea into a coherent story about the redesigned work. The vision is a drawing showing what the new work practice would

The “pen" weaves the team's ideas into a story of new work practice

be like if the vision were in place (Figure 13.1). It shows people in the roles they play, the systems they use, how they communicate with each other and the systems, and how the systems are structured when that's necessary to thinking about the vision. Vision pictures are very informal—they are drawn quickly, without a lot of structure. They tend to have lots of arrows showing communication, lots of faces showing people, and lots of boxes indicating screens, systems, or other technology components. They aren't restricted to the system being designed but may include the delivery mechanism, third-party relationships, and additional services that work together to make the vision possible.

Any vision has a thread, which starts with the initial starting point

and then is played out as participants expand on it. A facilitator helps participants pursue a thread by tying together ideas into a story of work practice and suggesting additional issues from the work models or affinity, additional roles from the flow model, or values the team agreed to from the cultural model:

Pen: So we're starting with the idea that shopping is like bumper cars. (Draws a bumper car.) What happens?

Designer (D1): Well, the whole idea is to get the kids involved. So the kids have to be able to drive. (Pen draws a kid at the wheel.)

Another designer (D2): Yeah, put the adults in the passenger seat. Then organize the store so you can drive through it in order. (Pen starts sketching the store.)

D3: And make the aisles narrow enough so you can pick things off both sides as you drive by. (Pen draws aisles on either side of the car.)

D1: You'll have to make all the aisles one-way.

Facilitator: But what about backtracking? We saw people have to go back for things they forgot.

D2: We'll give them a way to backtrack at the end of the aisles.

The facilitator and the pen should listen for ideas that are on the thread, postponing ideas that are too far off the main line to be starting points for another vision. When an idea conflicts with the thread the team is working on, the pen adds it to the list of starting points.

This keeps the thread coherent while assuring the team member that his idea has been heard and will be dealt with. Eventually the thread will play out—people won't have more ideas for extending it without taking a new starting point. At this point the vision is put aside and the next one started. Don't duplicate ideas from vision to vision good ideas will be recovered in the next step, so you don't need to go through them again.

Practicality is not a major consideration for a vision. If the team lets go of worrying about whether they can build their ideas immediately, they will be more creative and produce a vision that will account for more of the work practice, more coherently. Our team above is unlikely to ship a product that installs bumper cars in grocery stores, but working out the vision gives them a chance to explore issues of child control and participation that are very likely to be part of their final design. Balance creativity against practicality. After visioning bumper cars and some other fanciful ideas, the team might want to evaluate and consolidate them into a more conservative vision capturing the key benefits but using technology they think they can implement.

Any vision will specify more than the team wants to attempt in a single version, but that's all right—it means the team will have a plan,

a strategy, that they can use to drive delivery over several versions. (We'll talk much more about strategic development over several versions when we introduce the User Environment Design in Part 5.) Even if you know you are focused on a short-term deliverable—say, your next update due to ship in six months—you're better off thinking and visioning widely first. Then you can either synthesize and pick and choose the best parts for the deadline, or you can vision widely and then vision explicitly for a sixmonth deliverable. You'll find you automatically pull in ideas from the wider visions to put together a coherent plan that you can do in the time you have (once you do the inevitable trimming).

A good visioning session is a lot of fun. Everyone is tossing in ideas for what to do based on what matters in the work. Everyone is

talking at once and building on each other's ideas. The major gating factor for a visioning session is the ability of the pen to draw what he or she hears without a lot of filtering or explanation. If people feel like it's too hard to get their ideas on the paper, the

In a good visioning session, everyone feels their ideas have been heard

![](images/87bdaba78e7f8e9be951646fdd85a0e31512ed590a6d3906c5d01ebc7ae0f6a1.jpg)

FIGuRE 13.1 A vision for system management.¹ In this vision, the team has elected to focus on improving the communication between user and system administrator and on improving the diagnostic process. The vision started with the idea that the system administrators wanted to bring the problem to them, to make everything necessary to solve the problem available locally. In following the story, the team integrated a number of other issues—how to make it easy for users to get help, how the system administrator can get backup help, and how to use stories in diagnosing problems.

In the vision, when a user wants help with a system, they just push a big red "HELP" button on their phone. That automatically connects them with the right person for their system and organization and brings up their system information on the administrator's screen. The team wanted to make asking for help through the “approved" mechanism so simple that no one would be tempted to use personal or informal contacts to go around it. They found that having enough context about the user and system was a major impediment to administrators in providing support researching the system was always the first step toward doing any real work—so they had the system provide as much context as possible. When the time comes to implement, the "HELP" button will probably not survive as visioned—it's not reasonable to make changing every phone a prerequisite to using this system administration software. But the idea will prod the team to think about simpler ways to achieve the same intent—perhaps stickers to put on the phone with the right number, or autodial in the software for computers that support it. The vision is a stake in the ground saying, “This is the goal." The team can scale back and decide on reasonable ways to achieve the goal later.

To support diagnosis, the team noticed that system administrators depend on story and anecdote a lot when troubleshooting. Stories capture knowledge about what might work in different situations, but capturing the stories and making them available is hard. Typically this is done through tale swapping in the informal system administrators’ community. Even when people capture a log of what they did, it doesn't have the same flavor as a story—it doesn't include the different alternatives tried and the frustrations of trying to work things out. This vision attempts to capture stories and make them available when needed, while diagnosing another problem, through a database of stories. When done with a call, an administrator can tell the story of what happened into the phone—they are used to dealing with the phone. Later, they can search the database for stories relevant to the problem they are working on—perhaps from the same system or showing the same symptoms. Then they can listen to the stories while working on the problem. The challenge of the “story database" is not so much technical—it just depends on recording and playing back speech—as it is being able to capture enough information about each story so that the subsequent search picks out relevant stories.

This vision shows how even radical solutions to problems can be based directly on understanding the structure and nature of the work.

session will be frustrating for everyone. For the same reason, limit sessions to about 10 people—more makes it hard to get air time.

Expect to elaborate on each idea for about half an hour, then move on to the next. Keep going until you have at least three or four alternative visions, each on its own flip chart paper.

## CREATING A COMMON DIRECTION

Doing multiple visions lets the team consider alternatives and work out some of their implications. Each vision is built by the whole team and incorporates everyone's different perspective. But at the end of a visioning session, you have multiple visions, each suggesting a different design direction or addressing a different part of the work. How do you choose among them?

In Contextual Design, you don't have to. Instead, you synthesize a new solution incorporating the best of the individual visions. Commit-

Creating a common vision is not a compromise tees have the reputation of producing mediocre designs because people compromise; instead of doing either of two reasonable designs, they settle for something halfway in between, or they incorporate a few features to make everyone happy. Synthesizing a

common vision is a way to avoid this. Rather than compromising on features, producing a design with a little something for everyone, the goal should be a design that is coherent and clean and that supports the work issues everyone identified.

The key to such a design is to treat each vision, not às a monolithic block that must be accepted or rejected as a whole, but as a collec-

tion of options that can be reconfigured and redesigned into a single solution. If the team had to choose one option over another, they would argue each person would have their own preference as to how to trade off different issues. But it's a false choice. Every vision will have impractical or unde-

sirable elements; most visions will have some elements you don't want to lose. Create a better solution by identifying elements that work, recombining them to preserve the best parts, and extending them to address more of the work and overcome any defects. The individual visions become databases of design ideas that you can draw on and recombine to come up with a better solution.²

We do this through a structured evaluation of each vision. Look at each one in turn and first list the positive points of that vision—the

reason why it's good, fits the customer work situation, solves real problems, is easy to build, or fits the skills of the organization. Even people who dislike the vision overall can find points about it that work; people who are particularly against it are on the spot to identify some points they like. List each positive

As soon as you list negatives, people start xing them

point on a sheet and attach it to the vision. Then list the negative points—all the reasons why it would be hard to build or would break the customer's work practice. People who love the vision can find a few points to dislike—it will help them to let go of an idea they might be overly attached to. List these negatives and attach them to the vision as well. List positives and negatives for each vision in turn (see Figure 13.2 for an example of the system management vision). While you're listing negative points, people will tend to start solving them— to suggest ways that the potential problem can be overcome. These ideas become important in the next step of the process, but don't let them derail you now. Write them on Post-its and stick them to the vision to save them for later.

Then look across the visions and at the positive points. Use them to identify the core parts of each vision you don't want to lose. Then look

at how to combine these points into a single coherent vision. The team will be primed to do this as a result of the discussion of positive and negative points. They'll already have ideas for how to recombine the vision. Usually, most of the elements of the visions don't conflict directly—because each vision took a

Invention is driven by recombining existing good ideas

different approach, it will be possible to bring the best parts together without conflict. Where parts you like do conflict—two different ways of addressing the same problem, for example, when it doesn't make sense to do both—you'll have to choose. But now it's a very focused choice on specific aspects of each vision. If they both support the work well, choose the simpler or the easier to implement. If you aren't sure which is better for the work, use the ideas to identify what data will help make the choice and set up customer interviews to collect it. (We'll discuss working out the ideas with customers in detail in Part 6.) The final step of visioning is to draw the new consolidated vision reasonably neatly.

![](images/253727560a93a10a027cb55bde9400aa582de94d415cd0150ef6bc5c828babab.jpg)  
FIGURE 13.2 Positives and negatives for the system management vision.

This whole process is designed to bring a disparate, crossfunctional team of people to consensus. If some team member is

hooked on an idea, be sure to include that idea in the list of starting points. In one team, one member was hooked on the idea of a large monitor displaying test states in a scientific lab—it had gotten to be a joke in the team that this was his solution for everything. Making the large monitor the core of a vision and then doing positive and negative points (he had to come up with three negatives) made it clear what real advantages the large monitor offered. But comparison with other visions revealed that those same advantages could be achieved more simply. In the end, he didn't have a hard time letting go of the idea.

## MAKING THE VISION REAL

The code is only one component of a product. A commercial product also includes the documentation and services that help people use it,

the marketing plan that publicizes it, and the testing plan that ensures its reliability. Internal systems downplay marketing and services, but they still have to help users take advantage of the product, tell them about it, and get buy-in. Internal systems also have

The vision directs concurrent activity

to roll out the infrastructure, new procedures, and new organizational structures that will take advantage of the new system. With the vision in place, all functions can start working on their parts in parallel. They can first look to see if they can do what the vision requires at all reasonably; this may require technical investigation or may require going for management buy-in. Once the team knows what's involved in doing a piece of the vision, they can choose to attempt it, leave it out, or scale it back so they get the underlying benefit of the piece in a simpler way. Then, once they've decided what part of the vision to work toward for this project, people can work out in detail what's required for their part. All through, the vision acts as a map that keeps the groups coordinated even while they work independently.

## PROCESS AND ORGANIZATION DESIGN

Particularly when the system is for internal use, the vision may imply changes to business processes or business organization. The vision offers a new way of working, and the business structure may have to change to adopt that way of working. Salespeople may have a different reporting relationship to the home office. The purchasing department may no longer be an intermediary in making a purchase. Walls between offices might be knocked down to provide team rooms. Planning for these changes can proceed in parallel to the software and infrastructure development activities that will support them (though, of course, the implementation of any changes must be synchronized).

The vision can help a commercial vendor redefine how they do business as well as what products they deliver. Commercial vendors can mine their visions for implications on new delivery mechanisms, how customer service is viewed and how to improve it, and how to improve the sales channel to address issues that get in the customer's way. If one

The vision   
directs organizational   
restructuring

customer's issue is how long delivery takes, the delivery service might be changed. If salespeople are used as information resources by their customers, formalizing the information provision as a service might be part of the vision. If technology or products developed by a third party are important to the vision, the organization can start to create relationships with these other companies.

## MARKETING PLANS

Marketing builds the market message around the vision and consolidated models (and later the User Environment Design, described in the next part). The consolidated models show what customers care about and what message will interest them. Marketing can build scenarios from sequences and base the story of the new world on the vision. The vision captures the key innovations that constitute the substance of the market message. And the User Environment Design, especially when organized into components, gives marketing a way to communicate the design as providing coherent support for particular aspects of the work. This message communicates directly to people's experience; talking about features and benefits presents the system more abstractly.

The vision shows what customer characteristics make the difference in whether they will be interested in the product or not. The models

capture qualitative data about customers——now marketing needs quantitative data to decide whether the product is viable. The vision drives surveys to size the market and make the business case: test how many customers have those characteristics and how much they are likely to spend. As engineering finishes more of the designing and prototyping, these can be incorporated into the marketing events and used as the basis for focus groups, test drives with customers, and so forth. Marketing can also use the vision for prioritization—they can split it into components and decide which components to ship together for a coherent product, and in what order.

## SYSTEM DESIGN

The vision defines what is expected of any software and hardware components of the system. Engineers can get an advance look at what demands on technology the system will make. They can start investigating technological possibilities immediately, including possible platforms, whether specific technology is sufficiently reliable and whether it can meet the requirements of the vision, and UI possibilities. Then, when the decision is made to proceed, the rest of system design is based on the vision and consolidated models, as we shall see.

The vision drives technical investigation and hardware requirements

## STORYBOARDS

A vision drawing captures the new vision as a single picture, showing all parts of the vision together. It says what the new work practice will be without showing how it will happen over time. But to design well, we want to work out the system design in the context of doing work. We want to see how it fits into the overall work task to ensure that the transition into and out of the system works and that the task stays coherent. We do this by working out the vision in storyboards. (This approach to deriving system requirements from usage is becoming popular in the industry; see, for example, Carlshamre and Karlsson [1996]; Jacobson et al. [1992].)

Storyboards show how specific tasks will be accomplished in the new world. The technique was originally borrowed from movie making and has been used by others to work out system designs.³ A storyboard captures the new procedure for doing a task pictorially, like a storyboard for a film. Each frame in the storyboard captures a single scene—an interaction between two people, a person and the system, a person and an artifact, or a system step. The storyboard frame might show the people interacting and the content of their interaction. It might sketch a system screen with annotations showing how it's used at this point. It might sketch the artifact and how it's used. Or it might just list the actions the system takes on the user's behalf.

Storyboards are based on the vision, follow the structure of a consolidated sequence model, and pull implications from other models as necessary. The vision defines what the new work is like; the consolidated sequences define the structure that underlies doing a task and the intents people achieve in doing it. To build a storyboard, choose a task to redesign that is represented by a consolidated sequence. Then

review the models and affinity, gathering issues relevant to this task. Collecting the issues resets your focus, allowing your mind to design from all the issues at once.

Then sketch out how you want to redesign the task. This is a more detailed vision, focused on the

work of this task and constrained by the larger vision. In this step, you work out the exact approach you'll take to dealing with the different issues. Sketch out two or three options, do positives and negatives, and consolidate one approach. Do this quickly—it's more focused and can be fast.

With the detailed vision drawn out, walk through the consolidated sequence step by step. Look at the intents, different strategies, and steps.

Account for the intents—if the first step of diagnosis is to find out more about the system and its history, any new system should account for this need. You could support it, by displaying system context automatically when a call comes in; you could eliminate diagnosis by implementing an expert system that can always figure out what's wrong; or you could decide that they have ways to get context already and you don't need to give them more, and leave this step manual. Look for ways to overcome problems and achieve intents more directly, within the context of your detailed vision.

Capture the work practice as you've redesigned it in the storyboard, including interactions with the system, interactions with other people, and manual steps. The goal of the storyboard is to represent the whole work task coherently, so don't limit the storyboard to only those steps that interact with the system. Sketch storyboard frames to represent each step of the new work practice.

Because each frame of a storyboard is a sketch, it limits the amount of detail the designer can squeeze into that frame. This is

intentional, just as the sketchiness of the vision is intentional. By its nature, a storyboard inhibits the designer's natural tendency to dive down into the low-level detail of each part of the system before the whole system has been roughed out. A screen sketch in a storyboard isn't a specification for the UI of that screen—it's a thinking tool enabling the designer to work out what has to happen in the user's interaction with the system at that point in the task. The UI sketches in the storyboard communicate ideas to the UI designer, who will create a consistent and comprehensible UI for the whole system later

We usually build storyboards in pairs. After finishing the whole task, the pair brings the storyboard back to the whole team for review. They walk through the storyboard, and everyone posts issues on the storyboard: mismatch with the customer's work practice, mismatch with the vision, alternative design ideas, or implementation worries. The pair then reworks the storyboard to account for the issues.

A set of storyboards for the key tasks to be supported in a new system defines how the system will work in supporting those tasks. By

telling the whole story of the task, including manual steps, automated steps, and interactions with the system, the storyboard keeps the work task coherent. Storyboards work out elements of the vision by unraveling them, laying them out step by step. They provide the next level of detail for the design. In work-

Storyboards capture all the steps needed to do the redesigned work

ing out the storyboard, all aspects of work come together: roles interact, people move around and pass artifacts, and culture influences everything. The storyboard synthesizes all these issues into a coherent redesign of a work task within the context of the overall vision (Figure 13.3).

## REDESIGNING WORK

This is what it means to redesign the work: First, understand the structure of work as it exists and the issues implicit in the work. That will

tell you what to address. Become knowledgeable about possibilities for redesign, either by learning about different possible technologies or bringing experts into the room and steeping them in the data. Then vision a new world, using the knowledge of the team and building on your understanding of the

The vision and storyboards guide the corporate response

issues. Once that's done, you can work out the implications of that vision in storyboards that show individual instances of doing the work.

The vision holds your corporate response. It shows how all the different actions you might take as an organization work together to address the user's work problem. With a vision in place, the different functions of your organization can work together toward a common goal. Each function then will follow its own process to work out the implications for its part. In the rest of this book, we'll discuss the process for engineering to develop the system itself.

![](images/0cacc36019fe1cf62229cb900738d86bedc15ab4ef955c18a46dc28a7f9384f4.jpg)  
FiGuRE 13.3 A storyboard for the system management vision. This storyboard follows the structure of the consolidated sequence for dealing with a call for help. At each step, the storyboard reinvents how that step would be accomplished given that the user can take advantage of the new system.

## KELLY'S STORY

Everybody talks about spending a day in the life of the customer, but it's very hard to do and get meaningful data. I've tried a lot of different processes and have found that the people who participate get insight, but there's no way to capture it, communicate what you learned, or use it again on the next project for the same market. Contextual Design is unique in that it gives a framework and models to capture the data in ways that are more meaningful than any other process I've used. It supports sharing and communicating the insight and lets others participate in a way they cannot otherwise.

I'm a product manager in a group building large computer systems. We wanted to address a new market segment with our product line, but we had not spent much time understanding what was important to these customers. We used the whole Contextual Design process, with a cross-functional team drawn from marketing, R&D, and manufacturing, and external facilitators to guide us.

We interviewed about 15 customers; consolidated the models and affinity; visioned new product, service, and delivery ideas for the market; built a User Environment Design for some parts; and used prototypes to test the ideas. We found the cultural model particularly useful for defining our marketing objectives, including defining the value proposition for the market. The other models were more useful to R&D in building the actual products.

The vision we produced drove marketing requirements for several different organizations. Producing a computer system for this market requires the combined effort of several software organizations, two hardware organizations, manufacturing, and service organizations. For example, we discovered how critical it is in this market to be able to add capacity easily——this recognition drove hardware requirements for ease of installation, software requirements for dynamic reconfiguration, and a manufacturing requirement for 48-hour turnaround of a new order. That will require process changes in the manufacturing organization, but they’ve put together a task force to figure out how to do it.

For us in marketing, the strongest part of the process was through visioning. This project wasn't driven by the engineering organizations, so we didn't have enough commitment to the results. No one organization felt their business depended on the success of the project. We could get individuals to buy in, but it was harder to affect the plans of the whole organization. So we found it easier to communicate the results of the vision using our traditional methods. We are getting the changes we designed into products to be delivered over the next 12 to 18 months.

I have to say that none of us had a clue how much time and energy this project would take, particularly since we had no data to start with. The results were well worth it, though. If we hadn't done this work up front, we would have had to do it later, when plans are harder to change. We're planning to use Contextual Design on our next project, but augmented with other marketing techniques and contextual interviews with people who make the buy decision.

![](images/48b7a40c749872c4a19f77d9cd5db57a784d9fab128694213185361b1b4c3989.jpg)