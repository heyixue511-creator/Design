C h ap t e r 2

# What Makes Android Different

For many years since its release, the Android OS has been behaving like a teenager in the grip of raging hormones. Growth has been nothing short of explosive, and the changes have been sweeping and profound. With the release of Ice Cream Sandwich, the user interface (UI) standards and design elements have changed dramatically, and the platform has matured and stabilized somewhat. Nevertheless the OS has retained its rebellious hacker DNA with unique features that are authentically Android.

## elcome to Flatland

The first thing you might notice when comparing the Android OS apps with Apple iOS is that the world of Android apps is flat. Flat are the buttons. Flat are the content areas. And flat are all the toolbars and controls. Just like the Flatland people from Rudy Rucker’s story, “Message Found in a Copy of Flatland,” Android does not “see” anything outside two dimensions. Nor does it pretend to be anything other than a pure digital artifact: a thing imagined and created, not real in any physical sense. It’s a piece of software that runs the hardware, not the other way around. And that, as far as I am concerned, is a very good thing. Why? Because dispensing with the need to make things “real” and “pretty” allows the content to shine and sets a stage for the authentic minimalist digital experience for your customers. In many ways, Android 4.0 uses a flat digital visual scheme similar to that used in Windows Modern UI, another mobile operating system that stands in sharp contrast to Apple iOS.

Compare, for example, the Android Messaging app with the iOS counterpart in Figure 2.1.

![](images/6f8b7f8d2438e4feea928a74f484ab638257276df63c3850aa470d68b681659e.jpg)  
Figure 2.1: Compare the two Messaging apps from iOS and Android 4.0.

The first thing to notice is the information density: There is a great deal more content crammed on screen in the Android app. Part of the reason is that the iOS uses the “speech bubble” representation of the message, whereas the Android app is simply listing messages in the table. Boring? For some folks, perhaps. However, Android makes no excuses and no decorations—the app is a straightforward, flat, and highly functional SMS machine. The overall visual scheme is reserved, almost corporate. Notice also the toolbars: iOS dictates that the toolbar elements have a three-dimensional quality that makes the elements seem to pop off the page. This is achieved with the gradients that help digital objects like toolbars visually approximate the physical world. In contrast, the Android toolbars, and indeed the entire page is decidedly two-dimensional and completely free from having to look like a physical object. Unabashed embrace of Flatland and “freedom from threedimensions” opens the door to creating menus that are semitransparent (see Figure 2.2) and commit fully to the “content-first” directive. (Various menu styles are covered in more detail in Chapter 13, “Navigation.”)

![](images/d42a489f04696a2e33d568ff9345e28b3fa082e89a7133ce44cef6dc5b795471.jpg)  
Figure 2.2: Compare the semitransparent menus of Android 4.0 in the Google Earth app to the physicality of iOS menus in the iPhone app.

![](images/4facef72522090f0c8e9851436b21a64c66adf30ff6661674d426c7660298a52.jpg)

The entire Android screen is built with grayscale, using just enough color to make the toolbars a bit darker, whereas the content areas mostly remain light. Color is one area in which many other mobile OSs, such as Windows Modern UI, contrast strongly with the Android Ice Cream Sandwich OS. Even though both design languages embrace the Flatland, Windows Modern UI veritably explodes with both color and interactivity, and the home screen literally “pops” with movement, as each element vibrates, flips, and slides with clever transitions and contrasting color combinations. In contrast, a typical Android screen looks compact, serious, business-like, and provides only the essentials—exactly like a typical wireframe. Even more interesting, this “flat world” scenario applies to buttons and tap-targets. Android “buttons” also have no gradients, which is the subject of the next section.

## Tap Anywhere

In the early days of using the mainframe workstations (that was a very long time ago), I remember being stumped when first seeing the message Tap Any Key to Continue. Programming was such a precise discipline, that it seemed inconceivable that any key would work. You could tap any key, but which is the best key? Is one better than the other? Of course the confusion quickly passed, and I learned to enjoy the freedom to just jam anywhere on the keyboard without having to think hard—most of the time just hitting the space bar with my thumb.

Android takes buttons to a new level. Whereas the iOS painstakingly identifies any tap-worthy element with the three-dimensional beveled button, Android simply assumes that any element on the screen is a tap target, often providing no additional clues. Compare, for example, the two message rows in the messaging app shown in Figure 2.3. The iOS implementation provides the beveled, round circular > button, whereas Android in contrast provides…absolutely nothing.

![](images/337dd5f5f747e37e20f68ba8c14abbb956c0c175078f5afcc137a55138832cdc.jpg)  
Figure 2.3: Compare table rows in Android 4.0 and iOS.

VZW FREE MSG: Your bill is ready. Your balance \$73.98 is scheduled for eCheck payment on 10/26/2012. Please visit http://mobile.vzw.com/

Yahoo! ID -

In Android 4.0 the customer must figure out that she can simply tap anywhere on the element (that is, anywhere in the row) to get more information. The initial cognitive friction for taking the action is often high, especially if the customer is transitioning from iOS or previous Android versions. However, most people figure out the new visual scheme quickly: If a customer wants more information about something, she is (usually) able to tap it (even if an element has no visual tap affordance). Android trains customers to simply “tap any key to continue.”

The Tap Anywhere visual design principle finds its ultimate expression in the typical Android buttons, which are implemented instead as “tap-worthy areas” (to borrow a favorite catch phrase from the mobile design expert and book author, Josh Clark, http://globalmoxie.com). In Figure 2.4, the iOS takes the time to make sure the buttons look and feel tappable with an elaborate combination of a prominent bevel, inner drop-shadow, and gradient.

![](images/de5d7311638bc080d4bd46f8ab42d967b05fc018b82c3ed27178b3e9051add27.jpg)  
Figure 2.4: Compare the Android tap-worthy areas to the iOS beveled buttons.

In contrast, Android commits whole-heartedly to the Tap Anywhere approach, using areas instead of buttons with just a hint of a vertical separator. This underscores the Android theme of not defining rigid visual border areas for tap targets and not wrapping touch targets with whitespace. This theme is profound because in its purest expression this means that everything on the touch screen is a touch target. For designers, this is both a challenge and an opportunity. It’s a challenge because without primary or secondary tap targets, a consumer might be justifiably confused about the tap-any-button scenario: “If you can tap anywhere, which area is the best one?” The Tap Anywhere scenario also presents a hefty challenge for designers and developers: Everything that the customer would conceivably want to touch should be responsive and do something intuitive. This book discusses how to adhere to this design principle without losing sight of your customers’ primary goals (and your development budget) in Chapters 10, “Data Entry,” and 11, “Forms.”

Tap Anywhere is also a tremendous under-exploited opportunity to introduce accelerometer gestures, multitouch gestures, and “hidden” menus that promulgate the content-forward design and promote immersive digital experiences. The myriad exciting possibilities are covered further in lucky Chapter 13, “Navigation.”

## Right-Size for Every Device

In the early days of Android, it became clear that simply porting the Apple menu model to every device would result in failure. Part of the reason was the tremendous range of different devices that were running Android: From the tiny HTC Hero, to the 7- and 10-inch tablets, to Android-enabled ski-goggles, smart homes, and in-car touch control panels—Android interfaces offer a great variety of space constraints in which customers must operate. Recall from the AutoTrader app case study in Chapter 1, “Design for Android: A Case Study,” that simply hiding every function in the navigation bar menu on the bottom of the screen as Android had done for versions 2.3 and earlier was not the answer, either, because it hid vital functions for devices that actually had the space to show them, as well as made having more than three or four contextual actions difficult (see Figure 2.5).

![](images/ed4fac64b5a2de76def77a1ecd566ee17b3cfc3578ef665b586de9a9e6235264.jpg)  
Figure 2.5: This example from the AutoTrader app demonstrates how the hardware menu functions for Android 2.3 and older hide essential functions.

To solve this problem, Android 4.0 designers used an authentic mobile solution: the overflow menu. To understand how to design for Android 4.0 and 4.1, it is essential to understand how this menu works. Functions are distributed to one or more menus called action bars. When the interface distributes functions along more than one action bar, the second action bar is called…get ready for it…a split action bar. An app with two action bars is shown in Figure 2.6.

Regardless of the number of bars (typically one or two: the action bar on the top and the split action bar on the bottom), the menu acts as an accordion, expanding and contracting with the available screen real estate. Smaller screens get only a few essential functions. Larger screens such as in tablets get the entire available menu, with a bias toward having only a single action bar. Additional functions that do not fit on the action bars end up in the overflow menu, which is an excellent, highly scalable, mobile solution to the problem of limited real estate. Figure 2.7 shows a comparison of menus on a tablet (top) and a phone (bottom).

![](images/683fb9f168c39be4d78d48c7aad2feabe1381b6e571b2cc0af44e7c9f53c0c32.jpg)

## Silicon Valley Entrepreneurs &Nov 15

You're invited to Friday Party & Mixer - SF -★ [image: Meetup] New Meetup Friday Party &

## Silicon Valley Entrepreneurs &Nov 15

You're invited to Friday Party & Mixer - SF —★ [image: Meetup] New Meetup Friday Party &

## Mobile Internet Forum - HTM... Nov 15

You're invited to iOS Monthly Meetup — [image: Meetup] New Meetup iOS Monthly

## »Silicon Valley iOS Developers Nov 15

You're invited to iOS November Meetup — [image: Meetup] New Meetup iOS November

## Silicon Valley Entrepreneurs & Nov 15

You're invited to Friday Party & Mixer - SF —★ [image: Meetup] New Meetup Friday Party &

## Mobile Internet Forum - HTM... Nov 15

You're invited to iOS Monthly Meetup — [image: Meetup] New Meetup iOS Monthly

![](images/85f70c83efc0f796f5a012f75970068ca57ccff7ec66f786731df6077933401d.jpg)  
Figure 2.6: The Gmail app has an action bar at the top and a split action bar at the bottom.

![](images/5ef7e6f33fe76ef207f10e90c89ed38cbbf26fe983af823fc71b12d1088ff447.jpg)  
Figure 2.7: In the Gmail app on smaller screens, extra functions move to the overflow menu.

In stark contrast to iOS and older Android menus, the action bars, as a rule, use only icons, whereas the overflow menus use only text. Icons and words together are still used in Android 4.0—for example, in places such as some Cancel/OK action buttons and in the Drawer menu in Google Plus, as shown in Figure 2.8.

![](images/8e91e61c71362edc9c7474cda623d484ff82c048a5314ec336d6fd223cff39ae.jpg)  
Figure 2.8: The Google Plus app uses icons and text in the Drawer menu.

Action bars combined with the overflow menu usually enable the Android to work reasonably well on a majority of screens and device orientations. However, not all resulting UIs are ergonomically desirable: Specific device constraints are discussed in the next chapter. Chapter 13 discusses how to make the most of this pattern using the “hidden” menus and active corners in Swiss-Army-Knife Navigation, and Chapter 8, “Sorting and Filtering,” shows you different menu

approaches for essential functions like Search. Discover how to design effective 7- and 10-inch tablet UIs in Chapter 14, “Tablet Patterns.”

## M obile Space, Unbound

One important corollary to the principles of Tap Anywhere and Right-Size for Every Device is the unabashed removal from the interface of containers of any kind, in stark contrast to iOS, which typically features multiple containers with rounded corners, as shown in Figure 2.9.

![](images/eada4a4091424cee4e1211744e70c80b713fe20e2d63862ad09dc57d1175cd35.jpg)  
Figure 2.9: The iOS Settings app demonstrates emphasis in iOS on UI containers.

Many designers point out that the defining features of the Windows Modern UI (see Figure 2.10) are the multicolored square containers, called tiles, as well as the unifying backgrounds and sweeping headers in the Panorama controls (read more about those in Chapter 13).

![](images/cc3ddcb75bd189026ec8f93de9589753b06302575c1fc73126c41984ecda533c.jpg)  
Figure 2.10: Windows Modern UI Settings app demonstrates the sweeping backgrounds and titles in a Panorama control.

In contrast to both iOS and Windows Modern UI, one of the signature features of Android 4.0 are the simple headers that completely dispense with containers. Instead of containers, when separation of the UI elements’ sections is necessary, Android 4.0 OS uses the contrasting colored headers, executed in uppercase Roboto font and underlined with a horizontal divider, as shown in Figure 2.11.

This general absence of containers promotes flow of the forms and uses every pixel to emphasize the content. The absence of containers also helps the UI look great on a variety of devices, regardless of the width and height of the screen.

Containers behave best when they are smaller than the size of the screen; in other words, the screen shows more than one container. For this reason, containers in iOS often behave awkwardly when the device is positioned in the horizontal orientation. This is a special consideration for Android because, as discussed earlier, Right-Size for Every Device means that the interface must work for every screen, no matter how small or strangely proportioned (within reason of course). Thus containers as an interface principle do not work well because they cannot be adjusted dynamically for every situation. Instead, the content flows free, unbound, and adjusts appropriately to the size of the screen.

![](images/c222f09ca06cbbfb155ac44f7b51656905b8d1ccb55434589e5e11ab6e6273ed.jpg)  
Figure 2.11: The Android 4.0 Settings screen uses simple headers instead of containers to promote page flow.

Unfortunately, nothing on the mobile platform comes free, and the absence of containers is no exception. Although form flow is enhanced, the absence of containers places an extra burden on vertical spacing to help separate the form fields from one another. On smaller devices sometimes this can be difficult, resulting in the forms that simply seem to go on forever without any idea where the person is at any given moment. The other issue is the minimalist color treatment. In the Settings screen, the headers are rendered in light gray, which is similar to the color of the links. In other native apps like Calendar, the headers are colored in the same way as the active fields; Both are light blue. Either treatment can cause confusion because it is not clear which are the active tappable fields and which are the headers. Using a header color that is visually distinct from both the active links and active fields is a good basic usability practice and usually helps resolve the confusion.

## Think Globally, Act Locally

One of the most interesting and brave principles of the new Android 4.0/4.1 design scheme is the local-actions-first principle. Practically all other OSes on the market, including the older Android OS versions, take special care to make global navigation available throughout the app. For instance, Apple iOS does this through the prevalence of the tab bar, as shown in Figure 2.12.

![](images/09940145880eca286d884e771793ec40b8ef27f85e09dac018c5f7710b6fa900.jpg)  
Figure 2.12: The Amazon.com app uses the iOS tab bar to make global navigation accessible throughout the app.

The same principle used to apply to the older, pre-Ice Cream Sandwich Android apps, such as the pre-4.0 Android Amazon.com app design, as shown in Figure 2.13.

In contrast, Android 4.0 offers the customers a brave, new world in which the actions presented to the customer are always the most appropriate ones to the task at hand.

For example, in the Mail app as shown in Figure 2.14, the key actions in the action bars on the app’s summary pane are Search, New Message, and so on, plus a few more general actions such as Settings, Help, and Send Feedback, which are hidden in the overflow menu.

![](images/925d96d5d5a8777af68d21081924345b22b93014cddaf7a0eb92edefe1a1c659.jpg)  
Figure 2.14: The Gmail app’s List view shows global actions.

Drilling down into the specific piece of mail, however, makes a dramatic change to the available actions. In Figure 2.15 instead of the top-tier menu items, such as Search and New Message, you see contextual actions such as Favorite and Reply (the star and arrow icons on the top bar), as well as commonly used Archive, Trash, and Tag (the file cabinet, trash can, and tag icons on the bottom bar).

![](images/8653acb028d2a3c9b6ccdaa794f3ad3f14482f9a618f9913a316182e6a742dba.jpg)  
Figure 2.15: The Gmail app’s detail view shows contextual actions instead of the global menu.

The more general action such as Settings, Help, and Send Feedback are still available in the bottom overflow menu, but global functions that were available in the list view are completely gone. This is important because due to the Act Locally principle, from the e-mail detail screen, it is impossible to access Search and

New Message, for example. The Act Locally principle also extends to the overflow menu: The top overflow menu is not merely an extension of the message functions but instead augments the Reply options with less frequently used functions, such as Reply All and Forward.

The Android 4.0 screen label is yet another corollary to this design principle. For example, in the iOS, the screen label tells the customers where they are and the back button often spells out where people will be going should they tap it. As in the mail app example shown in Figure 2.16, iOS Mail app uses 14 of 69 as a screen title, and the Back button displays All Mail (41).

![](images/fdb921354e28aa996b047c73d43e2e529ac89a4a3dba15e7f584c437271e7755.jpg)  
Figure 2.16: Compare the Android title header on the left with the back button and screen title in iOS on the right.

Android 4.0 offers no indication of where customers would go should they tap the back button. Instead, the entire bar is devoted to a screen label showing the subject of the e-mail—that is, where the customer is at the moment. This creates some confusion, especially among the iOS designers and customers taking on the Android design patterns. To these folks, “< + logo + label” means that the action would be going back to the destination shown on the label, in sharp contrast to the Android 4.0 where the same visual treatment means “you are at the label location” and “tapping the back button would go up a level.” Unfortunately, there is no good solution at the moment to this mental model transition, other than simply perhaps to get used to it.

If you contrast this hyper-local screen labeling with the older Android OS breadcrumb treatment, such as the one shown in Figure 2.17, you can see that the change is actually profound. The Android 4.0 OS simply ignores anything other than the hyper-local context.

Using only local functions on each of the screens is a departure from the earlier versions of the mobile technology—one that signals that Android assumes that people are no longer going to be “lost” without some global tab navigation showing them at all times where they are. Instead, Android 4.0 uses the “Think Globally, Act Locally” principle: The hyper-local actions and screen labels remove the global navigation (that used to be in the breadcrumb) from being in front of the customer. At the same time, in the back of their minds, Android 4.0 customers have to understand that to get to all the global navigation, they must press the back button one or more times.

![](images/c33eb5512e0fa43652764b14807e079276523d14554d99ce090558621e35a40c.jpg)

![](images/2abb780ce8c0bf2c1f66813d65c45873a6ab66b46d5819e032f08b51da505331.jpg)  
Figure 2.17: Compare the Android 4.0 action bar from the Photo Gallery app on the left to the Android 2.3 breadcrumb on the right.

Interestingly, this hyper-local context does not exactly fit with many apps’ best use cases. For example, Facebook is a notable exception that uses the Swiss-Army-Knife top-left navigation to make global actions universally available. Some practical design patterns for addressing this tension between global and local are covered in Chapter 13.

Now that you’ve had an overview of the general design principles that make Android 4.0 different, it’s time to dig into how these principles are implemented in a variety of devices that support Android.

C h ap t e r 3

## Android Fragmentation

Like a shrapnel grenade in the ball-bearings factory, Android fragmentation has now reached epic proportions. Here’s how to sort out what’s important and create the app User Experience (UX) design strategy that works for various device flavors.

## W hat’s Fragmentation?

According to OpenSignal, in April 2012, 6 months prior to the time this book was written, there were more than 3,997 distinct Android devices (based on a study of more than 681,900 devices: http://opensignal.com/reports/fragmentation.php). The number-one brand was Samsung, with 40-percent market penetration. HTC, SEMS, and Motorola together accounted for approximately 30 percent of the market share. Approximately 9 percent of the total devices were Samsung’s GT-i9100 (the Galaxy SII), but beyond that there is little in the way of the trend, including multiple one-offs such as the Concorde Tab (a Hungarian 10.1-inch device), the Lemon P1 (a dual SIM Indian phone), and the Energy Tablet i724 (a Spanish tablet aimed at home entertainment). For those that don’t mind the price tag, the famous Swiss watchmaker Tag Heuer released The Racer: A \$3,600 Android smartphone with "unparalleled torsional strength" built with carbon fiber and titanium elements and a shockproof rubber chassis. (I don’t know about you, but I think I’d rather fancy one—http://www.afterdawn.com/news/article.cfm/2012/03/13/ tag\_heuer\_launches\_carbon\_fiber\_android\_phone\_with\_huge\_price\_tag).

Staggering diversity did not end with devices and brands. The study found that Android OS versions are likewise varied, with only approximately 9 percent of customers using Android 4.0 or above, and approximately 76 percent of customers using Android 2.2 and 2.3. In addition, most manufacturers further customize each Android OS version in hopes of achieving market differentiation.

Screen resolution was similarly varied, presenting an almost continuous range from insanely generous 1920 n 1200 and 2040 n 1152 to a tiny and barely usable 240 n 180. And this fragmentation is likely to get worse in the near future as an even greater variety of screens and devices, such as TVs, smart refrigerators, Android ski goggles, and 3-D screens and projectors, will be hitting the market shortly.

How is a designer to deal with this staggering complexity?

## Everything Is in Time and Passes Away

with LG not far behind—at least in the United States. In Germany, the smaller and cheaper Sony phones are reigning supreme. As of the time of this writing, Sony phones are virtually unknown in the United States.

The bottom line is that if your app works on today’s top two or three models of the phones and tablets, you are generally in great shape. You don’t need to worry about what was around 6 months ago or what’s coming around the corner because it has not been invented yet! The point is not to sweat the small stuff. In other words, most of the phone models, versions, and manufacturers that are #1 today will be displaced from the top spot six months from now. Consider once-great mobile brands that today are barely remembered:

■ Palm and the Web OS

Motorola, which was swallowed by Google and quickly lost its hardware leadership

■ Nokia, which was bought out by Microsoft and all but disappeared off the face of the Earth

■ Blackberry OS, which is barely hanging on to a tiny fraction of market share with the skin of the right thumb

The important thing for design is not the latest gadget. It is a set of touch technology Android device trends, which do not change as quickly because they are based on the ergonomics of a human interacting with basic touch-screen technology. These device trends form the basic DNA of the mobile and tablet design patterns which changes slowly over time.

## Android Device Trends

When flexible screen material is popularized, with touch panels on the back of the device and other interesting near-future technology advancements, the device trends described here will change, of course. For now, the thickness and weight of the device; the cost of components; the size of the screen; and the size and flexibility of hands, fingers, and pocket sizes of modern clothing dictate the basic range of sizes of mobile devices and interactions with them. Over time it seems that the variety of touch-screen Android devices has standardized itself around five basic sizes: compact phones, full-size mobile phones, tablet-phone hybrids, small tablets, and large tablets. Much more than various screen resolutions, these classes of devices present specific design decisions and ergonomic requirements for app interaction design, as discussed in the following sections.

## Compact Phones

These are small, usually inexpensive Android devices. As of this writing, Kyocera Milano is a good example. These devices are tiny, $4 . 5 ^ { \prime \prime } \times 2 . 5 ^ { \prime \prime } ,$ with a screen of only about $1 . 8 ^ { \prime \prime } \times 2 ^ { \prime \prime } .$ . Because of this, the entire area of the device can be accessed easily with a thumb of one hand, as shown in the “hot zone” (the area most accessible when a customer uses the most common grip) on the right in Figure 3.1. Unfortunately, the tiny screen means that the hand holding the device also covers much of the bottom screen area, even while the customer is simply holding the device, which makes split action bar navigation problematic.

![](images/b52b1be0f596b7a0e64c4b50f141b6a3a4c9805ef7964e85e458e1d83039830b.jpg)  
Figure 3.1: Compact Phone Kyocera Milano is used to demonstrate the right-hand grip hot zone for the touch screen.

Note that the buttons are forced to be taller, and there is only room across the screen width for three or four buttons. This is the issue with the smaller devices that need not only to show the on-screen text and icons but also present a suitably large touch target. In fact, simply having two navigation bars on the screen would take up more than 30 percent of the screen area!

There is room for only a single action bar on the top of the screen. This top action bar can display only two or three functions accurately (only one function if a screen title is used). Because of the restricted screen real estate, creating an immersive user interface with a semitransparent Swiss-Army-Knife navigation pattern, which uses zero screen real estate for menus (so the entire screen is devoted to content) makes a lot of sense. See Chapter 13, “Navigation,” for some ideas on this topic. Be aware that the menu, when opened, will likely take over the entire screen, as will most secondary selection controls such as the picker wheel.

their on-screen counterparts. The major difference is that the screen does not enter the “extraction” mode (See the “10.7 Pattern: Free-Form Text Input and Extract” section) when the hardware keyboard is enabled. Instead, the orientation of the screen simply changes from vertical to horizontal, so the form is a bit wider. The input is then performed via the hardware keyboard, and the form navigation is done by scrolling the form using the touch screen. There is little difference between the hardware and software keyboard modes of input otherwise.

## Full-Size M obile Phones

This is the most popular size of devices on the market. At the time of this writing, a good example is the Samsung Galaxy SIII, $5 . 4 ^ { \prime \prime } \times 2 . 8 ^ { \prime \prime }$ , with a 4.8-inch diagonal screen size. The screen resolution is purposefully not mentioned. Actually, in doing mobile UX research, the way the device is used has little to do with screen resolution and more to do with the size, dimensions, and weight of the device. If the resolution is too low to display the required set of touch icons across the screen, then the behavior changes. However, for most modern devices the resolution is already adequate. Adding more pixels improves the picture and makes for great marketing campaigns that motivate people to buy a new gadget; it has little effect on the customers' behavior after they acquire it. The one distinguishing factor behind the mobile phones is that they tend to be light enough and small enough to be used one-handed. The hot zone for a full-size phone in a right-handed grip is shown in Figure 3.2.

![](images/3bbdfd08221ee8021083a8b7f05e181a4d1ed5c8ceb11f58be94583b20018d2f.jpg)

As the right-hand hot zone in Figure 3.2 shows, the bottom action bar is easily accessible, however the ergonomics of accessing the top action bar don’t quite work out: Most customers need to use their left hands to tap the controls on the top of the device or have to reposition the device and stretch their fingers awkwardly. This is especially true for women and teens, or customers with smaller hands. Another drawback of commands on top of the screen is you have to cover the screen to reach them. This is not exactly toeing the Android “Party Line” because, unfortunately, the top action bar is where the Android guidelines recommend placing most of the key functions. Indeed, that’s where the key functions reside in the majority of the Google Android apps as of the date of this writing.

In the United States, the Android phones tend to come in larger, literally pocketbursting sizes. This is partly due to the current market penetration of the Apple iOS iPhone. It helps marketing campaigns define differentiation if the Android devices have a visibly larger screen, so the full-size Android mobile phones tend to be larger than the iPhone’s 3.5-inch screen. Although this is a strong trend, larger size is not always the case. As already mentioned, in Europe slightly smaller and less expensive Android phones made by Sony are about the size of the iPhone 4. Anything smaller than the size of the iPhone 4 can safely be considered to be a compact phone and treated accordingly.

On these smaller Android phones that have the 3.5-inch screens, it is much easier to reach the top action bar; although it still requires awkward juggling. The result is that features such as the Drawer navigation in the Google Plus and Facebook apps are actually hard to reach. As discussed in Chapter 1, “Design for Android: A Case Study,” one workaround is to use the left-to-right swipe gesture to bring out the navigation drawer, as indicated by the bevel on the left side of the screen. Chapter 13 discusses using bottom corners for immersive Swiss-Army-Knife navigation that are more easily accessible than the top corners. Keep this in mind as you design your own apps. Also consider using gestures like the C-Swipe that's discussed in Chapter 14, “Tablet Patterns.” As this book is being written, these gestures are not part of the Android 4.0 guidelines, but they do work in the real world.

screen sizes that are more forgiving of fat fingers, as well as softwaredriven keyboard input improvements such as predictive text, Swype, ShapeWriter, SlideIT, and so on. You can find more information about these in the Android Forums at http://androidforums.com/android-applications/ 50081-swype-vs-slideit-vs-shapewriter.html.

## Tablet-Phone H ybrids

Tablet-phone hybrids such as the Galaxy Note are a conundrum. For most apps, visibly, there is no improvement in the screen resolution, so the person using the awkward device gets the same on-screen experience as the full-size mobile phone customer. However, bringing one of these giant hybrid phones (roughly one-inch taller and one-half an inch wider than the big full-size mobile phones) to one’s ear for making a phone call is rather awkward, to put it mildly. Yet as the success of the Galaxy Note has proven, people are actually rather interested in these devices. Part of the appeal is the larger screen that enables comfortable e-book reading and mobile web surfing.

Hybrid phone customers find that for the vast majority of tasks, the use of the device is a dedicated two-handed affair. Although it’s possible to easily hold Galaxy Note in one hand, even if you have Niccolò Paganini’s legendary long fingers, it is almost impossible to use that same hand to reach and operate the top action bar functions. As shown in the hot zone in the Figure 3.3, one hand is not enough to reach all the functions of the tablet-phone hybrid, which forces an asymmetric one-handed grip with one hand holding the device while the other hand does the tapping.

![](images/b6941cd3855263ce4cf5bcc29a38fa0ed8c3b2182b4109b0f64734ba7dc5d7df.jpg)

![](images/e816b1814f6246c921a41d79301265612edb23fed64860f0dcf9e304d7c2ad91.jpg)

Most of the apps on the device are not customized to take full advantage of the larger screen size; some apps, most notably the Calendar, offer additional features such as slide-out tabs, which are interesting interface approaches but can still be rather awkward to use. My recommendation for these devices is not to customize the native app experience unless a large percentage of the app's customers are using one of these hybrids, or you are designing a native app specifically customized for this device class.

Gesture-based menu interactions, like the slide-out drawers and C-Swipe mentioned earlier, would actually enable one-handed use because these hybrid devices are light enough and compact enough to be held comfortably in one hand. This is because the device’s center of gravity still falls comfortably within the reach of the fingers of one hand. Most of the issues of one-handed use come from the inability to reach the navigation components, not the device size or weight distribution, as is the case for true tablets.

## Small Tablets

Small tablets, such as the 7-inch Samsung Galaxy Tab 2, offer some unique use cases and challenges. Whereas all the previous devices were mostly used in a vertical (portrait) orientation, tablets are more often rotated, doubling the complexity of the interface (see Figure 3.4).

![](images/305a34d92d2242308992a3f655e8bdcfcba66f5972e321d35c47f1003973df85.jpg)

![](images/1b52776b930b034b512b9cd294efb8b37ac893e2525de790eeec1a10bed93676.jpg)

As the hot zone picture in Figure 3.5 shows, in a vertical orientation, most small tablets are held with one hand, with the second hand tapping the controls. On the other hand (literally) in the horizontal (landscape) orientation, the device is most often held in a committed two-handed grip.

![](images/844f3347df78176c041d74f5ba25b68686c33b473695009adfeb1165a5810e4d.jpg)  
Figure 3.5: Small tablets dictate different hot zones for one-handed vertical, two-handed vertical, and two handed horizon tal orientations.

Why this distinction? Holding the device in horizontal orientation in one hand is simply more difficult than holding the same device vertically in one hand. (Really, try it!) It has to do with a center of gravity of the device and where the center of gravity is located with respect to the fingers and the wrist. This is a simple physiological reality and is not likely to change any time soon: The fundamentals such as device weight, dimensions, and materials must change first.

What does all this mean from the standpoint of the interface design? There is enough space on the small tablet device to show one or more action bars comfortably. Looking at the hot zone in Figure 3.5, on small tablets in vertical orientation, the entire top and bottom action bars are easily accessible, with the top bar being slightly more so. Thus Android guidelines can be followed as-is, and there is no need for measures like immersive navigation. Swiss-Army-Knife navigation measures can lead to less satisfying experiences on tablets because they hide essential functions and force customers to learn where they are, which can cause cognitive friction. This guideline does not apply to immersive tasks such as reading and gaming, which traditionally use lights-out navigation, but to more navigation-centric tasks such as shopping.

in a state of flow, offering simple, intuitive functions and wide, sweeping gestures (such as swiping to turn the page) that come naturally with the larger touch device. The C-Swipe gesture can be used for either the hand that is holding the device, or the hand that does the tapping, but chances are that the C-Swipe will happen in the middle of the device, or near the top portion of the screen, not on the bottom as it would for a one-handed grip on the mobile phones.

Things might be a little different in the horizontal orientation, which calls for a committed two-handed grip. Most of the navigation functionality is accessed using thumbs, while the rest of the fingers rest on the back of the device. Fortunately, most of the screen surface area, (including the essential Android back button) is easily accessible with average thumbs on a small tablet with a two-handed grip. Thus again the Android guidelines can be used out-of-the-box; actually, they seem to be developed especially for small tablets!

Which is the preferred orientation? This question is difficult to answer, and most often no clear distinction can be drawn, even for specific tasks. From doing research and hours of field observations, people tend to read mostly with the device in a vertical orientation, where the interface forms a single column. On the other hand, the keyboard in vertical orientation does not offer the greatest experience—most people tend to rotate to horizontal when needing to use the keyboard-centered tasks such as filling out a form. Unfortunately, it is hard to see much of the form on a 7-inch tablet while the soft keyboard is also shown on the screen, so the entire form interaction on 7-inch tablets tends to be a rather awkward shuffling from vertical for scrolling to horizontal for typing, which is a less than ideal situation. This problem and some creative solutions are covered in detail in Chapters 10 (“Data Entry”) and 11 (“Forms”).

Another unique quality of small tablets is that they are actually small enough and light enough to be both held and manipulated with one hand, albeit with limited capability. Where you see this show up is in longer-term immersive activities such as reading. The person may want to both hold the small tablet and flip pages without using the second hand. This works well for the right-handed grip near the middle of the tablet, especially if the tablet is also partially resting on the person's lap, table, or chair arm. This is in part due to the generous margin around the touch screen, which enables the grip to be solid without touching the screen. Unfortunately, the same is not the case for the left-handed grip; most book apps flip the pages backward when they are tapped on the left side of the screen. The solution is to put controls along the left and right side of the screen or use a C-Swipe gesture to call up the menu from anywhere, as discussed in Chapter 14.

From what can be observed in the field, the entire one-handed grip-and-use approach is not the most solid use case for the Apple iPad mini. The margin around the screen is simply too small to enable a comfortable grip.

Finally, what actually defines the tablet as “small”? It is the quality of comfortable accessibility of the entire screen by the target customer population, without letting go of the sides of the device, with a possible one-handed vertical grip-anduse hold that defines the tablet as “small.” When some of the screen becomes inaccessible or a tablet can no longer be held and used by the same hand, it can be classified as “large.”

## Large Tablets

You might think that large tablets such as the 10-inch Samsung Galaxy Tab 2 (see Figure 3.6) have been around long enough for people to get used to the unique interface challenges these devices present. However, in the Android 4.0, much of the interface guidelines are not adopted well for large tablets. Instead they are treated by Android exactly like their small counterparts. However, from the UXperspective, although there are some similarities, there are also important and significant differences, as I point out here.

![](images/35af10c17debcebba71fc7c83a46199136a2c4b12ad8ada61834bf69e317b305.jpg)

it is in smaller tablets. However, there is also much less in terms of vertical space constraint on a 10-inch device when you're using the horizontal keyboard, so horizontal tends to be the preferred orientation for apps that require data entry, web browsers, and many other applications. Anecdotal observation suggests that reading tasks tend to be split about 50/50 between horizontal and vertical orientations, based on the reading medium and personal preference.

Unlike small tablets, large tablets do not allow one-handed unsupported gripand-use hold. There is no balancing a larger tablet in one hand; instead, the device in either orientation is held in a committed two-handed grip that supports the heavier, more awkward (and more expensive) device securely. Figure 3.7 demonstrates the hot zones for a large tablet in a two-handed grip in vertical and horizontal orientations.

![](images/f4bd2a7da0dcafaf5743bd149e6dd6d419abd0c61e782ac187fee0eb53173834.jpg)  
Figure 3.7: These are the hot zones for a large tablet in a two-handed grip in vertical and horizontal orientations.

For larger tablets in either orientation, the bottom of the device is not nearly as accessible as the top. That is because the bottom of the tablet is usually resting on some surface, like the person’s lap or a table. This makes accessing controls on the bottom of the screen (including the essential back button!) awkward at best. The same goes for the controls located in the middle of the top action bar. Your customers will have to let go of the device to tap there, in which case Fitts's law takes over: The time required to rapidly move to a target area is a function of the distance to the target and the size of the target. If the target is small, such as tapping a button or an icon on the top action bar, it makes unsupported free-hand movement required to reach the target quite awkward, especially if it has to be repeated over and over. Mobile designer Josh Clark brilliantly calls this an “iPad elbow” (which you can rename with a slightly more utilitarian “large tablet elbow”). Large tablet elbow is especially pronounced for repeated tasks in a horizontal orientation, where reaching the middle on the top action bar or any portion of the bottom action bar is particularly awkward.

What does this mean from the interface perspective? As discussed in great detail in Chapter 14, one idea is to use only a small portion of the vertical action bar and forgo the bottom bar. If you're more adventurous you might want to try navigation and functional controls that run vertically along the left and right sides of the large tablet, instead of horizontally across top and bottom. Another idea is to use the C-Swipe to call up the menu in any part of the screen, an approach also discussed in Chapter 14. Neither of these approaches fits within the general Android guidelines and will definitely go against the “party doctrine.” However, for the adventurous product team, native tablets apps offer the best opportunity for experimentation and creative differentiation.

## Celebrate Fragmentation

Fragmentation is always going to be a challenge in Android app development. Yet as the OpenSignal article points out, there is much to be celebrated. Android has reached more than 195 countries, which is more places than most people visit in a single lifetime. Even more impressive is that the five countries with top Android use are the United States, Brazil, China, Russia, and Mexico, which means the developing world is leading Europe, at least in Android mobile computing. With cost of the Android hardware further dropping on a daily basis, your app is just as likely to be downloaded by a rural farmer in India as by a New York stock broker. Or if you look at it another way, your work can reach billions of people around the globe and make a real difference in their daily lives.

The mobile design is all about the context. To ensure that your app solves the right problems for the right audience, you need to customer-test your app as early and as often as possible with your target customers. Read the next chapter to discover a cheap and effective way to do just that using sticky note prototyping methodology.