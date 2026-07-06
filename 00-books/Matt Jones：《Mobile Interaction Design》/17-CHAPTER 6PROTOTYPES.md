# CHAPTER 6 PROTOTYPES

## OVERVIEW

6.1. Introduction

6.2. What is a prototype?

6.3. Different prototypes for different purposes

6.4. Low-fidelity

6.5. Higher-fidelity

6.6. Finishing the process

6.7. Issues in prototyping

6.8. A final note on development

## KEY POINTS

Prototypes provide common and unambiguous communication for multi-disciplinary development teams.

■ Low-fidelity prototypes support the possibility of having the end-users become part of the design team – ‘Participatory Design’.

Prototype creation requires compromises in time to create the prototype (hi-fidelity vs low-fidelity) and the functionality of the prototype (vertical vs horizontal).

Mobile prototypes often need to be evaluated over a long period of time, so must be robust.

## 6.1 INTRODUCTION

The goal of this chapter is to give you the tools to turn your ideas into something resembling finished software. This will involve the creation of prototypes.

In the words of Scott Jenson (Jenson, 2002), prototyping is a way to ‘fail fast’, his rationale being that if we fail enough times, then eventually we will get it right. No matter how good the designer, it is unlikely that their first design will fulfill all the varied user, engineering and esthetic requirements. Designers need to communicate these ideas to the various members of the team (and the end-users) in order for them to critique and comment on the design. The designer then alters the design and opens it up for another round of critique. And so on.

At some point the design phase ends and it becomes necessary to commit to a final design. The success of the final design will depend a lot on how many cycles of critique were completed. Using prototypes is a great way to ensure that you get the most out of design cycles.

## 6.2 WHAT IS A PROTOTYPE?

When you see the word ‘prototype’, what image does it bring to mind: experimental spacecraft, scale model, buggy software . . . ? Software developers almost always associate the term prototype with pre-release software, as there are various RAD (Rapid Application Development) software development methodologies that talk about iteratively developing software prototypes until they become final products. For artists or designers, it is usual to think of a prototype as being a rough pencil and paper sketch of the final artifact’s appearance.

Although there are no hard and fast rules about what a prototype is, the crucial thing is that it lets you express a design idea as quickly as possible. So, for programmers, it is easier to create an interface skeleton in Visual Basic than sketch the equivalent interface using pencil and paper. Artists, on the other hand, need not learn a programming language to create a prototype.

## 6.3 DIFFERENT PROTOTYPES FOR DIFFERENT PURPOSES

We can create prototypes for almost any design using a wide variety of materials and technology. Due to this diverse nature, it is important to understand the differences between various types of prototype and the value in building each different type.

One common way to differentiate prototypes is according to how closely they resemble the appearance of the final artifact. Prototypes which do resemble the final product are referred to as ‘high-fidelity’ and those which do not are referred to as ‘low-fidelity’. It is worth noting that this notion of ‘appearance’ relates to the user’s perception and not that of, say, the software developer. For example, we may have a software prototype which contains code to be used in the final product, but looks nothing like the final version – this would be low-fidelity as that is the user’s perception.

Obviously prototypes do not always fall neatly in the low-fidelity/high-fidelity classification. Instead, it is more useful to think of a scale starting with, say, paper sketches at one end and beta release systems at the other. In the next section we will discuss a number of prototyping techniques starting with low-fidelity and working our way to high-fidelity prototypes. Along the way, we will consider why each technique is useful and what you might expect to gain by building that type of prototype. As a brief rule of thumb, however, low-fidelity prototypes are more easily created and should therefore be used earlier in the design process before exact details are known. As the design process matures, so should the fidelity of the prototype.

## 6.4 LOW-FIDELITY

## 6.4.1 SELF-CHECKING

We’ve all had experiences where something makes perfect sense in our minds, but when we try to explain it to someone else, all sorts of embarrassing mistakes and flaws begin to surface. ‘‘It seemed like a good idea at the time’’ does not really cut it in interface design.

Prototyping is a good way of working through ideas, promoting, rejecting and refining them. Therefore, designers will often make low-fidelity prototypes for themselves to see whether their ideas make sense before discussing them with others on the team. The most famous example of this in mobile computing is Jeff Hawkin, who carried a piece of wood around in his shirt pocket to act as a surrogate for a PalmPilot (Bergman and Haitani, 2000). Sounds crazy, but it worked for him and the PalmPilot went on to succeed in a market of notable failures (not least, the Apple Newton).

A much more common form of low-fidelity prototyping is sketching an interface. By committing ideas to paper, designers are able to see how their interface might look: how many buttons are required, what warning lights and displays are needed to give feedback, etc. Figure 6.1 is a sketch showing the interface to a digital library system for mobile handsets. After some shuffling of components, making design compromises along the way, the interface contains the key elements which allow the user to interact with the underlying functionality.

![](images/b4855cabd6dcb17f5102ff7f51ef83b8591d7f1a8e00c00aa3f2a7b6b91e69e6.jpg)  
FIGURE 6.1  
A sketch from the design process which created an interface to the Greenstone digital library which allows content to be deployed on mobile handsets

As an alternative for those of us who find sketching a chore, we tend to use Post-it notes for each interface element, which can then be moved around without redrawing from scratch. In Figure 6.2, you can see the same interface created using Post-its on a whiteboard.

![](images/96473b3a4574ca3737346570f486587f1fc81d41383759e0ea6aad02a5531936.jpg)  
FIGURE 6.2  
The same interface, but using Post-it notes on a whiteboard

Another key, but less obvious, benefit of prototyping is the time it gives to reflect on a design idea in isolation from implementation issues. When struck by a design idea, there is a tendency, among programmers at least, to code up the idea, developing the design in tandem with the code. Often this leads to premature commitment to a half-baked design idea. I am guilty of this myself, and wasted about three months of programming time when developing the ideas for the new menu structure discussed in Chapter 8. In my rush to create a functioning handset, I glossed over design considerations and made some arbitrary decisions, such as the number of lines of text the menu should display. For example, had I taken the time to sketch out the interface before committing to code, I would have realized that I needed to use the bottom line of the screen to display the number and not use it to display further menu options. Again, it seemed like a good idea at the time.

## 6.4.2 COMMUNICATING WITH OTHERS

Just before we were married, my wife and I went on a course to help us prepare for married life. One exercise we undertook required one of us to describe an image and the other to sketch it based on the verbal instructions. It was one of the hardest things we’ve ever had to do – speech is the wrong medium to convey visual information. I believed I was following her instructions implicitly, but I ended up with a completely different shape.

For interaction and interface designers, the same holds true. I’ve sat at design meetings and discussed an interface with the programming team. I leave the meeting feeling confident that I’ve accurately conveyed my ideas and the programmers leave convinced that they too understand exactly what I want. When the demonstration rolls around, however, it is clear that the meeting was a waste of time.

## EXERCISE 6.1

## PORTABLE MP3 PLAYER – SPECIFICATION

Here is the specification for a portable MP3 player. The YAMP MP3 device will have the following features:

Play, Pause, Next Track, Previous Track, Forward, Rewind

Give status about track name, track length and battery status

Should fit comfortably in pocket.

Read through the specification and sketch a low-fidelity prototype that conforms to the specification. Now, show the specification (but not your sketch) to someone else and have them sketch it. Regardless of how many people you do this with, it is unlikely that any two sketches will be identical. Unless you use prototypes early on in the design phase, a lot of ambiguity is going to creep in. ■

Obviously, the best way to convey a visual design is to draw it. Many people are embarrassed by their sketches and hence reticent to show them to others. This is missing the point. The idea of an initial sketch is to convey abstract ideas, not give a look and feel for a final product.

A sketch of the interface is the first point in communicating a design idea with the rest of the development team. In particular, we have found that the combination of whiteboard and Post-its is very empowering. With paper and pen, of necessity, one person is in control and acts as a filter for updates to the design. With a large shared surface and independently movable controls, all members of the team feel empowered to make changes to the design.

## 6.4.3 INTERACTION PROTOTYPING

Having sketched the layout of the interface, it’s time to give some consideration to how someone will interact with the device. For this, we bring in to play the earlier work on scenarios. Scenarios allow designers to dry-run their ideas on the paper sketches provided. In Figure 6.3, you can see a prototype system we used for one scenario in the digital library application, sliding the appropriate ‘screen’ into position on the handset.

![](images/817fa98583cfbed0e4bf77f521344f11d6f692d9de4f3088013684465f267c0b.jpg)  
FIGURE 6.3  
A scenario being tested by moving the correct screen into position in response to user selection

Working through scenarios is similar to a technique called storyboarding which is used in the movie industry. The basic idea is that a series of sketches are drawn to show the steps required in interacting with the interface design. Note that although storyboarding is based in film, we have adapted it to take in ideas from state-charts to enhance the representation. For example, in Figure 6.4, the items down the left are separated by a dotted line which means that they are present on all screens. As we all understand state-charts, this works well for our group, but you may want to develop your own conventions. (We would, however, recommend you learn about state-charts as they are fantastically useful for designing any interactive system. A good place to start is Horrocks excellent book (Horrocks, 1999).)

![](images/f35c9b9eb5fa1a77d4ec364633e1ef9cb35ca4c775f28bb84e1ab2af8ca0bb57.jpg)  
FIGURE 6.4  
Here, the effect of each button on a screen can be seen. The items on the left are accessible at any time

The main limitation of storyboarding is its linear nature. Storyboards are constructed to accommodate a fixed set of sequential interactions. Of course, we know that interacting with computers rarely follows this model. Often users wish to explore and will take unforeseen paths through an interface. Therefore, as in Figure 6.4, we have shown possible paths through the interface, rather than examining one particular path through the software.

To support this type of interaction, we have adapted slideshow software. A package such as PowerPoint allows a number of screens to be joined in a nonlinear way. Each sample screen becomes a slide and clicking on a button causes a transition to the next screen in the appropriate sequence.

There are obviously more powerful tools one might use for this role, such as Flash or even video editing tools. In fact, systems such as SILK (Landay and Myers, 1995) use a digitizer to allow users to sketch directly into the computer and then link together the sketched screens to prototype screen flows. Our experience, however, has been that more advanced tools require too great an effort for most designers to learn. Slideshow applications, however, are taught to most students entering tertiary education as a matter of course. The simple ‘branching’ type interaction they support has proven more than sufficient for this level of prototype.

If you don’t want to go so far as to use PowerPoint, it is of course possible for one of the design team to play at being the computer and show the appropriate screen at the appropriate time. Within the HCI community, this is known as a Wizard of Oz prototype, where a human is used to simulate the part of a perfect computer. Usually, Wizard of Oz techniques are used to simulate artificial intelligence solutions or speech recognition – Gould and colleagues pioneered this approach with a ‘listening typewriter’ back in 1983 (Gould et al., 1983).

## EXERCISE 6.2

## PORTABLE MP3 PLAYER – FURTHER TASKS

For the YAMP MP3 player discussed in the last exercise, sketch out what will happen to the display when each of the buttons is pushed. Now, try your design with three target users, swapping the screens corresponding to the buttons they push (Wizard of Oz). Chances are you will find this tricky and frustrating (so will the user). Now repeat the exercise, but creating the display using PowerPoint. Create each screen as a slide and link together with the hyperlink feature. Sure, this is harder to do the first time you try it, but now that you have learnt, it is going to save you a lot of time and frustration in future. ■

## 6.4.4 EMPOWERING USERS

In the next chapter we will look at how functional prototypes (and final systems) can be evaluated with real users. However, we need not wait until that stage of development; we can, in fact, employ users to be part of the design team.

This is formally known as ‘participatory design’, where selected members from the end-user community develop the design along with programmers, interaction designers and the rest of the development team. Participatory design has a long history and comes in many forms. One of the most popular is PICTIVE (Muller, 1991). Based on low-fidelity prototyping, PICTIVE consists of a kit containing plastic versions of common interface widgets which the participants arrange on a shared surface (usually a horizontal whiteboard) until they reach a consensus of how the interface should appear. The shared surface is video-recorded throughout the session to provide a design rationale.

As noted in Section 6.4.2 above, the shared surface is a very democratic way of creating an interface by making the elements available to, and understandable by, every person on the design team. If you really care about having input from your users in the design process, this technique is hard to beat.

Another form of participatory design is related to live-action role playing. This technique is perhaps more applicable to mobile computing as it relates to users in their real environments. Essentially, participating users are given some low-fidelity props to act as surrogates for mobile devices (similar to Jeff Hawkin’s block of wood) and are filmed using these ‘devices’ in various work scenarios. In one example (Nilsson et al., 2000), the participant is a worker in a reprocessing plant who needs to monitor flow rate in pipes. The worker has a mobile device which he can use while walking round the factory to gain readings from various valves in the system. The mobile device then shows graphical representations of these values which allow the worker to diagnose problems and monitor performance. Of course, this rather relies on the willingness of the participants to be filmed and to role-play – neither of which come naturally to a lot of people.

In Figure 6.5, the participant is using a polystyrene ‘computer’ to take readings from cardboard ‘sensors’ in order to explain his design ideas to the development team.

## A Note on Low-fidelity Prototyping

Some of our work has been in virtual reality gaming, where the production costs are prohibitively high. So, before we start designing, programming and modeling, we play a ‘cardboard’ version of the game (see Figure 6.6). Playing in cardboard allows us to decide whether the idea has any merit before taking it to the rest of the team.

![](images/971f2a9b3cfb7cd4413ca714c0079f42737466e5de38c3a62cdd96e91071739d.jpg)  
FIGURE 6.5

A worker enacts a scenario using low-fidelity prototypes of mobile computers and sensors  
![](images/6528046d7e30ae70db742194882013b737e7cd93773cb38f211a21c556340613.jpg)  
FIGURE 6.6  
A low-fidelity prototype of a VR game using pens, paper and plastic figures

When we started using cardboard and paper, the rest of the team were very skeptical about the value of such an approach – virtual reality is a technology-heavy research area. Once they saw how quickly we could refine ideas and empower non-technologists to contribute to the discussion, they realized that cardboard is an essential component in virtual reality. Depending on the culture of the organization you are based in, you may need to do some work before they accept the validity of low-fidelity approaches.

## 6.5 HIGHER-FIDELITY

## 6.5.1 DECIDING WHAT TO PROTOTYPE

By the end of the prototyping stages listed above, you should have a clear idea of the basic design and be in a position to draw up a fairly comprehensive list of features. It is then important to see how well the designs support the tasks and scenarios of the target user groups. At this stage of the process, one does not want to implement every feature and screen, so it is essential to determine which aspects of the design are critical and which are not. These critical aspects are then tested in another round of prototyping.

A large part of prototyping is about deciding what to test and what not to test. If you tested everything, then you would be creating a final product and not a prototype. Prototyping, therefore, requires intelligent compromises to be made. One way to think about compromises is in terms of horizontal and vertical prototypes. Horizontal prototypes show as much of the functionality as possible, but none of the functions are active. Vertical prototypes, on the other hand, are designed to test one particular part of the functionality of the device. In the case of the cellular handset design (Chapter 8), we created a vertical prototype which tested the ease with which menu commands could be accessed. Although every aspect of the menu access system was implemented, activating the functions had no effect.

In order to guide the trade-off between horizontal and vertical prototyping, it is worth returning to the original scenarios for the design. Nielsen (1993) suggests that prototypes should primarily support the user scenarios, so that we can use the prototypes for future user testing. So, provided the user sticks to the path of the scenario, it will appear as if the prototype is fully functional. If the user wanders from the path, obviously this illusion will be shattered.

As we move on to looking at creating higher-fidelity prototypes, it’s time to start focusing on the particular needs for creating prototypes for mobile devices. For example, in the next chapter, we will discuss the benefits of conducting longitudinal studies with mobile devices. Longitudinal studies will require the prototype to be used over extended periods – one study ran for over a year (Petersen et al., 2002). This pretty much rules out the use of any prototype which relies on using a human to play computer and fake the interaction. In fact, a viable period could be as little as a few hours. In their study, Liu and Khooshabeh (2003) report facilitator fatigue after a few hours of playing computer.

## 6.5.2 HARDWARE AND SOFTWARE INTEGRATION

Prototypes for mobile devices create interesting compromises not found in other devices due to the close integration of software and hardware. Software prototypes for desktop computers can rely on the fact that the input and output hardware is fairly standard (monitor, screen, keyboard, etc.), allowing the prototyper to focus on software issues alone. With mobile devices, the hardware is often very specialist and optimized to the application. In an ideal world, the hardware would be complete and the software tested on the platform. However, in reality, the hardware and software are highly interdependent and developed in tandem – think of designing the interaction for an iPod without the scroll wheel hardware available. Sadly, due to the costs involved, the hardware iteration cycles are much slower than those for software. This means that the software prototypes have to be developed on hardware that is completely different from the deployment platform.

Another reason for using different hardware is the performance characteristics of the processor and memory of the mobile device. If you’re developing an application for a device slated for release in a year’s time, then current devices will obviously not have the processing or memory resources available at release time. This effect is much more pronounced for mobile systems than for desktop systems; most current applications do not use anything like the full capability of the available processor. This is not the case with current mobile devices – the form factor, and other issues such as battery life, mean that processor speed and hardware resources are at a premium.

So how do you prototype software for hardware that doesn’t exist?

## PC-based

The simplest solution is to develop the software on a desktop PC using a software emulator. Many development systems come with a variety of emulators (see Figure 6.7). For programmers used to working in a tool such as Visual Studio, this can be a very easy and natural progression. To help programmers migrate to the mobile platform, Microsoft and Sun use subsets of their desktop APIs rather than force programmers to learn completely new libraries. So, for example, Microsoft PocketPC and Mobile devices carry a subset of the .net APIs in Flash-ROM. Not only does this reduce development time, but by using ROM, the libraries do not take up valuable volatile storage space.

A further benefit of this subset approach is that it better supports evolutionary prototyping (more on this later) and gives the programmer a clearer idea of what is possible on the target platform.

For many programmers, the approach outlined above may be overkill. Perhaps the interface they’re building is not sufficiently complex to warrant learning the intricacies of the API subset. Or perhaps they’re creating an interface with a completely different look and feel than that currently supported on a standard emulator. One approach we’ve used in these instances is to create what is essentially an interactive photograph. Figure 6.8 shows a prototype we used to evaluate the alternative menu system in Chapter 8. It’s a Java applet (we wanted people to have access to it on the Internet) where invisible buttons are overlaid on the various keys and buttons present on the scanned photograph. We’ve reused this code for various prototypes we have built, so the initial effort has more than paid off.

One great benefit of developing this way is the separation between the application logic and the interface code. In the case of the new menu scheme, we wanted to check the underlying algorithm first to see whether it was possible to structure functions according to the scheme we had developed. We therefore created this structure in Java. Once it worked, we could simply wrap a simple presentation layer around the object to facilitate the user testing. Once that was complete, we could then use the same code for the final product. Sadly, the interface never made it to market, but that’s a different story.

Please note that it was not possible for us to test the interaction with the new menu scheme using paper prototyping – it would be impossible for the Wizard of Oz computer to keep up with the user interactions. This was also the case with the photo browser we discuss in Chapter 10 – there is simply no way we could re-create this effect in paper.

![](images/6df42f69290897f514b5b0b1348e06e51cb4e1c9043845bcb1fbf08d6dcc5e81.jpg)  
FIGURE 6.7  
A screenshot of the PocketPC device emulator in Microsoft Visual Studio

![](images/5f16f9b34045da3f1151d819ed1f5375b03cb163d9ab6b23ba9342fb2f921b47.jpg)  
A screenshot of our Java-based emulator  
FIGURE 6.8

For designers with limited programming experience, using Java or .net is not a viable option. Rather than using a full-strength programming tool, designers may choose to use more traditional prototyping tools, such as Flash, and create their own mobile prototype. While Flash and similar tools provide a good migration path for those who are familiar with image-editing software and want to add interaction to their designs, there are some pitfalls. Chief among these is the problem of extracting application logic from the prototype. Code in this type of scripting tool tends to evolve organically, which is great when prototyping but hopeless for use in the final system. Our experience has shown us that even flexibility starts to be lost for any sustained development cycle – over time, the patching and changing makes the prototype more and more brittle. If you want to use one of these tools, you should be prepared to throw your code away at the end of the prototype stage and start anew in another language for final implementation. (More about this when we discuss evolutionary and revolutionary prototyping.)

## Pitfalls

Developing on PCs has all sorts of benefits as discussed above. However, there are a number of things to be aware of:

1. Keyboards. The PC has a great big keyboard which makes data entry rapid. This can skew the value of user testing if you are investigating an application which is reliant on a lot of text entry.

2. Mice. Most PCs use a mouse as a pointing device, a device which is almost never found on a mobile computer. This function is often replicated with a stylus or trackpad. Anyone who claims these devices are equivalent to a mouse has obviously never tried dragging and dropping on a mobile computer. It may be possible to skip over this difference if the application is not too reliant on the characteristics of the input device – for example, there is little difference in clicking a cellphone button with a finger or a mouse. For other applications, such as handwriting recognition, or the photo browser in Chapter 10, the input modality is crucial. It may be possible to fake this using a Tablet PC or pen input device like a touch-sensitive tablet, but be careful that any evaluation you conduct is not skewed by these hardware differences.

3. Portability. Desktop personal computers usually live on desktops and cannot be easily moved around. It is therefore hard to mimic real-world situations that users of mobile computers will encounter – direct sunlight on the screen, noisy environments, etc. Also, we run into the problem of conducting longitudinal or contextually based evaluations. Mobile computing is, after all, mobile and it makes little sense to conduct only laboratory-based evaluations.

4. Weirdo hardware. This is really the converse of problem 2 above. In this case, the mobile device has hardware which is not available on the desktop PC. Jog-wheels, thumb scanners, even Bluetooth connections are rare on most desktop systems. It’s possible to cover for these inadequacies, however. (For example, we use a Griffin PowerMate – www.griffin.com – as a jog-wheel replacement.) Again, it should be noted that these devices will inevitably be different from those found on the final hardware of the system. Caution should be exercised in drawing conclusions from prototypes with this type of replacement hardware.

5. Performance. Desktop PC performance will always be faster than that of mobile computers. Make sure that it is possible to execute your application on the target hardware.

## Using a General Mobile Platform

To overcome the problems listed above, with the possible exception of problem 4, one can use an existing mobile device or platform to develop prototypes.

A device such as the HP iPAQ 5550 has ample computing resources (400 MHz XScale processor, 128 Mb of RAM) and connectivity (802.11b, infrared, Bluetooth and an optional cellular jacket). This device also has a variety of text input modes and a high-resolution touch screen.

There are fewer high-level software prototyping tools available for mobile computing platforms than for desktop machines, due to the relative market size (a version of Flash is available for PocketPC, however). If you’re going to create a software prototype for a mobile device, almost certainly you’ll have to do some programming in a language such as C# or Java. To help programmers get up to speed, there exist multi-platform APIs such as Microsoft’s .net or Sun’s J2ME. In each case, the mobile platform represents a subset of the full desktop API, so that programmers can transfer more easily between platforms.

If you do decide to prototype on the iPAQ or similar PDA, we would recommend that you write all your code for the target device from the outset and not try to shoehorn code from a PC onto a mobile device. On one project we tried to migrate some J2SE code to an iPAQ. Sadly we could not convert to J2ME as we used libraries reliant on SE. We then tried a variety of JVM (SE) implementations and even converted the iPAQ to run Linux at one point. Eventually, after a month of tinkering and the purchase of a 1 Gb memory card, the application ran (very slowly). After rewriting the code from scratch for the .net compact framework, the same application runs smoothly, even without the extra memory.

Some quite advanced interfaces have been implemented using these standard devices. Brewster et al. (2003) report using an iPAQ as part of a personal spatialized sound archive. Part of the work involved the creation of algorithms which allowed the iPAQ to recognize, and act on, certain gestures. For example, to turn up the volume of the music, the user drags their finger in clockwise circles on the screen.

One new alternative to using a general mobile platform is reported by Nam and Lee (2003). Here they use a specially constructed, but non-functional, model of the final product (think of the cellphone handsets they have on display in shops). The only functionality it has are a few buttons linked back to a desktop PC. Onto the screen of the device is projected the software component generated by the same desktop PC. The user can move the device around, as it is tracked, and the computer ensures that the screen output is mapped onto the correct part of the hardware model (see Figure 6.9). This work is still at the preliminary stage and it remains to be seen whether there are benefits from this system that cannot be found using other, less technically expensive approaches.

## Using a Specialist Platform

For some mobile applications, it’s essential to have the correct hardware and software available – problem 4 from the above list. Sometimes it’s possible to mock-up the hardware functionality from existing components. This was done to great effect in the Peephole project (Yee, 2003) which relied on tracking the position of a PDA in three-dimensional space. Rather than construct a device containing the necessary hardware, the researcher simply attached the PDA to a series of cables which were, in turn, connected to a desktop mouse (see Figure 6.10). As the user moved the PDA, the cables tugged the mice and the movements were relayed to a PC. The design appears somewhat ‘Heath-Robinson’, but allowed the researcher to gage the effectiveness of the interplay between the software and hardware.

When developing the Handspring Treo, the team built a general-purpose testing rig they called the ‘Buck’ (see Figure 6.11) (Pering, 2002). This consists of the Treo keyboard hooked up to a standard laptop. The laptop was used as an output device and to execute the software being evaluated. In order to evaluate the software properly, it was essential to see how well users could interact using the small keyboard. The design team felt that the rewards from the effort of creating custom hardware were worthwhile as they caught interaction issues that would not have appeared any other way.

![](images/fc0e197bb5daaae5c0a2302faa13236a4a379af9660bea7bfd0f99a56a63fcd0.jpg)  
FIGURE 6.9  
The participant holds a prototype device while a camera on the floor in front of the chair tacks the prototype’s position, allowing the projector (on the shelf above and behind the participant) to project the desired output onto the prototype’s screen

![](images/001fcd096814551c7ec55837c8bc9db8d0cd9927ad51246e24ef4be1834c1f2c.jpg)  
FIGURE 6.10  
The cables attached to the mouse wheels allow the PDA to be tracked in two-dimensional space

![](images/325d26b5e314ba37cb2750e73f0e07f3b6347b89d98117bc4a03caa10f2ac37c.jpg)  
FIGURE 6.11  
The Buck is used to capture key presses on the small keyboard, which are passed on to the laptop running the prototype software

One drawback of the Buck is that is it not mobile, which means that it will only provide data on how people react to the device when stationary. This means that the design team could miss out on a lot of useful data, under-utilizing the potential of the prototype. Another team which built a custom mobile prototype is reported by Brown and Weilenmann (2003). Here the team was building a location awareness device for ski instructors. One big change they noticed when deploying the prototype, which would never have been detected in the laboratory, is that the cold weather of the ski slope meant that the battery life was insufficient to make the device useful.

## Using Version 1.0

Dray & Associates highlight the problems created by the close software–hardware ties when trying to evaluate prototypes of the Tablet PC (Dray and Siegel, 2002). This represents an entirely new category of product and, while the normal tests had been conducted with earlier prototypes, there remained the problem of whether or not anyone would actually use the device. One alternative would have been to release the product and see what happened. Should reaction be unfavorable, then no matter how much the product was improved, it was unlikely to be a commercial success. Another alternative was to use the beta prototype to gather data. Using the prototype with the usual beta testers is unacceptable as they are hardly typical users. Testing the beta prototype in the field with target users will also cause problems, as the unreliability of the system will skew their attitude towards it.

In the end, the team deemed it so important to have user feedback on the design that they completed the product in full, but only released it to 47 chosen evaluators. The feedback from these users was analyzed, and the first version released to the general public was actually the second version. While this is a laudable approach, it’s probably beyond the financial means of most companies to use a fully engineered release of a product as a prototype.

## 6.6 FINISHING THE PROCESS

Having made all the effort to create a high-fidelity prototype, how does one move from prototype to product?

## 6.6.1 EVOLUTIONARY

After putting in a lot of effort, one might be tempted to ‘tidy up’ the prototype code and release that as the final product – evolve it to a higher plane. It’s a seductive route but, like all seductions, can lead to major problems later on.

Firstly, the coding requirements for prototyping and for product are vastly different. Prototyping should support fast fail; we should be making rapid changes to our code. For release-quality code, every change must be checked and fully documented – not exactly ‘fast’. Another requirement for product code is that of performance. Prototype code is optimized for alteration but not for performance. It was primarily for these reasons that Fred Brooks concluded that it was cheaper by far to throw away prototypes and rewrite the product from scratch (Brooks, 1975).

## 6.6.2 REVOLUTIONARY

The alternative to evolution then is revolution, where the prototype is discarded and the final product is developed afresh. Unsurprisingly, this is also known as ‘throwaway’ prototyping. To avoid temptation, one could force the prototyping team to work using tools that will not produce code for the final deployment platform, as advocated by Schach (2002). Of course, one need not abandon all the effort put into the prototype. It may be possible to reuse elements in the final product. Typical examples would be:

User interface layout. If the prototype was created using an interface building tool such as VisualStudio, one could simply remove the associated code but keep the interface forms intact.

Vertical prototypes. Key functional interaction, such as that developed in stage 3 of the process described in Section 6.6.3 below, could be reused in the final implementation.

Prototype as specification. The image of revolutionary prototyping is that the prototype is discarded, never to be looked at again. This is clearly not the case, as the prototype needs to inform the construction of a requirements specification for final development. Alternatively, the prototype can become the specification. This is the approach adopted by the Windows 95 team (Sullivan, 1996), who found that the creation of a separate specification document slowed down the iterative cycle. While this led to problems in communicating their ideas to external groups, the benefits were felt to be more important.

## 6.6.3 PROCESS

Over the years we’ve been creating mobile prototypes, our ideas of how to prototype have gone through a number of iterations. While we’ve always used paper, in the early days of mobile computing there were no emulators or toolkits. Instead, there were many hours of typing code directly into Psions and Newtons, worrying about memory constraints and then losing all the code because the cable to the power supply fell out. Currently, our prototypes are developed according to the following process:

1. Paper. We use paper to sketch out initial ideas primarily to support discussion within the design team. People feel free to doodle over designs and chop and change them around. When the changes become very frequent, we transfer key design elements onto Post-it notes and move them around on a whiteboard. Once everyone on the team has agreed on a design, we take digital camera shots of that design and then draw it out using a tool like Visio or PowerPoint. (Remember to use a camera with a high mega-pixel count if you’re photographing a whiteboard; those Post-it notes can be hard to read later on.) Over time, we’ve collected together a kit which we keep in a large box with a portable whiteboard for everyone in our lab to use. Although people keep pilfering from it, usually it contains the following items:

Whiteboard makers (multicolored)

As many different sizes of Post-it notes as possible (the small 1.5 2 inch are most useful)

Lego bricks

Card for making custom shapes, as well as adhesive tape (single- and double-sided), scissors and craft knife.

2. Digital screens. The neater versions of the screenshots are then placed in PowerPoint and linked together to show how the interface would support different tasks. PowerPoint doesn’t support group editing very well but, as we said earlier, it’s known by everyone on the design team, so can be changed by anyone who wishes to share an idea.

3. Vertical functionality prototype. At this point we commit our ideas to code. Because we work in computer science departments, this tends to happen in a full-strength implementation language rather than, say, Flash. The other reason to use full development systems is that often we have no idea whether the solution we’re proposing can be implemented at all. Therefore, we identify the most technically challenging aspect of the design and try to build a vertical prototype to test that concept. Assuming it is possible, we move on to the next stage.

4. Scenario prototype. Having built the functionality, we then implement enough of the user interface to allow the prototype to support the core usage scenarios. There are two reasons for this: to allow us to do some testing with trial users, and to get funding for tests with real users. Being academics, our work is supported by external funding bodies or companies. We’ve found that it’s essential to have a working proof-of-concept when making an approach for funding, especially to commercial organizations.

5. Handheld deployment. Assuming someone is interested in supporting the project, we build our final prototype on a mobile device of some kind for more user testing. The scenario prototype is usually built on a desktop machine and allows us to conduct lab-based testing. The mobile computer allows us to perform contextual and longitudinal studies. If we’ve developed stage 4 using a multi-platform toolkit, then it may be that the code on the handheld requires little or no alteration. The tricky part is the logistics of running an evaluation with multiple handsets given to multiple people in multiple locations over multiple days. We will deal with these problems directly in the next chapter, so don’t worry yet.

Usually, it’s at this stage that our development process stops. As researchers in academic departments, we’re usually required to show the validity of our ideas but not to develop them into full products. Often prototypes are used for the sole purpose of conveying an idea – architectural building prototypes serve no other purpose than to convey an idea of a building from the architect’s mind to the customer’s bank account.

For comparison purposes, however, outlined below is the prototyping process followed by Handspring, as reported in Interactions (Pering, 2002). The paper describes the prototyping process of the Treo from original concept to final product.

1. Paper. Again, Handspring’s prototyping process begins with paper prototypes. Due to the multi-disciplinary nature of their design teams, they see paper prototypes as the ‘lingua franca’ for design communication. Individual screen sketches are created and then joined using arrows (the arrows originate from buttons and show the screen that appears when the button is clicked). These screens are then used for expert evaluation.

2. Screen prototypes. This stage is very similar to our stage 2. Here, the screen sketches are linked using a PowerPoint presentation in order to track task and scenario completion.

3. Buck prototyping. To resolve complex design issues, Flash prototypes are created and then deployed for user testing in the Buck test rig. This shows up a major difference between our process and that of a commercial company. Presumably Handspring do not need to conduct technical feasibility tests as they themselves have designed the target platform and therefore know what the hardware and operating system are capable of. They can therefore skip our stage 3. Buck prototyping is thus very similar to our stage 4 and is where real user testing takes place.

4. Alpha. Here the software is developed and deployed on fully functional hardware. Although not strictly a prototype, the alpha devices are used by company staff for everyday use. From this internal user testing, information is fed back to the design team and the appropriate changes are made.

The process summary is therefore

1–2: Paper in, digital images out. For design team

2–3: Digital images in, PowerPoint out. For design team

3–4: PowerPoint in, interactive code out. For design team, users and funders.

## Ethics

If you’re developing a prototype mobile system for a longitudinal evaluation, then you have a responsibility to make it as robust as possible. I speak from personal experience on this. I once developed a phone application for my PDA. This required me to use a large PDA in an even larger GSM jacket as my cellphone for the best part of a year. The phone was cumbersome, crashed mid-conversation and lost many SMS messages. The experience was intensely frustrating and I eventually abandoned the project before subjecting any other users to the system. Mobile devices are a lot more invasive than desktop systems. If you’re going to invade someone else’s life, we suggest you try it yourself first.

## 6.7 ISSUES IN PROTOTYPING

We’ve presented you with a number of techniques for prototyping and discussed why they might be useful in the process of interface design. To help you decide when to use a given technique and to give you a better understanding of the compromises involved, the key issues are presented in Table 6.1, summarizing the article by Rettig (1994) in Communications of the ACM, and are then discussed.

## TABLE 6.1

Key issues in prototyping
<table><tr><td>Type</td><td>Advantages</td><td>Disadvantages</td></tr><tr><td>Low-fidelity</td><td>• Less time</td><td>• Little use for usability test</td></tr><tr><td></td><td>• Lower cost</td><td>• Navigation and flow limitations</td></tr><tr><td></td><td>• Evaluate multiple concepts</td><td>• Facilitator driven</td></tr><tr><td></td><td>• Useful for communication</td><td>• Poor detail in specification</td></tr><tr><td></td><td>• Address screen layout issues</td><td></td></tr><tr><td>High-fidelity</td><td>•Partial functionality</td><td>• Creation time-consuming</td></tr><tr><td></td><td>• Interactive</td><td>• Inefficient for proof-of-concept</td></tr><tr><td></td><td>• User-driven</td><td>• Blinds users to major represen-</td></tr><tr><td></td><td>• Clearly defined navigation</td><td>tational flaws</td></tr><tr><td></td><td>scheme • Use for exploration and test</td><td>Users may think prototype is &#x27;real&#x27;</td></tr></table>

## EXERCISE 6.3

## PORTABLE MP3 PLAYER – PROJECT PLAN

Returning to the YAMP project for the final time, draw up a project plan for turning the initial PowerPoint prototype into a final product. Use one of the processes above and discuss the prototypes you would need at each stage and what aspects of the final system these prototypes would allow you to explore. Finally, speculate about how you would go about testing these prototypes with real users – we shall cover this in more detail in the next chapter. ■

## 6.7.1 SOME CONSIDERATIONS

## Cues to Users

To users, well-drawn interfaces imply that the design must be approaching finality and hence they feel less likely to suggest design changes. This is crucial for architects showing building designs to clients. Figure 6.12 is taken from Schumann et al. (1996) and shows a system which generates sketches from exact CAD models. So, if you would like your users to suggest changes to a software prototype, it may be worth sketching the interface on paper before showing it to users.

![](images/0d568caaaeeac3052abe6943c456be2d263c5d16e139be49cec7e2c7a03c33eb.jpg)  
FIGURE 6.12  
The ‘sketch’ on the right is automatically generated from the volumetric model on the left

## Misleading Expectations

One of the criticisms of high-level prototyping is that it leads to unreal expectations of how close the product is to completion. Users and clients see a seemingly working demonstration and wonder why it will take so long to implement the final version. This can be very frustrating for the development team as the expectation placed on them is much higher. Less scrupulous people have, of course, used high-fidelity prototypes to their advantage in trying to convince some other party that the promised software is almost complete.

## Project Constraints

Most projects run to a particular schedule within a particular budget. Obviously, low-fidelity prototyping will be a lot cheaper, and provide more design iterations, than high-fidelity. If highfidelity prototyping is required, say for user testing, then it may be more strategic to go for a vertical prototype.

So far as time constraints are concerned, prototyping has two key drawbacks: it’s fun and you’re never finished. Often our projects have become locked into endless debates and cycles of prototypes, usually because we cannot agree on a design compromise and wish to test it on real users. We suggest that before you start prototyping, you pick a cut-off point and stick to it. Furthermore, creating prototypes is fun, whether this be drawing a low-fidelity sketch or finishing an accurate screen representation in Photoshop – within our research group, this disease is known as Photoshop-itis, where a whole day is spent altering the appearance of a few pixels not discernible to anyone but the designer.

## Communication

Low-fidelity prototyping is a great way for the designer to communicate ideas to others, but the lack of fidelity also means there is room for ambiguities to creep in. This is not always desired, but can lead to opportunistic design ideas and leaves the designer some degree of flexibility. Creating a high-fidelity prototype removes the ambiguity, but the investment involved in creating the prototype makes the designer loath to change anything.

For communicating a design idea, or flow of interaction, low-fidelity is great. For a specification which developers can follow, you need high-fidelity.

## Evaluation

We deal with evaluation extensively in the next chapter. For the purposes of this discussion, it is worth noting that it is impossible to do any user evaluation with a low-fidelity prototype. While participatory design is great for getting ideas from users, the reliance on a Wizard-of-Oz means that the evaluations cannot be objective. For usability testing and gaging user reaction to a system, high-fidelity prototypes are required. One warning with high-fidelity is that the prototype is unlikely to have the response time of the optimized final system. Make sure that these response times can be factored out of your experiments.

## 6.8 A FINAL NOTE ON DEVELOPMENT

Although written by people with a background in computer science, this is a book primarily about interaction design and not about programming. However, when the time comes to convert your prototype into a functioning device or application, there are a number of considerations unique to mobile computing which should be taken into account:

Computer performance. In case you hadn’t noticed, mobile devices tend to be smaller than desktop systems. This means smaller components inside the device, which means much fewer computing resources both in terms of processor and memory. This is exacerbated for the processor which is usually clocked more slowly to preserve battery power. Also, don’t assume that a mobile device treats all memory in the same way. If your application is larger than the memory available on, say, a PDA, don’t assume that you can insert a memory card to overcome the problem. Most PDAs treat memory cards as secondary storage (due to their slow speed) and this memory is not available for execution space.

Power. Mobile devices have limited power. You can do a lot to overcome this problem by writing your application to use the machine’s resources in an intelligent way. For example, if your target device has a hard disk, pre-load as much data as you can from it, then shut down the disk.

Different contexts. Most mobile computing devices have mechanisms for exchanging data. This can be a fairly simple type of exchange, say between a PC and an MP3 player. However, as more devices become equipped with wireless connectivity and users acquire more than one computer, the synchronization issues become very complex. We have yet to see a convincing solution to this wider problem, so cannot offer advice other than to be very careful when figuring out how data should be shared and how to guarantee its integrity.

## SUMMARY

No designer is perfect – every design will have flaws. The fastest way to get rid of those flaws is to show the design to as many target users as possible. The most effective way to show a design is to create a prototype. We have discussed different forms of prototype from low-fidelity, paper-based sketches through to complex pieces of software written for specialist hardware. We have also looked at some of the challenges that arise from prototyping mobile applications and why this is much harder than prototyping desktop applications. Finally, we looked at two processes which can be followed to translate an initial idea into a fully-fledged piece of software.

## WORKSHOP QUESTIONS

If you’re familiar with any software engineering methodologies, discuss where prototyping might take place within that methodology.

Can you think of a project where evolutionary prototyping is preferable to revolutionary prototyping?

What do you think would prevent people from developing prototypes?

Write down the first words that come into your mind when you read the word ‘prototype’

## DESIGNER TIPS

When creating initial prototypes, it’s a lot better to use a whiteboard and give everyone a pen than have a single person sketching on paper.

Programmers and engineers can be skeptical of using whiteboards (too low-tech) but persevere; once they have used them, the benefits are obvious.

PowerPoint is a great way to create a prototype interface which can provide interactivity through its hyperlink.

When building a high-fidelity prototype, be careful of scripting systems like Flash or HyperCard as the code logic can become buried. If possible, prototype in a system where the interface and functionality are easily separated.

Don’t be lured into testing prototype software only on desktop PCs; there are many reasons why the results will not hold true for the final device.

Users are often intimidated by prototype designs that have obviously been created on computer; they are less likely to suggest changes than when shown something that has been sketched.

Be warned that prototyping is fun and can consume all available time unless it is properly managed.