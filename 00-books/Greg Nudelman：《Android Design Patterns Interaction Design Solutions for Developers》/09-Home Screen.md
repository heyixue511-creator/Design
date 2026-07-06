C h ap t e r 6

# Home Screen

See if you can spot a crucial difference between the following two statements:

A. “I heard this great joke on a train today. It was told to me by a grayheaded man while we were riding together on the train from Santa Clara….”

B. “A mushroom walks into a bar. The bartender says to him, ‘We don’t serve your kind here.’ And the mushroom replies, ‘What’s wrong? I’m a fun-guy!’”

OK, maybe that’s not the best joke, but I have a point to make: Even if both statements contain about the same number of words, there is a crucial difference between them: Statement A tells you about the story, whereas statement B actually tells the story. That is the difference between good and great home screen patterns: The good ones actually tell you the story. The rest, well….

## 6. 1 Pattern: List of Links

Sometimes called Hub-and-Spoke (first documented by the User Experience (UX) w expert Jennifer Tidwell in her essential 2011 book Designing Interfaces from O’Reilly), List of Links is a popular and venerable design pattern used all over the mobile world on all manner of platforms and applications. Unfortunately, this pattern frequently tells people about the story, rather than telling the story itself. Here’s how to spruce it up to improve its usefulness.

## H ow It W orks

The home screen acts as a hub that presents a bunch of links or icons of primary functions or popular views that can be obtained with the app.

## Example

You don’t have to look hard to find an example of this pattern. Travelocity (see Figure 6.1) offers a good one that also highlights the key issue with this pattern: telling customers about the story (instead of the story itself).

![](images/bf1eb226089a40f515103efcfe9d78c9478f15b33a51cbb99e2bc858cc3212e5.jpg)  
Figure 6.1: The Travelocity app uses a typical List of Links pattern.

The screen makes it clear what information can be obtained within the app and what actions you can take if you engage with the app as a customer. The icons are clear.

However, despite the clarity of the display, the screen leaves the customer feeling… a little blue (or a little gray, if you are viewing this screenshot in gray scale). There is absolutely no information that pertains to the customer: Everyone gets the same set of links. How would you make this static page tell customers more of a story?

One approach is to use notification badges somewhere on the page or on the individual icons or links. One example of this is the older version of Google Plus (see Figure 6.2), where notifications are featured prominently on the top of the screen (the 3 in the red box).

![](images/d6eb119038b8afa77cb9b31a3cd46a511be5ae152fc1a6899768c5e3207014fe.jpg)  
Figure 6.2: Google Plus List of Links tells more of the story.

A simple variation of this would be to put notifications as smaller badges on individual icons—for example, place a (1) on the Photos icon if someone shared a new photo and a (2) on the Circles icon when two people have been added to your circles, and so on. The additional notifications would help the List of Links provide a few more details of the story (rather than telling people about the story).

## hen and W here to Use It

List of Links is the default pattern most people should consider as the first design for the home screen because List Of Links does a great job of cataloging various aspects of the app’s functionality. Even if you do not end up ultimately using this pattern for your home screen, drawing a List of Links for your app is a great exercise in organizing the app’s Information Architecture (IA) and cataloging possible use cases and those of your competitors.

Other patterns in this chapter are better for certain applications; however, List of Links is the basic default you should consider if your app covers a lot of highly variable functionality. Consider that in the Travelocity example (refer to Figure 6.1) the customer can book hotels, flights, or cars; read about new and exciting vacation destinations; and even find gas. This is a great deal of useful functionality to pack into a mobile app!

## W hy Use It

The List of Links pattern is one of the easiest and most intuitive for a novice to navigate. It’s easy to design and build (provided you have a decent icon designer), and it launches instantly because it does not require a server call to retrieve any information that is not already on the phone. Even if you do decide to go to the server to grab the badges, as shown in the Google Plus app (refer to Figure 6.2), these updates are typically single digits, which require minimal download time.

## Other Uses

One popular variation from this basic pattern is the Grouped List of Links shown in the Southwest Airlines app in Figure 6.3.

![](images/6ce5408d6a87656679d150b141312e6fa6a9c04053aacc804268b86db6d709f1.jpg)  
Figure 6.3: The Southwest Airlines app shows a grouped variation of the List of Links pattern.

This is a great variation for apps that have a lot of links because it enables a logical grouping that helps reduce the cognitive load on the customer.

## Pet Shop Application

List of Links enables designers to succeed with a wonderful variety of IAs. For example, Figure 6.4 shows just two: the IA on the left enables exploration by type of object (Dogs, Cats, Birds, Fish, Reptilians, and Other), whereas the IA on the right is more centered on what you can do (Find Pets, Care & Feeding, Local News, and Your Profile). It’s a great exercise to pause here and imagine a few other alternative IAs that fit the Pet Shop theme. Which one should you choose? Obviously the one on the left emphasizes the e-commerce application, whereas the one on the right is more suited to social networking applications. The one you ultimately choose depends on what your app is designed to do.

![](images/11231054de7dd86918faa6c7118d3183b9f5f9aa1fd9fb2b937121e9cff07286.jpg)  
Figure 6.4: The List of Links pattern supports multiple IAs.

The badge update mechanism mentioned earlier is also included so that some links (for example, Local News in the right-hand design variation) show the new updates that have come in since the last time that particular area of the app was visited.

## Tablet Apps

This pattern always feels a bit dry on the tablet with a large expanse of space available to the viewer. List of Links is less suited to the tablet in general. If you do use List of Links, consider having a split pane view with one of the other patterns in this chapter shown in the other pane.

## Caution

None

## Related Patterns

6.4 Pattern: Browse

## 6. 2 Pattern: Dashboard

Sometimes, the app lends itself uniquely to displaying a current state and trends that can be expressed using graphs and tables. Take full advantage of this situation with the Dashboard pattern.

## H ow It W orks

When the customer opens the app, he sees the current state of affairs displayed as a dashboard—for example, graphs and tables.

## Example

An exceptional mobile dashboard is Mint (see Figure 6.5), which displays an excellent Overview dashboard that shows a snapshot of the current financial state: inflows and outflows, budget, and cash flow.

![](images/0276a03d892ad4c385383c22c452d61d66f00f58650c3edccf24c0955801b9da.jpg)  
Figure 6.5: The Mint app is an excellent example of the Dashboard pattern.

Note that the graphs and tables are compact, leaving some room for the Alerts and Advice sections, which are prominent and represent a large portion of the value proposition of the app.

## hen and W here to Use It

Any time you can obtain some numbers that are important to the person using the app, Dashboard is the pattern to use. Financial and banking apps are obvious choices, but elements of this pattern can be pulled in almost anywhere. For example, travel apps can track prices on hotels and flights for recently researched destinations, issuing alerts when it’s time to pull the trigger and purchase the trip. Social media can signal how many new friends you’ve acquired since the last time you used the app and how many photos, updates, and so on you posted as well as any badges you earned. Even the simple examples of using icon badges and notification you saw in “Pattern 6.1: List of Links” also constitute a kind of a primitive dashboard.

## W hy Use It

You swim in the sea of digital information. That means you consume numbers for breakfast, lunch, dinner, and snack. Providing aggregate information that helps you make sense of your numbers and trends is an increasingly crucial function for which mobile devices are ideal. A small display space forces aggregation; as a result, dashboard-type displays are becoming increasingly common. Last but not least, the best dashboards enable your customers to grok the complete story at a glance, while also making it possible to drill into life-defining questions, such as “Why did the mushroom think he was such a fun-guy?”

## Other Uses

None

## Pet Shop Application

You can imagine several scenarios for the Pet Shop app in which dashboards would be useful. One idea is to track the health and well-being of the pet. The dashboard in Figure 6.6 tracks past and upcoming vet visits, distance walked, and weight of the pet.

If your pet were for some reason in poor health (or just young), you could watch his progress toward recovery and his healthy growth.

![](images/f921f8059209482a4e5108356b5c02f3680cd93a9034fce609c36bd8507ba9f1.jpg)  
Figure 6.6: Use the Pet Shop app Dashboard pattern to keep track of Fido.

## Tablet Apps

Dashboards can be fantastic for tablets. Greater screen real-estate allows for extensive multisectioned displays with highly customizable dashlets (small graph or table displays) that the customer can rearrange as desired. Tablets are an ideal device to look at dashboards, especially in the context of shared attention, such as office meetings or contextual discussions right on the factory floor. At the present, tablet dashboards are greatly underused—don’t let this opportunity pass you by!

## Caution

When creating a dashboard avoid overstuffing it with data. This is easy to do with so much information available right at your fingertips. Test with your customers to make sure your design displays only the most important things upfront and allows people to dig deeper into the information as needed by tapping the desired section.

If one dashboard is good, are multiple dashboards even better? Sometimes, too much of a good thing is…well, bad. Avoid the page carousel effect of multiple dashboards that require your customers to swipe left to right around an endless list of pages. When it comes to seeing more information, scrolling is much more intuitive than paging side to side. If you are forced to have more dashboard information than can fit comfortably on one screen, use scrolling instead of side-to-side pagination because scrolling allows for longer pages, which use irregular screen space formed by dashlets more efficiently. For instance, on a long page you can alternate as many large and small elements as needed, instead of forcing one large graph and a few smaller dashlets into a complete page layout on every individual dashboard page. If you must have multiple dashboards, use the Tabs pattern instead (see Chapter 8, “Sorting and Filtering”) to identify each dashboard page or use the simple drill-down method, as shown in the Mint example (refer to Figure 6.5).

## Related Patterns

6.1 Pattern: List of Links

8.5 Pattern: Tabs

## 6. 3 Pattern: Updates

Whenever you have regular relevant personal information of interest to the customer, consider using the Updates pattern on your home screen.

## H ow It W orks

The home screen shows one or more posts or messages from the customer’s update stream.

## Example

There are many examples of this pattern, from e-mail apps such as Gmail to news apps such as CNN. However, where this pattern really shines is in social media apps such as Twitter and LinkedIn. Perhaps the quintessential and richest example is Facebook (see Figure 6.7).

The Facebook app home screen shows a running summary of updates of various different types, all arranged in the order of Most Recent First. This design is easy to understand and use and immediately tells the freshest story possible anywhere. Note also the roll-away side menu that Chapter 13, “Navigation,” covers in more detail.

![](images/5e500458b9cf4fe1304b8b1495a648b22c8ebadcfd3b46737a84a09f5e1dc719.jpg)  
Figure 6.7: The Facebook app’s implementation of the Updates home screen pattern is excellent.

## W hen and W here to Use It

Regular updates that are of some interest to the customer are the prerequisite for using this pattern. Thus, it is most often used in communications-driven apps, such as e-mail and social media, and less so in e-commerce, e-readers, and other content- and action-centric applications.

## W hy Use It

Updates tell the story—pure and simple. Recall the earlier discussion of the Google Plus app in Figure 6.2. The older design of the Google Plus app notifies the customer that he had three updates. It is slightly better than no notifications, but still it tells no story—but only tells about the story—and requires the customer to make the extra tap to reveal the details. In sharp contrast, the Updates design pattern makes the story the front centerpiece of the display. For the apps where the story matters, this is an effective pattern because it enables your customers to immerse themselves in the story from the beginning, which means they navigate less and stay engaged longer. Compare the older design of the Google Plus app shown in Figure 6.2 with the recent design that uses the Updates pattern as shown in Figure 1.7 in Chapter 1, “Design for Android: A Case Study.”

## Other Uses

In addition to personalized feeds from social media and e-mail apps, news stories of general interest are also appropriate for the Updates pattern implementation. Here you have a choice: Whereas typical updates are posted in the order of Most Recent First, news can also be posted in order by Most Popular First or in multiple sections, such as Breaking News, Most Popular Stories of the Day, and Editorials.

## Pet Shop Application

Figure 6.8 demonstrates the Updates pattern designed with the screen in two sections: Local Canine News and New Puppies on the Market. Both sections assume you have identified some pieces of information about yourself: where you live and what kind of pet you are looking for. Note that you do not need to label each section explicitly if they have different layouts (though there is nothing wrong with labels). This design saves some screen real estate by not labeling the New Puppies on the Market section because it should be pretty clear to the customer even without the label that it has some “featured” type items that the system judged relevant for him or her. This arrangement also enables you to experiment with this important section and create the perfect mix of content for each customer without being constrained by the section title.

This kind of information might be useful to a dog enthusiast, who would be the target customer for this kind of app. The local news section is shown first because it is less likely that there is much local dog news, so these events are more urgent/ important. This section can be entirely optional. For example, if there is no local dog news happening right now, the section might be empty. Verify any assumptions you make in your own designs through user research that will help you understand the needs of your market and design accordingly.

The second section can be based on the last search the customer performed or set up on a separate page, looking for new arrivals on the market of dogs and puppies of a particular breed. There are usually more updates to this section because inventory turns over quickly. Therefore, this section can extend well below the fold. (Above the fold is the portion of the screen that is visible without scrolling.) Depending on the design, the entire page can be made scrollable, so the news, once read, can be scrolled off the screen easily. This mixed content updates is a useful model adopted from Facebook; as you can see it can be successfully applied in many different situations.

![](images/6382ae36a4088ea8705bcca1dfde2dead0be414074498731d67d37e312225df1.jpg)  
Figure 6.8: This wireframe presents an alternative approach to mixed media: the two-sectioned Updates pattern in the Pet Shop app.

## Tablet Apps

Updates on the tablets are fantastic and constitute one of the best tablet home screen patterns. Because screen real estate is much less of a problem than on a smaller device, you can devote more space to tell the story with updates without worrying about the mechanism for hiding the navigation; there is usually plenty of space to display navigation alongside the updates.

Whether you use List of Links, Dashboard, or any other pattern described for your tablet home screen, make an effort to also include a section of updates. You’ll be glad you did.

## Caution

Keep it simple, especially on tablets. One or two sections of updates are usually plenty; a single section of mixed updates (using the Facebook model) is often best. Remember, the customer is most likely to have the Facebook model in mind when she sees your updates, so she will expect the sort order to be Most Recent First. If you choose a different sort order, make sure that you have a good reason to change, and signal it appropriately to the customer.

## Related Patterns

6.1 Pattern: List of Links

## 6. 4 Pattern: B rowse

Sometimes, the best home screens are the ones that engage the customer in browsing items or information important to them—provided you supply enough information to avoid pogo-sticking.

## H ow It W orks

When the home screen loads, it displays some actual items and item categories of interest to the customer.

## Example

A decent example of this pattern is the Amazon.com app (see Figure 6.9). When the app loads, the home screen displays some items of immediate and personal interest to the customer based on his previous search history, or items obtained via the People Who Shopped for X Also Shopped for Y loose-matching algorithm.

Why is this not the best possible example? Even though Amazon.com has a good Browse section, it is small compared to the overall screen real estate. There is a lot of branded miscellaneous junk, such as Gold Box, greeting, and navigation. Most important, individual item-level information is completely missing; the customers have no idea why this shoe is shown, what the item’s title is, or (this is the key) what the item’s price and any associated discount are. All the customer sees is the picture.

A better approach is developed by the redesigned Newegg app, as shown in Figure 6.10.

![](images/3355f24ca1487b70b90368e71aa16bbb98dd68c3caa09501d6357de596365373.jpg)  
Figure 6.9: The Amazon.com app includes a decent example of the Browse pattern.

![](images/b5c9b5d417237c19ce555c15e8f859d5c9aa14efcc3bcfcf4483919e04e06d6c.jpg)  
Figure 6.10: The Newegg app has a better implementation of the Browse pattern.

Most of the page is devoted to products on sale. Each product is shown with a good-sized thumbnail and description, and the price and discount take centerstage. This is an actionable home screen designed so that the customer can immediately make a purchase decision without looking at the detail page. If you scroll past the sale items, you come to the category list, which offers browsing opportunities by category for those customers not immediately interested in sales.

Depending on your app, an even better approach to design a Browse pattern home screen might be to use the 2-D More Like This pattern (similar to Netflix and Gowalla). You can find more information on this useful pattern in Chapter 14, “Tablet Patterns.”

## W hen and W here to Use It

Any time you have some content that might be of interest to the customer, Browse is a great pattern to put to work. A Browse section can be small, like it is on the Amazon.com app or implemented as the 2-D More Like This pattern over the entire home screen as it is in the Netflix app.

## W hy Use It

Much like the individual updates in the Updates pattern, real items of interest are the story. Seeing these actual items front and center tells the story and engages the customer immediately.

## Other Uses

You could argue that Updates and Browse are similar patterns, and you are, of course, correct. However, there is one crucial difference: Updates are strictly devoted to showing updates from the people you are already connected with or real updates happening in the system. Browse is another facet of the same idea, but it can be expanded greatly to also show related merchandise, upsells, deals, local inventory, and the like. Most successful apps including Amazon.com experiment with a mixture of items in their Browse streams, making a fresh list each time the person visits the home screen. You should, too.

Browsing content for local information and deals is always popular, and it’s great to include these things on a mobile device that tracks a customer’s immediate location via on-board GPS. Make sure, however, that this content relates in some way to the person’s interests and avoid spam and outright ads.

## Pet Shop Application

Figure 6.11 shows a simple example of the Browse pattern created with a gallery of new pets available in the customer’s area.

![](images/303f69683a271e7a312aaf4dcf15832e8864ec105b8a19454bb71d5b0e870a94.jpg)  
Figure 6.11: This wireframe shows a gallery of pets on the home screen of the Pet Shop app using the Browse pattern.

This approach is both effective and attractive as a homepage that enables new customers to know upfront what they can expect from the app. For another great example of a Browse home screen interface design, see the Pet Shop section in the 2-D More Like This pattern in Chapter 14.

## Tablet Apps

Browse is practically made for tablets because of the more expansive real estate and free-flowing swiping gestures. Any browse content you can bring into the tablet interface improves the customer’s home screen engagement and the appeal of your app.

## Caution

It’s easy to yield to the pressure from the marketing department to include items that have nothing to do with the customer and are basically ads. Don’t do this. If you do, conversion and customer loyalty will both plummet.

Another thing to watch out for is to ensure that you provide not just images of items but also enough supplemental information so that the customer can make a solid, committed decision to drill down into details to investigate further and possibly purchase or otherwise engage; you want to help the customer avoid pogosticking into multiple items. This commitment on your part must include a large enough thumbnail image for the customer to see the necessary detail and also sufficient supplemental textual information (refer to the earlier Amazon.com and Newegg examples).

## Related Patterns

14.5 Pattern: 2-D More Like This

## 6. 5 Pattern: M ap

Often the mobile information is highly local and geo-centric. A map-based home screen is the perfect pattern for these applications, provided you get the zoom factor correct.

## H ow It W orks

When the home screen loads, it displays a map of the customer’s immediate area and shows items of interest.

## Example

One great example of this pattern is the Google Maps app (see Figure 6.12).

Maps loads the map of the immediate area, optimized for quick navigation and shows nearby roads and freeways.

![](images/0cf30b31e6dec0b41de7d1aad068baf8a20670dbe333bc49579577c9521b2fc6.jpg)  
Figure 6.12: The Google Maps app makes excellent use of the Map pattern.

## W hen and W here to Use It

Map is a great home screen pattern to use any time geo-centric information is of interest and can be plotted on the map.

## W hy Use It

Maps are something you are familiar with from an early age. They are intuitive and tell the story. And now, with mobile on-board GPS technology, you have a unique

opportunity to display an in-context map that accurately represents the customer’s immediate surroundings.

## Other Uses

Simple maps for navigation are just the beginning. You can use the Map pattern with any geolocated points of interest. For example, the SitOrSquat app shows nearby restrooms, and Trulia shows homes for sale in the nearby area (see Figure 6.13) .

![](images/ad2b9deb15973cc296f26cef8bd5e7ebb6cbec4ada0aba74ea63a1582525ff3d.jpg)  
Figure 6.13: Compare the Map pattern implementation in the SitOrSquat app (on left) and the Trulia app (on right).

## Pet Shop Application

It’s easy to imagine showing pets for sale in the immediate area. Figure 6.14 shows a hand-drawn wireframe with a simple implementation of the Map pattern.

![](images/2a269edf54cb5258a5d12d6c5ae184aec15743749b5f6293bff6503fb866c4b4.jpg)  
Figure 6.14: This is a suggested implementation of the Map pattern in the Pet Shop app home screen.

## Tablet Apps

With tablets of all kinds, you must be careful with the GPS data; sometimes it is not available (or not accurate) for tablets that run on a Wi-Fi network. Also be aware that tablets often do not travel as easily or as widely as smaller mobile devices; consequently map-based local information is generally of less interest to tablet users. This is, of course, a generalization. You must do some research to figure out just how pertinent this kind of pattern will be to tablet users of your app.

If you do use the Map pattern on a tablet, one possibility is to show the map corresponding to the last search that was done on the device instead of the local map. To see information in a different area, the customer must provide the area of interest as a search parameter, so the tablet app does not need to rely on the GPS data alone for geo-location and can be successfully operated via any Wi-Fi network.

## Caution

One thing to watch out for is the initial zoom level. For example, the initial zoom level in the SitOrSquat app discussed earlier shows a map area that is not sufficiently large to show nearby bathrooms (at least in the heart of the Silicon Valley), as shown in Figure 6.15.

![](images/f27f0749b72c517b078000798fb97d8f73d5d41de4d3df5417195e443a011feb.jpg)  
Figure 6.15: The initial SitOrSquat Map pattern zooms too close.

It takes several “zoom out” actions to make the nearby bathrooms visible. Inexperienced bathroom (err…app) users might think that there are simply no bathrooms or that the app is malfunctioning. Be sure to zoom out your initial view sufficiently to capture two or more points of interest. In general, it is easier to zoom into a selected area than to zoom out. Zooming in can be done one-handed using a double-tap shortcut, whereas zooming out requires the pinching multitouch gesture that requires two hands (one hand to hold the device and the other hand to pinch the screen).

## Related Patterns

8.4 Pattern: Parallel Architecture

8.5 Pattern: Tabs

9.6 Pattern: Local Results

## 6. 6 Pattern: H istory

Whenever you encounter app engagements that span multiple sessions, it is a great idea to re-engage customers by reminding them of the subjects of previous searches.

## H ow It W orks

The home screen displays a list of links or items that represent recent previous queries, with the most recent query listed first.

## Example

One of the best examples of this pattern is the Android Global Search app (see Figure 6.16). It shows a mixture of apps, web pages, and contacts that have been recently searched. If customers look for the same “person, place, or thing,” they do not need to search again—the information and call to action is right there. The page also tells a complete story about recent activity on the device (versus telling the customer about the story).

![](images/86ecc1f8c8a36090d91409850fe7cd492b91e34c7f27a922f324700b2fcd9209.jpg)  
Figure 6.16: The Android Global Search app has an excellent History pattern homepage.

## W hen and W here to Use It

Anytime the person looks for the same thing multiple times and needs to be reengaged in the search process, or when the customer needs to be inspired or reminded of the previous searches, History is the module to use.

## W hy Use It

Why not? Despite easy availability of search history and its tremendous usefulness, few apps take full advantage of this pattern. For example, the Priceline homepage, as shown in Figure 6.17, simply displays the search screen and offers an option to look in a nearby city (Fremont, CA) or in a different location (marked by Choose a City).

![](images/c88b46dfd9f7137973aab48e742ad00b0f9e239d5c87962d71f61557177ab5b0.jpg)  
Figure 6.17: The disappointing Priceline app homepage doesn’t include the History pattern.

The Choose a City function is disappointing, to say the least; it simply displays an alphabetical list of popular destinations. This page would certainly be enhanced by a modest History function. If only the app remembered the last four to seven places you’ve looked at! Often, booking a hotel is a multistep process, so the customer is likely to revisit the app such as the Priceline Negotiator multiple times in between getting driving directions, calling a friend, texting, looking at Twitter and Facebook updates, looking for a place to eat on Yelp, and so on.

But multitasking only scratches the surface. Recently I had an experience looking for a hotel in the middle of the large metropolis of Los Angeles, which, as it turns out, is actually composed of multiple small towns. Each town has its own hotel inventory, each of which requires a different search by city name. Jumping between searches for Beverly Hills, West Hollywood, and Santa Monica with the goal of finding a reasonably priced hotel at the intersection of all three cities was most tedious. Having a basic History module with 5 to 10 recent destinations on the homepage would take care of this common problem.

## Other Uses

Search history often acts as a wish-list functionality when it kicks in automatically. Unfortunately, few apps take full advantage of this pattern. For example, the Trulia app forces the customer to tap the Save button to save the search, which in turn, forces him to log in (see Figure 6.18) . This is a lot like my HP printer saying, “You can no longer print in black and white. The magenta ink cartridge has expired.” Seriously Hewlett Packard, you are not fooling anyone: Even my three year old knows that you don’t need the magenta crayon to draw a black and white picture. You only need one crayon: black! Although logging in by itself is not a huge deal, it is completely unnecessary to save a short history of recent searches. Every native app has some local storage space it can use to store history (or a temp guest session token if you prefer to save recent history on the server). Having to tap the Save button to save a search is both tedious and unnecessary; the extra tap is one more thing for your customers to do, and it interrupts the natural flow of searching.

![](images/c988d64e8b24e79752a369c4ea804989e525cd62b81ec4eee65bbe5c6a6c9b75.jpg)  
Figure 6.18: The Trulia app forces an explicit save and login instead of adding to on-board app History.

A better implementation would be to provide a search history function that automatically remembers the last 10 to 15 searches run by the customer. People looking for a home tend to run the same few queries over and over again, so automatically remembered searches would serve people well in this context. Do the customers need to log in at all? Only if they tap a Share This Search or Share This Property button that would replace the Save button to share information with other people or multiple devices. At this point, logging in would be both expected and natural.

## Pet Shop Application

The History pattern is perfect for pet searches because the shopper might be looking at several different breeds while dealing with a rapidly changing local inventory. For example, if a customer looks for guard dog puppies, the History module would be advantageous; he could redo local searches for “Dogue de Bordeaux,” “Bouvier des Flandres,” and “Boerboel” without twisting his fingers while trying to retype these names. (See Chapter 7, “Search,” for more ideas about helping customers with typing long or difficult queries.) Figure 6.19 shows a simple wireframe of how this History-forward page could look, augmented with the Updates pattern, which shows the count of new dog inventory within 20 miles of the area from the last time the search was run.

![](images/d7c09b92d434b62135ae02faa6c7a605540a31c2787f94595fb15de8c9aa7ca9.jpg)  
Figure 6.19: The Pet Shop app History pattern home screen with local Updates is highly effective.

For Pet Shop customers, this kind of home screen would be “killer functionality,” and might just be the selling point for the entire app.

## Tablet Apps

Typing on tablets is less tedious, and connections are often faster than on other devices. That does not mean that people using tablets like to think any more or any harder than the people using smaller mobile devices. History is a great module to include in everything from a simple map app to sophisticated shopping services.

## Caution

No matter the detractions, having the History module is almost always better than not having one. That said, remember to provide a simple way to edit or clear the history because it can become a big privacy issue.

## Related Patterns

5.3 Antipattern: Sign Up/Sign In

6.3 Pattern: Updates

7.2 Pattern: Auto-Complete and Auto-Suggest

7.3 Pattern: Tap-Ahead

## C h ap t e r 7

## Search

Search is a fundamental mobile activity. Think about it—mobile is much less about creating stuff (unless you are talking about taking pictures or writing an occasional tweet). Instead, you use mobile devices mostly for finding stuff. Riffing on Douglas Adams’ Hitchhiker’s Guide to the Galaxy, mobile devices help you find places to eat lunch, people to eat lunch with, and directions to get to the restaurant, which helps everyone to get there sometime before the Universe ends— which makes search patterns important.

## 7. 1 Pattern: Voice Search

Audio query inputted via an on-board microphone is used as input for searching instead of a keyword query. Typing on the phone is awkward and prone to errors. This makes audio input a great alternative to text.

## H ow It W orks

Usually, the searcher taps a microphone icon, causing the device to go into listening mode. The searcher speaks the query into the on-board microphone. The device listens for a pause in the audio stream, which the device interprets as the end of the query. At this point the audio input is captured and transcribed into a keyword query, which is used to run the search. The transcribed keyword query and search results are shown to the searcher.

## Example

One of the most straightforward implementations of the Voice Search pattern is the standard input box for writing text, augmented with a microphone icon, as exemplified in Google’s native Android search. (See Figure 7.1.)

![](images/1e632a63b6b52c31bfbecc91ebabfe29e9478ed52d8ca8b89d8886a6745afb87.jpg)  
Figure 7.1: Google’s native Voice Search in Android 4.0 is straightforward.

## W hen and W here to Use It

Most apps that have a search box can also use the Voice Search pattern. For example, the Yelp app, as shown on the left in Figure 7.2, does not currently include the Voice Search feature, but it can be easily augmented with a microphone icon, as shown in the wireframe on the left.

![](images/e84b283a8079049a8ff48edd005f225143e9983cffa5b1623c67745d2fad7e61.jpg)  
Figure 7.2: Adding the Voice Search pattern to the Yelp app would be easy from the UI standpoint.

People often use Yelp while they’re walking around with a bunch of friends and talking about where to go next. In this case, simple voice entry augmentation makes perfect sense: Speak the query into the search box (which is quite a natural behavior as part of the human-to-human conversation already taking place) and share the results with your friends by showing them your phone. Then, after the group decision has been made, tap Directions, and use the map to navigate to the place of interest.

## W hy Use It

Most mobile search is done “on the go” and in context. Given how hard text is to enter into a typical mobile phone (and how generally error-prone such text entry is) voice input is an excellent alternative. Other important considerations for using the Voice Search pattern are multitasking activities such as driving. Driving is an ideal activity for voice input because the environment is fairly quiet (unless you are driving a convertible), and the driver’s attention is focused on a different task, so traditional text entry can be qualified, to put it mildly, as “generally undesirable.”

## Other Uses

The release of Siri for the iPhone 4S kicked into high gear a long-standing race to create an all-in-one voice-activated virtual assistant. Prior to Siri, Google had long been leading the race with Google Search: the federated search app that searched across phone’s apps, contacts, and the web at large. Vlingo and many other apps took the Voice Search pattern a step further by offering voice recognition features that enabled the customer to send text messages or e-mails and do other tasks by simply speaking the task into the phone. However, none of the apps have come close to the importance and popularity of Siri. Why? There are many reasons, including the mature interactive talk-back feature in Siri that enables voice-driven question-and-answer interactivity, including the amazing capability to handle x-rated and gray-area questions with consistent poise and humor, as shown in Figure 7.3 (in other words, Siri has something of a personality). Another important feature was a dedicated hardware Siri button (on iPhone 4S you push and hold the Home button to talk to Siri) that enabled one-touch interaction with a virtual assistant without having to unlock the phone.

![](images/2bf4b94c487555764c6f566adff4010fb45eb030c07abe9a24b786f02d419b18.jpg)  
Figure 7.3: Siri responds to a Voice Search query: “I need to hide a body.”

Although it’s pure speculation at this point, one of the applications of Google’s voice recognition technology could be the same sort of virtual assistant for your phone or tablet, activated by pressing (or holding) one of the hardware buttons (the Home button would be a good choice). Added security can be achieved via voice-print pattern recognition. Voice recognition technology would also help distinguish your voice patterns from those of other people in loud, crowded places, thereby further increasing the personalization of the device and making it completely indispensable (if that is even possible at this point!).

If this becomes the case, dedicated in-app Voice Search (refer to Yelp in Figure 7.2) can be completely superceded by the Google virtual assistant. For example, the customer could say, “Assistant: search Yelp for xyz.” The assistant program would then translate the voice query into keywords using advanced personalized voice recognition, open the Yelp app, populate the search box with the keyword query, and execute the search.

In some Google Search apps, the simple action of bringing the phone to your ear forces the app into a listening mode by using input from the on-board accelerometer to recognize this distinctive hand gesture. Unfortunately, this feature does not seem to be automatically enabled on Android 4.0 as of this writing. It is, however, an excellent feature and one that should come included with the voice recognition because it makes use of what we already do naturally and without thinking, so the design “dissolves in behavior.”

The role of voice input is not limited to search. It can be used for data entry and basic tasks as well. For example, while driving you could push the button and say, “Text XYZ to James,” and the device will obey. I should also mention that Google is not the only supplier of voice recognition technology. For example, Nuance communications, the maker of Dragon Naturally Speaking products, is likely the largest and most vocal (pardon the pun) distributor of speech-recognition software. As of this writing, the Target app uses technology licensed from Nuance for its voice recognition feature.

## Pet Shop Application

Just as in the earlier Yelp example, you can use voice recognition to search for a specific pet. The customer would launch the Pet Shop app and then swing the phone up to his ear and speak a search query, such as “black lab.” When the customer has a pause in speech, pushes the Done button, or simply swings the phone down, the query activates and displays the appropriate search results.

## Tablet Apps

For Voice Search, tablets are different from phones. Although there is some debate about this (and no official studies have yet been performed) anecdotal evidence points to typing on the tablet being not quite as challenging as it is on the

phone. Thus voice input for tablets is likely to be more error prone. While using a tablet, the person is also less likely to be multitasking in a loud environment or be engaged in an activity that requires the user’s attention to be placed outside the visual interface of the device (driving, for example)—most of the tablet use happens at home or work. Does this mean Voice Search is not useful on the tablet? Not at all. There still exists an opportunity for high-end, high-touch, visual interaction with a virtual assistant software program. Apple’s original vision for the tablet device, The Knowledge Navigator, created in 1987 (sorry, Google, you were not yet born at that time) involved exactly that kind of speech recognition interaction with the device.

The best way to implement a high-end, personalized virtual assistant might be to create a hybrid of software plus human virtual assistant. The person using the tablet would get high-end service with a consistent, pleasing visual and auditory representation. Given Google’s reputation for awesome inventive geekiness, highly customized animated Obi One, Jarvis, and HAL virtual assistants (as well as various Playboy models, anime characters, and maybe a little something for the millions of John Norman fans) complete with high-end graphics and voice simulations might be coming soon to the Android tablet near you. Perhaps this book can serve as an inspiration?

## Caution

Voice recognition is still a fairly new technology, and despite the apparent similarity of the interface, there are many important considerations and ways to get this pattern wrong:

■ Don’t forget the headset: Some users of the technology will be on a Bluetooth or wired headset. Ideally, Voice Search can be activated by using the buttons on the headset, without having to touch the phone. For example, with Apple’s Siri: “When you’re using headphones with a remote and microphone, you can press and hold the center button to talk to Siri. With a Bluetooth headset, press and hold the call button to bring up Siri.” (See http://www.apple.com/iphone/ features/siri-faq.html.) Similar convenience features are conspicuously absent from the Android 4 interface for the simple reason that the headsets from various manufacturers lack consistency in the hardware configuration. (In other words, there is no “center button.”) As mentioned earlier, this needs to change. Convenience is the key for Voice Search on Android to be a contender.

■ It’s not “Done” until the fat finger sings: The Android 4 implementation of the Google’s native search (refer to Figure 7.1) waits for you to stop talking before accepting the voice query. This works most of the time, but it can be a serious problem in loud environments, in which the interface fails to stop and keeps listening for almost a full minute! Always remember to provide a Done button to stop the input. One of the best implementations is to make the microphone icon act as a Done button. Of course, it must also look “tappable.”

■ Extremely loud and incredibly personal: In loud environments in which other people are talking, it’s hard to parse the owner’s voice from the background of other conversations. Fortunately, voice imprint is as unique as your fingerprints, and with some “training” the user’s unique vocal patterns can be parsed out of the background conversations in the crowd. Voice imprint has a lot of privacy issues.

■ Full-circle audio experience: The Driving Mode paradigm that exists in certain older Android phones is an antipattern. There is an excellent reason no one uses vi editor for coding Java or writing books. As Alan Cooper so eloquently stated in About Face (2007, Wiley), switching modes is tedious and error-prone, not to mention downright dangerous while driving. The only reason why Airplane mode works is because a nice flight attendant tells us it is time to turn it on. For all other applications, the system simply must make an effort to match the output mode to the user-selected input mode. For example, if Yelp were asked for directions to a museum using voice input, chances are the customer is doing it while driving (the app can also detect when someone is moving at car speed automatically using the on-board GPS). This means that the output directions should also be available using voice. Ideally, Yelp should read out loud step-by-step driving directions if the customer asks for them via a simple voice command such as Tell Me or Give Me Directions. This completes the 360-degree, full-circle Voice Search experience. As of this writing, for example, Apple’s Siri has made inroads into integrated audio directions—a feature Android sorely needs to compete in the Voice Search space. Of course, this also works great for folks with disabilities.

■ Watch out for uncanny valley: Uncanny valley (http://en.wikipedia.org/wiki/ Uncanny\_valley) is a term coined by Masahiro Mori to describe the strong revulsion people feel for robots that are almost, but not quite, human in appearance. One of the consequences of the uncanny valley is that more realism can lead to less positive reactions. As virtual assistants improve, and especially when they acquire visual appearance as well as voice, you need to make sure you make the purely digital entities look decidedly less than human. Uncanny valley might turn out to be an especially dangerous place for high-end hybrid human-software assistants. In their brilliant book Make It So (Rosenfeld Media, 2012), Nathan Shedroff and Christopher Noessel mention another issue: Authentically humanappearing digital assistants increase the expectations of the near-human

capabilities, which sharply increases the person’s level of annoyance when the assistant screws up the task or fails to understand the person correctly. They suggest an elegant way of solving this problem by making a digital assistant into a talking pet: Although most owners consider their dogs intelligent, a talking dog would engender both lower expectations and the higher wow factor, while avoiding the uncanny valley entirely. Here’s my own recommendation: Using mid- and low-fidelity animation for pure or hybrid digital assistants (think animated Obi Wan Kenobi from the series Clone Wars or the LEGO Star Wars games, instead of video of a live actor) should likewise be helpful in achieving the same goals.

## Related Patterns

13.5 Pattern: Watermark

## 7. 2 Pattern: Auto-Complete and Auto-Suggest

Auto-Complete and its sister pattern, Auto-Suggest, are broad classifications of keyword-entry helper patterns. Both reduce the number of characters the person needs to type and reduce the number of entry errors and queries that produce too many or too few results.

## H ow It W orks

When the person enters one or more characters into the search field, the system shows an additional “suggestions layer” that contains one or more possible keyword combinations that in some way correspond to what the person has entered. At any point, the person has the option to keep typing or select one of the system suggestions.

Strictly speaking, Auto-Complete uses a part of the query the person typed in as a seed to providing suggestions (so that the suggestions include the original keyword or fragment). This does not always work perfectly on a mobile device because many times a small fragment contains fat-fingered misspellings. That’s where Auto-Suggest comes in.

Auto-Suggest has more “freedom of movement” than Auto-Complete, providing keywords and queries that include

■ Spelling corrections

Controlled vocabulary keyword substitutions

■ Synonyms of what the person originally typed in, query expansions, and so on

The suggestions work best when they are a clever combination of Auto-Suggest and Auto-Complete, with the system drawing the best ideas from multiple sources.

## Example

Google Android search is a great example of the combined pattern, splitting the suggestions layer into two sections: first providing three auto-complete ideas and then auto-suggesting some contacts and apps that can be found on the phone (see Figure 7.4).

![](images/27bc33f4947f28e2beb09031a3156d20ddaa4ae0fe77a85350fcbe60a614bf88.jpg)  
Figure 7.4: The Auto-Complete and Auto-Suggest patterns work in tandem in Android 4.0 Native Search.

## W hen and W here to Use It

Any time there is a keyword query entry box, Auto-Suggest and Auto-Complete are both great patterns to implement. As search expert Marti Hearst reports in her book, Search User Interfaces (Cambridge University Press, 2009) These features generally rate great on usability and work well with other user interface (UI) patterns.

## W hy Use It

For most people, typing—especially on the mobile device—is tedious and prone to errors. Generally, the less typing you do on the phone, the better. Therefore, any UX pattern that can assist a person in entering information is a big win.

Auto-Complete and Auto-Suggest help reduce errors and increase satisfaction in multiple ways:

Reduce spelling errors: By reducing the total keys that need to be pressed, the system reduces errors associated with simply fat-fingering incorrect keys.

■ Improve query specificity: If the suggestion includes more keywords than the user was originally planning to enter, the customer often picks the more specific query, which ultimately makes her happier by providing her with the inspiration to enter “Nike Shoes” instead of just “Nike.”

■ Reduce zero results: Often queries are spelled correctly but include incorrect or conflicting keywords, which produce bad results or no results. Giving the person appropriate suggestions before she finishes entering the entire query often allows the system to forestall zero-results conditions before they occur. If the person starts typing Harry and the system displays a suggestion “Harry Potter and the Deathly Hollows,” the person is less likely to paint herself into a corner with an incorrect query such as “Harry Potter and the Sleepy Hollows.”

## Other Uses

Auto-Complete and Auto-Suggest can draw from many other resources to improve the quality of the suggestions:

■ Local: Mobile phone use cases are unique, because these devices are used literally “on the move.” Thus auto-suggestions must take into account local results (obtained via on-board GPS or wireless signal triangulation) whenever possible. For example, depending on the app and use case, a query such as “Coffee” could easily include auto-suggestions such as “French Roast Coffee” for online purchases and one or two nearby coffee shops.

■ History: The Auto-Suggest pattern need not always make use of the Internet connection. One of the most important mobile User Experience (UX) patterns is Re-engagement, which means picking up the previous task after an interruption of some sort (phone call, text, needing to find directions, and so on). Therefore, one of the most important functions of Auto-Suggest is to recall previous queries (History) that can be stored locally on the device using the on-board app databases (refer to the Browse and History patterns in Chapter 6).

■ Voice Search: At the time of this writing, voice queries typically do not produce auto-suggestions. This is surprising because voice recognition is often worse than the fat-finger typing recognition. Voice query Auto-Suggest is one interesting application to look into, particularly for nondriving applications in which the system needs to display only the suggestions on the screen rather than reading them back to the user.

■ Jump into other apps: One common use case, especially with heavily networked apps, is the need to open another app to accomplish a task. Auto-Suggest can help providing a one-touch solution to shorten the task considerably. One example could be a “gas station” query on Yelp. One autosuggestion could be “Directions to the nearest gas station”—a highly relevant use case when you are about to run out of gas. Hitting this auto-suggestion would jump directly into the Google Maps app to display directions. This kind of suggestion is also highly relevant to Voice Search use cases because it could provide a full-circle voice interaction with the system reading off directions to complete the experience. Other ideas could include providing suggestions that jump directly into the MP3 player if the query is “Like a Rolling Stone,” or into a book reader to see a sample of War and Peace. Note that it helps the customer to understand what will happen if auto-suggestions that jump directly into other apps include an icon of that app somewhere in the auto-suggestion row.

## Pet Shop Application

With the variety of common names for dog breeds (and difficulty of spelling them) it’s easy to envision a useful combination of the Auto-Suggest and Auto-Complete layer for the Pet Shop app, as shown in Figure 7.5.

In this simple example, the person types in Mas, and the suggestions layer presents the Auto-Complete options Massive and Mastiff as possible query completions, thereby forestalling the common misspelling Mastif, which would have likely resulted in zero results. In the same suggestions layer, Auto-Suggest also kicks in with English Mastiff, Neapolitan Mastiff, and an interesting keyword variation Bullmastiff, a popular Mastiff breed that the person may not have thought of using as a query.

![](images/b5a2d8171172f0b33d3f06b01111cb1b7284275e7847f4c325eb6194170897a9.jpg)  
Figure 7.5: This wireframe is for a useful combination of Auto-Complete and Auto-Suggest in the Pet Shop App.

Mastiff is also a generally accepted synonym for a query “large guard dog,” so the auto-suggest layer can expand the original query by suggesting a category Guard Dogs, which can expand into a number of related breeds the person might not have thought of originally, such as Doberman, Rottweiler, American Bulldog, and so on. Both Auto-Suggest and Auto-Complete automatically scope the suggestions using a controlled vocabulary with a preset list of recommended search terms that match common tasks the app supports.

## Tablet Apps

Tablet auto-suggestions represent a different use case from auto-suggestions on mobile devices. In principle, large tablets do support mobile activities; in practice, the mobility pattern for a typical consumer large tablet device is found in the area between the refrigerator and the couch, as user researcher Marijke Rijsberman explains in her perspective “A Fine Line: The iPad As a Portable Device,” which is in my first book Designing Search (Wiley, 2011). Simply put, it is more common for large tablets to be used as casual, “lean back” devices.

Typing on large tablets is easier and less error prone, so they are closer to desktops and can use the same auto-suggestion database as a desktop web application. Also, one-tap auto-suggestions that jump directly to a different app are not as important on large tablets as they are on mobile devices because people on tablets are typically not in as much of a hurry and are less likely to mind a few additional taps, as long as it’s clear that they are progressing toward their goal. Also, local results are generally not as important as they are on mobile devices; however, they should definitely be included.

Note that this does not necessarily apply to mid-size 7-inch tablets and notetablet hybrids (refer to Chapter 3, “Android Fragmentation”). These smaller tablet devices are at once more mobile and harder to type on than their large counterparts. For the purposes of this pattern, these smaller tablet devices can be treated as mobile phones, and you should design for them accordingly.

Finally, another consideration is the interface element. In mobile devices, the auto-suggestions layer often occupies the entire page, whereas on a tablet autosuggestions are presented in a popover layer occupying only a small part of the screen. (For more on tablet design patterns, see Chapter 14, “Tablet Patterns.”)

## Caution

If you do provide a custom auto-suggest layer (which is highly recommended) remember to turn off the device’s auto-suggest feature.

Remember that mobile phones are a different class of device. They may require a completely different auto-suggest approach (one of such mobile-only approaches is described in the next pattern 7.3 “Tap-Ahead”). Mobile Auto-Suggestions are prioritized differently because they are meant to respond to different needs. Mobile devices need to give higher weight to auto-suggestions based on on-board sensors that are only available on mobile devices. For example, local auto-suggestions, previous mobile search history and category browsing (for example, Guard Dogs, as described in the Pet Shop example) need to be higher on the list than typical desktop web auto-suggest options, which are mainly controlled vocabulary substitutions.

People misspell things differently on desktop web and tablets with full keyboards than on smaller mobile devices. Mobile misspellings mainly arise due to fat-fingering, not from common spelling misconceptions. This dictates ideally using and maintaining a different database for mobile auto-corrections that take the unique nature of mobile keyboards into account.

## Related Patterns

7.3 Pattern: Tap-Ahead

7.1 Pattern: Voice Search

## 7. 3 Pattern: Tap-Ahead

Tap-Ahead implements auto-suggest one word at a time, through step-wise refinement, creating a kind of keyword browsing.

## H ow It W orks

Instead of trying to guess the entire query the customer is trying to type at the outset and offer the best one-shot replacement the way desktop web does, Tap-Ahead on mobile devices guides the auto-suggest interface through the guessing process one phrase or keyword at a time.

This is how it works: When the searcher enters a few characters, the autosuggest function offers a few query suggestions. At this point the searcher has two choices:

■ Tap the query if it is a sufficiently good match for what she is looking for.

■ Tap the diagonal arrow on the right side of the screen to populate the search box with the query keywords, and execute the auto-suggest function again.

By giving the searcher the ability to “build” the query instead of typing it, the interface offers a much more natural, flexible, and robust auto-suggest method that’s optimized to solve low bandwidth and fat-finger issues people experience on mobile devices. Using the Tap-Ahead interface, customers can quickly access thousands of popular search term combinations by typing just a few initial characters.

## Example

An excellent example of this pattern is the Android native search (see Figure 7.6). As you can see from the following example, the Tap-Ahead pattern offers an excellent alternative to typing longer multi-keyword queries.

![](images/89bcebb8e64d573ce88223adc28fe2719c911bc4ea414c4014852c2894254a1d.jpg)  
Figure 7.6: The Android 4.0 Native Search includes an implementation of the Tap-Ahead pattern.

In this case, by tapping the diagonal Tap-Ahead arrow, the searcher could enter a complex query “Harry Potter spells app” by typing only four initial characters (harr) and tapping the diagonal arrow two times. The traditional one-shot autosuggest interface is unlikely to be able to offer this entire fairly unusual phrase as an auto-suggestion, so the customer is likely to have to type most, if not all, of the 23 characters of the query Harry Potter Spells app.

## W hen and W here to Use It

Use the Tap-Ahead pattern anywhere the auto-suggest is used outside a oneshot controlled vocabulary auto-suggestion and where longer, multistep, multikeyword queries offer an advantage and create a better set of results.

## W hy Use It

In contrast to desktop web search, auto-suggest on mobile devices is subject to two unique limitations: It’s harder to type on a mobile device and signal strength is unreliable. Tap-Ahead solves both issues in an elegant, minimalist, and authentically mobile way. Tap-Ahead enables the mobile auto-suggest interface to maintain flow and increase speed and responsiveness on tiny screens that is simply not possible to currently achieve with the traditional one-shot auto-suggestion interface.

Is there evidence of this? The author’s field research shows that in mobile environments people often select search suggestions they do not need, just to save typing in a few characters. (Read more about this in “Mobile Auto-Suggest on Steroids: Tap-Ahead Design Pattern,” Smashing Magazine, April 27th, 2011, http://www.smashingmagazine.com/2011/04/27/ tap-ahead-design-pattern-mobile-auto-suggest-on-steroids/). Tap ahead effectively resolves this issue.

## Other Uses

For the few years that the Android platform has been around, the keyword suggestions have evolved from being an exact match to Google’s web suggestions to being its own mobile-specific set. Yet you can do even better in your own app by using a simple trick: Offer Tap-Ahead one keyword at a time.

The advantage of the one-word-at-a-time Tap-Ahead refinement interface is that the refinement keywords can be loaded asynchronously for each of the 10 autosuggestions while the customer makes the selection of the first keyword. Given that most queries are between two and three keywords long, and each successive auto-suggest layer offers 10 additional keyword suggestions, Tap-Ahead with step-wise refinement enables customers to reach between 100 (10 \* 10) and 1,000 (10 \* 10 \* 10) of the top keywords through typing only a few initial characters.

Anecdotally, although Tap-Ahead is useful, few people have discovered its power to cut through tediousness and all the fat-finger mistakes associated with typing. By offering keywords one at a time, the interface is optimized for the Tap-Ahead pattern, so discovery should increase, thereby also increasing the satisfaction. Tap-Ahead one word at a time is an excellent variation of the Tap-Ahead for e-commerce apps.

## Pet Shop Application

It’s easy to imagine Tap-Ahead being useful in entering complex keyword queries. However, it’s not as important with dog breeds, for example, which form a controlled vocabulary. There is scant advantage to provide a Tap-Ahead expansion from Mas to Mastiff to Neapolitan Mastiff because there are not many queries that start with Mastiff. Instead, a simple, traditional one-shot controlled vocabulary auto-suggestion (Mas directly to Neapolitan Mastiff) is a more useful approach because it not only allows the user to pick up standard keyword queries such as English Mastiff and Neapolitan Mastiff but also an interesting keyword variation Bullmastiff and category expansion Guard Dogs (see the “7.2 Pattern: Auto-Complete and Auto-Suggest” section).

## Tablet Apps

The owners of large tablets are generally more willing to type a longer query, and low bandwidth is usually less of a problem for them (many tablets are used with Wi-Fi only). Nevertheless, Tap-Ahead is no less useful on tablets, where less work is perceived as a good thing and tapping a suggestion is as easy as tapping the next character on the touch keyboard. There is also early evidence that tablet queries are slightly longer, which also speaks in favor of keyword browsing.

## Caution

The best auto-suggestions on a mobile device come from a database that’s different and distinct from the web auto-suggestions database. This is especially true for Tap-Ahead implemented one keyword at a time—but that’s how important this function is to creating an excellent search experience!

At this point it’s not clear who, if anyone, holds a patent on this functionality.   
Google began using it first in its general device search and Google App for iPhone;   
although it is not used for single keyword browsing as of the time of this writing.   
Microsoft and Apple are both likely actively pursuing similar patents.

## Related Patterns

7.2 Pattern: Auto-Suggest and Auto-Complete

## 7. 4 Pattern: Pull to Refresh

Search results are refreshed when the customer swipes down (pulls down) on the results. Slick and convenient, this is a great pattern to refresh results that update frequently.

## H ow It W orks

The customer is presented with a long list of updates, typically sorted by Time: Most Recent First. The customer typically reviews the list of updates starting at the top, reading the most-recent messages first. When the customer wants to load newer updates, he pulls down on the results list, performing a scrollup function. Typically, a watermark appears that lets the customer know that when he pulls down and then releases the list, it will update. The system issues an update call, which is reflected by a visible timer, followed by loading of the updated results.

## Example

A great example of this pattern is the original application that helped popularize it: the Twitter mobile app. (See Figure 7.7.)

![](images/a674fa606c382e566a227d59d0c00bbead2b07aea1ba841b20327cc71dedfd93.jpg)  
Figure 7.7: The Pull to Refresh pattern was popularized in the Twitter app.

## hen and W here to Use It

Use Pull to Refresh for long lists of search results or updates sorted by Time: Most Recent First. This pattern is especially useful for social update streams, active inboxes, and other long lists that update frequently.

## W hy Use It

The Pull to Refresh pattern uses a gesture instead of a button, which is always an excellent idea if you can communicate the needed gesture in an obvious and unobtrusive way. For Pull to Refresh, the gesture needed is the one the customer already uses to scroll the results up, so the call to action naturally “dissolves in behavior.”

When the customer first loads the results, he typically engages with the list by scanning or reading the newest updates or search results first, starting at the top, and scrolling down the list to read or scan more. When the customer reads far enough down and wants fresher results, he naturally scrolls to the top and keeps scrolling until he reaches the top of the currently loaded results and scrolls past the top of the list. At that point he sees the watermark telling him what to do to load the newest results. This often happens naturally and in the state of flow, when the customer flicks rapidly to scroll the results quickly.

One other point makes this pattern feel natural. The action to pull down on the list “pulls” new data from the server, which is an excellent fit to the customer’s existing mental model. This is a fine example of using unique capabilities of mobile and tablet touch devices to expand on the desktop web model of buttons and links.

## Other Uses

Most applications of this pattern deal with search results or updates sorted by Time: Most Recent First. Another possible application might be triggered by transversing space instead of time. For example, if your customer looks for points of interest around him as he moves through a city, he has a different set of attractions within walking distance as he moves. Depending on the specific goal of the interaction, you can use the Pull to Refresh pattern to show the search results list sorted by Distance: Nearest First. This way, as the customer moves through the city, he can have an updated list of points of interest around him with a flick of a finger.

## Pet Shop Application

One possible way to use Pull to Refresh in the Pet Shop app is to show updates of lost pets. If your pet is lost, for example, you can stay on top of the search with the updates page that tracks found pets in your neighborhood by periodically pulling to refresh the list. However, forcing the customer to do this may be a stressful activity if the list keeps coming up empty or static. If the list is mostly static, instead consider using some sort of a push alert (an alert that is loaded on the device and shown automatically, as opposed to being triggered by some action the customer explicitly needs to take) that notifies the customer when a new pet is found. To create a push alert a polling technology is frequently used, but from the standpoint of the customer, the alert is being “pushed” to him.

## Tablet Apps

Pull to Refresh works just as well on medium- and large-size tablets as it does on mobile phones. The vertical space needed to communicate Pull to Refresh should grow proportionally to the size of the device and the extent of a gesture needed to scroll the results. Larger tablets require longer, more sweeping gestures with which to execute the “pull.”

## Caution

Although it’s tempting to use it due to the pattern’s sheer coolness, Pull to Refresh is not recommended for the majority of search results that deal with mostly static content. It is simply not satisfying to execute a pull and release and get the same data, and the watermark on the top of the list becomes chart-junk—a useless distraction. Other counter-indications of Pull to Refresh is for lists sorted in ways that do not lend themselves to rapidly updated content, such as Best Match, Price, and so on.

Here’s another thing to keep in mind: The Pull to Refresh pattern is patented. That’s right; Twitter currently holds the patent on this design. Although it’s unlikely that Twitter would go after anyone other than a direct competitor using this pattern, it’s an important caveat to keep in mind if you plan to use it in your app.

## Related Patterns

None

## 7. 5 Pattern: Search from M enu

Search is an option that can be accessed from the navigation bar menu.

## H ow It W orks

To do the search, the user must tap the menu button in the phone’s navigation bar (that also houses the Back, Home, and Recents buttons) and then select the Search option. After Search has been tapped, the resulting page may show one or more of the following: saved searches, search refinement options, popular searches, nearby locations, and so on.

## Example

In the Amazon app (see Figure 7.8), the customer accesses the search feature by tapping the magnifying glass in the menu located in the navigation bar.

![](images/3929c8ff31cb056543498aa9d6ddf75e8b28185ec64a8631e2cda3597715dab6.jpg)  
Figure 7.8: The Amazon app uses the Search from Menu pattern.

The resulting Search page shows the previous query and a list of alternative query entry mechanisms, in this case a picture or a barcode that the customer can scan with an on-board camera. The menu is opened from the phone’s navigation bar, which has been dynamically modified to add the app menu function.

## W hen and W here to Use It

Despite being used by some of today’s leading apps, this pattern is now largely deprecated. Most of the native Google apps in Android 4.0 have a dedicated Search button on the app’s action bar or in the overflow menu (see the “7.6 Pattern: Search from Action Bar” section later in this chapter). Search from Menu is a transitional pattern that can still be used for a short time (or at least until the Android 4.0 Police show up) as a way to bridge apps in older Android versions with those in Android 4.0.

## W hy Use It

This is a popular pattern descended from older Android OS implementations, which recommended that the app’s menu button always be present in the device’s navigation bar. This handy pattern enables the designers to hide the search along with most of the rest of the navigation, on the navigation bar, which often eliminates the need for an additional action bar. This provides the advantage of a simple interface and “taller” vertical space so that more screen space is devoted to products or content.

## Other Uses

Some older Android implementations, most notably those on the Motorola and LG hardware, provide a special dedicated hardware accelerator button for search. Tapping this button is the equivalent of tapping the menu button in the navigation bar and selecting Search from that menu.

This dedicated Search button has been removed from the latest hardware designed to run Android 4.0. You can speculate as to what this means long term, but in the immediate Android future, Search from Menu and Search from Action Bar search design patterns appear to take precedence over the dedicated hardware button.

## Pet Shop Application

In implementing this pattern with the Pet Shop app, there are two options of what to put on the Search page. One option is to provide alternative input methods (refer to the Amazon app shown in Figure 7.8). Other popular options include previous searches and search refinements, such as filtering or sorting. Figure 7.9 shows previous searches.

![](images/bfc7c3731d004f523abb1f5d856d125f1e6faee861e142834e1cceecf1c23f34.jpg)  
Figure 7.9: See the Search from Menu with previous searches in the Pet Shop app.

When showing the alternative query entry mechanisms such as barcode scan, picture, voice, NFC, and so on, recent previous searches can be shown as a grouped button (Recent Searches); although, this is generally less effective than actually listing previous queries in the list. Whatever strategy you decide to use, be sure to highlight (select) the current query as shown or provide an X or Clear button for the searcher so that starting a new search is easy.

## Tablet Apps

Tablets do not generally need to use this pattern because there is plenty of room to install a dedicated search box or use the Search from Action Bar pattern instead.

Also, the Search from Menu pattern is ergonomically inferior to most other tablet patterns of search implementation because the menu button moves around constantly. In portrait mode the tablet’s navigation bar is on the bottom of the device, which makes it generally awkward to access a menu from a normal tablet viewing position. (Read more about ergonomics in Chapter 3, “Android Fragmentation”.)

## Caution

In addition to this pattern being deprecated in Android 4.0, using Search from Menu can lead to an awkward separation of the keyword query from the refinement tools. See the “7.9 Antipattern: Separate Search and Refinement” section.

## Related Patterns

7.6 Pattern: Search from Action Bar

8.4 Pattern: Parallel Architecture

7.9 Antipattern: Separate Search and Refinement

## 7. 6 Pattern: Search from Action B ar

The customer can access search via a dedicated button on the app’s action bar.

## H ow It W orks

The Search button (usually styled as a standard Android magnifying glass icon) is shown on the top or bottom action bar. After the user taps Search, the resulting page shows one or more of the following: saved searches, search refinement options, popular searches, nearby locations, and so on.

## Example

Google Plus offers an excellent example of this pattern (see Figure 7.10).

![](images/6452d4c8125e2153b690909b654b189051a367a9ba81e52b436954e268ac97ca.jpg)  
Figure 7.10: The Google Plus app uses the Search from Action Bar pattern at the top of the app.

Google Plus offers a dedicated Search button on the top action bar. Tapping the Search button navigates the user to the dedicated tabbed search page, with two search subdomains, Posts and People, displayed as tabs. Tabs are a common pattern in search, as discussed in Chapter 9, “Avoiding Missing or Undesirable Results.”

Another example of the dedicated Search button in the action bar is in the Android Messaging app.

![](images/f8f41af2141266ec5f6406849c5ed23eadf272e4a5f28dc1e89b0d9ba078f276.jpg)  
Figure 7.11: The Android Messaging app includes the Search from Action Bar pattern in the split action bar at the bottom of the screen.

In the Messaging app, the Search button is in the middle of the split action bar, which is at the bottom of the screen. Inconsistent? Sure. But relative freedom of placement of controls on the screen is a large part of the Android DNA (refer to Chapter 2, “What Makes Android Different”).

## hen and W here to Use It

Any time you have an action bar in your app that has some space on it and search is important to your customers, this pattern is a great choice. Ergonomically, placing the Search button on the bottom of the split action bar makes it easier to access the function one-handed.

## W hy Use It

Although I am not aware of any official standing on the matter, it seems that the Google Android team has made a real effort to generally replace the Search from Menu pattern with the Search from Action Bar pattern, at least in native Google apps in Android 4.0. This is a strong signal that search remains important at Google. If search is likewise important to you, this pattern is an excellent choice and is now more or less “official” (to the extent that anything in Android can be considered official).

## Other Uses

When the app’s screen real estate shrinks due to the size of hardware that runs it, some action bar functions may move into the overflow menu, as discussed in Chapter 1, “Design for Android: A Case Study.” In this case, the search function shown on the action bar might be forced into an overflow menu as well. To access the search function, the customer will have to tap the overflow menu and select Search—pretty straightforward.

## Pet Shop Application

Contrast the Search from Action Bar pattern shown in Figure 7.12 with the Search From Menu pattern referred to in Figure 7.9.

![](images/d31172fd488ad2f231b777ff1ef023f40de1bfa5f73ac1f0d51f4d4b23cccdf9.jpg)  
Figure 7.12: Check out the Search from Action Bar in the Pet Shop app.

Both patterns enable access to the search page from anywhere in the application and use the same search page design. However, with the Search from Action Bar pattern, getting to the search page is accomplished via a single tap on the dedicated Search button on the App bar rather than in the two taps required by the Search from Menu pattern. Search from Action Bar saves an extra tap and surfaces the search much more prominently in the mind of the customer. There is a drawback, however; using this pattern adds an action bar, which takes away precious pixels from the vertical space available for viewing content and products.

## Tablet Apps

This is the standard search pattern to use in tablet apps. However, if you use the standard top action bar layout that places the search icon somewhere close to the middle of the action bar (refer to the Messaging app in Figure 7.11), your customers may get a severe case of what Josh Clark has dubbed “Tablet Elbow” if they must tap this button often (read more in Chapter 3). A better placement of this button is on the right or left nav bars, which run vertically along the edges of the device (see Chapter 14 to find out more about tablet-specific patterns).

## Caution

Similar to Search from Menu, Search from Action Bar can also lead to an awkward separation of the keyword query from the refinement tools. See the “7.9 Antipattern: Separate Search and Refinement” section.

## Related Patterns

7.5 Pattern: Search from Menu

8.5 Pattern: Tabs

7.9 Antipattern: Separate Search and Refinement

## 7. 7 Pattern: Dedicated Search

The search box is placed on top of the search results and does not scroll with them.

## H ow It W orks

The search box sits on top of the search results, which enables customers to easily edit and fine-tune the keyword query. Often, a refinement (filter) button is placed to the left or right of the search box.

## Example

A great example of this pattern is Yelp, as shown in Figure 7.13.

![](images/8bd6741252a569e564201d05f91ef5a8aef1dd9565780b96dfd0f5f69ea26ac3.jpg)  
Figure 7.13: The Yelp app includes a good example of the Dedicated Search pattern.

The dedicated search box in Yelp sits on top of the search results and does not scroll when the search results are scrolled. In addition, search tools, such as Filter and Map, are located on the same line as the search box.

## W hen and W here to Use It

For apps in which search is a key part of functionality, the Dedicated Search pattern is an excellent choice. The Dedicated Search pattern shows clearly what keyword query yielded the search results and provides convenient, dedicated tools to change the query and access other refinements.

## W hy Use It

As Peter Morville and Jeff Callender so eloquently stated in their book Search Patterns (O’Reilly, 2010), “What we find changes what we seek.” Nowhere is this statement truer than in the mobile space, where typing is awkward and people are highly distracted with multitasking. People prefer to start general and refine rapidly, and changes to the keyword query are part of that refinement. The Dedicated Search pattern addresses the need with unmatched simplicity and elegance. The original keywords that the searcher types are always visible on top of the results and are retained in the search box for easy editing.

## Other Uses

If additional filters and sort options are used with the keyword query, the Dedicated Search pattern combines well with the Filter Strip pattern that shows filters and query refinements (see Chapter 8, “Sorting and Filtering”). Together, these two patterns show the searcher the entire contents of a complex query.

## Pet Shop Application

Figure 7.14 shows the implementation of the Dedicated Search pattern.  
![](images/63cb3780c670743a4a4bffcc25362d9aef57462edd8e1dd6897f60eae5efaccd.jpg)  
Figure 7.14: This is how the Dedicated Search pattern looks when used in the Pet Shop app.

This is a fantastic pattern for the Pet Shop app if you expect customers to edit their queries often.

## Tablet Apps

Tablets are much less screen space–challenged than mobile phones. For most apps that use search, having a dedicated search box is an excellent idea. Simply having a dedicated search box on top of every page in the app implements the Dedicated Search pattern nicely.

## Caution

Having a dedicated search box on top of the page does not mean that you need to give up the person’s history of previous searches or auto-correct functionality. Remember that previous searches can be easily presented via a layer under the search box (refer to the “7.2 Pattern: Auto-Complete and Auto-Suggest”).

On smaller devices this pattern takes up a fair bit of vertical space (20 to 30 percent of the total screen space), which significantly reduces the number of products or the amount of content that can be shown to the customer. The Dedicated Search pattern is akin to reducing the number of books that can be shown on a bookstore shelf because of the giant sign that tells you the name of the section. It’s not always a bad thing, but it is something to keep firmly in mind.

## Related Patterns

8.3 Pattern: Filter Strip

7.2 Pattern: Auto-Complete and Auto-Suggest

## 7. 8 Pattern: Search in the Content Page

The search box is on top of the search results and part of the content page, so it scrolls with the rest of the content. This pattern is an alternative of the Dedicated Search pattern.

## H ow It W orks

The basic premise of this pattern is that the search box is part of the content page. When the page first loads, the search box is shown to the customer. As the customer scrolls the content page down, the search box simply scrolls out of view with the rest of the content. To search, the customer must scroll back to the top of the page.

## Example

The Twitter app makes an effort to have a consistent interface on iOS and Android, which makes it a good example of the Search in the Content Page pattern (see Figure 7.15).

![](images/fb1725a5dbc260c061b38835d133c58d2cc6a3811bdcaf85e5cdfa493202b5b3.jpg)  
Figure 7.15: This is how the Twitter app uses the Search in the Content Page pattern.  
This pattern works well with the Pull to Refresh pattern described earlier.

## hen and W here to Use It

Any time you have a screen that is content-centric but might need to be occasionally searched, Search in the Content Page is a great option. However, make sure that your customers want to only run keyword queries and that sort order is obvious and does not need to be changed. Ideally, people never want to have any refinement on the query because this pattern generally makes search refinement awkward.

## W hy Use It

This pattern is popular in iOS but is currently seldom used in Android. That’s a shame because it’s ideal for certain applications. In particular, content-centric screens such as name lists or activity streams such as updates, which are normally browsed but not searched, make great candidates for use of this pattern.

The Search in the Content Page pattern makes search easily available but does not take up permanent screen space the way the Dedicated Search pattern does.

## Other Uses

One modification popular in iOS but virtually unknown in Android is Scroll to Search. When a content page loads, a search box is hidden on top of the page. Pulling the page down reveals the search box that searches within the content on the page. After the query runs, the resulting page shows the search box with the query.

## Pet Shop Application

This pattern is not suitable for e-commerce because it makes refinement awkward. However, you can use it for an update stream or Pet News section, where search is likely to be infrequent and made up of keyword queries (see Figure 7.16).

![](images/f171a366599bbdf230254abdbfe46633a5d23f31b4133ceba6a00072596ee219.jpg)

![](images/6438db919497caf4bb03f42cf3b4ad7efffa52013b7ac5c2539ef5ffe7804056.jpg)  
Figure 7.16: The Search in the Content Page pattern appears in the Pet News section of the Pet Shop app.

![](images/a8437f260dc3c183ff91bca3beb498ab33379d6514c885f81c17c2ae65bf3ad6.jpg)

## Tablet Apps

This pattern is all about saving space, which makes it superfluous for tablets, which generally have enough space. However, it still has its place because it is easy to implement.

![](images/9346cc96c96698742094bd4a3f1db60b275d20da02164970918a88fcf1a7d45e.jpg)

## Caution

This pattern is currently rare on the Android platform but is quite widespread on iOS. The reasons for this are not clear. One possibility is that iOS enables a quick scroll to the top of the page (which thereby “jumps” to the search box) using a single tap in the middle of the top App bar. This single tap jump to the top of the page shortcut is unavailable on Android because the top of the screen is normally occupied in the Android OS by the Notifications strip, which understands the pulldown touch gesture. This could make frequent use of search functionality in Search in the Content Page implementations problematic on Android because the person must deliberately scroll back to the top of the page “the long way” to reveal the search box.

For the Scroll to Search modification of this pattern described in the “Other Uses” section, the reason could be even simpler but more insidious. Although at this time I’m not aware of any limitation, Apple could be holding a patent to this pattern, so Android apps are generally prevented from using it (or it could be more popular in iOS simply from lack of screen space, which is less of a problem with larger Android devices). If you’re in doubt, use the simple version of this pattern implemented by Twitter as described in the “Example” section.

## Related Patterns

7.7 Pattern: Dedicated Search

7.4 Pattern: Pull to Refresh

## 7. 9 Antipattern: Separate Search and R efinement

An awkward experience results when the keyword query search box is removed by two or more taps from the other search refinements.

## W hen and W here It Shows Up

Any time the keyword query and multiple complex refinement options are separated, you must pay attention. Although this shows up frequently on iOS, this antipattern is especially an issue on Android because of the widespread use of dedicated search pages, the result of Search from Menu and Search from Action Bar patterns.

## Example

It’s easy to mess up when blindly copying successful apps and applying a slightly different paradigm. For example, the Amazon app manages to pull off using Search from Menu and a separate keyword search page successfully by using a simple filter drop-down located in-page with the rest of the content (refer to Figure 7.8).

Contrast the Amazon app search and filter scheme with that in TheFind, as shown in Figure 7.17.

![](images/339316e6a4278372c8ff8361ae8cdbac6e0265c73d204d46a388069c41c8775d.jpg)

![](images/52be97a5d95d7e2b003085e43e935a067d0fc1d1df14b01f56391fa2f8d88909.jpg)  
Figure 7.17: There’s an awkward separation of keyword search from the rest of the search refinements in this antipattern from TheFind.

The refinement page is a dedicated page with multiple text fields. One thing is conspicuously absent: the keyword search box. To change the keywords in the query, the user must tap the Menu button and then tap Search. This separation is completely artificial and therefore awkward, which should be avoided.

## W hy Avoid It

In most people’s minds, search is an iterative activity. (Recall Peter Morville’s quote, “What we find changes what we seek.”) So in the mind of searchers, there is little separation between keywords, filters, and sort options. These are all tools to find what they want. Separate Search and Refinement is an antipattern precisely because it introduces awkward separation between the keyword query and everything else. This is neither wanted nor needed. Separate Search and Refinement breaks the association between different parts of the query and makes it difficult to find what you want and stay in the flow.

A better pattern called Parallel Architecture or any of the simple faceted search patterns covered in Chapter 8 offer a more usable configuration.

## Additional Considerations

Although often harder to recognize, the Separate Search and Result antipattern also occurs when search is presented in a different way on the homepage and on a separate search page. For example, TheFind app also offers a different search from the homepage shown in Figure 7.18.

![](images/ca528ac9ac5041be9c62e1839064c8c06770438634b3d67b1fbd5b0291127bba.jpg)  
Figure 7.18: In this antipattern there are two slightly different places for a keyword search in TheFind homepage and dedicated search page.

Although it has similar search functionality at first glance (neither one have any refinements, for example), the homepage search doesn’t have the previous search’s history widget that the dedicated Search page has. This “separate homepage search” antipattern is a child of the Separate Search and Refinement antipattern. It can be daunting to customers who quickly get lost.

Unfortunately, this situation happens quite often and is much harder to recognize and prevent. Two great solutions for this issue are the Parallel Architecture pattern, where the homepage is the basic search page, and the Dedicated Search pattern, which presents a consistent search box and functionality on the homepage and search results pages.

In general, it’s a good idea to offer the same basic search functionality every time you have the search box. If you offer history and auto-suggest in one place, do it everywhere you use the basic search box. Also, avoid having multiple places for search that differ only slightly; it makes it too easy for people to get lost and confused and abandon search altogether.

## Related Patterns

8.4 Pattern: Parallel Architecture

7.5 Pattern: Search from the Menu

7.6 Pattern: Search from Action Bar

7.7 Pattern: Dedicated Search

C h ap t e r 8

## Sorting and Filtering

After your customers get the information scent that lets them know they are on the right track to finding what they need, the next step is to help them winnow down the avalanche of data to the size manageable in the mobile context of use. That’s where the sorting and filtering design patterns in this chapter prove invaluable. Many of the so-called Experimental Patterns, such as Sliders with Histogram (Chapter 10, “Data Entry”) and Filter Accelerators (Chapter 11, “Forms”) can also be used for sorting and filtering, so be sure to also check out relevant sections in those chapters.

![](images/69db8c00dcec08ca52b412404e4fecfbcaad42bd76f62e9891a9934b692efe4b.jpg)

## 8. 1 Antipattern: Crippled Refinement

Before talking about refinement patterns, let me make something very clear: Mobile web should be as good as desktop web, or better. Crippled Refinement is a fundamental UX antipattern to be avoided at all costs.

## W hen and W here It Shows Up

Whenever there is an option to filter and sort mobile or tablet search results, there is a great temptation to “dumb down” the interface to only one or two refinement options. Additionally, mobile interfaces that limit search refinement to a single step fundamentally cripple the flow of search experience, which proceeds via multiple consecutive refinement steps.

## Example

Although it is overall a highly successful and lucrative mobile app, Amazon provides the example of a dumbed-down filtering process.

Just compare the only refinement option, Department (see Figure 8.1), available in the mobile app to the multitude of filters and sort options available for the same “Harry Potter” query in a desktop browser, as shown in Figure 8.2.

![](images/468f159890e9a27fdf6efccc07e0b74ee5c86adf9bad8bf4755a9e6f6ec520c2.jpg)  
Figure 8.1: The Amazon app includes an example of the Crippled Refinement antipattern.

![](images/b1c05054ef617ca2350def2054f3365d7d14e37932d233356dee1319999981dd.jpg)  
Figure 8.2: Here’s a battery of filters and sort options in the Amazon.com desktop web.

The mobile app seems rather seriously deficient, doesn’t it? But the real, more insidious UX problem is deeper still. Typical search flow involves multiple steps of refinement and changes, with each step directly informing what the customer will do next. Because the Amazon mobile app refinement is designed to be only a single-step operation, the interface does not support any changes to the original keyword query. Actually, any changes to the query reset the entire search (see Figure 8.3).

Referring to the sequence of steps pictured in Figure 8.3, the searcher started the search broadly, by searching for Harry Potter. Remembering that his niece wanted a DVD, he picks a category Movies & TV. Viewing the items in the search results, the searcher realizes that he wanted to see all the buying options for the first movie, Harry Potter and the Sorcerer’s Stone, so he taps the Menu button and selects Search once more, updating the keyword query to include the full name, Harry Potter and the Sorcerer’s Stone. At this point, the searcher unexpectedly finds his category reset back to All Departments—his refinements gone, his discovery flow interrupted.

The best mobile interfaces support multistep refinements, allowing the customers to do more, not less, than the desktop interface.

![](images/2a554c522ab907fab063df41fec4398533c08df0cc7fb27d06baf3f18e2042b6.jpg)  
Figure 8.3: The Amazon mobile app does not support multistep refinement.

## W hy Avoid It

Edward Tufte (the “Da Vinci of Data”) famously quipped, “Clarity and simplicity are completely opposite of simple-mindedness.” Nowhere is this adage more true than in mobile and tablet design. Mobile and tablet apps must support most if not all the desktop web filters and make available what you know to be a multistep refinement finding flow.

If you decide to provide less functionality simply because you think it is too much to handle for mobile customers, think again. Experience with crippled apps such as the early version of Facebook clearly shows that people want to do more with mobile apps, not less. Instead of dumbing down, think of the way to provide filtering and sorting functionality that works with the on-board sensors and device limitations.

The key to great mobile design is not really having customers doing more (that is more work), but getting more: more capabilities, more value out of the experience. Well-designed mobile interfaces actually enable people to do less work because you can leverage other sensor data to infer more of the customer’s context. You could say people want more or expect more from their mobile device, which means they want to do less. The key is context and real human desires, not doing more or less because of some abstract principle. Use the patterns in the rest of this chapter as a guide and be sure to test early and often with your target customers.

## Related Patterns

All patterns in this chapter

## 8. 2 Pattern: Refinement Page

Search results enable access to sort and filter options on a separate page or lightbox.

## H ow It W orks

When the customer wants to refine the query, he can access a dedicated page or a lightbox with filter and sort options, followed by some sort of a “go” button to re-initiate the now refined search. Optionally, the set of refinements applied to the search might be shown to the customer with a Filter Strip design pattern. (Filter Strip is covered next, in section 8.3.)

## Example

One excellent example of a full-featured mobile refinement is the eBay app. (See Figure 8.4.)

![](images/a34ee32c84b8697d6c602c2c34885b1c89ef568a77950265a0da15009d55f4ca.jpg)  
Figure 8.4: The eBay app is an excellent example of a Refinement Page pattern.

Despite apparent complexity, this remains one of the most useful and profitable mobile apps, with several billion mobile e-commerce dollars generated as of the date of this writing. One reason for its success is that designers refused to dumb down the experience and have instead done an excellent job managing complexity: The app provides a full-featured eBay search experience in a tiny mobile device.

This app makes an excellent example because it shows off some uncommon but useful refinements, including

■ Multiple select check boxes (Free Shipping, US-only) as shown in Figure 8.5

■ Multistep drill-down refinement (Refine c Category c Sporting Goods) with additional subcategories (see Figure 8.6)

Sort on the same refinement page as search (Best Match and so on) as shown in Figure 8.7

![](images/f14e1ce0a98e7e504a0401b7d253dd05d1f99aa06e05d71aa05d2bac9269abb3.jpg)  
Figure 8.5: One uncommon refinement in the eBay app is the use of multiple select check boxes.

![](images/82ac437feebc15cbbff891ad5c7b43e68b6e8e0ef47e2bc88729833fe4f0c02c.jpg)  
Figure 8.6: This is an example of drill-down refinement.

![](images/bb0802a6d4c55292486375e412e04568465fd803d64de4a13f76c0f2a0eae507.jpg)  
Figure 8.7: The eBay app provides both search refinement and sort in the same Refine page.

But the eBay app not only offers full-featured refinements, but also actually does more than the desktop web version—for example, offering refinement by distance from the current location without having to enter the ZIP code (see Figure 8.8).

![](images/1707f35b205ecbdbd5901632addd66d2f30200b19fd0e3cb05911e6400ad5f30.jpg)  
Figure 8.8: The Refinement Page pattern in the eBay app offers distance-based refinement.

## W hen and W here to Use It

Any time you have a faceted search or there is a use case for changing the sort order, the Refinement Page pattern is an excellent tool for the job.

## W hy Use It

Refinement is an essential part of search, especially on the mobile device where typing avoidance generally gives rise to shorter, more general queries, which need to be refined quickly and efficiently.

## Other Uses

Some of the best implementations of the Refinement Page pattern are not pages at all. They are Refinement Page lightboxes (also somewhat loosely called popups). Early Android phones simply did not have sufficient real estate to implement refinement in a lightbox that could still be operated with fat fingers, and the iPhone’s smaller size still prevents iOS designers from doing this effectively in most cases. However, today’s higher-end Android devices have a decent-size screen, which means multiple refinement options can be displayed in a lightbox, as shown in Figure 8.9, demonstrating the excellent Yelp refinement example.

![](images/b9539923fe997e605179a6c6a322afacda2831718e837da6d172ba3d1e7b9318.jpg)  
Figure 8.9: The Refinement Page Lightbox in the Yelp app is a good implementation of the pattern.

Why is there a distinction between lightboxes and dedicated pages? The reason has to do with maintaining flow within the current task. As discussed in greater detail in Chapter 13, “Navigation,” immersive UIs (of which Refinement Page Lightbox is a good example) maintain the illusion of staying on the same page and within the same task, whereas separate pages appear to switch the task from one interacting with the content to that of refinement. Separate pages yank the person out of the search results and place her in a different environment. If you can accomplish your refinement tasks using a lightbox without sacrificing functionality, it almost always creates a better experience.

## Pet Shop Application

Either the dedicated refinement page or lightbox refinement could be usable for the faceted refinement and sorting in the Pet Shop app. What makes the design of the refinement functionality even better is the addition of the Filter Strip pattern. In the next section, the entire package is wireframed together using the agile sticky notes methodology.

## Tablet Apps

Refinements are important for tablets. Tablets have more surface area, which exposes more inventory to the customer and presumably causes them to make the decision to refine even sooner. Tablet owners also presumably care more about flow than the mobile users, and tablet search tasks last on average longer than similarly structured mobile tasks. Together these factors clearly dictate that the tablet refinements need to be as full-featured as web refinements, plus provide the refinements that are only available on touch devices (such as using the GPS locator feature for distance filtering).

Because tablets have more surface area, most refinements should be done via lightboxes, not dedicated refinement pages. Remember to place the lightbox in the correct ergonomic position where the controls can be manipulated easily in both portrait and landscape orientations. In the absence of specific use information, the best place is typically on the top-right corner of the screen, where inputs in the lightbox can be manipulated with the right thumb without the user having to let go of the device completely or while using a typical two-handed grip with the bottom of the tablet resting on the user’s lap or a table (see Chapter 3, “Android Fragmentation”).

## Caution

With the increase in screen size, there is a strong trend in many apps, such as Kayak, to have separate filtering and searching controls (large buttons on the bottom of the screen), as shown in Figure 8.10.

![](images/f9b1551668baa3a150c97d2e02920e27803f0113bc485cbaa3ed47251edcdf67.jpg)

![](images/1441278c8f4fe161a8b0ba755bf9f26636c6afc3a03df2de13727fb3239a1a5d.jpg)  
Figure 8.10: The Kayak app includes separate Sort and Filter refinement controls.

This is a mistake. As described in Designing Search: UX Strategies for Ecommerce Success (Wiley, 2011, ISBN: 978-0-470-94223-9), my original research shows that most people have trouble differentiating sorting from filtering. Furthermore, this distinction is not nearly as important as most designers and engineers think. Consider that most people will never see more than the first 100 to 300 items of a typical result set, especially on a mobile device. In other words, people can never hope to view anything but a tiny fraction of today’s typical high-volume result set numbering in the thousands. The result is The Mystery of Filtering by Sorting. In many people’s minds they filter out high-price items when they sort by Price: Lowest First, because they can never go through the entire result set to view the highprice items at the bottom of the list. Thus the action of sorting creates an inherent filtering effect due the large number of items in the set.

On mobile devices with limited screen real estate, filtering and sorting options are often placed on the same refinement page or lightbox. (Both the Yelp and eBay apps do this.) This is a great trend that should be encouraged because it matches well with the user’s mental model of these controls, which are both seen by customers as types of “refinement.” Furthermore, as I explain in my first book, sorting controls should often be shown first and called out especially because sorting often creates a much better refinement of the result set: It never causes zero results; its outcome is predictable; and it’s hard to screw it up. So, in short, you should consider combining filtering and sorting under a single Refine Area, unless there is a good reason to do otherwise, and make refinement as much of an integral part of finding, in general, as possible

Last but not least, faceted filtering cannot strictly be considered being faceted without letting the customer know the numbers of items that will result when the facets or filters are applied. Numbers of items associated with refinements let customers know how to proceed. Unfortunately, knowing numbers of items is particularly hard to do with multiple refinements being applied in a single shot using check boxes, as they are in the eBay and Yelp apps. By default, this creates a refinement experience that is inferior to that of using a desktop web browser. In your apps, if at all possible, try to indicate the outcomes of user refinement actions, including how many items will be left over after the filter is applied in order to avoid zero-results outcomes.

## Related Patterns

8.3 Pattern: Filter Strip

13.5 Pattern: Watermark

## 8. 3 Pattern: Filter Strip

A small horizontal section of the screen shows the keyword query and the filters applied.

## H ow It W orks

After the search is run, the entire contents of the query are shown to the searcher in a thin Filter Strip. Any changes to the query (such as filters applied, sort order, and so on) are continuously reflected in the Filter Strip that acts as an informational display to show the searcher the details of the exact query he applied to his search.

## Example

Yelp is a good example of this pattern. Because the Yelp app is an example of the Dedicated Search pattern (read more in Chapter 7, “Search”), showing the keyword query again is not necessary. Instead, Filter Strip (see Figure 8.11) shows up only when additional refinements (filters and sort order) are applied to the search.

Note that the Filter Strip text is small and that it wraps around in the rare cases in which this is warranted by the number of refinements applied.

![](images/8fe99bbabad0f1e5dc1faf48750bd67b1ea3a35265d3c80482bfa010b548ac24.jpg)  
Figure 8.11: The Yelp app uses the Filter Strip pattern when refinements are made to a search.

<table><tr><td colspan="2">4. Beijing Restaurant</td></tr><tr><td>1801 Alemany Blvd, Mission Terrace</td><td>$$ 7</td></tr><tr><td>★★★★★157 Reviews</td><td>Chinese</td></tr></table>

## W hen and W here to Use It

Any time a set of filters or sort refinements can be applied to a query, consideration of the Filter Strip pattern is warranted, regardless of whether the search box is a dedicated one (as it is in Yelp) or if search is initiated in some different manner as discussed in Chapter 7.

## W hy Use It

Knowing “where you are” is a continuous challenge in mobile space with its small screen and constant interruptions. Having a solid reliable way to communicate all the search parameters to the searcher enables him to adjust search parameters, sort order, and refinements until the query results are satisfactory. The Filter Strip pattern enables designers to effectively accomplish this in an unobtrusive way that takes up only a fraction of the screen real estate.

## Other Uses

Filter Strip in its best implementation is semi-transparent, as shown in the iOS Yelp app in Figure 8.12.

![](images/6dce8b0e7758123b9fdf4a545e1b25f288a961fe20197b35b3da39ff274e8d8e.jpg)

<table><tr><td colspan="2">5. Marnee Thai</td></tr><tr><td>2225 Irving St, Outer Sunset</td><td>$$ 7</td></tr><tr><td>⭐★⭐★大667Reviews</td><td colspan="2">Thai</td></tr></table>

<table><tr><td>309 Clement St, Inner Richmond</td><td>$$ 7</td></tr><tr><td>⭐⭐⭐⭐2470Reviews</td><td>Burmese</td></tr><tr><td>Special Offer</td><td></td></tr></table>

7. Hunan Homes Restaurant  
![](images/c1d33464719ef905ac20c814ee9910f002acb590b18eb41ca3aea636e9fbef72.jpg)  
Figure 8.12: In the Yelp iOS app, the Filter Strip is semi-transparent.

In contrast, the majority of Android implementations of the Filter Strip are solid. This is a mistake. Making the Filter Strip semi-transparent enables the searcher to read the search results while also seeing the query clearly, especially while scrolling the page. If the Filter Strip is semi-transparent, the focus shifts from the process of search and refining to what is most important to the searcher: search results content. Furthermore, the screen space is used efficiently—not a pixel is wasted. This is important for immersion as discussed in more detail in Chapter 13. For now, suffice it to say that successful games such as Angry Birds use semitransparent controls frequently, and you should consider the lessons from the games to improve the effectiveness of the search experience in your own app, while balancing immersion with competing UX concern of legibility and perceptual noise.

## Pet Shop Application

Filter Strip is perfect for the Pet Shop search because of the many refinements that can be applied. The example of the complete search refinement and filter strip package (first introduced in the discussion of the Refinement Page pattern earlier in this chapter) is wireframed, as shown in Figure 8.13, including a semitransparent Filter Strip that appears after the refinements have been applied.

![](images/99476a4cfaaa9f73a04af5396dc4a065e5a47c412912b161098daab828b20030.jpg)  
Figure 8.13: Filter Strip and Refinement Lightbox play well together in the Pet Shop app.

Several unusual refinements are used, such as a dual slider with histogram to filter by price. To learn more about this Slider experimental design pattern, head over to section 10.1. Also note that the lightbox comes out of and is connected to the Filter button—this is deliberate because it projects a strong perception of the app’s Information Architecture (IA) through intuitive visual means. Maintaining this connection clearly states, “This lightbox is the contents of the Filter expanded.” Having the lightbox connected with the element from which it originated also dispenses with the need for a dual Go and Cancel button arrangement in the lightbox, as shown in Yelp. Instead, to exit the lightbox, the searcher needs to tap only the Filter button again to collapse the lightbox. This design greatly decreases any accidental fat-finger taps on the Cancel button and increases “fool-proofness” and satisfaction. Use the custom Expand and Collapse animation effect (where the lightbox literally “grows out” of the Filter button) for the open lightbox transition to further support the sense of place and provide added visual slickness.

Last, but not least, note that the Filter Strip reports that the price has been applied as “around \$100”; this is deliberate. The additional precision that is so important for computers carries little meaning for human beings, so it pays to shorten the numeric filter settings to human-scale formats such as “around \$100,” especially on mobile devices and tablets. For more on this, see Chapter 8 of my book Designing Search: UX Strategies for Ecommerce Success (Wiley, 2011, ISBN: 978-0-470-94223-9)

## Tablet Apps

Filter strip is just as important for tablets. You do not need to use as small a font as is typical for the mobile devices because tablets have more space and are meant to be read comfortably at a longer distance from the eye. Transparency of the Filter Strip element is also less of an issue; although it's still recommended, especially if the search results are more visual in nature, such as large pictures. You want as little as possible to detract from the content, and semi-transparency of the filter strip helps it “disappear,” which encourages immersive flow interaction with the content.

## Caution

Use text that is as small as possible, but don't lose legibility. To do this effectively, avoid temptation to use the Filter Strip as a clickable object or button, unless it is at the very top or very bottom of the screen. The main purpose of the Filter Strip in most cases is to provide information while remaining unobtrusive; it's not to be clicked.

## Related Patterns

7.7 Pattern: Dedicated Search

13.6 Pattern: Swiss-Army-Knife Navigation

13.5 Pattern: Watermark