# Design Guidelines and Examples

T<sup>his</sup> <sup>new</sup> <sup>goal</sup> <sup>of</sup> <sup>HCAI</sup> <sup>resolves</sup> <sup>the</sup> <sup>fifty-year</sup> <sup>debate,</sup> <sup>lucidly</sup> <sup>described</sup>by New York Times technology writer John Markof, between those who by New York Times technology writer John Markoff, between those who sought artificial intelligence and those who sought intelligence augmentation (IA).<sup>1</sup> This debate over AI versus IA now seems like arguing about iron horses versus horses or how many angels can fit on a pinhead. Designers can produce HCAI by integrating artificial intelligence algorithms with user interface designs in ways that amplify, augment, empower, and enhance people.

The current version of Google’s design guidebook buys into the need to choose: “Assess automation vs. augmentation . . . One large consideration is if you should use AI to automate a task or to augment a person’s ability to do that task themselves . . . For AI-driven products, there’s an essential balance between automation and user control.”<sup>2</sup> However, the authors of the Google design guidebook are open to the possibility that “[w]hen done right, automation and augmentation work together to both simplify and improve the outcome of a long, complicated process.” That’s the right message—do both!

Google’s complementary website gives guidelines for responsible AI that are well-aligned with my principles.<sup>3</sup>

• Use a human-centered design approach

• Identify multiple metrics to assess training and monitoring

• When possible, directly examine your raw data

• Understand the limitations of your data set and model

• Test, Test, Test

• Continue to monitor and update the system after deployment

Other early guidelines, such as those from Microsoft Research leader Eric Horvitz,<sup>4</sup> paved the way for Microsoft’s Guidelines for AI-Human Interaction.<sup>5</sup> These eighteen guidelines, which were presented with appealing graphics and even distributed as a deck of playing cards, cover initial use, normal use, coping with problems, and changes over time.<sup>6</sup> They are on the right track with their emphasis on user understanding and control, while addressing ways for the system to “make clear why the system did what it did” and “learn from user behavior.”

IBM’s Design for AI website discusses issues more broadly, ofering a high-level tutorial that covers design foundations, technology basics, ethical concerns, accountability, explainability, and fairness.<sup>7</sup> However, I publicly questioned its suggestion that a system should “endear itself to the user” and “form a full emotional bond.” Those phrases were changed, but the description of trust still includes the questionable encouragement to get users “to invest in an emotional bond with the system.”

Mica Endsley’s “Guidelines for the Design of Human-Autonomy Systems” has twenty thoughtful items that cover human understanding of autonomous systems, minimizing complexity, and supporting situation awareness.<sup>8</sup> Her guidelines include: “Use automated assistance for carrying out routine tasks rather than higher-level cognitive functions” and “Provide automation transparency,” each of which she explains in detail.

Successful designs are comprehensible, predictable, and controllable, thereby increasing the users’ self-eficacy, leading to reliable, safe, and trustworthy systems. These successes require careful design of the fine structure of interaction, which emerges from validated theories, clear principles, and actionable guidelines.<sup>9</sup> In turn, this knowledge becomes easy to apply when it is embedded in programming tools that favor human control. I playfully developed a compact set of Eight Golden Rules (Table 9.1) of user interface design, which I have updated in successive editions of Designing the User Interface.<sup>10</sup> These Eight Golden Rules remain valid for HCAI systems.<sup>11</sup>

User experience designer Euphemia Wong encouraged designers to follow these rules so as “to design great, productive and frustration-free user interfaces.”<sup>12</sup> YouTube videos present these rules in many languages and parodies poke fun at them, which is just fine with me.

The design decisions to craft user interfaces based on the Eight Golden Rules typically involve trade-ofs,<sup>13</sup> so careful study, creative design, and rigorous testing will help designers to produce high-quality user interfaces.

## Table 9.1 Eight Golden Rules for design<sup>14</sup>

<table><tr><td></td><td>I. Strive for consistency</td></tr><tr><td></td><td>2. Seek universal usability</td></tr><tr><td></td><td>3. Offer informative feedback</td></tr><tr><td></td><td>4. Design dialogs to yield closure</td></tr><tr><td></td><td>5. Prevent errors</td></tr><tr><td></td><td>6. Permit easy reversal of actions</td></tr><tr><td></td><td>7. Keep users in control</td></tr><tr><td></td><td>8. Reduce short-term memory load</td></tr></table>

Then the implemented designs must be continuously monitored by domain experts to understand problems and refine the designs. There is always room for improvement and new demands require redesigned user interfaces.

The examples that follow clarify the key ideas of supporting users to express their intent through visual interfaces. In addition, auditory and haptic interfaces are also valuable in many situations and for users with disabilities (the second Golden Rule). These designs give users informative feedback about the machine state, with progress indicators and completion reports. Many realworld designs are flawed, but these positive examples describe how it is possible to support both high levels of human control and high levels of automation. Part 3 will expand on these examples by describing supertools, tele-bots, active appliances, and control centers. For now, here are some examples:

Example 9.1 Simple thermostats allow residents to take better control of the temperature in their homes. They can see the room temperature and the current thermostat setting, clarifying what they can do to raise or lower the setting. Then they can hear the heating system turn on/of or see a light to indicate that their action has produced a response. The basic idea is to give residents an awareness of the current state, allow them to reset the control, and then give informative feedback (the third Golden Rule) that the computer is acting on their intent. There may be further feedback as the residents see the thermometer rise in response to their action, and maybe an indication when their desired goal has been achieved. Thermostats ofer still further benefits—they continue to keep the room temperature at the new setting automatically. In summary, while some thermostats may lack the features necessary that give clear feedback, well-designed thermostats give users an understanding of how they have controlled the automation to get the temperature they desire in their homes (Figure 9.1). Newer programmable thermostats, such as Google’s Nest, apply machine learning to allow residents to accommodate their schedules better and save energy. However, human behavior can be variable, undermining the utility of machine learning, as when residents change their schedules, adopt new hobbies such as baking, or have visitors with diferent needs. Getting the balance between human and machine control remains a challenge.

![](images/3d534e4db2917771502009151f2f2479435d134d740b565619e80ca87e5c5cf9.jpg)  
Fig 9.1 Honeywell thermostat shows status clearly and ofers simple up and down markers to increase or decrease the temperature. Tele-operation is supported by way of a user’s smartphone.

Example 9.2 Home appliances, such as dishwashers, clothes washers/dryers, and ovens allow users to choose settings that specify what they want, and then turn control over to sensors and timers to govern the process. When welldesigned, these appliances ofer users comprehensible and predictable user interfaces. They allow users to express their intent, with controls that let them monitor the current status and they can stop dishwashers to put in another plate or change from baking to broiling to brown their chicken (the seventh Golden Rule). These automations give users better control of these active appliances to ensure that they get what they want (Figure 9.2).

Example 9.3 Well-designed user interfaces in elevators enable substantial automation while providing appropriate human control. Elevator users approach a simple two-button control panel and press up or down. The button lights to indicate that the users’ intent has been recognized. A display panel indicates the elevator’s current floor so users can see progress, which lets them know how long they will have to wait. The elevator doors open, a tone sounds, and the users can step in to press a button to indicate their choice of floors. The button lights up to indicate their intent is recognized and the door closes. The floor display shows progress towards the goal. On arrival, a tone sounds and the door opens. The automated design which replaced the human operator ensures that doors will only open while on a floor, while triply redundant safety systems prevent elevators from falling, even under loss of power or broken cables. Machine learning algorithms coordinate multiple elevators, automatically adjusting their placement based on time of day, usage patterns, and changing passenger loads. Override controls allow firefighters or moving crews to achieve their goals. The carefully designed experience provides users with a high level of control over relevant features supported by a high level of automation. There are many refinements, such as detectors to prevent doors from closing on passengers (the fifth Golden Rule), so that the overall design is reliable, safe, and trustworthy.

![](images/cba62958b09b1ff2204d6df4fb36719641e783668f8ac88c0a96dba05aaf3db6.jpg)  
Fig 9.2 Active appliances operate automatically, but show their status and allow user control.

Example 9.4 Digital cameras in most cell phones display an image of what the users would get if they clicked on the large button (Figure 9.3). The image is updated smoothly as users adjust their composition or zoom in. At the same time, the camera makes automatic adjustments to the aperture and focus, while compensating for shaking hands, a wide range of lighting conditions (high dynamic range), and many other factors. Flash can be set to be on or of, or automatically set by the camera. Users can choose portrait modes, panorama, or video, including slow motion and time lapse. Users also can set various filters and once the image is taken they can make further adjustments such as brightness, contrast, saturation, vibrance, shadows, cropping, and red-eye elimination. These designs give users a high degree of control while also providing a high level of automation. Of course, there are mistakes, such as when the automatic focus feature puts the focus on a nearby bush, rather than the person standing just behind it. However, knowledgeable users can touch the desired focus point to override this mistake.

![](images/3b296e58f7bfd2eabb79ccac78ec703f4ed0493bc1d03c565ed1cff71ecd5b6b.jpg)  
Fig 9.3 Digital cameras give users great flexibility such as taking photos and editing tools to mark up photos, adjust color, change brightness, crop photos, and much more.

Example 9.5 Auto-completion is a form of recommender system that suggests commonly used ways to complete phrases or search terms, as in the Google search system. In Figure 9.4, the user begins a term and gets popular suggestions based on searches by other users. This auto-completion method does more than speed performance; it reminds users of possible search topics that they might find useful. Users can ignore the recommendation or choose one of the suggestions.

![](images/23f20bae80833f3fb76039a1fe56718d84d87bef00bcc2d9f0b670a7b3c903d4.jpg)  
Fig 9.4 Google Search auto-completion suggests search terms, but users can ignore and continue their typing.

![](images/bc801abdf4fbb794a9b154bb777c3a33f7c7808c09cf7db7a80e8ed263285592.jpg)  
Fig 9.5 Spellchecker shows a possible mistake with a red wiggly line. When clicked on, it ofers a suggested fix, but leaves users in control to decide whether they want to repair the mistake and when.  
Example 9.6 Spelling and grammar checkers as well as natural language translation systems ofer useful suggestions in subtle ways, such as a red wiggly line under the error, as in Figure 9.5, or the list of possible translations in Figure 9.6. These are examples of good interaction design that ofers help to users while letting them maintain control. At the same time, autocorrecting text messaging systems regularly produce mistakes, alternately amusing and annoying senders and recipients alike. Still, these applications are widely appreciated when implemented in a non-intrusive and optional way so they can be easily ignored.

![](images/191cf2b79467923e0bc80ef137dd9e353396402391ba4b546b37cc09db6b47fd.jpg)  
Fig 9.6 A natural language translation user interface that allows users to select the source and target languages, ofers a choice of complete sentences, and invites feedback on the translation, by way of the pencil icon.

The Eight Golden Rules for design help designers develop the comprehensible, predictable, and controllable interfaces. Many of the principles are embedded in human interface guidelines documents, such as Apple’s, which stipulates that “User Control: . . . people—not apps—are in control” and “Flexibility: . . . (give) users complete, fine-grained control over their work.”<sup>15</sup> These guidelines and others that emphasize human control ofer very diferent advice than the pursuit of computer autonomy.<sup>16</sup> The Eight Golden Rules are a starting point in leading to what I believe is desired by most users: reliable, safe, and trustworthy systems.

There is room to build on these Eight Golden Rules with an HCAI pattern language (Table 9.2). Pattern languages have been developed for many design challenges from architecture to social media systems. They are brief expressions of important ideas that suggest solutions to common design problems. Patterns remind designers of vital ideas in compact phrases meant to provoke more careful thinking.

1) Overview first, zoom and filter, then details-on-demand: The first one will be a familiar information visualization mantra that suggests users should be able to get an overview of all the data, possibly as a scattergram, geographic map, or a network diagram. This overview shows the scope and context for individual items, and allows users to zoom in on what they want, filter out what they don’t want, and then click for details-ondemand.

## Table 9.2 An HCAI pattern language

8. Incident reporting websites accelerate refinement

2) Preview first, select and initiate, then manage execution: For temporal sequences or robot operations the second pattern is to show a preview of the entire process; it allows users to select their plan, initiate the activity, and then manage the execution. This is what navigation tools and digital cameras do so successfully.

3) Steer by way of interactive control panels: Enable users to steer the process or device by way of interactive control panels. This is what users do when driving cars, flying drones, or playing video games. The control panel can include joysticks, buttons, or onscreen buttons, sliders, and other controls, often placed on maps, rooms, or imaginary spaces. Augmented and virtual reality extend the possibilities.

4) Capture history and audit trails from powerful sensors: Aircraft sensors record engine temperature, fuel flow, and dozens of other values, which are saved on the flight data recorder, but are also useful for pilots who want to review what happened 10 minutes ago. Cars and trucks record many items for maintenance reviews; so should applications, websites, data exploration tools, and machine learning models, so users can review their history easily.

5) People thrive on human-to-human communication: Applications are improved when users can easily share content, ask for help, and jointly edit documents. Remember the bumper sticker: Humans in the Group; Computers in the Loop (Figure 2.1).

6) Be cautious when outcomes are consequential: When applications can afect people’s lives, violate privacy, create physical damage, or cause injury, thorough evaluations and continuous monitoring become vital. Independent oversight helps limit damage. Humility is a good attribute for designers to have.

7) Prevent adversarial attacks: Failures can come not only from biased data and flawed software but also from attacks by malicious actors or vandals who would put technology to harmful purposes or simply disrupt normal use.

8) Incident reporting websites accelerate refinement: Openness to feedback from users and stakeholders will bring designers information about failures and near misses, which will enable them to continuously improve their technology products and services.

These patterns are discussed in Parts 3 and 4. The examples in this chapter show successful designs for user interfaces that give users the benefits of AI methods with the control they want.

In summary, design thinking is a powerful way of putting AI algorithms to work as vital components of HCAI systems that will amplify, augment, empower, and enhance human performance. These examples of supertools and active appliances are familiar and easy to understand, and they convey how the popular Eight Golden Rules from the past are applied, while showing how a newer pattern language for HCAI systems could become just as valuable in guiding designers.

Future users, including those with disabilities, will have supertools and active appliances to enable them to take care of more of the activities of daily life, explore creative possibilities, and help others. They will benefit from augmented and virtual realities to see more clearly, make better decisions, and have enriching entertainment experiences. Novel three-dimensional printing devices will give users options to make new devices that they want, repair existing devices, and fabricate custom jewelry or decorations. HCAI services will guide them to what they want to do, share products more easily with others, or start new businesses.