## BOX 3.4

# PUSH-TO-TALK

While text-based instant messaging might not be such a big hit on mobiles, voice versions could be more popular, as a study by Allison Woodruff and Paul Aoki of the Palo Alto Research Center (PARC) suggests (Woodruff and Aoki, 2003).

Push-to-talk is a feature being provided by a number of mobile telephone networks around the world. It allows walkie-talkie type communication – users press a button to send a voice message directly to one or more other subscribers.

In the PARC study, a group of young people were observed using the technology. What the researchers found was that the service enabled a range of communications, including:

Chit-chat: gossip-type conversation over the day

Extended presence: keeping in touch with loved ones

Micro-coordination: sending messages in order to organize activities and rendezvous

Play, e.g. sending each other funny sounds or comments.

Many of these sorts of interaction are of course seen in SMS; however, the participants showed they particularly appreciated the very low interactional costs of using the voice approach and the lack of the ‘persistence’ of messages (the audio messages were not stored, unlike text messages), allowing them to engage without the risk of being held to account later for what they said.

All the participants enjoyed the service and were moderately enthusiastic about using it in the longer term. ■

## 3.3.2 INTERFACE STYLES

Designing a new system to accommodate a user’s previous knowledge and experience at the interface and interaction level seems sensible in attempting to promote the product’s adoption and in reducing the amount of relearning. Such motivations are noted by some researchers to justify their attempts to provide a full QWERTY keyboard for mobile devices (Roeber et al., 2003).

In early versions of the Microsoft operating system for PocketPCs, the aim was to replicate the desktop interface experience extensively – the goal was Windows on a small screen. But the effect was a less than usable experience, as one of the developers recounts:

From a usability standpoint, interface consistency was not enough to ensure success in the first iterations of the Palm-sized PC . . . If quick data entry lookup was a key requirement for the product, then it wasn’t being satisfied with the multiple screen taps necessary to acquire information. So, while familiarity and functionality were satisfied, usability was not. (Zuberec, 2000)

Microsoft’s competition, in the form of Palm, approached the problem quite differently. The PalmPilot developers rejected the idea of emulating the PC experience. Noticing big differences between the ways people used PCs and PDAs, their whole approach was to make things simple, direct and fast to complete. With a PC, people work for extended periods on a word processor or spreadsheet; handhelds, in contrast, are used in short bursts, many times during the day. As Rob Haitani, one of the early designers, says:

You have to ask yourself if the usage pattern is diametrically opposite, does it make sense to copy the design paradigm, and our response was no. (Bergman and Haitani, 2000)

The PocketPC Windows developers learned from their experiences and later versions were more mobile-adapted.

## BOX 3.5

## SHRINKING TO FIT

One approach to design is to take existing applications on one platform and refit them for the smaller screen. This is Microsoft’s advice for adapting applications for their Smartphone from the PC or PocketPC (Microsoft, a). Note that the ‘Common Dialogs’ referred to here are the dialog boxes used to select a file, and a ‘Spinner’ control is an interface element that allows users to toggle through a list of options using arrow buttons on the phone.

## Microsoft’s general guidelines

To design an effective user interface (UI), here is a procedure you should follow to optimize your results.

Step 1: Review your current UI for the desktop version of your application or PocketPC.

Locate all unnecessary interface elements and remove them.

Locate all elements that are not supported and remove them or replace them with Smartphone elements.

Try to avoid dialogs that pop up dialogs that pop up dialogs, . . ., and so on.

Step 2: Put all interface elements under each other instead of having them side-by-side.

Use descriptive labels on top of elements instead of to the right or left (see Figures 3.3 and 3.4).

You can have longer dialogs since they scroll automatically. ➤

![](images/5058e494e78fa3b62176a42b5e7bdb27f945f1c159cc0bbd3db2f5f8ff68c7d3.jpg)  
FIGURE 3.3

PocketPC user interface  
![](images/acbb78e90ab2b5969e39dd048b13e6be2af502ce311b743c54508fff9a7df308.jpg)  
FIGURE 3.4  
Smartphone user interface ➤

Step 3: Locate all Common Dialogs and remove them. If your application requires the user to select a file, do the following:

Store such files in ‘/My Documents’.

Load the list of all those files into a Spinner control.

Show the Spinner control instead of the Common Dialog.

Step 4: Reduce the number of menus to one and menu items to 4–8.

Step 5: Define your SoftKeys. If you have a menu, use SoftKey 2. Otherwise follow this guideline: use SoftKey 1 for ‘OK’ or any other positive selection (i.e. ‘Yes’, ‘Done’ or ‘New’) and SoftKey 2 for ‘Cancel’, negative selection (i.e. ‘No’) or any further actions.

Step 6: Test your application user interface with one hand.

Force yourself to operate even the emulator with just one hand to ensure it will work to the satisfaction of the user. ■

## 3.4 BUILDING ON PAST MOBILE SUCCESS

Instead of trying to take well-known PC services and shrinking them, another possibility is to look at what has worked on mobiles and see how to build on these successful services. On mobile phones the obvious winners are voice and messaging, and many providers are looking at how to extend the ways people can use these methods of giving and receiving information (see Box 3.6).

## BOX 3.6

## EXTENDING THE SUCCESS?

Voice and text messaging enjoy a success that service providers would like to extend. There are a range of possibilities, some commercially available; but which ones will really fit with users’ needs?

Push-to-talk: simply press a button on the phone to talk directly, walkie-talkie fashion, to another user (see also Box 3.4).

TAP: send a message containing just the sender’s name and time, a simple, fast way to tell someone they are on the sender’s mind (Jenson, 2004). ➤

Voice SMS: send short voice messages directly to another phone (Jenson, 2004).

Picture/multimedia messaging: enrich text messages with photos, music or video.

SMS to voice: type a text message and send it to a non-text-capable phone, the system converting text to speech.

Fixed phone SMSing: have a fixed phone that can display and send text messages.

SMS archiving: access all the text messages you’ve sent or received via a website when you are at a PC at home or work. ■

As the mobile IM case shows, just assuming that variations of an effective form of service will also be highly desirable is naive. Be wary of complicating a simple but effective service, like SMS, and weakening its power by doing so.

Multimedia Messaging (MMS) is an attempt to provide SMS users with richer ways of getting their message across. However, as Scott Jenson explains, in its initial form it failed to add substantial value to users:

MMS assumes its value is based upon the value of SMS . . . [but] Current user research implies the true value of SMS is based on a complex series of social and interactive attributes which don’t seem to be greatly enhanced by digital photos. There indeed may be great value to sending photos, but it will be a new, currently unknown value. (Jenson, 2004)

MMS also breaks the simple interaction model seen in SMS. Figure 3.5 illustrates a typical task flow with users having to complete a complex series of steps, potentially involving repeated activities such as selecting and attaching sounds or image. Compare this with the simple, linear sequence that characterizes SMS (see Figure 2.7 in Chapter 2).

![](images/3878f57a19a2676031825ac208e74a8cfbc0f4bae3c96b83096e924f277d571b.jpg)  
FIGURE 3.5  
MMS task flow: creating an MMS can be complicated (inspired by Jenson, 2004)

## 3.5 DRAMA

Playwrights create both worlds and characters to act in them. They know everything about the creatures they conjure up, limiting their interactions with the world they inhabit. The focus in on defining the lives of a handful of individuals, with a story that carefully weaves their actions into the meaningful whole.

As a mobile designer, you might see yourself as a bit of a playwright, developing ‘scripts’ for how people will use the technology, imagining how it will be employed in a world you invent. But what seems useful and viable in interaction terms, when imagined, may be hopelessly ineffective in the real world. When conjuring up users and their worlds, the scale and complexity of the actual world is easily overlooked.

Take some of the proposals for location-based, targeted mobile marketing: ‘money-off’ coupons and the like. The possibilities opened up by the technology seem very useful and potentially lucrative, and a whole range of applications have been suggested. Some examples, from an IBM researcher, give a flavor of the exciting drama we might all be involved in:

Notify a consumer as they enter a shopping center that an office supply store’s back-to-school sale is over in two hours; . . . Send tourists brief multimedia descriptions in the Washington, D.C. Mall as they enter each monument’s surrounding area; . . . Inform lottery players that they are close to the ‘pot of gold at the end of the rainbow’ and they should look for someone dressed as a leprechaun . . . (Munson and Gupta, 2002)

Sounds convincing? Who would turn down the opportunity to receive such timely information, helping save (or win) money and to make the most of a visit? But how would you cope with the deluge of messages when every store, public authority and lottery-running organization can send you ‘useful’ information? Email spam will seem harmless by comparison, if there aren’t easy-to-operate mechanisms for users to control the type, number and occurrence of such mobile interruptions. Such mechanisms will be a major usability challenge for the industry.

It is easy, too, to overlook the social, group effect of these notifications if you are simply imagining one user feeling pleased to have received a useful message. Take the blinkers off and visualize hundreds of people in a busy shopping mall all hearing about the last moments of a shop sale; a highly unpleasant, unfulfilling shopping experience is guaranteed for all as shoppers rush and converge on the store – not so much a case of a ‘smartmob’, more a smarting one.

On top of this problem of managing scale, add the issues of integrating these types of service into the other things a user is doing and wants to achieve. Imaginary users have nothing else to do except play a part in the system being envisioned – they are waiting for the designer’s cues. So, in the mobile notification case, the assumption seems to be that users are keenly waiting for their next stage direction: ‘‘turn left now for a bargain!’’, ‘‘look up and see Abraham Lincoln’’, ‘‘There’s the leprechaun!’’.

Real people might well have other things on their mind, like rushing through a shopping mall to pick up their children, or they might simply want peace to reflect on a visitor attraction. Next time you visit an art gallery, watch how some people stand for long periods in front of a painting, in awe and silence, then imagine a flurry of mobile ‘educational’ messages interrupting this peace.

The gap between fantasy and reality was also seen in a major magazine advertising campaign for a hi-spec phone during 2004. The glossy advert tells the story of how a father, away on a business trip, can still read stories to his children using the device. He sits in his hotel room, looks into hi video phone, and his little ones at home watch him on another mobile while tucked up in bed on the other side of the planet.

Anyone with young children will immediately spot the limitations of such a vision. Putting aside the wisdom of entrusting a small child with an expensive handset – one of ours recently dunked a handset in a cup of milk – the technology does not supply what the child (and adult) really enjoys: close, physical contact. Cuddling, not content, is king.

You cannot imagine what your users will want to do – you have to keep a careful watch.

## BOX 3.7

## PICTURE PHONES AND PARENTS

Sam, a four-year-old, loves spending hours making complex constructions out of wooden blocks or Lego. When it was time to tidy up at the end of the day, there were always tears; he just could not bear to see his creations so quickly dismantled and put away. When his father bought a mobile phone with a built-in camera, things changed. One day, Sam said ‘‘Daddy, give me your phone, want to take a picture’’. Slightly bemused, Dad handed the phone over, set it to picture mode and watched as Sam carefully photographed his tower. ‘‘Look, Daddy, a picture’’, Sam happily said, ‘‘now we can take it down’’. No request was made to print or store the photo. Ever since, Sam has used the mobile to momentarily document his work.

![](images/acfcf6a5285c2c9a548a3968d0d56f3fb388821b6731d8bb1a00089c52a18548.jpg)

A simple real-world example that illustrates how a designer’s plotline falls apart is played out millions of times a day at major international airports around the world. With global roaming, when a passenger arrives in a new country, as soon as they turn on their phone they’ll receive several messages welcoming them to the region and offering them networks to choose from. This ‘service can be extremely annoying when all you want to do is send a text message or place a quick call to tell friends you’ve arrived. After coping with the initial interruptions, heralded by a series of message arrival beeps, you may then need to spend a minute or so deleting messages now cluttering your device’s message memory.

## 3.6 FRAMEWORKS FOR HUMAN-CENTERED THINKING

Psychologists have long been interested in what motivates people, identifying the activities that drive them. Similarly, any visit to a bookstore will confirm the ongoing popularity of books that discuss methods, habits and techniques for successful living.

Ben Shneiderman has drawn on these traditions to produce a framework to spot the sorts of future devices, applications and services people will want (Shneiderman, 2002). He strongly argues we all want to be creative, to be involved in transforming ourselves and others. His recommendation to technology innovators is to support these needs. He breaks this creative process down into four activities:

<sub>•</sub> Collecting (gathering information)

Relating (communicating with others)

Creating (innovating)

Donating (disseminating the results of the creativity).

All of this creativity involves relating to others. Some of these relationships are close and personal (relating to oneself, family and friends), others are organizational (colleagues and neighbors), and there are large, societal interconnections too (citizens and markets).

Putting the activities and relationships together forms the ART, the Activities Relationship Table, a tool for generating human-focused technology ideas (see Table 3.1). You can use this table to generate ideas for candidate mobile products. For any square in the table, ask the familiar brainstorming questions of what, how, where, when and why. What might a person want to communicate to their friends and family? (Their mood, current activities, perhaps?) Why might someone want to remain in touch with a large group of people while mobile? (To check or make bids on an auction site, in the way a mobile service offered by eBay does, or to keep track of important developing new stories, for instance).

## EXERCISE 3.3

## USING ART TO GENERATE POTENTIAL MOBILE SERVICES

Using Shneiderman’s ART framework:

What information might you want to gather from the strangers you repeatedly see on your commutes to and from work, in the coffee-shop where you buy your ➤ morning takeaway, or in the doctor’s waiting room when you take your baby for its regular check-ups? How could this information be collected via mobile devices and what use might it be?

TABLE 3.1  
Mobile applications activities and relationships (adapted from Shneiderman, 2002)
<table><tr><td rowspan="2">Relationships</td><td colspan="4">Activities</td></tr><tr><td>Collect information</td><td>Relate communication</td><td>Create innovation</td><td>Donate dissemination</td></tr><tr><td>Self</td><td>Reminders (capture things you want to follow up later – a book in a store, advert</td><td></td><td></td><td></td></tr><tr><td>Family and friends</td><td></td><td>Find a friend (locate contacts in a city you are visiting) Info-doors (send</td><td>Mobile blog (write notes, send photos to your personal diary)</td><td></td></tr><tr><td>Colleagues and neighbors</td><td>Network effectively (pick up the contact details of groups of people you</td><td>messages to a digital display on your office door)</td><td></td><td></td></tr><tr><td>markets</td><td></td><td>Click-n-pay (m-commerce); on-the-go bidding (in online auctions when away from the</td><td></td><td>Tourist tips and recommenda- tions (if that sought-after attraction is closed, let others know)</td></tr></table>

Nokia launched a service in mid-2005 to allow users to create a sort of web page on their phone that other users in close proximity can view. Where would this application fit in Table 3.1?

Another framework for thinking through user needs is provided by usability consultants Aaron Marcus and Eugene Chen (Marcus and Chen, 2002). They suggest exploring different ‘spaces’ in which mobiles will have a role:

Information (services ranging from weather reports to diary assistants)

Self-enhancement (the mobile as a memory aid, health monitor, etc.)

Relationships (with the device extending existing social interactions)

Entertainment (services include games and music with an emphasis on short bursts of content)

m-commerce (the e-coupons we mentioned earlier would fall into this category).

While taxonomies like ART help you think through design proposals from a human perspective, they are only a start to a process and certainly do not provide the guaranteed successful choices. Innovations need to be tested with real users, so use these thought-tools to begin the ideas-bubbling process and then build prototypes, evaluate and refine them (see Box 3.8).

## BOX 3.8

## MESSAGING TO YOUR OFFICE DOOR

One idea for linking mobiles to other information devices is the InfoDoor (Shneiderman, 2002). Place PDA-sized networked displays on office doors and allow the office owner and others to post messages remotely. These digital noticeboards might function either banally as electronic nameplates or in a more sophisticated way, for instance in displaying a message sent to tell visitors you’re stuck in traffic.

While the idea is appealing, building and testing such proposals with actual users is vital if you want to uncover problems and understand nuances of use, as Keith Cheverst and his team discovered when they built the Hermes system at Lancaster University in the UK (Cheverst et al., 2003). Every office door was given a message pad with messages sent via text message, email or a web interface. Visitors can also use the system to leave a message to the absent occupant; when this happens a text message is sent to the room owner’s mobile phone prompting them to pick up the note via the web.

When the system was deployed in the trial, one problem was the users’ perception of its reliability. On a number of occasions, room owners would send a text message only to discover later that it had not been delivered to their door. To strengthen trust in the system, the prototype is being modified to send a confirmation SMS back to the sender when their message has been successfully displayed on the door.

Skeptics might feel all this technology is overkill – why not just phone the departmental secretary and ask them to pin up a message? Cheverst’s user test showed, however, that the system encouraged message sending that would not occur otherwise. Messages such as ‘‘in big q at post office . . . will be a bit late’’ were seen as too unimportant to bother a secretary with, but could be quickly and easily sent from the mobile. ➤

The Hermes system also usefully illustrates the notion of viewing mobiles as just one of an ensemble of devices – a collection of things that work together to provide useful services. In contrast, some mobile manufacturers and network operators are jealously guarding their networks and devices. ■

## BOX 3.9

## TECHNOLOGY VERSUS USER-CENTERED DESIGN

Jesper Kjeldskov and Steve Howard have reported on an interesting attempt to compare technology and user-centered design approaches (Kjeldskov and Howard, 2004). They put together two teams each made up of interaction design researchers and industrial practitioners, engineers and students. The brief was for the teams to develop prototypes for a context-aware mobile system to promote and support the use of public transport in Melbourne, Australia.

One group used the classic user-centered approaches, immersing themselves in users’ lives through interviews, field studies and the like; the other team took a strongly technology-driven approach, taking hardware features such as location sensing capabilities, and producing prototypes that made use of these.

The user-centered team produced a range of ideas, such as an MP3 player complemented with speech output to guide users to their destinations, and a foldable mobile office to be used while traveling by the city’s trams. They then further developed one of the prototypes, called TramMate. This system gave users travel information linked to the appointments logged on their mobile. It could alert them when they had to depart to catch the tram, tell them how to get to tram stations based on their current location, and give other useful information such as travel times and route changes. The TramMate prototype was not a functional one; rather it was presented as a series of sketches.

The technology-driven group focused on exploiting the potential of GPS (for navigation) and GPRS (for data transmission). The working prototype they ended up with had some similarities with TramMate from a functional perspective, providing textual route descriptions and annotated maps based on the user’s current location. However, the interface was very different: users had to look up tram timetable information manually as there was no link to their appointments diary, and updates to the information to reflect the user’s change of location happened only when the user actively requested them.

In comparing the two outcomes, the user-centered approach was seen as very useful in producing prototypes that accommodated current practice and perceived needs as well as in envisioning some more radical concepts. However, the real-world usability and feasibility could not be easily tested. In contrast, the technology-centered ➤ strategy identified some of the technical constraints that would have to be addressed as well as providing a functional prototype that users could try out in realistic contexts. In doing this, usability and broader use issues were identified.

The study suggests that designers should combine technology with user-centered design methods in their attempts to envision future mobile services. ■

## SUMMARY

Inspiration for new services can be spurred in several ways. Tracking technology evolutions, asking questions like ‘‘What novel experiences will this make possible?’’ and ‘‘How might the technology change the established ways of looking at communication, information access, social interactions, etc.?’’, is one way. Then there’s history to draw on – looking at successful non-mobile applications, to consider which might transfer to the small screen, and analyzing existing mobile winners in an attempt to divine effective extensions. Design is not a mechanistic, clinical activity, and the role of the designer’s imaginative flair should not be downplayed. But design should also not be purely an art, and there’s the science of disciplines like psychology and sociology which can be applied in a generative way. However, each of the methods considered here has pitfalls.

Technology-centered approaches can lead to follies, with vast sums spent on providing a highly sophisticated service that no one wants. Failing to notice the differing requirements of a mobile context when looking to past applications is easy to do too. When we dream or imagine, we can quickly suspend the constraints and messy nuances of reality; what appears a great innovation might fail to scale, crumbling in the bright lights of our complex world. Finally, just as self-help books can only generalize about the human condition, providing starting points for readers to address their own problems, human-centered frameworks such as ART are springboards: their advice needs to be tested and refined by engaging with actual users.

## WORKSHOP QUESTIONS

Look in business and technology magazines (such as The Economist and Wired Magazine) and find examples of the ways new devices and services are marketed. Critique the storylines and characters being presented – does the innovation really fit? How would it scale? How could you improve on it?

Shneiderman was inspired by Stephen Covey’s Seven Habits of Highly Effective People (Covey, 1990) and Maslow’s hierarchy of human needs. Visit a bookstore and select another of the top-selling self-help books. What values and needs does it address? How might a mobile service be designed to accommodate these?

Design a set of auditory tones (they could be auditory icons or earcons – flick back to Section 1.3.3 to remind yourself about the difference) that could communicate another user’s mobile status. The application context is push-to-talk type services; the user presses a button to contact a friend or colleague and the system responds to give their status if not they are not available.

## DESIGNER TIPS

Before transferring a successful service – like instant messaging – from desktop to the mobile, ask yourself how much of the service’s appeal is dependent on its non-mobile context.

When integrating a mobile with a desktop service, adopt the maxim ‘everything, underwhelmingly’. That is, provide access to as much of the user’s data as possible (and remember many mobiles will soon have vast on-board storage) but at the same time provide a small set of mobile-adapted tools to manipulate and view it. For a word-processing application, for example, users will want to annotate draft documents created on the desktop – the device might allow them to highlight text using a joystick and select from a set of predefined notes like ‘follow-up’ or ‘unsure’, or it could employ voice-notes. In terms of information access, automatically extracted summaries of previously viewed or available content will be important.

When looking at previous mobile success stories, step back from the details of the service and look for the general qualities they embody. SMS is a winner because of the simple interaction model it uses, the satisfying sense of closure it gives (with a clear beginning, middle and end to the interaction), and the range of uses it can be put to.

Brainstorming is clearly an important part of innovation. Let your imagination run free, and strive to change the world – people who communicate and relate better; improved understanding within and across organizations and cultures; greater access to the democratic process . . . Look to sociological insights into what drives people, what they hold dear. After each ideas-generating session, nominate one team member to be an enthusiast and another a skeptic: the enthusiast should talk up the proposal, thinking of extensions; the skeptic should focus on flaws, puncturing any unrealistic, over-positive groupthink.

## PART II DEVELOPING EFFECTIVE MOBILE APPLICATIONS

CHAPTER 4 INTERACTION DESIGN 93   
CHAPTER 5 WATCHING, ASKING, PROBING 121   
CHAPTER 6 PROTOTYPES 169   
CHAPTER 7 EVALUATION 195