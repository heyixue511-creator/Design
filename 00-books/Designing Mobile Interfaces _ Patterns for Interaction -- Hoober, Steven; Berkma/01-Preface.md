# Preface

The fact that you are reading this book means you don’t need to be told how ubiquitous mobile is, how quickly the mobile market is growing and changing, and how much mobile computing is supplanting desktop computing as well as more traditional media such as film, television, radio, newspapers, and books.

Mobile is so huge and is growing so fast that astonishing growth numbers from just a few years ago pale in comparison to growth numbers today—so much so that we won’t even bother quoting any figures, as they will be outdated long before the rest of the content loses its relevance.

One thing that has not happened yet is true standards for design. Movements are now underway to design for the mobile experience first, before focusing on other forms of computing. A good reason for this is that in many markets, many of your customers look at your website on mobile devices more than on desktops.

Yet, too much design is based on older paradigms for the desktop, or even for TV or print. Within mobile, too many design discussions are very narrowly focused. They pay special attention to applications on a single platform, or only to the mobile web—and almost always at the expense of every other platform. Certainly, almost no one discusses anything but smartphones, despite the huge market share and vast usage rates of feature phones.

Fragmentation is discussed as a bad thing for marketing, and sometimes for design, but designers themselves contribute to this fragmentation too often by focusing on pixelbased layouts and the specifics of their favorite OS. This does no one any good, and is especially pointless when you consider the user. Devices generally have many more features and methods of interaction in common than their differences might imply.

Serious mobile design now, and especially in the future, will require building for every user, and providing some solution on every platform.

This book offers a set of common patterns for interaction design on all types of mobile devices. A few patterns require specific hardware or form factors, but most are absolutely universal.

Most do not concern themselves at the top level with implementation details. The correct solution is correct even at the OS level, as an application or as a website.

Of course, there are notes to discuss alternatives, methods, and limitations to assist with decision making. And many of the specific patterns are coupled with alternatives or variations that allow similarly useful solutions to be achieved on any type of device.

## Who This Book Is For

As with any good form of interactive design, we have kept a specific scope in mind from the moment we started writing this book. If this book was intended to be all things to all people, it would be much larger or we’d simply never have finished it. Our focus here has been on design. By this we mean information architecture; information, interaction, interface, and visual design; and copywriting.

If your job title, job description, or deliverables have names like those just mentioned, and you work in mobile, you need this book. Whether you are working on apps or websites for mobile (or any of many other things), this book addresses the common underlying principles in order to help you make better decisions and understand how to create better designs.

If you are moving from another field, such as desktop web design, or are switching from one narrowly focused mobile area to another, this book encompasses general patterns that can help you understand how to move from one type of device or one type of interaction to another.

If you work in a related job, this book still has something for you. Human factors engineers and HCI experts will find numerous discussions of why these solutions have become patterns, and references to cognitive psychology- and physiology-based reasons these are true.

Development is not addressed as such, but the book is organized so that you can use it to find specific solutions to any form of mobile interaction. If you don’t have a dedicated design team, you can use the patterns to find and focus on solutions, confirm they are technically possible, and avoid common implementation pitfalls.

Hardware designers, or anyone who can influence hardware design, will find specific guidelines to best practices in interactive, such as key labels and the use of sensors. Though these are included primarily for use by interaction designers—to understand how the hardware influences their on-screen behaviors—they are also specific enough to be used for design of the interactive portions of the hardware itself.

## What We Mean by “Mobile”

Over the years, the reaction to my job title, “mobile interaction designer,” has migrated from blank stares to significant interest in this suddenly mainstream technology. Still, only about half the time do people have any idea what that title means. And if they do, they almost always assume my job is to design mobile phones or apps for them.

![](images/d1b7ba3fdc4d6c448f754d3bf4065d482fcb7f9c148ead79f905184669a0c15d.jpg)  
Figure P-1. Traditional media, and desktop computing, require the user to make an effort to go to where the display is; even a laptop requires creating an ad hoc workplace. When the mobile device is always with you, everywhere is a place to do work, be entertained, or consume information.

Occasionally, someone asks if we also design games for the Nintendo DS, or make maps for GPS navigation, or do work for some other sort of device. Has the definition of mobile changed? This is a list of the types of things we looked at to find and validate these patterns:

• Mobile smartphones

• Mobile feature phones

• Mobile network access points (aircards)

• Mobile Internet Devices (MIDs)

• Tablets

• eReaders

• Media players

• Image viewers and digital picture frames

• Portable game systems

• Remote controls

• Handheld navigation devices (see Figure P-5)

• Portable scanners

• Cameras and other capture devices

• Printers, scanners, copiers, and mopiers (multifunction devices or MFDs)

• Kiosks

• Wearable computers

• Telematics, and vehicle-mounted devices

• Industrial automation

• Portable surveying, measuring, and metering equipment

The preceding list is not exhaustive. And although the items in the list share many characteristics, many are not particularly mobile. Kiosks are, by definition, bolted to the ground, for example. And no one much thinks of a camera as being similar to a phone.

So our first answer is that mobile is not a useful word, and that this book addresses a lot of these devices. Their design can be informed by the mobile patterns in this book and elsewhere. The ubiquity of mobile devices also may mean that employing these as universal patterns is a good thing, as users may require less training when using interfaces to which they are accustomed. If you design cameras or printers, you should be paying attention to the state of the art in mobile.

![](images/4e029b90f910f640572e449a582ff5a491f1104a0116dbed44811f5698203a59.jpg)  
Figure P-2. Always-available devices encourage use at every idle moment, with an increasingly broad definition of idle time. Law, custom, or commonsense notwithstanding, devices will be used in every conceivable environment.

We didn’t come up with this answer out of the blue or just trust our instincts. Instead, years of work, discussion, writing, and arguing led to some principles of “what is mobile.”

We like to think of the evolution of mobile telephony as having occurred in four eras:

• Voice

• Paging and text

• Pervasive network connectivity

• General computing devices

Yes, this leaves out a lot of interesting devices that are on the longer list shown earlier. The Game Boy and GPS receivers predate by several years what most of us would call mobile phones. But mobile telephony is what changed the world and ushered in all this, so it’s a good anchor point.

If you consider a current mobile phone as being a “fourth-era” device, you find that it has the following characteristics:

## Small

It’s small enough to carry with you all the time, preferably in a pocket (see Figure P-1).

## Portable

It’s battery-powered and otherwise independent of the world, so it doesn’t have to be plugged in or attended to regularly (see Figure P-2).

## Connected

It’s wirelessly connected, not attached to the wall or connected only when the user makes special effort. Whenever possible, it is connected in multiple ways, to both voice and data networks (see Figure P-3).

## Interactive

It’s inherently interactive. Unlike a watch, or even most MP3 players, which are limited to display, playback, and a small subset of interactions, a mobile phone allows more undirected actions to be taken, such as text entry and keyword search.

## Contextually aware

It (or services it is attached to) uses its ability to understand the network to which it is attached, and its other sensors, to help the user get things done, and preemptively gather information (see Figure P-4).

With this many facets, it’s easy to disregard any one of them and still feel the device meets your needs. By strapping an iPad to a wall and calling it a kiosk, all you’ve done is simply remove its “portable” feature, so it’s still a “mobile” device.

Consider the Wii or the Xbox Kinect instead. Though the display used on these devices is not at all portable, at its core it is aware of the user’s position, it changes with the type of input being used, and the entire interface has been designed to support interaction via a game controller, or via the user simply waving his arms at the screen. These meet the interactive criteria to be a “mobile” device.

![](images/8cc65e2c08e41c8277587bc04b878cacb09f77ccf779faadeb786dd3505fdb4e.jpg)  
Figure P-3. This wearable scanner, attached to a Tablet PC (used for inventory control), is representative of trends in workplace computing: contextually useful so that the operator has it with her constantly, and connected so that the enterprise can use the intelligence immediately.

Now take a Windows Tablet PC. It has pen and touch input, can be quite small and portable, is networked, and has sensors. But we argue that it is not mobile. It’s not really connected, because it connects like a desktop, so you have to open dialog boxes and press buttons. It isn’t usefully interactive, because you cannot use it on the go, but rather have to stop to use it. It’s not contextually aware, because the GPS, or camera, or accelerometers don’t do much of anything by themselves.

![](images/95213508df8d9c919c1d2c539990632d58e630a28b1d9b5ef03a98658636fb94.jpg)  
Figure P-4. A few years ago, I used this combination of a GPS and Windows Mobile device to record and track my location (in a snowstorm, no less). Today, the results of sensors in mobile devices can be seamless, automatic, and so intelligent as to risk violating privacy.

## What Type of Patterns We Will Cover

So, although this book does still focus on the mobile phone and, in particular, the smartphone, similar interactions from kiosks to game stations to telematics are also considered. In some cases, we’ll even refer to these devices directly in the patterns.

The patterns are guidelines for implementing interaction design on these devices. So they talk about page-level components such as scroll bars, display components such as pop ups, widgets such as buttons, and input methods such as keyboards.

But they also talk about things such as the labels and lights for hardware keyboards. These are covered because you can influence them. You can fail to implement the keyboard correctly, and cause keyboard entry to fail. You can change scroll bar behavior, if there’s a special case for your application. Increasingly, as HTML5 technologies roll out, mobile websites can take advantage of interesting interactive features.

Also, you might be working on a device operating system—likely the GUI layer on top of an existing OS. There are many, many devices, and new classes are still emerging. Overlays have migrated down to the point that end users may change the basic behavior of their handsets. You may have to work in this space sooner than you think.

If not, you still need to understand why certain OS-level behaviors are standard, or should not be, so that you can make informed decisions about your design.

## What Is a Pattern?

There has always been a concept of reusing and reapplying known best cases in graphic design. There has always been a culture of sharing, borrowing, and building on the work of others. As graphic design (and designers) moved into and influenced interactive design, this philosophy of repurposing the best ideas, coupled with the principles of objectoriented development—which also develops by modules and reuses components—led naturally to the evolution of design patterns.

Patterns as applied to interactive design are much like patterns in software development. This has led to a conflict between design managers who push for repeatability and the use of templates, stencils, and patterns, and designers who want to be free to explore solutions. However, this is an artificial mismatch, arising from a misunderstanding of how patterns should be used.

The concept of a pattern was actually developed by the architect Christopher Alexander in the late 1970s. He argues that patterns are components of a language, and can be used to conduct a dialogue about building and organizing, and the nature of human existence in space. Although architecture and engineering are only so analogous to the fields of software and interactive design, the concepts did translate well.

Object-oriented software development applied the concept directly from Alexander’s early work starting in the late 1980s. This was applied as a straightforward problem/ solution statement; select the pattern whose problem statement most closely matches the implementation technology problem. There is room to design the specific solution, and to modify it to meet the needs of the specific system, but they are still very plug-and-play.

While Alexander’s arguments may be hard to follow—especially when he talks of concepts such as the “life” in spaces, or underlying “morphogenesis”—the core of his process is at the core of all design processes. Patterns are simply well-defined, well-researched best practices, but fundamental principles of design must always be followed, the user must always be kept in mind, and the purpose of the design must always be considered.

In mobile interactive design, we might summarize these core principles as user-centered design, context, and other principles. A set of more specific principles are listed at the end of this introductory section. You must always consider these principles—or others you may be more comfortable with—to ensure that the proper pattern for the situation is determined, and the correct application is created from the user’s needs, his context, and by integrating the solution into the whole system.

## Where Did These Patterns Come From?

Another way to think about patterns is that they are simply all the heuristics available, shoved together and placed into a form where you can simply look at the end result. In many ways, that is how this book was created. For years, we have been collecting implementations, trying to tease out behaviors and patterns, and gathering them up. In other formats, and at conferences, we’ve been distributing these to the mobile design community.

And when we went to write a book on them, we had a pretty good handle on the categories of information that had to be created, and the patterns that would occupy each one. And then almost immediately we ran into trouble. At this level of detail, gut checks and common practice and simply knowing how it works was not good enough. So we did research. A lot of it was simply observing devices.

![](images/e36e7a7f05ccdb5ddea354b9af89f2b5c1f9a62d8ba10c6e69f50b6369d1fd02.jpg)

Figure P-5. A selection of the devices surveyed to discover, confirm, and understand the patterns that ended up in this book. This is just a small sampling. Add another 30 or more handsets, 10 tablets, 10 eReaders, numerous game controllers and portable game units, a handful of GPS navigation devices, and many others to the list. These devices are not just for show; many work, and are readily available to refer to during design (and when we were writing this book). Many have Velcro on the back, and are stuck to the wall of the design studio, to be in our faces every day when we come to work.

Many are those we gathered over time, but we also acquired new ones, and asked people we know, work with, met at parties, or ran into at conferences to let us see their devices. We hit up stores when new devices came out. We noticed, and took photos of, the way PIN pads and kiosks work. We skulked around electronics recyclers to get old devices on the cheap and begged friends to let us have their dusty old phones. Figure P-5 shows a sample of these devices.

And then we compared the implementations. In many cases, the all-new, super-cool best practice was just a very minor change (or no change at all) to something on a 10-yearold PDA, or on many feature phones. In all too many cases, the newest technologies had lost common and best practices from the well-established methods of scroll-and-select devices.

We engaged with the users, too, in any environment. Whether at an airport, in a coffee shop, on a busy street, in the office, or in our family room, we recorded behavior. We observed these individual, social, and cultural interactions in varying contexts, paying close attention to how people use these devices in their everyday lives. We also interviewed them to gain rich, insightful, qualitative data about their needs, motivations, and attitudes about using mobile devices. All of this ethnography and contextual inquiry—whether formal research or ad hoc discovery—further validate the design recommendations presented throughout this book.

As a result of this research, we hope we have provided balanced and interlocking coverage of emerging technologies, the common practice of the most buzz-worthy current devices, and the best practice of the well-established “low-end” devices.

And whenever possible, we performed literature surveys to determine why those activities work the way they do, and to explain them—not just stating that they represent the right way, but why they do so. This sort of work helped us, and will help you, to understand the relationships among the different implementations of a pattern. Only understanding why lets us explore the edges without wasteful trial and error. Understanding human cognition, perception, and physiology lets you predict what will work and what will not before building it.

## Art, Graphic Design, and Experience

We needed these patterns and heuristics before writing this book because we design mobile applications, websites, services, and OSes. Besides being paid to gather this information, we also have gained access to a lot of other information, such as user research and user behaviors with products in production. In addition, we have been able to perform our own research, and we have gotten firsthand experience with many of these device classes.

We also have other experience, in graphic design, art, human factors, industrial design, engineering, and education. And when working on real projects, to launch with real products, we also have to work with many other individuals, with dozens of other job functions. So these patterns are also grounded in the knowledge base of those skills, often backed by well-documented scientific research again.

## Common Practice Versus Best Practice

A key overriding principle behind much of this work is the differentiation between common practice and best practice. Although not always explicitly stated, this is what drove activities such as the inclusion of antipatterns (or “worst practices”) for each pattern. There are many, many design patterns that do not work, or do not work as well as alternatives.

This is a key reason so much effort went into researching the patterns. We didn’t include something just because it was heavily used, or is a much-lauded feature of a new and well-covered device; if it was common or well known, but bad, we included it, but with warnings.

This also means, again, that we had some serious discussions about what qualified as a pattern. In general, a pattern must be a best practice, and common enough to be recognized or encountered.

Therefore, there may be some odd cases where an antipattern has general solutions listed, but no specific solutions in the body of the pattern. Though the problem is known, no single solution has emerged.

A best practice that is not implemented anywhere (or only very rarely) is not described, as it does not rise to the level of a pattern. Only real-world items are patterns by our thinking, not clever concepts, demonstrations, or videos of how the future might work. These are, however, sometimes mentioned as future technologies or options to look forward to.

## Reading the Patterns

Almost before we even started to figure out which patterns we wanted, we started talking about how they should be internally arranged. There’s a surprising amount of variation here, but primarily we decided that a single, totally consistent method was most important. That way, you have a fighting chance of taking two competing patterns and comparing them.

The most important section ended up being the one on variations. Something like 15 to 20 patterns disappeared over the course of writing this book, and ended up being better described as variations of existing patterns. And a few patterns we split into two or more patterns instead: after we started writing, the variations for some of the patterns were a bit too severe, so we split those patterns into two or more patterns, instead of just one with variations.

## Names

Names are as short as practical while still being clear, and whenever possible they do not conflict with an existing concept. Some ended up being a bit of a mouthful as a result, but we did our best. In far more cases than expected, there was no name at all for a well-used design element, and we had to make something up.

We always used title case for the actual pattern names. If you run across a name that is capitalized and blue for no apparent reason while reading a sentence (e.g., “Input Method Indicator”), that means it is in reference to another pattern in the book, which you can refer to in order to make a comparison. Whenever possible, this is also made clear in the text, such as “see the Input Method Indicator pattern for an alternative method.”

## Problem

Some people get nervous when the word problem is used in a project or design sense. But problems foster solutions, so try not to worry about any history or bad implications that term may have to your organization.

The “Problem” section of each pattern is just a summary of why you’d want to use the pattern. Ideally, patterns are grouped with similar problems, and you can get to the right section and then compare the problem statements as a way to help identify which one you really have.

## Solution

The “Solution” section provides a definition of what the pattern involves, which other patterns are key overlaps or provide key components, and (when relevant) the important technologies required to make it operate.

This is one of the sections that can vary widely, from a very brief introduction to comprising half of the pattern. If it is difficult to explain, difficult to implement, or often poorly implemented, this will get longer. Simple patterns are shorter.

## Variations

Our patterns aren’t stencils, so they aren’t restrictive. All of these have variations that you can choose and that are defined so that you can choose the correct one based on the content to be delivered and the context in which you will use the pattern.

The length of this section varies widely depending on the number of and differences among the variations. Some have multifaceted variations, so more than one list may be encountered. In some cases, the variations are so pronounced that much of the interaction and presentation is covered in this section as well.

## Interaction Details

This section explains how the user interacts with the item being described—including pressing buttons (or swiping the screen) and what the screen displays that the user can click on or type inside.

## Presentation Details

This section explains things on the screen that you cannot click on, or details about the manner in which displayable items are presented which do not directly influence the interaction. A shadow on an interactive item might help with visibility, so this would matter but would not directly influence interaction, for example.

The difference between interaction and presentation can be a bit difficult to fathom sometimes, but breaking them up helps a lot when trying to seek the core truths of a function and separating what must be present and what is optional or additional.

## Antipatterns

Specifics of the implementation you should watch out for are always listed. These cover both antivariations (methods that should never be used) and more minor pitfalls or edge case uses of proper variations to watch out for. These are not speculative, but are known to be bad because they violate heuristics, and often are verified by research.

These do not encompass all the possible antipatterns, but the key and most likely problems. Rest assured that there are many other ways to break a good pattern. Use design principles and heuristics, and carefully read the rest of the pattern to prevent poor implementations.

If you cannot avoid an antipattern for technical reasons, you should not use the pattern and instead you should find a technically feasible replacement. This is a common occurrence, and is a key reason the antipatterns are explicitly listed.

## Examples and Illustrations

We deliberately chose not to include a lot of screenshots. In fact, we include hardly any. We did not arrive at this decision lightly; we gathered and extensively annotated screenshots for the first several patterns. But we decided to take this route for the purpose of practicality. It’s very hard to find enough adequate examples, and often the best one is on a device that is difficult or impossible to capture. Some of the clearest examples are on feature phones, old PDAs, GPSes, and the like.

This leads to the key problem we encountered with screenshots: clarity. Patterns are the pure essence of an implementation. And almost every implementation layers its own style on top—or buries a pattern alongside others. Screenshots required explanation, and very often caveats about what not to do.

To solve the problems with screenshots, we used illustrations almost exclusively throughout the book. These are all of the same basic style, but vary widely in the detail level used, sometimes in adjacent drawings in the same pattern.

In each case, only the required amount of detail is used. Sometimes that detail is just boxes and lines, and the words and images are implied. Sometimes words and so on have to be in there to communicate the point. Sometimes actual raster icons or websites, drop shadows, and other effects are used.

As a general rule, large blank areas on a page do not mean there’s nothing there. It just means we’re not discussing that component, so we removed placeholder information for clarity. The Annunciator Row is almost always assumed, so space is provided, but is not displayed—again, for clarity and to reduce clutter.

Color, especially when clearly not naturalistic, generally has a meaning:

• Yellow usually refers to the displayed, interactive elements.

• Blue is for images, and graphical displays such as information visualizations. A different color is used so that it is clear that it’s not just a box.

• Grays represent nonselectable items, like the parent when a child has popped up over it.

• Orange is used when the item is in focus, as when scrolling in a list, or to indicate the primary button that is going to be selected for a process.

This is not always adhered to, especially in the higher-fidelity drawings, but it is a good guideline.

That being said, there are a few photos and screenshots in the book. We used these when creating an illustration of sufficiently high fidelity would have been pointless, for clarity when describing certain hardware details, and as example implementations when introducing new categories of patterns.

## Successfully Designing with Patterns and Heuristics

As we just discussed, patterns are often misapplied and used as rote answers to problems. Or they are specifically rejected because they are perceived as having to work in a certain way, and so stifle creativity.

While neither of these statements is true, the next problem with best practices is more insidious.

## Avoiding the Heuristic Solution

Good, well-intentioned practitioners of interactive design, like you, apply well-established principles, procedures, and processes in an attempt to seek the right solution.

We all perform heuristic evaluations, apply patterns, copy best practices (or at least “common practices”), and—whenever possible—perform user research to confirm the design is good. Without inspiration or luck, all too often the end design is what could be called the “heuristic solution”—the rote, safe answer is the default result.

And very often this is fine, strictly speaking. There are no serious errors, and satisfaction is within norms. But have you ever found a design to be boring? Or that it only solves that specific issue, so you end up redesigning it for the next version?

A lot of demands are (and should be) placed on interactive designers to meet the brand, to find and meet the users’ greater goals, and to differentiate from an ocean of interactive products competing for attention. Mobile especially is very competitive and has strong drivers for differentiation of your products in the market.

To develop interfaces that delight like this—or must entice users to revisit or share—requires using patterns and best practices as just one input into the design process. The product must be understood holistically, and design options must be developed tangentially in order to discover the multiple ways to approach the solution.

While there is no single method or movement to achieve better results, here are a few concepts that lead in that direction and are worth considering for your design process:

## Conduct validation exercises

Before you even start, perform user interviews, ask the business what they want, and gather any other information about current and expected usage that you can gather. Develop measurable objectives, stick to them during design, and be sure to measure them after the product launches. Without feedback, you cannot learn.

## Use studio methods

The best ideas come from individuals or small teams working independently. To get the greatest number of good, unique ideas, task those individuals or small teams to develop quick, independent designs and regularly share and regroup, iterating to a final solution.

## Realize that every idea is unworthy

When working with design concepts, from competitors to the design teams just mentioned, remember to approach the design from a modular point of view, and evaluate the suitability of each element to the overall goals and process. Do not just accept (or reject) whole designs.

## Embrace your constraints

Whether in conceptual exercises, during workshops, or as individual designers, only work within the domain, set preconditions, and remind everyone that the goals and objectives define the desired end state.

## Collaborate

Design teams will, ideally, have a variety of individual skill sets, or at least multiple individuals that each has her own background and opinions. Use the individual skills of the team members to find solutions and explore concepts.

## Seek outside opinions

Not everyone has all knowledge of the arbitrarily complex systems we work on all too much, so cross-functional collaboration can have great value in confirming concepts, getting input on the viability of concepts, and discovering tangential solutions already considered or in progress somewhere else.

## Using User-Centric Execution Principles

The other key problem with interactive design is actually getting the product built. To us, this is the new, more critical “gulf of execution” and the most important problem across the practices of user experience and interactive design.

What are needed are principles of what we can call user-centric execution. They are not yet a process, or a series of fixed procedures. It is possible that they may never be. But like the principles, heuristics, and patterns of design, the idea should be followed and there are best practices. First, let’s discuss the principles.

To encourage successful execution or implementation, UX teams should:

## Never walk away

Always stick with the project through development, at least making yourself available for questions, rework, changes, and testing. Ideally, become integrated into the team, and attend daily meetings, test planning, and so on. Plan to do this from the start so that your budget accounts for it.

## Ensure that goals are for everyone

The business and user goals you should have developed at the beginning of the project must be translated into actual, measurable metrics. Make sure the whole organization has these goals as their top drivers, instead of cost savings, efficiency of developers, or other internal measures. While “we’re building for the end user” may not resonate, remind the team that they work for the larger company, not just their department. You may also have to push to include the analytical tools to make sure they get built and are not forgotten.

## Use object-oriented principles when discussing and delivering

The efficiencies and enforcement of consistency that componentized, object-oriented practice emphasizes in design are just as valuable to software developers and the development process. Sometimes this is just called “modular reuse” or something similar, as “object-oriented” is a larger set of principles. But the core concept is the same. Instead of designing every detail for every state, and building by state or building hundreds of items to bolt together, a few dozen modules are built and reused over and over in common templates.

## Design with polymorphism

This is a subset of the preceding item in the list, but it is harder for some organizations and designers to grasp, so we’ve broken it out. If there are several variations of an on-screen module you design, make sure you express them as variations of one another so that they are clear. Of course, if there is only one variant (omnimorphism), it should be explicitly stated as well. Always keep efficiency and reuse in mind.

You should not find any of these processes to be burdensome. They should instead make for a much more efficient method in which to develop, and ensure that everyone on the team works hand in hand, at every level.

It is also important to keep this in mind even if you are a developer. Make sure you do not fall into developer traps, and keep yourself true to the design principles.

Patterns are a reference, and a starting point for design. Use them carefully to avoid being overly constrained, and use the principles of modular design to efficiently communicate and build the end product.

## Principles of Mobile Design

Principles exist at a higher level than any pattern. They can be considered patterns for the patterns, if you will. Each pattern, and each detail of interactive or presentational design, should adhere to each of these principles at all times.

Each section and chapter in the book will begin with a discussion of the core principles for their sections, as well as other helpful guidelines that apply to those patterns.

Each of these principles could be discussed in great detail, and in fact we could have organized the book differently so that each of them was a chapter, with patterns associated to it. In the interest of clarity, the discussion of each of these is limited. If you are interested in further details on the rationale, these are generally discussed in greater detail within the patterns they apply to, as well as the chapter introductions.

## Respect User-Entered Data

Input is hard. Users slip. You have a new phone, or are borrowing someone else’s, and someone jogs your arm: suddenly minutes of typing is gone. Do whatever it takes to pre serve user data—from saving as the user types so that auto-complete can bring lost input back, to not clearing forms on error, to planning for a loss of connection. Consider contexts and plan for crises and real-world behaviors, not bench tops and labs.

## Realize That Mobiles Are Personal

Although security is important, there is no longer the need to assume that maybe the website is being viewed on a library computer. Mobiles can be presumed to be “one device for one person,” and no one wants to have to regularly tell his device his name, location, or favorite music. Only implement passwords and clear personal information when required by law or regulation, and take other types of reasonable and transparent precautions to prevent misuse of information.

## Ensure That Lives Take Precedence

Mobiles are contextual, meaning they are used alongside people’s actual lives. Desktops (and some other devices) can suck people in, so you can go ahead and issue alerts that blink in the corner of the screen and they will be noticed. Mobiles are glanced at, used in gaps between conversation and driving and watching TV. They are even used to enhance these other experiences. So make sure they don’t interrupt unless they have to. And if they have to, make sure they interrupt in a way in which the interruption will be noticed. A blinking LED, for example, is easily missed when a device is glanced at for a fraction of a second.

## Realize That Mobiles Must Work in All Contexts

Make the device behave appropriately, or allow users to make the device behave appropriately, to make it work where they are. Most devices are too bright at night, making it hard to read that last email before bedtime, or to tell what time it is when the alarm goes

off first thing in the morning. If the phone doesn’t have a good way to change brightness, your app can override it or your website can just have a dark/light switch. Think about the context in which the device will be used.

## Use Your Sensors and Use Your Smarts

Whenever possible, perform actions for the user based on sensors and user data. Why should you have to silence your phone for a meeting, when the phone knows where you physically are and knows from your calendar that you have a meeting in that room right now? Mobiles can be better than computers, because of their personal nature and their sensors. Use them.

## Realize That User Tasks Usually Take Precedence

If the user initiates a task, and especially if the user is in the middle of a task, do not interrupt the user so that the task is ruined. When the user is typing an SMS, feel free to beep, but do not change the focus so that the user is suddenly typing in another field. And never cancel the operation to take the user to another page, losing her information.

## Ensure Consistency

Whatever the rest of the application does, do that. And the application standards should follow the edict: “whatever the OS does, do that.” Even if the OS does something dumb, it’s probably what the user expects, so changing the paradigm generally results in more problems than solutions.

## Respect Information

Although presentation and visualization can be used to clarify information, or view it in different ways, do not modify the fundamental truth for saving space, or because you do not understand the value of it. More information than you might expect rises to life/ health/safety levels with the ubiquity of mobiles. Weather, for example, must be presented perfectly accurately. Know the difference between precision and accuracy, and understand implications of meter types, relative values, off-scale errors, and more.

Naturally, these will change over time. Just in the past five years we have changed or expanded these several times. Be aware of the reasons these principles exist, and keep abreast of the industry so that you are aware of changes.

Although we feel these principles are universal today, you are very free to disagree. Many others do, and they have their own principles, or variations on the understanding of what these mean. Just be sure you develop a set of design principles or objectives for your work or your project, and then stick to them.

## Safari® Books Online

![](images/701dca5cf68947cfa3f82a5252e74a306586f47fa5f78a360398e1fa6d4359fb.jpg)

Safari Books Online is an on-demand digital library that lets you easily search more than 7,500 technology and creative reference books and videos to find the answers you need quickly.

With a subscription, you can read any page and watch any video from our library online. Read books on your cell phone and mobile devices. Access new titles before they are available for print, and get exclusive access to manuscripts in development and post feedback for the authors. Copy and paste code samples, organize your favorites, download chapters, bookmark key sections, create notes, print out pages, and benefit from tons of other time-saving features.

O’Reilly Media has uploaded this book to the Safari Books Online service. To have full digital access to this book and others on similar topics from O’Reilly and other publishers, sign up for free at http://my.safaribooksonline.com.

## How to Contact Us

Please address comments and questions concerning this book to the publisher:

O’Reilly Media, Inc.

1005 Gravenstein Highway North

Sebastopol, CA 95472

(800) 998-9938 (in the United States or Canada)

(707) 829-0515 (international or local)

(707) 829-0104 (fax)

We have a web page for this book, where we list errata, examples, and any additional information. You can access this page at:

http://shop.oreilly.com/product/0636920013716.do

To comment or ask technical questions about this book, send email to:

bookquestions@oreilly.com

For more information about our books, courses, conferences, and news, see our website at http://www.oreilly.com.

Find us on Facebook: http://facebook.com/oreilly

Follow us on Twitter: http://twitter.com/oreillymedia

Watch us on YouTube: http://www.youtube.com/oreillymedia

If you have any thoughts or questions you’d like to share with the authors, feel free to contact us. We enjoy communicating with our audience.

Steven Hoober Kansas City, Missouri steven@4ourth.com @shoobe01

Eric Berkman   
Sydney, New South Wales, Australia   
eric@4ourth.com   
@ericberkman

For the latest lists of reference materials, visit:

www.4ourth.com/wiki

## Acknowledgments

Though we have both written extensively before, and even self-published a book once, this was much more involved than we’d have guessed going in. We couldn’t have done it—and certainly not this well—without the assistance of a number of others.

Mary Treseler, our editor, championed this whole project and showed great faith in both of us, especially during somewhat challenging times, as the scope of the book began to grow and as we stretched the bounds of what an O’Reilly technical book normally is.

The various members of the production team at O’Reilly have also been extremely helpful in working through our unique demands and sometimes-mediocre writing. Without them, this would be a much less readable and sensible book.

We’d also like to acknowledge the efforts of the technical editors. Steven also edits other books, and is very aware of how much work this can be. Josh Clark, Dan Saffer, Jennifer Tidwell, Bill Scott, and Christian Crumlish all gave us excellent feedback, if sometimes painful to hear and difficult to implement.

Similarly, there were innumerable small conversations on Twitter, in blogs, via email, on LinkedIn or Facebook, and face-to-face at work or industry events. Dozens of people gave us encouragement or useful feedback, or asked for a feature to be addressed that we might have forgotten otherwise.

Matthew Irish helped us with many technical aspects, such as setting up the wiki and taking some of the many screenshots we needed at the last minute.

Our device collection has been invaluable for research and perspective, so we want to thank everyone who donated an old device to us. We’d especially like to call out Ed Madigan, who donated his desk drawer collection on leaving Sprint. Though they do not know they helped, the Surplus Exchange in Kansas City—which has the best electronics recycling program, perhaps anywhere—has minimal interest in phones and PDAs, so we were able to get some neat old gear for terribly low prices.

We’d like to thank Allan Swayze, who provided better soldering and wiring gear, and a power supply to help Steven get many of these old devices running. He also exposed us to all sorts of interesting industrial automation devices, adding a lot of hidden technology to our knowledge base.

Thanks also go to Paige Miller, who has been growing up just down the street from Steven’s house, and, along with her friends (especially Audrey and Lily), let me observe their phones, interview them, and perform free user tests. They have provided great insights into the youth market.

Thanks to Jesse Schifano and Mike LeDoux, for letting me put their exploration of an iPad kiosk in here, and to the rest of the Ai design team for only occasionally making Steven come out to dinner instead of writing or editing all night long.

And of course, thanks to our friends and families for putting up with almost a year of spending every bit of spare time writing, editing, photographing, drawing, and editing more in a seemingly endless cycle.

The page is the area that you will spend your time designing for any application or website. A part of it is visible in the viewport of the mobile screen during its current state. There are states and modes and versions to be considered, as well as addressing what is fixed to the page, what can float, and what is locked to the viewport.

Based on cultural norms of reading conventions and how people process information, you have to design elements for the page, and place items on it in ways your users will understand. You also want to create information that is easy to access and easy to locate. Your users are not stationary, nor are they focused entirely on the screen. They’re everywhere, and they want information quickly and to be able to manipulate it easily.

Unlike later parts of this book, which cover broader topics, the Page patterns that we will discuss here are contained in only a single chapter:

• Chapter 1, “Composition”

## Helpful Knowledge for This Section

Before you dive into the patterns, we will provide you with some extra knowledge in the section introductions. This extra knowledge is in multidisciplinary areas of human factors, engineering, psychology, art, or whatever else we feel is relevant.

For this particular section, we will provide background knowledge for you in the following areas:

• Digital display page layout guidelines

• Page layout guidelines for mobile users

## Digital Display Page Layout Principles

The composition of a page has to do with the assembly of components, concepts, content, and other elements to build up the final design. As we already know, consistency is important, so these elements are not placed arbitrarily on the page, or even just as the one page dictates, but on rules across the system, or even the whole OS.

![](images/3171347c935386c73919f12e5f20da1a9edc1e5171e7036ba581a34aaa3c71de.jpg)  
Figure I-1. Developing a common grid and hierarchy of information for the entire application or site is key to a consistently usable and consistently branded experience. After a grid such as this is created and wrapper elements are defined, a series of templates can be created, and then individual pages and states.

At the highest level is the grid. This is a regularized series of guides, defining the spacing and alignment of the main elements on all the pages in the system, as shown in Figure I-1. Some rules are inviolable, such as margins, and some are specifically designed to offer options for special page layouts, or unexpected future changes.

From these are developed a series of templates, from which each page in the application, site, or other process will be designed and built. This encourages a consistent user and brand experience that supports content organization and layout, advertising requirements, navigation, and message display characteristics such as legibility and readability.

Patterns within Chapter 1, such as Fixed Menu, Revealable Menu, Notifications, and Titles, are repeated at the same place on each and every page, and so reside in each template. A subsidiary concept is that of the wrapper, which defines these common components— and others, such as scroll bars—so that they are consistently designed and built for each and every page template.

Mobile users have specific tasks and goals. They require that the information be quickly located and effectively organized. Therefore, the page layouts need to reflect the mental models and schemas understood by users. If you ignore these, you will end up with situations such as that shown in Figure I-2. Your users can become frustrated and dissatisfied with their experience, create miscues and errors, and maybe even give up!

Furthermore, using page layouts wisely allows you to organize and place content effectively on valuable screen real estate, where every pixel is important.

## Page Layout Guidelines for Mobile Users

![](images/c5232a9ff296602929dccbd5d2b5145276d14d3aa6d6108676860f4f6113b1d3.jpg)  
Figure I-2. If you don’t follow the principles of a grid and templates, you will end up applying components in overly variable ways. Here, the title is far below the tab, separated by the banner ad. On the search page, there is a search dialog above the title, pushing it farther down. On the home page, the addition of the “more” icon makes it unclear whether “Top Stories” is the page title, section title, or something else. And in Settings, the new style of banner draws the eye, so it seems, for a moment, that this is the title.

Here are some page layout guidelines to follow:

• Mobile screen real estate is valuable. Avoid the use of banners, bars, images, and graphics that take up space without any specific use. This use may be secondary, such as communicating the hierarchy or structure, but the designer should always be able to describe the reason.

• Lay out elements within a design hierarchy. There are optional versions, and some interactive types insist that time is another component, but for simplicity, the hierarchy is Position→Size→Shape→Contrast→Color→Form. The most important items are larger, higher, brighter, and so on.

• Consider the Gestalt laws of Closure, Continuity, Figure and Ground, Proximity, Relative Size, Similarity, and Symmetry. These are discussed further in Part II, “Components.”

• Use consistent and simple navigation elements. People have limits to the amount of information they can store in their short-term memory. Therefore, they automatically filter information that is important and stands out. Information elements that are excessively displayed and irrelevant will be ignored and overlooked.

• Wayfinding is really rooted in real-world navigation, like getting around town or finding the right room in a building. Kevin Lynch, an environmental psychologist, established five wayfinding elements that people use to identify their position: Paths, Edges, Nodes, Landmarks, and Districts. These same environmental elements are also referenced when navigating digital content on websites or mobile devices. Page numbers, titles, headers and footers, tabs, links, and more provide a lot of help that we’ve inherited almost as a whole for interactive design.

• Consider how users will view your page when plotting content. Generally, users will look for high-priority information in the upper left of the content area (Nielsen 2010).

• Multicolumn text is not used to meet some design style, but to restrict line length. And line lengths are not based on fixed sizes, or even percentages of page width, but on character count. Long lines are harder to read. Around 60 to 65 characters (on average) is the maximum length you want to use. A definition for what is too short depends on how many long words you have.

• Titles describe pages, elements within a page, and content sections. Use them consistently and appropriately.

• Default text alignment is left. For right-to-left UI languages, default text alignment is right.

• Try to use bulleted information instead of a table.

• The term false bottom, or false top, is specific to interactive design and refers to users thinking they are at the end of the content and not continuing to scroll. If text flows from one column to the next or one page to the next, it must be designed so that the relationship between the columns or pages is clear. “Continued on page 86” is all but a hyperlink from the past, which has been inherited by interactive; “Read the rest of this blog post” is basically the same thing.

• Interactive systems have an additional challenge in that the page might be larger than the screen (or viewport, as we often call it).

## Getting Started

You now have a general understanding that a page is an area that occupies the viewport of a mobile display. Pages can use a wrapper template to organize information consistently across the OS that will allow for a satisfying user experience. When making design decisions you must consider everything in this page section, even if you don’t have control (i.e., you’re not building an OS). You must know what it might do to your design. Consider your user’s goals and cognitive abilities, page layout guidelines, and the importance of legibility and readability in message displays.

The following chapter will provide specific information on theory and tactics, and will illustrate examples of appropriate design patterns. Always remember to read the antipatterns, to make sure you don’t misuse or overuse a pattern.