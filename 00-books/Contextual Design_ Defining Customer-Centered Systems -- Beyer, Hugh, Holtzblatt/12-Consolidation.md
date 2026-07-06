# Consolidation

t's remarkable that systems can be built to support large numbers of -people at all. People don't coordinate across industries to make sure they work in consistent ways. Even in a single department, people develop idiosyncratic ways of doing their job. But as we've discussed, any system imposes work practice on its users. It structures work and interacts with work in many complex ways. Since a system always structures the work of its users, and since they don't coordinate to work consistently, why should a single system work for them all? Yet we take it for granted that products and systems can be built and will be successful with all their disparate users.

Systems are not designed, for the most part, for individuals; they are designed for whole customer populations—intended users of a system in the market to which a product is sold, or in the departments of an organization. If a system can address the needs of a whole customer population, it's because aspects of work hold across all customers: common structure, strategy, and intent. A design responds to this common work structure while allowing for individual variation among customers.

The challenge is to design for a population, but meet the needs of individuals

But how can we discover these common aspects? How do we recognize them among all the surface differences in how people work? And how do we represent the common aspects of work so a whole design team can respond to them? As discussed in the last part, a design team needs to make the work of their individual customers concrete, tangible, and available for sharing with others. Without an external representation, the team has only their opinions and unarticulated knowledge of customers to base their decisions on. They have no concrete way to communicate what they know and to justify their designs. But the work models introduced in the last part represent individual customers. What models will show the work of a population?

Without the ability to see the work of the people they support, design teams are limited in what they can do. They are less able to act strategically to address the needs of their customers, taking short-term actions to advance long-term goals. Strategic action is as important to IT departments as to commercial product developers, but the motivations differ. We will discuss the issues for the two groups separately, then show how a single set of design tools meets the needs of both.

## CREATING ONE REPRESENTATION OF A MARKET

A commercial vendor supports a market—the people who are interested, or who the vendor wishes were interested, in their product. The challenge for a vendor is to address the market with a coherent set of products, supporting the customer's primary work within the vendor's area of expertise.

Providing complete support for the work is important——any gap is an opportunity for a competitor to start selling to the vendor's customers and perhaps win their loyalty. (Or, for niche vendors of products that fill gaps in others' product lines, understanding the whole work practice is important to recognize and take advantage of the gaps.) A gap in a product line can happen because the vendor's line is incomplete, because they do not have the skills to address everything about the cus-

tomers' work, or because they do not recognize how the work hangs together. For example, Microsoft dominates the office market largely because they recognized that providing a bundled suite of products would give them an advantage. Office work hangs together, so packaging a well-priced set of products that support the whole office is better than selling word processing, calculations, and presentations separately even if the products in the package aren't particularly well integrated.

Without a clear picture of the work of their customers, a vendor's grip on their market is limited. It is common, for example, to hear vendors of generic office tools say, "We have millions of users, and they all use our product differently. There is no one office user." Those who say this put themselves at a standstill. There's no way to go on to understand those aspects of work that are common. There's no way to find the common tasks that, if they were better supported, would give a single product a market advantage. There's no way to see the common flow of work that a suite of products could support directly and that would give that suite a market advantage.

It isn't just the vendors who say that their customers all work differently. People are invested in being unique, an the first thing that customers often say is how different they are from everyone else in the industry. But much of the detail that makes people different is not relevant to the common pattern and structure of work practice, and it is this common pattern and structure that make generic software possible.

When we studied configuration management, we found that some companies make it a very formal process: there are people who have the

job title “Configuration Manager," who decide what goes into a configuration and make sure it gets built and tested. We found that UNIX shops generally don't work this way—they value minimal process and a “just do it” mind-set. But, in a UNIX shop on the afternoon a base level was supposed to be finished, we

found someone walking the hallways saying: "Okay everybody, the build starts in an hour! Get your code checked in! Bob, get your testing done. We need that feature in this build. Sue, hold off on your stuff. We don't need it and we don't want to destabilize the build with too much new code. . . ."

The first organization recognized the role and formalized it as a job; the second didn't recognize the role formally, but made sure someone was responsible for performing it informally. The role is part of the common work structure of the market; the different ways of assigning the role as a job are differences of detail. A product could be structured to support both types of organizations, though it might have to be packaged and marketed differently to deal with the customers' different attitudes.

## A SINGLE REPRESENTATION IS AMARKETING AND PLANNING TOOL

When companies can't see the work of the whole market, they have no way of saying who their market is. They fall back on segmenting

Don't let individual differences blind you to common patterns of work

Segment markets by differences in work practice, not industry types

markets in ways they do understand—by demographics and market characterization of the sort we discussed in Chapter 2. People say things like, "This accounting tool is useful to small businesses; this other product is for home-based businesses." But do "home offices" work differently from "small businesses" in any real way? Don't they have essentially the same tax, payroll, and cash flow issues? And what happens when a "home business"

grows up and becomes a "small business"? Do they suddenly acquire a new set of issues? Or another division might say, "This is a query and report tool for flat files. It doesn't substitute for a database." But don't users of flat files care about data integrity? What happens when their small, flat file application is used by two people? What happens when they want to access their database with the same flexibility as their flat files? Or a company will say, "This product is for home and school use."But do people at home have the same needs as schools? Is there any reason to think that an environment of school-age kids, adult teachers, and administrators, sharing computers in the regimented time structure of a school, has the same needs as a family in the flexible environment of a home? In each case, people are segmenting the market using the only tools they have available—demographics. Without a clear understanding of work practice and work practice differences, there's no other way to segment the market.

Without a way to recognize work practice, vendors also find it difficult to address a market over a series of releases with a coordinated set

of products. "This is a data manipulation tool; that is a charting tool." Which is responsible for reducing the data into a form the charting tool can use? "This is an operating system work environment; that is an office work environment."Which is responsible for finding a file, or switching between applications, or maintaining reminders? Without a clear understanding of work practice, there's no good way to look at the whole range of customer activities and carve them up so that each product supports a distinct set of tasks and every handoff between tasks and products works. There's no good way to grow a product over a series of releases, recognizing the whole work problem and expanding support for it over time. Instead, vendors tend to drive products from customer wish lists: "Which features can we get into this version? Which one is most important? Who is yelling the loudest?" They respond to the immediate demands of individual customers, not to the coherent needs of the work practice.

Contextual Design gives vendors of commercial products the tools they need to address a market strategically. As we will see, con-

solidation creates a coherent understanding of the work in the affinity diagram and consolidated work models. With these tools, a vendor can grow a point product into complete support for a market. If a product supports one task, natural progressions

Grow product offerings to support related work

(either with the next product version or with related products) might be to support the work tasks that precede or follow the first task, to support other tasks performed by the same people, or to support others who interact with these people. The vendor can see all the issues that matter to the market and prioritize them, planning an attack that delivers coherent product versions over time. Vendors can see who the customer is and what they care about most.

Work models give vendors rational ways to segment a market. If the work practice is common, it can be represented in a single set of consolidated models that define a market. A single product or suite can address the needs of this whole customer population. Where the models identify differences—such as different cultures—they show how the product must be packaged or sold differently to different groups of people. But when one set of models cannot represent all customers, it shows that there is not one market. It shows that the work is too different for a single product to address.

With the consolidated work models of a customer population displayed on the wall, a vendor can use them like a map to show what

aspects of work they support, what aspects are the prime targets to support next, and what related work they might support in the future. A vendor could show their competitors on the same chart to reveal relative strengths and weaknesses and where the competition is vulnerable to a well-positioned

A map of customer practice supports rational decisions

product. Such a map drives a company's product strategy, just as the detailed work practice knowledge drives the structure of the company's products. Without it, marketing, like designers, operates off intuition and misses opportunities for a strategic advantage.

## FACILITATE THE PARTNERSHIP BETWEEN IT AND CUSTOMERS

IT departments exist to help the business take advantage of technology—to implement and maintain the systems that make the business run. Because IT's job is to deliver systems that support the work of the business, they may well become more aware of the processes that run the business than the departments are themselves. A department in the business is nearly always focused on getting their part of the job done most effectively, spending less energy on understanding how that part affects other departments. Even within departments, groups and individuals focus on their own job rather than worrying about how others do their jobs.

## IT CAN BE THE VOICE FOR COHERENT BUSINESS PROCESSES

More and more, IT departments are being asked to support larger business processes. It's the IT department that notices when they have to waste time delivering systems that duplicate work because the departments themselves are duplicating work. The IT department has the problem of recognizing and rationalizing the work practice of the business, so they can develop a coherent set of systems to support it with minimum effort and redundancy.

As a result, the IT department is often at odds with its clients. If a client wants something to simplify their work, but their work is part

A systems perspective reveals overlap in business processes

of a larger process, does IT optimize that one part of the process at the expense of the whole, or do they antagonize a client to make the overall process work better? IT is often the player stuck with the job of thinking about process and systems across the business. They need a way to talk to the business about

how they work and how to build information systems that not only support current processes, but provide opportunities to simplify and automate them.

IT departments have the opportunity to drive process improvements themselves. They also must respond to organizational change driven from above—from management and business process reengineering (BPR) initiatives. These efforts tend to focus on the large organizational structures: departments and their responsibilities, flow of materials between departments, and large process steps. Individuals trying to figure out how to do their jobs in the new organization are often lost and confused. They need a way to bridge the gap from the policies and directives of management to define daily actions and expectations. It's a good idea to include the people who do the job in redefining it—only they know what's really required—but their own work practice is not conscious to them. They need techniques to make work practice visible so they can design procedures that meet management's directives and work on a day-to-day basis for the people and for the job.

From this perspective, a job description for the business analyst (or the cross-functional team doing analysis) might be, "We are responsible for understanding our client's business and helping them to do it better." To do this, a business analyst needs knowledge in the work domain of the client, skill in seeing process issues that elude even those who do the work on a daily basis, and understanding of the technological possibilities, as well as

ability to design the infrastructure, or work with the technical people who can do so. It should be clear from the book so far that this is not an impossible task. Interviewing and work modeling enable the analyst to learn the business and see process issues; consolidation represents the work of the department in a stable way. By including customers on the team, and creating events for including customers, the analyst can partner with the business in process design and specification of the infrastructure, maintaining the coherence of the supporting systems.

Consolidated work models help drive consistent process design.

Departments, like customers in a market, tend to be invested in

thinking their work is unique. The highly advanced, fast-moving, innovative part of the company doesn't want to think that their work is really structured just like that of the stodgy, old-fashioned part of the company. Engineers don't want to think that ordering their complex supplies has the same structure as ordering refrigerators. So they resist using the same

Reveal common work patterns to support cross-department system consistency

system as another department uses, insisting on one tailored to them.

But if these people see the structure of their work in an external model, they can see how similar it is to the work done by others and can come to accept that the same system might actually work for both. Similarly, if people see how the work they do fits into the larger process, they can make rational decisions about what makes sense. For example, if they see how all the work they put into formatting their report is thrown out and redone by the people who roll results up into a final report, they might accept a system that applied standard formatting automatically.

The overall work structure is a backbone, showing how small systems and individual customizations are variations within the larger framework. A consolidated view of the work allows IT to be strategic about the systems they deliver, building systems with the most impact first and extending initial versions to build up complete support for the work.

"Enterprise models" are another approach to seeing consistency across departments. But enterprise models focus on shared data— important, but not the only aspect of work practice that matters. Object models showing the information infrastructure are an important part of the representation of the business, but are built up as part of systems design, later in the process. Neither of these address the common structure in the work, which, if

recognized, could lead to reusable systems across the organization.

Consolidated models become a strategic resource to the business. They show what is going on in the day-to-day doing of the work and how the work hangs together so the business and IT can have conversations about the work people do. The IT organization can maintain models that show the work of the business they support, extending them over time as new projects bring them into contact with more and more of the business.

## REPRESENTATIONS OF WORK STABILIZE REQUIREMENTS

Whether it's new systems or new processes, IT departments face the

Participation in redesign fosters buy-in to change huge problem of introducing changes to a skeptical and change-resistant customer population. People know these changes will affect the way they work on a daily basis—unless they buy in, they will find ways to subvert the new systems. People can accept change when they are part of the process of looking at the work and designing new systems that make work more efficient. Since IT is the department chartered to provide systems, it is a natural part of IT's job to raise process awareness in the departments they work with. Then the business department and IT can work together, combining technical knowledge and knowledge of the business domain to identify process problems and define process and system solutions.

Contextual Design generates representations of the work of a business that make process management and collaboration with the customer possible. It shares with Participatory Design a concern for including customers in the design of how their work will change. Consolidated models and affinity diagrams show where the breakdowns and bottlenecks are and drive design conversations about removing them. For example, the consolidated flow model might reveal that most of the purchasing department's job has turned into mechanical, clerical work, leaving no time for the knowledge work of creating relationships with suppliers. Knowing this is an issue, a team can design systems that automate the clerical work and provide the information needed to support purchasing's real job—and customers on the team can communicate the new ideas back to their organization and prepare them for redesigning their roles.

Consolidated models elevate what would otherwise be a bunch of anecdotes to reveal systemic problems: from “He's complaining about the PC support group. It doesn't mean anything everyone complains about the PC support group," to “Look at this! Everyone is getting held up by the PC support group! We have to fix this!" Making elements of work practice explicit makes their impact apparent and helps set priorities.

Move from process anecdotes to known data to drive decisions

Consolidated models give the IT department a way to talk back to the business about prioritization decisions: “I know this system is important to you. But look, it will be more powerful if we put it off

until we implement this other system here. That system will tie this whole process together and can drive your system with the data you need instead of requiring you to enter it manually." It's easier for people to be flexible when presented with a rational—and externalized——plan than when they are just told they can't have what they want. A shared

Make the big picture concrete to help departments prioritize their parts

Models reveal work issues so customers can choose what to redesign

representation of work can foster a partnership between business and IT, in which both focus on the work of the business and how it can be improved and supported.

Making work practice visible stabilizes shifting requirements. Client organizations don't change requirements on a whim—they are trying to respond to real work issues. But without a way to see the underlying structure of work, everyone responds to the immediate current pain without looking for the underlying problem causing the pain. One-shot solutions to point problems always run the risk of becoming obsolete quickly. Stability

depends on seeing how work hangs together and responding with a system that supports it coherently. An old story has it that one company employed an army of mops to clean up spots of water appearing on the floor before someone noticed that the janitor's bucket had a hole in it.

Requirements change because they are trying to patch surface details, and tomorrow a new detail may seem more important. Understanding the structure of work leads to supporting work at the level of structure, which rarely changes, and suggests structural changes that radically improve the work.

## SEEING THE WHOLE

Customer data informs a team what kind of system is needed and reveals the detailed structure of the work the users do. Both commercial and IT organizations can use the data to learn what kind of system to deliver. But customer data also reveals the pattern and structure of work. It guides a team in designing the detailed structure of the system they develop.

The work practice of a customer population has its own coherence. It is a web of interrelated parts. Change any part of it, and

everything else has to shift to adjust. To respond with a coherent system, designers need to see the interwoven pattern of work as a single whole. Whether designers support internal customers or an external market, they need a guide for what we will call systemic thinking: seeing the pattern of customer work practice as a unified whole and responding to it with a coherent system. Systemic thinking views both work and system as coherent wholes that respond to each other, not as a collection of features, each meeting a specific need.

With a coherent understanding of work, designers can recognize people's different work styles and strategies and account for them in the system. They can check that the work still hangs together and anticipate what may break as a result of the new system. They can balance needs against each other, recognizing which have the most impact on the work as a whole. No list of needs or requirements will give designers this synthetic view; treating each "need" or “requirement" as an independent entity makes it too hard to see how they interrelate.

The first step in systemic thinking is to develop a coherent understanding of work, based on actual customer data. That's what consolidation does.