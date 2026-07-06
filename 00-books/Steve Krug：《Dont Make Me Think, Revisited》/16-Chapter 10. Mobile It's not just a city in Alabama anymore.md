# Chapter 10. Mobile: It’s not just a city in Alabama anymore

## WELCOME TO THE 21ST CENTURY — YOU MAY EXPERIENCE A SLIGHT SENSEOF VERTIGO

## [shouting] PHENOMENAL COSMIC POWERS! [softly] Itty-bitty living space!

—ROBIN WILLIAMS AS THE GENIE IN ALADDIN, COMMENTING ON THE UPSIDE AND DOWNSIDE OF THE GENIE LIFESTYLE

Ahh, the smartphone.

Phones had been getting gradually smarter for years, gathering in desk drawers and plotting amongst themselves. But it wasn’t until the Great Leap Forward<sup>1</sup> that they finally achieved consciousness.

## <sup>1</sup> Introduction of the iPhone June 2007.

I, for one, was glad to welcome our tiny, time-wasting overlords. I know there was a time when I didn’t have a powerful touch screen computer with Internet access in my pocket, but it’s getting harder and harder to remember what life was like then.

And of course it was about this same time that the Mobile Web finally came into its own. There had been Web browsers on phones before, but they—to use the technical term—sucked.

The problem had always been—as the Genie aptly put it—the itty-bitty living space. Mobile devices meant cramped devices, squeezing Web pages the size of a sheet of paper into a screen the size of a postage stamp. There were various attempts at solutions, even some profoundly debased “mobile” versions of sites (remember pressing numbers to select numbered menu items?) and, as usual, the early adopters and the people who really needed the data muddled through.

But Apple married more computer horsepower (in an emotionally pleasing, thin, aesthetic package—why are thin watches so desirable?) with a carefully wrought browser interface. One of Apple’s great inventions was the ability to scroll (swiping up and down) and zoom in and out (pinching and...unpinching) very quickly. (It was the very quickly part—the responsiveness of the hardware—that finally made it useful.)

For the first time, the Web was fun to use on a device that you could carry with you at all times.   
With a battery that lasted all day. You could look up anything anywhere anytime.

It’s hard to overestimate what a sea change this was.

Of course, it wasn’t only about the Web. Just consider how many things the smartphone allowed you to carry in your pocket or purse at all times: a camera (still and video, and, for many people, the best one they’d ever owned), a GPS with maps of the whole world, a watch, an alarm clock, all of your photos and music, etc., etc.

![](images/4598518da10d152c2e6008212c339ff1e7097b2ede0638ea3e0265925c4728ac.jpg)

It’s true: The best camera really is the one you have with you.

And think about the fact that for most people in emerging countries, in the same way they bypassed landlines and went straight to cellphones, the smartphone is their first—and only— computer.

There’s not much denying that mobile devices are the wave of the future, except for things where you need enormous horsepower (professional video editing, for example, at least for now) or a big playing surface (Photoshop or CAD).

## What’s the difference?

So, what’s different about usability when you’re designing for use on a mobile device?

In one sense, the answer is: Not much. The basic principles are still the same. If anything, people are moving faster and reading even less on small screens.

But there are some significant differences about mobile that make for challenging new usability problems.

As I write this, Web and app design for mobile devices is still in its formative “Wild West” days in many ways. It’s going to take another few years for things to shake out, probably just in time for innovations that will force the whole cycle to start over again.

I’m not going to talk very much about specific best practices because many of the bright interface design ideas that will eventually become the prevailing conventions probably haven’t emerged yet. And of course the technology is going to keep changing under our feet faster than we can run.

![](images/80ef8b845c1d6419a0d86eada1c0464c36c59494622aa80b727dbd91ea6f65d0.jpg)  
“App” | xkcd.com

What I will do is tell you a few things that I’m sure will continue to be true. And the first one is...

## It’s all about tradeoffs

One way to look at design—any kind of design—is that it’s essentially about constraints (things you have to do and things you can’t do) and tradeoffs (the less-than-ideal choices you make to live within the constraints).

To paraphrase Lincoln, the best you can do is please some of the people some of the time.<sup>2</sup>

<sup>2</sup> ...if, in fact, he ever actually said “You can fool some of the people all of the time, and all of the people some of the time, but you cannot fool all of the people all of the time.” One of the things I’ve learned from the Internet is that when it comes to memorable sayings attributed to famous people, 92% of the time they never said them. See en.wikiquote.org/wiki/Abraham\_Lincoln.

There’s a well-established meme that suggests that rather than being the negative force that they often feel like, constraints actually make design easier and foster innovation.

And it’s true that constraints are often helpful. If a sofa has to fit in this space and match this color scheme, it’s sometimes easier to find one than if you just go shopping for any sofa. Having something pinned down can have a focusing effect, where a blank canvas with its unlimited options—while it sounds liberating—can have a paralyzing effect.

You may not buy the idea that constraints are a positive influence, but it really doesn’t matter: Whenever you’re designing, you’re dealing with constraints. And where there are constraints, there are tradeoffs to be made.

In my experience, many—if not most—serious usability problems are the result of a poor decision about a tradeoff.

For example, I don’t use CBS News on my iPhone.

I’ve learned over time that their stories are broken up into too-small (for me) chunks, and each one takes a long time to load. (If the pages loaded faster, I might not mind.) And to add insult to injury, on each new page you have to scroll down past the same photo to get to the next tiny morsel of text.

Here’s what the experience looks like:

![](images/35d16c8fe6ed62ee9fd03d9e707cf5b4865c294172e77cf42e45d2967b906141.jpg)  
Tap to open the story, then wait. And wait. And wait.

![](images/207401e3f8c834942472b67952ef721e64189b53e310186c63c0b95c9ffcf6fe.jpg)  
When the page finally loads, swipe to scroll down past the photo.

![](images/ef6e44763e35cb0304aa6aef6fe5a3fc9249f0621af151bf70b15719f8af29bc.jpg)  
Read the two paragraphs of text, then tap Next and wait. And wait.

![](images/bc40110cbb55355e342b6fcd0a1cf7cdc115698eb8d9ce1547d00f922b7faf5e.jpg)  
Repeat 8 times to read the whole story.

It’s so annoying that when I’m scanning Google News (which I do several times a day) and notice that the story I’m about to tap is linked to CBS News, I always click on Google’s “More stories” link to choose another source.

When I run into a problem like this, I know that it’s not there because the people who designed it didn’t think about it. In fact, I’m sure it was the subject of some intense debate that resulted in a compromise.

I don’t know what constraints were at work in this particular tradeoff. Since there are ads on the pages, it may have been a need to generate more page views. Or it could have something to do with the way the content is segmented for other purposes in their content management system. I have no idea. All I do know is that the choice they made didn’t place enough weight on creating a good experience for the user.

Most of the challenges in creating good mobile usability boil down to making good tradeoffs.

## The tyranny of the itty-bitty living space

The most obvious thing about mobile screens is that they’re small. For decades, we’ve been designing for screens which, while they may have felt small to Web designers at the time, were luxurious by today’s standards. And even then, designers were working overtime trying to squeeze everything into view.

But if you thought Home page real estate was precious before, try accomplishing the same things on a mobile site. So there are definitely many new tradeoffs to be made.

One way to deal with a smaller living space is to leave things out: Create a mobile site that is a subset of the full site. Which, of course, raises a tricky question: Which parts do you leave out? One approach was Mobile First. Instead of designing a full-featured (and perhaps bloated) version of your Web site first and then paring it down to create the mobile version, you design the mobile version first based on the features and content that are most important to your users. Then you add on more features and content to create the desktop/full version.

It was a great idea. For one thing, Mobile First meant that you would work hard to determine what was really essential, what people needed most. Always a good thing to do.

But some people interpreted it to mean that you should choose what to include based on what people want to do when they’re mobile. This assumed that when people accessed the mobile version they were “on the move,” not sitting at their desk, so they’d only need the kinds of features you’d use on the move. For example, you might want to check your bank balances while out shopping, but you wouldn’t be likely to reconcile your checkbook or set up a new account.

Of course, it turned out this was wrong. People are just as likely to be using their mobile devices while sitting on the couch at home, and they want (and expect) to be able to do everything. Or at least, everybody wants to do some things, and if you add them all up it amounts to everything. If you’re going to include everything, you have to pay even more attention to prioritizing.

Things I want to use in a hurry or frequently should be close at hand. Everything else can be a few taps away, but there should be an obvious path to get to them.

![](images/91895033d2ad42a22a1c74404625a603dbd4c998503bcb119366a58e6b38dc2e.jpg)

The screenshot at left represents Now. Now, 10 Day, Hourly, and Details menus are at top with Now menu selected. The date and time is indicated as Dec 3, 2013, 6:09 PM. The current conditions of the given date and time are displayed on the screen. Forecast for the day is at bottom left which is indicated as 31 degrees Mostly Clear. The second screenshot from left   
represents the forecast for the next 10 days. 10 Day menu at top is selected. An arrow from 10 Day menu of the screenshot at left is pointing toward the current screenshot. Forecast for the   
next 10 days is displayed in rows. The third screenshot from left represents forecast for the next 12 hours. An arrow from Hourly menu of the screenshot at left is pointing toward the current   
screenshot. Hourly menu at top is selected. The forecast for each hour is displayed in rows. The   
screenshot at right represents the forecast for next Tuesday. An arrow from a row representing

Tuesday in the screenshot second from left is pointing toward the current screenshot. 10 Day menu is selected at top. The forecast for day and night of next Tuesday is displayed in rows.

In some cases, the lack of space on each screen means that mobile sites become much deeper than their full-size cousins, so you might have to tap down three, four, or five “levels” to get to some features or content.

This means that people will be tapping more, but that’s OK. With small screens it’s inevitable: To see the same amount of information, you’re going to be either tapping or scrolling a lot more. As long as the user continues to feel confident that what they want is further down the screen or behind that link or button, they’ll keep going.

Here’s the main thing to remember, though:

## MANAGING REAL ESTATE CHALLENGES SHOULDN’T BE DONE AT THE COST OF USABILITY<sup>3</sup>

<sup>3</sup> Thanks to Manikandan Baluchamy for this maxim.

## Breeding chameleons

The siren song of one-design-fits-all-screen-sizes has a long history of bright hopes, broken promises, and weary designers and developers.

If there are two things I can tell you about scalable design (a/k/a dynamic layout, fluid design, adaptive design, and responsive design), they’re these:

It tends to be a lot of work.

It’s very hard to do it well.

In the past, scalable design—creating one version of a site that would look good on many different size screens—was optional. It seemed like a good idea, but very few people actually cared about it. Now that small screens are taking over, everybody cares: If you have a Web site, you have to make it usable on any size screen.

Developers learned long ago that trying to create separate versions of anything—keeping two sets of books, so to speak—is a surefire path to madness. It doubles the effort (at least) and guarantees that either things won’t be updated as frequently or the versions will be out of sync. It’s still getting sorted out. This time, the problem has real revenue implications, so there will be technical solutions, but it will take time.

## In the meantime, here are three suggestions:

Allow zooming. If you don’t have the resources to “mobilize” your site at all and you’re not using responsive design, you should at least make sure that your site doesn’t resist efforts to view it on a mobile device. There are few things more annoying than opening up a site on your phone and discovering that you can’t zoom in on the tiny text at all. (Well, all right. Actually there are a lot of things more annoying. But it’s pretty annoying.)

Don’t leave me standing at the front door. Another real nuisance: You tap on a link in an email or a social media site and instead of taking you to the article in question it takes you to the mobile Home page, leaving you to hunt for the thing yourself.

![](images/9280f6812bd8143f690cd1b0dd80de0c580621cf232f419e0b94e120885adaa5.jpg)

A server says “Hi! I’m a server! Who are you?” A smartphone replies “I’m a browser. I’d like to see this article.” The server says, “Oh boy! I can help! Let me get it for– …whoa! You’re a smartphone browser?” The smartphone replies “Yeah.” The server further says “Cooool! Hey, I’ve got this new mobile version of my site! Check it out! Isn’t it pretty?” The smartphone says “Sure, but this is just your mobile site’s main page. Where’s the article I wanted?” The server asks “What article?” The smartphone replies “The one I–.” The server again asks “Who are you?” The smartphone replies “I–.” The server says “Hi! I’m a server!”

一 Always provide a link to the “full” Web site. No matter how fabulous and complete your mobile site is, you do need to give users the option of viewing the non-mobile version, especially if it has features and information that aren’t available in your mobile version. (The current convention is to put a Mobile Site/Full Site toggle at the bottom of every page.)

There are many situations where people will be willing to zoom in and out through the small viewport of a mobile device in return for access on the go to features they’ve become accustomed to using or need at that moment. Also, some people will prefer to see the desktop pages when using 7″ tablets with high-resolution screens in landscape mode.

## Don’t hide your affordances under a bushel

Affordances are visual clues in an object’s design that suggest how we can use it. (I mentioned them back in Chapter 3. Remember the doorknobs and the book by Don Norman? He popularized the term in the first edition of The Design of Everyday Things in 1988 and the design world quickly adopted it.<sup>4</sup>)

<sup>4</sup> Unfortunately, the way they used it wasn’t exactly what he intended. He’s clarified it in the new edition of Everyday Things by proposing to call the clues “signifiers” instead, but it may be too late to put that genie back in the bottle. With apologies to Don, I’m going to keep calling them affordances here because (a) it’s still the prevailing usage, and (b) it makes my head hurt too much otherwise.

Affordances are the meat and potatoes of a visual user interface. For instance, the threedimensional style of some buttons makes it clear they’re meant to be clicked. The same as with the scent of information for links, the clearer the visual cues, the more unambiguous the signal.

Report

Report

Report

Report

Strong affordance

Not so much

A colored oval labeled Report, a colored oval with dark borders labeled Report, a rectangle labeled Report, and a label Report are from left to right. An arrow from a label “Strong   
affordance” is pointing toward “Not so much” at right below the Report labels indicating that the affordance of the Report labels reduces as it proceeds from left to right.

In the same way, a rectangular box with a border around it suggests that you can click in it and type something. If you had an editable text box without a border, the user could still click on it and type in it if he knew it was there. But it’s the affordance—the border—that makes its function clear.

## Name

Name

Name John Smil

Name

John Smil

For affordances to work, they need to be noticeable, and some characteristics of mobile devices have made them less noticeable or, worse, invisible. And by definition, affordances are the last thing you should hide.

This is not to say that all affordances need to hit you in the face. They just have to be visible enough that people can notice the ones they need to get their tasks done.

## No cursor = no hover = no clue

Before touch screens arrived, Web design had come to rely heavily on a feature called hover— the ability of screen elements to change in some way when the user points the cursor at them without clicking.

But a capacitive touch screen (used on almost all mobile devices) can’t accurately sense that a finger is hovering above the glass, only when the finger has touched it. This is why they don’t have a cursor.<sup>5</sup>

<sup>5</sup> Did you ever notice that the cursor was missing? I have to admit that I used my first iPhone for several months before it dawned on me that there was no cursor.

As a result, many useful interface features that depended on hover are no longer available, like tool tips, buttons that change shape or color to indicate that they’re clickable, and menus that drop down to reveal their contents without forcing you to make a choice.

As a designer, you need to be aware that these elements don’t exist for mobile users and try to find ways to replace them.

## Flat design: Friend or foe?

Affordances require visual distinctions. But the recent trend in interface design (which may have waned by the time you read this) has moved in exactly the opposite direction: removing visual distinctions and “flattening” the appearance of interface elements.

It looks darned good (to some people, anyway), and it can make screens less cluttered-looking. But at what price?

In this case the tradeoff is between a clean, uncluttered look on one hand and providing sufficient visual information so people can perceive affordances on the other.

Unfortunately, Flat design has a tendency to take along with it not just the potentially distracting decoration but also the useful information that the more textured elements were conveying.