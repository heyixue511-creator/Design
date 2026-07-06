SHAHAFGAL

# Footholds for Design

In a design environment, knowledge is generated, enacted, and reflected on in an ongoing process between the materials and the participants' intentions and attached meanings. Learning occurs when users create concrete things, such as drawings and models based on their knowledge, and then reevaluate that knowledge based on what they have just learned.

In conjunction with Donald Schön (see Chapter 9), Shahaf Gal conducted a series of studies of engineering students çompleting design projects. 'The story of Ray's bridge, recounted in this chapter, was one of four cases that Gal analyzed in detail. Ray's experience in a 3-week student design competition offers us a distilled and visible version of what happens in more sophisticated and hidden ways in every design project. The problems that Ray grapples with have direct mappings onto software-design contexts: top-down versus bottom-up approaches; the practice of basing new designs on standard examples; the temptation to use matcrials because they are available; and the struggle between adding features and simplifying.

Ray goes through a directed but winding search, adding and dropping concerns that constrain his design, being surprised by the results of explorations, and making messy decisions that change over the course of the project. He is a student, not an expert, and his lack of sophistication helps to reveal the process more clearly, since the breakdowns are more visible without the facade of expert polished performance. We can clearly see the tradeoffs between different concerns, the abandonment of a path when it seems to have reached a dead end, and the pain of getting stuck. As David Kelley points out in Chapter 8, these phenomena happen to every designer, and are not to be avoided.

—Terry Winograd

![](images/f72bd59677d23cbd76e2f64f88ed24f120e781e692ce031d56267fbfef094262.jpg)

OMPUTERS CAN PLAY AN IMPORTANT ROLE in the design proCess, as image footholds. In a design environment, knowledge is gener  
ated, enacted, and reflected on in an ongoing process between the   
materials and the participants'intentions and attached meanings.   
Learning occurs when users create concrete things, such as drawings   
and models, based on their knowledge, and then reevaluate that   
knowledge based on what they have just learned. If we are to respond

effectively to design situations, our tools—including those based on computers—need to be aligned with the process of the design inquiry.

An analogy for the role of computers in a design environment is that of rock climbing. A rock climber knows that she wants to get to the top of the mountain. She chooses a route for the climb based on her knowledge when she is at the bottom of the hill. As she climbs. she constantly faces new situations where she needs to choose a new footing to proceed. She seeks footholds that are safe and stable on which to pause momentarily to catch her breath and to plan her next step. Each foothold is both an endpoint that sums all the steps she has taken so far, and a point of departure from which to plan the next one. Her choice of a new foothold is determined by the steps that she has taken to get to her current position on the mountain in relation to her goal. She is also guided by her past climbing experience, and she uses her rock-climbing tools as an anchor. At each step, she needs to plan her next step considering what is in her reach; each step presents her with new and different conditions. Thus, a rock climber continuously faces a challenge of making future decisions based on the here and now of her foothold.

Like the rock climber, designers face similar challenges in design settings. Situations of design evolve constantly as a designer secures a point in the design on which he feels safe relying, then moves on again. The following story of a student designing a bridge illustrates the use and value of a computer program that serves as a design foothold. The general principles discussed at the end of the chapter show how the lessons go beyond this case.

## The Riddle of Die Brüicke

Ray was a senior in mechanical engineering at the Massachusetts Institute of Technology (MIT). As a high-school student, he gained experience working with wood, especially with balsa wood. Ray designed and constructed a bridge as part of the fourth annual bridgedesign contest at MIT in the winter of 1988. This bridge contest was his first; he worked by himself, in competition with 16 other students from different departments within the School of Engineering. Their task was to build models of bridges that could best withstand a test load. Participants were given a kit of materials containing strings, wire, glue, and a variety of wood blocks—basswood, balsa, and pine. They had 3 weeks to complete the project.

Students were encouraged to use the engineering laboratory and Growltiger—an expert-system engineering program—to build their models. Growltiger's purpose was to serve students as a design tool and as a virtual laboratory for experimentation in structural engineering. As a virtual laboratory, Growltiger is programmed as a channel of guided discovery, where the system guides designers to enter the necessary data for structural analysis, to manipulate the appropriate computational components, and to evaluate the results against known parameters of structural engineering. The program also assists the designer by providing a default setting that offers standard-sized beams, properties of standard construction materials, and four types of indeterminate structures. Thus, students can test how their designs behave in accordance with a range of standardized degrees of tolerance. The test can serve as a starting point from which students try to optimize the structure. They can then change the shape of the structure, the loading, and the stiffness. Within seconds, the new structure can be analyzed and tested.

Students can also use Growltiger as an open-ended design tool, building their own structures. With the exception of curved supports, students can design the structure, and decide on the kind of material and the loading system; the program will display the deflection. (See Figure 9.2).

## Top-Down Design

Ray chose a strategy for building his bridge that attempted to address a range of issues. He strove to manage effectively the time and manufacturing constraints (gluing, amount of work), while creating a strong bridge that was beautiful and original. He aimed to build with a clear design concept. As a partial response to the tradeoff, Ray searched for a bridge with simple structure that would be easy to manufacture. In a design notebook that he kept throughout the contest, Ray wrote at

this early stage:

• Main problem: TIME! TIME! TIME!

• Main constraint: Bridge must be finished in time!

• Main tradeoff: Aesthetics and partial stability versus speed of construction

Ray believed that he could build the bridge in a classical top-down approach: arrive at a concept, prepare a few alternative designs, narrow down to one design, work out its details, check the materials available, and move on to manufacture the bridge.

What I originally proposed was a clear top-down approach. You start off with comparison of main frames, which means main ideas for designing a bridge, as I did here with several design sketches. For example, take those six ideas of bridges, then take the two best ones, and then elaborate on those to get a good idea of how the geometry looks. Then, go back to the material. From there on, it's a circle among material, manufacturing, and the design; they are all factors from then on, but only from then on. That is a classical top-down approach.

Following this top-down scheme, Ray started by collecting ideas about bridges, and searching for a bridge-design concept. He watched a video of the previous year's bridge contest, looking especially for the mistakes participants made in their design, and he leafed through a book on bridge designs. The Roman arc bridges caught his attention first—they last long, which is proof that they work, he reasoned. Following more reading, he contemplated two other kinds of basic designs—the bow bridge and cable-stayed bridge—and leaned toward the latter in which he had more trust.

After his search, he decided to stick with one general structural idea: to use twin towers—a two-legged bridge—in his design. The concern about settlement of such a bridge introduced the idea of a hinged center span so that each tower would act as an independent element in carrying the load. Given these three considerations, he drew his first design: a two-towered, cable-stayed bridge with a hinged center span (Figure 11.1).

Ray soon realized, however, that the hinge mechanism would destabilize the bridge, and would require much construction work. Still worried about the uneven settlement of the towers, he considered a bridge with a freely suspended span that would rotate and compensate for the settlement. The bridge would be like an arc, and would swing back and forth to compensate automatically for the settlements (Figure 11.2).

![](images/508c10d4caa8e32da33f7e0409c8c0371f0178208f904c8ce2f8b60937ed1d8d.jpg)  
FiGURE 11.1 Fan Cable-Stayed Bridge with a Center Hinge Working with sketches, Ray could explore both the visual and mechanical properties of his proposed designs. This bridge had a certain elegance, but the hinge could destabilize it.

Time constraints and concern about the strength of the strings caused Ray to drop this idea altogether. He decided to tolerate the settlement problem as a constraint, and remained with cable-stayed bridges.

He then tried another angle on bridges, seeking beautiful bridges. Hyperbolic bridges and classical cable bridges—such as the Golden Gate Bridge in San Francisco—attracted him the most. In his design notebook, he experimented with cable-stayed bridges arranged in hyperbolic patterns. Ultimately, however, he found this pattern impractical because the nearly horizontal members could carry only small loads.

Feeling the pressure of time, Ray dropped the search for aesthetic bridges and focused on function: cable-stayed bridges with vertical tension members. Ray then placed an additional constraint on his bridge: to use as much as wood and strings as possible, for maximum strength. The kit had plenty of materials, and he liked to include horizontal tension members:

![](images/f7b507dc6ff69a806d707d87ec4a1d93713e774ea6d32679c052b7dee312cd25.jpg)  
FiGURE 11.2 Arc Bridge Each half of the arc could swing back and forth to compensate for settlement. This rough sketch was an attempt to solve a specific technical problem, as a prelude to a more comprehensive design.

![](images/cfe92bb02e6b8487bd9712999ff7ff4042fc274c3cc9b53bb74b4f658c04e0d6.jpg)  
FiGURE 11.3 Suspension Cable-Stayed Bridge The classical suspension bridge was aesthetically pleasing and made use of the string as a tensile member. In looking for the best overall design, Ray was balancing constraints in several different dimensions, including beauty, strength, and feasibility of construction.

I am trying to make the maximum with the material that I have been given. The string is the longest piece of material I've been given, and it's a tensile member, so I want to take advantage of it. You could design it without strings, of course: I just believe in using all the material.

The bridge design was then changed into a suspension bridge, as in Figure 11.3.

Ray eliminated this design soon after its inception, because a top cable would weaken the bridge—the bridge needed to be very large and the vertical strings to be very long, and the forces acting on them would be very strong. A few days into the contest, Ray was stuck. Time was becoming a critical factor, and his brainstorm sessions had resulted in neither a clear design nor any elaborate specific structural constraints. Ray decided to change his general approach.

## Simulation as a Design Tool

Ray now turned to Growltiger to help him choose from the various designs. His decision to use Growltiger for that purpose did not come easily. After seeing a demonstration of the system, he felt a general mistrust of its capabilities and usefulness. Growltiger, he reasoned, did not design; it simply helped the user to evaluate design parameters. In addition, he surmised that the system would not be useful for constructing the bridge, because its design model was too simplistic to match an actual bridge in its environmental context.

At this point, however, Growltiger proved useful. Ray prepared six preliminary models of the main bridge types, each reflecting main modes of handling load, and had Growltiger predict their success using default material properties. During the comparison of the designs' general structural behavior, he noticed that two designs showed the greatest strength. He therefore narrowed the possible bridge candidates to two designs: the cable-stayed bridge and the girder bridge.

He then ran a comparative analysis of the two bridges, elaborating and changing their design, and testing various structural options. The bridges, he found, were both strong, but they behaved differently:

These two performed well. The girder bridge was decent, too, to my surprise. It's the simplicity that gives it a rigidity that's amazing. Looking at how it bends and how it behaves, I could see how stable, it would be— what the overall performance would be.

Ray was using the computer as a medium for reflection, in which to explore the kind of surprises that Schön describes in Chapter 9. His conversation with the materials (even in this simulated medium) led to new insights and provided a way to test his specific design ideas.

## Conversation with the Materials

After using Growltiger, Ray realized that bridge construction must begin from small components of the bridge. Most important, he realized how critical it was to link the overall design approach with the process of constructing the pieces of the bridge. This realization was the catalyst for another shift in Ray's approach. He changed the direction of his work from top-down to bottom-up, as he became concerned with construction issues, which he had thought he could leave for later. He also began to have second thoughts about building a cable-stayed bridge that relied solely on strings as the main system to transfer the load. The strings, he realized, had limited reliability as tensile members, especially because the strength of the bridge largely depended on the string attachment to the wood, where the stress will be concentrated. This shift in approach brought about a change in Ray's activities. Ray now needed to test the various components of the bridge. He decided to use the physical laboratory to test the performance of the deck and the supports, which he believed were important to any bridge. He started testing generic examples made of wood.

When you do experiments, you get an idea of the material. That's something Growltiger doesn't give you at all. You build the box, touch the materials, glue them. I got a lot out of it.

The laboratory tests provided him with a deeper understanding of the structural behavior of the beams and ribs for his deck, which could not be provided by Growltiger's simulation. For a structure of the deck, he compared three alternative approaches. Based on the results, he eliminated two options and decided to go with the box girder, which had unexpectedly proved to be the strongest.

Ray's concern about the weight of the bridge and the use of strings as the main material for the tensiles caused him to recheck the literature on cable-stayed bridges for the kinds of tensiles and cable arrangements used. He learned that the most effective cable arrangement for carrying load keeps the tensiles vertical to the deck. By this point, his bridge design had become detailed and definite: the overall design would be a cable-stayed bridge, with a box-girder deck, two towers, Hsupports, and many tensile members made of strings (Figure 11.4).

![](images/c49374afcc831ed50ffee3138b77465f6c51efe23472fcfc043ff129cb5e4af7.jpg)  
FIGURE 11.4 Cable-Stayed Bridge with H-Supports and Strings Ray's experiments with the physical materials led him to consider this design, in place of the earlier suspension design. Working in the laboratory gave Ray insights about practical construction feasibility that were not provided by the computer simulation.

Following his experiments in the laboratory, Ray remained concerned about the use of strings to support the towers. At first, he tried to calculate the load that the strings would carry. He returned to the problem of how to attach the strings, and could not find a solution. At that time, he considered dropping the idea of a cable-stayed bridge. But he could not tolerate the thought of omitting the strings.

I could not let go 100 feet of worthwhile material! So, I looked for a different solution, and that was the first time that I came up with the idea, "Why not use an additional bar across, and use vertical strings?"

Ray then planned one deck on top of the load-carrying deck, and another below, from which 30 to 40 strings would link the load-carrying deck with the bridge's deck. That design would use the strings and the remaining basswood. This idea also linked and resolved many of his earlier concerns about structural forces, use of strings, and use of as many vertical tensiles as possible.

I didn't come up with the idea of vertical strings. It came from constraints propagation—from the top and from the bottom. It just suddenly popped up. I stuck with it because I felt good about it. All the problems I was worried about before—the materials, strings that I had, vertical alignment, vertical force performance—were solved by this design.

Ray's bridge design, which he called Die Bricke (the Bridge), now looked like Figure 11.5.

![](images/78e8f84ebb7a3b3c945408613c5b97c8c6f3dc4461312320de0ea6e95540f691.jpg)  
FIGURE 11.5 Triple-Deck Bridge with Strings as Vertical Tensiles Ray was led to this design in a creative leap (see Kelley's discussion in Chap ter 8) that grew out of his persistent focus on how to make use of a single design element—the strings.

GAL  
![](images/bfb0b1bcffabeb9ccd55e43b66794e57b4888eb903b742dd944c93273f10c983.jpg)  
FiGuRE 11.6 Ray's Final Design Structural analysis, construction concerns, and a desire to use all of the available materials all played a role in producing the final bridge design.

In the final moments before the contest, Ray decided to add trusses, which he had considered previously, to strengthen the support of the towers. His final bridge is shown in Figure 11.6.

At the testing session that culminated the bridge-design competition, Ray's bridge drew much attention from other participants and from the audience. It passed the first loading test, but failed in the second round, when both ends of the deck were crushed. In the overall contest, the bridge came in fourth place.

## Growltiger as an Image Foothold

This detailed case illuminates the many and messy decisions that take place over time in a design situation. The process of design evolves as a process of identifying emerging new questions to address. Through the task, a personal design world is created within which answers are sought out with the use of tools (Figure 11.7).

The personal design world is bounded by the designer's tools and design knowledge. The challenge of the situation is to create a way to test a proposed design solution—which in turn generates new questions. Each point of testing requires the designer to pause on the question, while considering future design questions. She uses design tools, drawings, and models to create design pauses that momentarily freeze the knowledge, and that represent a culmination of the knowledge gathered thus far. Engineering drawings, geometric displays, and algebraic computations assist engineers in maintaining an image, a map for orientation, and a language for explaining the design in the process of work.

![](images/f59ac25cb3bc4f3b18eea09fc52d2179350e089f970c94e6fcde1ff192cb4a67.jpg)  
FiGuRE 11.7 Ray's Personal Design World Ray's design world is composed of the tools and design knowledge that he applied to the bridge problem. Each component can lead to new questions and new solutions.

Reflecting on Ray's experience, it is interesting to observe his use of the computer. Ray used Growltiger to hold images of his design ideas, to test their quality, and to set constraints on his work. And-unintended but perhaps more important—his use of Growltiger shifted his design process. Ray first attempted to work top down. Time constraints and his inability to yield enough concrete constraints on his bridge design caused him to rethink his design approach. When he got stuck, Ray used Growltiger to come up with basic bridge-design ideas that guided his work. From the bridges' simulated performance, he learned about their load mechanisms: the cable-stayed bridge using cables to transfer the load, and the girder bridge using its rigid beam. This knowledge led him to try alterations on each bridge.

The session with Growltiger turned out to be important to his work in another way: It placed the first concrete design reins over his work—from there, he worked within the conceptua! frame of these two bridge designs.

Growltiger also served as a preliminary trigger to a moment when—not by intention—all Ray's bridge design theories and work strategies amalgamated into one cohesive image of a bridge. Growltiger provided the critical piece: It was an image foothold in the jigsaw puzzle that he was putting together. He used the computer to trigger, unintentionally, a critical reflective moment that allowed him to focus on a bridge design. It also provided him with a reflection of his design strategy. The design strategy and image foothold are part of the same design initiative. They are not easily separated, because it is the strategy that gave birth to the image, and it is the image that informed the strategy.

A significant challenge exists here for software designers. They need to create tools that assist designers to reflect on past steps, and to inform plans for the next foothold—while allowing for the designers creativity to emerge and to be tested in an intentional way.

## Suggested Readings

Ken Baynes and Francis Pugh. The Art of the Engineer. London: Lund Humphries, 1981.

Shahaf Gal. Building bridges: Design, learning, and the role of computers. Journal of Machine-Mediated Learning, 4:4, 1991, 335–375.

Chris Jones. Essays in Design. London: Wiley, 1984.

Donald Schön. The design process. In V. Howard (ed.), Varieties of Thinking. New York: Routledge, 1990.

About the Author

![](images/31fbf7db3bbf35cb4121bac9d5de79a18788b963300ca648185a82219bc37bf0.jpg)  
Shahaf Gal directs the Computers for Instruction Department of the Centre for Educational Technology in Tel Aviv, the largest educational computer research and development company in Israel.