C h ap t er

# Avoiding Missing and Undesirable Results

When customers attempt to operate tiny mobile screens with a fat thumb, using only one hand, or while being jostled in the metro and eating a sandwich at the same time, mistakes are bound to happen. You must realize that those mistakes are not errors. They are a natural outcome of mobile computing, which takes place in a fast-paced, multitasking world. This makes avoiding missing and undesirable results a priority. The extent to which your app assists your customers in figuring out how to resolve the missing and undesirable results condition determines in large part their sense of satisfaction with your app, their brand loyalty, and whether they will recommend your app to their friends.

Essentially, recovery boils down to three essential elements:

■ Telling the searcher that the system did not understand him

■ Focusing on providing a way out

■ Leveraging to the fullest extent the sensor and history information available in the mobile context of use

This seems like a straightforward strategy. Unfortunately, as you see in this chapter, most apps still struggle with relatively simple problems.

![](images/602130ade31a7807d3d62ed057af2c09be3f1c90bd6b6cdad0d0c7529963c6cb.jpg)

## 9. 1 Antipattern: Ignoring Visibility of System S tatus

On a small mobile device with its frequent user entry errors, it is tempting to bypass telling a customer about the problem and instead just take corrective action. This is generally better avoided by simply telling the customer “I did not understand,” and thus it makes the first antipattern.

## W hen and W here It Shows Up

This antipattern is fortunately not common. However, whenever the system takes some significant action on behalf of customers without telling them about it, this antipattern rears its ugly head.

## Example

Here is an example from Yelp, an otherwise fine app, where the system takes unusual liberties in trying to guess what people are typing in. For example, in the image shown in Figure 9.1, the person is looking for sushi restaurants in Cupertino, a city in the heart of California’s Silicon Valley. Unfortunately, the searcher mistypes the word Cupertino as Coppertine.

The results are sushi restaurants located in… West Jordan. Needless to say such results would be confusing to the extreme. The person may not even pay attention to the city marker, but instead attempt to call a restaurant to book a reservation or even try to navigate to it. Imagine the surprise! All this grief could be easily avoided if the system clearly stated that it did not understand the query rather than silently attempting to give its best guess instead.

![](images/c36fd2263188807fbde801a7d0b82b4800e914b7337531900a67777f0e394fba.jpg)

![](images/dc5135fffb61613e60d723e38198713c3d2694bb00ebe9f87a004d5b410a0382.jpg)  
Figure 9.1: The Yelp app includes an example of the Ignoring Visibility of System Status antipattern.

## W hy Avoid It

The first strategy of the zero-results recovery pattern is to tell customers that the system did not understand them. Ignoring this fundamental strategy makes the entire system less trustworthy in the eyes of customers. If people are unaware that the app did not understand them, they might think that the app is malfunctioning or, worse still, violating the basic rules of logic and reason. Not stating that a misunderstanding occurred, violates the implicit agreement of the mental models people construct to operate complex machinery, so they get stuck. In the real world that means that customers feel frustrated but try again or—a worse scenario—move to a competitor’s site or app and never come back.

## Additional Considerations

To clarify, it’s actually a great idea to try to guess what the person is trying to type in—many patterns in the chapter are devoted to doing exactly that (see the “9.4 Pattern: Did You Mean?” section). But if you are trying to guess, be sure that your customer realizes what is happening.

## Related Patterns

9.4 Pattern: Did You Mean?

![](images/36e1fed733fe15a898386192222fbee5ee061c8e2c7a5076623e9307fb9b473c.jpg)

## 9. 2 Antipattern: Lack of Interface Efficiency

Whenever a zero-results condition occurs, avoid the temptation to show an “error” state, particularly the one that requires an extra tap to get out of. Because missing or unwanted results are not an error, Lack of Interface Effieciency is an antipattern.

## W hen and W here It Shows Up

This antipattern is common in apps that do not spend time designing missing results recovery mechanisms, but instead “blame the user” by showing the “official” Android error, and thus requiring an extra tap.

## Example

Figure 9.2 shows an example from the Target app. When the keyword query is not recognized by the system, the app pops up an alert that says, Sorry, No Results Found Matching Your Request.

This alert inconveniences the customer in two important ways:

■ It requires an extra tap to acknowledge the missing results condition.

After the tap, the system navigates away from the Search Results tab and into the Shopping Basket tab.

This is both unexpected and inconvenient because the person looking for an item most likely mistyped it, so he needs to return to the Products tab again, which requires an unnecessary additional tap. Thus to recover from a common fat-finger mistype, the system requires two additional taps. This is an antipattern.

![](images/13efac82dc77695f7025ed5151b0aea8d0c2810eedc5b9e88d3f4fbffb601894.jpg)  
Figure 9.2: The Lack of Interface Efficiency antipattern is evident in the Target app.

The error dialog, plus additional tap required to get out of it, signal to the customer that he did something wrong and committed a sin…maybe even one of the unforgivable ones. If you recall that missing and unwanted results are both logical and natural outcomes of the mobile context of use on a tiny screen, it’s easy to see that the extra tap acts as a sort of punishment added to an insult. You're hitting the customer’s knuckles with a metaphorical ruler.

## Additional Considerations

Recall that the second strategy in the missing or unwanted results recovery is focusing on providing a way out. The best way to do that is through an efficient, straightforward interface that does not treat any break down in communications with hostile dialogs. The dialogs and additional clicks they contain yank the person out of the state of flow, interrupting the search process abruptly.

Flow in search is important (read more on this later in the chapter), and it needs to be maintained at all costs. Dialogs that ask for additional taps and take the customer away from the task at hand (such as the Target app navigating to the Basket and away from the Products tab) break the flow. As Alan Cooper so eloquently said in his book About Face (2007, Wiley), dialog boxes “Stop the Proceedings with Idiocy.” So although you must signal clearly to the customer that the misunderstanding has indeed occurred, you also must do it without breaking the sense of flow of the finding process. That’s what keeps your customers going and keeps them engaged in the finding task.

## Related Patterns

None

![](images/2dd5efe1375c4c6dab90502a8d3b0dd8396c38c53e7c6b1d147b57a7647b24bb.jpg)

## 9. 3 Antipattern: Useless Controls

All too frequently the controls provided by the interface on a zero-results screen are the same as those provided on a screen with actual results. This is an antipattern.

## W hen and W here It Shows Up

The Useless Controls antipattern occurs on zero-results pages treated the same as those pages that have results.

## Example

Unfortunately, this antipattern is quite common. Figure 9.3 is an example from TripAdvisor, where the customer accidentally fat-fingered the word "saucelito” (while trying to enter "sausalito”), and the system helpfully said, Sorry, but Nothing Matches Your Search. So far so good—the app avoids Antipattern 9.1 Ignoring Visibility of System Status. Unfortunately, the screen also displays the Filter Search Results link.

![](images/01fce134c44bb055c83640a588f30fbea55d7de760f4755ade4f1d8fb4a49556.jpg)

![](images/3873d43544090830a08463e7dd151356492c2a34392a4eff0bf896f30c060c40.jpg)  
Figure 9.3: The TripAdvisor app demonstrates the Useless Controls antipattern.

Tapping the Filter Search Results link causes a filter dialog to display so that the customer can filter results by Destinations, Hotels, and so on. When the customer taps the Hotels button, he goes back to the same zero-results screen, but now the Hotels filter is applied. Of course, filtering zero results by hotels again produces zero results.

## W hy Avoid It

As you know from elementary algebra, zero divided by a number always yields zero. Zero results condition renders the filtering control useless. Actually, it's worse than useless because this filtering interaction drags the customer deeper into the quagmire of the zero-results search by having him go through the motions of actually filtering a nonexisting collection of zero items. Do not underestimate the customer confusion and damage to the experience that useless controls inflict. Useless controls are a clear antipattern. The zero-results situation requires that all the available controls focus on recovery and navigating somewhere useful.

## Additional Considerations

None

## Related Patterns

9.4 Pattern: Did You Mean?

## 9. 4 Pattern: Did You M ean?

The simplest and arguably most powerful missing results recovery pattern is Did You Mean?—named after the Google search feature of the same name.

## H ow It W orks

When the customer types a keyword query that's not recognized by the system, the system offers a set of controlled vocabulary substitutions that are based on creative spelling of the original keyword query. The resulting list of keyword suggestions may or may not include the Did You Mean? title that Google uses, and it's not limited to a single suggestion. Given the number and creative quality of the misspellings possible on the mobile platform, the number of suggestions could also be correspondingly large.

## Example

One creative implementation of the Did You Mean? pattern is done by the Booking.com app (see Figure 9.4).

![](images/0b17489c21c47efa69e5e767e87dada93cf2d804a45178f7e24fb5f3f14218c5.jpg)  
Figure 9.4: The Booking.com app includes a creative implementation of the Did You Mean? pattern.

Booking.com flips the entire search equation on its head by assuming from the beginning that you somehow mistyped the query. The result is a robust Did You Mean? interface that automatically suggests one or more controlled vocabulary substitutions for every keyword entry. Booking.com recognizes that the world is getting smaller, so you might just like to travel internationally, so it offers creative spelling suggestions from all over the world, as a kind of query prescreening. This is a nice example of the company branding expressed as a user interface feature.

One thing to note is that Booking.com adds the extra details (for example, Los Angeles, city in United States) which makes the extra click of the mandatory Did You Mean? query prescreening process worthwhile even for entries that are exactly correct in the initial spelling. After the city and country are positively identified, the added country meta data makes the final results for Hotels and Attractions reliable.

## W hen and W here to Use It

At least one Did You Mean? suggestion is mandatory for any search suspected of keyword misspelling. Sometimes misspellings may be difficult to identify—a controlled vocabulary tuned to mobile-specific misspellings (such as one discussed in the “7.3 Pattern: Tap-Ahead” section) could be very helpful. Lastly, if you can’t find any helpful Did You Mean? suggestions, you probably shouldn’t suggest anything, just indicate zero results and use one of the other patterns in this chapter instead.

## W hy Use It

Misspellings caused by fat-fingering of the mobile device's tiny touch keyboard are common. Yet keyword queries are by far the most popular search methodology. This makes it imperative to implement the keyword query correction as a first line of defense against missing or unwanted results.

## Other Uses

Did You Mean? is basically an Auto-Suggest pattern (refer to Chapter 7, “Search”) that was implemented after the search has taken place. Given the tight bandwidth of most mobile devices, Did You Mean? is currently the more common pattern of the two. However, don't forget that almost anything that can be done after the search query is run can potentially also be implemented using Ajax on the front end before the query is run. Sometimes, Auto-Suggest is clearly superior to Did You Mean?, particularly in multi-field parametric queries, such as booking a flight. The name of the airport can be quite challenging to remember or guess, so a lookup with the Auto-Suggest based on the city name or airport code is essential. Ideally, at some point in the near future, as networks become faster, the entire process of two Auto-Suggest lookups (from and to airports) and the Did You Mean? feature in the results set (to suggest alternative departure times) becomes virtually seamless. In other words, the distinction we now draw between Auto-Suggest and Did You Mean? patterns will become even more blurred and eventually disappears entirely as you get instant feedback and suggestions for your query even as you view the results, much like Google Search now does on the web. Patterns such as Tap-Ahead (refer to Chapter 7) help show the way.

A related approach is to cache controlled vocabulary substitutions on the mobile device itself, much like the high-end paid language translation apps do currently. Mobile devices are actually full-featured computers. For specialized terms (like Pets or Airports) you can cache on the order of 100,000 or more Did You Mean? substitution terms locally and use the mobile device itself to run sophisticated regular-expression matching algorithms against this collection locally, instead of sending anything to the server. If you decide on using this approach, consider storing queries that cause the Did You Mean? function to activate in a log stored locally on the device, and periodically upload that log to the server, where it can be analyzed and used to improve suggestions in the future.

## Pet Shop Application

Given the complex spelling of various pet breeds, it’s easy to see how a Did You Mean? pattern can be useful in a Pet Shop app. However, it is tricky to see how to integrate Did You Mean? with various other refinement strategies. See "9.6 Pattern: Local Results" later in this chapter to see all the various missing and unwanted result strategies working together.

## Tablet Apps

This pattern works the same way for tablets as it does for the smaller mobile phones.

## Caution

Did You Mean? is also sometimes called controlled vocabulary substitution. This means exactly what it says: The keywords suggested to the customer as part of the Did You Mean? recovery pattern come from some table in the database that contains the “good” or “allowed” keywords that form the controlled vocabulary. The quality of the substitution depends greatly on the quality of the controlled vocabulary, which, as discussed in Tap-Ahead (refer to Chapter 7) could be quite different on the mobile from its web counterpart. Not only can the queries be different, but the misspellings can also be different driven in part by the mobile keyboards. To make things even more interesting, there is anecdotal evidence that these misspellings depend in large part on ergonomics of the keyboard on a particular device. Therefore, iPhones, Android mobile phones with touch keyboards, Android devices with physical keyboards, Android tablets, and Blackberry phones may all give rise to different misspellings depending on the keyboard ergonomics of a particular device.

One idea might be to keep a specific database of the mobile-only misspellings and Did You Mean? suggestions. This enables you to better tailor the experience for mobile customers, without polluting the Did You Mean? database on the desktop web, which might include different misspellings. Whether you choose the approach with two split databases over the combined database depends wholly on your specific use case.

## Related Patterns

7.2 Pattern: Auto-Complete and Auto-Suggest

7.3 Pattern: Tap-Ahead

## 9. 5 Pattern: Partial M atch

The second most important recovery strategy for missing results is Partial Match, which lets you recover from the missing results condition by omitting some search terms from the query.

## H ow It W orks

For queries with multiple keywords that return zero results, it is not always clear which keyword created the missing results condition. In this case, Partial Match Pattern can be used to recover. Partial Match reruns the query that consists of matching fewer keywords than were entered by the customer—that is, the system removes one or more of the keywords.

## Example

One of the best examples in the industry comes from Amazon.com’s mobile website (see Figure 9.5), which mimics the desktop in important respects.

![](images/cfc201435b31c46ca60cd6af97ed4bce682b6a25d898689a62bcb156b1b8b9a9.jpg)

![](images/eb781dab4b23dda60f261c963f7a42fe37297dd6de7ff62c41e6130553ef501f.jpg)  
Figure 9.5: Amazon.com's mobile website includes an excellent example of the Partial Match pattern.

The query Nike Ruskie Red produces zero results. The website clearly massages the condition. As part of the recovery strategy, Amazon.com helpfully does the search without the problem word “Ruskie” so that a results “appetizer” can be presented to the customer, which says in effect, “If you remove the problem keyword, you see more items like these.” Strikeout coupled with the contrasting font color used for the problem keyword “Ruskie” creates a highly effective visual treatment that communicates how the Partial Match works.

Unfortunately the same cannot be said for the Amazon.com app. Although the mobile website works extremely well, the app does not provide any Partial Match recovery; it merely states that zero results have been found, as shown in Figure 9.6.

This forms an effective demonstration of the value of the Partial Match as a missing results recovery strategy.

![](images/6dc8835fc080fcc472b50f393fad33e04567e784c1d040406dcbf20e29190b99.jpg)  
Your search "nike ruskie red shoes" did not match any products.

Figure 9.6: The Partial Match pattern is missing in the Amazon.com app.

## hen and W here to Use It

Partial Match is somewhat less important for mobile than it is for the desktop web. This is, of course, due to the difficulty of typing on the mobile, which results in slightly fewer average words per query. However, for some applications, e-commerce, and business apps, for example, the number of keywords entered on the mobile is quite close to that on the desktop. For those applications that employ long queries with multiple keywords, Partial Match forms the second most important recovery strategy after the Did You Mean? pattern discussed in the previous section.

## W hy Use It

Human beings are subject to a strong psychological effect called anchoring. Anchoring is a cognitive bias that refers to relying too heavily on one piece of information—in this instance, one query keyword. My book Designing Search: UX Strategies for Ecommerce Success (Wiley, 2011, ISBN: 978-0-470-94223-9) describes a situation in which the test participant was so convinced that the book she was looking for was titled Harry Potter and The Sleepy Hollows that she kept adding more and more information to the query (including misspelled author’s name as “JK Rolins”) over and over again, while the query kept returning zero results. The person in question anchored on the erroneous word “Sleepy” and no amount of failure would get her unstuck. She was so anchored on that term that at the end of the test, she erroneously concluded, “The store must not carry any Harry Potter books.”

Her search behavior while on the system could be characterized as churning, what Peter Morville and Jeffrey Callender describe in their book Search Patterns (O’Reilly, 2011, ISBN: 978-0-596-80227-1) as running similar queries over and over while getting the same missing or unwanted results. The Partial Match pattern stops churning and anchoring behavioral antipatterns by showing clearly which keyword of the bunch caused the problem. The best implementations of Partial Match also return a sample “appetizer” (or the full search result) of the query without the extra keyword present to demonstrate the outcome of the query. Such implementations usually break the anchoring most effectively.

## Other Uses

Sometimes it’s hard to tell which keyword is an issue. In this case, Partial Match may provide multiple keyword combinations, with one or two keywords removed,

each showing a small sample of items that would result from dropping the keyword(s). Usually these groups of results are sorted by the number of results retrieved from the query, highest first.

On a mobile device, Partial Match can also be effectively combined with the Local Results pattern, as shown in the "Pet Shop Application" section of "9.6 Pattern: Local Results."

## Pet Shop Application

The complete implementation with the Local Results pattern is described in the "Pet Shop Application" section of "9.6 Pattern: Local Results."

## Tablet Apps

Partial Match applies to tablets the same way as it does to mobile apps. Tablets have larger keyboards, thus the number of keywords per query is anecdotally similar to the number of keywords in desktop web applications. Therefore, the importance of Partial Match as a recovery mechanism is much higher. Simply showing a No Results Found message, as the Amazon.com app does (refer to Figure 9.6) is not resourceful. Besides, the No Results Found words would look so lonely on a giant tablet screen! Be sure to augment your tablet zero-results screen with one or more recovery strategies in this chapter.

## Caution

None

## Related Patterns

9.6 Pattern: Local Results

7.3 Pattern: Tap-Ahead

## 9. 6 Pattern: Local Results

When implementing missing results recovery on the mobile, take advantage of the local inventory of the results that can be retrieved using the on-board GPS.

## H ow It W orks

When a zero-results condition occurs, the system delivers some local results based on a partial match query or by providing a set of featured local results.

## Example

The Target app store finder provides a simple example of the Local Results pattern. When the app first loads, it takes into account the customer’s location via the on-board GPS. This location is used to display a map of nearby store locations even before the customer enters anything. This is a logical implementation because it is a safe assumption that 90 percent or more of use cases would find a local store. However, the app also provides a keyword search (presumably based on city name).

If the keyword entry cannot be successfully resolved into a city name, the app pops up an alert that requires tapping OK to dismiss it, which is an antipattern (refer to "9.2 Antipattern: Lack of Interface Efficiency"). However, after the dialog is dismissed, the apparent missing results “recovery” works well; the customer sees the local store results loaded in the previous step (see Figure 9.7).

![](images/2f71977525a306636464d5ff6f6dd3358cbdadf7098100fdcbe00cdd3043e1cf.jpg)  
Figure 9.7: The Basic Local Results pattern assists with missing results recovery in the Target app.

## hen and W here to Use It

Mobile queries tend to be local. That’s not the only use case, of course, but it’s a common one. In the absence of clues from the customer as to the records the system needs to look for, or when executing a Partial Match pattern (refer to "9.5 Pattern: Partial Match") local results make an excellent bet.

## W hy Use It

When implementing zero-results screens, it is not enough to just avoid the antipatterns. The best mobile experiences are “designed from zero”—that is, the prevention and recovery from zero results goes to the core of the way the search is implemented. Zero-results recovery based on the person’s location determined via the built-in GPS is a true mobile feature not available on the desktop. Thus it constitutes a pure case of mobile-first advantage.

## Other Uses

Local Results constitutes the “basic view” of the Parallel Architecture pattern (read more in Chapter 8, “Sorting and Filtering”) and is the default search for most travel, reviews, and local shopping apps. Many of the excellent travel apps like Booking.com (see Figure 9.8) offer local results as a default browse tab—this one is labeled Around Me.

![](images/1c3da464b470cd6b956928b37ad35e18d182832cea9f7df2d1d4518187daa742.jpg)  
Figure 9.8: The Local Results pattern is used as the default Around Me tab in the Booking.com app.

## Pet Shop Application

This is the moment you’ve been waiting for: Figure 9.9 shows all the missing and unwanted results recovery patterns (Did You Mean?, Partial Match, and Local Results) in one example running a query for “Russian Mastiff.”

First on the page is the clear indicator that zero results have been found. Next are several Did You Mean? suggestions, derived from the popular keywords available on the site. Finally, because one of the keywords is correct and recognizable (“Mastiff”), the system performs a partial match, removing the problem keyword (“Russian”) and redoing the search with the additional local component. This is a safe, useful, and resourceful assumption; most people like to buy their pets locally.

![](images/0e5d1bb14b9f9ed4f8bd48859113badcaa0e43cd970553575aa2ad1b7aa6c637.jpg)  
Figure 9.9: The Did You Mean?, Partial Match, and Local Results patterns work together in the Pet Shop app.

Sure enough, there are seven local “Mastiff” results to choose from, and a small sample displays on the screen so the customer has a good idea what these dogs actually look like. The customer can scan the results using the carousel or tap the 7 Matches Near You For link to redo the search with the keyword “Mastiff” and the location set to within a reasonable radius around the current GPS coordinates of the mobile device. With all three strategies working together, an excellent missing results recovery screen was created to rival that of the mighty Amazon.com mobile site! Recall how important this screen is to the success of people using your app, and spend a little extra time and care to make it work well for your customers.

Last but not least, I used a little Pet Shop humor (“Bow-wow!”) to indicate zero results. This is highly recommended for most apps (other than Financials—refer to Chapter 12) as long as it is not the same funny line repeated over and over—that gets obnoxious in a hurry. (Recall the timeless scene from the first Jurassic Park in which the security system keeps saying “Uh uh uh! You didn’t say the magic word!” over and over) Instead, have a few different well-chosen “wisecracks” picked at random to facilitate the missing results recovery.

Wisecracks are something at which Apple’s Siri excels. Unfortunately, humor is where Android apps often come up short. Most Android apps still treat missing results as errors. Recall earlier in this chapter that mangled input is a natural and expected outcome of using a mobile device. Humor can be a wonderful tool to keep the search conversation going, despite momentary hiccups in human-mobile communication. And that’s the important thing!

## Tablet Apps

Although G3 and G4 tablets can both get a precise location, many tablets are purchased to run on Wi-Fi only and have no wireless connectivity. This makes obtaining a precise location of the device a problem. Tablets, especially large ones, are also less likely to be used in a local context (for example, navigating to a local Target store). Keep that in mind and rely on other recovery mechanisms such as Did You Mean? and Partial Match for tablets making local results available only if they can be obtained and make sense in the context of your app.

## Caution

See the preceding “Tablet Apps” section for this pattern.

## Related Patterns

8.4 Pattern: Parallel Architecture

## C h ap t e r 10

## Data Entry

Data entry on mobile devices is particularly tricky because of our fat fingers and the devices’ smaller screens. There are literally hundreds of data entry patterns currently in use, and you could write an entire book specifically on this subject. Actually, my friend and mentor Luke Wroblewski did exactly that by writing an excellent book called Web Form Design: Filling In the Blanks (2008, Rosenfeld Media). In this chapter, rather than covering every conceivable input strategy currently in use, we concentrate on the trickiest aspects of Android forms, which people most often get wrong.

## 10. 1 Pattern: Slider

Web page developers for years tried to popularize sliders and make them part of the standard HTML development toolkit. Many rejoiced that sliders came standard with the Android data entry widgets because, frankly, sliders are cool. Unfortunately, along with the sliders came a whole scope of issues that can sometimes be hard to pinpoint.

## H ow It W orks

Sliders come in two types: single and double. In addition to that, each type of slider can enable a continuous adjustment or have a set of predefined positions that customers can select from.

## Example

To see how these two types of sliders work, it is instructive to compare two different apps: Trulia and Zillow. Trulia (see Figure 10.1) solves the price data entry problem using a dual slider.

![](images/0e03dbba072c973d467d42569367906a4ee43e932af1840af07638418d48e2bd.jpg)

On the other hand, Zillow offers the same price entry but has two single sliders (see Figure 10.2).

![](images/31644719dfa2d87e09082e72648da1ac09b6e2e820528ed1921c36eb9094cb9a.jpg)  
Figure 10.2: The Zillow app uses two single sliders.

The Trulia slider does not display the minimum and maximum range of values before the sliders are moved. Strictly speaking, neither does Zillow—instead it displays text \$0 and No Maximum, which carries no information useful for the customer.

## W hen and W here to Use It

Single sliders are intuitive for entering individual values. Dual sliders are great for ranges of values such as search filters and form values that include ranges.

another physical control that can serve a similar function. In contrast to sliders, knobs do not translate as well to the touch screen, are hard to “turn,” and usually take up more screen real estate than sliders. Dual sliders in particular are useful for bounding the interval within the specific range.

## Other Uses

Single sliders with discrete values are interchangeable with Stepper controls, which are covered in the next section of this chapter. Sliders with Histogram and Slider based on Inventory Counts are two great experimental patterns that are variations of the standard slider that are unfortunately not common. These are described in the “Pet Shop Application” section.

## Pet Shop Application

You can read about a Pet Shop dual slider example, which uses a Slider with Histogram design pattern, in Chapter 8, “Sorting and Filtering,” in the section 8.3 “Pattern: Filter Strip.” Sticking with the same example (that is, using sliders for entering price ranges on a search filter screen), can you use a dual slider to enter a price range without running into the issues listed in this pattern’s “Caution” section? One way you can accomplish this is to use sliders with discrete values arranged according to inventory counts. Here’s the explanation.

A typical price slider is arranged in a linear pattern, which means that an equal distance movement of the slider axis represents an equal absolute change in value. For example, in a five-position slider, the price can go from \$0 to \$100 in \$20 increments, as shown in Figure 10.3 (numbers in gray are optional).

Select Price Range  
![](images/22b7544e596687777903d4bf868317c8e476428be7513e74e9d40adc27b97cc0.jpg)  
Figure 10.3: Each mark on the axis represents an equal absolute change in value on a linear price Slider.

literally—For a Few Dollars More (with apologies to Clint Eastwood and Western film lovers everywhere). This is where a Slider with Histogram (as shown in Figure 10.4) is helpful. The idea behind this experimental pattern is simple: The 50 to 100 pixels above the fixed position slider is the histogram representing the inventory in a particular section of the linear price range. Large numbers of dogs show a large bar, and smaller numbers show a proportionally smaller bar—that’s it.

![](images/54db2cea919c5661a73c7f379bb41ad99de7aad65390f56cf3c79a47d7df61b9.jpg)  
Select Price Range

![](images/1f8882eb7e3b3d85eb960526e86670cd16174bce1ed8e5e52aa348fee934ab51.jpg)  
Figure 10.4: A linear price Slider with Histogram pattern provides more information.

When using a Slider with Histogram pattern, you can still dial the part of the range with low inventory; it is just difficult to make that mistake accidentally because the inventory counts are clearly shown in the histogram. You can use the Slider with Histogram pattern where a standard discrete position Slider pattern would be used, taking up only a little more vertical space in exchange for a satisfying customer experience.

Another way to implement a Slider pattern without resorting to histograms, is to arrange the slider intervals based on the inventory counts. To do this, divide your entire inventory—say, 100 puppies—into five intervals, and you get 20 puppies per interval. Now scan the price range to figure out the price (rounded to the nearest dollar) that corresponds to the approximate inventory count of 20. Say the first 19 puppies cost between \$0 and \$60, (recall we assume no inventory in the \$40 to \$60 range). The second 21 puppies fall in the \$61 to \$65 range, and so on. Figure 10.5 is an example of what such a slider might look like (compare it with Figure 10.3).

![](images/c20554ec75991a14f144a616a0faa1d8435d2a9439386d06b7d83c46c9a45bd9.jpg)

Which implementation should you choose? It depends on the task. Most people don’t mind paying a few dollars outside the budget, but they absolutely hate getting zero results. If inventory is less than 20 items in a specific interval, that is not a satisfying result for most tasks, so you must use one of the other approaches to create a better experience. Both the Slider with Histogram and Slider Based on Inventory Counts patterns are far superior to the traditional Slider pattern. Breaking the interval by price is the flexible approach because it shows the distribution clearly, while never causing a zero-results condition. If the customer’s price range is larger than that of a single 20-puppy interval, he can simply select a larger interval using the dual Slider. (Looking for the code for these experimental sliders? Visit the companion site for this book, http://androiddesignbook.com, for downloadable sample apps and source code.)

## Tablet Apps

Sliders perform well in tablet apps. Make sure you heed the warnings in the “Caution” section; in particular, opt for the slider with discrete values instead of a continuous slider to ensure accuracy—it’s harder to adjust a continuous slider accurately on a larger device. Take care of the device ergonomics, and avoid placing sliders in the middle of the screen. Instead, place the sliders near the top of the screen next to the right or left margin, optimized for one-handed operation with the thumb while the fingers hold on to the back of the tablet.

Depending on the design and purpose of your app, experiment by having two sets of sliders on the left and right sides of the screen to be adjusted by left and right hands, respectively. This would be especially interesting for apps such as music synthesizers. Finally, experiment with placing sliders vertically along the edge of the tablet (top to bottom) rather than horizontally from left to right, which is the easiest position to adjust precisely.

## Caution

Keep the following considerations in mind when using the Slider pattern:

![](images/53c12c8cab87e0c609d6e9fece5340c2966c4d7ad8edc6b5fec1f8cc4ec092d6.jpg)  
Figure 10.6: The continuous price slider fails to dial a reasonable hotel price in Los Angeles on the Kayak app.

■ Show the range: Speaking of range, it’s a great idea to show the actual range of prices available in the entire collection, as the Kayak app does in Figure 10.6 (\$16 to \$750) as opposed to using arbitrary numbers such as \$0 and Max (refer to Figures 10.1 and 10.2). Neither Zillow nor Trulia show the true max and min associated with local home inventory. Imagine how useful these sliders would be if they actually said from the beginning that the range was from \$476,000 to \$3,234,700. Showing the range also helps avoid “dead zones,” such as looking for a home in San Francisco priced less than \$476,000, which yields zero results. Be aware of how filtering affects the inventory; it is best to rely on the range of the overall collection without the filters applied.

■ Don’t cover the numbers: While the customer adjusts the slider, the numbers should be shown above the pegs, where the fingers do not cover them. Placing the numbers below or to the side of the slider is not as ideal. The Kayak slider (refer to Figure 10.6) is good in this regard: The range is covered while the customer adjusts the slider, but the actual filter value is not, which is about the best you can do on a mobile device.

physical world and on touch devices. That’s why you almost never see a slider for volume adjustment on a stereo. Ironically, the larger the device, the harder it seems to adjust the slider precisely. This is the consequence of Fitts’ Law: The time required for the action is dependent on the distance and size of the target. In other words, it’s difficult to adjust a tiny peg of the slider 1/32 of an inch in the middle of a large tablet.

Regardless of the screen size, it is hard to adjust continuous sliders precisely while being bumped around in the metro or a taxi. (You have permission to refer to this thereafter as Nudelman’s Law if you want.)

Continuous dual sliders also make it easy to over-constrain the range. To use the Pet Shop example, creating a continuous slider that enables the customer to dial a price of \$45.50 to \$46.10 yields a zero-results condition and does not serve the customer well. On the other hand, sliders with discrete positions (stops) are much easier to adjust. There is also less possibility of dialing a range that is too small.

Don’t forget to consider the Slider with Histogram or Slider Based on Inventory Counts patterns. As described in the “Pet Shop Application” section, these experimental Slider pattern modifications offer a more resourceful user interface (the interface that helps customers act effectively and feel more capable) to avoid most of the pitfalls typically associated with Sliders.

## Related Patterns

10.2 Pattern: Stepper

8.3 Pattern: Filter Strip

## 10. 2 Pattern: Stepper

When the task calls for dialing a small whole number from 0 to 5, use a Stepper control.

## Example

An excellent use of the Stepper is to dial the number of rooms and number of occupants on the search page from the Kayak app, as shown in Figure 10.7. Note the good use of reasonable defaults: Most people using the app are business travelers who travel alone and need only a single room so the Stepper controls are set to 1 in each case.

![](images/82dc13ac8fdb69f3a06dd7de51ab0046e3669a28ee4eeac657874356b1f93659.jpg)  
Figure 10.7: The Kayak app makes excellent use of the Stepper pattern.

## W hen and W here to Use It

Whenever the customer needs to quickly enter a number between 0 and 5 where there is limited screen real estate, the Stepper pattern is the logical choice. A typical use is to adjust item counts during a purchase. Normally, the stepper value is submitted via a separate Submit button.

directly on screen, without the need to pop up the keyboard or use additional layers, keyboards, or lightboxes. The Stepper pattern is self-explanatory and easy to use.

## Other Uses

One interesting variation of the Stepper pattern is to use it as a row-level repeating UI control as a method to add items directly to the cart. This is how the Peapod app uses a customized Stepper control (see Figure 10.8). The first action is a simple Buy button. After the customer taps the Buy button, the item is added to the cart, and the button turns into a stepper.

![](images/3478ea137bea5fdbcd328c32864301782e20cae4b26e40188e0a399a1af46a46.jpg)  
Figure 10.8: The Peapod app uses Stepper as a row-level auto-submit control.

Whenever the customer taps a + or – button, the stepper control submits the new item count in the shopping basket to the server. This obviously slows things down a bit. However, most items come in only ones, twos, and threes, enabling this method to work well for shopping orders such as groceries, where total number of products purchased in a single shopping trip can be quite large, but individual item counts per product tend to be low.

One variation of the Stepper pattern as implemented by Peapod is the custom editable central text field. When the customer taps the central text field, the lightbox control launches so that the customer can edit the field directly (see Figure 10.9). So when the customer wants to buy those 99 Bottles of Beer for his Wall, he can do it easily by entering 99 using the lightbox keyboard.

![](images/530dcc28fad984fcd2caea7f615d061d4be9aa796d4c596eb2596eea251fabb2.jpg)  
Figure 10.9: When the customer taps the center of the custom Stepper pattern implementation in the Peapod app, the numeric keyboard lightbox opens.

Without this customization (using the standard stepper control) the customer would have to tap the + button and submit the new count of beers to the server 98 times—as tedious as the famous song. (If you don’t know the complete lyrics, check out http://99-bottles-of-beer.net/, which offers 1,500 different code variations in different programming languages with which to render the song.) Unfortunately, this unique customization is not discoverable—a better version of this is shown as part of our trusty Pet Shop app.

Another nice-to-have customization that allows steppers to enter larger numbers is press-and-hold: This action can be used to increment the count and accelerate the rate of increase with a longer button press. This is a very old pattern for devices using touch affordances. Of course this modification does not work for row-level Steppers that submit the value to the server with every tap.

## Pet Shop Application

As mentioned, although Peapod’s custom implementation of the Stepper pattern is highly effective, the discoverability of the editable text field in the center is quite low because the custom Peapod stepper looks similar to the standard Android stepper, which unfortunately does not have this direct data entry functionality.

amount. The resulting control looks customized but still carries all the correct stepper affordances; in other words, it’s clear that the customer can tap – and + to increase and decrease the count in the middle.

![](images/ea38cb0b3823cdf1273bf07757938d2567a0cebd1ecc422989d6dda2cda0d7f0.jpg)  
Figure 10.10: This wireframe shows the use of the custom Stepper pattern implementation as a row-level, auto-submit control in the Pet Shop app.

At the same time, this custom stepper also makes it more obvious that the customer can tap the middle text field directly to launch a “dial a number” lightbox. I also simplified the direct data entry lightbox from the one used by Peapod. Compare Figure 10.11 with Figure 10.9. Note the number in the textbox starts out highlighted for direct editing.

![](images/459b055041fa85f5136ebc2416dac161e9187562b9053df3e29a8cd118c7c9ef.jpg)  
Figure 10.11: This is a simplified dial-a-number lightbox design.

The row-level arrow is omitted on the right in Figure 10.10, relying instead on people tapping the picture or item title to see the details. This is an example of the Tap Anywhere Android design principle discussed in Chapter 2, “What Makes Android Different.”

## Tablet Apps

Stepper works the same way for tablet implementations as it does for mobile phones. Remember that tablets are likely to display more rows than smaller mobile devices, so if you have a repeating in-row stepper control, you may want to make sure there is enough room to tap the –/+ buttons and also that the stepper control is positioned along the left or right margin of the device so that the customer can tap the control with a thumb while the rest of the fingers still hold on to the device.

## Caution

Do not attempt to use the standard Stepper pattern implementation for routinely entering numbers greater than 5. If you need to enter larger numbers, use the custom version described in the “Pet Shop Application” section. However, be aware that even the custom control does not accept numbers larger than 99 unless you make more modifications. Stepper is not for entering large ad-hoc numbers. For large numbers, instead use the textbox with the Input Mask pattern discussed in the “10.8 Pattern: Text Box with Input Mask” section later in this chapter.

You can use both a single slider and stepper to enter numbers 0 through 5. Which one you use depends on the exact nature of the app. Stepper is more flexible and can be used to enter numbers greater than 5 on occasion, whereas slider implies a bound (fixed) range of values.

Finally, ensure that steppers have good default values. The ideal mobile control is the one that has the value your customers already want, so they do not need to adjust it.

## Related Patterns

10.1 Pattern: Slider

## 10. 3 Pattern: Scrolling Calendar

When it’s necessary to enter a date, most apps opt for a calendar that paginates by 1 or 2 months. This is traditional, but it’s also tedious. A much slicker alternative is the Cadillac of Calendar Patterns: the Scrolling Calendar.

## H ow It W orks

The calendar control is the continuous scrolling ribbon of dates ordered in fixed columns by day of the week, with months separated by a thicker line.

<table><tr><td rowspan=1 colspan=14>M F              才11:15Choose Check In                         Choose Check InNOVEMBER 2012                       DECEMBER 2012Sun  Mon  Tue  Wed  Thu   Fri   Sat   Sun   Mon   Tue  Wed   Thu   Fri   Sat</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>09</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>15</td></tr><tr><td rowspan=2 colspan=1>18</td><td rowspan=2 colspan=1>19</td><td rowspan=2 colspan=1>20</td><td rowspan=2 colspan=1>21</td><td rowspan=2 colspan=1>22</td><td rowspan=2 colspan=1>23</td><td rowspan=2 colspan=1>24</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>22</td></tr><tr><td rowspan=2 colspan=1>25</td><td rowspan=2 colspan=1>26</td><td rowspan=2 colspan=1>27</td><td rowspan=2 colspan=1>28</td><td rowspan=2 colspan=1>29</td><td rowspan=2 colspan=1>30</td><td rowspan=2 colspan=1>01DEC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1>29▲</td></tr><tr><td rowspan=2 colspan=1>02</td><td rowspan=2 colspan=1>03</td><td rowspan=2 colspan=1>04</td><td rowspan=2 colspan=1>05</td><td rowspan=2 colspan=1>06</td><td rowspan=2 colspan=1>07</td><td rowspan=2 colspan=1>08</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>01JAN</td><td rowspan=1 colspan=1>02</td><td rowspan=1 colspan=1>03</td><td rowspan=1 colspan=1>04</td><td rowspan=1 colspan=1>ⅢI05</td></tr><tr><td rowspan=2 colspan=1>09</td><td rowspan=2 colspan=1>10</td><td rowspan=2 colspan=1>11</td><td rowspan=2 colspan=1>12</td><td rowspan=2 colspan=1>13</td><td rowspan=2 colspan=1>14</td><td rowspan=2 colspan=1>15</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>06</td><td rowspan=1 colspan=1>07</td><td rowspan=1 colspan=1>08</td><td rowspan=1 colspan=1>09</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>12</td></tr><tr><td rowspan=2 colspan=1>16</td><td rowspan=2 colspan=1>17</td><td rowspan=2 colspan=1>18</td><td rowspan=2 colspan=1>19</td><td rowspan=2 colspan=1>20</td><td rowspan=2 colspan=1>21</td><td rowspan=2 colspan=1>22</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>19</td></tr><tr><td rowspan=2 colspan=1>23</td><td rowspan=2 colspan=1>24</td><td rowspan=2 colspan=1>25</td><td rowspan=2 colspan=1>26</td><td rowspan=2 colspan=1>27</td><td rowspan=2 colspan=1>28</td><td rowspan=2 colspan=1>29</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>26</td></tr><tr><td rowspan=2 colspan=1>30</td><td rowspan=2 colspan=1>31</td><td rowspan=2 colspan=1>01JAN</td><td rowspan=2 colspan=1>02</td><td rowspan=2 colspan=1>03</td><td rowspan=2 colspan=1>04</td><td rowspan=2 colspan=1>05</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>01FEB</td><td rowspan=1 colspan=1>02</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>03</td><td rowspan=1 colspan=1>04</td><td rowspan=1 colspan=1>05</td><td rowspan=1 colspan=1>06</td><td rowspan=1 colspan=1>07</td><td rowspan=1 colspan=1>08</td><td rowspan=1 colspan=1>00</td></tr><tr><td rowspan=1 colspan=7>                           # 8 m</td><td rowspan=1 colspan=7>U                           日日</td></tr></table>

Figure 10.12: The Kayak app includes an excellent implementation of a scrolling calendar.

This calendar design takes advantage of the fact that although the number of days in a month changes from month to month (and sometimes year to year, as in February for leap years), the days of the week repeat continuously and unerringly— Monday through Sunday. Thus, the scrolling calendar consists of a ribbon that scrolls through seven columns representing repeating days of the week: Monday, Tuesday, Wednesday, and so on. Thus, even though the line separating the individual months is jagged, the dates flow through the days of the week in a continuous stream of numbers.

Note the additional “name of the month” feature is at the top of the page. As the month advances during scrolling, the name of the next month is partially displayed in the register. The customer can also paginate through the months in a more traditional manner by using the side arrows.

## W hy Use It

Pagination of the calendar is a paradigm as old as the Gregorian calendar, which is old—430 years old as of the date of publication of this book. Essentially this includes the mental models of the physical wall calendar you flip pages on, which is not exactly the most modern implementation. As Alan Cooper eloquently points out in About Face, it’s time for a modern and user-friendly design. I consider the Kayak mobile app implementation more usable even than its desktop website—an impressive accomplishment!

## Other Uses

I used this Calendar pattern in a client app for a major U.S. retailer with one variation: The month on top of the scrolling calendar reflected the month selected, not the month displayed (as in the Kayak example). The default view is today’s date. After the customer selects another date, the register displays the month of the new selection, regardless of the scroll state of the wheel.

To know which month currently displays in the scroll wheel, customers must rely on the three-letter abbreviation printed below the number 1 in the cell representing the first of the month. If you try this method, keep in mind that the range of available dates for that client goes to only approximately 2 months, which makes scrolling convenient, but also limited. If you have a longer time period to cover, you may want to stick with the Kayak implementation that dynamically shows the month displayed in the wheel as the calendar scrolls below.

Be aware that the Scrolling Calendar pattern is not just for dates; any continuous strip of timeline, including months, years, and most commonly hours of the day can be shown in a scrolling format that emphasizes the range between the two points.

## Pet Shop Application

A wireframe for the Pet Shop app would not differ from the Kayak app, so it isn’t reproduced here. However, feel free to indulge in a little practice by drawing this pattern yourself.

the device. The top-right corner would likely be ideal for most people. Remember to plan for vertical and horizontal orientations of the tablet and accommodate both orientations in your popover placement and sizing.

Kayak does not currently do this well in the landscape (horizontal) orientation (see Figure 10.13). The lightbox that contains the calendar is located smack in the middle of the screen, making it necessary to let go of the edge of the tablet to scroll and select, even on the 7-inch device. This interaction is even more awkward for larger tablets.

![](images/108818adcfe7fa041b12cfd10af91f96c35a2df127f4d3dee9fc50124237faa5.jpg)

## Caution

Remember to indicate the dates that are not available by graying them out. If it’s important to your application, indicate today’s date by putting the gray text “Today” in the cell under the number. Finally, don’t forget that this pattern enables you to indicate gracefully a range of dates that spans a month or more, such as the length of stay, by highlighting the cells in the range for one-half a second just before the contents of the screen are sent to the server.

If your customer attempts to enter a date that is not allowed, make sure to message him before resetting the date to the first allowable date, and keep the customer on the scrolling calendar screen. Kayak currently does not do this, which makes the workflow confusing. Here is how the functionality currently works. Say the departure date is set to November 14 and the return date to November 18. The customer means to change the departure date to November 13, but mistakenly changes the return date instead. Obviously, this is Kayak, not Isaac Asimov’s time-travel novel, so it’s impossible to return before you arrive. However, instead of alerting the customer properly, Kayak silently resets the return date to be 1 day after the departure date—to November 15 in this case. (See Figure 10.14.)

![](images/602da2e58b9bf38c96aac554b74a100ac3adf04c0b573add3c0cb016ed724235.jpg)

![](images/67bb90202258c66d0973993b6a77982cc8cd24b772fa4affc0b51563ae9f3100.jpg)

10.4 Pattern: Date and Time Wheel

## 10. 4 Pattern: Date and Time W heel

For complete flexibility in entering dates and times from an arbitrary length of time in the past or future, use the Date and Time Wheel pattern.

## H ow It W orks

When the customer needs to select a date, she taps the date or time field, which displays a lightbox of all the date components in a vertical picker format.

## Example

Google Calendar provides a reference implementation example for this pattern (see Figure 10.15). Both date and time are shown on one line—a convenient and flexible, yet space-saving, arrangement. The presence of the Date and Time Wheel control is indicated with the Android’s signature folded-corner triangle. Tapping the Date control brings up the Date Picker lightbox.

![](images/03f5229bade7d08cde5d94e2680db5372501c32d4c46907988f56b24af17a13b.jpg)

![](images/b3279de8aa2a0b22375e32509bdee372be4b5747481702c822a390fcfc568713.jpg)  
Figure 10.16: Here’s the Time picker lightbox of the Date and Time Wheel in the Google Calendar app.

Android 2.3 and earlier wheel controls had to be adjusted by tapping the +/– buttons on the control or by tapping the textbox in the middle and editing the value directly via the keyboard (see Figure 10.17). There was no ability to use multitouch to “spin the wheel.” If the person wanted to advance the values faster, she would hold down the appropriate + or – button.

![](images/b23249a79c26d476cd6f9a7ec42d6a53e56d0920ca10fd62566fa453e6b39389.jpg)

![](images/2067bc73c4784b237b886ed065d5d91184efaa0446af7cdbe9d579dea099d9c2.jpg)  
Figure 10.18: The Alarm Clock Xtreme app uses the Android Picker widget.

Starting with the Ice Cream Sandwich version (4.0) of the Android OS, the standard +/– wheel widget also includes the iOS Picker functionality for direct manipulation of the wheel’s selection by swiping, as shown in Figure 10.19. For lack of a better name for this mode of adjustment, I call this swiping multitouch mode the Wheelie mode.

![](images/a0a844a7b2973311ddd11b4e8ae52b5e6e4c0a2e7f4f71aae3996f505818c13f.jpg)

## hen and W here to Use It

Any time you need to enter an arbitrary date or time, this is the standard pattern to use. However, be aware that unlike the Scrolling Calendar pattern, this pattern does not show ranges. This pattern is also subpar for removing disallowed states (as described in this pattern’s “Caution” section), so if the range of dates functionality is important to your app, you may want to look at the alternative patterns such as Scrolling Calendar or Dual Combo Wheels (see the “Pet Shop Application” section) for both the dates and time ranges entry.

Other uses of the wheel include any continuous ranges of strings 1 to approximately 20 characters. The only requirement to using the wheel control is that the values be obviously consecutive (numbers in order, seconds, months, and days of the week) and that the value can be displayed on a single line.

## W hy Use It

The Date and Time Wheel pattern is the standard pattern recommended by the Android OS, which enables complete flexibility.

## Other Uses

Did you notice that the date and time entry required separate sets of multiple taps? If not, revisit Figures 10.15 and 10.16. With complete freedom comes complete responsibility. Entering dates and times like this is like playing Robinson Crusoe on a deserted island and having to make your shoes from scratch out of palm leaves and vegetable fibers. Yes, you don’t have to go to the office every day where someone tells you what to do. But no, you can’t get any Italian leather loafers in your size, and you have to chop all your own firewood. For most people, too much control is just as bad as too little. Having to use multiple taps to enter date ranges is excessively tedious, and it’s why many people absolutely hate to enter dates on mobile devices.

So what’s a designer to do? As it turns out, people rarely enter events years in advance. Most people do wait for the $2 ^ { \mathsf { n d } }$ of January to start planning New Years resolutions. (Shocking!) If you take that into account and let go of some of the flexibility of the separate Date and Time Wheel controls, a simple modification of the pattern takes care of the excessive taps issue. Figure 10.20 shows the iPhone screenshot of the date entry screen from the Pocket Informant app. The Combination Wheel control employed by the app consists of three parts: day of the week/ date, hour, and minute.

![](images/a8af64348e49539b0b14d136829475fad88965230772d23c5a944bf7ff64471f.jpg)  
Figure 10.20: This Combination Wheel Date and Time Picker control is from the Pocket Informant iPhone app.

Having all the controls in the single wheel takes care of having multiple taps to open first the date wheel and then the time wheel, while still allowing plenty of flexibility. What you give up is the ability to easily pick anything, say, 10 years in advance. Most important, you can add a critical piece of data that was not available in the original design: the day of the week. Think of this Date and Time Wheel pattern implementation as a Robinson Crusoe who works remotely from his island on his MacBook Pro, ordering his Nike flip-flops from Zappos—all while sipping a frosty margarita.

## Pet Shop Application

Imagine using a modified Date and Time Picker to book an appointment with a vet. Figure 10.21 shows a simple wireframe of what this implementation might look like on Android.

![](images/203d886e1f9d3059c282e8974e5de187e38f851733cf106e13f3e4a74766222a.jpg)  
Figure 10.21: This wireframe shows a Combination Wheel Date and Time Picker for the Pet Shop app.

Another great solution would be an experimental pattern of dual composite sets of wheels for setting both from and to dates on the same screen, as shown in Figure 10.22.

This experimental pattern makes it much easier to enter dual dates on small tablets, allowing key information, such as the day of the week, to be clearly visible for both dates. This pattern would be particularly good for setting travel dates and meeting appointments on larger mobile devices and would cut down on taps while greatly improving clarity. You can even add the calculator of the event duration— handy indeed.

![](images/2a50d177d5ee5ad21845a42f9b7cbfb4b907158811093884bbc71c5668eafee9.jpg)

![](images/560a8896778a1cc2c8736f45ffcacaab25ca8ff8eee623d9c3b9339fbebd47ef.jpg)  
Figure 10.22: This experimental pattern of Dual Combo Wheels would enable the user to set to and from times and dates in one shot.

## Tablet Apps

Although the Date and Time Wheel is a standard Android widget, it’s actually hard to use on a tablet. Because the control is so tiny, it’s difficult to swipe it using a normal-sized male thumb. This makes it hard to use the Wheelie mode of the Android control on a large device. (This is the same Fitts’ Law at work on tablets once again as discussed previously in this chapter in the “10.1 Pattern: Slider” section.) On the other hand, the individual up/down arrows seem to work well on tablets, so the preferred implementation keeps the older Android 2.3 interaction mode, which disables the multitouch swipe control. To advance this wheel, the customer taps the +/– buttons (in this case the up/down arrows) and holds down the buttons to make the wheel advance faster (see Figure 10.23).

![](images/390b4710ce85ec7e8b80f277acf41d2c9de684fd6d526ca970c1f3fad00808b0.jpg)

Note the scrolling calendar added to the right of the control. It’s a nice touch; however, it does make it hard to adjust the control with the right hand, forcing left-handed use of the wheels or letting go of the device with the right hand. It might be better to swap the placement of the calendar and wheels to improve ergonomics.

Just as with the older Android 2.3 wheel implementations, you can adjust this control directly by tapping on the date and typing in the value using the keyboard (see Figure 10.24) .

![](images/4c90d83a9c9633e1746aad19324567ec679c4b4151be824768b476a2671e358e.jpg)  
Figure 10.24: You can type the date directly into the Calendar Android date wheel on a Galaxy Tab 2 7-inch tablet.

This interaction is currently reserved only for tablets and pre-4.0 Android devices. Directly typing the value into the wheel is not available on the Android 4.0 mobile phone implementations of this pattern.

## Caution

The general difficulty of swiping in the Wheelie mode was previously mentioned. This is inherent in the control, so there is little you can do about this, but you should generally be aware of the issue and look for the fix in later versions; increasing the height of the control, for example, would make it easier to use the swipe gesture.

situations in which the larger number, such as 59, is selected and the customer must spin all the way back to 00 to reset the control. This also applies to on/ off switches such as AM/PM. The current implementation of the Calendar does not enable this (compare Figures 10.16 and 10.21).

■ Message entry errors and help recover: If the business logic does not enable the customer to enter certain dates, the wheel control should message out the bad selection right on the date wheel lightbox itself without going to the main screen. Current behavior of the Google Calendar app in Android 4.0 is the antipattern; it accepts the bad To entry of September 19, which occurs before the From date of September 26, and then simply resets the To date back to the 26<sup>th</sup> without bothering to let the customer know that anything went wrong.

![](images/0fe80db09ce9d5ab15e02801ae161a2be2c262f7212372ef6ae2b8ceea6081c7.jpg)

![](images/73e67233d8756fc75fb1da1c3630949278b9d5e705d8675b1ccb7065dc26314a.jpg)  
Figure 10.25: This is an antipattern; the Google Calendar app simply swallows date entry errors.

Remember: Dates are tricky. In the United States, many people make a mistake of entering the wrong AM/PM marker for appointments that span the noon hour, so they accidentally end up with meetings lasting more than 24 hours. If the person makes a mistake, the last thing you want to do is “swallow the error.” As discussed in Chapter 9, “Avoiding Missing and Undesirable Results,” you must let your customers know the correct system state and help them recover as soon as possible. That does not mean popping up errors all over the place. If you use a single composite wheel to enter both date and time (refer to Figures 10.20 and 10.21), you can slowly rotate the date dial to the next date using a smooth transition, while they are adjusting the time or AM/PM wheel. Most people notice the movement of the date wheel transition easily, and that is usually enough to cause them to self-correct. Another pattern that makes immediate error reporting and correction in-situ easy is the dual composite wheel experimental pattern shown in Figure 10.22, which would enable even more sophisticated business logic, such as excluding holidays or weekends, and, of course, not allowing the To date to be prior to the From date.

## Related Patterns

10.2 Pattern: Stepper

10.5 Pattern: Drop Down

## 10. 5 Pattern: Drop Down

Whenever you need an arbitrary value in the list of allowable values, Drop Down (also called Spinner or Select) is the natural pattern to call upon.

## H ow It W orks

When the customer taps the control’s value, the popover box is launched with all the available Select values. Selecting one of the values from the list replaces the default value with the new value. Tapping outside the popover cancels the Select action.

## Example

A typical example comes from the Trulia app (see Figure 10.26), where the customer uses the Drop Down to select a number of bedrooms and bathrooms in the search.

![](images/2a8243881bb2438f7ae4417efe1e46a1e45892b64781a71060be0120fa0d6ed1.jpg)

Despite there being a reference Android 4.0 implementation, a different version of the control is offered by the competing app Zillow. Zillow’s version of the Drop Down pattern (see Figure 10.27) looks a little different, but it performs the same function.

![](images/24a8c67a5ccd5e3c47d2414aebf9741e0aee11b7d2de9c2409d60d4d2da3cb85.jpg)  
Figure 10.27: The Zillow app implements the Drop Down pattern a little differently.

## hen and W here to Use It

Use the Drop Down control any time you to need to allow the customer to pick from a list of 2 to 20 item sections that do not necessarily follow a specific sequence. The Drop Down control is also useful when the item text needs to wrap. You can use the Drop Down pattern in place of the radio buttons sequence.

## W hy Use It

The Drop Down pattern binds the value of a variable to a specific set of predefined values. It’s intuitive to use and easy to operate.

the auto-suggest list of contacts that can be selected to fill the Contacts field. This is an effective variation of the Drop Down pattern. Not only does the customer provide the criteria for selection (the initial few characters), but the Drop Down control is also augmented with a small thumbnail of the person’s face to ensure slickness and positive identification. Where the picture is not available, the app substitutes the generic “portrait” thumbnail (see Figure 10.28).

![](images/8d703c2ceed428267eee714b61365ab96031994ea88241520b84497b9c7d2cf3.jpg)  
Figure 10.28: The Calendar app includes an implementation of the Drop Down Combination control with pictorial and text values.

See more about this pattern in the “10.9 Pattern: Textbox with Atomic Entities” section.

and so on, and each type of pet is shown in the drop-down with a handy thumbnail. The thumbnails aren’t drawn—this is just a wireframe. When you can practice drawing this pattern, and if you are so inclined, you can make your own pretty icons for each type of pet.

![](images/51d22ed2552104bbe92f4c9ec8e7a9d1d38c4833c4fbfedc90ab6501acecabf1.jpg)  
Figure 10.29: Check out the Pet Shop app implementation of the Select control with pictorial and text values.

## Tablet Apps

On a tablet, this control works just the same way it does on the mobile device. As always, if you expect your customers to manipulate the control often, be sure to place the popover next to the right or left margin for easy reach with the thumb.

items might be the Dedicated Selection Page Pattern, or even a Combination Select control with a search function (refer to Figure 10.28).

Be aware that although the Drop Down pattern is quite versatile, it has limited styling options. For example, if you want to show a picture, text, and dollar value on a sky blue background, you must customize. When you do decide to customize, be aware of the competing pattern of a Dedicated Page Select (discussed in Chapter 12, “Mobile Banking”) that discusses the differences between Drop Down and Dedicated Page patterns in more detail.

Some older or custom Drop Down controls enable the label to be on top of the control. Depending on the desired functionality, this might be a good idea—even though it is not strictly necessary. However, it is a good idea to implement the header that tells the customer what he is selecting in standard long-list implementations that are popped up in a lightbox window that darkens the background or obscures the page, to the point that makes it hard to determine the context of the selection. Use your own judgment here. Read more about this topic in Chapter 11, “Forms.”

Be sure to create a good default value for the control—do not force the customer to make extra selections when not necessary. Be aware that any selection from the Drop Down involves at least two taps: one to open the control lightbox and one to select the item.

If the number of options is small (less than or equal to 5) and the value is numeric (such as number of passengers and rooms) consider using the Stepper control instead, as described in section 10.2. Stepper is much more elegant and is contextual in its selection. In other words, Stepper makes values inside it transparent to the customer and enables the customer to change the selection in the page itself, without popping a lightbox that can disorient him.

## Related Patterns

12.2 Pattern: Dedicated Selection Page

10.4 Pattern: Date and Time Wheel

## H ow It W orks

The drop-down version: When the customer taps the control, a popover box opens with a set of check boxes that enable the selection of multiple values from the list shown in the popover. After the selection is completed, the customer taps the Done button to apply the selections or the Cancel button to discard the changes and close the popover.

The gallery version: The customer can select one or more items from the gallery or list by tapping and holding down one of the items. This switches the gallery into a Multiple Select mode, which enables the customer to pick one or more items and perform actions on the selected items.

## Example

One example of the Drop-Down Multiple Select control is to apply groups to a contact in the Contacts app (see Figure 10.30). The Multiple Select control enables the customer to pick one or more groups from the list and add the new contact to them.

![](images/ff86cc1536a504fb2efbc4acdd740fb44821e66753530e933e8466fb62c600a7.jpg)

## hen and W here to Use It

Any time your customers might want to select more than one item from a long list, the Multiple Select pattern is the way to go.

## W hy Use It

Sometimes, selecting one item at a time is simply too slow. The Multiple Select pattern provides flexibility. For bulk operations (such as selecting multiple spam messages in Gmail app) the Multiple Select pattern provides a graceful and usable alternative to performing the delete action one item at a time.

## Other Uses

Another variation of this pattern is to select multiple items from the Gallery, such as the Android Photo Gallery app implementation. For the Gallery, multiple actions may include sharing, deleting, or even rotating the selected photos (as shown in Figure 10.31).

![](images/d6bae413bea04c93a3bf70b0e65cb0f29bb58a7470fe6915b88ce50e73890d16.jpg)  
Figure 10.31: The Gallery variation of the Multiple Select pattern is in use in the Photo Gallery app.

To enter the multiple select mode, the customer must tap and hold one of the items in the gallery. After that a single tap is sufficient to add to the multiple selection.

For the Drop Down version of a Multiple Select control, one interesting feature is the ability to add a new element. Figure 10.32 shows the Contacts app again, but this time the customer taps Create New Group, so she gets a separate pop-up for entering a new group name.

![](images/d18d6eeefa42229bfe651096aa0ecca35147c4f22deb6eb3c6951a377d959f44.jpg)  
Figure 10.32: Another variation of the Drop Down Multiple Select pattern is being able to add a new value in the Contact app.

![](images/d40cae1ccc347d7346f056d84bcd4b0c2c75ea163a328264bd36d2e1831e9a96.jpg)

This Pet Shop functionality works similar to the way Gmail app Multiple Select works. In contrast to the Photo Gallery app, the check boxes are shown all the time, and as soon as an item is selected, the contextual menu on the bottom floats up, revealing the actions that can be taken on the selected items (in this case, Wish List, Bid, and Contact Seller). Tapping the check box on the top of the page exits the Multiple Select mode, releasing all of the selections and removing the bottom action bar.

## Tablet Apps

Customers using tablets presumably have a bit more time for leisurely contemplation and to perform maintenance tasks; therefore, they might draw upon a multiple select even sooner than their mobile counterparts. It’s not uncommon to provide Multiple Select functionality for tablets, and it works great to accommodate those urges to tidy up a gallery or add some group information.

## Caution

This option tends to be less discoverable—that is, it is not obvious how to enter a Multiple Select mode in some apps, such as the Photo Gallery. If this function is essential for your app, be sure to provide a quick tutorial overlay. See Chapter 5, “Welcome Experience,” for ideas.

## Related Patterns

10.5 Pattern: Drop Down

## 10. 7 Pattern: Free-Form Text Input and Extract

Whenever customers need to enter random text, give them this basic text input pattern.

## Example

One example of this pattern is the Contacts app (see Figure 10.34) . The Contacts app appears with the soft keyboard already in place, ready to enter values.

![](images/c9d8eab34242bf03ddfdd9c6640282e12ca22148565de8f21ba675fa17b49f0d.jpg)  
Figure 10.34: This typical textbox implementation is in the Contacts app.

Turning the mobile device horizontally while maintaining focus on the textbox launches an important variation of this pattern: the Extract Text Input (see Figure 10.35).

![](images/d0b939f6a4f1e60bb6c7c472bd76a7ca72e211a9e75f4a858807d57c1f929988.jpg)

## hen and W here to Use It

Use this pattern any time you need a free-form text input, such as the name, description, status update, and the like. The Extract version of the pattern is particularly useful for longer messages, such as an e-mail message body, because it make the input field larger; so the customer can see two to three lines of text at the same time, and has a larger soft keyboard, which for many people allows for more precise typing.

## W hy Use It

This pattern is the standard control to enter text via a keyboard on Android.

## Other Uses

Starting with the Nexus phone in the Android 4.0 OS, any form field that accepts text also accepts voice input. Tapping the microphone button on the keyboard (or on some models, swiping across the keyboard horizontally) brings up the voice input mode. The keyboard swiping method is less discoverable, so fewer people know about it.

This voice input function is handy, especially for status updates or longer fields like an e-mail body. Unfortunately, it’s still somewhat incomplete because the customer needs to tap the Next button to send the update or move onto the next field. (See Chapter 7 for discussion of the differences between standard voice input and the true convenience of digital assistants such as Siri.)

## Pet Shop Application

This implementation is straightforward, so I did not create a wireframe for it;   
however, you can practice on your own.

This is a good place to mention the one recommended departure from the stickynote wireframe style of the previous chapters: not to draw various keyboards in the sticky-note Pet Shop app wireframes. Drawing keyboards is tedious and time consuming, and it yields no tangible benefit in user testing. Instead, do what works: Simply print and cut out various keyboards and glue them onto smaller sticky notes using a glue stick or tape. Once created, you can place these stickynote keyboards on top of the wireframed screen to simulate the keyboard coming up from the bottom. Then these paper keyboards can be moved down as needed to give the participants the feel of a complete sequence of filling out fields on the page. The sticky-note keyboards can be reused on other screens and projects, as needed.

## Tablet Apps

On tablet devices, there is far more real estate for the form, so the form never enters the “extract” mode. Typically, the form just scrolls up to where the target field comes up just above the keyboard, regardless of the orientation (see Figure 10.36).

![](images/e9832c0944e2671d909783c8a861430e02a9c938f852019f34a3aa3289092c49.jpg)  
Figure 10.36: This is how a textbox implementation looks in the Calendar app on the 7-inch Galaxy Tab 2 running Android 4.0.

Unfortunately, flipping the tablet from vertical to horizontal orientation and back again sometimes closes the keyboard. This is definitely a bug; the keyboard should stay open until dismissed or until the customer taps Done or goes to the next field. See more about keyboards in the following “Caution” section.

## Caution

![](images/423b1cd7f66df6e0eb4f53f6fed263b5d66d548031c7b21b9d2a6f958a09b1ac.jpg)  
Figure 10.37: The Next and Done buttons appear on textboxes in the Calendar app.

Unfortunately, things break down when your form includes a multiline text field, such as a long description, which omits the Next or Done button in favor of the Enter key. If you happen to be in the multiline field, the keyboard remains on the screen until the form is submitted. So in effect, for the entire remainder of the form, the customer is left scrolling the form up and down with her finger to move into the next field in a small fraction of what remains of the screen real estate above the keyboard, while the system focus remains on the multiline description field. This is an antipattern, as shown in Figure 10.38.

![](images/9b39f6d569fe7892afc91c2e5195962850db06db8c65e4f0bd66ff3cf278e816.jpg)

You might say that the standard behavior is to use the hardware Back button to exit the keyboard while in the multiline description field. That is true; this function is available. However, the discoverability to use the hardware Back button to get rid of the keyboard is low. This function is counterintuitive because the multiline entry field looks exactly the same as the single-line field, minus that critical Next/Done button. To add to the confusion, this same multiline text field has an explicit Done button when viewed in a horizontal format (see Figure 10.39). The Landscape Done button moves to the next field, whereas the Portrait Done button actually submits the form!

![](images/1e10c0d6c6a2f5ecce87ce030c4dcac529ef35ddf0aa04444cbbe8dd6220d584.jpg)

![](images/4765722c77326655efe2d1d910cb43654e8cd620983c3a8c38526b046c3b31f8.jpg)  
Figure 10.39: In Google Calendar, Done buttons in landscape and portrait perform diametrically opposite functions.

The absence of the way to exit the long field explicitly (that is, the Next/Done button) means that you must be careful with the keyboard behavior, especially in portrait mode on smaller mobile devices where the keyboard obscures most of the rest of the screen. For this reason, the keyboard should collapse as soon as the customer taps any other form field, regardless of type.

One last note of caution: When your form or lightbox contains a single text field, strongly consider launching the form with the keyboard already in place to save your customers an extra tap. For example, in the Contacts app, when creating the new group, the lightbox with the single entry field is shown without the keyboard. The customer must tap the field to launch the keyboard. Another weird thing happens after the customer taps the OK button on the lightbox: The focus shifts upward to the Address field (see Figure 10.40).

![](images/8c2a62d992148040344c35ec8b222c5a6180c348001473b5af6ba80d3d990ffd.jpg)

![](images/ac9521aceed769cc8b4053de36d638249941d3e6617867335f7e34dbcfa170fd.jpg)  
Figure 10.40: In the Contacts app, the single text entry lightbox is launched without the keyboard and focus shifts randomly.

A better interaction would be to launch the lightbox with the keyboard already in place (refer to the second screen from the left in Figure 10.40) and shift the focus to the groups Multiple Select field after the new group name has been selected.

## Related Patterns

10.8 Pattern: Textbox with Input Mask

10.9 Pattern: Textbox with Atomic Entities

12.5 Pattern: Wizard Flow with Form

## H ow It W orks

When the field accepts only specific data, such as e-mail, phone number, Social Security number, or ZIP code, the system can provide the right kind of keyboard to facilitate data entry. Also, depending on the location of the field label, it can optionally show the input mask inside the field.

## Example

When adding a new contact, the Name field provides a “Name” in-field label shown in a lighter gray font inside the entry field (see Figure 10.41). The in-field label remains in place until the customer starts typing.

![](images/8e45504b1f4bbdc5529dab51e3a2760b15b1144bd5556c2c18fb2e86aeb451df.jpg)

Despite being open to all sorts of characters, the Name field has some restrictions, such as field length, which is always limited to some practical number (for example, 100 or 255 characters) and disallows the “enter” character (also called “new line” or “carriage return”). This makes the Name field different, from, say the Notes field. The Notes field enables up to 1 Mb of text data and accepts a press of the Enter key to add a new line to the text. In this way, it is useful to think of anything written inside a field that also happens to shape the customer’s expectations of the format and allowable values as a kind of input mask.

So what is the Input Mask pattern good for? One useful feature is to facilitate the correct data entry by launching the right kind of keyboard. For example, notice in Figure 10.42 how the soft keyboard changes accordingly when the Name, Address, Phone Number, and E-mail fields are entered; that is the implicit input mask at work.

![](images/1c8c230fd6b854461eb15f53eefe00351c086805c97f93096f7a56a4c2d2dd50.jpg)  
Figure 10.42: Implicit input masks launch various types of mobile soft keyboards.

The Name and Address both provide voice input capabilities, whereas Email provides a handy @ sign (which can be hard to find on the standard keyboard). Most of the new Android 4.0-style minimalist native form fields are going to be limited to this type of implicit input mask—that is, an input mask that is logically implied by the label.

![](images/efd524646c7355062ac7009cca268a99140ed93e9836462510221ed8013a8d07.jpg)

![](images/10ce0babcee1141ace1575a92203110d10750f9b023b41b54e7891da290550c0.jpg)  
Figure 10.43: The Kayak app uses explicit input masks.

This explicit input mask reduces input errors because it shows the field format ahead of time and also keeps the label present during data entry. Of course, nothing comes free, particularly on mobile devices (just ask AT&T about their texting plans), and the resulting form sacrifices some of the length of the label. And some minimalists would argue this format also adds extra “noise.” I disagree. Although the Kayak form does looks a bit busier than the native Android form designs, it is a small price to pay for improved clarity.

## W hen and W here to Use It

issue. Input masks reduce data entry errors and therefore should be used whenever possible to produce a better mobile experience.

## Other Uses

As discussed earlier, for fields that allow a wide range of possible values, an implicit simple mask such as Phone Number is sufficient. However, if your app requires enforcing a specific format for entry, you can use the effective experimental variation, as shown in a high-resolution wireframe in Figure 10.44.

![](images/3458b4d2beb4cac12b5e9ed3234ce3b8d704a54123e1fc4719e3ccfad4e7bdf3.jpg)  
Figure 10.44: This experimental pattern puts a static input mask inside the Android 4.0-Style phone number field.

the strange separator characters popping up seemingly at random all over the place (as discussed later in the “Caution” section). Unfortunately, to this day, this remains largely an experimental pattern and has not gained wider adoption.

## Pet Shop Application

For the Pet Shop app, you can use a different tactic for the Phone Number field in the Pet Registration Form. Because the app accepts both U.S. and international phone number formats, you can choose to make the input mask simply say 111-111-1111 (see Figure 10.45). This should accommodate both the formats with and without the country code and phone number extensions.

On the other hand, the second field is the Social Security number of the pet’s owner: a well-formed nine-digit number. For this field use Luke Wroblewski’s idea of a static input mask inside the field.

![](images/a7a284990e7a287e5e5406a305062f855d754f4fa40f98979bb388fc138edb5b.jpg)

![](images/d8d82d14aff4cd5b334a09cd448f742cdcf20a6af8d57539517b2423008a90e8.jpg)

## Tablet Apps

The input mask applies even more strongly to tablets because the screen has plenty of real estate to provide a separate label and a static in-label input mask. Unfortunately, most native reference form implementations (such as Calendar) fail to take advantage of the cornucopia of screen space and consequently do not provide additional input instructions, even when abundant space is available. Instead, the Contacts app in the Galaxy Tab 2 7-inch Tablet with Android 4.0 reveals the format gradually using a loose dynamic input mask. As shown in Figure 10.46, the system initially removes a perfectly good “–” separator character that the person initially types as part of 415–222 and replaces it with the ( ) format as the customer continues to type (415) 222–33, surprising him with the additional characters popping up in the field. On the other hand, as shown on the right side of the figure, the Galaxy Tab 2 tablet also seems to enable all sorts of nonsensical user formatting that can be used to, seemingly at random, override the native dynamic input mask.

![](images/afece5be0b89aabb7dde2357cd0f923d2cf970cbf5637b0288049215d4549342.jpg)

![](images/1acb945da1a2707a69fc7c0fc1516c16d3901ae2cdb651a3397f06d5c3ae8e00.jpg)

![](images/90d06358116f357655abbcdac64fe71780d4bb9ae71d3399db7b72a20a0b2833.jpg)

<table><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2ABC</td><td rowspan=1 colspan=1>3DEF</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>4GHI</td><td rowspan=1 colspan=1>5JKL</td><td rowspan=1 colspan=1>6MNO</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>7PQRS</td><td rowspan=1 colspan=1>8TUV</td><td rowspan=1 colspan=1>9WXYZ</td><td rowspan=1 colspan=1>?#+</td></tr><tr><td rowspan=1 colspan=1>大</td><td rowspan=1 colspan=1>0+</td><td rowspan=1 colspan=1>#</td><td rowspan=1 colspan=1>Next</td></tr></table>

Sometimes the system overrides the format the person puts in, and sometimes it doesn’t, creating a confusing experience. This implementation is not recommended. It is always best to reveal the formatting information upfront, if possible.

## Caution

Although this pattern is thankfully becoming rare, some apps strictly auto-format the text input as it is typed; that means the system immediately removes any characters it deems inappropriate, even when they are part of the mask. As Luke Wroblewski so eloquently showed in his article “Input Masks Design,” (December 13, 2008, http://www.lukew.com/ff/entry.asp?756), this kind of strict dynamic input mask is actually an antipattern because it creates a confusing interaction when handling in-field characters that are part of the mask.

For example, as shown in Figure 10.47, while entering \$60,000.00 into a strict dynamic input mask field, the system swallows the \$ character after it’s typed and further formats the commas in a way that’s entirely different from the decimal point, which all adds up to a confusing interaction.

![](images/4ac38f65bd08e4b39cc01fe99a58faafe59bb8780aa6bcdb3a00f2cf32410d63.jpg)

US Dollar:

\$

Number: \$#,###.00

US Dollar:

Number: \$#,###.00

US Dollar:

\$6

Number: \$#,###.00

US Dollar:

\$600

Number: \$#,###.00

Another thing to keep in mind is to not go overboard on the keyboard specificity. For example, the specialized time entry keyboard from the Pocket Informant Android App, as shown in Figure 10.48, actually tries to limit the hour entry to the numbers 1 and 0 for the first digit then to the numbers 0 through 9 for the second digit, which depends on the first digit typed. This is presumably meant to help people avoid typing nonsense entries such as 91 hours. Unfortunately, the result is rather confusing because keys on the keyboard light up and go dim for no apparent reason while the customer enters even a simple time such as 8:00 AM, which distracts the customer greatly from the primary task.

![](images/962c370a19e9201a43caba2e482016ccfec8273fc9faa9c4ef8ba261904981e1.jpg)  
Figure 10.48: Disabling Keyboard Keys is an antipattern.

Avoid disabling the specific keyboard keys because it is overkill and a (fortunately rather rare) antipattern.

Finally, at all costs avoid breaking up fields into their component parts. For example, don’t abstract the U.S. three-digit area code into a separate field in front of the phone number. This is an antipattern and creates a confusing interaction. Fortunately, this has become rarer in recent years.

## Related Patterns

## 10. 9 Pattern: Textbox with Atomic Entities

Some textboxes are used as a kind of search box to locate and enter specific discrete, nondivisible system objects, also called atomic entities.

## H ow It W orks

The customer starts by typing a few characters that identify the atomic (also called discrete) entity, and the system performs a dynamic look up, returning the auto-suggestions, usually as a drop-down below the textbox. As soon as the customer taps one of the auto-suggestions or the typed characters resolve themselves into a single entity, that entity is added to the textbox. If multiple atomic entities are allowed in the same search box, the focus remains in the textbox, enabling the next text entry, which is input the same way.

## Example

An excellent example of this pattern is the Invite field in the native Android Calendar app (see Figure 10.49). The customer can enter one or more people who are pulled in dynamically from the Contacts database.

If one of the contacts is not recognized (for example, Joe Plumber), the system forms a red box around the unrecognized contact. The customer can then edit the name or delete the entire entity with a single tap of the Delete button on the keyboard.

## W hen and W here to Use It

Use this pattern any time you enter one or more discrete entities from a long collection (50 or more objects). Typical uses include Contacts, Social Media Connections, Countries, and Airports.

## W hy Use It

As the information in the world becomes richer and more ubiquitous, more collections begin to qualify as “large,” so they become awkward to enter using a drop-down/select control. Textbox with Atomic Entities pattern provides a robust solution for this problem. You can use it to search the server or operate on local databases that are cached on the mobile device entirely on the client side.

![](images/a0747fc3ced3a9bf9e8a78c14cd02240338825f82d9848690b9b0ee0ce587c65.jpg)

no one has yet implemented this Country Selector in the mobile app. The text field auto-suggest search Christian created is robust and intuitive, surfacing more common items (United States) higher in the list than the less common ones (United Emirates). Add to this a few techniques discussed in Chapter 9, “Avoiding Missing and Undesirable Results,” such as a quick controlled vocabulary substitution (Holland to Netherlands), and you have a chance to create an industry-defining mobile experience. Other capabilities of this pattern include the ability to enter new entities on-the-fly, as dictated by the purpose of the app. For example, the Calendar app enables the entry of a well-formed e-mail address directly, instead of picking an existing entity from the Contacts database.

## Pet Shop Application

According to the current version of Wikipedia, there are from 400 to 600 different dog breeds. When registering a dog in the Pet Shop app database, you can use the list to form a controlled vocabulary from which the owner can select a breed of a dog. The wireframe set is fairly straightforward (see Figure 10.50).

![](images/68f44b60c2c7c49084e93d73658a953ca679d99e4ced34e02a08170e6078114d.jpg)

the full name of the breed) or simply select the breed he wants from the list of auto-suggestions. The pet breeds do not change often, so these can be cached in a small database on the mobile device, providing a smooth and responsive experience.

## Tablet Apps

This pattern should work the same for the tablets as it does for the mobile apps but fit more auto-suggestions. Remember that depending on the orientation, the auto-suggestion layer can display below the field (vertical tablet orientation) or to the right of the field (horizontal orientation). Don’t get caught up with following the mobile implementation.

## Caution

Remember to test boundary conditions. What happens when the invite has more people than can fit on a single line?

## Related Patterns

10.7 Pattern: Free-Form Text Input and Extract

## C h ap t e r 11

## Forms

Data entry on a small screen is fascinating, but customer inputs must be combined together in forms to ultimately enable interaction. Luke Wroblewski made an eloquent statement about filling out forms in Web Form Design: Filling in the Blanks (2008, Rosenfeld Media): “Forms suck.” That’s the reality. This chapter is mostly about how to make them suck less on Android devices—and in some cases, even make filling out Android forms downright fun.

## 11. 1 Pattern: Inline Error M essage

Whenever an error occurs when you fill out a form, the Inline Error Message pattern provides the standard way to help the customer out of it.

## H ow It W orks

When an input error occurs, the system notifies the customer which fields need to be corrected. Generally you can recognize two components of the Inline Error Message: a field-level error indicator and a general error message (usually on top of the screen).

## Example

Visual error indicators differ greatly between apps. My favorites are positive visual indicators such as icons combined with the traditional red color, such as the reference implementation from the registration flow of the Calendar app (see Figure 11.1), which adds a red round (!) icon on the right side of the textbox if the person attempts to move past the e-mail field.

![](images/4e55ef2a7f7d561e7b0975c1ee54af39ce21f81d964066460b24e9ca0ac82d90.jpg)

![](images/475c4c5307e0d4c4488b01a3f0e18c637ebd258547d3b5bb9390143f035433ff.jpg)

The Calendar app does not show a message in addition to indicating a missing value in the field. Although it’s often preferable to show the message and indicate which field has an issue, sometimes the answer is obvious, especially for shorter forms.

An alternative to this example is the eBay app’s registration form. In Figure 11.2 you can see that the form messages field-level errors by putting a red box around each field and places a composite error message on top of the form in red font.

![](images/005a9462234001cb9a3b223a7ee174b9712a3d2161c98e4e74eba741395869d6.jpg)  
Figure 11.2: The Inline Error Message pattern in the eBay app uses two ways to alert the customer of issues.

In the eBay implementation of this pattern, all the fields that have an issue receive the red border. This is the correct way to implement this pattern.

Both the Calendar and eBay forms disable the Next/Continue button, which provides a further indication that something has gone awry and the form is not yet ready for submission. Read more about this in the "11.5 Pattern: Cancel/OK" section.

## W hen and W here to Use It

Any time you need to show your customers that they made an error in the form, this is the default pattern to use.

## W hy Use It

## Other Uses

One potential modification that you can make for long forms, such as the eBay registration, is to show the error message as a toast alert (see the next section, "11.2 Pattern: Toast Alert"). The advantage of doing this is that the error message is shown to customers even though they have scrolled down past the message (which is hidden from view on top of the page). Compare the toast alert wireframe shown in Figure 11.3 to the message on top of the page shown in Figure 11.2.

![](images/e2cc86e347636ab27f47eab93cf0fe834ee0d0e541e15fe3b9a649bae21dcd2a.jpg)  
Figure 11.3: This proposed wireframe provides an alternative implementation (the Toast Alert) of the eBay app's Inline Error Message.

One disadvantage to using the Toast Alert pattern with the inline error message is that the overall error message is not “resident.” In other words, the alert disappears after a few seconds, which could be confusing to customers if the message is long and contains detailed instructions as to how to solve the issue. For example, if your password error message reads something like “Your password needs to be 8 characters long and contain 3 special characters, 3 numbers, and 2 letters, upper and lowercase, and it cannot be the same as 10 previous passwords, nor can it contain the name of a movie character like C3PO or Darth Vader or Han Solo or Leah Buns or…,” you may not want to use the Toast Alert. (And you may just want to consider making it a wee bit shorter and easier for your customers. See the “11.2 Pattern: Toast Alert” section for more discussion.)

## Pet Shop Application

Because I am a fan of short registration forms and error messages on top of the page, the example shows you how to sketch a simple inline error with the top message for registering with the Pet Shop app (see Figure 11.4).

The form takes advantage of having an e-mail address on hand on the mobile device, so it prefills the e-mail address field but still enables the customer to change it if necessary. The app uses phone device ownership as a two-factor authentication pattern (read more in Chapter 12, “Mobile Banking”) and use the Login Accelerator pattern (see the “12.1 Pattern: Login Accelerator” section in Chapter 12) to secure the account with only a four-digit combination.

![](images/292a7d5b054add234b0497698898c431bbdd0e66cdea71d1cc2bd16034a36339.jpg)  
Figure 11.4: This wireframe of the Inline Error Message pattern is for the Pet Shop app user registration form.

In the left wireframe, the customer just started to fill out the form. On the right side you see the form with the inline error, as the customer missed entering the name of his pet, his e-mail address, and the four-digit PIN, all of which are required. I used the same round red icon on the top level message to indicate the field-level error. This is intentional—both icons are similar in shape and color to draw attention to the tie-in of the message above the form to all the error fields below.

## Tablet Apps

In tablet apps, there is a bit more room, both vertically and horizontally. Because of that, the message on top of the page is easier to find (see Figure 11.5) and is most likely to be displayed above the fold, making the toast alert modification described earlier unnecessary.

![](images/9107e6c9a144d9998653cc7c34117e7a9c52b61552aaa646f5dfc400d5aec1ba.jpg)  
Figure 11.5: The Inline Error Message pattern in the eBay app registration form works even better on a 7-inch Galaxy Tab 2 with Android 4.0.

Another thing all that wonderful extra space lends itself well to is more detailed instructions located next to the field. Depending on the device orientation and form design, these can be shown on the right of the label or immediately below it. Figure 11.6 shows a wireframe of the example of how that might look in a vertical (top) and horizontal (bottom) tablet orientation. Unfortunately, today this largely remains an experimental pattern.

Like 1111 or 11111-1111

Figure 11.6: These proposed wireframes of the Inline Error Message pattern in the eBay app registration form provide extra field-level help information.

## Caution

Beware using only color gradations to indicate problem fields, as eBay has done. People that are color-blind (which is approximately 3 percent to 5 percent of the population, depending on gender, location, and other factors) may have trouble picking out the fields with a red box around them. A good test is to print the error and nonerror states in black and white to check if there is enough contrast between the states. As you can see with the eBay form example, there is enough contrast between the error and nonerror states (see Figure 11.2), though just barely. When in doubt, it is best to use a secondary positive error indicator, such as an icon in the field or next to it, as shown in Figure 11.1 and in the Pet Shop app wireframe in Figure 11.4.

## Related Patterns

11.2 Pattern: Toast Alert.

## 11. 2 Pattern: Toast Alert

Toast Alert is named thus because in the original implementation the alert layer would pop up from the bottom of the screen like a piece of bread popping out of the toaster. The actual transition of the alert popping up is much slower than the bread ejected from your toaster—the latter always seems to fly out with the force equal to that of a conductive payload coming out of the railgun, but hey, you can’t beat those sweet Android food metaphors. The current Android 4.0 implementations of the Toast Alert have a variety of entrance motion variations, including just appearing on the screen. Today, the name “Toast Alert” is used mainly as a way to distinguish general messages that do not have buttons and go away by themselves after a short time from so-called Pop-up Alerts (see the next pattern) that do have buttons and remain on the screen until customers take action to dismiss them.

## H ow It W orks

When the condition that generates the toast alert is met, the screen displays a small overlay window with the specific message, icon, or both. After a specified time period (usually a few seconds) the alert window disappears. The alert window can also be dismissed before the time period has elapsed by tapping on the alert window or anywhere else on the screen. The entrance and exit of the alert window are sometimes performed as an animated transition, which may include darkening of the background application window.

## Example

One example of this pattern is a white Toast Alert that comes up when the Trulia app loses a network signal (see the left side of Figure 11.7). Its counterpart on the Kayak app is black (which is pictured on the right side of Figure 11.7).

![](images/b1286aaf6d9576f585f11cd7914ec67c1f6caf6f3f33cbc3f1570f2fb50c597a.jpg)  
Figure 11.7: The Trulia (left) and Kayak (right) apps use the Toast Alert to indicate a weak network signal.

The more “traditional” implementation of the Toast Alert used for confirmation comes from the LinkedIn app. The Alert comes up if the customer has any messages and after accepting an invitation to connect, for example. In both cases, the alert comes up from the bottom and overlays the results. (See Figure 11.8.)

![](images/eec23ae7ba2b0cdff7db59b01cfbc8e6ca6ac4090ffb29a09c699e7908cb4a6b.jpg)  
Figure 11.8: The “Traditional” Toast Alert comes up on the bottom of the page in the LinkedIn app.

Yet another implementation of this pattern comes from the Amazon Fresh app (see Figure 11.9) when the customer adds an item to the cart. Note the Toast Alert actually comes up on top of the page, pushing down the search results, so the toast falls out of the toaster, as it were.

![](images/60fa347f535e96530a7d4b318e4bf4109193f1a40c5bbbe01932aa4b5e0bce80.jpg)  
Figure 11.9: The Amazon Fresh app's confirmation Toast Alert displays on the top of the page.

Because the alert is on the top of the page and (though you can’t tell) it’s actually a solid red high-contrast color, the fingers never cover it up, as they do on the LinkedIn app. This enables Amazon Fresh to keep the alert small, so it does not cover up any results, and the customer can keep on shopping without any interruptions. The alert is also close to the shopping cart icon, the badge on which gets incremented each time the alert pops down, reinforcing in the customer’s mind the tight relationship between the alert and the count of items in the shopping cart. There is one bad thing about this implementation: The results keep moving up and down on the screen; so if the customer is too quick with her finger, she can miss the next Add to Cart button or add the wrong item by mistake.

## W hen and W here to Use It

Any time you have a transient condition that needs to be communicated to the customer but does not require confirmation or any other action on the part of the customer, use the Toast Alert pattern. Toast Alert is particularly good as a confirmation device.

## W hy Use It

The Toast Alert pattern juxtaposes nicely against its ugly stepsister, the Pop-up Alert. Unlike the Pop-up Alert, the Toast Alert doesn't need an explicit function to be dismissed; it just goes away by itself, which is convenient on a small mobile screen.

## Other Uses

See "11.4 Pattern: Callback Validation."

## Pet Shop Application

Figure 11.10 shows the Toast Alert that comes up after the item has been added to the shopping cart using the interface shown. The Toast Alert comes down from the top of the page (refer to the Amazon Fresh example in Figure 11.9) but this time, the alert comes on top of the search results, partially covering up the top result on the page (instead of moving the results down, as Amazon Fresh does).

Thus you still get the benefits of the alert that comes close to the shopping cart icon and one that is not covered up by fingers holding the device. However, you also solve any issues that involve wrong buttons being pressed due to the search results inventory moving up and down. The only thing that could be the fly in the ointment in this case would be that the top search result is partially covered up. However, due to the nature of the Toast Alert, it is easy to dismiss it by tapping anywhere on the screen, so if the customer wants to get to that first result, all she has to do is tap anywhere onscreen (including the alert), or simply wait 1 second, and the alert disappears, so the result becomes accessible again. The message can be varied so that it does not get boring.

![](images/7b97b2aadd4f0bbe2d8c37453da1cfd3a2de64359163390a65a8154426be447c.jpg)  
Figure 11.10: The Alternative Confirmation Toast Alert drops down over the top of the search results in the Pet Shop app.

## Tablet Apps

In tablets even more than on mobile devices, you must be concerned about fingers covering up the alert. You also have another problem to deal with: A much larger screen, which means the customer’s attention can be anywhere, and she may not see the alert. That said, an alert that comes down from the top middle of the screen, regardless of the orientation, is usually a safe way to go, especially if it’s done in contrast colors and includes a quick, smooth animated transition. Figure 11.11 shows one example from the N.O.V.A. game on the tablet.

![](images/eb1a83298a03218d5fbef605b390353cf16b5193562e1adaf86f3cf171e8a783.jpg)  
Figure 11.11: Here is the Welcome Toast Alert on the top of the page in the N.O.V.A. Game app on a tablet.

## Caution

A cautionary example of using this pattern is as a warning that additional actions are needed, as exemplified by its use in the Peapod app (see Figure 11.12) to indicate that the quantity is too high and the customer needs to call customer care. This use of the Toast Alert is an antipattern because this alert text is complex, yet by its nature, the Toast Alert disappears too quickly to read and fully grok the message properly. In addition, Toast Alert is particularly poor for recommending further actions because traditionally tapping the alert or any negative space around it should simply dismiss the alert, leaving the confused shopper to wonder where exactly does she need to go from here to call customer care.

![](images/fcdb1118148329f9f3b2decd8e51c9c10ebc494b1710389c294885f13029ecfb.jpg)  
Figure 11.12: This long and complicated Peapod app  
Toast Alert that requires customer action is an antipattern.

If you need to give your customer a choice of whether to perform a certain action, a Pop-up Alert, which is discussed in the next section, makes a better choice.

## Related Patterns

11.3 Pattern: Pop-up Alert

## 11. 3 Pattern: Pop-up Alert

## H ow It W orks

When an alert condition occurs, the system pops up a lightbox, while also often darkening the background of the current task. The popup requires the customer to choose one of the actions that displays on the alert, which use up to three buttons on the bottom of the popup window.

## Example

A typical implementation of a three-button Pop-up Alert is shown in Figure 11.13.

![](images/fab5283cf65403735168145f08bfe37b4065f7b1e3e9f5b1d91377d0cc165689.jpg)  
Figure 11.13: The Mailchimp app includes a typical Pop-up Alert with three buttons.

Note that the alert stops the proceedings, requiring the customer to take one of the three actions offered by the popup.

Another appropriate way to use the Pop-up Alert is as a warning about the system state; as shown in Figure 11.14, it warns about the battery running low.

![](images/938eb737387cfd81dac9cfd27349070dd66439bacfedcda2aa04de85430c3960.jpg)  
Figure 11.14: This system Pop-up Alert warns about a low battery.

## W hen and W here to Use It

Use this pattern when you need to disrupt the current task flow with an alert that requires the customer to take a (preferably urgent) action. Pop-up Alert is the atomic bomb of the alerts arsenal; use it with caution.

## W hy Use It

Sometimes things go wrong and you do need to shout “Stop the presses!” The Pop-up Alert does the trick and suspends all other operations of the device until the customer takes some action.

## Other Uses

![](images/cd13bd391a7fb60d73ca44678c47cdfe985063100c151633de7703c6a5b802f9.jpg)  
Figure 11.15: You can use the Pop-up Alert as a Welcome tutorial this example from the Maps app.

![](images/9ba3869cda0951f60166cf09b3e22cf66df51405f904c332e18606ac3e02642c.jpg)

For more information about terms and conditions and Welcome tutorials, see Chapter 5, “Welcome Experience.”

## Pet Shop Application

In the Pet Shop app, you can use the Pop-up Alert to give the customers a reminder of the benefits that come with registering their pet. (See Figure 11.17.)

![](images/7783872bacecf42f89c43d66dbcfed635afa154667494791bad3047c83cca10a.jpg)  
Figure 11.17: The Pop-up Alert is used as a reminder to register in the Pet Shop app.

The reminder has only a single button—OK—and is shown only one time when the app first loads.

The buttons on the bottom are fairly awkward to tap and can be hard to find. If you do end up using this pattern, consider smaller size modal windows that sit on top of the existing content background, leaving some empty space around the edge of the popup.

![](images/3cfb470a672724411d1f96710bd24d8741db588edc15a48d26a21cd47dff9464.jpg)

## Terms of Use

By clicking Agree, you agree to be bound by the eBay Mobile Privacy Policy and Terms of Use.

## EBAY MOBILE APPLICATION PRIVACY POLICY AND TERMS OF USE - United States

Revision Date: August 14, 2012

Last Modified: May 07, 2012

This Application, Privacy Policy, & Terms of Use © 2010 - 2012 eBay Inc.

By using this eBay Mobile Application and related Widgets (collectively, the " Application"), you agree to be bound by this eBay Mobile Application Privacy Policy and Terms of Use. Certain features of this Application may require you to be an eBay member or provide personal information and your use of these features and this Application is also subject to the www.ebay.com Privacy Policy and User Agreement

## PRIVACY POLICY

This Mobile Application Privacy Policy applies to your use of the Application and tells you how we use and protect the information we may collect.

Data Collection and Use. This Mobile Application Privacy Policy describes how this Application collects, uses and protects your information. When you use this Application, we may collect, use and store some or all of the following, for the purpose of providing you a mobile eBay user experience:

• Device sign-on data (including device ID)

Location data

● If you don't have an existing eBay account, personal information when you register for an eBay account

• An encrypted copy of your eBay user ID and password

•Your preferred language and country site

•Your email address and correspondence sent via the Application

● Information about how you interact with the Application and the applicable eBay site(s)

• Information you provide to or input into the Application

We and our service providers use this information to operate and improve our eBay applications, sites, services, and tools

Sharing information. We may share the information we collect with members of the eBay corporate family to provide joint content and services (like registration, transactions and customer support), to help detect and prevent potentially illegal acts and violations of our policies, and to guide decisions about their products, services and communications. Members of our corporate family will use this information to send you marketing communications only if you have requested their services.If you have accounts with or use more than one eBay Inc. mobile application, we may share a limited amount of your information within the eBay Inc. mobile applications in order to improve your mobile experience.

This Application may use third parties to provide parts of our services as well as to provide analytical data about your use of the Application back to us. We may deploy devices such as cookies that enable those third parties to anonymously collect and aggregate usage data and report it back to us. Third parties that we contract with to

## Caution

In his seminal book About Face (2007, Wiley), Alan Cooper famously called the Pop-up Alert pattern “stopping the proceedings with idiocy.” That’s a perfect description of using the Pop-up Alert incorrectly, and there are many ways to do this, so much so that I selectively chose the examples for this “Caution” section.

One of the common antipatterns is discussed in Chapter 9, "Avoiding Missing and Undesirable Results." It uses the Pop-up Alert to show no results conditions, as the Booking.com app does in Figure 11.19.

![](images/eaa29e87a287f6c3f4fb1f5b62c6c87094372accc31d4ab4c6e5a17bfbff80ca.jpg)  
Figure 11.19: The Pop-up Alert can be an antipattern if it shows a no results condition as it does in the Booking.com app.

Another misuse of the Pop-up Alert is to use it to show that the wrong data has been entered via a wheel control, as shown in Figure 11.20. Refer to Chapter 10, “Data Entry,” for the right way to show Date and Time wheel input issues.

![](images/73c039ad9c12157b2f021859dc0072856a23359733db4ef078971721a04a5615.jpg)

![](images/d8cafd97316fbde45977d21cc8c8da5018c02630c27181bf5f53ac6f4c640c00.jpg)  
Figure 11.20: This Pop-up Alert antipattern shows the Date and Time Wheel input errors in the Booking.com app.

But the Pop-up Alert misuse prize goes to the Yelp sign-up form, which uses it to reveal form errors, one at a time. The proceedings are stopped by the idiocy of having a Facebook sign-up pop-up alert, which sets up the playing field nicely for all the other pop-up errors, that march across the mobile screen like an out of tune Highland Pipe Band. The Pop-up Alert Legion Antipattern is shown in Figure 11.21.

This is the equivalent of “slapping” your customer “with a splintered ruler,” one strike for each mistake he makes (as Alanis Morissette so brilliantly sang in “All I Really Want”). This antipattern will annoy your customers and greatly negatively impact the completion rate of your form. As egregious as this sequence of Pop-up Alerts looks, this pattern is unfortunately fairly common. A much better alternative is to use the Inline Error Message pattern described earlier in this chapter; not only does it avoid the strike of the ruler (having to tap OK on the Pop-up Alert, which many people equate to acknowledging that they are “idiots”), but it also shows all the missing and error fields at the same time, so the customer can correct them all at once and resubmit the form correctly.

![](images/987a6652678bf270ab1380a431676d581c58245b346c0af997a8f503c9175a7a.jpg)  
Figure 11.21: In the Pop-up Alert Legion antipattern, multiple Pop-up Alerts show form input errors one at a time in the Yelp app.

## Related Patterns

11.1 Pattern: Inline Error Message

## 11. 4 Pattern: Callback Validation

Sometimes, it’s impossible to validate form inputs in-situ using only client-side code. The Callback Validation pattern is the mobile equivalent of the Ajax call that allows an asynchronous server trip for more sophisticated dynamic databasedriven validation.

## H ow It W orks

When a chunk of customer-input data needs to be validated on the server, the system detects when the input is completed and issues an asynchronous server call to validate the data, returning with one of two states, OK or Fail. Fail states are often accompanied with the dynamic suggestions meant to help customers correct the error condition.

## Example

A great example of the Callback Validation pattern is the Twitter app registration form.

![](images/b3ba74ef154c219234004c4dd5be9efcf537ea3eb3246fe71cfe99b706f2985a.jpg)  
Figure 11.22: The Twitter app includes an excellent implementation of the Callback Validation pattern.

The Twitter app waits for a delay of approximately ½ to ¾ of a second (500 to 750 milliseconds) in the typing of an @username and uses that delay as a starting point to issue the server-side lookup call to determine if the username is available. The typing delay is a more robust and satisfying way to issue the lookup call than waiting for the press of the Next button or an OnBlur event, even though it results in a lot of “false negatives” when the customer has not yet finished typing the full username.

## W hen and W here to Use It

Any time the client-side validation does not provide enough information or robustness and a server-side trip is necessary, use the Callback Validation pattern as a preferred method of validation.

## W hy Use It

As the speed and availability of mobile networks keeps improving, the customers are beginning to have expectations of near-instant contextual feedback. The Callback Validation pattern satisfies their craving for nearly real-time system response by looking at the break in the typing pattern instead of waiting for the submission of the entire form to report the error.

## Other Uses

Callback Validation is not just for usernames. You can use it for any kind of entry that needs to be validated using a server-side call—for example, airport names; hotel, flight, or car availability dates. Or you can use it for potentially any dynamic entity that can also be entered using a server-side variation of the Text Box with Atomic Entities pattern (discussed in Chapter 10).

## Pet Shop Application

With more than 7 billion people in the world today, picking a clever yet unique username is becoming more and more of a challenge. Actually, it is a task that is important enough to use a dedicated page for picking a username and providing some auto-suggestions, as the hand-drawn example in Figure 11.23 demonstrates.

![](images/6ca181a484ebc84ff85c98251eda583e75b371d7381519a71d685ab1a4662a01.jpg)  
Figure 11.23: The Pet Shop app sports Callback Validation with auto-suggestions.

Just as the Twitter app detects a brief break in the typing, the Pet Shop app would do the same. However, in addition to saying that the username is taken, the app also offers some clever suggestions based upon the customer information entered in the previous screen (not shown). Data such as fragments of the area code, street address, ZIP code, pet type (dog, cat, or “bulldog”) can all be used to help people create suggestions.

## Tablet Apps

If you need your app to display auto-suggestions in addition to the dynamic validation, it helps to have a dedicated page for this type of interaction, as shown in Figure 11.23. However, a separate page is not necessary, especially on larger devices like tablets. Tablets should use this Callback Validation pattern more, which will probably occur in the near future. This pattern is especially pertinent for tablets because many of these devices operate on a strong Wi-Fi signal, rendering response capabilities that are similar to those of desktop web apps, where the Callback Validation pattern using Ajax is an accepted and expected part of the web.

## Caution

As with any mobile pattern that requires a server-side call, be aware that the signal may not go through, so build a robust backup strategy for validation using a server-side call after the entire form has been completed. It might show exactly the same UI as it would when the asynchronous call has been issued, even though the original asynchronous server call did not go through.

The Callback Validation pattern as used by Twitter strongly drives the “append” strategy of error recovery; in other words, the customer is most likely to recover from the error by appending additional characters to his username, as shown in Figure 11.22. If that is acceptable for your app, this version of the Callback Validation pattern works great. As an alternative, you might present some autosuggestions alongside with a statement that the username is not available, as shown in the Pet Shop app section.

## Related Patterns

10.9 Pattern: Text Box with Atomic Entities

## 11. 5 Pattern: Cancel/OK

For designing forms, at some point in the process, clients inevitably ask, "Should I position the buttons as OK/Cancel or Cancel/OK?" This pattern describes how to position action buttons and hopefully to help you avoid 3-hour meetings devoted solely to this topic.

## H ow It W orks

Action buttons are positioned as Cancel/OK on the top or bottom of the form. The primary button is on the right and is sometimes larger or implemented with a more saturated color and/or icon. Often, the primary action button is disabled at the beginning of the process before a valid value is entered into the text field. (The last option is not recommended; see the "Caution" section.)

## Example

The reference example of this pattern shows the action buttons positioned on top of the form in Android Calendar, as shown in Figure 11.24. The buttons remain on the screen even when the form scrolls up and down.

![](images/f1428198c6bc3c79e7f4efbd8799dcaf461e6614a453c371a2be0e7bee44289c.jpg)  
Figure 11.24: This reference implementation of the Cancel/OK pattern is from the Calendar app.

Even though both buttons have the same gray color saturation, they have different icons, with the OK (Done) presented as the check mark and Cancel as an X.

![](images/1c690b6d7ab74eb94c9e418e9d8eeafa24adfbaf94c9b5535c958d124c62af92.jpg)  
Figure 11.25: This second reference implementation of the Cancel/OK pattern is shown in lightboxes from the Calendar (left) and Contacts (right) apps.

The OK button is disabled for the Contacts app lightbox because there isn’t yet a valid value in the form field. This is a common part of the pattern for simple forms or those that implement the Callback Validation pattern, but you must be cautious when disabling the action button (see the later "Caution" section for this pattern).

An alternative implementation with the buttons on the bottom of the screen is the search form from the Trulia app, as shown in Figure 11.26.

Even on the black-and-white picture you can tell that the primary action button (Find Homes) is much wider and more saturated in color (in real life it’s dark orange) than the secondary button. Also Trulia uses descriptive verbiage on the button instead of the generic Search or OK.

![](images/4c8329c676cdb501ccf09970462220ba08ee4cf07b1eae958e35215fb6fe1bac.jpg)  
Figure 11.26: This form (with buttons at the bottom) from the Trulia app is a great alternative Cancel/OK implementation .

## W hen and W here to Use It

This is the standard pattern that should be used for every form in your application.

## W hy Use It

Why implement action buttons as Cancel/OK instead of vice versa? This is not an idle question. Ergonomically speaking (read more about device ergonomics in Chapter 3, “Android Fragmentation”), the button on the left is easier to tap when operating the mobile device one-handed. Why would you want to override this natural convention and switch the buttons? The Cancel/OK convention on mobile stems from the early mobile phone app designs, which come from the western convention of reading from left to right. Following this convention, buttons on the left (Cancel) usually take you closer to the top menu or home, whereas the buttons on the right (OK) take you deeper into the Information Architecture (IA) of the device down to the leaf node of whatever function you are looking for. Thus the convention of Cancel/OK has taken a firm root in the smartphone design, even though some apps still refuse to follow it.

## Other Uses

What should you do when you have only one button? If you follow the same convention (that the right side is equivalent to more or deeper into the IA), you should put it on the right side of the screen. However, for a single button, the ergonomic considerations often win, as in the example from the Contacts app shown in Figure 11.27, which places the button on the top left.

![](images/20e708a0ef7454bb0d66a44bbc49e0b27fbf07ff2be31aca56f94c7a5252da05.jpg)

In the Android OS, the menu is traditionally assigned to the right side of the screen. Thus the menu button placement often wins the right side when competing with a sole action button (which then goes on the left).

Another great solution to the sole action button placement is to make a single large button across the entire width of the screen, as shown in Figure 11.28 on the Kayak search form.

![](images/a20debf13ed94a264dabfa669e3321d3fff5328854865ee41c46dcf4c0bc78fa.jpg)  
Figure 11.28: A sole OK button spans the width of the screen on the Kayak search form.

Unfortunately, although they're functional, large buttons that span the width of the device tend to look a bit goofy and old-fashioned, especially on larger tablet-like devices such as the Galaxy Note. If large cartoony buttons offend your sensibilities, you may want to consider making a slightly smaller button that can still be centered in the middle, as on the Contacts app (see Figure 11.29).

![](images/661aafd2ec5aaaa2d71339c6014ec4d0b7c23c498c101dafc47c8441b252710d.jpg)  
Figure 11.29: The Contacts app uses a smaller sole Add Another Field button in the middle of the screen.

Provided the sole action button is sized to at least 30 to 50 percent of the width of the screen, the central placement is both attractive and ergonomically satisfying, which makes the design in Figure 11.29 a good choice.

## Pet Shop Application

The Pet Shop app follows the Trulia model to make the primary action button Register Pet stand out with both size, color, and a check mark icon. Refer to Figure 11.4 to see how this looks in a hand-drawn wireframe.

## Tablet Apps

This pattern applies to tablets with the caveat that the entire button group be placed along the right edge of the device for easy accessibility without compromising hand position on the tablet. The example from the Calendar app in Figure 11.30 includes a good version of the recommended implementation, even though the buttons are reversed (OK/Cancel instead of Cancel/OK).

![](images/344daf5e429d75e3b77c6428bff9ced02d1c80db0ced18f55fe8481db3887570.jpg)  
Figure 11.30: The Calendar app includes a good placement of the Cancel/OK button group on the top-right edge in the Samsung 7-inch tablet; although, the buttons are reversed.

Provided the action buttons are near the edge of the screen, the top placement is preferable to placing action buttons at the end of the form because of the better ergonomics. Top placement buttons are easier to find and enable optional form fields to be ignored without having to scroll all the way to the bottom of the form. The information in the "Caution" section does not apply to tablets. Unlike the smaller mobile devices, tablets are held in two hands, so there is no hand contortion needed to tap the top action buttons.

Unfortunately, tablet apps often ignore both ergonomics and conventions and place action buttons in a haphazard manner, which is an antipattern, as the lightbox in Figure 11.31 demonstrates.

![](images/14603f754fff70067fb7d045b644458d8294b0e8f195e5f0c6ecfcf06782afaa.jpg)  
Figure 11.31: The haphazard placement of the action buttons in the Calendar app on a 7-inch Samsung Galaxy Tab is an antipattern.

Even though the lightbox is fine, the action buttons are in the wrong order. The OK button is far away from the fingers of the right hand (which is the dominant hand for the majority of the population), and both buttons are presented in the same size and visual treatment. Set is a smaller word label than Cancel, which means that the primary action button is further de-emphasized! (The label “Set” is also unexpected; the more standard label for this action would be “OK.”) Finally, note that the Cancel button is also much too close to the scrolling calendar, suggesting that it might be hit by accidental swiping. Altogether, this “antipattern smorgasbord” creates a strong possibility that people will often tap the Cancel button by mistake instead of tapping the Set button and thus will be frustrated several times a day—each time they need to add an appointment.

## Caution

Should you place actions at the top or at the bottom? It depends. The action buttons positioned at the top are easy to find, which is essential for a form like the New Event form in the Calendar app (refer to Figure 11.24) because most fields are optional, and in 90 percent of the cases, the customer will not scroll to the bottom of the screen.

However, obvious placement comes at a price of ergonomic accessibility: Buttons at the top are difficult to tap with one hand. This is both good and bad. Top placement is bad because most people expect to operate their device one-handed. For precisely the same reason, the top placement of action buttons is also good because the action buttons are out of the way and are unlikely to be tapped by accident.

For a one-time registration form, top placement is a good choice because you want your customers to be careful while filling out the form. However, for the Calendar app’s New Event form, it’s a bad choice because people want to comfortably use one hand to accomplish routine tasks like entering an appointment. Then why are the buttons at the top? For the Calendar, the optional form field requirement wins out, so the action buttons get top placement; placing them at the bottom of the form would require a lot of scrolling every time your customers fill out the form. For the Calendar app’s New Event form, having the customer contort his hand to tap the top action button is the lesser of two evils.

Should you disable the primary action button until the form is filled out correctly? No. Disabling the primary action button is usually not recommended unless the form is simple or uses a Callback Validation pattern. If the action button is disabled in a long form and something that's not obvious is missing, the customer will need to hunt around the screen. That puts him at risk of not finding whatever it is that is missing/incorrect, which increases the chance that he will abandon the form altogether from sheer frustration. For example, if the action button were disabled in the Yelp form shown in Figure 11.32, the customer may never find out that he is missing the required Picture field, as it is nowhere labeled as required. And furthermore, pictures are not usually required in forms.

![](images/83a57277eb45b09ac41ca12573bc9c31f99215b7691821ec6c313faf24a24cf4.jpg)  
Figure 11.32: If the Sign Up button was disabled in this Yelp form, the customer may never find out that the Picture field is required.

However, because the action button is available and active, the customer may try to submit the form and get the error, which facilitates the corrective action. The result is a more robust and customer-friendly experience. In that case, even this rudimentary Pop-up Alert is better than no error reporting, which is what the disabled action button is tantamount to. (Recall that you should not use the Pop-up Alert pattern Yelp uses for reporting form errors—use Inline Error Message instead (see the “Caution” section for “11.3 Pattern: Pop-up Alert”). However, if you decide to ignore this warning and go with the disabled primary action button in your form, at least make sure you do some customer testing of the finished interface.

Should you make the primary action stand out compared to the secondary action? Absolutely. The recent trend has been to make both Cancel and OK look the same, as in the Kayak app refine screen shown in Figure 11.33. This is an antipattern.

![](images/b60f4fcb34f5750ca795d0d64d372aee41cb2a50f09f465f49f6e44f9e2177ef.jpg)  
Figure 11.33: Antipattern: Cancel and OK look the same in the Kayak app refine screen.

This is a bad decision because customers rely on subtle visual cues such as color saturation, size, text, and placement to make the choice of which button to tap. Do help your customer out, if you can, by making it absolutely obvious which button to push. As Steve Krug so famously quipped, “Don’t make me think!” in his seminal book by the same title (2005, New Riders). This advice goes double for small mobile screens, where text on the button is often difficult to read in bright sunlight or because the device screen vibrates while the user walks or rides in a vehicle.

## Related Patterns

11.1 Pattern: Inline Error Message

## 11. 6 Pattern: Top-Aligned Labels

When it comes to labels, top-aligned is the standard implementation.

## H ow It W orks

When the form is presented to the customer, form labels appear above the fields.

## Example

The Android reference implementation is the Calendar app’s Add Event form, which is a frequent example in this chapter. (See Figure 11.34.)

![](images/b779cc8a896dba2956c2d598c0606a6751c3b6f771066723beb357b0204994e1.jpg)

Calendar uses the standard Android 4.0 Ice Cream Sandwich OS visual scheme, so the labels appear in a smaller uppercase font, whereas the in-field Input Mask appears in a slightly larger mixed font. This can create a bit of confusion because everything runs together, especially on mobile devices with smaller screens.

A more OS-agnostic presentation of labels is on the eBay app registration form, as shown in Figure 11.35.

![](images/0ca91012532d36372e36965fd6af07ee329e7138a992a70defc4e051af56d02e.jpg)  
Figure 11.35: The eBay app uses a device-agnostic style for the Top-Aligned Labels pattern.

eBay’s form fields are actual full boxes, which separate from the field labels better and create an overall cleaner user interface than the reference Android OS implementation. However, that is solely my opinion. What is a well-researched fact is that mixed case text offers better readability than all uppercase text. Presumably this insight applies equally well to form labels, so you might want to take that into account.

## W hen and W here to Use It

Any time you present your customers with a mobile form, you should use topaligned labels.

## W hy Use It

According to Luke Wrobleski’s research that he presented at Design 4 Mobile, Chicago 2010 (http://www.lukew.com/presos/preso.asp?23), which is supported by my user research, top-aligned labels offer the best all-around versatility and usability on mobile.

Here’s how top-aligned labels compare with other types of labels:

■ Left-aligned labels: Compared with the top-aligned labels, left-aligned labels limit the size of the readable portion of the field, as shown in the form from Southwest in Figure 11.36. Note that even a modest-length e-mail address does not fit completely into the input field.

![](images/e92feb15edace6af40cb825e0e953835bb924d9e83f874c12b7c3f69440d54ad.jpg)

![](images/6359b18360978282ddd63f5ddf874963c4a6f115118a290fd80e094c82cafc49.jpg)

■ In-field labels: In-field labels are another popular alternative to the Top-Aligned Labels pattern. In-field labels generally work fine for short forms, such as Login, but they make it easy to get lost in a long form.

The problem is that the label is lost as soon as the person starts to edit the field, so the current field your customer is on and all the previously filled-out fields no longer have any labels. This is not the best option on mobile because if the customer is interrupted or distracted (as happens a great deal on mobile) she will not be likely to remember what the field was that she was in the process of filling out, and she will be confused—or worse, she'll abandon the form altogether. When the customer is editing the textbox with the in-field label, it becomes a plain textbox, as shown in the sign-up form from PayPal in Figure 11.37. Can you tell which field the customer is filling out in the form?

![](images/ecdda539b23f9dbc0cf67bd10da3c73ee356d6c7c7822bcc27174b7625557695.jpg)

![](images/636d4dfe56fb508699dcf2bd53576207b739ac180cd452db1ca03fd669c0bb2f.jpg)  
Figure 11.37: The in-field labels in the PayPal app make it hard to tell what field is being filled out.

In contrast to other labeling strategies, top-aligned labels do not have any of these inherent limitations. They use the entire width of the mobile screen; have complete flexibility to employ any format mask; and remain labeled throughout the form’s life cycle. This makes top-aligned labels the best all-around choice for mobile forms.

## Other Uses

You can also use top-aligned labels to identify the entire group of related controls, such as in the implementation from the Contacts app shown in Figure 11.38. In this case, the blue Events group label (plus a blue underline) delineate a group of two events.

![](images/0d111f52174a684894960bee8d914431e96d7e6e35af5a419b628b75125f17bf.jpg)

![](images/588e7fd05f487d91185b09f6d230c5fbb077cdf5136739e47caec7a90bd943d1.jpg)

## Pet Shop Application

Throughout this book, the Pet Shop app designs mostly follow the standard Android 4.0 Ice Cream Sandwich OS visual design guidelines for fields and their labels. Refer to Figure 11.4 to see how this looks in a hand-drawn wireframe.

## Tablet Apps

Tablet apps enjoy ample real estate, so the Top-Aligned Labels pattern is not a requirement for tablets. However, it is easier to simply follow the mobile design conventions for forms, and that’s exactly what most tablet apps do. Unfortunately, the vertical space is limited when the tablet is in the horizontal orientation, especially with the soft keyboard onscreen (see Figure 11.39).

![](images/69ddb6857a44edd62c0cb80b90ad8b96f9d4d733f530e06f483676e734cbd4eb.jpg)  
Figure 11.39: Top-aligned labels limit vertical space for tablets in the horizontal orientation.

One experimental pattern to try out for this situation is to make the labels fluid. When in the horizontal orientation, make the labels left aligned; when in the vertical orientation, make the labels top aligned. Figure 11.40 is a hi-def wireframe of what such a form might look like (compare it with the Figure 11.39). Because I haven’t seen this customization, it remains an experimental pattern.

![](images/4fca1ac55def03976b7c6339b992afa1d71c89176839ea9978032cde9bc4a50a.jpg)  
Figure 11.40: In this experimental pattern, labels adjust to optimize space based on the tablet's orientation.

## Caution

When using the Top-Aligned Labels pattern, you must be aware of the vertical space taken up by the label. This is particularly important for the group labels mentioned in the "Other Uses" section because those labels take up an additional 36 pixels of vertical space (see Figure 11.41).

![](images/257502ea2a66ab1bca1e71426ef70e6779de66f536f1f913c2fc22fd368678ce.jpg)  
Figure 11.41: A group label takes up 36 pixels of vertical space.

Thirty-six pixels does not seem like a lot, but it adds up quickly for long forms. Also, group labels add a vertical line, which could confuse things a bit with the new Android 4.0 visual scheme, which is almost entirely composed of horizontal lines. Avoid using group labels for simple forms. (See Figure 11.42 for an example of an antipattern of group labels in the Contacts app.)

![](images/4292b1c5dbe303ebe29e7b720542c1362bd3faa902a1337ac976e47d7f7636d7.jpg)  
Figure 11.42: Using group labels for nongroup fields is an antipattern in the Contacts app.

The entire form in Figure 11.42 would be much cleaner and save approximately 180 pixels (5 group headings n 36 pixels each = 180 pixels) of vertical space if it used the standard single-field labels. You can always create groups dynamically, as the customer fills out the form, and update from single-field labels to group labels as needed—for example, if the customer adds another phone number, thereby turning a single field into a group of similar fields.

## Related Patterns

None

## 11. 7 Pattern: Getting Input from the E nvironment

Desktop forms are keyboard-centric and get little information from the environment. In addition, environmental information is not that useful; most desktop web forms are filled out in the office or at home, so the environment remains static and yields little useful information. In contrast, mobile forms are frequently filled out on the go, so they can often benefit from surprising amounts of environmental data collected with a mobile device.

## H ow It W orks

Whenever the form needs to be filled out, the mobile device uses the read out of the on-board sensors (voice, gestures, accelerometer, location, images, video, and ambient light) as form input.

## Example

Chapter 7, “Search,” describes at length how voice can be used as an input mechanism. Gestures as input are used often in games such as Angry Birds, Fragger, Hungry Shark, Grabatron, and Burn the City—although you rarely consider game inputs to be forms. (Although of course that’s exactly what they are.) Figure 11.43 shows a welcome animation that explains the gestures for putting everyone’s favorite angry bird into explosive action.

![](images/56f8be9965044fec54fe7782e9d2c01aa2aa0bf64a5661fdd0ef3126c671f40a.jpg)  
Figure 11.43: Gestures are used as input in the Angry Birds game.

Gestural input doesn't need to be limited to games, however. Map-based inputs are fairly common, with the on-screen map area (located by pinching and stretching gestures) used to constrain the corresponding list in the example from Trulia shown in Figure 11.44. Zooming out on the map presents a longer list of homes, going from three (in the screens on the left) to seven (in the screens on the right).

![](images/abc14cc705d8f7ce9a4caca198ef756f3d09f7d4fbf40396587a7f99ac5fca68.jpg)

Gesture-based character input has a long history on touch devices, starting with Graffiti apps in the early versions of the Palm Pilot. The latest iteration of the original Graffiti input method is the Gesture Search app from Google Labs. Gesture Search enables simple phone operations and shortcuts to be performed by drawing letters and symbols using the entire screen as a touch pad and the finger as a stylus. The interface also enables customers to erase letters by drawing a horizontal line. (See Figure 11.45.)

![](images/2de1b003e66ab6ca68f7c7f0e7bc8dad8b71334811dbb7c5c0b6415d3438e524.jpg)  
Figure 11.45: Gesture Search uses sophisticated gestural form input.

Another popular option to get input from the environment is to use Location as an input. As Luke Wroblewski reported in his Design 4 Mobile 2010 workshop, location can be obtained by the mobile device through many means, each of which has different performance characteristics, such as speed, precision, and effect on the device battery. Although the mobile industry usually abbreviates the entire bundle of location services as “GPS”, Global Positioning Service (GPS), the satellite navigation system, is only one of the ways the phone obtains location information. It is the most accurate method; it can locate the mobile device to approximately 33 feet, but it can take anywhere from 2 to 10 minutes to obtain the position. Also, using GPS drains the battery quickly.

Another popular location service is triangulation using multiple cell towers. Cell tower triangulation has a negligible effect on the battery and provides nearly instant location information to a range within 1,600 to 8,200 feet for a single tower and 328 to 4,600 feet for multiple towers.

Most mobile devices obtain location information via a combination of both methods (plus Wi-Fi, when available). When location function is first called, most people observe the phone drawing a large circle initially based on the cell tower triangulation. If GPS is enabled, the location circle gets progressively smaller, and the location gets more precise in a few minutes as the GPS comes online. Location is a favorite input for mobile devices because it is useful for local in-person interactions, such as those facilitated by Yelp (see Figure 11.46).

![](images/49ca1e772fa6b2902ea11b09a6eb6f85963ade773201fcb7300b33adbcff9324.jpg)  
Figure 11.46: The Yelp app makes effective use of location-based form input.

Image-based input is becoming increasingly common as well, particularly to take a picture of a QR code. QR codes can have a variety of payloads, depending on the size of the code and encoding density—from a chunk of text nearly the size of the American Constitution (4,296 characters to be exact) to phone numbers and URLs, all of which can be used as simple form inputs. QR codes can also encode a variety of specialized formats, such as MeCARD, which contain complete structured data that can be interpreted for the purposes of filling out a form. Out of the many QR code readers currently on the market, Red Laser remains one of the easiest to use and the most versatile (see Figure 11.47).