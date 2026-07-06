CHAPTER 1 0

# Summary and Skeptic’s Corner

We should stand in awe of the capacity of the human mind, and of the achievements of human culture.

Brian Cantwell Smith, The Promise of Artificial Intelligence: Reckoning and Judgment (2019)

M<sup>y</sup> <sup>aim</sup> <sup>is</sup> <sup>to</sup> <sup>help</sup> <sup>designers</sup> <sup>to</sup> <sup>make</sup> <sup>better</sup> <sup>AI</sup> <sup>systems</sup> <sup>by</sup> <sup>taking</sup> <sup>a</sup>human-centered approach. The HCAI framework separates the is- human-centered approach. The HCAI framework separates the issue of human control from computer automation, making it clear that high levels of human control and high levels of automation can be achieved by good design. The design decisions give human operators a clear understanding of the machine state and their choices. Designers are guided by concerns such as the consequences and reversibility of mistakes. Well-designed automation preserves human control where appropriate, thereby increasing performance and enabling creative improvements.

The HCAI framework clarifies when computer control for rapid automated action is necessary, when human desire for mastery is paramount, and when there are dangers of excessive automation or excessive human control. It clarifies design choices for (1) consumer and professional applications, such as widely used recommender systems, e-commerce services, social media platforms, and search engines, which have brought strong benefits to consumers; (2) consequential applications in medical, legal, environmental, or financial systems that can bring substantial benefits and harms; and (3) life-critical applications such as cars, airplanes, trains, military systems, pacemakers, or intensive care units.

The HCAI framework is based on the belief that people are diferent from computers. Therefore, designs which take advantage of unique computer features, including sophisticated algorithms, voluminous databases, advanced sensors, information-abundant displays, and powerful efectors are more likely to increase human performance. Similarly designs and organizational structures which recognize the unique capabilities of humans will have advantages such as encouraging innovative use, supporting continuous improvement, and promoting breakthroughs to vastly improved designs.

An important research direction is to develop objective measures of the levels of control and autonomy. Such measures would stimulate more meaningful design discussions, which would lead to improved guidelines, evaluations, and theories.

Human responsibility for mistakes is another powerful driver of design advancements such as the inclusion of detailed audit trails, consistent informative feedback about machine state, and strategies to collect incidents and accidents. Then retraining of users and redesign of systems can proceed to reduce failures and near misses. Dificult questions remain, such as how to deal with the deskilling efects that undermine the very human skills which may be needed when automation fails. Another dificult question is how to enable operators to remain vigilant as their actions become less frequent—how can a human in a self-driving car stay engaged enough to take over when needed?

Ethical questions, such as considerations of responsibility, fairness, and explainability, are helpful in developing general principles. When these general principles are combined with deep knowledge of and experience with the complexities of product and service design, they can yield actionable guidelines.<sup>1</sup> The HCAI framework lays a foundation for responsibility, fairness, and explainability. Recommendations for bridging the gap between ethics and practice are collected in Part 4.

A human-centered system will be made better because of (1) improved reliability from sound software engineering practices, (2) safety culture through business management strategies, (3) trustworthy certification by independent oversight, and (4) regulation by government agencies. HCAI systems will evolve rapidly because mechanisms for monitoring failures and near misses support rapid improvements.

The HCAI framework and the examples seem modest to some readers who have bolder aspirations of synthesizing human intelligence, perception, decision-making, and autonomous action. They prefer to design systems that perform without human attention or intervention, focusing on machine autonomy rather than human autonomy. They believe that fully reliable systems can be built, so they ignore or reject eforts to add audit trails, control panels, failure reporting, and other features in existing systems, especially in consequential and life-critical applications.

Other skeptics see the two-dimensional HCAI framework as too modest. They envision three-dimensional models and more elaborate models. This is fine, so they should build the case for these extensions. Others complain that the example user interfaces are too simple and that they represent only modest cases of what AI systems can accomplish. Maybe so. I welcome examples of what novel designs of more autonomous systems would look like and how they would perform. Dealing with fundamental failures, such as loss of power, loss of wireless connections, and breakage of components, is a key part of design excellence. Other failures come from adversarial attacks by malicious actors, so substantial efort is needed to prevent or deal with them.

AI researchers and developers who shift from one-dimensional thinking about levels of automation/autonomy to the two-dimensional HCAI framework may find fresh solutions to current problems. The HCAI framework guides designers to give users appropriate control while providing high levels of automation. When successful, these technologies amplify, augment, enhance, and empower users, dramatically increasing their performance.

Then designers can imagine future supertools, tele-bots, active appliances, and control centers that improve life for many and advance eforts to achieve the UN’s Sustainable Development Goals. Their designs may be guided by the original Eight Golden Rules or the new HCAI pattern language.

![](images/69f2a4207bd2be5456a57dc94ff547685de8c87be8953c34f91635fc8b710e4f.jpg)

## PART 3

## Design Metaphors

11 Introduction: What Are the Goals of AI Research?

12 Science and Innovation Goals

13 Intelligent Agents and Supertools

14 Teammates and Tele-bots

15 Assured Autonomy and Control Centers

16 Social Robots and Active Appliances

17 Summary and Skeptic’s Corner

teve Jobs famously described a computer as “a bicycle for our minds,” clearly convey-Sing that computers were best designed to amplify human abilities, while preserving human control. Current computers may be more like a Harley-Davidson for our minds, but some suggest that in the future, computers will be chaufeur-driven limousines for our minds, taking us to our destinations automatically. The contrast between riding a bicycle and being driven can be understood by using the HCAI framework. The humancontrolled bicycle ride may be pleasurable and healthy exercise, but the automated limousine with a chaufeur metaphor suggests comfort and maybe safety. However, how does a passenger convey intent about destination and influence performance, especially if the driver is unresponsive to requests to slow down or to stop? Human needs are complex and changing; sometimes people prefer to enjoy the pleasure of driving, exercising their driving skills; other times, they may appreciate being able to rest, read, or have a discussion with others.

Building on the transportation metaphor, we might think about computers as being large commercial jets that take many passengers to their destination in comfort, quickly, and safely, without having passengers learn how to fly. The plane is responsive to air-trafic controllers who monitor performance and to agencies that certify the aircraft, inspired by the upper right quadrant of the HCAI framework (Figure 8.4).

Readers may reflect on how civil aviation is safe because of the combination of automated features and the supervision from pilots and air trafic controllers. The answer is that both are needed. Automated features can take a plane from Washington, DC to Paris, France on a routine flight, allowing pilots to monitor aircraft systems more closely, but occasionally on-board fires, passengers with heart attacks, bird strikes that shut down engines, or hundreds of other problems require a skilled pilot to make dificult decisions rapidly.

While all metaphors, including this one, have their limits, they do have their value in conveying ideas that may open minds to fresh possibilities. Part 3 builds on the HCAI framework in Part 2 by directly dealing with the two design goals of AI and HCAI research:

1) Science goal: University of British Columbia professors David Poole and Alan Mackworth write that the science goal is to study “computational agents that act intelligently.” They want to “understand the principles that make intelligent behavior possible in natural or artificial systems . . . by designing, building, and experimenting with computational systems that perform tasks commonly viewed as requiring intelligence.”<sup>1</sup> Often, the science goal is based on research to understand human perceptual, cognitive, and motor skills so as to build systems that perform tasks as well as or better than humans, such as playing chess or identifying a cancer tumor.

2) Innovation goal: develop computers that amplify human abilities so people can do the job themselves. The innovation goal comes from research to build widely used products and services. Poole and Mackworth write that innovations “are built to be useful for an application domain.”<sup>2</sup> Success stories include map-based navigation systems, natural language translation, and search query completion.

Both goals have value in thinking about design metaphors for future technologies. The challenge is to understand when each goal is most appropriate, and how to combine these goals. Some features may be best handled automatically, such as setting the focus and aperture in a digital camera, while other features may be best given to human control such as composing the image and choosing when to click—what photographers call “the decisive moment."

These two goals lead us to four pairs of design metaphors that describe AI and HCAI research. All are valuable, but for diferent reasons: high levels of computer autonomy allow unattended activity and high levels of human control enable human intervention. One of the pairs of metaphors is intelligent agents, which suggests competent independent action, and supertools, which suggests human control in use of a machine. The second pair is teammates, hinting at human-like action, and a tele-bots (tele-operated devices), indicating human operation. The third pair is assured autonomy, which promises to be safe because of its design, and control centers, which promise safety because human controllers can monitor and intervene. The fourth pair of metaphors is social robots, designed to behave like a person, and active appliances, designed to be like a dishwasher or clothes dryer.

These pairs of design metaphors refine the HCAI framework by suggesting solutions that are tuned to the needs of diverse contexts, some favoring more automation while others favor greater human control. A key idea is combined designs that take an automated approach for tasks that can be carried out reliably, and a user-controlled approach for tasks that users want to manage. Combined designs enable more nuanced decisions about which features can be carried out reliably by a computer and which features humans want or need to be in control.

Users of recommender, question-answering, and game-playing systems may ignore imperfect responses and maybe even enjoy the occasional surprise. However, with consequential or life-critical applications in medical care, transportation, or financial systems, correct responses become essential and predictable behavior is vital in building trust.

This book favors a new synthesis, which combines a human-centered approach with AI algorithms as essential components of successful designs for advanced systems.

##