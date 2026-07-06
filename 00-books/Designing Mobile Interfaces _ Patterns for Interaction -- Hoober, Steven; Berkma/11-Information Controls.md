# Information Controls

## The Weilers, Version 1

Jack, Maggie, and their 5-year-old, Melissa, approach the entrance to the brand-new shopping mall that recently opened in their hometown. Melissa, thrilled with the opportunity to finally go to a Build-A-Bear Workshop, skips ahead in pure excitement.

Just inside the main walkway Jack sees the large vertical store directory and map. Rather than getting lost in such a large place through exploratory wandering, he decides to use the directory to figure out exactly where in the mall the Build-A-Bear store is.

The directory in front of him is typical. A floor plan is illustrated that labels each store using apparently arbitrary numbers. Those numbers are referenced and sorted by category to comprise the store directory.

Immediately, Jack’s frustration begins to build. He struggles to determine what category Build-A-Bear falls into; he’s looking under Gifts, then Baby, both without luck. Maggie chimes in and finally finds the store under Fun & Games with a label of “L34.”

Once again, frustration builds when the family members can’t find their current location, or determine where L34 is. They do not see a “You are here” indicator. Annoyed by this barrier, Jack and the family give up, and walk farther into the mall in hopes of eventually coming across the store.

## The Weilers, Version 2

![](images/8e320ac0f2e010bc085d8db46f4d5d29a872f91fc58a6a5b3bc89086424cdcc2.jpg)  
Figure 8-1. Search within the address book is a modal behavior on some of the newest touch-centric OSes. The fact that it varies from all the other search capabilities on the device, and is more like the classic Search Within pattern, indicates how important and expected the function is.

Jack, Maggie, and Melissa are excited about visiting the Build-A-Bear Workshop in the new shopping mall. As they enter the mall for the first time, they see a crowd of people gathering at the story directory kiosk.

As they walk toward the crowd, they are amused to see that the mall uses a multitouch interactive table to display its layout and directory. Jack places his fingers on a portion of the screen to begin. That portion of the interface lights up and generates a pop up with an option to locate a store or to begin a video chat with the mall’s customer service department.

Jack is presented the option to filter his search by general category, with proxemics to his current location, or by alphabetized store name. Jack selects the alpha search, which reveals a vertical list of stores with location jump controls, as well as a text field with a touch keyboard.

Excited about this experience, Melissa engages with the table and uses the location jump control to find the stores that begin with the letter B. The “Build-A-Bear Workshop” label displays within the list. As she selects the name, an interactive floor plan of the mall immediately populates, illuminating the store’s location.

The floor plan at first shows the entire mall’s layout with callouts to the family’s current location and the Build-A-Bear location. Then the display slowly zooms and reorients to the family’s current position and animates an eye-level view of the walking route from their location to the Build-A-Bear store.

Having visually seen that the store is located on the second level next to the Food Court, one level above them and slightly to the right, the family heads in that direction, still excited by the engaging user experience.

## The Difference

![](images/ded754e7890fee4e1e12c52a8aeca8b280a1ecac26326ec886c146b7db54ec54.jpg)  
Figure 8-2. Gestural interfaces, almost by their nature, have little or no affordance before use. Location Jump is useful to allow initial gestures to expose more functions, and allow the user to reach his goal faster.

The two different scenarios provide polar examples of how a common task of locating information can lead to a frustrating user experience, or an enriching one. The solution was not just the power of the technology. It was also, and more importantly, how the content was organized, displayed, and made available to the user, in a manner useful to the user’s immediate needs and current context.

In the first scenario, all the information was presented at one tier, without the user’s ability to use controls to drill down, sort, and filter information for his current needs. This lack of control placed too much burden on the user, and resulted in a failed experience.

In the second scenario, the Weilers had access to a variety of information controls, such as location jump, search within, zoom and scale, and sort and filter, which made searching for relevant information much quicker. Each particular control provided a unique way of revealing different types of information.

## Information Controls in the Mobile Space

In the mobile space, where limited display sizes constrain the amount of information presented at a given time, a user will require affordable functions that provide quick access to her intended goals.

The following are some guidelines for providing information controls in the mobile space:

## Provide controls that afford their functionality by resembling their intended function

A control using a + or – button will be understood to zoom in and out, as opposed to using controls with arbitrary labels such as “A” and “B.”

## Make the controls visible

Users need to be immediately aware that controls exist to access and control the amount of information visible. Keep the control placement consistent across the OS or application. Because mobile screen real estate is valuable, consider using the Revealable Menu or Fixed Menu pattern.

## Use appropriate metaphors to establish learnability through familiarity

As Dan Saffer explains, “Metaphor is not just about language; it’s really about thought. We conceive of things in terms of other things” (Saffer 2005). When using metaphors, be aware that they may have various meanings across cultures, and match the metaphor to the content, not the content to the metaphor.

Consider how we understand the use of a magnifying glass to see detail. Some zoom and scale controls use this metaphor to communicate one’s ability to see more or less information.

## Provide immediate and appropriate feedback

A control must produce immediate feedback to communicate a change of state (contrast, color, shape, size, sound) that is measurably different from its initial state. Delaying feedback can result in the user performing other actions in the belief that the intended action failed.

## Provide constraints

Provide only the control functionality that is needed to complete the user’s task. Use a control for its purpose only. Do not assign it multiple, unrelated functionalities.

## Follow wayfinding principles

Make sure your users know where they are in the control’s current state, while providing information to communicate its range of control. For example, when using an alphabetical Location Jump widget, ensure that the selected letter is visible within the range of letters, while also communicating its relationship to other letters.

For more information on designing controls for people, refer back to Chapter 4. For a book on the subject, consider The Design of Everyday Things by Donald Norman (Basic Books).

## Patterns for Information Control

Using the information control widgets allows users to quickly access the type and amount of information within the current state of the device. In this chapter, we will discuss the following patterns:

## Zoom & Scale

Provides the ability to adjust the level of detail of high-density information by changing the levels of zoom and scale

## Location Jump

Allows the user to quickly jump to a specific location within a list of information (see Figure 8-2)

## Search Within

Allows the user, via a search field, to quickly filter or jump to specific information the user knows exists within the page (see Figure 8-1)

## Sort & Filter

A method to aid exploratory search by progressively disclosing search options to narrow the relevant results

## Zoom & Scale

## Problem

You must provide a method for users to change the level of detail in dense information arrays, such as charts, graphs, and maps. Design a zooming function or metaphor to provide this control.

Certain platforms, especially gesture-driven OSes and those built for display of map data, will have built-in zoom controls which should be used when available. Custom zoom widgets are easy to build and interact with, but retrieval of information in a seamless manner, especially from remote sources, can be more challenging.

## Solution

![](images/9a88bbf9471c07eba46bb2467c193ecad71f63d2b99001b823a9a9df2889ce77.jpg)  
Figure 8-3. The Interactive Scale combines the zoom control and zoom indicators. Often, they are accompanied by scale limit indicator icons as shown here in the country map and house (meaning neighborhood level). The scale can be used by clicking a zoom level to jump to it or dragging the control to a specific level. When included, zoom-in and zoom-out keys may be used to change one zoom level at a time.

High-density information, such as that in charts, graphs, and maps (as in Figure 8-3), can be especially difficult to use on small-screen devices. Showing a sense of the whole space can preclude viewing sufficient details for analysis and other uses.

Zooming into (and out of) the information is the general solution. As this is similar to changing the depth of view, it is a different axis than scrolling, and so requires a unique control set.

In coordination with changing the zoom level, you must also communicate a sense of scale, whether relative or absolute.

## Variations

## The Zoom & Scale pattern has the following variations:

## On-screen buttons

Buttons are very often provided to zoom in and out by single steps. There is no indication how large the step is, or how many are available. These may be placed at the corner of the view area, within a menu, or within an Annotation for a single point on the map or chart. See Figure 8-4.

## Interactive scale

A bar may be provided for direct control that indicates the whole range of zoom. Generally, icons are used at the top and bottom of the control that indicate the range of the control, such as (for a map) the country for the maximum zoom out, and a house to indicate block level for zooming in. These controls may support direct selection of a zoom level or direct control of the zoom level by moving the slider dynamically. They are also often combined with on-screen buttons to offer all options.

## Screen gestures

The most common of these is the two-finger “pinch to zoom” gesture. Other onscreen gestures are also used, including single-finger spinning actions (clockwise to zoom in, counterclockwise to zoom out). These may be useful for systems that cannot (for technical or user needs) support multitouch. See Figure 8-5.

## Hardware buttons

Devices that do this a lot, such as GPSes, might have dedicated zoom buttons. In addition, you can repurpose unused hardware keys; if the five-way pad is used to scroll along the x- and y-axes (and select points), the volume rocker can be repurposed to control the z-axis and be a zoom control.

Additional methods may emerge in the future, such as the use of sensors to change detail level as the device is moved toward the viewer’s eye.

You can combine some or all of these for interfaces that work on multiple devices without change, to appeal to different user types or to surmount lack of affordance in screen gestures.

For controls that do not integrate a scale, you should provide some sense of scale. This may be an explicit scale (labeling axes or a bar of distances), or it may be implicit, by showing items of a well-understood size.

Interaction details  
![](images/4c5feae9c05e8e77056ff2280b2c48baf77151076f1379f0cb7a58221a7e9895.jpg)

![](images/f62c1b6cecea681c9fcea88ad8a3720746482740fd6408dac02e2faf60ecf552.jpg)  
Figure 8-4. On-screen buttons may also have a permanently visible indicator of zoom level. If it is not interactive, as this one is not, it does not become an interactive scale. Zoom may be for only one axis for some items, such as this one which zooms only the data. The scale indicators for graphs and charts will vary by axis. Make sure the scale is clear by providing all needed labels to understand the full context.

Consider zoom to be a third axis of movement about the screen. Like the x- and y-axes are along the edges of the screen, the z-axis sticks straight out from the screen. You can think of the zoom control as moving to layers or levels along this axis.

The z-axis must be directly related to the request method, so the zoom does not break the user’s expectations. There are two basic methods to establish this center point:

View center

The zoom axis is about the center of the displayed graphic, usually the center of the viewport.

## Activity centroid

The zoom axis is centered on the indicator, pointer, or gesture used to indicate the zoom.

Zoom actions taken with no particular item in focus, without an on-screen cursor and without controls attached (visually or by use of gesture) to a specific point on the screen, use the view center method. All others use the activity centroid model, with the axis centered along the in-focus item or the gesture centroid. Note that these are not fixed conditions based on the device hardware or the overall interaction model; you can switch between them in a conditional manner. Zoom buttons (whether on-screen or hardware) will use the view center method when nothing is in focus, and switch to the activity centroid method when a virtual cursor is moved onto the screen or an item is in focus.

Any effect requested should show an effect immediately. Whenever possible, load a few additional zoom levels in advance, in a similar manner as described in the Infinite Area pattern.

For devices with keyboards and without dedicated zoom keys, you should provide accesskey functions (and their corresponding labels) for at least the zoom-in and zoom-out controls (see the Accesskeys pattern).

Disregard input to zoom over the limits of the current information set, either too high or too low; for example, do not display errors for which insufficient information is available for the zoom level. The user will simply have to initiate another zoom control to back out until the information is again useful.

Presentation details  
![](images/598737657bb09da1e961fa4cdcc98030626a013013f81bc959693f6edcad5385.jpg)  
Figure 8-5. Even if the screen is otherwise devoid of zoom control elements, as with this touchscreen example, display the current zoom level during a zoom change. Place the indicator so that it is not occluded by the user’s hand or fingers.

Regardless of the interaction variation, you must display a zoom indicator on the screen whenever the zoom level is changing. This indicator must immediately reflect the current zoom level setting; if there is a delay in loading the new data, display the requested setting, not the previous one. The indicator should remain visible for a short time after the zoom level has completed loading.

If there will be delays in loading, be sure to follow the principles in the Infinite Area pattern, and display a Wait Indicator, either for the entire application or for each frame of information being loaded.

Whenever practical, display a scale on top of the displayed information. For maps, this is a simple distance scale. The scale must automatically adjust to fit the available space, both in size and in units used. On maps, you may switch from hundreds of miles to hundreds of feet as the zoom rate increases.

When a zoom level is unavailable—such as when the end of the range has been reached— gray out the control to make it clear it is inaccessible. This is generally preferable to simply suppressing the control, as it may be confusing if it is usually present.

When there is a choice (such as on maps versus labeling individual axes of a graph), the scale bar should be horizontal. The scale bar should be large enough to be easily visible so that numeric labels are readable, and small enough that it takes up no more than about one-third of the width of the screen.

Label units of measure, and use standard abbreviations to label them. See the Ordered Data pattern for more discussion along these lines.

For gestural actions, such as pinch to zoom, use live transitions so that the user can see the effect of his gesture and adequately control the request.

For all zoom methods, if full-resolution imagery cannot be preloaded, you should use a variation of the ghost method described under the Wait Indicator pattern. You can scale the available imagery to match the requested panel size, giving a sense of the requested scale and information.

## Antipatterns

Avoid delays in loading new zoom levels. Do not assume a Wait Indicator will solve the issue, but if one is needed, use it, as the Infinite Area pattern does when loading new data. Use the ghost method instead of explicit indicators such as short wait whenever delays cannot be avoided.

Don’t use a toggle between two levels of zoom because your only convenient interaction does not support steps or gradations. Zooming via double-tap, for example, has value in some cases but is not a typical zoom and does not cover the majority of the needs for zooming into data.

![](images/bf5d763123218a4c5ac2f306cc261bcdc7c4df7f345b873d915ddaf75aae3b15.jpg)  
Figure 8-6. A very common use of this pattern is in the address book. It is often a long list, the data is easily divided into a simple alphabetical index, and contacts are referred to by name so that users can easily find them by using this indexing system. Note that the entire index often cannot fit on the screen. Some scrolling may be required to get to other parts of the index.

## Location Jump

## Problem

Scrolling to items in a long vertical list is cumbersome. You must be sure to design an indexing system to assist in retrieval, and to design a method to allow easy access to key indexed portions of the list.

Location Jump controls are typically custom-built to integrate with their host interactive methods. Enough variations of this pattern exist to allow it to work on any device, but be sure to choose one that works best with your display and input features and standards of interaction.

## Solution

The problem of accessing long lists of ordered data is not unique to interactive systems, and the solutions are directly related to the methods derived in the machine era. The Rolodex (a portmanteau of “rolling index”) is the prime example, a series of cards separated by tabbed label cards for letters of the alphabet.

This might seem to be akin to the Tab pattern, but the tabs here are different. Instead of providing access to different, parallel information sets, they are simply markers inline with the same, continuous list.

The variation on this, the flat Autodex with a single list of letters and a sliding control to select the section, is even more directly what is copied into digital Location Jump systems. An indicator of location, or indexing system, is visible on the screen, as in Figure 8-6, and this may be used to jump to the front of an indexed section.

These are used with the Vertical List pattern, but you could also use them in other types of displays as well. Specifically, the Location Within pattern used on Film Strip-like Home & Idle Screens can be interactive instead.

The Location Within pattern is very similar, but does not have interaction. Pagination is likewise similar, but page numbers are not an indexing method as they are unrelated to the content itself.

## Variations

![](images/1f08cf88a0f70cad154f3a420268289b508dac073bef1eb3b95caf8aeaa1fd09.jpg)  
Figure 8-7. The Location Jump widget can be used to reference or jump to any type of relevant index value. Here, a photo gallery is displayed in a single list, with index points by month and year. Without this pattern, a similar organization would have required a folder structure. The indicator shows index information with additional specificity.

There are two key sets of variations. The first is in display:

## Content indexing

The strict Rolodex style, with letters, numbers, or whatever other key indexing item is in the list. Thumbnails generally do not work well.

## General indicators

Most often dots, sometimes in varying quantities or sizes, but also icons and numbers. These are only really suitable for smaller sets, such as Home & Idle Screens, but there is much room to expand the pattern here.

You can also allow interaction with each of these in one of two key ways:

## Direct selection

Click on the indicator label directly, or type it in. Press a P, and jump to the “P” section.

## Drag selection

Drag an indicator of the current position, much like a scroll bar, to the position you want. See Figure 8-7.

Of course, you can use both of these together. You can also use other methods to move the list, such as the simple Scroll.

Interaction details

![](images/4174bd6694de841f0db69a615120a53eb3c87a0bf9b53e40b4096ea757f9e6aa.jpg)  
Figure 8-8. Items with no obvious index value, such as a multiple home page, can use more generic identifiers. Here, the Location Within widget appears to be used when static, but when motion begins it transitions to a larger, directly selectable set of Location Jump indicators.

Direct selection, or scrolling within the list, is very straightforward when touch or pen interfaces are used. Virtual cursors and five-way Directional Entry pads do not work well with this pattern.

You may take advantage of the Location Jump pattern for scroll-and-select interfaces by using Accesskeys for the input method. This works best when the input method corresponds to the indexing method. A 10-key device will present difficulties with alpha input, though methods have been devised, such as clustering and using numeric keys to jump to sections. More often, the Search Within pattern is used for the actual keypad input, even if a Location Jump-like Position Within indicator is also presented.

For Vertical List displays, you must usually remove or heavily modify any scroll bar in favor of the Location Jump indicator complex. Any use of the other scroll methods, such as gestural scroll or hardware keys, must work in concert with this pattern, and indicate changes immediately.

## Presentation details

Store any indicators, whether a symbol or an index value such as a letter, in a strip (which may not be opaque) along the axis of movement of the list. A vertical list will have a vertical strip. Generally, you should put this on the lowest-use side, so put it on the right side for vertical lists.

The key problem with this pattern is making the widget large enough to be visible—or for touch devices, large enough to be selected—without using too much screen space or distracting the user from the primary task.

The general solution is to always present the indicator, but very small (with the characters as much as half the conventional minimum size). As soon as any action occurs relating to item finding—such as scrolling, direct input via keypad, or on-screen gestures to that edge—have the indicator strip expand to a viewable and selectable size.

An alternative is to have only the portion that is currently in focus expand to the larger size, if scrolling instead of direct selection is the access method. For all scrolling-only interfaces, the index item currently in focus should be approximately centered in the viewport along the scroll axis. At the ends of the list this may look odd, and it may have to skew to the natural edge instead.

When a position is selected by scrolling the Location Jump widget, the list itself must have live scroll, although you may simulate this by adding a motion blur to the data presentation if the distance to be scrolled is more than a few items. When the user jumps to a new position by direct selection of an index feature, the interface will scroll to the new position to indicate the change.

If the distance is very large, simulate a scroll by accelerating, then jumping closer, then decelerating to the location. This jump may also be obscured with a brief motion blur. The total transition should only take one-half to one second, but the transition helps a great deal in understanding that the action was carried out. One part of a list is very much the same as another, so a change may not be noticed if an instant jump occurs.

The current position in the location indicator must always be communicated. Anything clear will do, from highlight, to bold, to an indicator bar or other icon in the bar. This must also animate live when scrolling or jumping to a new position. See the interaction in Figure 8-8.

## Antipatterns

![](images/880c472efc9854c2ef755c14144150a52da100653d4d2540eadacc4fe718de8d.jpg)  
Figure 8-9. Avoid placing functions in the list items next to the location bar, to avoid accidental input. Here, the indicator to see details on a contact will interfere with the Location Within widget. Allow for more space, or place the actions on the left side of the list.

As with any scrolling method, do not jump to the new position. Always indicate that the new position in the list was scrolled to by actually showing the animated scrolling to the actual new position in the list.

Do not allow indicators to disappear during scrolling and other movement. They must also transition live whenever possible.

Use caution when placing items within a list. Do not allow critical labels to disappear under the position indicator. On touch devices, keep buttons and other interactive items away from the Location Jump controls side of the list. See Figure 8-9.

## Search Within

## Problem

Finding specific items within a long list or other large page or data array is cumbersome.   
You must provide a method for the user to find and display this information.

Though search forms are very commonly built-in functions, live or component updating may not work, or not work well, on all platforms. This pattern is especially difficult to implement well and consistently on the Web.

![](images/f8a23a609fe10ce744dc8aea0aa743b2137868ed3eb2d42e5ae7c623df3201a6.jpg)  
Figure 8-10. The live jumping Search Within style is almost ubiquitous on scroll-and-select address books such as this. Both the search field and the first line item (until the user scrolls) are in focus, one for typing and the other for selection. It is also often a good idea to indicate what about each result caused it to be displayed, here by making the search string in bold.

Even the most common informational display on interactive systems can contain impressive amounts of information. Even if a user knows that a particular piece of information is present—from a web search or from memory—it may be very difficult to find by simply browsing or scrolling through lists.

It is also implausible to assume that all information finding may be solved by proper page design. The design of web pages, for just one example, is out of the hands of web browser designers. A method must then be provided to search for specific items within the displayed information set.

Search is, in fact, exactly what is used. You simply place a text search on the page, and the results of this search are jumped to or filtered within the space of the default results list. For mobile devices requiring this feature, the search must more often than not be visible by default, and very often have focus on entry to the page. When of secondary importance, it may be a feature that is explicitly summoned from a menu.

## Variations

Variations of this pattern depend widely on the pattern used to display the information:

## Live jumping

The most common and the oldest style of the Search Within pattern is especially suited to long lists such as address books, and for scroll-and-select devices. When the page is loaded a search field is in focus. Typing will immediately result in a jump to the results. See Figure 8-10.

![](images/a79fa55fe450228ea64c00394481364f39777f5940d465a9519d3e09cf3aea3d.jpg)  
Interaction details  
Figure 8-11. Explicit filtering, especially in lists, may look almost exactly like live jumping. If both are used in adjacent lists, care must be taken to differentiate the two interaction methods. Users will usually have to deliberately select the search box to enter information, and then press the Search button (or OK/Enter key) to submit. This variation is particularly suitable for very large lists, especially if they are retrieved from a remote server and there is a time delay.

## Explicit filtering

This is most often used as a replacement for live jumping when explicitly revealed by the user, and very often for touch or pen interfaces. Due to the perception of a conventional search and the familiarity of many users with web search, this behaves as a filter for the list data displayed, suppressing all other results. The search is typed in its entirety and then submitted by the user. This may also be more suitable for Infinite List pages, where live jumping may have odd-looking delays in the display of some results. See Figure 8-11.

## Highlight results

This is a display method alone, though often explicitly operated as opposed to being opened by default. The search method should display as live results whenever practical but should use explicit submission when needed, as when the results set is not loaded. These are commonly encountered when searching within web pages, documents, or maps. The results only make sense when displayed in context, and so are left as such. See Figure 8-12.

A key and increasingly relevant variant of this is non-text-faceted search. Other, preset parameters are offered for selection and may be used alone or in combination with a text search. This is particularly suitable for maps; a preselected list may include restaurants, transit, and types of shopping.

The live-jumping style of list display is loaded with a Search Within entry box anchored to the top of the viewport. On scroll-and-select devices, this has an unusual, almost unique sort of in-focus relationship with the list. The top item in the list is generally in focus and is displayed as such. Pressing Enter (or sometimes using the Left and Right keys) will commit whichever action corresponds to the line item.

However, regardless of the list item in focus, typing from anywhere in the list, at any time, will enter characters into the Search Within field at the top of the viewport. Naturally, you have to disable Accesskeys for such interactions as the keys are dedicated to typing instead.

A variation is to make nothing appear in focus; the text field behaves in the same manner, but a downward scroll is required to bring the first item in the list into focus. When this is used, the top item in any result is still presented as though it is in focus. Yet a smaller subvariant of this—usually specific to an existing OS standard—is to have the same search either initiated by a dedicated search button or revealed when any text entry is made.

For the highlight-results variation, when more than one result is found, a simple Pagination widget will be provided, with the total number found, the current position in the results, and a method to move between individual results, such as Back and Next buttons.

Search methods—whose results are displayed from a particular entry—are left to the specific implementation, and must consider the way the data set is most naturally used.

![](images/183e7aff23ffaaf699b82a6b568cb22163e900b427bc65486352a48dddacc502.jpg)  
Figure 8-12. Highlight results on web pages and within text documents simply highlight the text results and jump to the next relevant result when selected by the user. The current item is highlighted slightly differently, and may be in focus for other interface purposes. The map on the right is displaying in essentially the same manner, using one form of icon for all results, and the item in focus has a larger one. A button is provided for a list view, and Previous/Next buttons are provided.

Display of results must be immediate, and require as little additional user input as possible. Display the number of items found and the total number of items in the data set for all types of lists and results.

For the live-jumping variation, the list is unchanged and simply scrolls so that the first relevant result is at the top of the viewport. The remainder of the list is still there, and may be found by scrolling.

For the highlighted-results display variant, each individually found result will be indicated. Usually, as the namesake would indicate, they are highlighted with an underlying color that contrasts with the background and allows the text to be readable.

The current result, when multiple highlighted results are available, will be highlighted in a unique manner and must always be moved to appear within the viewport. Zooming and other techniques may be automatically employed to ensure that the result is readable in context if it is not of a readable size or position when the search is initiated.

When the information found is not explicitly visible or cannot be usefully displayed by simply zooming in, you can add a Tooltip or Annotation bubble to label the results. For multiple results, a small pinpoint is generally used; the item in focus is an expanded label.

Results are generally as close to instant as possible, as the information is already loaded. For certain uses, such as for Infinite List or Infinite Area displays, there may be a delay for some of the information. This may be confusing for live-jumping-type displays, so instead the explicit filter style should be used, and a suitable Wait Indicator used for any delays that cannot be avoided.

## Antipatterns

Use the correct method for the information set available. Using an improper method can confuse the user or provide inappropriate or incomplete results.

Carefully consider what an “Enter” key action performs during a live-jumping search. If the user is not looking at the screen and does not notice the results are already displayed, he can assume an explicit search. If a result is in focus, pressing “Enter” may commit an action the user did not intend or which is destructive.

## Sort & Filter

## Problem

Large data sets often hold information with multiple, clearly defined attributes, shared among many items in the set. You have to provide a way for users to sort and filter by several of these common attributes at once, in order to discover the most relevant result.

Sort & Filter is an information processing and organizational pattern. Although some variant implementations may have special technical needs, the concept can be implemented on any platform, even on a website for the lowest-end, script-free browsers.

![](images/f812add6fccef8d734e76e2df7444b2791b574ddba7aceff39e3929d28287847.jpg)  
Figure 8-13. In most cases, only one selection should be offered at a time, and the selection should be a simple single selection. This may be used without complex interactions, and works well with text entry or pull-down selectors. Note the title, revealing some of the categorization, and the counter of results, which assists the user in understanding if more filtering is required. Breadcrumb labels should be identical to the selectors, including category labels (such as “Brand” on the right), to preserve the user’s mental model of the system architecture.

Search can be considered as either information finding or information exploring. Simple tools such as Search Within are for finding specific information the user already knows to exist. This is clearly exemplified by that pattern’s most common use, the handset address book. The user should know each of these individuals, has generally added each one by hand (though the rise of contact synching makes this less sure each year), and is looking for a specific one by name.

Exploratory search is used to find items the user suspects exist, or which the user cannot explicitly recall. Faceted search (searching on different attributes to approach the results from multiple angles, such as the cut facets or faces on a jewel) may be required to find such ill-defined items. Sorting is used to present the most relevant results first, from of a possibly large results list.

The keys to implementing Sort & Filter features on mobile devices are:

• Progressive disclosure

• Contextual relevance

Even when there is room, users may not understand that multiple selections are offered within a single selection area and may be confused or only make a single selection at a time.

Some options—and especially sorting options—may not have a clear value to the user before the results are displayed. Instead, offer a single key selection and then, when results are displayed, present additional facets for search, or the ability to sort the results.

To aid users in obtaining the best results, always make informed default choices for them. Sorting, for example, should be “best match” for most cases, but may need to be alphabetical for items such as people, due to the familiarity with names.

## Variations

The exploration of information that Sort & Filter offers may be presented in one of two distinct manners:

## Navigation

The current filter set should appear as a similar navigational paradigm. The whole displayed set will be applied to the same level, and when the individual selection is made, others will be excluded and cannot be selected again. When no subsidiary facet is available (or when selection of another facet requires an explicit action), these may appear to be a structure like Tabs, and indicate which selection has been made. Otherwise, the selection is effectively a Button, and submits the change. This display method is not suitable for sorting, as it may be perceived as an exclusive set (a filter) and the results may confuse the user. See Figure 8-14.

## Submission

The current set of filters is offered as a series of links, or a set of Form Selections such as a pull-down list. When selected, these will be submitted immediately. Sorting should always use this pattern. When space allows, use a series of links as a breadcrumb (see the Link pattern) so that the entire set of options is visible to the user. See Figure 8-13.

As long as additional facets are available for selection, the next one in turn will be offered, generally at the top of the results page. Sorting is always offered, but in an area distinct from the filter, and with a clear label.

Interaction details  
![](images/3640631ceb43345ab5225174d6c2a520b5d10a12e9beaaacae469001297a9379.jpg)  
Figure 8-14. Your site or application may benefit from making the filters appear as navigational elements, such as tabs or similar selectors. This exemplifies the pitfalls of any such system as text is inefficient in the horizontal plane. The “Search” label on the Back button indicates that the previous filter applied was a text search, and the user may step back to change the search parameters.

As each facet is applied individually, whether of “navigation” or “submission” style, only the one set of items is offered, and the user must use a separate method to access and change other facets.

This will be presented as a history list, “breadcrumb,” or “back” function. Allow the user to step back in the process, or jump to the relevant section. Additional, subsidiary choices should be retained and reapplied, or the previous settings should be the default values when subsequently offered within this session.

Though the initial selections should be offered individually, once they are selected, the user may have formed a mental model of the system, so the entire set may sometimes be presented as a series of selectors. The user may change as many as desired and submit these changes as a batch, or individual changes may immediately take effect.

User input should be preserved in general. Especially when some filters have been applied as text entry, some sort of retrieval, undo, or history function should be provided. Though it may not seem like user entry, the Cancel Protection and Exit Guard principles should be applied due to the possibility of the user spending some time creating a detailed, custom search.

Some filters should support multiple selections for a facet, or may already do so in the desktop iteration. An example is to view only certain brands; in this case, only being able to see one at a time may not help. If needed, this may require a large modal dialog or fullpage selector and a Select List. A similar problem, also requiring a large dialog or full-page selector, may be encountered with range selectors.

Presentation details  
![](images/d11f1e408771b7527441cfbd82651ecc8a7b5588d3324719b9ad571546bb9b7a.jpg)  
Figure 8-15. The bottom of the list should ideally have the same filter mechanism, or easy access to it (such as anchoring to the edge of the viewport). Try to make sure at least some results are still visible, so the user is aware he is still in the list view. As shown, this may preclude inclusion of some components; here, only the breadcrumb is shown. When space is short, sorting may appear only at the end of the list, and should always be explicitly different. This is centered, is labeled, and uses links, even though a pull down would work at least as well, to avoid confusion with the form elements used for the filter.

Faceted search helps users who need or want to learn about the search space as they execute the search process. Facets educate users about different ways to characterize items in a collection. If users do not need or want this education, they may be frustrated by an interface that makes them do more work.

The search space is classified using accurate, understandable facets that relate to the users’ information needs. As we’ve discussed before, data quality is often the bottleneck in designing search interfaces. Offering users facets that are either unreliable or unrelated to their needs is worse than providing no facets at all.

Display results in the most suitable method. Usually, you will find this to be a Vertical List. Sufficient space must be provided for the functionality described. When space provides, and when technically possible, it is desirable to have the Sort & Filter functions be docked to the top of the viewport. In this way, the user may decide additional or different selections are required at any time when browsing the results, without scrolling to the top. If this is not practical, place the selectors at both the top and bottom of the results.

Display methods, such as limited-size lists with Pagination or using an Infinite List, are up to the designer and the needs of the user. Consider the entire interaction, though, and ensure that the user can get to the Sort & Filter functions easily.

The currently applied filters should be presented in the page Title or just below it, as space allows, and repeated at the bottom of any scrolling page as in Figure 8-15.

## Antipatterns

Many conventional sorting patterns, such as clicking on column headers in table displays, do not work well in small screens. Even when screen space is available, user expectations are not the same, and these generally will not work without explicit instructions.

Users can easily confuse the actions of sorting and filtering, so you should present these options in different areas or at different times. Use clearly differentiable labels such as “Show only” for filter and “Show first” for sorting. The terms Sort and Filter are largely meaningless to the majority of end users, and so should be avoided.

Do not simplify navigation or search systems for mobile due to the constrained interface. If the information is the same, the user’s needs are the same. In many cases, the need for getting specific information quickly is greater due to the additional difficulty of browsing and reading content from many results.

Selected actions should always be performed on the entire results set. Do not, for example, just sort the items currently displayed on the screen, or that have been downloaded to the device cache.

## Summary

## Wrap-Up

As we’ve discussed, mobile widgets are highly reusable items and are used repeatedly, across the device’s OS and applications. Widgets can be used to quickly access related levels of information, provide visual cues about the current state of the device, and control the amount of information and level of detail needed on a page.

## Pattern Reference Charts

The pattern reference charts in the following subsections list all the patterns found within each chapter described in this part of the book. Each pattern has a general description of how it can apply to a design problem while offering a broad solution.

Cross-referencing patterns are common throughout this book. Design patterns often have variations in which other patterns can be used due to the common principles and guidelines they share. These cross-referenced patterns are listed in the following charts.

## Chapter 5, “Lateral Access”

This chapter explained how lateral access widgets assist the user in quickly navigating to and accessing content in the same tier level. This is especially important on mobile devices because the potentially smaller screen sizes affect the amount and type of content presented, and the user’s ability to successfully search, select, and read this information.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td>Other patterns to reference</td></tr><tr><td>Tabs</td><td>Access must be provided to a small number of items at the same level in the information</td><td>Follow the file folder metaphor by creating distinct labels that separate three to eight sets of content.</td><td>Titles Pagination Location Within</td></tr><tr><td rowspan="2">Peel Away</td><td>architecture, while also clearly communicating this hierarchy of information. Display a small amount of</td><td>For touch and pen displays, use a</td><td>Simulated 3D Effects</td></tr><tr><td>deeper information, or provide access to related controls or settings, in an organic manner.</td><td>simulated 3D effect to represent a paper page, which can be peeled or flipped back to view a second page behind it.</td><td>Pagination Pop-Up Film Strip Fixed Menu</td></tr><tr><td>Simulated 3D Effects</td><td>Display a small amount of directly related information, provide access to related con- trols or settings, or provide an alternative view of the same information, in an organic</td><td>Use Simulated 3D Effects to pretend components on the page, or even the whole page, merely present one side of a physical object. Rotating the object, moving it aside, or look- ing past it can then be done without 3D technologies.</td><td>Stack of Items On-screen Gestures</td></tr><tr><td>Pagination</td><td>manner. Location within a series of screens continuing display of a set of content should be clearly communicated and access provided to other pages in the stack.</td><td>Page numbers, and a sense of the relative position within the total, are displayed. Tied to this display is a method to move between pages easily and quickly. Methods to jump further than the previous and next pages are also usually offered.</td><td>Infinite List Search Within Location Within Peel Away Directional Entry Accesskeys</td></tr><tr><td>Location Within</td><td>Location within a series of screens with alternate views, or which continue the display of a set of content, should be clearly communicated.</td><td>When several screens of similar or continuous information are presented with an organic access method, an indicator is usually re- quired so that the user understands his position within the system.</td><td>On-screen Gestures Slideshow Film Strip Pagination On-screen Gestures Tabs</td></tr></table>

## Chapter 6, “Drilldown”

In this chapter you learned that drilldown widgets are used to support many functions that contain parent-child relationships. These widgets can be used in any context to provide access to related content, allow the user to submit information, create a change in the current state of the device, and provide related information in a glanceable manner. Drilldown widgets support the parent-child information architecture relationship.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td colspan="2">Other patterns to reference</td></tr><tr><td rowspan="3">Link</td><td rowspan="3">A function must be provided to allow access to related content from arbitrary locations within a page.</td><td>Links are content-only items that provide access</td><td colspan="2">Pop-Up</td></tr><tr><td>to additional information</td><td colspan="2">Vertical List</td></tr><tr><td>either by loading a new page, jumping to a piece Icon</td><td colspan="2">Indicator</td></tr><tr><td rowspan="3">Button</td><td rowspan="3">Within any context, an action must be initiated, information submitted, or a state change</td><td>of content, or loading a pop-up dialog.</td><td colspan="2">Button</td></tr><tr><td>Use a Button to initiate an immediate action such as</td><td colspan="2">Link</td></tr><tr><td>changing device modes and committing user selections.</td><td colspan="2">Icon Indicator</td></tr><tr><td rowspan="3">carried out.</td><td rowspan="3"></td><td rowspan="3"></td><td colspan="2"></td></tr><tr><td colspan="2">Mechanical Style Controls</td></tr><tr><td colspan="2">Pop-Up</td></tr><tr><td colspan="3"></td><td colspan="2">Exit Guard</td></tr><tr><td>Indicator</td><td>Within any context, an action must be initiated, information submitted, a link followed to more information, or a state</td><td>The Indicator pattern is a type of action initiator be- tween a Link and a Button.</td><td>Link Button</td></tr><tr><td rowspan="5">Icon</td><td rowspan="5">change carried out on the current page. Provide access to disparate items or functions, in a glance-</td><td>Indicators are always used</td><td>Icon</td></tr><tr><td>with text labels, and may perform any action: linking,</td><td>Pop-Up</td></tr><tr><td>state changes, and commit</td><td>Pagination</td></tr><tr><td>actions. Icon widgets provide im-</td><td>Link</td></tr><tr><td>mediate access to additional</td><td>Button Indicator</td></tr><tr><td rowspan="6">Stack of Items</td><td>able manner.</td><td>information such as target destinations and device</td><td></td></tr><tr><td rowspan="6"></td><td>status changes, and are</td><td>Home &amp; Idle Screens</td></tr><tr><td>easily understood by their</td><td></td></tr><tr><td>graphical representation.</td><td>Grid</td></tr><tr><td></td><td>Carousel</td></tr><tr><td>Thumbnail List</td><td>Avatar</td></tr><tr><td rowspan="6">contents. Annotation</td><td>A set of closely related items,</td><td>A set of stacked thumbnails</td><td>Hierarchical List</td></tr><tr><td>which can be represented as icons or thumbnails, must be presented in a manner</td><td>are arranged with only the top one completely visible.</td><td>Icon</td></tr><tr><td></td><td></td><td>Grid</td></tr><tr><td>implying the hierarchy and providing easy display of the</td><td></td><td>Fixed Menu</td></tr><tr><td></td><td></td><td>Revealable Menu</td></tr><tr><td rowspan="6">A data point in a dense array of information must be able to show additional details or options without leaving the original display context.</td><td rowspan="6"></td><td></td><td>Wait Indicator</td></tr><tr><td>An iconic element points to the information selected,</td><td>Link</td></tr><tr><td>and presents (sometimes</td><td>Button</td></tr><tr><td>Tooltip only after further selection,</td><td></td></tr><tr><td>or in another area of the Fixed Menu</td><td></td></tr><tr><td>screen) a label and ad-</td><td>Revealable Menu</td></tr><tr><td colspan="2"></td><td>ditional options.</td><td>Simulated 3D Effects</td></tr></table>

## Chapter 7, “Labels and Indicators”

In some situations, you may be required to use small labels, indicators, and other additional pieces of information to describe content. Mobile users each have unique goals. Some require instant additional information without clicking. Others may need additional visual cues to assist them while quickly locating information. In any case, the information labels must be presented appropriately while considering valuable screen real estate, cultural norms, and standards.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td>Other patterns to reference</td></tr><tr><td>Ordered Data</td><td>Present information, especially text and numerical data, in the most appropriate and</td><td>Content types that are displayed frequently have become regular- ized in their display, and must be</td><td>None</td></tr><tr><td>Tooltip</td><td>recognizable format for the context and viewer. A small label, descriptor, or additional piece of information is required to explain a piece of</td><td>presented in specific formats to be easily recognizable to users. A tooltip is a transient, contextual, informational assistance widget initiated by hovering over a target,</td><td>Fixed Menu Revealable Menu</td></tr><tr><td>Avatar</td><td>page content, a component, or a control. A glanceable representation of a person should be provided, for use in various contact- listing contexts.</td><td>or automatically presented when the system determines the user needs help. An avatar is an iconic image used to represent or support the label for an individual, such as a contact in the address book.</td><td>Icon Indicator Thumbnail List</td></tr><tr><td>Wait Indicator</td><td>Processing, loading, remote network submission, and</td><td>Use a Wait Indicator to inform users of delays which are imposed by</td><td>Link Tooltip Interstitial Screen Infinite Area</td></tr><tr><td>Reload, Synch, Stop</td><td>other delays must be clearly communicated to the user. User control must be provided for loading and synching op- erations with remote devices</td><td>technical constraints. Due to specific user needs, acciden- tal inputs, or system constraints,</td><td>Reload, Synch, Stop Notifications Icon</td></tr></table>

## Chapter 8, “Information Controls”

This chapter explained how information control widgets can be used to quickly find specific items within a long list, information set, or other large pages or data arrays.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td>Other patterns to reference</td></tr><tr><td>Zoom &amp; Scale</td><td>Data in dense information arrays, such as charts, graphs, and maps, must be able to change the level of detail pre-</td><td>Use Zoom &amp; Scale to zoom into and out of information while commu- nicating a sense of scale, whether</td><td>Annotation On-screen Gestures</td></tr><tr><td rowspan="5">Location Jump</td><td>sented by a zooming function or metaphor.</td><td>relative or absolute. An indicator of location, or indexing</td><td>Ordered Data Wait Indicator Infinite Area</td></tr><tr><td>Scrolling to items in a long vertical list is cumbersome. The information must be</td><td>system, is visible on the screen and</td><td>Tabs</td></tr><tr><td>indexed to assist in retrieval,</td><td>may be used to jump to the front of an indexed section.</td><td>Vertical List Location Within</td></tr><tr><td>and a method provided to al- low easy access to key indexed portions of the list.</td><td></td><td>Home &amp; Idle Screens Accesskeys</td></tr><tr><td></td><td></td><td>On-screen Gestures</td></tr><tr><td rowspan="5">Search Within</td><td>to find and display this</td><td></td><td></td></tr><tr><td rowspan="5">Finding specific items within a long list or other large page or data array is cumbersome. A method must be provided</td><td>A text search may be placed on the</td><td>Search Within</td></tr><tr><td></td><td>Infinite List</td></tr><tr><td>page to search for information within the displayed information set.</td><td>Accesskeys</td></tr><tr><td>Annotation</td><td>Pagination</td></tr><tr><td rowspan="5">Sort &amp; Filter</td><td>information.</td><td></td><td>Wait Indicator</td></tr><tr><td>Large data sets often hold</td><td></td><td>Tooltip</td></tr><tr><td>information with multiple,</td><td>Use Sort &amp; Filter to present the</td><td>Search Within</td></tr><tr><td>clearly defined attributes,</td><td>most relevant results first, from of a possibly large results list.</td><td>Exit Guard</td></tr><tr><td></td><td></td><td>Vertical List</td></tr><tr><td rowspan="5"></td><td>shared among many items in</td><td></td><td></td></tr><tr><td>the set. Users must be able</td><td></td><td>Infinite List</td></tr><tr><td>to sort and filter by several of</td><td></td><td>Select List</td></tr><tr><td>these common attributes at</td><td></td><td>Pagination</td></tr><tr><td>once in order to discover the most relevant result.</td><td></td><td></td></tr></table>

## Additional Reading Material

If you would like to further explore the topics discussed in this part of the book, check out the following appendixes:

The section “General Touch Interaction Guidelines” in Appendix D

This appendix provides valuable information on appropriate sizes for visual targets and touch sizes for interactive displays.

The section “Fitts’s Law” in Appendix D

In this appendix, you will become familiar with Fitts’s Law, which explains that the time it takes a user to either select an object on the screen or physically touch it is based on the target size and distance from the selector’s starting point.