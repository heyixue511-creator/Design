# C h ap t e r 5

# Welcome Experience

The first thing your customers see when they download and open your app is the welcome mat you roll out for them. Unfortunately, this welcome mat commonly contains unfriendly impediments to progress and engagement: End User License Agreements (EULAs), disclaimers, and sign-up forms. Like the overzealous zombie cross-breeds between lawyers and customs agents, these antipatterns require multiple forms to be filled out in triplicate, while keeping the customers from enjoying the app they have so laboriously invested time and flash memory space to download. This chapter exposes the culprits and suggests a few friendlier welcome strategies that keep the lawyer-custom agent crossbreed zombies at bay.

## 5. 1 Antipattern: End User License Agreements (EUL As)

When customers open a mobile website, they can often engage immediately. Ironically, the same information accessed through apps frequently requires agreeing to various EULAs, often accompanied by ingenious strategies that force customers to slow down. EULAs are antipatterns.

## W hen and W here It Shows Up

EULAs are typically shown to the customer when the application is first launched and before the person can use the app. Unfortunately, when they do show up, EULAs are also frequently accompanied by various interface devices designed to slow people down. Some EULAs require people to scroll or paginate to the end of a 20-page document of incomprehensible lawyer-speak before they allow access. Others purposefully slow people down with confirmation screens that require extra taps. Truly, things have evolved nicely since the days of medieval tortures!

## Example

Financial giant Chase provides a good example of a EULA. As shown in Figure 5.1, when customers first download the Chase app, they are faced with having to accept a EULA even before they can log in.

![](images/18833cfd237a8d572a1e5dbec96bd286b3c4d7db795b2b5edb2847d6bb2f6c2d.jpg)

What makes this example interesting is that the same information is accessible on the mobile phone without needing to accept the EULA first: through the mobile web browser, as shown in Figure 5.2.

![](images/2bc6d18dead5d14013af973bdaa74c41c7230839991c737e993323d610d0aa04.jpg)  
Figure 5.2: There is no EULA on the Chase mobile website.

## W hy Avoid It

The remarkable thing is not that the EULA is required. Lawyers want to eat, too, so the EULAs are an important component of today’s litigious society. Dealing with a firstworld bank in the “New Normal” pretty much guarantees that you’ll be faced with signing some sort of a legal agreement at some point in the relationship. The issue is not the EULA itself—it is the thoughtlessness of the timing of the EULA’s appearance.

The app has no idea if you have turned mobile access on or have your password set up properly. (Most people have at least a few issues with this.) Therefore, the app has no idea if the bank can serve you on this device. However, already, the bank managed to warn you that doing business on the mobile device is dangerous and foolhardy and, should you choose to be reckless enough to continue, the bank thereby has no reasonable choice but to relinquish any and all responsibility for the future of your money. This is hardly an excellent way to start a mature brand relationship.

What should happen instead? Well, the mobile website provides a clue. First, it shows what the user can do without logging in, such as finding a local branch or an ATM. Next, the mobile site enables the customer to log in. Then the system determines the state of the EULA that’s on file. If (to paraphrase Cream’s lyrics in “The Tales of Brave Ulysses”) the customers’ “naked ears were tortured by the EULA’s sweetly singing” at some point in the past, great—no need to repeat the sheer awesomeness of the experience. If not, well, it’s lawyer time. Consequently, if customers do not have Bill Pay turned on, for example, they don’t need to sign a Bill Pay EULA at all, now do they?

The point is that the first page customers get when they first launch your app is your welcome mat. Make sure yours actually says “Welcome.”

## Additional Considerations

Has anyone bothered asking, “How many relationships (that end well) begin with a EULA anyway?” How would your use of the Internet feel if every website you navigate to first asks you to agree to a EULA, even before you could see what the site is about? That just does not happen. You navigate to a website and see engaging welcome content immediately. (Otherwise, you’d be out of there before you could spell E-U-L-A.) When you use a site to purchase something, you get a simple Agree and Proceed button with a nearby link to a EULA agreement (not that anyone ever reads those things anyway) and merely proceed on your way.

If you can surf the web happily, taking for granted the magnificence of the smorgasbord of information on the mobile and desktop, without ever giving a second thought to the EULAs, why do you need to tolerate a welcome mat of thoughtless invasive agreements on the world’s fastest growing platform?

## Related Patterns

5.2 Antipattern: Contact Us Impediments

![](images/82ffe7e0f31e16c05a71f09b51b7cc049e878ba47f95820b4c475ef179e0af88.jpg)

## 5. 2 Antipattern: Contact Us Impediments

Whenever things go wrong, your customers need to contact support. Including impediments such as untappable phone numbers and long contact forms without presets is a User Experience (UX) antipattern.

## W hen and W here It Shows Up

This antipattern is unfortunately quite common because it takes time and effort to mobilize the customer support contact mechanisms. These often get left behind when desktop web applications are converted into mobile apps.

## Example

In the US Bank app shown in Figure 5.3, things went wrong during the initial registration. At this point in the flow, customers are completely stuck. There is literally no self-service possible—customers must call customer support. So the app notifies customers of the error by a pop-up alert, asking them to call the number shown. Unfortunately, the phone number is not tappable. Nor is it possible to copy the phone number. In other words, customers are forced to either remember the phone number they need to dial or else they need to get a piece of paper and write down the number. Don’t forget that the device your customers hold is also a phone. Forcing customers to write down the number they need to call while they are on the mobile phone already is an egregious failure of service—you might as well ask them to chisel it on a little stone pyramid or write it in plant pigment on the walls of their cave.

![](images/33a6d83755368afe981c8f3b44a497d4c6ad9f0a94d7daa1c77e5cb2dc50f65d.jpg)  
Figure 5.3: When things go wrong during registration in the US Bank app, the customer experiences the Contact Us Impediments antipattern.

However, you can argue that a simple act of having to write down a phone number simply pales in comparison with sin #2: long Contact Us forms that are devoid of any presets. The example in Figure 5.4 is courtesy of Kodak.

![](images/9338c69f06a87c82a7323ec5dfad328e32515b214e2b16233aacf740cac5834b.jpg)  
Figure 5.4: The Contact Us Impediments antipattern is expressed as a long form in the Kodak app.

Yes, sure, I’d like more information about your product. But no thank you; I will not fill out a helpful form that has more fields than an average mobile customer fills out in a week.

## W hy Avoid It

At the point the customer needs to seek technical assistance, she is already unrecoverably stuck, which means that she is already frustrated with your app, your company, and your brand. Throwing up impediments and barriers to contacting the people she needs to get to simply does not make sense—it’s an antipattern.

## Additional Considerations

Frequently, I hear from my consulting clients the argument that allowing their customers to contact tech support by phone is just too costly. On the other hand, these companies need to allow access to the phone number or e-mail address to enable their customers to recover in cases where they cannot do so simply using the online help. So the companies compromise by giving a number but making it difficult to dial with the single-tap action the phone makes so easy—in other words, the companies create Contact Us Impediments. This is a false economy. Do not forget that the smartphone is also a phone and an e-mail client. If the customer is forced to do something unnatural with these simple calls to action when she is in trouble and needs help, your brand will be damaged in significant ways, and the customer will be that much harder to deal with when she finally calls your 800 number after she manages to write it down. If you don’t want your customers calling you, simply do not provide a number.

## Related Patterns

9.2 Antipattern: Lack of Interface Efficiency

![](images/a2cd0d54c2109d6961a45893a7e6fc5aca54b996cea93410b43696a88254d4df.jpg)

## 5. 3 Antipattern: Sign Up/Sign In

I hope by now you are getting my drift: Anything that slows down customers or gets in their way after they download the app is a bad thing. That includes sign-up/ sign-in forms that show up even before potential customers can figure out if the app is actually worth using.

## W hen and W here It Shows Up

This antipattern seems to be going away more and more as companies are beginning to figure out the following simple equation:

Long sign-up form before you can use the app = Delete app

However, a fair number of apps still force customers to sign up, sign in, or perform some other useless action before they can use the app.

## Example

The application SitOrSquat is a brilliant little piece of social engineering software that enables people to find bathrooms on the go, when they gotta go. Obviously, the basic use case implies, shall we say, a certain sense of urgency. This urgency is all but unfelt by the company that acquired the app, Procter and Gamble (P&G), as it would appear for the express purposes of marketing the Charmin brand of toilet paper. (It’s truly a match made in heaven—but I digress.)

Not content with the business of simply “Squeezing the Charmin” (that is, simple advertising), P&G executives decided for some unfathomable reason to force people to sign up for the app in multiple ways. First, as you can see in Figure 5.5, the app forces the customer (who is urgently looking for a place to relieve himself, let’s not forget) to use the awkward picker control to select his birthday to allegedly find out if he has been “potty trained.” This requirement would be torture on a normal day, but—I think you’ll agree—it’s excruciating when you really gotta go.

But the fun does not stop there—if (and only if) the customer manages to use the picker to select the month and year of his birth correctly (and how, exactly, does the app know the customer has selected correctly?) he then sees the EULA, which, as discussed earlier in the chapter, is an antipattern all to itself. The EULA is long, complex, and written in such tiny font that reading it while waiting to go to the bathroom should be considered an Olympic sport, to be performed only once every 4 years. Assuming the customer gets through the EULA, P&G presents yet another sign-up screen, offering the user the option to sign in with Facebook. I guess no one told the P&G execs that the Twitter message “pooping” is actually a prank. They must have legitimately thought that they could transfer some sort of social engineering information about the person’s bathroom habits to “achieve and maintain synergistic Facebook connectivity.” I would have to struggle hard to find monumental absurdities from social networking experiments that are equal to this. I can’t imagine that anyone thinks, “Finally! Sharing my bathroom habits on Facebook has never been easier!”

![](images/2cb6acc92fdfe6296589224cebda96d8ec8e8b25ba97c3ff323eaf9752c64833.jpg)

![](images/7e6da36bcda0d839752e9880875baf822e55d57836f1225fa2c5df6ba9f11b58.jpg)  
Figure 5.5: This registration failure is a Sign Up/Sign In antipattern in the SitOrSquat app.

Assuming that the user is a legitimate customer looking to use the bathroom for its intended purpose, and not a coprophiliac Facebook exhibitionist, the assumption is that he will naturally dismiss the Facebook sign-in screen and come to the next jewel: the tutorial. Note that the entire app outside of registration consists of basically four screens if you count the functionality to add bathrooms. However, if you include all the sign-up antipattern screens (including my initial failure to prove that my potty training certificate is up to date, as referred to in Figure 5.5), it takes seven screens of the preliminary garbage before the content you are looking for finally shows up (see Figure 5.6). If you count the number of taps necessary to enter my birthday, there are almost 50 taps!

One of my favorite UX people, Tamara Adlin (who is coauthor of The Persona Lifecycle: Keeping People in Mind During Product Design with John Pruitt, 2006, Morgan Kaufmann) wrote brilliantly: “For Heaven’s Sakes, Let Them Pee.” I believe that never before has this line been so appropriate. In the absurd pursuit of social media “exposure” coupled with endless sign-up screens, and heavyhanded “lawyering up,” P&G executives completely lost sight of the primary use case: letting their customer SitOrSquat.

![](images/0e66dc300ffe944ac72045f929d51da19cb9af8e5c02cd3b6c01155af410c26d.jpg)  
Figure 5.6: Behold the glory of the Complete Sign Up/Sign In antipattern in the SitOrSquat app.

## W hy Avoid It

Long sign-up screens detract from the key mobile use case: quick, simple information access on the go. Overly invasive sign-up/sign-in screens presented up front and without due cause can cause your customers to delete the app.

## Additional Considerations

When deciding whether to force the customer to perform an action, consider this: If this were a web app, would you force the customer to do this? If you have an Internet connection, you can save everything the customer does and connect it back to his device using a simple session token and a guest account. And even if you don’t (for example, while riding in a subway, using airplane mode, and so on), today’s smartphones have plenty of on-board storage you can use for later syncing with your servers when the mobile network eventually becomes available.

This means there is simply no reason to force anyone to register for anything, other than if they want to share the data from their phone with other devices. As a general rule, rather than forcing registration upon download or at the first opportunity, it is much better to allow the customer to save a piece of information locally on the phone without requiring that he log in. Wait until the customer asks for something that requires registration, such as sharing the information with another device or accessing information already saved in his account; at that point completing the registration makes perfect sense.

For example, imagine how absurd the Amazon.com shopping experience would be if the app asked you for your home address, billing address, and credit card upfront— before allowing you to see a single item for sale! Yet entering the home address (where would you like to have the items shipped?) and credit card (how would you like to pay for this?) makes perfect sense during the checkout, after the customer selects a few items and indicates she would like to complete the purchase.

Finally, as Luke Wroblewski quipped in his book Web Form Design (Rosenfeld Media, 2008), “Forms suck.” Only ask for what you strictly need to proceed to the next step and omit extraneous information. (Read more detail on this topic in Chapters 10 through 12.)

## Related Patterns

## None

## 5. 4 Pattern: W elcome Animation

Welcome animation is a prominent feature on iPhone; however, it’s all but missing on the Android platform. As Reel 2 Real sang in a (very) animated film Madagascar, it’s time to “Move it, move it.”

## H ow It W orks

When the customer first opens the app, a small animation clip plays to welcome the customer and show off the brand. Often this is done tongue-in-cheek, with a bit of light humor.

## Example

Android boot animations are often lavish and spectacular affairs, such as the one for the Galaxy Nexus Ice Cream Sandwich OS, as shown in Figure 5.7.

![](images/275f0efc23eccc40a53ea67654b3780afb68e9775597ceb560d7143044f037ca.jpg)  
Figure 5.7: This lavish boot animation variant of the Welcome Animation is on the Galaxy Nexus.

However, animations for apps seem to be mostly absent on the Android, so I had to look to iPhone to provide a suitable example. One of my favorite implementations of this pattern is the Priceline app on the iPhone. (See Figure 5.8; the app does not exist on Android at the time of this writing.) You can hardly do better than having Cap’n James Tiberius Kirk punching a hole through your phone; it certainly gets your attention!

![](images/247a385eb3cbc02d82423720cb7e1ac241a587091c27beba377a994a68b564c2.jpg)  
Figure 5.8: The Priceline iPhone app includes a creative implementation of the Welcome Animation.

## W hen and W here to Use It

Apps that have longer startup times can use a Welcome Animation to help occupy people while they wait for the app to load. However, as startup times become shorter, this pattern is used more for effect and branding purposes, and it runs only once when the app is installed.

## W hy Use It

Smartphones are used to have fun, play games, and accomplish serious tasks. (Once in a while, people even use them for making a phone call.) A Welcome Animation is a way to set the atmosphere for a fun experience, not only for games, but also for serious apps. A Welcome Animation is also an excellent way to pass the time when you have a slow transition.

## Other Uses

One of the best ways to use the Welcome Animation is to tell a story. The best apps create a story that is integrated as a tutorial at the same time (see the “Tutorial” section for examples).

## Pet Shop Application

Welcome to the Pet Shop application! This important section is a homage to the Java Pet Store, the original reference application for the Java 2 Enterprise Edition (J2EE) platform created by Connie Weiss and Greg Murray (http://en.wikipedia.org/wiki/ Java\_BluePrints). Thousands of people (including the author) learned how to program in Java by looking at the code patterns in the Java Pet Store. Throughout this book, I follow a similar format, presenting various Android patterns using hand-sketched sticky-note wireframes.

Ironically, I’m starting with the section that does not have a wireframe. Why not? Two reasons: First, it’s easy to imagine a snazzy Welcome Animation of happy cartoony dogs or cats running or jumping around the screen, so you don’t really need to draw a wireframe for it. Second, actually drawing a Welcome Animation in the production-ready format is just a bit beyond the drawing capabilities of most people (including yours truly).

Rather than presenting some spectacular welcome drawing and thereby discouraging anyone reading this book from trying to draw, I chose to omit the drawing entirely. In this book I stick to simple wireframes that anyone should be able to draw. Indeed, drawing your own wireframes and creating practical sticky-note prototypes for customer testing based on the patterns I present here is the entire point of this book.

That said, if you would like to give it a shot to see how a cartoony cat and dog Welcome Animation might look, feel free to draw one using the sticky-note methodology I outline in Chapter 4. (If you do, be sure to send it to my team at http:// androiddesignbook.com. I would love to feature it alongside our tutorials.)

## Tablet Apps

This pattern should work the same way for tablets as it does for the smaller mobile phones, just be mindful of screen resolution. You want to make sure the animation looks great and fits the screen; otherwise, it defeats the entire purpose and you are better off skipping it.

## Caution

In addition to the warning about keeping screen resolution in mind when designing for tablets, two things you should keep in mind are

1. Don’t make the animation too long—3 to 5 seconds is plenty. Anything longer than 10 seconds starts to feel too long.

2. Don’t run the animation more than once. It should run only when the app is launched, if needed. Don’t run it when switching between apps during multitasking.

## Related Patterns

5.5 Pattern: Tutorial

## 5. 5 Pattern: Tutorial

In my workshops, I am often asked about designing tutorials. Most apps don’t need one, but occasionally, apps that have nonobvious features need a little help explaining how to get the most out of the functionality.

## H ow It W orks

During the welcome experience, the customer gets a short lesson in how to use the app.

## Example

There are many spectacular examples of tutorials. One format uses a separate page that explains how the app functions. The SitOrSquat app example includes a tutorial of this type (refer to the “5.3. Antipattern: Sign Up/Sign In” section earlier in this chapter). Although this style is the easiest and cheapest to implement, “extra page” tutorials are also the most annoying and frequently unnecessary because they directly interrupt the natural flow of engagement with the app.

In contrast, the best tutorials are integrated directly into the use of the app. My favorite examples come from games such as the N.O.V.A series by Gameloft, where tutorials are so much a part of the story that they can be considered a work of art. Note the prominent “Skip” button in Figure 5.9.

When the person starts playing the game for the first time, Yelena, the virtual assistant AI comes on and asks you to “check your guidance system” by using it to turn your head and walk around. It then performs similar “guided checks” of the weapons system while giving you helpful notes in snide tones perfectly in keeping with the rich storyline of the game.

Fortunately, you don’t need to spend a million dollars or know anything about storytelling to create an integrated tutorial. All you need is a simple overlay, also called a Watermark, which is covered in more detail in Chapter 13, “Navigation.” A good example of using overlays for tutorial purposes is the Flipboard app (see

Figure 5.10), which features a simple overlay pointing to the ribbon-like window shade menu. (Read more about window shade and other implementations of the Swiss-Army-Knife navigation in Chapter 13.)  
![](images/edd035132c4407c00b771ba0903bb7e1d1e3d6c270ae1fcb028dfa82ee79b92f.jpg)  
Figure 5.9: This excellent integrated Tutorial pattern is from the game N.O.V.A.

![](images/9d09ad387aec0dd025ff275cc865bf25c0a734bb0b40bd5a39d2ddd4bc27e802.jpg)

When the page first loads, it is fully functional as is, with no additional actions needed by the customer. However, it also includes the additional Watermark, which points out the menu ribbon. If the person chooses to ignore the ribbon, well and good—she is free to engage with content instead. However, the overlay is obviously, yet unobtrusively, explaining how to get to “all the good stuff.” Voilà—an integrated Watermark Tutorial.

## hen and W here to Use It

Deciding whether to use the tutorial is easy. If any of the evaluators have a legitimate reason to be confused during user testing, go ahead and put one in. Tutorials are fairly inexpensive to create, can easily solve user frustrations, and help people feel like an expert from the get-go.

## W hy Use It

Sometimes, as in the game Myst, it’s the customer’s job to figure out the puzzles. Most of the time, however, for social media and e-commerce apps, decreasing cognitive friction is your duty as a designer. Tutorials help—use them.

## Other Uses

Another excellent application of the Tutorial pattern is repeated controls. For example, in the search results, often there are multiple nonobvious functions that the person can take on a given row, and people have trouble figuring out that multiple taps on a single result are even possible. One solution to this problem is to put several strong calls to action on each row. The problem is that this makes the interface busy because repeated controls clutter the interface with chart junk. After the initial discovery is complete and the person learns how to use the app, these controls serve no useful purpose. In this case a tutorial can help educate the customer about the available functionality. After the customer understands how to use the system, she no longer needs all the chart junk that would have otherwise been there to clutter the interface for the rest of the life of the app.

## Pet Shop Application

As described in the “Pet Shop Application” portion of the “5.4 Pattern: Welcome Animation” section, Figure 5.11 shows an example sticky-note wireframe of the row-level integrated tutorial. Note the integrated tutorial state and then, after the customer scrolls down or navigates to another page, the “after” state, without the tutorial.

![](images/1f06a422260b3c5870e5c995c33bfb907fbc8e4e3f58e7d938683124222c71a2.jpg)  
Figure 5.11: This wireframe shows a row-level integrated Tutorial in the search results of the Pet Shop app.

## Tablet Apps

This pattern applies to tablet apps the same way it does to apps on mobile phones.

## Caution

Don’t overdo it. You don’t have to explain all the functions. Including the bare minimum the person needs to survive your great app design is sufficient. Let people discover the rest on their own.

## Related Patterns

13.5 Pattern: Watermark

13.6 Pattern: Swiss-Army-Knife Navigation

5.3 Antipattern: Sign Up/Sign In