# CHAPTER 9 INFORMATION ACCESS

## OVERVIEW

9.1. Introduction

9.2. Small-screen impacts

9.3. Designs for browsing

9.4. Improving search

9.5. Mobile information ecologies

## KEY POINTS

Users will want to use mobile devices to access all sorts of information – from emails to novels.

Designing the interaction with this content involves both detailed screen layout considerations and wider aspects such as the degree of context adaptation and the information servers used.

Early research on non-mobile, small-screen devices suggests that users will have little trouble when reading or interacting with simple content – short chunks of material with limited navigation content.

■ If users try to interact with more complex content which is not adapted for small-screen viewing, usability disasters will occur. Guidelines and presentation techniques can help. These point towards the need to give users effective ways of overviewing and assessing content before having to commit to accessing it in full.

Mobiles must play their part in the information ecology, fitting in with other devices, network availability and physical resources in the environment. Peer-to-peer approaches offer interesting, novel possibilities.

## 9.1 INTRODUCTION

With always-on broadband connections commonly found in homes as well as workplaces, piping information into powerful, fully-featured desktop and laptop computers, you could be forgiven for thinking that people have all the access they could ever want to digital resources. Given the opportunities they have when not mobile, why would anyone, in addition to all this, want to use a small device, with limited input and output capabilities to find and read content?

There is, though, a strong information imperative – we are great consumers of information. We hunt and forage for it; sometimes we immerse and wallow ourselves in it, at other times we skip through it lightly, moving from one nugget to the next. You would think that after a day at the office, a day spent intensely at being productive and efficient, commuters would want to do anything but process more information – but a ride on any train or bus will show you how powerful this information seeking urge is: you will see people flicking through magazines and newspapers, and others browsing documents they’ve encountered during the day.

When mobile, then, users will appreciate access to lots of types of information; sometimes the purposes for and preferred format of the content will be similar to those when using their home and work computers, while at other times it will be quite different.

Standing in a bookstore, reading the dust jacket of a new book on naval history, Jenny decides to check what other readers have said about it by using her mobile to look up reviews on an online site. She also compares the price; it’s a little cheaper from the e-retailer but she wants the book right now so purchases it from the shop, anyhow.

Having mislaid the directions to a meeting, John needs to use his mobile to look up the address of an office; directions would be helpful too.

Rosie stores hundreds of emails on her mobile. She’s on a train traveling to see a client and just wants to double-check the agenda she proposed a few weeks ago. How will she find and skim-read the notes quickly?

Nathan works in London and a major natural disaster has just hit his home continent, many thousands of miles away. Whenever he gets a moment, he wants to find more news of the incident in any way he can, be it on his desktop computer or via his mobile device.

Jason wants to call Paul, an acquaintance, but doesn’t have his telephone number. He thinks one of his closer friends will have it in the address books stored on their mobiles. What if his mobile could access these friends’ contact lists and give him the number without his having to call them and ask? (Chen et al., 2002)

If you are developing content for mobile access, as well as identifying the information your users will want, you can use the user-understanding, prototyping and evaluation techniques we saw in the second part of the book to figure out how best to deliver it. Some aspects you’ll need to find answers for are outlined below; we’ll be considering such issues – and interaction designs to address them – throughout this chapter.

Simplicity. Does the user want a short, concise chunk of information or would they appreciate being able to browse more extensively? Often they will want the former – that is, where the content is brief and serves a focused purpose. This brevity might be an intrinsic quality of the information – for example, consider a set of news headlines, product information or directions to a location. Alternatively, it might be a function of a technique used to summarize or overview more complex information, which the user can further peruse if motivated. There will be occasions, however, when the user has the time and inclination to consider longer, structured forms of content (in some countries, for instance, reading novels on mobile phones is a popular activity).

Format. Is the content specifically designed for the mobile? If not, how will it be adapted to be useful and usable on these sorts of platform? Something to consider here, in particular, is the role of carefully selected, grouped information, sometimes called mobile portals or channels.

Context. To what extent is the content they are seeking context-driven? Is the information being accessed very much tied to things like the location or time of access, or is it something that could be sought anywhere, anytime? Location-based services are seen as a highly important form of information provision by mobile developers, but in rushing to produce many types of content that is tailored in this way, there is a danger that other contextual factors or the value of non-context adapted information are underestimated.

Source. Some information will be stored locally on the device, others on remote servers. There’s also the possibility of finding information in a peer-to-peer fashion, where other mobiles act as servers of content. Then there are technologies to enable nearby, short-range wireless connections, providing access to localized information servers: a street server could give content on shops in that street, a museum gallery server could give information on pictures in that room, and so on. Users may need to be made aware of the potential sources of content and given control over the information they draw on.

Interaction. How does the user get the information? It can be pushed to them, so they are automatically provided with it with very little interaction, or they can actively pull it by browsing content listings and the like. Hybrid push–pull approaches are possible too, with, for instance, users setting up details of the sorts of information they want to find out about (the pull component) and then, when that information becomes available, the system delivering it (the push part).

While we will see an example of non-visual presentation via a mobile a little later on, much information will be delivered via the device’s screen. That screen, in many handhelds, will be small. Even with the increasing quality of displays, their ability to convey information will remain limited in comparison to those seen in desktop contexts. We begin this chapter, then, by looking at the impact of this reduced screen real-estate for a number of information access tasks.

Two of these fundamental information activities are browsing and searching. Browsing is the process of moving through content, using access paths (such as menus and hyperlinks); searching, on the other hand, is about locating information resources in direct ways – that might mean entering textual search terms or taking a picture of something for the system to use in a search. Browsing, then, is finding things by navigation, and searching is finding things by querying (Furnas and Rauch, 1998). Innovative browse and search schemes have been designed for effective small-screen use; we’ll consider a number of these, weighing up their pros and cons.

In Chapter 2, we discussed the idea of information ecologies. That’s the notion of people making use of evolving sets of complementary information resources in carrying out their tasks. So, to conclude this chapter, we look in more detail at what this might mean in the mobile context, by considering how a device might be used with other digital and non-digital resources that surround it.

## 9.2 SMALL-SCREEN IMPACTS

There’s a scene in the Walt Disney movie Aladdin that encapsulates the challenge facing mobile designers. The genie is demonstrating his enormous potential and power; seconds later, he’s bemoaning the limited dimensions of his lamp: ‘‘It’s all part and parcel of the whole genie gig: phenomenal cosmic powers, itty bitty living space.’

Small display areas are part and parcel of the whole mobile gig. Table 9.1 compares the display characteristics of a number of mobile devices: a PDA, a PocketPC, a mobile communicator (telephone/PDA) and a mobile phone. The characteristics of a laptop computer and desktop screen are also shown.

Devices A, B and C are sophisticated consumer handheld devices. While resolution and color quality continue to improve, an aspect that will remain a very real constraint is the size of the viewable screen. To remain pocket-portable, the physical dimensions will have to be limited. Increasing the number of pixels packed into these small displays will enhance the user’s experience

TABLE 9.1

Display characteristics of example mobiles and conventional, large-screen devices (Jones et al., 2004)
<table><tr><td rowspan="2">Device</td><td rowspan="2"></td><td colspan="3">Display characteristics</td></tr><tr><td>Resolution (pixels)</td><td>Viewable dimensions (inches) (inches)</td><td>Colors</td></tr><tr><td>A</td><td>Palm Tungsten T PDA</td><td>320 × 320</td><td>2.3 width 2.3 height</td><td>16-bit (65 536 colors)</td></tr><tr><td>B</td><td>Compaq iPAQ 5400 series Pocket PC</td><td>240 × 320</td><td>2.26 width 3.02 height</td><td>16-bit (65 536 colors)</td></tr><tr><td>C</td><td>Nokia Communicator 9290 Mobile telephone/PDA</td><td>640 × 200</td><td>4.3 width 1.4 height</td><td>12-bit (4096 colors)</td></tr><tr><td>D</td><td>Nokia 6800 Mobile telephone</td><td>128 × 128</td><td>(approx.) 1.2 width 1.2 height</td><td>12-bit (4096 colors)</td></tr><tr><td>E</td><td>Apple Titanium Powerbook 15&quot;</td><td>1280 × 854 (max.)</td><td>(approx.) 12 width 8 height</td><td>Millions of colors</td></tr><tr><td>F</td><td>Philips 202P monitor</td><td>2048 × 1536 (max.)</td><td>15.2 diagonal 16 width 12 height</td><td>Millions of colors</td></tr></table>

in terms of legibility of text and crispness of images, but tiny pieces of text or graphics, however highly rendered, will not be usable.

## BOX 9.1

## FLEXIBLE ORGANIC LIGHT EMITTING DIODE (FOLED) SCREENS

Will small screens, and their inherent interaction challenges, pass into technological history in the near future? One remarkable, promising innovation that will have an impact on the design of mobile devices is Flexible Organic Light Emitting Diodes (FOLEDs). Whereas today’s LEDs are housed within rigid substances, like glass, FOLEDs can be embedded within bendable, rollable materials such as lightweight, thin plastic. Need a large screen? Just unroll one, view the content and roll it back up when you’ve finished. To further add to the full-screen experience, you could also use a technique like Canesta, where the large keyboard is projected onto any available surface, with finger tracking picking out the keys being ‘pressed’ (Roeber et al., 2003).

While these sorts of innovations will allow users to enjoy fully featured input and output devices while retaining much of the portability advantages of current mobiles, small screens (and input controls) will continue to dominate the market, at least in the medium-term future. Even when it becomes viable to use FOLEDs pervasively, and this is some way off, there will still be a strong desire for the ultra-portability of smaller screens. Users will continue to prefer devices that can be placed in a shirt pocket, are ready and available at all times with minimal startup or setup costs, and can be operated with one hand. ■

As well as considering screen resolutions, a useful way of understanding the impact of the small-screen factors is to consider the size of physical display relative to standard devices. Devices A, B and C offer only 6–7% of the display area of device E and 3–4% of that of device F. Device D is even more restricted, with 2% and 1% of the display areas of devices E and F respectively.

What we are faced with, then, is a world (wide web, even) of information, presented to the user through a diminutive window. Let’s consider the impact of these smaller display areas on user effectiveness. What we will see is that for simple tasks such as reading a bite-sized chunk of text users can cope well; however, as activities become more complex, such as browsing and searching web content, there could be significant problems if careful design is not carried out.

## 9.2.1 LESSONS FROM THE PAST

Long before the small screens of mobiles, there were other limited display areas that interested human factors researchers. Take automated cash machines. While today’s ATMs often have large, colorful screens, some early ones could display only one line of text, sometimes read through a periscope-style viewer. Then, there were electronic devices from photocopiers to sewing machines, all with small LCD displays to present information; many of these types of device, of course, continue to have relatively limited screens.

So during the 1980s and the early part of the 1990s, there were a number of studies looking at the effect on reading times, comprehension and usability of different-sized display areas.

## Reading and Comprehension

One of the early studies considered the effect on reading of window heights and line widths (Duchnicky and Kolers, 1983). These researchers found that difficulties arose mainly when the width of the display was reduced, with the full-width display being read 25% faster than the screen which was one-third of the width.

The impact of varying the display height, however, was very much less dramatic. Although very small window sizes (one or two lines, like those seen in early mobile phones, for instance) gave poor performance, a four-line display was only 9% slower than one with 20 lines.

Another experiment provides further evidence of the effect. In this, a smaller screen size also slowed down reading time, but not dramatically. Users were asked to read computer program texts and answer questions (Resiel and Shneiderman, 1987). On a 22-line display this task took 9.2 minutes, while on a 60-line display it was some 15% faster.

Fast reading speed with minimal understanding is, of course, of little use. Again, though, in terms of simple chunks of text with limited navigation possibilities, it seems that users will have few problems in making sense of the information unless the display size is very small (one or two lines high). In the study we’ve just mentioned, by Duchnicky and Kolers (1983), there were no significant improvements in comprehension when the display height was increased to 20 lines over the four-line display.

In another experiment, participants were presented with a 3500-line text using a 20- and 60-line display window and were asked to read the texts and later summarize the main points (Dillon et al., 1990). This study also found that the comprehension rates on the smaller screen were as good as those on the larger.

What are the implications of all this past research for future mobile devices? Unsurprisingly, reading and using simple textual materials on a small screen will be slower than if a large display is used. However, the experience will be manageable and not so dramatically different from the large-screen case.

The biggest impacts come as the width of the display used for the content is reduced – make sure, then, that you use as much of the horizontal plane as possible for the information itself: menu bars or navigation controls placed in columns, for example, will reduce the overall usability of the system.

## User Interaction

## Within-page navigation

If the content cannot be displayed within one non-scrolled screen, then obviously the user will have to use mechanisms that allow them to view the remainder. Techniques include scrolling (allowing small, fine-grained movement through the information) and paging (making bigger jumps, hopping from one chunk of the content to the next).

Not being able to see the whole doesn’t just potentially mean more effort to sequentially view all the content. Users may also have to scroll or page backward as well as forward through text to orient themselves, the navigation helping them to understand the context of the information being viewed (Dillon et al., 1990). For mobiles, then, keeping the content simple in terms of structure is a must – you don’t want your users having to do lots of navigation to understand the material and how to use it.