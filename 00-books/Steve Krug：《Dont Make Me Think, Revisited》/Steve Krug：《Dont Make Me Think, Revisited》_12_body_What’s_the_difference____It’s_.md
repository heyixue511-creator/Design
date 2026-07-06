# What’s the difference? / It’s all about tradeoffs / The tyranny of the itty-bitty living space / MANAGING REAL ESTATE CHALLENGES SHOULDN’T BE DONE AT THE COST OF USABILITY<sup>3</sup> / Breeding chameleons / In the meantime, here are three suggestions: / Don’t hide your affordances under a bushel / Name / No cursor = no hover = no clue / Flat design: Friend or foe? / I'M A HEADING / I'M A BUTTON / I'M A BUTTON I'M NOT / You actually can be too rich or too thin / Mobile apps, usability attributes of / Delightful is the new black / What is this “delight” stuff, anyway? / Apps need to be learnable / Apps need to be memorable, too / Usability testing on mobile devices / The logistics of mobile testing / My recommendations / Proof of concept: My Brundleyfly<sup>7</sup> camera / That’s it. / Finally... / Chapter 11. Usability as common courtesy / Nothing. / mensch?” / The reservoir of goodwill / Things that diminish goodwill / Things that increase goodwill / Know what questions I’m likely to have, and answer them. Frequently Asked / Chapter 12. Accessibility and you / JUST WHEN YOU THINK YOU’RE DONE, A CAT FLOATS BY WITH BUTTEREDTOAST STRAPPED TO ITS BACK / —JOHN FRAZEE, IN THE JOURNAL OF IRREPRODUCIBLE RESULTS / Why is that? / What developers and designers hear

> Section: body | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Steve Krug：《Dont Make Me Think, Revisited》\Steve Krug：《Dont Make Me Think, Revisited》\Steve Krug：《Dont Make Me Think, Revisited》\auto\Steve Krug：《Dont Make Me Think, Revisited》.md

## What’s the difference?

So, what’s different about usability when you’re designing for use on a mobile device?

In one sense, the answer is: Not much. The basic principles are still the same. If anything, people are moving faster and reading even less on small screens.

But there are some significant differences about mobile that make for challenging new usability problems.

As I write this, Web and app design for mobile devices is still in its formative “Wild West” days in many ways. It’s going to take another few years for things to shake out, probably just in time for innovations that will force the whole cycle to start over again.

I’m not going to talk very much about specific best practices because many of the bright interface design ideas that will eventually become the prevailing conventions probably haven’t emerged yet. And of course the technology is going to keep changing under our feet faster than we can run.

![](images/255a3687a2edcb646c8b48489990608fc1037a97cfc7a885b1612ceea4856445.jpg)  
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

![](images/496dc7b4f2ffa612547dbe7c5433cf68bbe012a2e8a3988d9c9edd9eee5f6537.jpg)  
Tap to open the story, then wait. And wait. And wait.

![](images/a71095eb244de2a3f2e2bfe3249896ba613b89e9cf6fec93006a282df57badd4.jpg)  
When the page finally loads, swipe to scroll down past the photo.

![](images/564b70d91e9a45a57c718cca60a808ced969e5a70fc05540a02a07692f234099.jpg)  
Read the two paragraphs of text, then tap Next and wait. And wait.

![](images/82f7978f9fd9f34ec7c1a445f79f96d887fb0e8a9bb76a8657676c7da82c8899.jpg)  
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

![](images/cd1de4defa28bbde699ead63f8ddad3bafc03fe8efdd51baea2a25daa6ca92fe.jpg)

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

![](images/5e8fb7b7da05d895f772cafe7b24dd6fe34b890b6de0eb4cb59f0d0d842077c8.jpg)

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

# I'M A HEADING

# I'M A BUTTON

## I'M A BUTTON I'M NOT

The distinctions required to draw attention to an affordance often need to be multi-dimensional: It’s the position of something (e.g., in the navigation bar) and its formatting (e.g., reversed type, all caps) that tell you it’s a menu item.

By removing a number of these distinctions from the design palette, Flat design makes it harder to differentiate things.

Flat design has sucked the air out of the room. It reminds me of the pre-color world in my favorite Calvin and Hobbes cartoon/comic/comic strip. (The rest of the cartoon is at the end of Chapter 13.)

![](images/d6c4e1a3b949ba649773a22ffb225da14066630ed1b947d9e859b72599d87a99.jpg)  
CALVIN AND HOBBES © 1989 Watterson. Reprinted with permission of UNIVERSAL UCLICK. All rights reserved.

Calvin asks his dad, “Dad, how come old photographs are always black and white? Didn’t they have color film back then?” Dad replies “Sure they did. In fact, those old photographs are in color. It’s just the world was black and white then.” Calvin exclaims “Really?” Dad says, “Yep. The world didn’t turn color until sometime in the 1930s, and it was pretty grainy color for a while, too.” Calvin says “That’s really weird.” Dad says, “Well, truth is stranger than fiction.”

You can do all the Flat design you want (you may have to, it may be forced on you), but make sure you’re using all of the remaining dimensions to compensate for what you lose.

## You actually can be too rich or too thin

...but computers can never be too fast. Particularly on mobile devices, speed just makes everything feel better. Slow performance equals frustration for users and loss of goodwill for publishers.

For instance, I prize the breaking news alerts from the AP (Associated Press) mobile app.   
They’re always the first hint I get of major news stories.

Unfortunately for AP, though, whenever I tap on one of their alerts, the app insists on loading a huge chunk of photos for all the other current top stories before showing me any details about the alert.

![](images/53669d48051aeedae387c1d3b1c5b3607f65f927e0c1b46ee1f0967c4244538a.jpg)

In the screenshot at the left, the time and date are displayed as 4:15 Monday, December 2. A box on the screen is titled AP Mobile with the text “Breaking (4:13 PM EST): NTSB: Train that derailed in NYC was traveling 82 mph as it approached 30 mph zone.” A right arrow button is at the bottom with a label “slide to view.” In the screenshot at the right, AP logo is displayed with the text “Loading AP News” displayed at the bottom.

As a result, I’ve formed a new habit: When an AP alert arrives, I immediately open the New York Times site or Google News to see if they’ve picked up the story yet.

We’re all used to very fast connections nowadays, but we have to remember that mobile download speeds are unreliable. If people are at home or sitting at Starbucks, download speeds are probably good, but once they leave the comfort of Wi-Fi and revert to 4G or 3G or worse, performance can vary widely.

Be careful that your responsive design solutions aren’t loading up pages with huge amounts of code and images that are larger than necessary for the user’s screen.

## Mobile apps, usability attributes of

You may remember that way back on page 9 I mentioned that I’d talk later about attributes that some people include in their definitions of usability: useful, learnable, memorable, effective, efficient, desirable, and delightful. Well, that time has arrived.

Personally, my focus has always been on the three that are central to my definition of usability:

A person of average (or even below average) ability and experience can figure out how to use the thing [i.e., it’s learnable] to accomplish something [effective] without it being more trouble than it’s worth [efficient].

I don’t spend much time thinking about whether things are useful because it strikes me as more of a marketing question, something that should be established before any project starts, using methods like interviews, focus groups, and surveys. Whether something is desirable seems like a marketing question too, and I’ll have more to say about that in the final chapter.

For now let’s talk about delight, learnability, and memorability and how they apply to mobile apps.

## Delightful is the new black

## What is this “delight” stuff, anyway?

Delight is a bit hard to pin down; it’s more one of those “I’ll know it when I feel it” kind of things. Rather than a definition, it’s probably easier to identify some of the words people use when describing delightful products: fun, surprising, impressive, captivating, clever, and even magical.<sup>6</sup>

<sup>6</sup> My personal standard for a delightful app tends to be “does something you would have been burned at the stake for a few hundred years ago.”

Delightful apps usually come from marrying an idea about something people would really enjoy being able to do, but don’t imagine is possible, with a bright idea about how to use some new technology to accomplish it.

SoundHound is a perfect example.

Not only can it identify that song that you hear playing wherever you happen to be, but it can display the lyrics and scroll them in sync with the song.

![](images/ab5329aad8edbde61b64bb17c310b18c7419e7593a9ef9ae14d36d418101f081.jpg)

![](images/ccea4f0338d6ef065cfb15a0d64cc53715f440563d4c9b05d66f60cdbfed481b.jpg)

![](images/3058a177fc196d080bf66b0f4ad56aa491c4f3951c360ea448f2e3ee99f823ca.jpg)  
In the screenshot at left, a button at top reads as “What’s that song? SoundHound Tap here!” Two photographs are displayed below the button. In the screenshot at center, “Listening” is displayed in a box. Cancel button is at top left. A poster with play button is below the box. The screenshot at right is titled Results. Home button is at top left and button with Home icon is at

top right. “Mambo Italiano Rosemary Clooney” is displayed next to a play button. Live Lyrics are displayed below the play button. Demi-Centennial 1995 is displayed with a right arrow next to it. “Listen Now on Rdio” and “Play Free in Spotify” icons are at bottom. Comment box is also at bottom with Facebook and Twitter icons.

And Paper is not your average drawing app. Instead of dozens of tools with thousands of options, you get five tools with no options. And each one is optimized to create things that look good.

![](images/5f037d4a3a96af684096ca0077ee31c63917a6847627f1202f1ca49fe2caffad.jpg)

![](images/e0f55cac154216193124daa7eb384daa3222d94ec258b7b406dc3c8585e95de0.jpg)

![](images/7d3fb69dd2c247de1d6ff4ff76971dbb1f5b2fef2959ce68c5258f4f39fa2991.jpg)

Building delight into mobile apps has become increasingly important because the app market is so competitive. Just doing something well isn’t good enough to create a hit; you have to do something incredibly well. Delight is sort of like the extra credit assignment of user experience design.

Making your app delightful is a fine objective. Just don’t focus so much attention on it that you forget to make it usable, too.

## Apps need to be learnable

One of the biggest problems with apps is that if they have more than a few features they may not be very easy to learn.

Take Clear, for example. It’s an app for making lists, like to-do lists. It’s brilliant, innovative, beautiful, useful, and fun to use, with a clean minimalist interface. All of the interactions are elegantly animated, with sophisticated sound effects. One reviewer said, “It’s almost like I’m playing a pinball machine while I’m staying productive.”

The problem is that one reason it’s so much fun to use is that they’ve come up with innovative interactions, gestures, and navigation, but there’s a lot to learn.

With most apps, if you get any instructions at all it’s usually one or two screens when you first launch the app that give a few essential hints about how the thing works. But it’s often difficult or impossible to find them again to read later.

And if help exists at all (and you can find it), it’s often one short page of text or a link to the developer’s site with no help to be found or a customer support page that gives you the email address where you can send your questions.

This can work for apps that are only doing a very few things, but as soon as you try to create something that has a lot of functionality—and particularly any functions that don’t follow familiar conventions or interface guidelines—it’s often not enough.

The people who made Clear have actually done a very good job with training compared to most apps. The first time you use it, you tap your way through a nicely illustrated ten-screen quick tour of the main features.

![](images/1a366f28bcb7f8366b449fd350b09630b13933c610b501b50d461a8e4697b4e4.jpg)

In the screenshot at left, items are listed on a mobile screen from top to bottom with text “Clear   
sorts items by priority. Important items are highlighted at the top” displayed at bottom. Second dot of seven dots at bottom is highlighted. In the second screenshot from left, an item on a mobile screen is selected with a vertical line on the mobile indicating that the item can be moved up or down. Text “Tap and hold to pick up an item. Drag it up or down to change its priority” is displayed at bottom. Third dot of seven dots at bottom is highlighted. In the   
screenshot at the center, three layers of a screen are given from top to bottom with the top level   
indicated as Menu, next level indicated as Lists, and the bottom level indicated as Items. Text   
“There are three navigation levels” is displayed at bottom. Fourth dot of seven dots at bottom is highlighted. In the second screenshot from right, the items on a mobile screen are pinched   
together vertically. Text “Pinch together vertically to collapse your current level and navigate   
up” is displayed at bottom. Fifth dot of seven dots at bottom is highlighted. In the screenshot at   
right, a list on a mobile screen is tapped. Text “Tap on a list to see its content. Tap on a list title to edit it” is displayed at bottom. Sixth dot of seven dots at bottom is highlighted.

This is followed by an ingenious tutorial that’s actually just one of their lists.

![](images/072ca16e7e1ca46bdbf2e060e8aa073498b1812926f107d21bbb94f101b36bed.jpg)  
In the screenshot at left, items with text “Swipe to the right to complete!” “Swipe to the left to

delete,” “Tap and hold to pick me up,” “Pull down to create an item,” “Try shaking to undo,”

“Try pinching two rows apart,” and “Try pinching vertically shut” are displayed from top to bottom. In the screenshot at center, the first item of the list “Swipe to the right to complete!” is shaded in a different color and slightly moved to the right with the text striked out. A tick mark is at the left of the item. In the screenshot at right, “Tap and hold to pick me up” item is selected

with another item “Swipe to the right to complete!” striked out at the bottom.

But when I’ve used it to do demo usability tests during my presentations, it hasn’t fared so well. I give the participant/volunteer a chance to learn about the app by reading the description in the app store, viewing the quick tour, and trying the actions in the tutorial. Then I ask them to do the type of primary task the app is designed for: create a new list called “Chicago trip” with three items in it — Book hotel, Rent car, and Choose flight.

So far, no one has succeeded.

Even though it’s shown in the slide show on the way in, people don’t seem to get the concept that there are levels: the level of lists, the level of items in lists, and the level of settings. And even if they remember seeing it, they still can’t figure out how to navigate between levels. And if you can’t figure that out, you can’t get to the Help screens. Catch-22.

That’s not to say that no one in the real world learns how to use it. It gets great reviews and is consistently a best seller. But I have to wonder how many people who bought it have never mastered it, or how many more sales they could make if it were easier to learn.

And this is a company that’s put a lot of effort into training and help. Most don’t.

You need to do better than most, and usability testing will help you figure out how.

## Apps need to be memorable, too

There’s one more attribute that’s important: memorability. Once you’ve figured out how to use an app, will you remember how to use it the next time you try or will you have to start over again from scratch?

I don’t usually talk much about memorability because I think the best way to make things easy to relearn is to make them incredibly clear and easy to learn in the first place. If it’s easy to learn the first time, it’s easy to learn the second time.

But it’s certainly a serious problem with some apps.

One of my favorite drawing apps is ASketch. I love this app because no matter what you try to draw and how crudely you draw it, it ends up looking interesting.

![](images/bb90d5192edaffe7cdc842b79c6a26f36d6bcc7971050b04a3132eaa190f0132.jpg)

But for months, each time I opened it I couldn’t remember how to start a new drawing. In fact, I couldn’t remember how to get to any of the controls. To maximize the drawing space there weren’t any icons on the screen.

I’d try all the usual suspects: double tap, triple tap, tap near the middle at the top or bottom of the screen, various swipes and multi-finger taps, and finally I’d hit on it. But by the next time I went to use it I’d forgotten what the trick was again.

![](images/fa81711c5c67cb0521e6da0362e990a27af0c1faf3bbcba1535b9243c9eea4f2.jpg)

![](images/5e519b7caee709c9d08df0abfc7bb3c7e8321a24c0249c3c6911d50793b0abde.jpg)

Memorability can be a big factor in whether people adopt an app for regular use. Usually when you purchase one, you’ll be willing to spend some time right away figuring out how to use it. But if you have to invest the same effort the next time, it’s unlikely to feel like a satisfying experience. Unless you’re very impressed by what it does, there’s a good chance you’ll abandon it—which is the fate of most apps.

Life is cheap (99 cents) on mobile devices.

## Usability testing on mobile devices

For the most part, doing usability testing on mobile devices is exactly the same as the testing I described in Chapter 9.

You’re still making up tasks for people to do and watching them try to do them. You still prompt them to say what they’re thinking while they work. You still need to keep quiet most of the time and save your probing questions for the end. And you should still try to get as many stakeholders as possible to come and observe the tests in person.

Almost everything that’s different when you’re doing mobile testing isn’t about the process; it’s about logistics.

## The logistics of mobile testing

When you’re doing testing on a personal computer, the setup is pretty simple:

The facilitator looks at the same screen as the participant.

Screen sharing software allows the observers to see what’s happening.

Screen recording software creates a video of the session.

But if you’ve ever tried doing tests on mobile devices, you know that the setup can get very complicated: document cameras, Webcams, hardware signal processors, physical restraints (well, maybe not physical restraints, but “Don’t move the device beyond this point” markers to keep the participant within view of a camera), and even things called sleds and goosenecks.

Here are some of the issues you have to deal with:

Do you need to let the participants use their own devices?

Do they need to hold the device naturally, or can it be sitting on a table or propped up on a stand?

What do the observers need to see (e.g., just the screen, or both the screen and the participant’s fingers so they can see their gestures)? And how do you display it in the observation room?

How do you create a recording?

One of the main reasons why mobile testing is complicated is that some of the tools we rely on for desktop testing don’t exist yet for mobile devices. As of this writing, robust mobile screen recording and screen sharing apps aren’t available, mainly because the mobile operating systems tend to prohibit background processes. And the devices don’t really have quite enough horsepower to run them anyway.

I expect this to change before long. With so many mobile sites and apps to test, there are already a lot of companies trying to come up with solutions.

## My recommendations

Until better technology-based solutions come along, here’s what I’d lean toward:

Use a camera pointed at the screen instead of mirroring. Mirroring is the same as screen sharing: It displays what’s on the screen. You can do it with software (like Apple’s Airplay) or hardware (using the same kind of cable you use to play a video from your phone or tablet on a monitor or TV).

But mirroring isn’t a good way to watch tests done on touch screen devices, because you can’t see the gestures and taps the participant is making. Watching a test without seeing the participant’s fingers is a little like watching a player piano: It moves very fast and can be hard to follow. Seeing the hand and the screen is much more engaging.

If you’re going to capture fingers, there’s going to be a camera involved. (Some mirroring software will shows dots and streaks on the screen, but it’s not the same thing.)

Attach the camera to the device so the user can hold it naturally. In some setups, the device sits on a table or desk and can’t be moved. In others, the participant can hold the device, but they’re told to keep it inside an area marked with tape. The only reason for restricting movement of the device is to make it easier to point a camera at it and keep it in view.

If you attach the camera to the device, the participant can move it freely and the screen will stay in view and in focus.

Don’t bother with a camera pointed at the participant. I’m really not a fan of the face camera. Some observers like seeing the participant’s face, but I think it’s actually a distraction. I’d much rather have observers focus on what’s happening on the screen, and they can almost always tell what the user is feeling from their tone of voice anyway.

Adding a second camera inevitably makes the configuration much more complicated, and I don’t think it’s worth the extra complexity. Of course, if your boss insists on seeing faces, show faces.

## Proof of concept: My Brundleyfly<sup>7</sup> camera

<sup>7</sup> Brundlefly is the word Jeff Goldblum’s character (Seth Brundle) in The Fly uses to describe himself after his experiment with a teleportation device accidentally merges his DNA with that of a fly.

Out of curiosity, I built myself a camera rig by merging a clip from a book light with a Webcam. It weighs almost nothing and captures the audio with its built-in microphone. Mine cost about \$30 in parts and took about an hour to make. I’m sure somebody will manufacture something similar—only much better—before long. I’ll put instructions for building one yourself online at rocketsurgerymadeeasy.com.

![](images/c5bd4a496152e15fa77db77a977fdd18bcfe2242cdd9e014b42731d156a1097d.jpg)

Photograph of Macally web camera is shown with online information displayed as follows: “Macally ICECAM2 USB 2.0 Video Web Camera with Built-in Microphone (White) By Macally (Five stars with 3.5 shaded) 209 customer reviews List Price: \$29.99 (striked out)

Price: \$16.59 You Save: \$13.40 (45%) Only 14 left in stock Ships from and sold by Amazon.com” Plus Photograph of reading light is shown with online information displayed as follows: “Lightwedge Flex Neck Reading Light, Soft Touch Black By Lightwedge (Five stars with 3.5 shaded) 250 customer reviews Price: \$15.03 Only 1 left in stock. Sold by DMK Retail and Fulfilled by Amazon” Equals Photograph of Brundleyfly camera. “Lightweight webcam plus Lightweight clamp and Gooseneck equal Brundlefly” is labeled at bottom.

Lightweight webcam + Lightweight clamp and Gooseneck = Brundlefly

Attaching a camera to the device creates a very easy-to-follow view. The observers get a stable view of the screen even if the participant is waving it around.

I think it solves most of the objections to other mounted-camera solutions:

They’re heavy and awkward. It weighs almost nothing and barely changes the way the phone feels in your hand.

They’re distracting. It’s very small (smaller than it looks in the photo) and is positioned out of the participant’s line of sight, which is focused on the phone.

Nobody wants to attach anything to their phone. Sleds are usually attached to phones with Velcro or double-sided tape. This uses a padded clamp that can’t scratch or mar anything but still grips the device firmly.

One limitation of this kind of solution is that it is tethered: It requires a USB extension cable running from the camera to your laptop. But you can buy a long extension inexpensively.

The rest of the setup is very straightforward:

Connect the Brundlefly to the facilitator’s laptop via USB.

Open something like AmCap (on a PC) or QuickTime Player (on a Mac) to display the view from the Brundlefly. The facilitator will watch this view.

Share the laptop screen with the observers using screen sharing (GoToMeeting, WebEx, etc.)

Run a screen recorder (e.g., Camtasia) on the computer in the observation room. This reduces the burden on the facilitator’s laptop.

## That’s it.

## Finally...

In one form or another, it seems clear that mobile is where we’re going to live in the future, and it provides enormous opportunities to create great user experiences and usable things. New technologies and form factors are going to be introduced all the time, some of them involving dramatically different ways of interacting.<sup>8</sup>

<sup>8</sup> Personally, I think talking to your computer is going to be one of the next big things. Recognition accuracy is already amazing; we just need to find ways for people to talk to their devices without looking, sounding, and feeling foolish. Someone who’s seriously working on the problems should give me a call; I’ve been using speech recognition software for 15 years, and I have a lot of thoughts about why it hasn’t caught on.

Just make sure that usability isn’t being lost in the shuffle. And the best way to do this is by testing.

# Chapter 11. Usability as common courtesy

WHY YOUR WEB SITE SHOULD BE A MENSCH<sup>1</sup>

<sup>1</sup> Mensch: a German-derived Yiddish word originally meaning “human being.” A person of integrity and honor; “a stand-up guy”; someone who does the right thing.

Sincerity: that’s the hard part. If you can fake that, the rest is easy.

—OLD JOKE ABOUT A HOLLYWOOD AGENT

Some time ago, I was booked on a flight to Denver. As it happened, the date of my flight also turned out to be the deadline for collective bargaining between the airline I was booked on and one of its unions.

Concerned, I did what anyone would do: (a) Start checking Google News every hour to see if a deal had been reached, and (b) visit the airline’s Web site to see what they were saying about it.

I was shocked to discover that not only was there nothing about the impending strike on the airline’s Home page, but there wasn’t a word about it to be found anywhere on the entire site. I searched. I browsed. I scrolled through all of their FAQ lists. Nothing but business as usual. “Strike? What strike?”

Now, on the morning of a potential airline strike, you have to know that there’s really only one frequently asked question related to the site, and it’s being asked by hundreds of thousands of people who hold tickets for the coming week: What’s going to happen to me?

I might have expected to find an entire FAQ list dedicated to the topic:

Is there really going to be a strike?

What’s the current status of the talks?

If there is a strike, what will happen?

How will I be able to rebook my flight?

What will you do to help me?

## Nothing.

What was I to take away from this?

Either (a) the airline had no procedure for updating their Home page for special circumstances, (b) for some legal or business reason they didn’t want to admit that there might be a strike, (c) it hadn’t occurred to them that people might be interested, or (d) they just couldn’t be bothered.

No matter what the real reason was, they did an outstanding job of depleting my goodwill towards both the airline and their Web site. Their brand—which they spend hundreds of millions of dollars a year polishing—had definitely lost some of its luster for me.

Most of this book has been about building clarity into Web sites: making sure that users can understand what it is they’re looking at—and how to use it—without undue effort. Is it clear to people? Do they “get it”?

But there’s another important component to usability: doing the right thing—being considerate of the user. Besides “Is my site clear?” you also need to be asking, “Does my site behave like a

## mensch?”

## The reservoir of goodwill

I’ve always found it useful to imagine that every time we enter a Web site, we start out with a reservoir of goodwill. Each problem we encounter on the site lowers the level of that reservoir. Here, for example, is what my visit to the airline site might have looked like:

![](images/a8f4124fa6e17e87f826475abf81c4eacb2969da6a73c2d6eb773ff63aa74fb8.jpg)

I enter the site.

My goodwill is a little low, because I’m not happy that their negotiations may seriously inconvenience me.

![](images/31fefb9731d2bdd6f985cc1b32088031ed75e0fb96ef13f5fa82a52831d23b99.jpg)

I glance around the Home page.

It feels well organized, so I relax a little. I’m confident that if the information is here, I’ll be able to find it.

![](images/3d7bfe93a20cd01ce688a64bb799c71da8f2e99de5537ea82b5e8d35d331e524.jpg)

There’s no mention of the strike on the Home page.   
I don’t like the fact that it feels like business as usual.

![](images/93bd3c4de1924ec9d93569e34e6871b43988fbdf2128e174dcfebe4c6dd42931.jpg)

There’s a list of five links to News stories on the Home page but none are relevant. I click on the Press Releases link at the bottom of the list.

![](images/c9f53ae451cc764ce067627824a487002738205c63e2774c1f9439cdb7a306d1.jpg)

Latest press release is five days old. I go to the About Us page.

![](images/8a146f4428731448ef711a8c762e008e13cc1bd3fa3ad5d2a82f85b4fed73dfa.jpg)

No promising links, but plenty of promotions, which is very annoying. Why are they trying to

sell me more tickets when I’m not sure they’re going to fly me tomorrow?

![](images/7e17742a4d6dd23ab1cc17f12494d3dca2bdb101a7ab0ec1a1c113449d26e4a9.jpg)

I search for “strike” and find two press releases about a strike a year ago and pages from the corporate history about a strike in the 1950s.

At this point, I would like to leave, but they’re the sole source for this information.

![](images/5677343c2540100995ea2ecdda231968f211f1985ba654e3e785d880bb293fcc.jpg)

I look through their FAQ lists, then leave.

The reservoir is limited, and if you treat users badly enough and exhaust it there’s a good chance that they’ll leave. But leaving isn’t the only possible negative outcome; they may not be as eager to use your site in the future, or they may think less of your organization and savage you on Facebook or Twitter. For those of you in marketing, your NPS (Net Promoter Score) probably goes down.

There are a few things worth noting about this reservoir:

It’s idiosyncratic. Some people have a large reservoir, some small. Some people are more suspicious by nature, or more ornery; others are inherently more patient, trusting, or optimistic. The point is, you can’t count on a very large reserve.

![](images/6a31bdacbea896b8ba02df5a6547de59ad7fd4eebe09d27e66cd9c5660a35569.jpg)

It’s situational. If I’m in a huge hurry, or have just come from a bad experience on another site, my expendable goodwill may already be low when I enter your site, even if I naturally have a large reserve.

![](images/20afd8ce7be3ab76424fea3f9b1ca693204f83751a9f606fb474b8fb58bd2353.jpg)

You can refill it. Even if you’ve made mistakes that have diminished my goodwill, you can replenish it by doing things that make me feel like you’re looking out for my best interests.

![](images/1de5de7cf2d40d7aa7000eac388609b46aeff78fc2530ab9939543eb6746dde0.jpg)

Sometimes a single mistake can empty it. For instance, just opening up a registration form with tons of fields may be enough to cause some people’s reserve to plunge instantly to zero.

![](images/4e7c3912cf7898ad7d6801ec18f9c99173f4049ebc900f0d064f167431fc5a2e.jpg)

![](images/fd803e7898f8aca2ac95315d33679e2dfee724ebb3d501c4d0dcc89d4958c9ad.jpg)

![](images/a24b07f8fddb43a6d48b9b6573727bfe169f15edaea2ae029fd880b37c6fd1c6.jpg)

![](images/d58eb70173c2d805bb350813bd485dc02855c834fe22f621d5a8e455ae4a9d84.jpg)

## Things that diminish goodwill

Here are a few of the things that tend to make users feel like the people publishing a site don’t have their best interests at heart:

Hiding information that I want. The most common things to hide are customer support

phone numbers, shipping rates, and prices.

The whole point of hiding support phone numbers is to try to keep users from calling, because each call costs money. The usual effect is to diminish goodwill and ensure that they’ll be even more annoyed when they do find the number and call. On the other hand, if the 800 number is in plain sight—perhaps even on every page—somehow knowing that they can call if they want to is often enough to keep people looking for the information on the site longer, increasing the chances that they’ll solve the problem themselves.

Some sites hide pricing information in hopes of getting users so far into the process that they’ll feel vested in it by the time they experience the sticker shock. My favorite example is Web sites for wireless access in public places like airports. Having seen a “Wireless access available!” sign and knowing that it’s free at some airports, you open up your laptop, find a signal, and try to connect. But then you have to scan, read, and click your way through three pages, following links like “Wireless Access” and “Click here to connect” before you get to a page that even hints at what it might cost you. It feels like an old phone sales tactic: If they can just keep you on the line long enough and keep throwing more of their marketing pitch at you, maybe they can convince you along the way.

Punishing me for not doing things your way. I should never have to think about

formatting data: whether or not to put dashes in my Social Security number, spaces in my credit card number, or parentheses in my phone number. Many sites perversely insist on no spaces in credit card numbers, when the spaces actually make it much easier to type the number correctly. Don’t make me jump through hoops just because you don’t want to write a little bit of code.

→ Asking me for information you don’t really need. Most users are very skeptical of

requests for personal information and find it annoying if a site asks for more than what’s needed for the task at hand.

![](images/d97ea1cac16fbfb56ec7801f7a935736aa91a42f3f011b18a6528adc080c4e30.jpg)

→ Shucking and jiving me. We’re always on the lookout for faux sincerity, and

disingenuous attempts to convince me that you care about me can be particularly annoying. Think about what goes through your head every time you hear “Your call is important to us.”

Putting sizzle in my way. Having to wade through pages bloated with feel-good

marketing photos makes it clear that you don’t understand—or care—that I’m in a hurry.

Your site looks amateurish. You can lose goodwill if your site looks sloppy,

disorganized, or unprofessional, like no effort has gone into making it presentable.

Note that while people love to make comments about the appearance of sites—especially about whether they like the colors—almost no one is going to leave a site just because it doesn’t look great. (I tell people to ignore all comments that users make about colors during a user test, unless three out of four people use a word like “puke” to describe the color scheme. Then it’s worth rethinking.<sup>2</sup>)

<sup>2</sup> This actually happened once during a round of testing I facilitated. We changed the color.

There may be times when you’ll choose to have your site do some of these user-unfriendly things deliberately. Sometimes it makes business sense not to do exactly what the customer wants. For instance, uninvited pop-ups almost always annoy people to some extent. But if your statistics show you can get 10 percent more revenue by using pop-ups and you think it’s worth annoying your users, you can do it. It’s a business decision. Just be sure you do it in an informed way, rather than inadvertently.

## Things that increase goodwill

The good news is that even if you make mistakes, it’s possible to restore my goodwill by doing things that convince me that you do have my interests at heart. Most of these are just the flip side of the other list:

Know the main things that people want to do on your site and make them obvious

and easy. It’s usually not hard to figure out what people want to do on a given Web site. I find that even people who disagree about everything else about their organization’s site almost always give me the same answer when I ask them, “What are the three main things your users want to do?” The problem is, making those things easy doesn’t always become the top priority it should be. (If most people are coming to your site to apply for a mortgage, nothing should get in the way of making it dead easy to apply for a mortgage.)

Tell me what I want to know. Be upfront about things like shipping costs, hotel daily

parking fees, service outages—anything you’d rather not be upfront about. You may lose points if your shipping rates are higher than I’d like, but you’ll often gain enough points for candor and for making it easy for me to compensate for the price difference.

Save me steps wherever you can. For instance, instead of giving me the shipping

company’s tracking number for my purchase, put a link in my email receipt that opens their site and submits my tracking number when I click it. (As usual, Amazon was the first site to do this for me.)

Put effort into it. My favorite example is the HP technical support site, where it seems

like an enormous amount of work has gone into (a) generating the information I need to solve my problems, (b) making sure that it’s accurate and useful, (c) presenting it clearly, and (d) organizing it so I can find it. I’ve had a lot of HP printers, and in almost every case where I’ve had a problem I’ve been able to solve it on my own. As a result, I keep buying HP printers.

## Know what questions I’m likely to have, and answer them. Frequently Asked

Questions lists are enormously valuable, especially if

They really are FAQs, not marketing pitches masquerading as FAQs (also known as QWWPWAs: Questions We Wish People Would Ask).

You keep them up to date. Customer Service and Technical Support can easily give you a list of this week’s five most frequently asked questions. I would always put this list at the top of any site’s Support page.

They’re candid. Often people are looking in the FAQs for the answer to a question you’d rather they hadn’t asked. Candor in these situations goes a long way to increasing goodwill.

Provide me with creature comforts like printer-friendly pages. Some people love

being able to print stories that span multiple pages with a single click, and CSS makes it relatively easy to create printer-friendly pages with little additional effort. Drop the ads (the possibility of a banner ad having any impact other than being annoying is even greater when it’s just taking up space on paper), but don’t drop the illustrations, photos, and figures.

Make it easy to recover from errors. If you actually do enough user testing, you’ll be

able to spare me from many errors before they happen. But where the potential for errors is unavoidable, always provide a graceful, obvious way for me to recover.

When in doubt, apologize. Sometimes you can’t help it: You just don’t have the ability

or resources to do what the user wants (for instance, your university’s library system requires separate passwords for each of your catalog databases, so you can’t give users the single login they’d like). If you can’t do what they want, at least let them know that you know you’re inconveniencing them.

## Chapter 12. Accessibility and you

## JUST WHEN YOU THINK YOU’RE DONE, A CAT FLOATS BY WITH BUTTEREDTOAST STRAPPED TO ITS BACK

When a cat is dropped, it always lands on its feet, and when toast is dropped, it always lands with the buttered side facing down. I propose to strap buttered toast to the back of a cat; the two will hover, spinning, inches above the ground. With a giant buttered-cat array, a high-speed monorail could easily link New York with Chicago.

## —JOHN FRAZEE, IN THE JOURNAL OF IRREPRODUCIBLE RESULTS

People sometimes ask me, “What about accessibility? Isn’t that part of usability?”

And they’re right, of course. Unless you’re going to make a blanket decision that people with disabilities aren’t part of your audience, you really can’t say your site is usable unless it’s accessible.

At this point, everyone involved in Web design knows at least a little bit about Web accessibility. And yet almost every site I go to still fails my three-second accessibility test—increasing the size of the type.<sup>1</sup>

<sup>1</sup> If you’re about to send me email reminding me that Zoom has replaced Text Size in most browsers, thanks, but you can save those keystrokes. Every site gets larger if you use Zoom, but only sites that have moved beyond fixed-size fonts (usually a good indicator of effort to make things accessible) respond to Text Size.

Before  
![](images/7c245c76b99738b5388d43e76899368322da4206f80ac3e76860dfd49c14aadf.jpg)

![](images/bdf9e21f08a3eca94d700d341d1d391ea2af97a2b26cad029ce92764fb6b0826.jpg)  
After (no difference)

## Why is that?

## What developers and designers hear

In most organizations, the people who end up being responsible for doing something about accessibility are the people who actually build the thing: the designers and the developers. When they try to learn about what they should do, whatever books or articles they pick up inevitably list the same set of reasons why they need to make their sites accessible:

![](images/3d93e8fe33db63cf34f3c1b650d4db2146d62efa6c5f3cbdfaf5b7cd4dc3483d.jpg)

The speech bubbles read, “It makes good business sense. People with disabilities use the Web, and they have lots of money to spend,” “Everyone should have the same opportunities and equal access to information,” “Most accessibility adaptations benefit everyone, not just people with disabilities,” “It’s a huge potential market. 65% of the population has a disability,” and “Section 508: It’s not just a good idea; it’s the law.”

There’s a lot of truth in all of these. Unfortunately, there’s also a lot that’s unlikely to convince 22-year-old developers and designers that they should be “doing accessibility.” Two arguments in particular tend to make them skeptical:

■ % of the population has a disability. Since their world consists largely of able-bodied 22-year-olds, it’s very hard for them to believe that a large percentage of the population actually needs help accessing the Web. They’re willing to write it off as the kind of exaggeration that people make when they’re advocating for a worthy cause, but there’s also a natural inclination to think, “If one of their claims is so clearly untrue, I’m entitled to be skeptical about the rest.”

Making things more accessible benefits everyone. They know that some adaptations do, like the classic example, closed captioning, which does often come in handy for people who can hear.<sup>2</sup> But since this always seems to be the only example cited, it feels a little like arguing that the space program was worthwhile because it gave us Tang.<sup>3</sup> It’s much easier for developers and designers to imagine cases where accessibility adaptations are likely to make things worse for “everyone else.”

<sup>2</sup> Melanie and I often use it when watching British films, for instance.

<sup>3</sup> A powdered orange-flavored breakfast drink, invented for the astronauts (see also: freeze-dried food).

The worst thing about this skepticism is that it obscures the fact that there’s really only one reason that’s important:

It’s the right thing to do. And not just the right thing; it’s profoundly the right thing to do, because the one argument for accessibility that doesn’t get made nearly often enough is how extraordinarily better it makes some people’s lives. Personally, I don’t think anyone should need more than this one example: Blind people with access to a computer can now read almost any newspaper or magazine on their own. Imagine that.

How many opportunities do we have to dramatically improve people’s lives just by doing our job

