Chapter 5

# Evaluation and Tool Support

"If we knew what it was we were doing, it would not be called research, would it?"

—Albert Einstein

This chapter presents a number of evaluations of different aspects of the pattern-based framework presented. It first compares the framework with the set of initial requirements from chapter 2, then shows the results of a peer review of a sample pattern from the HCI design pattern language, and continues with a comparison ofthe approach and format used in this book to the recent definitions from a collaborative workshop on HCI design patterns. Subsequently, the systems that have resulted from using this approach are evaluated, and the use of the patterns presented in follow-up projects and education is addressed.

The chapter closes with a design sketch of a computerbased toolto author, review, and use pattern languages as presented in this book.

## 5.1 Comparison With Framework Requirements

Then pattern-based framework presented in this book compares as follows to the initial set of requirements (see p. 47):

•Domain-independent,uniform,well-defined format. Patterns were defined using a formal notation and a more extended discussion of the meaning of each component. This format has been followed successfully in the example languages, regardless of the domain.

• Empirical evidence. Not all example patterns contain references to published empirical studies strengtheningtheir argument yet, but various patterns already include such information (see, for example, DYNAMIC DESCRIPTOR (H15)).

•Domain-appropriate,design-supporting hierarchy. The framework suggests a pattern hierarchy that reflects a top-down, unfoldingdesign process. All example pattern languages exhibit this organization principle. The musicalpattern language leads from patterns addressing the overall structure of a piece, down to patterns dealing with the characteristics of individual notes. The HCI pattern language starts with broad patterns about designing the overall user experience, leadingto small-scale patterns about individual user interface objects. The software engineering patterns range from architectural concepts to implementation-oriented details.

• Design dimension coverage. The framework is general enough to allow additional design dimensions to be incorporated, depending on the domain. All pattern languages inthe example actuallyuse time as additional dimension to measure the "scale" of their patterns, and several patterns that address dynamic or sequential solutions also reflect this in some of their example media and storyboard-like sketches.

•Lifecycle integration. The framework takes Nielsen's usability engineering lifecycle, a widely known model of designing interactive systems, and illustrates how the various pattern languages can be used at each stage of this process model.

In all, unlike any of the previously existing efforts, the framework and sample pattern languages presented in this text basically fulfil all of the initial requirements. Improvements in various aspects are of course still possible.

## 5.2 Pattern Peer Review

An established method of judging the quality of academic publications is peer review by other experts in the field. To judge the soundness of pattern-relatedwork,the software patterns community has established the writers'workshop procedure (see [Borchers, 2000a], or p. 38 for a summary of this method). This format has also been used successfully to evaluate HCI patterns [Borchers et al., 2001].

At the workshop Pattern Languages For Interaction Design: Building Momentum [Borchers et al.,2001],the pattern DOMAIN-APPROPRIATE DEVICES (H11) by the author, which is part of the HCI pattern language in the previous chapter, was reviewed by the following workshop participants, all of whom are also working in the field of HCI design patterns and have written patterns for this area:

• Austin Henderson (Rivendel Consulting, California)

•Karri-Pekka Laakso (University of Helsinki, Finland)

•Victor Lombardi (Razorfish, New York)

•Carol Strohecker (Mitsubishi Electric Research Laboratory, Massachusetts)

• Yongmei Wu (Darmstadt University of Technology, Germany)

Since the pattern included in the language of this book has been improved as the result of this review, and since layout and references are slightly different, the original submitted pattern, as it was reviewed, is reproduced on the following pages.

## 10DOMAIN-APPROPRIATE DEVICES \*

![](images/f70904b7eab47c026bcb12af21d87de4eaa88b2c47ba19d4ea35f582e967fcbd.jpg)  
For a video example, see (http://www.tk.uni-linz.ac.at/worldbeat/worldbeat.mov)

Sample pattern for the CHI 20000 workshop “Pattern Languages for Interaction Design: Building Momentum" by Jan Borchers (mailto:jan@tk.uni-linz.ac.at).

Note: This pattern closely follows the Alexandrian format to examine how that format holds up for HCI patterns.

... you know what application area your interactive system is going to be about, and you have decided on the overall temporal and structural format of your interactive system—INCRE-MENTAL REVEALING (4), FLAT AND NARROW TREE (7). You are now ready to think about how the user should physically interact with your system at each phase.

## 000

Modern interactive systems address a huge variety of application domains. Yet, they almost invariably use only mouse and keyboard as input devices.

Every interactive software system has a domain which it addresses and that its contents or functions are about. For example, a computer-based drawing course has the artistic domain of drawing as its application area, and a process control system in a power plant has the domain of that power plant and its functions as its application area.

However, most interactive systems use the standard keyboard and, nowadays, mouse as input devices, and nothing else. User interface designers put a lot of work into creating “metaphors"in which the virtual, on-screen world resembles items and concepts from the well-known, physical world. But all the while, those objects remain virtual, volatile images to be manipulated with the same, generic set of input devices and physical actions: type, point, click.

A reason that is commonly stated for this is that the development effort to create dedicated input devices is too high. But often,it is not even attempted to estimate the amount of extra work and its possible payoff, because it requires a lot of thinking from the designers to come up with new ideas apart from mouse and keyboard, and it is an area where products and standards are as comfortably developed and accessible as in the world of standard input devices.

But psychological research as well as common sense tell us that users are much more efficient, successful, and satisfied when they are offered input devices that resemble physical objects of the application domain. For example, Norman [1988, p. 23 ff.]talks in detail about the advantages of “natural mappings" from input device to system function, and gives a good example of a device perfectly designed for its dedicated purpose: a seat adjustment control in a car which is shaped like a miniature seat itself. To adjust his own seat, the user simply pushes the corresponding part of the miniature seat into the desired direction. It would have been far more cumbersome to understand and use the seat controls if they had been designed as a set of industry-standard buttons on the dashboard (and, if we imagine using those controls ourselves, it would probably also have been less fun).

![](images/fcf781b67a251e584ffa00871d00d0b1a5089c79f0c54861c8a02fbf96d43f1d.jpg)  
A domain-appropriate control to adjust a car seat.

The same is true for the WorldBeat system shown in the opening picture: It is an interactive exhibit that demonstrates to its users how computers open up new ways to interact with music, from conducting a computer orchestra, to improvising to a Blues band with computer support. While our initial designs included a standard keyboard and mouse as input devices, we gradually found out that we did not really need them, and that they would spoil the "musical atmosphere" that the exhibit tries to create. The two infrared batons, on the other hand, are artefacts that resemble a conductor's baton, or xylophone sticks— objects that are well known from the musical domain. In taking them up, the user is already led away from thinking about interacting with a computer, into an experience of interacting with music. The system was elected one of the three most popular exhibits in the centre where it is installed [Borchers, 1997], and received an award for its new way to convey musical concepts.

![](images/fbab1fa2ad6ae825ff014188ce1165002ce2a1045caf5a6674b40866bf89ddd5.jpg)  
Urp simulates wind between two physical building models

Ishii and Ullmer [1997] developed the concept of Tangible Bits where the gap between human and computer is bridged by "coupling digital inormation to everyday physical objects and environments". For example, they created an Urban Planning Workbench (Urp) where buildings are represented by physical models that can be moved around on a map of the neighbourhood. Effects such as shadows and airflow are simulated in response to the physical placement of the objects and projected onto the map. Informal studies showed that most architects who tried the system would use it immediately if available [Underkoffier and Ishii, 1999].This is another example of the advantages of dedicated, application-specific input devices.

Therefore:

Use input devices that resemble real objects from the application domain of your interactive system. Whenever users have to input something, determine whether the standard mouse and keyboard are really the best devices to use for this purpose, or if other devices can make working with the system more intuitive, efficient, and enjoyable.

![](images/8d6c823cf4408b17e1020f6e100a64229a6b4daa8adc061b402283bf0f51a055.jpg)

A new device is also a good starting point to create a system that looks fresh, different, and intriguing—INNOVATIVE AP-PEARANCE(12), and that does not look like “a computer"— INVISIBLE HARDWARE (15). If your interactive system requires different forms of input, try to map them to your new input device—ONE INPUT DEVICE (20). ...

## References

Jan Borchers. WorldBeat: Designing a baton-based interface for an interactive music exhibit.In Proceedings of the CHI 97 Conference on Human Factors in Computing Systems (Atlanta, GA, USA, March 22–27, 1997), pages131–138, New York, 1997. ACM.

Hiroshi Ishii and Brygg Ullmer.Tangible bits: Towards seamless interfaces between people, bits and atoms. In Proceedings of the CHI 97 Conference on Human Factors in Computing Systems (Atlanta, GA, USA, March 22–27, 1997), pages 234–241, New York, 1997. ACM.

Donald A. Norman. The Psychology of Everyday Things. Basic Books, New York, 1988.

John Underkoffiler and Hiroshi Ishii. Urp: A luminous-tangible workbench for urban planning and design. In Proceedings of the CHI 99 Conference on Human Factors in Computing Systems (Pittsburgh, PA, USA, May 15–20, 1999), pages 386– 393, New York, 1999. ACM.

The reviewing process is transcribed below, with the initials indicating the reviewer. The structure follows the format of a standard writers'workshop [Borchers, 2000a]. Remarks were usually agreedupon bythe other reviewers,otherwise conflicting opinions are indicated.

## 5.2.1 Summary

The following statements were made by the reviewers to summarize the pattern.

• The pattern describes how to use alternative interaction devices, and gives real-world examples. (YW)

• The pattern recommends the use of matching input devices. (VL)

• The pattern indicates that the domain of application is critical to choosing the device. (AH)

## 5.2.2 Positive Formal Aspects

• The layout looks exactly like Alexander's patterns, which helps those familiar with Alexander's format to quickly find the important parts in this pattern. (AH)

• The problem and solution are easy to find; highlightingthem using boldface works well. (YW, KL)

• The page size and column length are friendly to read. (VL)

• Title and photo introduce the pattern well. (VL)

• The rating helps reader to judge validity of pattern. (KL)

• The format uses implicit cues (typography, e.g. boldface) instead of explicit labels to indicate problem, solution, etc., which is good (repeated labels would be unaesthetic and boring). (VL, AH)

•Illustrations are frequent and distributed well across the text. (VL)

• The sketch echoes the opening photo, addinguser's thoughts and being more abstract. (CS, YW)

•Several examples are included, and they are suitable (e.g., quotes from Norman). (KL)

•References are included. (CS)

## 5.2.3 Positive Contents Aspects

•The cover photo is very appropriate. (VL)

• The URL link to a "home page" for the opening example is a good idea. (VL)

• The amount of introductory context is well chosen. (VL)

• It is a good point that mouse and keyboard are often inappropriate. (KL)

• The car seat example is very well chosen. (AH)

•The solution includes "intuitive, efficient, and enjoyable"as system goals. (CS)

• The solution is well worded. (VL)

• The pattern includes links to other well-related patterns. (KL)

## 5.2.4 Format Improvement Suggestions

• The pattern may seem unstructured due to the lack of labels. (KL)—Response: The format is highly structured. (AH, CS)

• The structure becomes clear after reading the entire pattern, but a quick summary would be useful. (VL)

• There is an empty line missing before the word "Therefore" in the solution. (AH)

## 5.2.5 Contents Improvement Suggestions

• References suggest trying to map most interactions to the single input device if possible; this may not always be appropriate. (CS)\*

• Modern interactive systems not only "address", but are even part of a variety ofapplication domains. (AH)

• Mouse and keyboard should be left out of the problem statement to make it more timeless. (AH)

• Examples of when not to apply the pattern could be useful. (KL, AH)

• The title could be more specific. (VL)

• Is the pattern about both input and output devices? (AH)

• Leave out the notion of“modern" interactive systems, instead recommend choosing from the plethora of new input devicesaccording to domain; as mobile devices, tangible bits, etc. become standard, this makes the pattern more timeless. (CS)

• The picture of URP could have close-up andwhole, or a linkto a video, or a photo series to make more self-explanatory.(AH, CS)

• Recommend to also choose actions (in addition to devices) from the realworld (push real car seat to adjust it). (AH, KL)—Response: impossible for the Tangible Bits example. (CS)

• Include morein-depth discussionof WorldBeat, explaining what can be done with it (two sticks are not appropriate for conducting or selecting onscreen buttons). (CS, AH)\*

(\*) The comments marked with asterisks arise because this pattern was taken from a larger language, because the reviewers did not know that thislanguage particularly addresses interactive exhibits, and because the text contains a detailed description of WorldBeat elsewhere.

## 5.2.6 Conclusion: Main Advantages

The Alexandrian form, the good page format, and the wording of problem andsolution were regarded particularly positive form aspects.In the contents, the reviewers liked the well-chosen examples; the concept was seen as clearly being a pattern, and relating to other patterns.

## 5.3 Comparison With CHI 2000 Workshop Results

At the same CHI 2000 workshop on Pattern Languages for Interaction Design, the following definition was agreed upon by the participants:

"An HCI design pattern captures the essence of a successful solution to a recurring usability problem in interactive systems."

It went on to define which components constitute an HCI design pattern:

• name

• ranking

• sensitizing example

context

• problem statement

• evidence (rationale, examples)

• solution

• sketch

• references (to other patterns)

• synopsis

• credits

Both this definition and the list of pattern constituents very much confirm the validity of the approach and format used in this book: it contains all constituents from this list, apart from the synopsis, which is partly replaced by a graphical representation of the patterns hierarchy, and the credits, which are obvious since the patterns are part of this text.

In fact, as a consequence of these similarities, the pattern DOMAIN-APPROPRIATE DEVICES (H11) reviewed above was used as an example of an HCI design pattern on the official workshop poster presented at CHI 2000 [Borchers et al., 2001].

## 5.4 Evaluation of a Resulting System: WorldBeat

To judge the validity of a method such as the pattern framework described in this text, it is helpful to have a look at the resulting systems that have been implemented using the approach.

The pattern-based approach was first considered during user interface and software design of the WorldBeat exhibit. Even though the pattern languages presented in this book did not exist in their entirety yet when WorldBeat design started,the idea to wrap knowledge from the application domain (music in this case) into pattern form was one of its initial design goals. This is particularly true for its Musical Design Patterns component (see below). More patterns, including those for HCI and software design, emerged during the design of this system.

To better understand how this exhibit used patternsin its design, its overallarchitecture and features are outlined here.

## 5.4.1 Project Background

WorldBeat is an interactive music exhibit that was designed forthe KnowledgeNet floor ofthe Ars Electronica Center (AEC).

The AEC is a technology "museum of the future" [Janko et al., 1996], demonstrating to the general public how information technology will change the way we live, work, learn, relax, and communicate in the next century. It opened in Linz, Austria, in September 1996. The centre consists of five floors, each addressing a different aspect of life - from a 3-D CAVE in the basement that lets users experience virtual realities with a focus on entertainment and scientific visualization, to the Sky Media Loftcaféon the third floor with a focus on personal and Internet communication.

Its second floor, KnowledgeNet, focuses on aspects of computer use in learningand working environments. It was designed andequipped byour Telecooperation Research Group at Linz University. It consists of a Class/Conference Room of the Future [Mühlhäuser et al., 1996], demonstrating the use of group support systems, teleconferencing technology, interactive whiteboards, etc., and an area withWorld-Beat and other individual exhibits that deal with certain subject areas such as new media, new user interfaces, or new learning approaches, in more depth.

The entire floor was designed to convey the message that careful use of information technology can make learning a more active,cooperative, and motivatingexperience.Naturally, this also had a strong influence on the design of the WorldBeat user experience.

## 5.4.2 System Features

WorldBeatwas designed to show AECvisitors new ways of interacting with music with computer support. Consequently, the entire exhibit is controlled using just a pair of infrared batons. This fulfilled our goals of creating a consistent way to control the exhibit, and of creating an innovative, appearance to attract visitors. It also led to a nontechnical look, which avoids scaring off computer novices, and resulted in an input device that was much more appropriate for the domain “music"than standard mouse and keyboard, but without intimidatingvisitors with a professionalmusickeyboard orsimilar instrumental interface. Both batonsare used for musical input in the various modules described below, with the right baton doubling as pointing device to select features on-screen.

Thefollowing software modules were designed and implemented for WorldBeat to demonstrate new ways of computer-supported interaction with music:

• The Virtual Baton module enables the visitor to conduct a piece of music. It shows that a computer system can play back a stored score while leaving (rhythmic and dynamic) control over the actual performance to the user.

• In the Query ByHumming module, visitors hum the beginning of a song, and the computer locates the complete piece in its database. Thisdemonstrates how computers can simulate human musical recognition processes.

With the MusicalMemorymodule, visitors can test how good they are at recognizing instruments through their sounds alone. It is an example of a game-like courseware to learn about music.

● In the NetMusic module, visitors can play together withpartners over the Internet.Itdemonstrates the cooperative possibilities ofcomputer-based learning environments.

![](images/617ae9b11d90f78ff0943bfef3aebd7c3d1490ceed0014441af5a4214bc987df.jpg)  
Figure 5.1: The Lightning II infrared batons by Buchla and Associates.

Finally, usingthe Musical Design Patterns module, users can change basic parameters of musical improvisation and performance "patterns", e.g., the "groove" (swing) in a blues piece, and they can even improvise to the music without playing wrong notes. This module shows that computers can offer a completely new way of creating music that can be attractive and rewarding to all players, regardless of their prior musical knowledge and abilities.

## 5.4.3Implementation

The WorldBeat exhibit runs on an Apple Power Macintosh® 8500/120 or higher computer. A Musical Instruments Digital Interface (MIDI) interface connects it to a Buchla LightningII spatial MIDI controller [Rich, 1996]that consists of two wireless, infrared batons (see Fig. 5.1), a tracker unit that we attached to the computer monitor, and the base unit that contains the controller interface and MIDI sound module. The batons are battery-operated, and each features an additional action button.The exhibit further consists of a microphone connected to a Roland pitch-to-MIDI converter (for QueryBy Humming),and standardaudioequipment (amplifier, tape deck, speakers, and headphones).

We developed the WorldBeat software using the MAX multimedia programming environment [Dobrian, 1995] by Opcode Inc., a development system especially for applications that process MIDI data in real time. MAX supports visual programming for most standard tasks. Applications are created as a hierarchical network of patches that each process data (usually MIDI messages) in a certain way.We extended MAX byimplementing new patch types, for example to manage the graphical user interface of WorldBeat.

The idea to use the infrared batons as navigational devices resulted in the following data flow in the WorldBeat system:

• The visitor stands in front of the exhibit (see the figure on p. 133), looking at the large display, and gestures with the two batons in her hands. Each baton contains infrared light-emitting diodes that continuously emit signals in all directions.Special signals are sent when the action button on a baton is pressed or released.

• The infrared tracker, mounted directly below the monitor, measures the angles at which it receives the signals from the two batons, and converts these into horizontal and verticalposition data with a resolution of 128 steps in each dimension. Italso uses the button press/release events sent from the batons to determine the current buttonstates. Thisresults in astream of tuples $( x _ { 1 } , y _ { 1 } , b _ { 1 } , x _ { 2 } , y _ { 2 } , b _ { 2 } )$ beingsent to the Lightningbase unit,with coordinates $x _ { i } , y _ { i } \in$ $\{ 0 , . . . , 1 2 7 \}$ and button flags $b _ { i } \in \{ 0 , 1 \}$

• The base unit converts those tuples into MIDI messages that imitate fourcontinuous andtwodiscrete MIDI controllers, and sendsthose out to itsMIDI port. The unit also contains basic gesture recognition which its presets use to directly create MIDI notes from downward "beat" gestures. This is used by WorldBeat modules that just require the user to play a virtualinstrument with the batons in a drumsticklike fashion.

•In the more advanced WorldBeat modules, the MIDI controller data is sent viathe MIDI interface to the Macintosh serialport, where it is picked up by the WorldBeat system and interpreted in several ways: the interface manager computes the cursor position on the screen depending on the position of the right baton, and the currently selected WorldBeat component usually uses the data to perform other actions.

• All resulting events that describe MIDI playingmessages are finally sent back from the Macintosh via the MIDI interface to the Lightning base unit.It contains a soundcard with sampled instrument sounds that follow the GM(General MIDI) standard for MIDI instrument setups. The base unit creates the requested audio signals, which are then sent to the amplifier and loudspeakers, tape deck, or headphones.

## 5.4.4 Usage Scenario

To explain how the visitor actuallyinteracts with the system, the followingsection describes the interaction metaphors used in each module.

When walking up to the exhibit, the visitor first gets a short on-screen explanation how tonavigate with the batons. Since the Lightning system features two batons, we established the convention that the right baton is always used for navigation, i.e., replacing the mouse. The visitor simply points at the screen where a yellow spot shows the current cursor position, and presses the action button to select something.

Playing virtual instruments in the Joy-Sticks module uses metaphors that are built into the Lightning hardware and depend on the instrument type. Instruments that are played with one or two mallets (includingdrum kits, xylophones and similar instruments) use a natural mapping: downward beatgestures playthe instrument(s) in avelocity-sensitive way.With chordalinstruments, either two-finger operation is employed (as in one of the piano settings), or a number of fixed chords are placedinto2-D space and can be triggered by beat gestures at their position (as in a guitar setup). Finally, instruments that in reality require some different action to play a note (like windinstruments) are simulated usingthe action button on the baton to play a note,and the 2-D baton position information to control pitch and velocity simultaneously.

Conducting a piece in the Virtual Baton module uses a more refinedgesture recognition than the one built into Lightning, to give exact control over the playback speed and dynamics of a classical piece. The software tracks the right baton, concentrating on vertical movement only, and plays the next beat each time it detects a change from downward to upward movement. Gesture size determines playback volume. The original algorithm was developed by a group of computer music professionals [Lee et al., 1992]; we adapted it to be usable by normal visitors, and integrated it into WorldBeat.

Improvising in the Musical Design Patterns module finally uses a new musical interaction metaphor: the visitor again plays with downbeat gestures on an “invisible xylophone" in front of him. The actual notes that are mappedonto the "keys" of this xylophone, however, are constantly recomputed by the system tofitinto the current harmonic context of the accompaniment.That way, the user has complete control over rhythm and melodic shape of his performance, while the system modifies his input with its own harmonic knowledge tocreatean aesthetically pleasingresult. For musical experts, this support can be switched off, showing the adaptability of the system to different user experience levels.

This last component also included the first examples of the pattern principle: various musical concepts and aspects of the playing styleof the accompanying blues band were modelled by groupsof interactingsoftwareobjects, and equipped with a user interface that allowed users to experiment with those concepts and understand them by interacting with them. Some examples are:

•The TRIPLET GROOVE(M9) playing pattern of the accompanyingband was made accessible through an on-screen slider. While the band is playing, visitors can change the timing of this accompaniment.

• The degree of freedom given to the bass player in conctructing a bass line can be adjusted interactively, or a standard WALKING BASS (M10) pattern can be activated.

• For improvisation, visitors can choose between a virtual vibraphone containing only a PENTATONIC SCALE(M7) plus BLUENOTES (M8),or a full chromatic version.

In all modules, we supplied a visual interface designed in cooperation with a graphic artist that allows the user to navigate through the functionseasily andsupports them with brief online descriptions of the current metaphor and features.

A more detailed storyboard of a typical interaction with WorldBeat is given in appendix B.

## 5.4.5 Evaluation

Four types of evaluation took place in developing the WorldBeat system and its user interface: during the design phase, we continuously had novice users have a look at our interface and had them use the exhibit modules that were already working. As a result, we redesigned and improved navigation and visual appearance several times.

During the opening week ofthe AEC, the author spent five days at the exhibit, demonstrating its use to visitors and receiving direct feedback, but also observing users and recording interaction problems and common errors. This showed that using the batons for navigation andplaying posed no problems to users, althoughsome detailssuch as the exact conducting movement, and the fact that most users would not read lengthy instructions, required us to redesign the online help.

Improvising in the Musical Design Patterns module turned out to be the most attractive component. Users enjoyed "jamming" with a blues band without playing wrong notes. This module appeared to have found the right balance between free user input and system guidance. With freedom in rhythm and melodic shape, nobody cared that the keyboard constantly changes to offer a matching scale.

It also showed that modelling musical concepts as “patterns", byturningthem into software objects with an appropriate user interface, helped visitors greatly to understand those principles. For example, it was frequently observed that visitors quickly grasped the concept of groove in jazz, by playing with the on-screen groove slider for a few seconds. It usually takes the author much longer to explain this concept to musical amateurs without the help of such an interactive tool.

After the opening week, the AEC conducted a survey among visitors. Each of the 13 major exhibits was given a grade from 1 ("very easy to understand, very interesting") to 5 ("very complicated to understand, very uninteresting").The 104 participants gaveWorldBeat an average grade of µ = 2.08, i.e., the second best grade possible, with a standard deviation of σ = 1.12.

The participants were also asked to list their three favourite exhibits. Here, WorldBeat reached the third position, with 13.5% of the participants listing it in their "Top Three" list. Onlythe two million-dollar virtualrealityinstallations in the AEC—the 3-D Cave, and a VR flight simulator—were listed more often thanWorldBeat, whose hardware can be purchased for around US\$15,000.

Finally, WorldBeat wassubmitted to the1998Multimedia Transfer competition, which has the goal of honouring academic software projects that show an outstanding success oftransferring research ideas into concrete systems. Selected in a two-phase competition from among 160 submissions comingfrom academic institutions throughout Germany, Austria, and Switzerland, WorldBeat became one of the nine Multimedia Transfer Award winners.

Since then, the system has been demonstrated to the public on many occasions. It remaineda permanent exhibit in the Ars ElectronicaCenter for four years from 1996 until 2000, and wasexhibited at other locations, such asthe Techniek Museum in Delft, The Netherlands, for most of 1998.

Details about the design ofthe WorldBeat system, particularly its user interface design and evaluation, can be found in [Borchers,1997], and in the video proceedingsof that conference. The video, as well as additional material about the system, is also available online on the actibits home page (see appendix A).

## 5.5 Reusing Patterns

The languages created during the design of WorldBeat were reused and refined in a series of follow-up projects.

## 5.5.1 The Interactive Fugue

In the Interactive Fugue project, the author worked with a graduate student to develop an interactive exhibit about Johann Sebastian Bach's classical fugue style of composition. In the final system, users can record their own fugue motif, create a simple fugue from this material, and learn about the structure of this musical style in the process (see Fig. 5.2). The system uses a baton-based interface similar to WorldBeat for input.

This project was initiated to prove the validity of the pattern-based approach presented in this book. Therefore, its entire design process, from requirements analysis to implementation, was based on this pattern format.

![](images/a9e8dbcb92d586d5d9eba5e892c1aa2ea330fc03b661e5a9b707d088925c550c.jpg)  
Figure 5.2:Openingscreen of the Interactive Fugue exhibit, offering the user tolisten to some classical fugue pieces, compose their own fugue, or hear other visitors'compositions. Additional information about Bach is available via his portrait.

For this project, 15 HCI patterns from the languages of the author, as well as from the collection by Tidwell [1998], and several new patterns were used to inform the user interface design. Here, the pattern format proved particularly useful to carry over experience from the earlier WorldBeat project to this new effort.

Moreover, the application domain (classical fugue composition)wasdiscussedwitha music teacher and expert in this field, who helpedusto model the fundamental concepts as a language of 16 patterns forfugue composition, which is also included in [Dannenberg, 1999]. The music expert was quick to understand the pattern format, agreed to its general appropriateness for this field, and was able to discuss musical issues using this approach quite well.

The project also made use of several software patterns that were partly adopted from the “Gangof Four" book [Gamma et al., 1995], such as theFAçADEpattern to hide different subsystem interfaces behind a common interface, and partly developed originally. These altogether 11 patterns are also included in the above Master's thesis.

## 5.5.2 Personal Orchestra andVirtual Vienna

The most current projects that served both to use the existing pattern languages, and to refine them, are two interactive exhibits designed by the author forthe HOUSE OF MUSIC VIENNA (see appendix A forthe URL), a large exhibition centre in the heart of Vienna that lets visitors explore the rich musical history,present, and future of the city.

Thefirst exhibit, PersonalOrchestra, lets visitors conduct a large video andaudio rendition of the Vienna Philharmonic orchestra. The materialwas custom-recorded by us in the Golden Hall, where the orchestra traditionallygive their New Year's concert that is broadcast worldwide. Visitors use the infrared baton technology to control not just volume, but also the exact speed of the orchestra playing,as well as the emphasis on individualorchestra sections, through conducting gestures in real time. The system builds on our experiencewiththeWorldBeatconducting feature, but adds a video display of the orchestra, and uses original digital audiomaterial instead of artificialMIDI sound generation for audio. Successful conducting is rewarded with a digitalphoto of the visitor in front of "his" orchestra.

The second system, Virtual Vienna, is a virtual reality city tour of Vienna, focusing on places that are important from a music-historical point of view. It uses a large display and spatial audio to immerse visitors in a photorealistic panoramaview of a place within the city. Users can move around in this panorama using a custom-designed NaviPad with three degrees offreedom, and change to other places either using hot spot links within the panorama, or by choosing a place from a mapthat is shown on a separate display integrated into the NaviPad. Information about objects of particular interest is available through hot spot links within the panorama that lead to short descriptive pages with text and graphics about the object in question.

At the time of writing, our formal user studies to evaluate thefinal systems are yet to be finished. However, the exhibits have generated very positive feedback already. In particular,the HOUSE OF MUSICVIENNA recentlyjudged the Personal Orchestra system to be its most attractive exhibit.

The HCI design patterns presented in this book were used during the development process. The HCI pattern language for interactive exhibits was passed on to the customer, and in subsequent design meetings, it helped tremendously to quickly explain and discuss design decisions.

As an example, at one of these meetings for Virtual Vienna, the customer suggestedthat several exhibits with standard monitors be installed instead of one exhibit with a large projection. The idea was to lower the cost for display hardware and increase visitor throughput. However, after pointing out that this idea would violate several of the HCI design patterns presented, particularly IMMERSIVE DISPLAY(H13)and COOPERATIVE EXPERIENCE (H3), the idea was withdrawn in favour of the single larger exhibit. Sound on this system was also made optional, and provisions for several headsets were installed, to avoid interference with the ATTRACTION SPACE (H2) of the neighbouring Personal Orchestra exhibit.

During meetings and written communication, not only with the customer, but also with the software development group, being able to point to the HCI patterns saved significant time that would otherwise have been spent on repeatedly explaining the importance of the respective concepts and their rationale from past projects. The concise and easily remembered pattern names especially were extremely valuable in this context, and helped to create a common vocabulary within the entire design team.

## 5.6 Study of Didactic Usefulness

An important claim made by this work is that the HCI pattern format is a form suitable not only to capture design experience for follow-up projects, but also to introduce new designers to important HCI design concepts, and to use this form as a teaching aid in HCI design courses.

During an HCI design course for first-year computer science undergraduates in the summer 1999 term, the author spent one lecture of 90 minutes altogether dealing with HCI patterns: the idea of patterns, their origin in architecture, and their use for capturingHCIdesign concepts were explained, andcopies of Jenifer Tidwell's Common Ground HCIpatterncollection handed out. Students then took about 15 minutes tostudy the collection,andto find patterns that they could relate to their first own user interface prototyping exercise on which they were working at that time.

Informal feedback during this exercise, and in the following week while the prototypes were finished, was very encouraging.Most students were ableto immediately relate several patterns to problems they had been facing during their design themselves.

This was confirmed in a formal statistical evaluation, which was carriedout two weeks after the above lecture, in an unannounced lecture evaluation.Students wereaskedto rate various aspects of thelecture, including the following questions concerning the design pattern approach presented:

1. I remember the following HCI design patterns:

2. For the overall understanding and remembering of user interface design concepts, the patterns were (1=very useful ...5=completely useless).

3.I was able to find problems and solutions for our own design project in the pattern collection (1=absolutely ...5=not at all).

4. I can imagine using this pattern concept in future design projects (1=certainly yes ... 5=certainly not).

## Results and Discussion

$n _ { 0 } = 3 2  \it$ students filled out the questionnaire; of these, $n =$ 26 answered the questions about patterns. The results are shown in Fig. 5.3.

![](images/c610b995b3a53568a7014775b82777eed2c61ae9ee642603833e64fd8a644cd8.jpg)

![](images/88dba86d6e45973769ffbde9ad50dfe05c9e1ba45e47a82ba92841f673904034.jpg)

![](images/b12044419377659af9da7ddcf01233a937d0b1b588a754dfb4dfb26571dcaeb9.jpg)

![](images/2f4afa4060367c4c5d9fb61f03a41e80cf01e5b54e982dce3083c7d3147c3bc4.jpg)  
Figure 5.3: Results of the patterns survey, showing how many patterns were remembered, and their perceived usefulness for learning, current work, and future projects.

On average, $\mu \approx 1 . 7 3$ patterns wereremembered, with a standard deviation of $\sigma \approx 1 . 6 5$ Lecturers will agree that this is quite promising, considering that students only spent relatively short time with the material during the lecture, only looking at a few patterns in any detail, and that thematerial had not been revisited by students for the final examinations yet. The vocabulary function of HCI design patterns seems to have succeeded quite well. The large standard deviation reflects the fact that several students wrote down no patterns at all, an effect that does not fit into the standard distribution; with an examination-like test situation, they may have spent more time trying to remember some of the patterns.

The usefulness of the pattern language for understanding HCI design issues was rated with an overall $\mu \approx 1 . 9 6 ,$ i.e., with the second-best grade possible, with a relatively small standard deviationof $\sigma \approx 0 . 6 5$ ,indicating a high level of consensus among the students.

Usefulness for current project work was rated slightly worse, but still with an overall second best grade $( \mu \approx 2 . 2 3 )$ Aslightly higher standard deviation $( \sigma \approx 0 . 8 9 )$ shows that there was less consensus on this question.

Finally, the confidence that this pattern concept would be reused in future projects was again quite high $( \mu \approx 1 . 9 4 )$ with relatively great consensus $( \sigma \approx 0 . 8 1 )$

In all, these results indicate that a pattern approach in HCI educationis useful and convincing. Throughthe structuredcombination of widely known examples with generalized recommendations, even first-year undergraduates can quickly relate to this format, and find it useful and worth considering for their further projects.

## 5.7 Publishing Peer Review

A final indication that the method and patterns presented in this book are sound is the fact that, based upon initial feedback from several experts in the field who reviewed a late draft, two major international computer science publishers have expressed in writing their intent to publish this work as part of their programme.

## 5.8 PET: A Pattern Editing Tool

One of the main reasons stated for the formal model of pattern languages as presented in chapter 3 was the possibility of building an authoring and browsing system to write, read, and browse a pattern language. This formal model defines a pattern language in a way that makes it quite straightforward to represent it as a hypertext:

• The pattern language is stored as a graph with patterns as nodes, and the references between patterns as directed edges, or links.

• Each pattern node consists of a sequence of contents blocks for name, ranking, sensitizing example, context, problem statement, several existing examples, solution, diagram, and references. Each content block is a multimedia container for text, graphics and/or other media types.

• The context andreferences blocks contain bidirectional links to other patterns within their textual section.

The pattern languages presented in this book, while written as readable texts without disturbing explicit text tags for each pattern component, nevertheless follow the formal definition exactly, and are therefore highly structured through implicit, typographicalrules. Inserting these patterns into a hypertext environment is therefore an easy task (see Fig. 5.4 below).

Numerous systems exist that try to make design patterns and guidelines accessible with computer support (see, e.g., [Alben et al., 1994]), and at the CHI 2000 workshop, an initiative was founded by Trætteberg and Welie [H:Trætteberg00] that has created an online repository of HCI design patterns, together with some means of adding review comments to these patterns.

The following sections show the requirements analysis for such a tool, and present the design anda prototype of a possible system, the Pattern EditingTool PET.

## Target Group

The system is supposed to represent pattern languages independently of their domain. This means that typical users are HCI designers and software engineers, but also user representatives and experts from the application domain of an interactive software design project. Moreover, interdisciplinary use asoutlined in the approach in this book will lead to people frequently browsing pattern languages in whose domain they are not themselves trained professionally.

## Tasks and Scenarios

Independently of their professional background, users fall into three categories according to the maintask they may wish to perform in relation to a pattern language: they may be authoring and creating it, they may act as peer reviewers of an existing collection, or they may be using it with the goal of applying the patterns to their current design problems, or to learn about a design field in general. Only the latter activity,though, will normally include users from other professions.

Typical sample scenarios are the following:

1. An HCI design practitioner needs to design an interactive exhibit, a field that he has not worked in before. He would like to find out what to look out for in interactive exhibit UI design. He will therefore be interested to get a quick overview of an existing HCI pattern language on the subject, and he will also want to find entries quickly via a keyword or full-text search.

2. A software engineer with some interest in research has been asked to peer-review a pattern collection written by a colleague,in the fashion of a writer's workshop. She willwant to be able to browse the collection for overview,and to read individual patterns on-screen or asprintout, andwill need to add comments to each pattern as suggested by the workshop procedure.

3. A domain expert about music has been asked to formulate his expertise as a set of patterns about classical music composition. He would like to write the body text with his favourite word processor, then convert it and add audio or score examples to the material for clarification.

## Design: Features and Constraints

The above scenarios lead to an initial conceptual design of the PET system that includes the following functionalities, in order of importance:

• creating, annotating, and reading pattern texts;

• includingmultimedia examples, such as audio and video clips, or diagrams and photos, as well as links to other patterns;

• creating an intuitive, graphical overview of the existing pattern hierarchy;

• providing quick access to patterns via keyword or full text search;

• offering a sequential way to navigate around the language and print patterns.

In addition, the system should fulfil some constraints that help its widespread use:

•It should not require explicit installation of some specific application software or the use of a specific operating system.

• It should allow for links to other patterns and pattern languages via internet standards.

•It should base the content format on widely accepted, open standards for maximum accessibility.

## Design: Architecture

The above requirements can be met by a system architecture that uses a document format basedon anExtensible Markup Language (XML) structure definition. A first such specification for user interface design patterns was developed by van Welie [2000]. Byapplying the formal definition from this book to that XML model, it was possible to improve the modelling of links between patterns.

However, it would be unwise to force a single "correct" pattern structure definition onto authors, since many mayalready haveproduced patterns that theywill bereluctant to rewrite, and also because the structure put forward here will not always be the best to use. Therefore, the system should merely suggest the use of thatstructure, but allow for the inclusion ofadditional pattern document classes, with different levels of formalstructuring. A minimum pattern format, for example, could simply be defined as a monolithic text document that does not includeany additional external information about its inner structure.

Pattern documents can then be displayed in an XMLcapable web browser window. Additional functionality, such as the graphical overview, is supplied via Java applets.

Each pattern is then accessible via a URL of the corresponding document. More detailed references can point to individual content blocks (components) of a pattern.

The authoring of individual contents blocks is best left to existing specialized tools. It would be unwise to try and force an “integrated pattern writer's environment"complete with editors for all sorts of media types onto pattern authors, since work practices, systems used, media types, and personalpreferences for content creation are highly varied.

Instead, the system should allow the author to hook his prepared content blocks into the pattern language, and support arranging, reviewing, and browsing this growing collection.

## Storyboard of Sample Implementation

This section describes a sample interaction with PET, and gives a few screenshots that show how the system can be implemented.

An author prepares his pattern content blocks in XML format with his favourite authoringtools, using a document definition of the pattern form used in this book, or a different one that is more suitable for his pattern format. He links those content blocks into PET by specifying the base URL of the pattern. PET parses the pattern document, and displays it in a structured form that makes the various components clearly recognizable(seeFig. 5.4). Problem and solution, the central components of each pattern, are emphasized visually to support quick visual scanning.

The user can customize this display by hiding or showing each pattern contents block,a setting that is retained when switching to a different pattern.Text and graphics are displayed directly, while audio and video samples can be activated by selecting their icon representations within the pattern contents block.

Links inside the context and reference sections of each pattern also lead to the respective target pattern. In addition, PET offers a breadth-first-search sequential navigation metaphor through the entire language via "next" and “previous" buttons, for those whoprefer to read a language from beginning to end. This navigation metaphor also defines the contents structure that PET uses to print the language for easier sustained reading. File handling, printing, and searching menus are not shown, for the sake of clarity.

As more patterns are created, PETautomatically builds and updates a graphical representation of the pattern hierarchy as a whole (see Fig. 5.5), which uses a semi-automatic layout algorithm and can be displayed separately,or next to the current pattern. The author, as well as the reader later on, can jump to patterns by selecting them from this graphical overview. The solution statement from each pattern is displayed as a short help text when the user moves the cursor over a pattern, so he can see what the pattern isabout before jumping to it. (This feature uses the DYNAMIC DE-SCRIPTOR pattern from chapter 4.)

![](images/4815131e032a5ed87f13c2548c13886efbb49c34bb7af76585ad90f1df007b95.jpg)  
Figure 5.4: A screen shot of PET displaying an individual HCI design pattern.

![](images/b7c48e272e57f5131007ad309591675198f653a865eccf25a43e1e8554034a37.jpg)  
Figure 5.5: PET displaying an entire HCI pattern language graph. Moving the cursor over a pattern pops up its solution statement as a quick help text.

Reviewing in the form of the Writer's Workshop presented in chapter 2, and exemplified earlier in this chapter, strongly depends on the socialinteraction of the reviewers. Nevertheless, it makes sense to collect comparable comments from reviewers who access the pattern online, alone or in a group. For reviewing,PET therefore offers a way to add comments to each pattern contents block. PET requires the reviewer to classify each comment. It distinguishes between positive comments, and suggestions for improvement, each for both formal aspects and contents aspects, as well as summary statements.

As presented here, PET is just an initial iteration in the design of a suitable support tool, and serves as proof of concept to show that such support is feasible.

This concludes the evaluation of the approach presented in this book, and the discussion of tool support for such a framework.