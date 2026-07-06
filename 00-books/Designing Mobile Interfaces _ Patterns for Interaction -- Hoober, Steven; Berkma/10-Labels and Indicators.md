# Labels and Indicators

## Down Under and Backward

Many of you have had experiences traveling or moving to another country. The opportunity to become immersed into another culture can be quite exciting while also a bit intimidating. Having recently moved to Australia from the United States, I’ve been encountering many cultural differences that I have been forced to quickly adapt to. Not all have been so easy to grasp. Here are just a few.

## Phone Numbers

The Australian Communications and Media Authority, which maintains and administers the telephone numbering plan, established a Full National Number (FNN) that is composed of 10 numbers: 0x xxxx-xxxx. The first two digits are the area code; the next four generally make up the Call Collection Area and Exchange. The last four numbers define the line number at the exchange.

Mobile numbers also have 10 digits but follow a different structure: 04yy yxx-xxx. Originally, the y digits indicated the network carrier. But now that Australia allows for Wireless Number Portability (WLNP), like the United States, there is not a fixed relationship between these numbers and the mobile carrier.

So, giving my new mobile number out to people was a bit confusing. I was always following the landline format of 0x xxxx-xxxx and getting a few confused looks.

## Gas Types and Pricing

So much to choose from, and so little knowledge! There’s E85, ULP (Unleaded), E10 (ULP + 10% ethanol), PULP (Premium), UPULP (Ultra Premium), Diesel, and LPG (Liquefied Petroleum Gas). Unlike the United States, where gas is sold by the gallon, Australia sells it by the liter and it is priced in cents. A typical petrol price of ULP may be 135.9. Having a US pricing format embedded in my head, I was shocked at first to think that gasoline was \$135 per liter, though my sense quickly rationalized this was a wrong deduction.

## Date Format

My first experience with this confusion occurred when I was applying for both my visa and my overseas health insurance and I had to enter my date of birth. The visa application was clear in the format I had to enter: day/month/year. The insurance form was not. It was a paper form with blank squares for each separate character.

The empty boxes had no label under them, just ☐☐-☐☐-☐☐☐.

In Australia, this format is culturally understood. However, for me it’s quite unclear. Do I enter my month or day first? Each of those fits within the constraints of the provided format. Yet each clearly yields an entirely different result.

## Understanding Our Users

As designers, we can limit these confusions by designing better UIs that meet the needs of our users. To do this, we must consider who are users are, what type of prior knowledge they have, and the context in which the device will be used.

## Users and Their Prior Knowledge

Mobile users come from a variety of cultures with a multitude of experiences, skills, and expectations. If the devices’ UIs cannot meet these user requirements, their experiences will quickly turn into frustrations while their actions result in performance errors.

To prevent this, start by identifying your users early in the design process. Use methods of observation, interviews, personas, and storyboards to gain insight into their needs, motivations, and experiences. Refer to this collected data to validate and guide your design decisions throughout the design process.

## Context of Use

Unlike desktop users, mobile users will use their devices anywhere and anytime. These users may be checking an email while walking down the street, snapping photos during a traffic jam, or lying in bed playing a game.

In all of these situations, external stimuli are present that affect the amount of attention the user can use to focus on the task at hand: lighting conditions, external noise, and body movements are all stimuli that affect one’s attention. Consider the effects of how bright sunlight on a glossy screen limits our ability to distinguish details, colors, and character legibility. Similarly, when the device is shaking up and down in the hands of the user as he walks down the street, selecting an element on the screen becomes prone to error.

These external stimuli are not always controllable, but the device’s UI can at least be designed to limit the negative effects on the user experience. Using labels and indicators can redirect the user’s attention away from the external stimuli and back to the task at hand.

## Labels and Indicators in the Mobile Space

Labels are either text or images that provide clear and accurate information to support an element’s function.

Indicators are graphical elements supported by text to provide cues and/or user control on the status or changes.

As you are now aware, displayed information is not always easily understood or easily detectable. The use of labels and indicator widgets can provide assistance with these issues through surface-level visual cues and functions. These visual cues and functions can help our users better understand the current context within the device. Labels and indicators can be used in the mobile space to:

• Indicate the current status or progress of the state of the device (see Figure 7-1)

• Present additional information, tips, or advice to clarify the current context

• Present information, especially text and numerical data, in the most appropriate and recognizable format for the context and viewer

• Provide user controls for operations involving access to remote servers

## Visual Guidelines for Labels and Indicators in the Mobile Space

![](images/8f8babf9e94e3d558417290e798f838def5a8ed437916b6ae8b1540b09bc7d3c.jpg)  
Figure 7-1. As we get better and better hardware and networks, we ask more of them. Delays appear to be inevitable. Do what you can to label, and communicate within context, so that users have some information to occupy and guide them.

The following are some visual guidelines for using labels and indicators on mobile devices:

• When using small text for a label, there must be a luminance color contrast from the background. The ISO recommends at least a 3:1 ratio between the luminance of text to the luminance of background color.

• When using color to show detail, luminance contrast is the most important principle. Using black and white together has the strongest contrast. Other effective combinations are yellow on black and dark blue on white (Ware 2008).

• Use symbols that are easily understood and represent the intended function. Use symbols familiar to your users, not to the designers and developers.

• When using animation, objects that have a constant motion may become habituated to the user, and may end up being ignored.

• If an object must grab a user’s attention, consider having it emerge, disappear, and reemerge every few seconds or minutes into the visual field. Be mindful of the overuse of multiple objects moving on a screen. The user will become easily distracted.

• Objects used to signal the user should emerge and disappear every few seconds or minutes to reduce habituation.

• Use motion, such as rotation or fill, to indicate an ongoing status change. Static objects provide a lack of feedback when it comes to progress or status. Users might feel such an indicator has “frozen up” if it lacks motion, especially if it has arrows or otherwise evokes movement.

• When possible, use images that evoke meaning, emotion, or desire to your users. These images will increase the user’s motivation to attend to these objects. If objects lack these emotional values, users will overlook and avoid them. One example is to use recognizable images as avatars that represent people we know. This works effectively well in contact lists. Better to avoid “default” objects that are repeated (Saffer 2005).

## Patterns for Labels and Indicators

Using appropriate and consistent label and indicator widgets provides visual cues and functions to communicate the current context of the device. In this chapter, we will discuss the following patterns based on how the human mind organizes and navigates information:

## Ordered Data

Presents textual information in the most appropriate and recognizable format for the context and viewer, while considering user expectations, norms, and display size constraints

## Tooltip

A small label, descriptor, or additional piece of information that is displayed to further explain a piece of content, a component, or a control

## Avatar

An iconic image or profile used to represent or support the label for an individual

## Wait Indicator

An indicator used to inform the delay status of a loading component

## Reload, Synch, Stop

User controls for operations involving access to remote servers, including override

## Ordered Data

## Problem

You must display information, especially text and numerical data, in the most appropriate and recognizable format for the context and the viewer.

The presentation of Ordered Data is largely a matter of design, and can be implemented with any technical means. For many interfaces, such as all websites, it is important that only the proper data be sent, so this is implemented at the server side. Any level of client software will work equally well.

## Solution

Content types that are routinely displayed have become regularized in their display. You have to present them in specific formats so that they are easily recognizable to the users.

The types of data being discussed are, for example:

## Names

Should the first name appear first or last? Should it include the middle name, initial, or neither?

Times

Should you use 12 or 24 hours? Are seconds needed?

## Dates

The order of items may vary, and abbreviations are rampant. In some cases, preceding zeros may be relevant.

## Days of the week

This includes languages as well as abbreviations, all the way to single letters in some cases.

## Locations

This includes city, state, and then zip code. But is the state abbreviated conventionally, is it abbreviated with two letters, or is it spelled out? And this is in the US only.

## Units of measure

This includes °F or °Fahrenheit, miles or mi., kilometers or km, and so on.

The list goes on. Some of these may be specific to a population, and may be technical terms or jargon only understood by the user community.

![](images/8d04fca41e771e4d7d633b601963d62b2974139cac09881bdfa60774e76e9925.jpg)  
Figure 7-2. A table showing how tabular data (for The Weather Channel mobile web) can be compressed or expanded as space allows. This shows many methods of displaying several types of ordered data.

The two key challenges you will discover in presenting ordered data are true for all systems, not just mobiles:

## User expectations

In many cases, this can go all the way to universally accepted standards for notation. Units of measure, for example, have standards for long and abbreviated display that should always be followed. Many others have cultural norms instead. Dates are displayed in several formats, commonly flipping month and date, without labels to say which is which.

If your product will be employed by users from different backgrounds, try to use unambiguous display methods whenever possible. For dates, avoid abbreviating months as numerals; 4/11 can be April 11 or November 4, so the only slightly longer “Apr 11” is entirely clear.

## Available space

For columnar display in any interface, but a special challenge on many mobile devices, ordered data types such as dates may have design pressure to be compressed to the point they can become unreadable. Do not just rely on common sense, but refer to universally understood display standards to ensure that the compressed format will be readable. Also consider use of variable formatting based on the available size; if a larger device is used, or the screen is rotated, display larger amounts of information. See Figure 7-2 for an example.

## Interaction details

This is a presentation pattern, and it generally supports no interaction at all.

You may wish to add additional details to explain any ordered data that may be confusing. For example, if a date is shortened to a large extent, a tooltip or some interactive method may present further details. Information can also be optionally presented in multiple formats; for example, a date-time code of “Yesterday” can present a tooltip that says “19 March 2011 at 11:21 a.m.”

All normal interactions are available for any of the information presented. A common method is to provide additional information on each line, accessed by the use of a Link, Button, or other common method.

## Presentation details

There are far too many of these formats to discuss in detail. We already provided some examples earlier in this pattern. Instead, we will use this space to discuss another method of displaying some content types: relative display. This is most useful for dates and times, but as these are very commonly encountered by many types of systems, they are worth detailing.

Relative dates and times use the conventional format users would when in conversation. People don’t say “I called him at 2:17 p.m.” when they can say “I called him about five minutes ago.” Communicating in natural manners like this reduces cognitive load, making interfaces more usable and speedier.

Timings can change depending on the context, but one example of how to do this is:

• Within the current hour, show the time as minutes ago; over 20 minutes, round to the nearest 5 minutes.

• Within the current day, or within eight hours, show the time as the number of hours ago.

• Within the past two days, show the day of the week, and the time range—morning, afternoon, evening, night.

• Within the past week, show the day of the week.

• Older than this, but within 12 months, show as Mmm/DD.

• Older than 12 months, show as the year alone.

## Examples:

• 20 minutes ago

• 8 hours ago

• Tues. morning

• Tuesday

• Nov 20

• 2008

## Antipatterns

Do not rely on user settings to solve cultural norm issues. The vast majority of users will not perform such a setup. Even if forced as part of a first-run process, defaults will be used to speed it up. Customization may be allowed, but ensure that default conditions are clear and unambiguous.

Do not make up abbreviations. If one does not come to mind, it doesn’t mean it doesn’t exist, just that you don’t know what it is. Use reference works to find the correct abbreviation. Always find good references, preferably by the governing body of any technical organization, and do not trust hearsay. Street labels in the United States, for example, are being rewritten somewhat randomly by local departments, and the abbreviation for Lane is now often “La” instead of “Ln.” This sort of change can be confusing.

Do not use the default label values without understanding whether they have meaning. For another roadway example, many digital mapping services use “Street” as the default type of roadway. However, in many cities, saying “Street” means it runs the opposite way of an “Avenue.” This carries as much meaning as assuming that unspecified times of day are “AM.”

Don’t go overboard with interactive display methods. Avoid interfering with the primary interaction of the display, such as selection of a line item. Although tooltips can be helpful, too many can make it difficult to read the rest of the data set.

## Tooltip

## Problem

You need to add a small label, descriptor, or additional piece of information in order to explain a piece of page content, a component, or a control.

The Tooltip is a common interactive element, included in desktop OSes and some mobile platforms. For others, you may need to design and manually build the display method.

## Solution

![](images/41611213b3a24e5708e7d2d2cf211ecade9786743a0695f19d2bff37ff98a1c2.jpg)

![](images/ecc78742612e08002a6aeee6024c42953d93aed6025db814fd4d6eb41da9da5b.jpg)  
Figure 7-3. Tooltips are most often used to explain controls which do not carry a label, such as these video playback controls. Due to familiarity and use of standard symbols, the labels have been eliminated; a Tooltip helps anyone who may be confused by appearing after a delay which may indicate indecisiveness. Tooltips may also show the current state of a control setting, such as the volume level on the right.

A Tooltip is a transient, usually contextual, informational assistance widget. Tooltips are initiated by the user hovering over a potentially interesting target, or they are automatically presented when the system determines that the user needs help—such as during her first visit, or when there is a change in the system since her last visit.

The information presented in a Tooltip will usually be a helpful label, or an addition to the content. Use this information to clarify short labels or icons or to explain jargon, requirements, or systematic needs that may not be clear.

When a function such as a Tooltip is called for, but it may be deliberately displayed by the user or has interactivity in the information label itself, this is instead an Annotation. See that pattern for more details and comparisons.

## Variations

![](images/424716973602daa2183fb2f2d9da428fe51845971e6b09ed10b59aa40943c824.jpg)

![](images/000aaee8cfadbb3dc28f4e3ec223575bc80cd6cbb584e2a52c57665d7fa97583.jpg)  
Figure 7-4. Banner-type tooltips are locked to the bottom of the window or viewport. They can display status information, as shown on the left, or they can display hover-state information. The target URL as shown on the right is a perfect example of information that cannot easily fit into the page, but that some users will want to be able to see before selecting the item.

Floating tooltips are the traditional Tooltip encountered in modern desktop windowing OSes. A small box appears adjacent to the mouse pointer, as in Figure 7-3, above every other item on the page. A small amount of content (almost always just text) populates the box.

Banner tooltips occupy a strip, generally anchored to the top or bottom of the viewport or window. These are most suitable for larger amounts of text, or when a message can appear on the page most of the time. This may carry labels for hover states as the floating labels, or information on the current state or mode of the application, such as a browser status bar. See Figure 7-4.

Banner tooltips that may use the style and functionality of any Fixed Menu or Revealable Menu used within the OS or application should be carefully considered, and may be reused without modification.

## Interaction details

For mobile devices, you will often find no explicit, built-in method to present tooltips, and you will have to develop the behaviors and presentation yourself. For any systems that support hover states (mostly scroll-and-select), any item in focus may display a Tooltip label. For any device, including touch and pen devices without a hover paradigm, tooltips can be used by the system to point out unused tools or new features. The lack of context makes this less immediately useful, and the items to be highlighted must be carefully selected to avoid overselling a single new feature.

Certain desktop systems allow entering a “help mode” where tooltips appear instantly (though still on hover), for all page items, but this has not yet become common in mobile and so cannot be considered a pattern yet.

The information labels, whether floating or in a banner, may not be selected in any way. They should be built so that they do not exist as far as selection mechanisms go; clicking an item behind the Tooltip is not impeded in any way. The Tooltip is simply disregarded, except for its visibility.

Ideally, the Tooltip will not even visually obscure other items. Any label being displayed must get out of the way of other actions the user might request. If any selection is made elsewhere on the page, including entering text input fields, it should disappear immediately.

## Presentation details

![](images/e067d59dce9bb071533c69355f1640bd5c86dc9fe19b1abaafa85060de22a952.jpg)  
Figure 7-5. Tooltips can be used to present all sorts of contextually relevant information that cannot, or should not, fit in the page, and not just for items that are already interactive—for example, definitions of jargon in technical descriptions. Any number of methods can be used to communicate that the item will reveal information, but it should not be entirely hidden.

The banner Tooltip may operate in one of two modes:

## Always present

The Tooltip appears in a permanently allocated space, which is empty when no messages are present. Labels for hover states appear and disappear without delay.

## As needed

Labels and the surrounding box will appear with the timing of the floating Tooltip, but the Tooltip always appears in the same place on the screen instead of adjacent to the relevant section.

You should present any floating Tooltip after a brief pause, to avoid interfering with use of the interactive elements on the page. The delay is intended to reflect hesitation on the part of the user as well.

Only one Tooltip may be present at a time. Moving to another element will overwrite the previous Tooltip or label with the new one.

A floating Tooltip should generally disappear after a few seconds. This timing is infinitely variable depending on the user context expected for the application. If the user is likely to not be paying attention to the screen when the Tooltip appears, the timing may need to be very long, or a banner style should be used.

Any floating Tooltip must be clearly not part of the page context. Use borders, shadows, and transitions to make this clear. It is often best to make it appear as though the Tooltip label is floating above the image, as in Figure 7-5, or protruding from the page. Certain practices described in the Simulated 3D Effects pattern may be used to emphasize this. Base the color, size, and other styles on the desktop standards, whenever possible.

The text inside any Tooltip should only be one line long whenever possible. If it must wrap, never exceed two lines. Avoid truncation, although some labels (such as URLs) make this unavoidable.

## Antipatterns

Do not rely on a Tooltip to solve interaction and interface design problems. If icons are unclear, make better ones, or apply fixed labels, for example.

Labels should never exceed the space available. Do not let them simply float off the page. Label text should not end in ellipses or wrap to a second line. Multiple lines of information may be displayed, but each line should carry its own information.

Avoid overburdening an already complex, interactive interface with tooltips. Though their noninteractive nature may seem to indicate that they can be added freely, they are still observed and must be understood by the user. This may interfere with speed of comprehending the entire interface. Additionally, when multiple small floating items are on a page, it may not be clear what the layer relationship is between them.

## Avatar

## Problem

You must provide a glanceable representation of a person for use in various contact-listing contexts.

Visual representations of any sort can technically be displayed by any platform. Providing the images can be a notable challenge if you have to make the images, or make arbitrary images fit in the space.

![](images/8553d7d1c19093813d78edcc43b00fe99d3a6c9ec8dd8e1d143b4a5f66a4f9f1.jpg)  
Figure 7-6. Avatars add quick scanability to lists; instead of making the user read each item, the user may recognize regularly used images for faster access.

Text is accurate and precise for listing or otherwise describing people. However, text labels can be slow to read, and this is often undesirable in a mobile context. Whenever possible, make the interfaces glanceable and scannable.

Much like the Indicator pattern, an Avatar is an iconic image used to represent or support the label for an individual, such as a contact in an address book.

This pattern is addressed separately from the Icon or Indicator pattern because the Avatar image represents a real person, as in Figure 7-6, not a concept or action, and because in many cases the image itself cannot be directly controlled by the designer or the user of the device.

![](images/6185f891172d5a72267165c73af602eed8b5b5e286ea707596c818a941144cf9.jpg)  
Figure 7-7. Avatars are a good way to label an individual in a very small space. Selecting these should reveal details of the contact, or options relating to the contact.

The two basic types of Avatar are different from other variations in the book in that they vary by individual use. Each one can, and very often will, appear in the same interface.

The first, and most obvious, is any custom representation, as in Figure 7-7. This may be a photo, or a personalized icon or other graphic. It may be loaded by the user of the device (as when a photo is taken of a contact for use on that device alone) or it may have been created by the owner of the avatar (as when the profile image from a social network is automatically loaded).

When no custom image is available, as will occur very often with first-time use, a generic icon or set of icons is often used as a placeholder. Whenever possible, avoid truly generic icons.

As described in the Thumbnail List pattern, irrelevant images may be simply left out. The specifics of your interface will determine whether this is a workable solution. During design, consider the likelihood of most or all items being populated with image content, and make decisions about use of the Avatar pattern accordingly. See Figure 7-8.

Interaction details  
![](images/ac7ca6624505e2a8073b9c2e83310f41611a258b3ad91b3a911bd70e7129f9a0.jpg)

![](images/7257e37c83d7c50b8282ce67be9113b6b2cca6e5848d1d00b03ac0dc97570669.jpg)  
Figure 7-8. When custom Avatar images are not available, either don’t use an image at all (as on the left) or use a generic placeholder that is appropriate. On the right, one of several different stand-in images is used for each unassigned Avatar.

Avatar images may be selectable or not. Be sure to follow the general paradigm of the context in which they are used. If they are used in a line item, such as an address book, you may make them selectable as an extension of the name, as a part of the whole line, as individual items with different behaviors from the other labels, or not at all.

Always consider how clearly the interaction which will follow selection of an Avatar can be communicated. If it is not perfectly clear, add additional information, such as an overlay icon as described in the Icon pattern. Otherwise, consider simply making the Avatar image display only.

When you display an Avatar without a label—such as in threaded messaging or an SMS conversation—the Avatar should always be selectable, and generally either display the user information or offer options for interaction with the individual as a Pop-Up or Annotation.

## Presentation details

Since the image itself often cannot be created, the designer must be careful when selecting borders, background, sizes, and aspect ratios.

Avatar images are almost always square, to account for both landscape and portrait orientation source photos, without adding masking bars to part of the image or causing inconsistencies in the display and alignment of page items.

Generally, to fit to a square, the long sides are cropped off, and the short side is fit to the image dimensions. Occasionally, it may be useful to crop the outer 10% or 20% of the whole image, to ensure that a recognizable face is in the image area. Base all such decisions on the final rendered size and aspect ratio; aside from source imagery varying widely, even very poor images will generally be much larger than the Avatar image.

Though some Avatar selection systems allow manual image cropping, this—as well as photographing within the mobile device to generate images—is not within the scope of discussion here, but should be designed to generate the best possible images and adhere to the design principles of the application or process. Feel free to explore alternative methods; facial recognition software, for example, is now reliable enough that it can be used to automatically crop Avatar images.

When practical, use avatars alongside text labels. When selectable, use the existing paradigms, discussed under the Link pattern, to denote that an image is selectable.

When no supporting label text is associated with an Avatar image, consider use of the Tooltip, when practical and supported by the device’s interaction model. If an Annotation or other interaction may conflict with the Tooltip, make sure label information such as the user’s name is in the interactive selection mechanism as well.

## Antipatterns

![](images/e233e1b580cf597941d97302a850e32b5e86f1821d0d51869fd7538d2f2a4fc8.jpg)  
Figure 7-9. Avoid using the same stand-in image for each Avatar (or so few variations that they repeat excessively). The image should add meaning to each individual use, not just fill a gap in the design.

Avoid using too many generic icons, or only having one style of graphic that serves as a placeholder for every empty slot. See Figure 7-9.

Always keep in mind the value of the Avatar, and do not fill it with arbitrary content to populate a flawed or boring design.

## Wait Indicator

## Problem

You must clearly communicate processing, loading, remote network submissions, and other delays.

The Wait Indicator is common, and is built into many platforms. However, many default messages violate key principles of usability and user experience, not to mention mobile design principles. Even when they are provided, you likely will need to build a custom interface to provide a good experience.

![](images/4b9f776d069a68906a146a8cf92ceb549a1f2e534ae84740b221c85219ca90d9.jpg)  
Figure 7-10. A short Wait Indicator is just a moving graphic that communicates a delay in loading. Explanatory text may or may not accompany the indicator.

A variety of wait indicators are used to inform users of delays that are imposed by technical constraints.

This widget may be used in many ways, as it best serves the needs of the user and the constraints of the design.

Some of the indicators described here are used almost exclusively on an Interstitial Screen. Read that pattern for implementation details, such as cancel functions, that are not considered here. Others may appear as portions of an interface, to communicate loading of modules or individual images.

Another common implementation is the loading bar, often used for web browsers, which may not disable the existing page until some or all of the new page has been retrieved. The Wait Indicator occupies a space along the edge of the viewport, and does not interfere with use of the old (or new) page.

## Variations

![](images/148f4698c7d85d3a920f601cc8463a3f9b4bdc83624b7db1cc10507438bf1a7a.jpg)  
Figure 7-11. Longer delays, when the percentage or time of completion is known, are typically displayed as bars, filling in from left to right. Shown here are two status bars, indicating loading of a web page. On the left, a spinning indicator (to the right) shows continuous progress even if the loading is very slow; also note the reversed text to ensure visibility. On the right, the bar itself has an animation, with the stripes constantly moving to the right to imply movement.

There are a number of variations on this basic theme, all of which will be considered here, as they address the same basic issue:

## Short wait

A one-part indicator used when the wait is very short or when the length of the delay is unknown. This consists of an animated, endless graphic. See Figure 7-10.

## Long wait

A two-part indicator, usually using a horizontal bar to indicate percentage complete and a text counter of size, percent, and/or time until completion. The long wait is used only for processes that take a reasonably measurable amount of time. This cutoff is almost infinitely variable, and depends entirely on the user’s perception of the speed of the system. Sometimes even five seconds, when the user is highly focused on the system, will seem too long for a unitless short wait indicator. See Figure 7-11.

## Ghost

Part of the lazy load concept, heavily used with images, where the content itself acts as the indicator. Think of an image loading slowly, going from fuzzy to sharp, or loading top to bottom.

The entire practice of loading web pages as the content is received is a sort of lazy loading implementation, as shown in Figure 7-12. Consider how slow loading of your page (or of many pages if you are designing a browser-based system) can influence the user, and whether the design may need to be optimized to communicate the delay better.

These variations may sometimes be used in conjunction. If, for example, ghost loading of an image is not entirely clear (and it often is not), you may add an additional short wait indicator on top of the image until it has completed loading, as in Figure 7-13.

![](images/5488811e21e5ca1b7af4d9f384558dd11cec91b657f0d4fb9ad98cb2c33c79c6.jpg)  
Figure 7-12. Wait indicators may take any form that suits the needs of the design and still communicates the delay and progress. Here, images not yet loaded have an animated progress indicator taking up the entire image space. These could also add a percent complete, if needed, and become long indicators.

## Interaction details

The Wait Indicator is the widget that informs the user of status only. It has no direct interactivity itself, though it may be used with buttons, soft keys, or other interactive elements.

See the Interstitial Screen, Infinite Area, and Reload, Synch, Stop patterns for the most common interactions to be used with the Wait Indicator.

## Presentation details

![](images/9f8b200ee2d65c91550f9a9b34ea0b449869e3addd68a41cb21abe96a37e13de.jpg)  
Figure 7-13. Ghost progress indicators use the lack of completeness of the actual content to indicate loading. A typical case is shown here, where images are loaded progressively. To add clarity, or for thumbnails not loaded at all, a short wait indicator is overlaid on top of the image. This is not always needed.

All indicators must remain moving or impart some other sense of movement if the load speed is too slow. Bars with internal animation are a very common solution to this.

Display the units in which any measurements are displayed. Do not just display “67” but “67%,” for example. You may display times in a unitless manner if the format is clear, and individual seconds are counted. For example, “5:15 remaining” is very clearly five minutes and 15 seconds, as long as the seconds change every second. There is no need to add additional labels.

Always make sure any visuals and units accurately map to the percent of task complete. Ideally, timing benchmarks should be made and the indicator updated with percentages in relation to time remaining for the task, rather than tasks pending in the execution queue.

You may save space by having labels appear on top of the indicator bar. However, ensure that labels are visible at all times. Consider reversing the text color pixel by pixel as the bar progresses, to preserve maximum contrast.

When a Wait Indicator is used alongside a content area or in conjunction with the content (overlaid), the indicator will disappear when loading is completed.

Do not use an indicator that is too seamless or unobtrusive, or the user may not notice that it has completed. One minor mitigation is to allow the “fully loaded” state to persist for a few more seconds and give the user more of a chance to see it.

In some cases, another indicator may be needed to indicate that there is no loading. This will usually appear in a permanent status bar, which is where the loading bar would appear. Typical messages are “Idle,” “Completed,” “100%,” and the like. Make sure the message is clear, is contextually relevant, and does not rely on jargon or excess familiarity with the system. This status area may constitute one state of a banner-style Tooltip.

Long delays, especially on mobile devices, may cause the user to not pay attention to the screen when the task is completed. For very long or important tasks, you may wish to announce the end of the delay with:

• A blinking LED

• A backlight that is turned on

• Vibration

• A tone

or a combination of these. If these are used, generally a “completion” message must be made available, to make it clear what has happened and what the annunciator is indicating.

## Antipatterns

Do not use the unitless short indicator just because the delay is unknown. Do whatever is possible to get an estimated time to completion. If that is impossible, be very clear in text descriptions that it will take approximately a certain time (e.g., two minutes) and alleviate the wait in some other way, such as with a tone on completion.

Do not mix paradigms. Develop a system of wait indicators, and use the same type of indicator for similar types of wait periods. Users recognize the distinctions we discussed in this pattern, and they will base expectations on the typically used graphic design patterns, so they may be misled by poorly selected indicators.

Do not allow indicators to stop animating. Users will perceive lack of movement as locking up or taking so long that they will not wait for it and will abandon the process.

Do not imply completion by the use of the wrong indicator graphic. Bars imply completion, and the common practice of repeatedly filling a bar (for each step of an install) is simply misleading to the customer. Rotating items must not be drawn so that they appear to be pie charts filling in, or the same can happen.

Avoid using a Wait Indicator as a mouse pointer, or otherwise mimicking modes from desktop computing platforms. Do not use the Wait Indicator as an error message; errors should be separate and distinct from fatal error messaging. As an example, the “Spinning Beach Ball of Death,” which indicates all system resources are used up, is not a suitable way to communicate this situation, especially on a mobile device.

## Reload, Synch, Stop

## Problem

You must provide the user with controls for loading and synching operations with any remote devices or servers.

Reload, Synch, Stop features are simply represented as buttons, so at the interface level they can be easily built in any platform.

## Solution

![](images/e6259dafb9352e84745eeb641a895caa6aecffd973c721a1df6c6037c4d0f9de.jpg)  
Figure 7-14. Ghost progress indicators use the lack of completeness of the actual Refresh and Stop buttons that are key to all web browsers. Here, the two buttons are adjacent to each other. The Reload button is in use (and should be animated) but is grayed out, and cannot be selected again. The Stop function is available for selection. The status bar reinforces the behavior requested, as does the animation of the loading button, with additional details.

Information from remote data sources provides the bulk of the functionality of interactive mobile devices. Due to specific user needs, accidental inputs, or simply system constraints, your users may sometimes have to manually start or stop data transfers.

Some examples:

• Loading web pages

• Synching with address books

• Synching with email servers

• Submitting transactions

• Transferring files to local devices

• Sending images over MMS

Although as much as possible should be done automatically, user override and user control should always be provided. These will be paired Reload and Stop buttons, either in the application directly or in settings.

![](images/c4b1a48b95aa51983ef1cb2256d56a7d89166909ad8fba7917b8167f6cfbd884.jpg)  
Figure 7-15. Here, the superimposed style has only one button visible at a time. Since the page is loading, the Stop button is the available item. To ensure that this is clear enough, a different status row is used, with the icon seen in the Reload function animated here.

Two very common methods are used to provide these functions. The selection of one over the other is largely up to design principles and space considerations; they are otherwise functionally equivalent.

## Adjacent

Space is provided for both buttons to be visible at the same time. Generally, only one can be active, and the other is grayed out. Disabling inactive buttons and indicating this is usually preferable to removing the inactive button entirely so that users become familiar with the controls. Inactive buttons may also convert to status indicators; a Synch button can spin to indicate synching, while leaving the Cancel button location free to carry out its function. See Figure 7-14.

## Superimposed

Only one space is provided for the two functions. Since they are mutually exclusive, only one function is needed. However, some users may become confused as to the location of the other function, and transitional states (e.g., stopping) require users to wait for their completion. Status may not be well communicated by the buttons, as the alternative action must take precedence. When synching, the button will convert to Cancel and status must be communicated elsewhere. See Figure 7-15.

## Interaction details

![](images/40dda386791f20016197d4dd6eaf1143594f26cbc4e393295fbb59e2f40d3be8.jpg)  
Figure 7-16. Synch and Cancel buttons can appear conditionally, and in different screens. Here, for example, a Synch Now function within application settings returns to the main screen, with an animated status icon indicating that synch is taking place. Adjacent to it is a Cancel button that otherwise is not present.

When the user selects any button, the action should begin immediately.

For either version, you should only allow access to buttons that can take effect in the current state. If a web page has completed loading, do not allow a Stop function to work.

Do not accept duplicate inputs. If a Stop command has been received, do not accept further Stop commands. If the system is poorly built, and might “forget” a previous command, fix the system instead of requiring the user to carry out a simple, single-point behavior multiple times.

For either case, it is best to assume that the request will take a brief time to take effect, and to account for accidental double-taps and other mistaken inputs. Especially if you choose the superimposed design, do not allow conflicting actions, such as Stop immediately followed by Reload. Make lockout periods brief so that a second selection within about half a second is disregarded.

## Presentation details

For either version, only allow access to functions that are available in the current state. Suppress or gray out buttons that do not apply. See Figure 7-16 for more on conditional display.

For functions that have already been submitted, a subtler state change may take effect to imply that the button has converted to an indicator. For example, when a Synch button has been pressed, you should animate the icon to indicate that the synch operation is occurring. Remember that many remote operations, even just stopping a request, will take some coordination to take effect; the in-progress state will take a significant amount of time and so must be represented.

When a status area is present, such as those described in the Notifications pattern or the banner variant of the Tooltip, any current behavior should also be indicated there. This should be true for actions that will result shortly after the process becomes idle. A command to cancel loading should display “Stopping...” or something similar.

Labels, whether as a graphical Icon, a text label, or only as a Tooltip, must be clear and accurate. Do not use “Reload” for a synch operation, for example.

## Antipatterns

Do not presume users will understand that selecting an action again will stop it. For example, an interface may have a Synch button. When selected, it animates. The user is then to understand that pressing it in the animated state is functionally “unsynch,” but in practice this works poorly. Explicitly label all functions, both graphically and with text.

Never provide just one button of a pair. Do not provide a Synch button if you don’t also provide a Stop Synching button.

Never display a status about load or synch behavior—especially not as a modal Pop Up— without a way for the user to cancel the operation. If canceling is technically impossible, clearly explain this, and indicate why.