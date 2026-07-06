# DESIGN STARTING POINTS

Some guidelines are about shaping your attitude toward or your perspective on design; others are more to do with helping you decide the shape of controls or widgets. To illustrate the range of advice available, consider the following design pointers.

Design for truly direct manipulation. Direct manipulation revolutionized the desktop experience. The blinking command line cursor was replaced by a graphical interface where the user could point and click, drag and drop. These are successful not only because they make the functionality of the system visible, reducing load on short-term memory, but also because their mode of operation fits well with people’s desire to interact and manipulate the world in direct, tangible ways.

The user experience of GUIs on a desktop, though, does not really come close to the sorts of direct manipulation we carry out daily in the world. We touch, pick up, examine, place and even throw objects. Mobiles of the future could offer a far richer experience; as Hiroshi Ishii puts it, we could ‘‘turn the world itself into an interface’’ (Ishii and Ullmer, 1997).

Direct combination, for example, has been proposed as a means for hyper-direct manipulation (Holland et al., 2002). Point at an object – say a document – with your mobile to select it; point to another object – say yourself – and the document is automatically emailed to you.

Alternatively, simply allow the user to see their body as part of the interface (this has been termed ‘embodied interaction’). Already there are simple consumer products demonstrating this approach – take Sony’s Playstation EyeToy, for example, with gamers using hand gestures and other body movements to interact with the software.

Design for ecological use. Recognize that the user will have other resources to hand as well as their mobile – from documents to signposts, from landmarks to desktop computers. Consider ways of using these resources – for example, how could mobiles be used to capture information relating to the physical world around them and then use this to access information resources?

Design for maximum impact through minimum user effort. Many usability guides encourage designers to keep things simple. However, it is easy to turn this advice into tedious, limited and banal designs. As we will see in Chapters 8 and 10, though, it is possible to have engaging, flexible interaction frameworks which are still simple for the user to understand and use. ➤

Design for personalization. Mobiles are personal technologies – users develop a greater sense of attachment to them than to other computing devices they encounter. Devices and services should allow users to adapt and personalize them both in terms of their look (note the popularity of altering ringtones and screensavers on phones) and functionally, setting up menu options, etc.

Design for play and fun. Users will appreciate the opportunity to have fun with their mobile. Fun involves a sense of enjoyment, pleasure, looseness and lightheartedness. To enhance the fun in your design, consider, for example, alluring metaphors, compelling content, attractive graphics, appealing animations and satisfying sound (Shneiderman, 2004).

Design for one-handed use. Often, preferred use will be one-handed (even for devices that offer two-handed use). Even when there are other options available (e.g. stylus) it is worth designing as if only one-handed use is possible, as this can force you to focus on direct, simple designs (Nikkanen, 2003). ■

Another way to reduce the seemingly overwhelming set of design possibilities is to draw on the past experience of others. Large numbers of guidelines already exist to point toward effective design choices: most focus on non-mobile systems (but are still often applicable); some deal more directly with mobile issues.

One sort of guideline provides high-level advice; these are design ideals or principles that will help you question the fundamental roles of mobile services and the way these services should be delivered. We saw some of these thought-provoking questions in Chapter 1 when we explored what mobiles could or should be. Other designer aids are much more directed – for example, many mobile platform developers have written interface-style guides (see Box 4.4 for two example excerpts). The International Standards Organization has also been actively involved; adhering to their advice can not only improve the user’s experience but also enhance the credibility of your designs as well as the process pursued in developing them (Bevan, 2001).

## BOX 4.4

## PLATFORM DESIGN GUIDELINES

Many mobile platform and product developers have published user interface guidelines on the web. Below are two extracts; in the Resources section at the end of the book we give a list of URLs to others.

Extract from the UIQ (User Interface platform for Symbian devices) guide for menu presentation:

Make the text for menu commands as short as possible. ➤

Use an ampersand (&) rather than the word and.

Use dividers to group similar menu commands together, and to separate them from commands that are unrelated but appear on the same menu. Don’t overuse them. If you’re starting from the menu layout below, a useful rule of thumb is that you should add no more than one extra divider.

Do not use ellipses (. . .) to indicate commands that lead to dialogs. This is another simplification in UIQ. A menu command is a menu command, whether it leads to instant action or a dialog.

The Delete menu command should always be the final command on the application menu, separated from other commands by a divider. Change the command type to reflect the type being displayed, e.g. Delete contact or Delete message. (Symbian)

## Extract from the Microsoft Smartphone menu guide:

On Windows Mobile-based PocketPCs, a pop-up menu displays additional commands for a screen item. The pop-up menu appears when a user taps and holds the stylus on the screen item. If the user taps any other area of the screen, the pop-up menu disappears. Consider the following when you include pop-up menus in an application:

Where possible, display the pop-up menu to the right of and below the screen item.

In general, commands on the pop-up menu should also be available from menus and buttons on the menu bar. For more information, see Menu Bars.

To minimize stylus movement, list commands from top to bottom in order of expected frequency of use.

Actions that are difficult to recover from, such as delete, should be placed at the bottom of the pop-up menu. (Microsoft, b) ■

In terms of managing the design space, you have to cope with the dual nature of the interaction design process. First, design can be a very fast-paced, energetic activity. You will often find yourself in participative, collaborative sessions with groups of people coming at the issues from different viewpoints – marketers, software engineers, end-users – with the ideas flowing freely. Whiteboards will be filled with colorful sketches; flipchart papers will be rapidly written on, torn off and placed round the room; and Post-it notes will be doodled on and stuck onto some other design artifact.

In such an environment, it’s very easy to overlook a good proposal, or to lose the design history – the steps you took and the reasoning you went through to get to your design. There are a number of techniques, called design rationale methods, that can help capture the designs and the thinking behind them as the design progresses (see Exercise 4.2) (MacLean et al., 1989).

The second face of design is far more introverted – design at times is a very quiet, considered process. The documents you generate during the exciting, creative sessions are used as the basis for reflection. Away from the dynamic environment of collaborative sessions, alone or with others – a user or another design team member – you can review the rationale behind the current designs. Are they really well founded? Is there enough detail for the next phase? What about that initial design we rejected – perhaps it does have some merits?

## EXERCISE 4.2

## DESIGN RATIONALE

QOC is a design rationale method (MacLean et al., 1989). Its three elements are:

Questions: key design challenges

Options: potential answers or solutions to the questions

Criteria: ways of assessing the alternatives.

The analysis is presented graphically with lines drawn between the options and criteria. A solid line indicates a positive connection (option satisfies criterion) while a dotted one signals a negative assessment (option does not satisfy connection). Figure 4.1 shows a partial analysis for a mobile weather service question. Complete it by specifying options and drawing lines between these and the given criteria.

![](images/3d82a1610e8a40ad33d2858e3a8e5c6fcddf77c3034120510cde44a6234ebc20.jpg)

Comments: in thinking about options, accommodate both the location(s) and time periods the user may be interested in. Think too about supplementary detail that is not shown on the main screen but accessible from it. ■

## 4.4.2 PROTOTYPING

It’s easy to think you have a good idea, fully formed and clear, while it’s still just in your head. When you try to write it down, though, you will often find it hard to express your thoughts in a simple way. Usually, the problem is twofold: there are conceptual weaknesses with the ideas and they need time to mature; and you need to experiment and refine how you articulate your thoughts.

Drafting out a document can help you with your thinking and improve the way your ideas are expressed. Some people don’t like showing early drafts of their work to others; they want to perfect it before exposing it – and themselves – to an audience. But early and repeated feedback from others is a sound way of working toward a better final document.

Interactive system prototyping is like document drafting. The purpose of a prototype is to pin down the design team, to make them articulate their proposals in forms that can be used and reviewed by others. Prototypes are the fuel of interaction design – vital in driving the progress, in generating and improving ideas and in involving people. Indeed, Daniel Fallman argues persuasively that prototyping – what he calls sketching – is the archetypal design activity, the core process that allows a designer to understand the problem and frame a solution (Fallman, 2003).

## BOX 4.5

## WHAT IS DESIGN?

Daniel Fallman reviews alternative perspectives on design, identifying three main standpoints (Fallman, 2003):

As a scientific process (the ‘conservative account’)

As an art form (the ‘romantic account’)

As an ad-hoc activity, as he puts it ‘a bustle with reality’ (‘the pragmatic account’).

As a designer, you might then see yourself as one or more of the following:

A scientist or engineer who works progressively from a set problem toward solutions, using guidelines, design knowledge and a scientific, rational approach

A creative genius, an artist who mysteriously or mystically brings a product to life, using your craft knowledge and imagination, inspired by art, music, poetry and drama

A ‘bricoleur’, a person who tinkers toward a solution, using tools and materials to hand, engaging with the situation (a thoughtful ‘hacker’, if you will).

Fallman argues that none of these accounts is adequate on its own. He presents a helpful notion of design as an ‘unfolding’, where the problem and solution are not seen as separate but evolve through a process of ‘sketching’ (prototyping). ■

Prototyping needs to start early in the design process and continue throughout. There are all sorts of ways that prototypes can be presented – from a paper sketch to functional, computer-based ones which users can interact with (Svanaes and Seland, 2004). Particularly in the early stages of design, it’s important to steer clear of focusing on the final system implementation. Thinking about implementation too early can reduce design quality in two ways:

Good proposals can be stifled by a resistance to any design that might not be fully implementable in the development environment – cries of ‘‘it can’t be done!’’ from your software engineer colleagues. In reality, even when there are technical limitations, it is often possible to code up the essence of a great implementation-independent idea.

Looking to the implementation can also lead to a low-level mindset of making the widget shape the focus, rather than the relationships between a user’s action and the system’s reaction. This is a bit like a house builder trying to position light switches before the room’s beams are fitted together.

![](images/66e136f98cc2278e4f5e0d5939533ce03fdd378860ddde128a21bdd1f6cb9630.jpg)

![](images/02fd336c153a3dc4f4e160897207f57f59f05c6148889d9ecdfd1a72bf58c530.jpg)  
FIGURE 4.2  
Examples of mobile prototypes  
Left: paper-based prototype for a peer-to-peer local search application. Right: contrasting with this is a physical working prototype where the user interacts with the handset and views results on the device’s ‘screen’ via a head-mounted display (Nam and Lee, 2003)

While you should keep away from implementation considerations as long as possible, that does not mean that every prototype should not be as realistic as possible. The comments you get from your users will be about the specific prototype you show them, the reactions and suggestions being very much driven by its actual form and features. For mobiles, this desire to produce prototypes with realism is driving some innovative new prototyping techniques, as we’ll see in Chapter 6.

## 4.5 EVALUATION

Prototypes, however simple, are there to be judged. As design proposals emerge, they need to be assessed to see whether they achieve what they set out to achieve. A big part of this process involves asking users to evaluate them, but there are other, less costly techniques for gaining rapid feedback on what works and what is likely to cause user problems. Again we give below a flavor of what’s involved, and talk more about issues and methods later (see Chapter 7).

## 4.5.1 TESTING WITH USERS

Standard, conventional testing practice – for the kind of interactive system you have on your desktop – involves bringing representative users to a usability testing facility, presenting them with a prototype and asking them to complete some specific tasks. Their completion times, their accuracy and the sorts of errors they make are all recorded for later analysis.

This quantitative data might be compared with the performance seen in competing designs in order to work out which of the proposals is best. Alternatively the design can be judged against some prior performance levels set by the team (e.g., ‘‘the average completion time should be 20 seconds’’, or ‘‘from out-of-the-box to network-connected should take no more than 5 minutes’’). Users’ subjective responses, the things they say about the system, can also be scrutinized; these qualitative insights can further help shed light on what works and what doesn’t.

But are usability labs and conventional testing approaches really appropriate for mobiles? Surely only on-the-move, in-the-wild evaluations are useful? While such streetwise evaluation methods are essential, a conventional usability laboratory can still be very effective. There will be many details of a design that are best explored in isolation from the distractions of the real world where the mobile will eventually be used. Take the case of a project to develop a wearable mobile for service technicians (see Figure 4.3). Lab-based experiments were used to find the smallest usable size for buttons on the touch screen panel; it turned out to be 0.3 square inches (Fallman, 2002).

There will also be cases where it will pay to use a lab to assess the relative advantages of a series of potential designs before embarking on a more costly field-trial. For example, researchers who

![](images/df95008a77cd57cf6b5f88c2acd59eab5c26bcafe50f4030f81506e217fa782f.jpg)  
Mobile wearable for service technicians (Fallman, 2002)  
FIGURE 4.3

![](images/f38f660910c76618309e92a728b32bf28b3af09794d3be085e8f7208ee274895.jpg)  
FIGURE 4.4  
Haloes for better map navigation (Baudisch and Rosenholtz, 2003)  
The Halo technique (left) was compared experimentally to an alternative design (right). Haloes graphically indicate both direction of target and distance, with closer targets being represented by smaller arcs. The alternative approach uses arrows combined with numeric indication of distance. The Halo approach led to time savings of 16–33%

developed the Halo technique – a method for giving mobile users information about the proximity of landmarks on a map (see Figure 4.4) – used conventional, controlled scientific methods. A handheld display was emulated and presented to users on a desktop computer screen; the performance of the design was compared with another prototype that gave less sophisticated landmark hints (Baudisch and Rosenholtz, 2003).

You will, however, almost certainly want to see how users cope with your proposed mobile in realistically demanding situations. Taking this to the extreme, Jason Pascoe and colleagues studied the use of a PDA-based wildlife tracking system for ecologists in Africa: these users interacted with the system, recording their observations while close to wild animals (Pascoe et al., 2000). How your users really cope with the system while in the wild, surrounded – be it by animals or cars – amidst the heat of the day, or the cold of an early city morning, will be rather different from their reactions while sitting comfortably in a softly furnished test suite.

There are other challenges for mobile evaluations (Thomas and Macredie, 2002). While it’s easy to measure performance in terms of time, how do you measure attributes like ‘unobtrusiveness’ or the device’s effectiveness at providing ‘ambient awareness’? Think too about study duration: typical lab-based studies last between 15 minutes and an hour, but you might be interested in how your users adapt and adopt your services over much longer periods. In one six-week mobile phone study, for instance, people’s perceptions of mobile services favorably improved over the period of the study (Palen and Salzman, 2002). To help track such changes, the researchers used a voicemail diary, encouraging participants to phone in and record their thoughts on the service, and rewarding them one US dollar for every comment.

## 4.5.2 TESTING IN THE ABSENCE OF USERS

Regardless of whether they are brought into the lab, or followed in the field, involving users is costly – it takes up your and their time, and you often have to pay them to participate. Some evaluation techniques do not need a user to be present and can provide rapid insights into the design qualities.

Scott MacKenzie demonstrates, for example, the usefulness of analytical models in determining the efficiency of different text entry methods for mobile devices (MacKenzie, 2002). He shows how to calculate the KSPC (key strokes per character), which is the average number of basic input actions, such as touching a key – like a mobile phone button, for instance – or gesturing with a pen-like stylus, needed to enter a text character. We won’t explain here how the calculation is made; the point is that while these sorts of model approaches do not replace user testing, they can cut down wasteful repeated studies. As MacKenzie puts it, ‘‘. . . potential text entry techniques can undergo analysis, comparison and redesign prior to labor-intensive implementations and evaluations.’’

In passing, if you interested in text-entry efficiency, it is worth looking at the KSPC for a range of common entry mechanisms, as shown in Table 4.1. As MacKenzie notes, it is likely that the methods with the lowest KSPC – the least effort for users – will give the best throughput of characters; from his results, then, the best approach is the unistroke method (gestures with a stylus) used together with word-level prediction.

TABLE 4.1  
Keystrokes per character (KSPC) comparison of text entry methods (adapted from MacKenzie, 2002). The smaller the value of KSPC, the more efficient the input technique
<table><tr><td>Interaction technique</td><td>KSPC</td></tr><tr><td>Multi-tap</td><td>2.0342</td></tr><tr><td>T9</td><td>1.0072</td></tr><tr><td>QWERTY</td><td>1</td></tr><tr><td>Word prediction (keypad, n = 10)*</td><td>0.8132</td></tr><tr><td>Word prediction (keypad, n = 2)</td><td>0.7086</td></tr><tr><td>Word prediction (stylus, n = 10)</td><td>0.5000</td></tr></table>

∗n is the number of alternative word options displayed in schemes that use word prediction.

In addition to model-based, performance-predictive schemes, other popular non-user based testing methods include the heuristic review where the design is checked against good design rules-ofthumb, and the expert-based review where someone who has lots of experience in designing mobile interactions uses their knowledge of what works to spot weaknesses in the design (see Box 4.6).

## BOX 4.6

## EXPERT INSIGHTS

## An interview with Scott Jenson, Head of Jenson Design (a product design consultancy) and former director of product design at Symbian

MJ: How did you get into mobile design?

SJ: I was working for Apple and had the chance to be on the Newton concept. Then, when I moved to London, I knew I just had to get into the mobile phone area as that’s where all the exciting design was – and is – going on. So, I ended up leading the DesignLab, working on projects such as the QUARTZ, which turned into the interface for devices like the Sony Ericsson P800 and P900.

## MJ: What did the DesignLab do?

SJ: There was a lot of usability testing and design refinement. So, we had three full-time people whose job was to create functional prototypes using Macromedia Director; then we’d review, user-test and change these designs. Sometimes this included taking the prototypes to different countries to see how they worked, or not, with a broad range of people. We’d also work on trying to define new concepts for mobile interaction and services and in these cases we’d think more about the design semantics.

## MJ: ‘Semantics’?

SJ: Yes, design is about semantics and syntax. First, you need to see what people do and what they want – the semantics – and then you have to find a way of making this possible – the syntax. I was involved in thinking about lots of early WAP services; the trouble was that the industry in general focused on and promoted a sort of syntaxfocused design; worse still, lots of the offerings had many syntax errors, with users having to carry out many steps just to get a simple piece of information.

MJ: In doing all these activities within a fast-paced, commercial environment, what did you learn about design?

SJ: Well, first, design needs to know its place. It’s not the only thing that’s needed for a successful product – functionality, price, marketing, fashion, brand: lots of things have ➤ a major impact too. As part of this ‘team player’ attitude, you have to accept that design is the art of compromise.

MJ: Can you give some examples of this pragmatic approach?

SJ: It comes in all sorts of forms. So, take the Sony Ericsson P800/P900 – we wanted to build a device that was a PDA and phone combined. Now Palm already had a very successful UI concept that really worked, but we couldn’t over-copy this as we wanted a distinct but also effective interface. Then, there were the rapid changes and additions to the platforms we were working with – so, we started with one set of devices in mind and then a company came along with another platform with a smaller display and a jog-wheel instead of a stylus. And, of course, when the design goes into production there are lots of times when something just can’t be done given the time and technical constraints; as a designer you then need to work with the engineers to try and retain as much of your idea as possible. So, for example, on a phone platform we worked on, for technical reasons, we had to have a ‘sync’ folder for email synchronized with the desktop client, and an ‘inbox’ for messages received when mobile. What we actually wanted was a single view of the ‘inbox’ combining all the user’s mail; so, we had to produce a ‘hack’ with a process that read mail from both sources and put it in a third on the device.

MJ: How did the DesignLab work to be what you’ve called a ‘team player’ within the company?

SJ: Design is an inherently social process. From the very start we’d ensure we had buy-in from key groups – our initial brainstorm sessions would, for instance, include software engineers. Then, when we produced the final design, before the development began, we’d draw up a ‘design manifesto’ spelling out our interaction concept in terms of purpose, functionality, marketing and the like, and get this signed off by a ‘champion’ from marketing, the technical team and the DesignLab.

MJ: Now that you’ve moved into independent consulting, what sorts of approach do you get from potential clients?

SJ: A whole range. The classic case is a company that phones you up and says ‘‘we’ve got two weeks to ship, can you look at the icons’’. At the other end of the extreme, I’ll be asked to generate ‘blue-skies’ concepts for future services.

MJ: When you’re shown concepts or designs, how do you assess them?

SJ: First, I’ll be asking ‘‘what’s the value of this?’’ – that is, will people really want it? Take the iPod music player. It’s really easy to articulate what the value is – ‘‘it lets me take all my music with me’’; compare that with mobile Instant Messaging – ‘‘it allows ➤ me to be online and show you my availability if I’ve set it’’. So, a quick test is to try and sum up the value in one sentence. Next, I assess it from my strong belief in simplicity. I was looking at a service recently that had all sorts of functionality with many, many nested menus. I sat down with the design team and tried to figure out the three key things that people wanted to do; then we hid all the rest of the functionality for the power users.

MJ: When you see UI ‘bugs’ in the systems, how do you help companies work on them?

SJ: First, you need to judge how important the bug is. Some usability people can be too pedantic and perfectionist: if you look at any mobile, you’ll find lots and lots of problems, but not all of them will have a noticeable impact on the users’ experience. One technique I use is to think in terms of a ‘red card’ (this bug needs sorting out) and a ‘yellow card’ (it’s a problem, but a lower-priority one). Once you’ve spotted the problems, it depends how near to shipping the product is – if it’s late, then quick hacks, help text and manuals can be a fix until version 2; if it’s early on, you then need to persuade the developers why change is needed. ■

## 4.6 ITERATIVE DEVELOPMENT

One of the first software development models to be developed was called the Waterfall Model (Royce, 1970). As water leaps off a ledge it falls quickly downwards, dragged inexorably to the base; similarly in the waterfall software model, development flows top-downwards, the system design moving from the abstract to the implementation through a series of well-defined phases. As each phase is completed it is ‘signed off’ and the next is commenced.

With interaction design there are some dependencies between the activities outlined in the previous sections. So it would be unwise to attempt to generate scenarios, the stories of use, before you have been immersed in the users’ world, for instance; and evaluation can obviously happen only after there is something to evaluate.

However, design is certainly not a case of following a simple checklist, moving with certainty from problem to solution. The design process does not proceed in a one-way, clear-cut fashion. Rather, many prototypes are built, designs being formed and reformed over and over again. Your skills in understanding users’ needs and your ability to shape and manage the design space, as well as your prototyping and evaluation expertise, may all be needed as each new design emerges.

In many of the projects we’ve worked on, then, the development process has proceeded thus. First, we do some ethnography and other types of in-situ study. Back at the office, we sift through our observations, extracting themes and issues. We call in users to interview, cross-checking with what we found earlier, and we return to the field to do more focused studies, guided by the initial fieldwork. Next come some prototypes that we take back to the field and put in the hands of potential users, both to check our assumptions and to further draw out possible opportunities and needs (the prototypes here thus acting as a fact-finding tool). More prototypes follow which are critiqued by us, other expert designers and users back at the lab. We usually develop a couple of competing proposals and get them to a status that allows them to be evaluated in a controlled test.

After refining the ‘winning’ system further, we might then deploy it in the field to see how it performs in context over time.

Although this oversimplifies the case a little, engineering and interaction design differ in the way they approach problems and solutions. In engineering, the aim is to take a clearly defined problem – say a bridge that can withstand gale-force winds and heavy vehicles – to produce an effective, robust, stress-tested solution. As an interaction designer, though, you will often find yourself trying to form a view about what the problem actually is as much as producing the solution. As designs develop you might well experience self-doubt, needing to reassess your certainties about what your users value, leading you to go back to further field observations, for example.

## 4.7 MULTIPLE VIEWPOINTS

Interaction design is a stimulating and demanding job. Part of the interest, and some frustration, results from the need to employ diverse techniques, to accommodate discordant attitudes and viewpoints, and to actively involve people with differing backgrounds and sets of skills.

## 4.7.1 MANY TECHNIQUES AND TOOLS

The previous sections present a sketch of the design process. In all of the main activities, there is a wide range of design techniques that can be used; Table 4.2, adapted from Dykstra-Erickson et al. (2001), gives a feel for the diversity of options available. At least three factors will influence the choice of methods:

The nature of the project

The team’s skills

The culture and style of the company you work for.

While you won’t need, or be able to use, all the available approaches every time, it is usually helpful to deploy more than one technique for a particular purpose: field studies combined with interviews, expert evaluations with design walkthroughs, and so on.

Design, then, can learn from geographical surveying: to find an object’s location, two or more readings are taking from known points. In design, this triangulation process means taking two or more perspectives to understand a situation more accurately (Mackay and Fayard, 1997).

## 4.7.2 MANY DISCIPLINES

The sorts of skills needed to produce effective interfaces have changed greatly in the past 40 or so years, as Jonathan Grudin notes (Grudin, 1990). While today, interaction design draws on many distinct disciplines, including computer science, marketing, sociology and the arts, things were not always as cosmopolitan.

At first, in the 1950s, computers were like newborn infants, adored by engineers and programmers. Interactions were unsophisticated and simple, and the main skills needed to produce effective interfaces came from electrical engineers.

By the 1960s, programmers were the predominant computer users, interacting with programming development software. These users were like schoolteachers – willing to put the effort into understanding the growing child while educating it to do useful things. Technical developments in computer science, such as operating systems and high-level languages, were the keys to improving the ways programmers and computers communicated.

TABLE 4.2  
Diversity of techniques useful in interaction design (inspired and adapted from Dykstra-Erickson et al., 2001), showing approaches organized by phase. These techniques have evolved from diverse disciplines – from ethnography to marketing, from arts to computer science
<table><tr><td>Finding out about use</td><td>Analyzing user data</td><td>Generating ideas</td><td>Designing systems</td><td>Evaluating systems</td></tr><tr><td>Naturalistic observations</td><td>Event coding (classifying and categorizing observations)</td><td>Oral brainstorming</td><td>Paper prototyping</td><td>Longitudinal (longer-term) field deployment</td></tr><tr><td>Contextual inquiries (field interviews shaped by user activities)</td><td>Task analysis (identifies structures in actions user carries out to reach goals)</td><td>Notecard brainstorming</td><td>Video prototyping</td><td>Usability study (e.g. review by usability experts)</td></tr><tr><td>Question- naires</td><td>Survey analysis</td><td>Video brainstorming</td><td>Software / hardware simulation Wizard of Oz</td><td>Lab trial</td></tr><tr><td>Focus groups</td><td>Persona and scenario analysis (consolidating observations into focused descriptions of typical users and uses)</td><td>Focus troupes (acting out potential uses)</td><td>(simulation where investigator plays role of system, responding to user interactions)</td><td>Design walkthrough (using psychology- based assessment tools to measure impact on learning,</td></tr><tr><td>Lab studies to assess specific behavioral / cognitive characteristics</td><td>Log analysis (data mining techniques to assess interactions with existing devices / services)</td><td>Bodystorming (brainstorm- ing carried out in field – i.e. designers take their bodies to the context)</td><td>Functional prototype</td><td>errors of design, etc.) Focus groups</td></tr></table>

TABLE 4.3
<table><tr><td>Finding out about use</td><td>Analyzing user data</td><td>Generating ideas</td><td>Designing systems</td><td>Evaluating systems</td></tr><tr><td>Probes: cultural, mobile, technological (tools and techniques</td><td></td><td>State-of-art review (analysis of published example</td><td></td><td>Diary study</td></tr><tr><td>aimed at prompting responses in engaging</td><td></td><td>designs and issues relating to area of concern)</td><td></td><td></td></tr><tr><td>Diary study (self-report technique where user</td><td></td><td></td><td></td><td></td></tr><tr><td>regularly completes diary entries</td><td></td><td></td><td></td><td></td></tr></table>

It took until the 1970s for the term ‘user interface’ to come into parlance, with end-user terminals and non-technical users. At this stage, as Grudin eloquently puts it, the computer had grown up and began making its first steps into the community, a place full of people with less commitment and time to adapt to it – it had to fit in. From this point, human-factors specialists, cognitive psychologists and the like become important.

In the 1980s and 1990s, computers increasingly moved out of the back office and onto the desks of many employees. Soon the need became apparent to understand how groups of people work together, supported by interactive systems. At this time, sociologists, anthropologists and the like came to the fore.

In recent years, computing technology has reached out even further, from the workplace to every place, into consumer products, becoming a backcloth to ordinary life. To meet the needs of this development stage, interaction design is further drawing on marketing and artistic disciplines. Nokia, then, have thought about phones for different segments of the consumer market: there are ‘classic’ styles for ‘controller’-type consumers, fashion-oriented ones for the ‘expressors’, and a premium look is targeted at ‘impressors’ (Lindholm et al., 2003). Meanwhile, the role of art-inspired approaches is concisely argued by the Royal College of Art’s Interaction Design Department:

. . . most hi-tech products and services are still a long way from meeting people’s everyday needs and desires. We require fun as well as function, poetry as well as power. (RCA)

## 4.7.3 PARTICIPATION AND COLLABORATION

For much of the last century, many workers were seen as cogs in a wheel. Their jobs and work practices had to be fine-tuned in order to make the overall process more and more effective. This mechanistic management style was fathered by Frederick Taylor who published The Principles of Scientific Management in 1911 (Taylor, 1998). In it, he laid out approaches to carefully specify how jobs should be carried out, the tools to be used, and how the work environment should be controlled. For employees, these approaches saw a dramatic loss of autonomy.

While widely deployed, such methods were challenged in Scandinavian countries. These nations, with a long tradition of social justice, developed participative and cooperative work design techniques. The thinking behind these approaches is that as well as being simply more humane, they increase productivity by nurturing commitment and enthusiasm in everyone involved.

Collaborative work practices have long been seen as important in computer technology development. The developers who build a system and the people who will use it are brought together, to work as equals in the development process. Everybody can contribute and each contribution is as welcome as the next – there is a notion, then, of equal opportunity.

Many variants of such participatory design (PD) methods exist; indeed, by 2001, Michael Muller, who has been involved in shaping key techniques, counted 61 separate approaches with seven different lifecycles (Muller, 2001). Participants come together and use low-tech objects, such as Post-it notes and marker pens, to work on specifying elements of the Graphical User Interface (GUI).

Many of the methods were developed in the era of desktop computers and GUIs. For mobile design, they need to be adapted for several reasons (Bødker and Buur, 2002):

Need to express novel interaction elements. Post-it notes, cards, marker pens and the like are excellent for prototyping GUI widgets – buttons, scroll bars, etc. – and their relationships on screens on forms. But what about the non-visual elements in mobile interactions and how a device and its environment might relate?

Need to accommodate mobile use-contexts. In conventional participatory design, teams meet in a laboratory, or an adapted meeting room. For the sorts of office-type systems the techniques were invented for, this sort of arrangement is more than satisfactory. Participants have a clear shared understanding of the office place environments the system will be used in; they can easily communicate their experiences away from their actual workplace. The complexity and diversity of use-contexts for mobiles make using a conventional meeting place less attractive.

Need to involve engaged, true stakeholders. In pure participatory design, the users involved are the ones who will actually end up using the systems. With many mobile systems, the aim is to produce services which will be used by a mass market – the people you involve in the design effort might be potential users, but they will have less of a commitment than those workers who knew they would be definitely affected by the final design outcome.

The ‘collaboratorium’ is one approach to overcoming such problems (Bødker and Buur, 2002). Participants use props and work together in locations – both indoors and outdoors – that better accommodate the features of mobile use. An example of the use of the collaboratorium is reviewed in Box 4.7.