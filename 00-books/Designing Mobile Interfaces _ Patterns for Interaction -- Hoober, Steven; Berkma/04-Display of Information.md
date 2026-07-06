# Display of Information

## Look Around

Take a moment and look around. Are you inside? Then you might come across books, a pile of mail, your computer, and your television. Or maybe you’re outside, carrying your mobile device and checking your appointments. The world we live in is surrounded by ubiquitous information. Information that is visual, audible, and tactile. It is meant to inform, to entertain, to instruct, and to warn. Because we are constantly bombarded with this information in our daily lives, we must quickly collect, filter, store, and process which information is important to use for specific tasks.

Consider a busy intersection you are trying to cross. You are surrounded by the sights and sounds of pedestrians conversing, cars and trucks honking, birds flying, signage on billboards, and thousands of other types of stimuli. Our minds have an amazing ability to focus on the task at hand, filter the surrounding noise, and process, store, and allow us to act on only the relevant “signal” information.

When the crosswalk signal changes to “Walk,” we identify the sign, interpret its meaning, determine an action to move our body forward, and carry out our actions by walking until we’ve crossed the street, achieving our goal.

Understanding how we process and filter visual information, or data, will help us to design effective displays of information on mobile devices. Let’s first explore the types of information we will encounter.

## Types of Visual Information

All humans have more or less the same visual processing system. However, without a standardized way to explain and notate our perceptions, our communication of this information becomes arbitrary and ineffective when designing to display information on mobile interfaces.

Ware (Ware 2000) introduces a modern way of dividing data into entities and relationships.

Entities are the objects that can be visualized, such as people, buildings, and signs. Relationships (sometimes called relations) define the structures and patterns that entities share with one another. Relationships can be structural and physical, conceptual, causal, and temporal.

These entities and relationships can be further described using attributes. These are properties of both the entity and the relationship, and cannot be considered independently. Some examples of attributes are:

• Color

• Duration

• Texture

• Weight, or thickness of a line

• Type size

For each of these we mean the attribute as it applies to a specific item. Not texture in general, or the texture of paper, but the texture of a specific type of paper (or even a specific sheet of paper).

## Classifying Information

In addition to creating descriptions of our perceptions, we have also standardized a way to classify them. Common classifying schemes that we use are:

Nominal

Uses labels and names to categorize data

Ordinal

Uses numbers to order things in sequence

Ratio

A fixed relationship between one object and another using a zero value as a reference Interval

The measurable gap between two data values

Alphabetical

Uses the order of the alphabet to organize nominal data

Geographical Uses location, such as city, state, and/or country, to organize data

Topical

Organizes data by topic or subject

Task Organizes data based on processes, tasks, functions, and goals

## Audience

Organizes data by user type, such as interests, demographics, knowledge and experience levels, needs, and goals

## Social

A collaboration of organizing data by users who share the same interests, such as tagging, adding to a wiki, and creating and following Twitter feeds

## Metaphor

Organizes data based on a mental model that is familiar to the user, such as organizing computer files with folders, trash, and a recycle bin

## Organizing with Information Architecture

![](images/5279ced3d9f0e613ac2d5ec0bc73895315b4214bfb790d0af639810e3700ea80.jpg)  
Figure 2-1. Even when given pen and paper, people will make lists, so it is not surprising that lists are the most common interactive element in mobile devices. Lists can be adapted almost infinitely, for viewing or selection, for any size, and for any type of interaction.

Now that we can describe the data we perceive and knowledge types we store, we must understand how this information should be structured, organized, labeled, and identified on mobile user interfaces.

One of the most common organization structures humans have used through time is a hierarchy. A hierarchy organizes information based on divisions and parent-child relationships. When using hierarchies to organize information, Peter Morville explains rules to consider (Morville 2006): categories should be mutually exclusive to limit ambiguity. Consider the balance between breadth and depth. When determining the number of categories regarding breadth, you must consider the user’s ability to visually scan the page as well as the amount of real estate on the screen. When considering depth, limit the scope to two to three levels down. Recognize the danger of providing users with too many options.

Another way to organize information is by faceting. In this, there are no parent-child relationships, just information attributes, such as tags, which may be sorted or filtered to display the most appropriate information. The tags do not have to be explicit, and faceting may be accomplished by searching text descriptions, or even through unusual methods such as searching for shapes, patterns, or colors directly within images.

Of course, these two methods, hierarchy and faceting, may be used in conjunction. A hierarchically ordered data set can also have tags attached to it, and the facet view may combine both strict and arbitrary ordering to display the information the user wants.

Date and location are essentially special cases, and depending on the data or needs, they may be approached either way, even though they are strictly defined. For example, location can be an arbitrary value, with filtering or sorting for distance around a single point. Or it may be considered as a hierarchy of continent→nation→state→county→city→address.

## Information Design and Ordering Data

![](images/bc904bf901c3ee5ca79a3869564e15b422a393da54813dd55055092bca7634e6.jpg)

![](images/e32912429983f854069e269d20f84c2f416e8ef512d6b89d9affd090fa77bd36.jpg)

![](images/eaf51d09e1889f9e72ef4b3beb2eabbbe09ff94fafd5bc0a8a0724aad636afcc.jpg)

![](images/341fcf65c7872eaecf1d27bbded1159ca3c607cd86b706e995b80318d00b541d.jpg)  
Figure 2-2. Grids are used to display ordered data such as photos by date, or for user-organized information such as home pages, where they often become filmstrips as well. Grids can lend themselves to selection, reorganization, and even inclusion of larger items, as long as they fit in the grid.

You can use the way in which people perceive attributes to communicate the relative importance and relationship of informational elements on the page. This design of pages or states, when it falls directly from the information architecture of the entire product, can be called information design.

Although many methods of considering these arrangements exist, an adequate grouping is from most to least important. Position is generally more critical to communicating importance than size, which is more important than shape, and so on:

## Position

Although relative position is unarguably critical, it can easily be lost. The Annunciator Row, with battery level and so forth, is not the most important, because it is almost lost in the bezel. This is purposeful, and the size is adjusted to account for it. Each attribute works with others to function properly.

## Size

Larger elements attract more attention, aside from providing more room for content. They can be too big, either obscuring other items or exceeding the expectation size for an element. Buttons can be so large that they are not recognized as buttons, for example.

## Shape

At their simplest, pointed shapes attract attention. Warnings should be triangles, and helpful icons circles, for example. Rounded corners on some boxes, and square on others, will imply meaning. Make sure it’s there, and not just a random design element.

## Contrast

Contrast refers not to color, but the comparative value (darkness) between two different elements, discounting color. Contrasting elements are more easily read, less affected by lighting conditions, and not as subject to users with color deficit.

## Color

High-visibility colors attract more attention, with significant caveats. The most important caveat is not always regarding colorblind users. Glare can make certain colors less prominent. Pervasive use of the color in the branding can also be problematic; a site with a lot of red cannot rely on red for warnings.

## Form

The last thing to use is specific forms of an element. The most common is type treatments, such as bold and italics.

We will discuss these in detail in other chapters as well. Here, the concept is useful when determining how to relate the elements within a single informational item, and how to keep the elements and adjacent items from becoming mixed. Rules and bars of color are but some of the techniques. The preceding list covers six categories, with hundreds of design tactics included.

It is also useful to decide what information must be present. More can be said about a good, easy-to-understand interactive design by what is left out of any particular view, than what is included. For each of the information displays detailed in this section, only a portion is shown, and details, or alternative views, are available when the user takes action.

Naturally, make these decisions by following heuristics, standards, and styles of design that already exist, such as OS-level standards and universal hierarchies of visual communication. Most decisions for an existing platform can be easier to make by consulting the style guide. Only a few choices will exist, and these will be well understood by users.

## Patterns for Displaying Information

One good way to think about the topic of interactive design is that it’s all about displaying information. This chapter in particular is concerned with components whose sole task is to present ordered sets of information so that users may understand and act upon them.

These patterns have been developed and refined based on how the human mind processes patterns, objects, and information:

## Vertical List

Rather than using horizontal space inefficiently, this displays a set of information vertically using an entire allocated space. See Figure 2-1.

## Infinite List

This reveals small amounts of vertical information at a time because the information set is very large, and not locally stored.

## Thumbnail List

This uses a Vertical List with additional graphical information to assist in the user’s understanding of items within the data set.

## Fisheye List

When a scroll-and-select device is targeted, and a Vertical List is called for, this can be used to reveal small amounts of additional information that can assist the user in his task.

## Carousel

This displays a set of selectable images, not all of which can fit in the available space but which can be scrolled through using many methods.

Preserve the integrity of the image used. Do not use programmatic shortcuts visible to the user:

– If the image is skewed to create perspective, skew the entire image. Don’t clip off corners of the image to simulate the skew, as demonstrated in Figure 2-19.

– Do not squash the image to change its aspect ratio. If necessary, add black bars or crop the image to fit a consistent space.

– Do not flip the image when displaying the back of a card, as in three-dimensional carousels.

Never use cheats, and come up with a different display method, or switch to another pattern such as a Grid or Slideshow.

## Grid

This presents information as a set of tiles, most or all of which are unique images, for selection. See Figure 2-2.

## Film Strip

This presents a set of information, which either is a series of screen-size items or can be grouped into screens, for viewing and selection.

## Slideshow

This presents a set of images or similar pieces of information using the full screen for viewing and selection.

## Infinite Area

This displays large, complex, and/or interactive visual information that must be routinely zoomed in on so that only a portion is visible in the viewport.

## Select List

This is usually a mode of another list pattern when selections, either individual or multiple, must be made from a large, ordered data set.

## Vertical List

## Problem

You must display a set of text-based information as efficiently and simply as possible. The list is the key organization and presentation method used on all sorts of mobile devices.

## Solution

![](images/632ded85b1769280bdb1ae1b217a4474d5faf5b3637f70d3473a13c51e384cbc.jpg)  
Figure 2-3. The Vertical List simply stacks individual line items one above the other. Only a few are visible within the viewport, but many, many more may be in the data set.

Text (at least in Western languages) is what we refer to as horizontally inefficient. It greedily occupies most of its space in the horizontal axis, but also uses a lot of that space to do it, and very often uses an unpredictable amount of horizontal space. Two labels for otherwise similar items may be of very different lengths. “Joe Smith” is just as much a person as “Narin Jaroensubphayanont,” but the two labels could not be more different.

Text cannot be easily repurposed to be significantly narrower, at an angle or vertical. Vertical lists are lists of text, or text-centric lists with supporting information, such as a Thumbnail List.

A Vertical List allows inefficient use of horizontal space by permitting each item to use the entire line. The width of the list may be the entire viewport, or a portion of it. See a rudimentary example in Figure 2-3.

Items are then listed serially, using vertical space, also using either the entire viewport (minus a Fixed Menu, Annunciator Rows, the page and list Titles, etc.) or a subset of it.

## Variations

Most variations of the vertical list have notable interactive variations, so you can find them discussed as separate patterns:

• Infinite List

• Thumbnail List

• Select List

Other variations are largely in visual display options, and are far too numerous to list.

You can add additional features to vertical lists to encourage their use, or increase the efficiency of the interaction. The most common are Location Jump, Search Within, and Sort & Filter.

## Interaction details

![](images/bf1355948036ea01b1484836563f47925cc04a28c8a4d55188c8d20ada72c438.jpg)  
Figure 2-4. Details are key to making the Vertical List work. Scrolling must be smooth, information must be clear, and individual items must be well labeled.

Selection of an item in the list will perform an action, such as viewing details of the selected item.

Scrolling acceleration, even on scroll-and-select devices, should be used to allow coverage of large amounts of ground without resorting to other methods. Even if other methods are provided, the user may prefer this or may not discover them.

In a circular list, when the end of the list is reached, another scroll action will jump back to the other end of the list, or just continue without interruption. Circular lists are strongly encouraged, but dead-end lists that do not cycle back to the top may be a better choice for certain data sets, or for specific tasks. If the OS standard is for dead-end lists, be sure to provide extra features such as Location Jump to allow easy return to the top.

Whether you use a circular or a dead-end list, when the end of the list is reached, acceleration should be canceled and the list stopped or slowed dramatically, to indicate a change has occurred.

Presentation details  
![](images/ee6c5d433ec042e39e576c0a6b8da461f409c7545e29e6c2a6d3415a3c0fee8a.jpg)  
Figure 2-5. Lists, like all components, do not need to be full-screen, if there is sufficient resolution. The list component must abide by the complete requirements outlined here, including titles, scrolling, and labeling.

As with all Components, you may use the Vertical List in an area smaller than the viewport, as shown in Figure 2-5. Be sure the size of the scrolling area is clear.

You should usually align text labels to the left, to ensure that the list can be scanned. The order should be clear from the label; for example, if the list is in alphabetical order by last name, list the last name first, or use subsidiary alignment so that all last names are in a single column.

You may present additional information on a second (or third) line, as shown in Figure 2-4, but this information must be indented, smaller, and/or reduced in contrast so that the primary label line is clear.

Make sure the divisions between items are clear. You can do this by using divider lines, “greenbar” alternating colors, or simply ensuring that there is enough space between them. The text itself can often form a suitable visual block, allowing surprisingly little whitespace to yield a suitable break between lines.

Use the Location Within widget to indicate the position in the list and the total list size. Naturally, scroll bars should be represented correctly, to indicate current position and give a sense of the relative size of the list. See the Scroll pattern for more details.

A break indicator, or top-of-list label, should usually be presented at the first item in the list, to indicate circular scrolling. Especially on smaller lists, users may not understand the total size and scroll past it many times.

## Antipatterns

Many lists, such as address books, may exist for the user with almost no content, or with many thousands of items. Be sure to consider all conditions when you make your design choices, and do not just pick one case. Also, be sure to consider the look and interaction of an empty list. Should it even be presented?

Lists should scroll smoothly, pixel by pixel. Do not scroll line by line unless this is a limitation of the equipment or OS in use. It rarely is anymore, so challenge your developers, and look at the documentation yourself, if they insist on doing it this way.

Similarly, never use page scroll. When the end of the viewport is reached, the next item in the line will appear. Do not jump and load an entire page (a viewport worth) of information, with the next selectable item at the top.

Use caution in selecting background and highlight colors. Make sure all users, in all lighting conditions, can both read the text and differentiate between selected and unselected items.

## Infinite List

## Problem

You need to display a Vertical List, but the information set is very large and may not be locally stored, so retrieval time is inconveniently long.

Increasing reliance on cloud services, and the availability of Ajax-like methods on the Web, makes the Infinite List a common answer to all sorts of applications and web interfaces.

![](images/00a4be16ba30b88f341b8629d705d33024ffec45908b69766725cc294072ee82.jpg)  
Figure 2-6. The Infinite List will, ideally, load items off the screen, before the user even sees missing items or loading indicators. Lazy loading may be used on each line item in progress to make this clearer.

Use an Infinite List to retrieve and display smaller amounts of information at a time. The first displayed set will fill the viewport.

Information displayed, and interactivity with the listed items, is the same as for any other list view. You can use all the variations of the Vertical List as an Infinite List.

You should preemptively load (prefetch) information outside the viewport whenever possible, to reduce the need for the user to be aware of the fetching and to reduce button pressing, as shown in Figure 2-6. Try out the interface, perform tests, and monitor usage in production to set this to the correct level. When detectable, give priority for prefetching to the existing direction of scrolling.

You may encounter resistance for implementing an infinite scrolling list on the grounds that it makes additional data requests. Be prepared to make your points about the data being needed by the user, and do what you can to reduce needless data both for the business and in consideration of the user’s bill and device.

![](images/6c81841cb50da47070b2c5a6d179029284fc9cef94e6710953c2f06ad164c7d4.jpg)  
Figure 2-7. Predictive retrieval loads user data before the user needs it. Occasionally, the user may catch up to the end of the list, and a loading indicator will be presented.

The preferred method of interacting with the Infinite List is predictive retrieval and is largely transparent to the user. No explicit action is required to load additional information, although scrolling may be used as an implied action to retrieve information outside the viewport. To reduce network load, you will almost never try to download the entire data set.

For certain types of data, or if there are restrictions on the ability of the software to automatically act (such as browsers without full JavaScript support), the user may need to manually request additional information when the end of the displayed data set is reached. This is called explicit retrieval and is shown in Figure 2-8.

A useful subvariation of explicit retrieval is for new-only or otherwise filtered data sets (such as RSS feeds). The user must select which set of information to retrieve, not for systematic purposes but because that defines the additional information set in which the user is interested.

You can combine additional list types. You can use both the Thumbnail List and the Select List, as well as the conventional Vertical List, with the features of an Infinite List.

![](images/469a6fc5795c3ef2aeaa216d0c796c1d351de2e08f45193de52d00f778a73447.jpg)  
Figure 2-8. When the end of an explicitly loaded Infinite List is reached, a message is presented and the user must choose to load additional data.

## Interaction details

For predictive retrieval, the user takes no explicit actions to load additional information. If an error occurs, a “refresh” or “reload” button may appear, and the list will temporarily function as an explicit retrieval list. You must carefully design the number of items loaded with each retrieval (especially the first), by considering the speed with which items will be browsed by the user. You should develop rules that react to a user scrolling repeatedly in the same direction by preloading more information than usual in the direction being scrolled.

For explicit retrieval, an informational box will be displayed as the last item in the list, with details on the required behavior, and a button to allow the loading of more items. It should be clear how many more items will be loaded, or some other definition of the range of items should be used, such as “Load next day” for calendar items.

For explicit retrieval where specific filters may be applied, the available filter criteria should be provided at the end of the list. A button may be offered to show “all” information, which will then load the remainder as an Infinite List—just a bit at a time. A series of selectors may be provided to allow selection of a specific limited set of information (such as all items within the past 30 days, 60 days, one year, etc.).

Some information sets may be browsed in arbitrary order. Compare an address book with an email client. Arbitrary-access lists will require Location Jump, Search Within, and/or Sort & Filter controls to provide access to the desired information without excessive scrolling (and excessive data retrieval). In these cases, a Wait Indicator will be more commonly seen, as predictive loading cannot be smart enough for all cases. The action of jumping or searching should always load the retrieved data set, and should not require an additional step to load the items.

## Presentation details

Under absolutely ideal conditions, the operation of the Infinite List is transparent to the user, and the list appears to be a conventional Vertical List.

Practically, you cannot plan on the ideal state. If the user reaches the end of the retrieved information, a message area should become visible. Depending on the variation employed, this will be a Wait Indicator indicating that more information is being retrieved, as shown in Figure 2-7, or a selector to manually load more information. Error messages may also appear here if there were errors in retrieving the information. This informational area should be much larger than a single line item and be visually differentiated by color or style. A good practice is to have the information at the top of an area that is at least as tall as the viewport. The user can continue scrolling into the empty area, which implies that more information is available and adds to clarity when scrolling at high speeds.

Retrieve a count of the list length and display the scroll bar—or other scroll position indicators—as though the whole set has been loaded. For web pages, you can do this by loading the full number of elements needed (on a web page, the div and li elements), and ensuring that they are drawn to the right height but not populating them yet. Do not allow the scroll bar to readjust when additional content is loaded. For unlimited data sets (if scrolling decreases constraints, such as a geographical search sorted by distance), it is best to eliminate all location indicators such as the scroll bar, and to use counters and other such labels.

## Antipatterns

For all types of explicit lists, the end of the list may not be the bottom. If the user can encounter the end of the information when scrolling up, the explicit request should be at that point, above the list. Do not use a single location, or one that can be misleading.

There are almost no good design reasons to require explicit lists for arbitrarily ordered sets. Use predictive retrieval whenever it is technically feasible.

Data costs are going down, and more and more users have unlimited (or very large) data plans. Unless you know your users are on limited plans or bad networks, load much more information than they likely will need, to prevent them from running into the end of the list.

## Thumbnail List

## Problem

A Vertical List is called for, but you need to include additional graphical information to assist in the user’s understanding of the items within the data set.

Almost every technology that allows for lists can simply and reliably include images adjacent to each text label.

## Solution

![](images/b5abb81b7f888935fe6cd65a444a2cbd206d51bfd237ade9070fd9f9d816afff.jpg)  
Figure 2-9. A Thumbnail List uses images, icons, or photos, usually to the left of the text, to help define and differentiate line items.

The Thumbnail List is the simplest of concepts. You use any type of Vertical List, but in addition to text information, you add a small image, or thumbnail, next to each item, as shown in Figure 2-9.

Information displayed, and interactivity with the listed items, is the same as for any other list view. Variations of the Vertical List can be employed as a Thumbnail List.

## Variations

Although the most common use of a Thumbnail List is where the thumbnail is expected to be the key identifier, and therefore it is the leftmost item, any arrangement is possible. Instead of assuming images are most important, try to lead—by position, size, or contrast— with the key element the user will use to index the list. This key element may be text or graphics.

If any one line item has no thumbnail image, it can be loaded without any thumbnail image at all, as shown in Figure 2-10, to place additional emphasis on the data which is relevant and specific to the item.

You can combine additional list types with this. The Thumbnail List may also be a Select List and can easily be loaded as an Infinite List.

![](images/99b7bbeeb84f388a3eb96a85580318d299c4cfb5070883e53867c61ffc3d1120.jpg)  
Figure 2-10. Do not overuse placeholder icons. As shown here, gaps may be left and only actual custom images presented with an improvement in scanability and comprehension.

The addition of the thumbnail to the list items affects no real changes in the interaction from any other list type.

For lists of information such as address books, additional options may be presented on-screen or within option menus to encourage setting up more contacts with custom avatars. These options should also be presented for individual items, either within the details for the list item (or even when an item is in focus but not yet selected) or within the detail or edit view for the item in question.

Naturally, you should make the thumbnail itself selectable. This may be as a result of the entire line being selectable, or you may choose to attach a special function to the thumbnail.

Presentation details  
![](images/302acbf867589ec945d788a1f376149c13dacea68d23e0b2f00fff66492a08cf.jpg)  
Figure 2-11. Any item that can be represented by an image can be displayed as a thumbnail list. In this example, websites use their favicon as a thumbnail.

Thumbnails are commonly cropped to a common size and shape, such as square. You must place sufficient room around the image to allow it to be differentiated from those on other lines, to be seen around the bezel, and for text adjacent to it to be readable.

Consider use of borders or shadows on thumbnails, so images masked to a color similar to the background, or that are in content similar to the background image or color, can still be detected as thumbnails. Favicons, as shown properly in Figure 2-11, often fall into this trap.

When no specific thumbnail image is available, you may replace it with a default icon or other image. However, do not repeat these too often. The value of thumbnails is in their ability to be identified at a glance. Too many placeholders can ruin this function for the real, custom images.

You may pay less attention to differentiating individual line items, as the thumbnails and their spacing (especially when used as the leading item) will solve this problem.

When the thumbnail performs an action that is different from the adjacent text, make sure this is clear. Preferably, make sure it is information carried by the thumbnail itself. For example, a call history log may only list in text the number and the date. Selecting those areas would reload the call details, allowing for callback, while the thumbnail would serve as a link to the Contact list itself.

## Antipatterns

Avoid using this pattern when there are not many unique thumbnails. Address books, for example, all seem to be Thumbnail Lists now, but are very often populated mostly or entirely with the default icon. This adds no value.

Even when only a few items have a default icon, carefully consider how to treat this. Images may be eliminated, a large set of default icons may be used instead of just one, or some other semi-unique visual identifier could be loaded based on other known attributes.

Do not crop images if the image itself is the key identifier. In a list of people, the thumbnail is an icon, but if an image list is being displayed, aspect ratio and full-frame images (even if thumbnails) may be crucial to identify the correct image.

Pay as much attention to type size, color, spacing, and weight as you would with a Vertical List. Do not assume that all text is equally secondary. Some users will rely on text, the image may not be helpful, or text may help differentiate similar images.

If text is truly not helpful, do not use a Thumbnail List. Use another pattern, such as Carousel or Grid, to make the selections.

## Fisheye List

## Problem

When designing for a scroll-and-select device, and a Vertical List is called for, you discover that displaying small amounts of additional information for each line would provide additional value.

This function relies on a focus or hover state, so for mobiles it is only really applicable to scroll-and-select devices. Many application frameworks support this feature natively. Web interaction will require scripting.

## Solution

![](images/d6478a215332bc49c50b82bec8d2b25d707594c3b6f9da23cdef5fe5b52d2bc7.jpg)  
Figure 2-12. In the Fisheye List, the item in focus expands to display additional information. All other items remain at their minimized state.

In a Fisheye List, items not in focus appear exactly as they do in any other type of Vertical List.

When a list item is in focus but is not selected, it will expand vertically, as shown in Figure 2-12. This additional room will be used to display more information about the list item.

The term refers to the fisheye lens, which has severe spherical distortion. Items in the center of the viewing area are much larger than those at the edges.

## Variations

As with other list items, details of arrangement are almost unlimited, and are not considered variations in principle.

This only works with selection methods that allow focus (or hover state) separate from selection. Current touch and pen devices do not support a hover or focus state, and so cannot use this. If you need something similar for those devices, or to preserve similarity of function on several device classes, you can apply the Windowshade pattern, or a Pop-Up, to each line item instead.

Do note that hover state indication is possible on many devices with touchscreens, if they also have a five-way-pad directional control. You would have to design the list on such a device to operate in both modes. If a Fisheye List is required, one of the touch actions may need to cause different behaviors on the list.

Interaction details  
![](images/4853cb54d8be6fa111068cd2e63e15c11ca166c1aa969dfd3b29d4e69f7ea0ca.jpg)

![](images/540e96c61945aeee0ba71b256d7d959d4a454759193bb33dc99229507c97d4f6.jpg)  
Figure 2-13. As each item comes into focus, it is expanded and additional information is presented. This only works well on scroll-and-select devices, and generally one item will always be in focus, and expanded. Here, the second item is in focus, and then the user scrolls down one to make the third item in focus.

On hover (when an item is in focus), the line item will expand, pushing down all items that are below it. See Figure 2-13. The new information will not overwrite other items in the list. Any Pagination or Location Within indicators will have to take this into account, as the number of items displayed may change.

When technically feasible, you should make the line item expand by transitioning to the new size, and revealing the new information as an animation.

Selection of an expanded item may perform any action desired, as with all other lists.

Presentation details  
![](images/a0885e510a9c6b80799eca7ebfbf15230d7bd9c70a7ca36dff63fda5596b1de8.jpg)  
Figure 2-14. When the list is expanded, additional information is presented, and this doesn’t always have to be text. Here, an image of the contact uses alignment reminiscent of a Thumbnail List to expand on the information in the line. This is also one good solution for Thumbnail Lists where few of the list items have an associated image.

An expanded list item will open downward, leaving the top of the list item in the same place.

You should leave unchanged and in place most or all of the layout and content that is visible before expansion. Add additional information in the space available below this information.

Additional information should generally be of lower priority, and so in smaller type or with lower contrast. Optionally, if truncation of the original list item information is a serious problem, such as with a book title, you may make the remaining information (at the same display type) wrap to another line. Rarely, when the point of the Fisheye List is to expand key information, the design may consider expansion to be from the middle, pushing any secondary information to the bottom of the list area and using the newly expanded middle space to display the longer title.

You can also display other types of information. For example, you can expand a text-only list to include a thumbnail, as shown in Figure 2-14, either because not all information has images or to provide for larger thumbnails than would otherwise be practical to display. An address book can expand to include call record information, for instance.

You should use care to ensure that the size of the expanded list item is clear and does not appear to be two items, or becomes confused with other list items.

## Antipatterns

Images, when used as a Thumbnail List, should generally not expand or change size. This throws off the alignment of text and reduces the amount of text that is visible, significantly reducing the user’s understanding of the state change and slowing her responses.

Do not confuse this pattern with others, such as Pop-Up. The expanded state pushes following items down the page, and never overlaps them.

Whenever possible, provide transition animations. Avoid jumping to the open state, and never refresh the entire screen. Users will not see the relationship between the two states and the value of the pattern will become lost. If you cannot do this for technical reasons, use another pattern.

## Carousel

## Problem

You need to present a set of information, most or all of which comprises unique images, for selection.

Carousels are graphically intensive, so they may not be easy to implement on devices without built-in support. Web implementations will need scripting or advanced HTML and CSS support.

## Solution

![](images/d816860c9620f243b42a50efe7e295958de9844a6686961183f1c7d1b94a1a14.jpg)  
Figure 2-15. Carousels may be laid out as actual circles, with much of the array visible to the user. Use of perspective and other 3D or simulated 3D effects assists with this.

A Carousel displays a set of selectable images, not all of which can fit in the available space. It simulates a continuous strip, stack, pile, or other arrangement of images, as exemplified in Figure 2-15, only some of which can be seen at once due to the limited size of the device’s viewport.

The images presented should be similar in size and aspect ratio. You can include a small amount of additional information about each image that can be displayed adjacent to the image as it comes into focus. In general, the in-focus item is larger, clearly has focus or actions attached to it, and so on.

The user can scroll through the set via any number of methods. Indicators should be present, but may not be based on OS standards. Scrolling brings more things in from the sides (or wherever), and changes the item in focus—it must always be live so that the items move instead of appearing in the middle of the page, or jumping from one position to the next.

Do not confuse this with a Slideshow, which only presents one image at a time, full-screen. The two are closely related, and users often switch between them within a single interaction. If you cannot implement a Carousel for technical reasons, use a Slideshow instead, or in combination with a simpler display method such as a Grid or Thumbnail List.

Variations  
![](images/1657a4dee9f3cf79289719e44922857a0c1964005acc0238f7d0a7b6b8675c01.jpg)

![](images/6cc0f26d08b90246886489719e52ca86a09874db15bd29504c1994a003ab7fa4.jpg)  
Figure 2-16. Vertical or horizontal arrangements may be used, depending on the type of data and the principles upon which the device OS already operates, and sometimes simply on the amount of space available.

You can design a Carousel to be presented either vertically or horizontally, as shown in Figure 2-16. Which design to use depends on the space available in the layout, device display or interaction paradigms, the nature of the items being displayed, OS conventions, and user expectation. Sometimes you may even wish to switch within a single implementation, due to device orientation changes.

Two-dimensional carousels use size differences to create a simple but false sense of perspective. Two-dimensional carousels may slightly overlap the items that are not in focus, to save space. Images should always be identifiable from the partially exposed image.

Three-dimensional carousels usually make the entire circle of the collection visible by using perspective. When oriented horizontally, the back of the circle is tipped toward the viewer. And contrary to the physical metaphor, the items along the back edge of the display are shown as though the image is on the back of the card, or as though the image is two-sided. Presenting the back of the image doesn’t seem to work.

Note that three-dimensional carousels can present a more engaging interface, but you can rapidly run into issues with density and complexity of information. They tend to be more expensive in terms of screen real estate for the display and in processing needed for any image conversion or animation.

![](images/d1261b457a3d97eae49f746df3fb1e0c6b7ac5b361e6ebc54e97787d5548b84e.jpg)  
Figure 2-17. The graphical nature of Carousels limits effect and actual on-screen space. Information and options will often need to be presented in informational bubbles, or as option menu items.

The item in the front-middle of the Carousel is the item in focus. You will make this item subject to the conventional interaction criteria for any in-focus item. For example, when the user makes menu selections, as in Figure 2-17, or presses the OK/Enter key, the actions will affect this item.

For touch or pen devices, any visible image may be selected. You may choose whether the result of selecting an image not in focus is to bring it into focus, or to immediately carry out a selection action. This is dependent on the context and process in which the carousel is being used.

Scrolling may be by gesture, directional keys, or selection of scroll functions on the screen. Scrolling must always be “live” or show the items moving on the screen. If this cannot be done, do not use the pattern and select another method. Be sure to support multiple methods so that touchscreen devices with directional pads work with all input devices.

You can identify position in the list with a conventional Pagination or other type of Position Within widget. The total number of items should be easily obtainable or shown, but other features of these widgets may not apply to the particular data set or presentation.

If it makes sense for your information set, a Location Jump widget may be applied. For example, a photo gallery may use this to avoid putting images in folders, and allow jumping to dates that the images were taken instead.

In many cases, the action on first selecting an image in the Carousel is to display it fullscreen, for a better look. You should always switch to a Slideshow at this point, and not require the user to go back to the carousel to select another image. The user may want to compare several images to select one for sending or deletion. Do not make anything difficult by excessively sticking to a specific interaction paradigm.

Presentation details  
![](images/9484a475651f4a93b04d8a5f0b64945553e2258f4a3bc434c3de5297684d1e87.jpg)  
Figure 2-18. Use all effects correctly, throughout the experience. Skewed images work well for presenting Carousels, but can be demanding to processors.

The item in focus is centered in the screen (or in the array, if the array is off-center for dimensional simulation). You should also indicate this by size, by adding a border, or with other indicators. A common addition is the inclusion of text labels, such as the name, to only the item in focus.

Images not in focus should have attributes other than position to indicate they are in a secondary position in the list. Size and angle (skew to simulate not-facing) are the most used. See Figure 2-18 for a simple example.

The last image that is not in focus but is visible should imply that there are additional images outside the viewport. This may be via size (shrinking to infinity), via angle (tilting “up” to become perfectly thin), or by having part of the image not on the screen. Each of these should lead users to believe there is additional information if they scroll.

You should use additional scroll indicators whenever you can. Simply add arrow/triangle indicators to the sides, or immediately to either side of the labels for the item in focus. If they are selectable directly, the indicators should change when they are selected and while the carousel is moving to indicate their activity.

## Antipatterns

![](images/30174dd92c606252e88c325c948509e264591e5d1610a16e39e8139f8e03eb2a.jpg)  
Figure 2-19. Skew images correctly. Do not just crop flat images to a skewed shape; users can tell the difference.

Preserve the integrity of the image used. Do not use programmatic shortcuts visible to the user:

• If the image is skewed to create perspective, skew the entire image. Don’t clip off corners of the image to simulate the skew, as demonstrated in Figure 2-19.

• Do not squish the image to change its aspect ratio. If necessary, add black bars or crop the image to fit a consistent space.

• Do not flip the image when displaying the back of a card, as in three-dimensional carousels.

Never use cheats, and come up with a different display method, or switch to another pattern such as a Grid or Slideshow.

## Grid

## Problem

You must present a set of information, most or all of which comprises unique images, for selection.

A Grid display does not require unusual or special conditions in order to be implemented. It may be easily used for applications or websites on any device that can display the images adequately.

## Solution

![](images/0f2d4de2ca9140d8a06d89c3050161b7210771a00faf238d0ea7c513ef3d3f31.jpg)  
Figure 2-20. Items may be displayed as a grid of images, with little or no text associated with each one.

A Grid displays a set of selectable images, not all of which can fit in the available space. It simulates a continuous array of images, only some of which can be seen at once due to the limited size of the device’s viewport.

The images presented should be similar in size and aspect ratio. You can display a small amount of additional information about each image as it comes into focus. The in-focus item will be indicated in some way, but does not change size.

The user can scroll through the set via any number of methods. Indicators should be present whenever acceptable to the OS standards. Scrolling brings more images in from the sides, and changes the item in focus. You must always use live scrolling, so the items move as part of the continuous list, instead of incongruously appearing in the middle of the page, or jumping from one position to the next.

Variations

![](images/665f12bfb68533c469fec84dde34f742a53afef44dd48e009194c4974cf725ab.jpg)  
Figure 2-21. Items in focus should clearly be indicated as such, and should display text labels such as titles and dates.

You should only use a Grid when one axis of movement works well for the display and organization of your information. This one axis can be either vertical (Figure 2-23) or horizontal. Two-dimensional grids will generally scroll in the longest direction of the viewport, regardless of orientation. No movement should be allowed in the short direction.

All Grids simulate an array of images on a flat surface, such as a desktop. See Figure 2-20. But they do not have to do so literally; the backdrop may be anything, or a solid color. Today it is common to use the conventional backdrop image, which indicates that the images in the Grid are floating above a relatively distant surface.

Some 3D effects may be used, especially with accelerometer-equipped devices, as loading or scrolling animations, to allow viewing more images by tilting and so forth. See Figure 2-24.

A rare alternative type of Grid arranges the thumbnail images as though on a sheet or globe, allowing scrolling in any direction. This may be useful for emphasizing certain types of data relationships between images in the grid. This is very similar to the Infinite Area pattern, but the individual thumbnails align it more closely to the Grid.

Interaction details  
![](images/b5a887e5e6d28ecb46c59c559fe892708db2c9c31a467d607ba103a85080994c.jpg)  
Figure 2-22. Grid items may have additional effects applied when in focus, such as zooming slightly to display the image in more detail.

Any visible item may be selected. Selection may result in any of a number of actions; you may display additional information, or perform drilldown methods such as a Pop-Up, a Slideshow, or simply displaying a new page of information.

If your information set can be applied to it well (such as for all images photographed on a certain day), a Location Jump widget may be useful.

You may offer scrolling by On-screen Gestures, Directional Entry keys, or selection of scroll functions directly on the screen. Scrolling must always be “live,” or show the items moving on the screen pixel by pixel as the movement is made. If you cannot implement this due to technical constraints, do not use the pattern and select another method instead.

For most data sets, scrolling should be circular, where scrolling past the end of the grid will load the next end of the grid. This prevents the user from having to scroll large distances in many cases.

Array items so that lines are read in the short direction, and then jump to the opposite end on the next line. For example, for a photo album with a grid scrolling horizontally, the newest item is in the top-left corner. The next-oldest is below it, and so on to the end of that column. The next-oldest item is at the top of the next column to the right.

Presentation details  
![](images/e6e1654b9f716d7f3cb974ddebdfaabef29bc4ea51de321a3fe2dc4bf03eb11f.jpg)  
Figure 2-23. Grids may also be displayed vertically.

Position in the list should be indicated with a conventional Pagination or Location Within widget. The total number of items should be easily obtainable or shown, but other features of the Pagination widget may not apply to the particular data set or presentation.

The item in focus must be indicated, as shown in Figure 2-22 and detailed in the Focus & Cursors pattern. The in-focus item may display additional information, such as labels, or metadata. This may be presented below the image, or in another area reserved for this information, such as a bar across the bottom of the entire image area. This is a good place to use a Tooltip or Annotation, as shown in Figure 2-21, to hold this information. A small Pop-Up dialog may also serve this need, and may be easier to implement.

For pen and touch devices, without explicit in-focus or hover states, the focus paradigm is usually eliminated and no attempt is made to simulate it. This is exactly the same as it is with position in the Carousel pattern. However, be sure to support scroll-and-select actions for devices that have Directional Entry controls, even if they are secondary to a touchscreen.

For circular scrolling grids, a gap or other indicator should be displayed to mark the start and end of the grid. This may be as large as the viewport, so a very deliberate scrolling action is required in order to scroll to the other end of the grid.

![](images/6f9077951d6a620e68084dece4f66e36009c7c03f901bda08514e18b5d12774e.jpg)  
Figure 2-24. Effects may also be applied to the entire grid. Tilt effects such as this may also be coupled with sensors, and related to the tilt angle of the device

Images at the end of the viewport, along the scrolling axis, should imply that there are additional images outside the viewport by being cropped and not fitting entirely within the viewport. This is to lead the user to believe there is additional information if she scrolls; if she just tries to scroll enough to see the rest of the image, she will also become aware of additional images.

Additional Scroll indicators are strongly encouraged. Simple arrow/triangle indicators to the sides, or immediately to either side of labels for the item in focus, are common. If they are selectable directly, the indicators should change when selected and while the carousel is moving to indicate their activity. Scroll bars or other such indicators may or may not work depending on the design of the page.

## Antipatterns

Use caution when choosing the selection action. Do not make it too difficult to do alternative tasks, such as clicking on adjacent items or functions attached to the image, by making a single selection task too easy.

Avoid making the display overly complex. Despite the information density of the grid, a conventional one-axis scrolling grid is easy to control. Two-dimensional (spherical) grids present challenging mental models, and may be difficult to control.

Only use the Grid display if there is sufficient room and resolution for the thumbnail images to be viewed. If the screen is too small or is of insufficient resolution, use another solution instead, such as a Slideshow.

If live scrolling is not available, avoid using this pattern. Jumping screens or refreshing will not present the items—or their relationship to one another as a set—as clearly to the user.

Be sure to provide plenty of space between images. Do not butt them against one another, as it is difficult to discern individual images when they are similar in content. Also try to account for common OS elements such as the Annunciator Row, and the Fixed Menu.

## Film Strip

## Problem

You must present a set of information, which either is a series of screen-size items or can be grouped into screens, for viewing and selection.

Several mobile OSes and programming platforms support the Film Strip directly. It can be simulated effectively on many others. It may be difficult to use this in certain platforms, such as within web pages, due to scrolling conditions.

![](images/b1676818e6aa5253c818a01685090e748b654dabe2391dd7188d00ec2b878dbd.jpg)  
Figure 2-25. When any one panel in a Film Strip is in focus, it is presented full-screen. In this condition, it cannot be differentiated from a slideshow.

As with many of these terms and concepts, the filmstrip is a real machine-era display device, a sort of cheaper way to display a slideshow. Instead of the slide film being cut up and placed into slides, however, the film was kept on a continuous roll and fed into a very simple machine that displayed an area as large as one exposed frame. The transition was not hidden but out in plain sight for all viewers to see. One frame slides up while another takes its place, separated by a small gap. Clever presentations embraced this paradigm and had images span the frames, or discussed processes as continuous vertical flows, with arrows leading from one frame to the next.

In mobile devices, a Film Strip is similarly a series of screens, displayed as a continuous strip, with small spaces or markers between them. When a particular screen is centered it fills the entire viewport. During a scroll, part of two screens and the divider can be seen at the same time.

For viewing individual items, such as images, you may fit the entire image to the viewport. For collections or groups of information such as articles, lists, or groups of icons, the individual screen may also scroll up and down.

## Variations

The Film Strip is used in two distinctly different ways.

When displaying full-frame items, such as images, this essentially is a Slideshow where the relationship between images is more clearly defined. You might find this to be helpful to your users when transitioning to this view from a Carousel or other list, where the relationship was explicitly stated.

When displaying complex items, such as a grid of icons or a page of text content, the individual frames are considered pages, either in a process or in a display of equal information. A common use is for a multipage Home & Idle Screen, as shown in Figure 2-26. The basic interaction of pages sliding in from the side may also form the basic interaction paradigm for the entire application or OS.

Rarely, you may wish to implement the Film Strip as a large grid, with scrolling between frames in both axes, or possibly even at angles. The full-screen nature of the individual panes makes this different from the rare version of the Grid or Infinite Area pattern.

Interaction details  
![](images/5670a51e84e005581ab904938dafbbb464eaede69136bafc086b56b8e192d18b.jpg)  
Figure 2-26. When scrolling or dragging from one frame to another, a gap between frames will be displayed. Shadows or some other effects should be used to make the distinction between frames clear.

When you use the Film Strip to display full-screen content, such as images in a Slideshow, only allow scrolling to reveal more images. Scrolling is most effective when performed side to side, or horizontal to the ground. This means you have to account for Orientation changes and make the display and interaction work in both portrait and landscape modes.

If you use the Film Strip to display complex, page-level information, the pages do not need to be restricted to the size of the viewport. Scrolling sideways via touch or with hardware Directional Entry keys will perform the usual action to reveal a new page, but conventional vertical Scroll may also be used within the page currently in focus. This is explained with gesture scroll in Figure 2-25.

Other methods of accessing the adjacent pages, such as clicking on a Link to reveal it, can be designed to look and feel related but are outside the scope of this pattern.

Scrolling must always be “live,” or show the items moving on the screen. If you cannot do this for technical reasons, the point of the pattern will be lost. Users will not understand the relationship between the frames. Do not use the pattern and select another method.

When designing for scroll-and-select devices, or touch devices with hardware Directional Entry keys, make a single click load the entire next frame, by animating a sideways slide. For gestural scrolling, enable dragging so that when the frame divider is about halfway across the screen, it will “snap” to the frame in the gestured direction. If the user’s touch input is stopped at this point, the next frame will slide into view anyway. Any movements that are smaller than this will revert back to the starting frame. For all of these, including snapping back to the starting point, the action should be animated.

For full-frame displays, such as Slideshows, include acceleration or key repeat functions to allow the user to scroll across several frames quickly. This should work for both touch and scroll-and-select devices. Unlike high-speed scroll through Vertical Lists, at each frame in a Film Strip, the scroll should pause for a fraction of a second. The time to transition may be greatly increased.

When not suppressed for full-screen display, the Annunciator Row should be fixed to the viewport and should not scroll.

When on any single screen or page, you can use conventional design elements, including scroll bars, Titles and Fixed Menus, or Revealable Menus. Or you may hide these if the frame is a full-page display and they are not appropriate. When the scrolling action is taking place, these items should generally be suppressed, to prevent users from becoming confused as to what is a selectable item.

For certain types of data, or certain interaction models on the device (e.g., especially scroll and-select devices), you will want to add Pagination. This may be visible at all times, made to be visible via an option, or made to be visible only when scroll has otherwise been initiated. Unlike the other widgets, Pagination is generally available during the scroll actions.

Circular scrolling is encouraged when practical, but may not apply to certain types of data. It may be important, for example, if you have a list of date-ordered information that has a distinct starting point, and proceeds from there.

## Presentation details

![](images/e96fad49e7533f0568756e304c7d2aaf5f6feab7c91d57899f18a79cdb38471e.jpg)  
Figure 2-27. When scrolling, the panels are drawn at full resolution, but only part of each one is visible.

You must make a clear delineation between the individual frames. The best solution is to display a gap, as though each frame is a physical object, floating above another surface, as in Figure 2-27. If this is not practical, you can sometimes get by with divider lines, or by creating a “gutter” from the margins along the edge of each frame. Without some indication of the edge, the relationship between elements while moving may not be clear.

A Location Within widget should be displayed if there is no Pagination widget as described earlier. Depending on the type of data used, this may be visible only when scrolling, or at all times.

When on any single screen or page, you should follow conventional design methods for page design, and include common elements such as Titles.

## Antipatterns

Do not allow horizontal scrolling within a single panel of the filmstrip. For example, if you are displaying a list of images, zooming in must disable the ability to scroll between frames, or must not be allowed. Without this, it will be unclear where the edge of the scrolling within the image is, and users will unexpectedly jump, losing their place.

Make sure each vertically scrolling area is entirely independent. Scrolling to the bottom of a page and then moving to the right will load the top of that page.

If live scrolling (animating the transition between screens) cannot be implemented for technical reasons, the pattern being used is not a Film Strip.

## Slideshow

## Problem

You have a set of images, or similar pieces of graphical information, which must be viewed in detail.

Large-area display of graphics is easy and common, though there may be limits to the ability of some platforms such as web pages to display these at truly full-screen.

## Solution

![](images/142fb318e59928831b503210e5fd12b1b39d74c7e86d5ba7f5d2ebd628dfefab.jpg)  
Figure 2-28. In most modes of a Slideshow, there is nothing to see but the content, which is presented full-frame, with no scroll bars or labels.

The core of the Slideshow is that each image is presented full-screen, as boringly shown in Figure 2-28, with a function to transition to the previous or next image in the series.

You will find this very often used exactly as its namesake, the slideshow. Much like presenting a series of vacation photos in the past, this allows the user a way to view a series of photos or other images. It can also be used to view other types of information summaries, such as consolidated sports scores.

Transitions between slides may be of any type, such as a cross-fade. This makes the Slideshow suitable for most devices, which may have technical difficulties with other types of patterns. If the images presented as though the images are on a continuous strip, this pattern becomes the Film Strip instead.

Do not confuse this with a Carousel, which presents all images in a continuous and visible series. The two are closely related, and users can often switch between them within a single interaction.

## Variations

Variability in Slideshows really concerns only the degree of control that may be imparted to each slide. Some will be simple viewers, and no individual control is available. Some will allow, for example, editing of the images. Controls may be presented on-screen, or under option menus.

## Interaction details

You should make sure the ability to switch between slides complies with the application or OS standards surrounding it. Gesture, directional keys, or selection of “Next” and “Back” functions on the screen are all suitable.

For image slideshows and some other types of data, additional options should be available, such as randomization, or ordering by various types of information. These may, of course, be available only under menus.

For certain types of data, or certain interaction models on the device (e.g., especially scroll-and-select devices), you will want to include a Pagination widget to allow the user to jump to specific locations in the list. This may be visible at all times, made to be visible via an option, or made to be visible only when scroll has otherwise been initiated.

A Revealable Menu should be made available via the expected (or an easy-to-discover) method such as that shown in Figure 2-29, to offer additional information or functions for the entire slideshow, or for individual slides. Even if the OS paradigm is for a Fixed Menu, the menu should be hidden by default to grant as much space in the viewport as possible to the slide information.

Circular scrolling is encouraged, but may not apply to certain types of data. For example, it may be important with date-ordered information that the set have a distinct starting point and proceeds from there.

Presentation details  
![](images/2f853b720a47db4f4fd02f8274d43fe80019df6d4ac9472b6cadaf8cf584f43b.jpg)  
Figure 2-29. If needed, or in certain conditions, information about the image should be presented on the screen. Soft keys or soft-key-like indicators may also be shown on the screen to allow access to the option menus.

The amount of extraneous information presented depends on the intended use of the slide information. Pure slideshows will specifically have no text, icons, or other items on the screen. You may even wish to suppress most or all of the Annunciator Row. This will become especially important as more devices have high-quality video-out capabilities, and mobile devices may be used as the source for large, projected presentations.

Design supporting information, such as filename, dates, and the links to options, should be nonintrusive and should obscure as little of the slide image as possible. Although specific implementations will vary based on user needs, you may find it useful to restrict the information presentation to when some selection is made (such as a tap on the screen) or after a pause of several seconds on a single image.

OS-level Notifications should usually be hidden by default, to give as much space in the viewport as possible to the slide image. When other information is presented (such as option menus, or image metadata) these may be presented also, in their normal location and style.

If any additional information is presented as an on-screen overlay, a Location Within widget should be employed.

## Antipatterns

Slideshows are not suitable for significant interaction with items within the individual slide. Although charts, graphs, text, or tabular data can be displayed as a slide, you will find that allowing selection of a single component, such as a link from part of the data, is not easy with the slideshow. If this is required, use another pattern, such as Film Strip for interacting with individual screens, or Infinite Area for interacting with arbitrarily large sets of graphical data.

You must take care to find the correct balance between information presentation and clutter. When you start to add all the useful controls, metadata, and indicators of position, you will rapidly run out of space and begin obscuring the image displayed. Consider the use of the product and the users. Push less-used items that have to be retained into option menus.

Do not develop new types of OS-level displays in order to save space. If battery level, notifications, and so forth are possibly important information within the Slideshow, use the normal icons from the Annunciator Row and hide the rest, or hide everything that is noncritical, to save space and avoid distracting the user.

## Infinite Area

## Problem

You have complex and/or interactive visual information, which should be presented as a single image, but is so large it must be routinely zoomed into so that only a portion is routinely visible in the viewport.

Infinite Area is best used with information considered actually infinite, such as maps of the whole world, and therefore usually requires a reliable data connection or very large local data capacity. The dynamic loading and reloading is difficult to implement or not supported by all platforms, such as some older web browsers.

Solution

![](images/53e2521affd9c29ef0fd334b230fb085ba02f97f9b1d2692373969a5cfb263ae.jpg)  
Figure 2-30. Infinite areas break up the visible regions into rectangles of graphical data. When they are first loaded, or when the user scrolls too far, the user may briefly see lazy loading indicators, where data has not yet loaded.

As we already mentioned, maps are the most common implementation of this, but there is no reason other information sets cannot borrow from it, and some demonstration projects already have used similar technology. You may find this to be a good way to display other photographic information (using very high-resolution, composite images) or to allow users to drill into complex infographics.

The entire breadth of the data set is generally available at every zoom level. Scrolling reveals more of the information. Zoom instead can be considered the depth of the data.

Whatever you are loading, the entire data set is considered to be a large, two-dimensional graphic, though these are generally actually broken into frames, as shown in Figure 2-30. Smaller subsets can be viewed as though “zoomed in” to portions of the larger image. Zooming reveals more information, generally with newly rendered images, which reveal additional layers of information. On a map, at the city level, you only see highways labeled, and street names only appear when they would be clearly useful and not clutter-inducing.

## Variations

A key variation is to provide only two-dimensional scrolling of the data set, as shown in Figure 2-32. Consider a large graph of historical information, such as stock prices or key moments in history. At the far right is the current date, with past dates going off to the left, far off the screen. You can provide scales as well as all other controls to both pan and zoom in for further detail.

Two information-anchoring paradigms are also available. These may be encountered in the same application, and vary based on the immediate user task. However, they are different cases, so you should be aware which one you are using so that you can address them distinctly in design.

• In the first case, live data uses a real-world anchor point—or a simulated one, based on reviewing historical data; for example, the current position of the device, or the current time. As this changes, the data set moves to keep this dynamic point centered. Maps in navigation mode, keeping the current position centered as the map moves about it, are a typical example.

• In the second case, a fixed point or range is selected by the user and information is browsed around this point; for example, restaurants within 50 miles of a specific point (not where they are currently located), or a date range for historical graphs. Zooming of the data to fit the range selected, and other design features, will accompany this sort of behavior.

Don’t be limited to the existing examples. You can also use predictive data, where rangelimited data is presented for predicted future tracks, such as restaurants you will be passing on a planned route, or expected trends for other types of information.

The Infinite Area pattern, especially the two-dimensional version, can work well as a subset of a page, and does not need to take up the entire viewport. This makes it easier to implement on platforms that do not allow taking over the full screen.

Interaction details  
![](images/879ad1b0d2a84ac57591963b7d2185e41ab52f5b707565cc049bebc77a6627b4.jpg)  
Figure 2-31. Graphical data representing the real world, such as the map shown here, is very commonly used as an Infinite Area.

You should, as with all of these Display of Information patterns, support scrolling with all the methods available on the device. In addition to the built-in gesture support or hardware keys, you might find it helpful to add on-screen buttons or other controls.

Zoom controls should be on the screen, or easily accessed. Zoom by gestures (e.g., pinch and unpinch) may not be discoverable, even if it is via a standard OS control, so an explicit backup to zoom control should be available.

Layers will be automatically controlled by the system to provide details as the user zooms. You can also offer optional layers, such as satellite versus map views, to the user as explicit controls. Optional methods of viewing data should be offered whenever they assist in understanding the data set. This can include manual control of the automatic layers, such as the ability to turn on and off road names at different zoom levels. You will have to design the system for the typical case, but not all data is typical, so user control can be helpful. In rural Kansas, roads are very far apart, and names can be useful at small scales; in downtown Boston (where every alley is named), even at maximum zoom it can be hard to see anything but the road names.

A key value of this pattern, or any information visualization like this, is that items within the data set may be selected and acted upon. For certain data sets, any point can be selected and actions taken. For a map, any point can display attributes, be saved as a favorite, and offer directions. You can offer such actions from option menus, or from more directly interactive features such as Annotations, as shown in Figure 2-31.

Presentation details  
![](images/a23560398396ff31b5a00e0edbd7e65c721902aa404981c9e2f5045894b70081.jpg)  
Figure 2-32. Two-dimensional infinite areas apply to things such as charts and graphs. A single axis, such as time, is effectively infinite, and the other axis is of a very limited scale. Any infinite area may also be a subcomponent of a page, instead of a full page.

Even if they are not used much, you may find that the presence of on-screen controls for zoom, scroll, and other functions is a great help in communicating to users that these functions exist. For complex interactive items, you should always consider the impact a visible control has, not just on the actual interaction, but on the perception of that interaction, and the indirect affordance, or communication, that an interaction is available.

In most view states—zoomed in to a portion of the image—user scrolling will require loading additional image data. These images are generally stored and loaded as panels, though when loaded the edges are seamless. You should always load at least one set of panels beyond the current viewport. When you can, develop simple predictive algorithms (based on scroll actions and other likely behaviors) to load additional panels in the direction the user is likely to scroll.

Panels that have not yet been loaded should display either a scaled (blurry) version of their previous zoom level or an explicit Wait Indicator.

You may receive great pressure from many sides to reduce prefetching as inducing too much overhead in data, processing, and so forth. Aside from arguments about making a compelling product, a well-designed system can, by the use of smaller-than-screen tiles, manage to use less data than a simple (but uninteresting) method of forcing the user to manually load the next whole panel. These require, among other things, overlaps in order to not let the user get lost, so pixels are loaded twice. Good Infinite Area design can be very data-efficient, and very engaging to the user.

Consider using 3D and other effects whenever it can add to the comprehension of the data. Tilting, or simulating elevation, may allow viewing relationships that are not clear in other ways (and not just for maps).

Scale must be indicated in some manner. This may be explicit, as marks for miles, but implied scale should also be used. For example, at close ranges on maps, roads can be depicted as actual width, and buildings can become visible. See the Zoom & Scale pattern for much discussion of this.

Decluttering is the process of determining how many layers of detail should be displayed for a particular zoom level. This includes not just the number of items, but how much detail is on a layer; a line on a graph, or a road, can be simplified to reduce the number of points drawn. The goal of decluttering is to provide as much relevant detail as possible without reducing readability and legibility.

## Antipatterns

Use caution with clutter control methods. If you declutter too much, you may remove so much information that the data set is not valuable; too little and no information can be read. To add to the difficulty, portions of the data set may have more information, and single rules may not apply. For example, a declutter factor for a suburb works less well in a dense city.

Scrolling must be live. Do not refresh the entire page. When using scroll-and-select devices, or nongestural scroll controls, still show the data set moving from one part of focus to the other. Do not jump.

For maps, do not confuse GPS with “location.” Many methods of finding location are available, and map applications should be available on devices without GPS, as well as on suitably equipped devices in which it is off, or cannot get a signal.

Do not assume all users will understand gestures, even those common to the OS. It may not be clear which methods apply to the particular application or element. Back this up with explicit controls, even if they are hidden in option menus.

Avoid the use of special effects, such as simulated 3D, that may cause data to be misrepresented or misperceived. Follow good infographics practices, such as those promulgated by Edward Tufte in his many books, lectures, and reports.

## Select List

## Problem

You must allow the user to make a selection—or several of them—from any of the large, ordered data sets discussed in this chapter.

The applications of this are essentially limitless, and can be applied to the simplest and the most complex of representations, and so can be used in one way or another for any type of implementation.

## Solution

![](images/16bc644fc0c9e9d51a83ab2ec7c552802f31308906c16d1cc728988c434712aa.jpg)  
Figure 2-33. The select list that is the most common and simplest to understand is the Vertical List, with selection checkboxes for each line item.

You can turn any of the other patterns within this chapter, but especially the Vertical List, shown in Figure 2-33, and the Grid, shown in Figure 2-34, into a selection mechanism by simply adding a checkbox or some other explicit and visible selection component.

For many selection methods, simply tapping or pressing the OK/Enter key on hover will serve to meet the needs of single selection. The checkbox pattern is used for multiple selections (more than one item may be checked) or when the selection may involve investigation and confirmation before committing to the selection.

## Variations

There are two variations to the select list. Single-select only allows one item to be selected, and then forbids subsequent selection, or deselects previous selections.

Multiselect allows you to check more than one item in the set. The limit is set by the application, or the requesting application, or may include the entire set.

Many select lists allow switching between these modes. This is useful when you cannot predict how many selections need to be made, but a typical number is just one, such as for selecting recipients of an email.

## Interaction details

![](images/2c66a000f548f5c48ed44d85a2ea79f8b690ddbb5181c548ef76b70ec501b104.jpg)  
Figure 2-34. You can make other methods of displaying large amounts of distinct data, such as grids, into select lists by simply adding selection mechanisms. A good use of this is to switch from a viewing mode to a selection mode, such as choosing photos from a gallery.

The Select List pattern is likely to be implemented as a mode of another list. This mode may be entered contextually, due to a request from another application, or explicitly via user action within the list view. Very often, you will be reusing a list that already exists for another purpose. Any type of list may be used, including highly graphical ones such as the Carousel, as shown in Figure 2-35.

Most single-select lists perform the selection and commitment of the selection as one action. Once the item is selected, you should take the user to the next step in the process without forcing him to select a Next button.

For multiselect lists, when the user selects an item, the indicator will change immediately. When the selection method is made again, the indicator will change to the deselected state. If details are available for an item, such as viewing an image or selecting it, the checkbox should have to be hit with some precision, and all other areas may result in viewing details.

Depending on the function, a “select all” may be necessary. Even if functions against all items can already be performed with a dedicated function (e.g., a “Delete All” option menu item, separate from a Select to Delete function), it can be useful for alternative selection modes. The user may want to select most items, and shorten the time required to do so by selecting all of them and then deselecting the few items he wants to keep.

For all multiselect methods, you will have to provide a “Done” function to determine when to move to the next step. This should be contextual, and should carry a label associated with the larger task—”Delete selected items,” “Send message to selected recipients,” and so on.

Especially for large data sets, the selection process may be involved, so you should “consider” it as a set of user-entered data. If the list is exited before commitment—such as if the “Back” button is selected by accident—you should preserve the selection information. The exit may have been accidental, and when next carrying out the same task (e.g., adding recipients to that same draft message), presenting the last selections instead of an empty selection state may be perceived as helpful. This concept is discussed further in the Cancel Protection pattern.

Since some uses of the “Back” button are deliberate, do not force the user to accept previous selections. See the Clear Entry pattern for some methods of removing user-entered data without placing undue burden on the interface.

Presentation details  
![](images/3fcb8a76fbbc53beea1a66a84599278fbbd2cedcb6ed61afe2e48e685ab4bcd1.jpg)  
Figure 2-35. Selection types where there is a strong difference between the in-focus and out-of-focus states, such as the Carousel shown here, should only allow selection when in focus. The selection condition should be displayed for all visible items.

Selector items should be overlaid on the list items. Within a grid view, for example, the checkbox should be over the image itself, or otherwise not take space from the interface. You will also enjoy doing this, as it reduces the changes needed to make a Select List variant of your existing lists or views.

A variation of the Location Within widget may be employed to indicate the number of selections. This is especially valuable when there is an easily reached limit on the number of selections. You may also choose to use this conditionally; when the selection limit is high, the indicator can appear only as the limit is approached.

To prevent errors, commitment of the selections should be prevented until at least one selection is made. You can do this by hiding or by graying out the relevant functions. You should always try to reduce explicit errors by making them impossible to reach.

## Antipatterns

Do not overthink the selector or indicator. Checkboxes work well. Radio buttons may seem to be the best choice for single-select items, but the web form paradigm is not well understood by many users. Novices are very common on mobile devices. Use checkboxes or similar-looking interactive elements for all selections.

Don’t let checkbox styling get out of hand. The selected and unselected states should be not just differentiable, but identifiable without comparison, to all users regardless of their vision, and in all lighting conditions.

Do not impose burdensome errors. If the user must be forbidden from making another selection, simply disallow the user from doing so. If a message is required, place it prominently, but away from the focus, and do not make it a dismissal-required modal dialog box.

Be sure the selection method is well associated with the item being selected. Do not place checkboxes by floating metadata, for example, but on the image itself.

Always show selection state, even when the item cannot be selected. If a Carousel is used as a Select List (and it generally should not be), only the item in focus can be checked. However, make sure to show the checkbox for all items in view.