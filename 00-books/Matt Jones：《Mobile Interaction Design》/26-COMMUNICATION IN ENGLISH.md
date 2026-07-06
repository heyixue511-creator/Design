## BOX 11.3

# COMMUNICATION IN ENGLISH

One of our colleagues, Marion Walton, was conducting some research into the communication patterns of students using cellular handsets at the University of Cape Town. She discovered that students often communicated in English rather than their home language. For example, one Zulu student would SMS her Zulu-speaking mother in English. When interviewed, the student explained that the design of the handset interface forced her to ‘think in English’. ■

The Hofstede dimensions deal with the hidden parts of a culture – the motivations, psychology and values that drive people. Another aspect of cultural analysis is the inspection of the tangible artifacts produced by that culture. For software developers, we are on firmer ground here, as these artifacts can be codified into unambiguous design rules. For example, paper sizes are different across different countries, but each country has an agreed standard set of sizes. Obviously cultural artifacts like address formats, measurement units, etc., would fall under this same category. It almost seems too obvious to state that, for software to succeed in a given country, it must conform to the various standards used in that country – something that most packages do well already.

There is a danger, however, in treating the internationalization of an interface as an exercise in tinkering with icons and formatting strings. In the various projects described below, we have made observations that lead us to conclude that it is essential to understand the visual literacy of the target user group. A person’s visual literacy is a measure of their ability to interpret signs and diagrammatic conventions. This ability goes beyond the simple interpretation of single images and relates to how groups of items are interpreted as a whole. At present, most of the research into cultural interpretation of visual interfaces is still at the level of guidelines on culturally appropriate use of colors and icons.

To pick an example from our work, we have found that certain groups of users struggle with the concept of a hierarchy (Walton and Vukovic, 2003). This cropped up in the CyberTracker project and the Mobile Digital Library project. We observed users struggling with navigation in both these systems. Initially we thought this was due to poor choices in designing the hierarchy, so the hierarchy was redrawn in different ways. After some further research, however, it became clear that the issue was not the symbols used to denote the hierarchy, but the whole notion of a hierarchy. To test this idea, we had subjects draw family trees which produced diagrams similar to that shown in Figure 11.1.

Similarly, when we explained the concept of standard hierarchical animal classification (e.g. Reptiles: Snakes: Adders: Puff Adder) to the animal trackers in the Karoo (see next section), they laughed in amazement – ‘‘Why would anyone want to do that?’’.

In summary, then, internationalization guidelines can take you only so far. While they are useful for minor formatting issues, the deeper structures and paradigms on which an interface is built must also be examined.

![](images/3cfe8222662b11932cf9b9f4bfb30fef377323917b8b0c7abb5e5a80a9684529.jpg)  
FIGURE 11.1  
The subjects had the concept of a family tree explained to them and were asked to draw a tree for their family. This is among the more sensible responses we received

## 11.6 CASE STUDIES

## 11.6.1 EMPOWERING PEOPLE – CYBERTRACKER

One of our colleagues at the University of Cape Town, Edwin Blake, produced one of the first demonstrations of how effective mobile computers could be in the developing world. In this instance, the target user group were animal trackers in the Karoo National Park. These trackers are able to infer all sorts of subtle information from the tracks left by animals moving through the park. Theirs is a rich oral culture which emphasizes an understanding of the environment. Sadly, much of this knowledge cannot be shared with those from outside the culture as the trackers are, to Western cultures at least, effectively illiterate. (Ironically, the trackers see Westerners as illiterate in reading the signs and symbols of the veldt.) Their inability to communicate their knowledge effectively is frustrating for tracker and ranger alike.

Professor Blake, however, realized that the tracker’s communication skills are highly visual; the tracker must attach information to the signs left by the animals. Iconic interfaces require the same skills. From this starting point, Professor Blake and his team went on to develop an icon-driven interface for the Apple Newton (this was 1996, after all) which allowed the trackers to record what they had seen by selecting appropriate icons.

Rather than apply any form of cultural dimensions, the team engaged in Critical Action Research with the trackers and rangers. This is a methodology whereby the researchers become part of the community with which they are trying to work. The researchers develop ideas about the behavior of the community (in this case, the interpretation of icons) which they write down and reflect back to the community for critique. Inevitably changes will need to be made after the critique, and the cycle is repeated until agreement is reached between researchers and community. To communities wary of outsiders, this can be an ideal way to work together in a sympathetic way.

After several cycles of critical action research, the interface shown in Figure 11.2 was developed. The interface first required the tracker to identify the animal, in this case a klipspringer. Next, activities were selected – the selection of more than one activity had to be supported by the interface.

![](images/875e6e60b4a861070bc619939e4c88cc3482ee6ed83e14028c3a2662d1594803.jpg)  
FIGURE 11.2  
Iconic interface for the Newton. The screen on the left shows the animal, which is selected first. The screen on the right then appears allowing the tracker to record the activity the animal was engaged in

Everything the system could do was displayed directly on the interface – there were no pop-ups or special modifiers required. One thing you may notice from Figure 11.2 is that the interface has descriptive words beside the icons (the language is Afrikaans, as spoken by the trackers). These words served two purposes: firstly, they could be used as an aid by those trackers who were literate to some degree; secondly, they could be used to help teach the words to the illiterate trackers.

Once the entry is complete, a time stamp and location information (the Newton was connected to a GPS) were added to the recording. This information remains in the device’s memory, until it is uploaded to a PC when the tracker returns.

To illustrate the importance of working in this way with the target community, consider the following two discoveries which seem to run contrary to existing research and intuition:

Recognition of animal icons. The trackers paid much more attention to the overall form of an icon than to any single given aspect. For example, when creating the icon for a zebra, the designer assumed that showing stripes would be sufficient, so created a vague animal shape with stripes. This caused confusion with the trackers, some identifying it as a dog, due to the haphazard way in which the silhouette of the animal was drawn. Again the researchers’ visual literacy is very different from that of the tracker.

Verb icons. Accepted wisdom has it that icons are better at showing nouns than verbs – after all, how do you show ‘broke twigs for small animal to eat leaves’ in a grid of 32 32 pixels? Yet the trackers seemed to identify the action icons much more readily than they did the animals.

The success of this system can be measured on many levels. It is used in many parks around the world for many purposes – the software was ported to the Palm platform once the Newton prototype was complete. (A version can be downloaded from http://www.cybertracker.co.za/.) In the Karoo park, where it was originally deployed, the park management have a wealth of data on rare species, and their behaviors, which was impossible to record before. They can therefore better plan for and manage these animals.

Most importantly, the effect on the trackers has been remarkable. Whereas previously their skills seemed irrelevant, the ability to impart their knowledge has improved their self-esteem and given them an incentive to further improve their skills. Being able to communicate this information outside their culture helps ensure their knowledge will be preserved and valued by future generations.

## 11.6.2 EDUCATION

At present in sub-Saharan Africa, four out of every 10 children do not attend school (UNESCO, 2002). With the number of children set to increase and the number of teachers decreasing (for various reasons, including HIV/AIDS), clearly something needs to be done to make education delivery more effective and efficient. For all the reasons we have discussed before – poor electricity supply, cost concerns, etc. – mobile computers make an ideal alternative to desktop systems in the classroom.

In an effort to measure the potential impact of mobile computers in primary education in Africa, the Open University in the UK set up Project DEEP – http://www.open.ac.uk/deep/. The optimism for mobiles gained from the Real Access criteria certainly seems to be borne out in the DEEP project. Teachers reported that by using laptops and PDAs they were better able to cope with the erratic electricity supply and were able to work at home (ICT usage was not limited to desktop machines at school). Also popular were the camera-enabled PDAs used in the project. Originally intended as a way for teachers to document the DEEP project, students and teachers alike soon started using them as resources for projects and fieldwork. These devices engendered learning and creativity in a way that was not happening with the desktop systems. One teacher on the project wrote ‘‘The [handheld] is my companion’’. Many teachers commented on the unique abilities of the PDAs to be used anywhere and how it opened up new possibilities for learning. Encouraging as it was, the DEEP team were educationalists, so took the technology as a given and saw how it could impact learning. As designers of technology, we are now interested in building systems optimized to developing world education environments.

One project we have completed tackles the problem of providing computing facilities in a developing world university. We were interested to see whether we could build a system which used technology currently available to students (i.e. cellular handsets) that did not require the university to purchase more expensive computer hardware. This resulted in the ‘Text Worm’ system which allows lecturers to pose questions during a lecture and have the students SMS the answer in real time back to the lecturer’s computer – the computer has a mobile handset attached in order to pick up the SMSs (Jones and Marsden, 2004). The system supported multiple-choice type questions (as seen in Figure 11.3), with results being displayed dynamically on a graph, as well as open-ended questions. The system was well received, but there were issues with the cost of SMSs and students abusing the open question system (questions were displayed on a side-screen as they were received, which ultimately proved too distracting).

Considering future handsets, we then developed a system which allows a lecturer to broadcast lecture slides to any device running Windows Mobile. This system allows students to follow a lecture without the need of a data projector (an expensive temperamental item that requires a constant electricity supply) by transmitting individual slides to the client devices. Students are able to annotate the slide using a sticky-note metaphor, as seen in Figure 11.4. At the end of the lecture, the students will have a complete annotated slide deck. These annotations are also shareable independently, so students can give them to friends. Also, the system supported lecturer polls and open questions, as in Text Worm.

![](images/90885c409b09f1d289a0e5769f62eeab0972577585acf832cf1fba666c32fc34.jpg)  
FIGURE 11.3  
The screen on the left shows the question the students must respond to. The screen on the right shows the results in real time as they are received

Our system was based on a peer WiFi network between the lecturer’s laptop and the client devices. We realized that not all handsets will have WiFi, so we adapted our network infrastructure wherein handsets with both Bluetooth and WiFi could act as bridges for Bluetooth-only devices.

This system may seem trivial to those familiar with campuses that have ample ICT resources. For our students, however, there are immense benefits to being able to share notes and download class materials directly without having to queue at highly oversubscribed computer laboratories. Using our software, teachers can run interactive lessons with students using nothing more than a laptop and smartphones.

## 11.6.3 COMMUNITIZATION

There is some excellent work currently being undertaken by various NGOs at making information and educational material available to the developing world. Some of these organizations realize that the problem is a little more complex than simply putting the material on the web. The Greenstone software, from the New Zealand Digital Library project, is an excellent example of this approach (more information on the project can be found at http://nzdl.org). While it can be used to run Internet-based digital libraries, it also allows collections to be stored on CD-ROM. This was a conscious decision as the designers realized that, in the developing world, CD-ROM is a more effective way of distributing information. Furthermore, Greenstone runs on Linux, OS-X and every version of Windows from 3.1 upwards. Currently Greenstone is used to distribute the UNESCO collections of humanitarian information. Of course, we have already made the argument that mobile devices are better than desktop systems in the developing world context, so we developed a proxy for Greenstone that would allow users to access Greenstone collections using nothing more than a device with a WML browser. The project worked well and we have had interest from various organizations about adapting the solution to their needs. As information access from mobile devices has already been dealt with in Chapter 9, we won’t debate the issue here. However, one interesting result which we did discover in user testing is that scrollbars are too small to be used as positional feedback in a document – they are fine if the user knows that they need to scroll down the screen, but are too small to give sufficient cues that there is more information to be scrolled to (see Figure 11.5).

![](images/070053b16d901aca6622e8ef911fc430acf987c197c9604b6df0056979d465e0.jpg)  
FIGURE 11.4  
A yellow sticky-note can be seen on the last line of the slide. Clicking here opens the standard text entry box so the student can annotate the slide

The only time users did scroll down is when a line of text was truncated (see Figure 11.6) by the bottom of the screen. In the final version of our system, we forced the scrolling to always have an incomplete line at the bottom of the screen.

Another finding from the usability testing was that users struggled with how the hierarchy of documents was presented: libraries are made from collections, which are made from books, which are made of chapters, which are made of pages. Believing our interface design to be sound, we decided to run the same tests using a standard desktop version of Greenstone and discovered that the same problems were evident. Obviously, users in developing countries are unlikely to have visited a library and so are unfamiliar with terms like ‘collection’, which are essential to understanding the interface. When this is combined with the result we reported earlier about users having trouble with hierarchies of information, clearly users are going to struggle with information that is stored and queried in this hierarchical way. If we do want people to be able to access this information, then we need to redesign the interface to suit them specifically. But, if we do that, then surely we must redesign the interface for every other group of users that we identify. Clearly there isn’t time to do this, so we concluded that it was time to empower users to create their own interfaces.

![](images/6627c918a2846ee5b2be747335b398fc66a8b24062f564fb1b0cd5d43685ee80.jpg)  
FIGURE 11.5  
A seemingly complete list of the contents of the document: being three pixels wide, the scrollbar does not give sufficient feedback for users to scroll on down to see the full list

The Greenstone work, and many similar projects, were presented in the Development Consortium at the CHI 2002 conference. At that consortium, the members agreed that it was necessary to develop interfaces targeted at specific groups of users in developing countries – they too rejected the notion that interfaces can be built using a tool as crude as cultural dimensions. The notion which arose was one of ‘communitization’ (as opposed to personalization) of software. Software created for user communities in developing countries should have the ability to be customized by a suitable member of that community. The Open Source movement would claim that such customization is inherent in open software. That is true, but there are few open source programmers in the communities which we are targeting.

![](images/68912831d81599cf5c3d7533c85908781ae68f2e94b32577def8bfca31d69135.jpg)  
FIGURE 11.6  
In this layout, users are much more likely to scroll, as the half-rendered text at the bottom indicates that the full list is not visible

Taking our Greenstone example once again, a suitable community member would be a librarian or school teacher who wanted to make the Greenstone information available to their community in an appropriate way. To support this idea, we created a librarian’s interface to Greenstone which lets them customize the appearance of the final interface. This software also has a specific option for creating a layout for mobile devices as well as the desktop version (see Figure 11.7). As Greenstone is open source, we could create this interface ourselves; so whilst open source may not be modifiable by the end-user community, it provides the possibility of modification by sympathetic third-parties.

We have not really fully explored the ideas behind ‘communitization’ and whether it’s really any different from personalization. However, the benefits come from the process of creating software for a community rather than an individual user. In the developing world, where a user is unlikely to have their own PC, creating software for a CC (community computer) is likely to be more successful. Thinking about the community as one that includes users with mobile handsets further improves the chances of success.

![](images/ce4eb173f70d181e7bd5996e471d27cb3342c7c6353d6c88e2e9acf83465f8cf.jpg)

FIGURE 11.7

Digital library design system for a PDA screen. The user selects options on the left, and the screen on the right immediately reflects how those choices will affect the display on the target PDA

## EXERCISE 11.3

## COMMUNITIZATION

Take a look at the ‘Preferences’ panel in your favorite piece of software. Given what we have just said about communitization, what else do you think should be added to the panel in order to make the software customizable by a community? ➤

Or, do you think that communitization at this level is not possible and that the Open Standards community should be engaged in order to separate out the presentation layer from all existing forms of software? Is this possible (commercially) or even desirable? ■

## 11.7 CALL TO ARMS

The projects described in this chapter are just scratching at the surface of how to create mobile technologies with the potential to radically improve the quality of life for huge numbers of people. However, to take the education example, our work and the DEEP project are the only ones looking at how mobile technology can be used for education in developing countries. We would therefore encourage you to get actively involved in creating mobile solutions for the developing world. If you have a project to complete, or are working for a company creating solutions for the developing world, we would urge you to study documents like the Real Access criteria and get involved with the target communities. Maybe it is not too late to undo the future . . .

## SUMMARY

Few ICT interventions into developing countries have succeeded; the one exception is cellular technology. For all the reasons we have listed above, and no doubt a lot more beside, cellular technology has the greatest potential to help the greatest number of people. We have been working on a number of disparate projects with a wide community of users in an attempt to understand how interaction design works in a developing world context. So, while methodologies which work closely with people (e.g. Action Research) seem to prosper, theoretical and abstract approaches (e.g. cultural dimensions) have been less successful. Our hope for the future is that more people will start to develop solutions that are sympathetic to the developing world context and we can enhance existing interaction design practice to help close the digital divide.

## WORKSHOP QUESTIONS

The term ‘digital divide’ is hard to define and has a wider application than the distinction between the developing and the developed world. Do there exist communities of ICT have-nots within your locality? Why is it that they do not have access, and can anything be done to alter the situation?

Do you think that culture can be measured in dimensions as Hofstede suggests? For your culture, do you think that these dimensions capture useful ideas? Ideas that can be used in interface design?

Universities in developing countries cannot really afford computers for all their students. How much of what is done at universities already could be successfully migrated to a mobile platform?

If you have a study break, a sabbatical or a placement to do, we would encourage you to get involved with a project in a developing country – the impact of your work and the personal rewards are greater than anything you will do in countries already saturated with technology.

## DESIGNER TIPS

Using the visual language of cellular handsets is a good starting point for any interface used in a developing world country.

When creating software for the developing world, be mindful of extra guidelines (such as the Real Access criteria) beyond the usual design heuristics you have used in the developed world.

It may be the case that you do not need to translate your software into local languages for it to succeed. Many users in developing countries welcome the opportunity to practice English.

For Africa at least, be wary of interfaces that rely on users understanding hierarchically classified data – we have found that hierarchies are not a common way of thinking across all cultures.

For highly visual cultures, we have shown that iconic interfaces can be effective.