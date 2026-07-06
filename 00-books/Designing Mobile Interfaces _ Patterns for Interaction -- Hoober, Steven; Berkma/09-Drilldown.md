# Drilldown

## Get Ready to Push!

Driving cross-country in your car can be quite exciting—whether you’re stopping in small, quaint towns that are hardly noticeable on a map, flying down coastal highways with perilous views below, or enjoying the endless horizons of the plains. However, that state of happiness usually breaks immediately when you notice the low-fuel status icon has now appeared in your gas gauge.

This icon’s design creates more user mental load than necessary. If you’re in the middle of nowhere, and you haven’t seen a gas station or fuel information sign in miles, and now, on top of your uneasiness, you must calculate and predict how far you can go without running out of gas, you’re wondering:

• Did this status light just come on?

• Or has it been on for several miles?

• How many miles am I going to have to walk to find a gas station after I run out of gas?

• Do I have the appropriate walking shoes?

What you really need is the ability to quickly access additional related information.

![](images/fc454ca63d281ab8188597f35c6b79f1976cffc8269705d31036cdee16a6c983.jpg)  
Figure 6-1. Iconic labeling allows you to add information and selection methods directly to graphical or visualized data elements. The user knows what the interesting stuff is on the page, can tell the difference between the various types of information, and has an accurate expectation of what will happen if he selects an item. Even if the element opens additional details, hints of the data are presented contextually and invite users to find other features without exploration.

## Maybe We Won’t Have to Push

Maybe the fear of running out of gas will come to an end; we’re not referring to alternate energy sources here, but rather to an improved display design on our dashboard.

Here are some suggestions:

• Provide more surface-level information. For example, imagine if this status icon was interactive. Pushing it may reveal numerical information about how many miles you have left before you run out of gas. Also, make the initial warning light blink on and off, and then pause in a calculated repetition.

• Because our short-term memory can only hold about three chunks of information at a time, we usually store chunks that are important to the task at hand. If a warning status light appears without undergoing periodic state changes, our current attention may not focus on it and we’ll assume it’s not even there.

• Provide drilldown access to additional information. For example, provide a button that is linked to your GPS navigation map. This could reveal your current location and the manageable route to the nearest gas station that you could make before you run out of gas, put on those comfortable walking shoes, and push.

## Drilldown and the Mobile Space

![](images/c916ba260049546ea89e8a291273c90b3011945863e4dcd59d312c929c92a909.jpg)

![](images/f9f55183385c0f5f2b1b47ac912c3bf8d9561d2747520fa14052df0a8fbef9d5.jpg)

![](images/1fcdc5dfdf810518d3c256d2a01310840a9f9bf540d6d6778e2b075c1c5d180e.jpg)  
Figure 6-2. Improved screens, processors, and input methods increasingly allow the use of naturallooking objects. These communicate their content and interaction organically, and so hold the promise of innate, learning-free use. They are not quite there, so design items like the Stack of Items carefully, and don’t be afraid to provide labels.

Throughout this book, we mention the importance of following a consistent information architecture to ensure a positive user experience across a device’s OS. In Chapter 5, you learned that it is important to design the interface to ensure that the user can effectively access this content because:

• Mobile displays are smaller than PCs, reducing the amount of information shown on a viewport’s current state. Common smartphones still (in 2011) have screen resolutions of 320 × 480 pixels. Many feature phones still have resolutions of 240 × 320.

• Smaller displays require larger buttons for gestural interaction, which, in effect, will reduce the amount of content that can be placed on the screen.

• On larger mobile displays that require the use of capacitive touch, interactive items cannot be as small as they would be on a similar-size computer with a mouse or comparable interface.

• The user’s finger and hand placement may occlude information during interactions, which may be much of the time the device is in use.

• Mobile screen real estate is so valuable that content and related features must be prioritized based on user goals and needs.

• A mobile user’s attention is competing with all the stimuli in the surrounding environment. Therefore, the access to the content must be detectable, even at a glance, and afford its function appropriately.

• There is a direct correlation between the size of the target, its distance from the user, and the amount of time it takes to select it.

Drilldown access also requires these considerations. But unlike lateral access whose information architecture is based on the same tier levels, drilldown is concerned with accessing related content based on hierarchical parent-child relationships, hence the name “drilldown.” You are accessing additional detailed information relating to the current content or the state of the device.

The fact that drilldown content is being accessed may appear directly on the state currently being displayed, or it may cause the user to jump around, whether within the current page or by opening a new one. If the user is required to access content on a new page, you must consider use of wayfinding principles to give the user an understanding of her current location as well as a clear path to follow back.

There are several reasons to use drilldown widgets across the mobile space:

• They allow the user to access more specific related content.

• They provide the user with visual cues that more related content is available.

• They allow the user to immediately notice the hierarchical relationship of the content.

• They allow the user to gain additional information, or change the state of the device, without removing himself from the original context.

Use of drilldown widgets affords the following benefits:

• They present immediate relevant information with a portal to access more specific content.

• They efficiently use valuable mobile screen real estate.

• They can allow for quick jumping to a specific section within the current page.

• They can provide additional surface information without removing the user from the context.

## Patterns for Drilldown

Using appropriate and consistent drilldown access widgets will provide an alternative way to present and manipulate content hierarchically. In this chapter we will discuss the following patterns based on how the human mind organizes and navigates information:

## Link

A selectable, content-only item that provides access to additional pages or content.

## Button

A distinct, visual element, within any context, that enables the user to initiate an action, submit information, or carry out a state change.

## Indicator

A visual representation—dual-coded with an image and text—that initiates an action and submits information similar to the actions of a link and button. See Figure 6-1.

## Icon

A clear and understood visual representation that easily provides the user access to a target destination or direct function.

## Stack of Items

A stacked set of related, selectable items that can be dispersed to reveal the contents, which provide further selection or access to each item. See Figure 6-2.

## Annotation

Reveals additional content details without entirely leaving the original display context. This additional content may also carry functionality.

## When to Use Links, Buttons, and Icons

Knowing when to use these types of drilldown widgets can be challenging to understand.   
Use this chart as a reference to guide you in that process.

<table><tr><td>Pattern</td><td>When to use it</td></tr><tr><td rowspan="4">Link</td><td>Use a link when a new page of related content must be loaded.</td></tr><tr><td>Use a link to jump to additional content within the current page.</td></tr><tr><td>Use a link to open a Pop-Up dialog containing relevant content.</td></tr><tr><td></td></tr><tr><td>Button</td><td>Use a button to initiate an immediate action.</td></tr><tr><td>Standalone</td><td>Use a standalone button to initiate an immediate action without additional user input.</td></tr><tr><td>In-conjunction</td><td>Use in-conjunction buttons with other user inputs or controls (radio buttons, spinners, checkboxes, etc.) to commit these user selections.</td></tr><tr><td>Delayed input</td><td>Use a delayed input button to interrupt the submission to request additional user data. A modal Pop-Up dialog will likely be used to retrieve this information.</td></tr><tr><td>Indicator</td><td>Use an indicator to initiate actions of linking, commit actions, and state changes. Use an indicator to visually describe the type of activity that will occur when initiated.</td></tr><tr><td>Content beyond</td><td>Use a content beyond indicator to visually explain what type of content will be loaded if the link is followed. This is typically an icon in front of the text label.</td></tr><tr><td>Type of action</td><td>Use a type of action indicator to describe the type of activity that will occur when the link is selected. For example, a“Refresh&quot;label can be accompanied by a revolving refresh icon.</td></tr><tr><td>Manner of action</td><td>Use a manner of action indicator to describe the way the action will be carried out. The icon should indicate that the action may go forward or backward in the process, opens a pop up, or performs some other type of action.</td></tr><tr><td>Icon</td><td>Use an icon to provide access to disparate items or functions, in a glanceable manner.</td></tr><tr><td>Fixed</td><td>Use a fixed icon to clearly explain, within the image, its function or target destination.</td></tr><tr><td>Status</td><td>Use a status icon to indicate a change with the current condition. This may be an external change such as the current weather, a system change such as inbound messages, or a user- initiated state change such as switching from scroll to select mode.</td></tr><tr><td>Interactive</td><td>Use an interactive icon to carry out a behavior directly, such as enabling WiFi. This icon does not provide immediate access to any target application, site, or information.</td></tr><tr><td>Stack of Items</td><td>Use a stack of items when information can be represented as thumbnail graphics, and all items in the group appear in a virtual stack which can be shuffled or expanded.</td></tr><tr><td>Annotation</td><td>Use annotation when more information should be presented for an item in focus, such as a pinpoint on a map or chart. An annotation is smarter than a tooltip, and may offer links or actions.</td></tr></table>

## Link

## Problem

You must provide a function to allow access to related content, from arbitrary locations within a page.

The Link is a very common action element, available in one way or another on every platform.

## Solution

![](images/91a3d985dc485fb858fdea535c44a2a58a6d67cc324f83bcae7af2062b42afc3.jpg)  
Figure 6-3. Links are clearly differentiated from the text in which they appear, and cannot be confused with any other text styling.

Links are simple, textual interactive elements which provide access to additional information, generally by:

• Loading a new page of content

• Jumping to the portion of the current page which carries the additional content

• Loading a Pop-Up dialog with the relevant content

• Revealing an adjacent page using the Film Strip pattern

Links are almost purely hypermedia elements. Although links were not invented by the Web and are not exclusive to it, the ubiquity of websites and links can serve as a good guideline for display standards and use of the pattern; your users can have a single understanding of the OS, applications, and the Web if consistent methods are used.

Links are generally found in content-rich areas, as shown in Figure 6-3, when used in application or OS contexts. Links to additional information within explanatory text, or for cross-referencing within help systems, are common uses outside the Web. Most other text found within an application or OS will be labels for lists, icons, buttons, and so forth.

![](images/586a0ba932ed7d8e1fb002c42f12e52137de3113e0118c1b818435c37cd297b2.jpg)  
Figure 6-4. Hover states must be indicated by a change in the link, usually a color change. The change is an important indicator that the correct item will be selected, as well as that it is indeed an active item. Visited items may also indicate this condition with a change in color, exemplified here with the word “Button.”

Links alone are rarely suitable for these situations, so this chapter discusses numerous interactive methods you can choose from for your specific needs.

## Variations

There are no true variations of the link. Links may be found anywhere on the page, and are differentiated from nonlinked content with a change in color and underline (for text), or a colored border (for images).

Other text which must function as a link should be the label within a Vertical List, have an associated Indicator, or be the label for an Icon or Button.

## Interaction details

Links can be selected by pressing the “OK/Enter” key while in focus (for scroll-and-select devices), or by tapping directly on the link text for pen and touch devices.

Be sure to support focus states, or hover, by changing the link color as shown in Figure 6-4, or possibly the text style. Of course, this will only work for devices which support hover, or focus-without-selection. Pen and touch devices generally do not have this capability.

![](images/e1df664a8085e24e4f1a4c8a3f853d6b01ee1c14fa012fe1d1c8433d37a7ef9d.jpg)  
Figure 6-5. Additional information about a link should be presented immediately after the link text, and not as a part of the link. File types and size may simply be text, as shown here. Use an icon or the name of the provider (if short) for content that will load a new application or leave the site.

Inline links should always be a different color from any styled text. Whenever possible, they should also be underlined, but be sure to follow the OS standards. Simply using color can be confused with style and not perceived as a link. If needed, dotted or dashed underlines, or slightly desaturated color, can be used to reduce the visual prominence of the underline.

Some systems will use highlighting (a field of color behind the whole link text) instead of an underline. This is easy to see, and you should follow it if it is the OS standard, but some users may not immediately understand the meaning.

Underlines should never obscure descenders. Underlines must break, or otherwise integrate cleanly and clearly. If they don’t, pick another typeface.

For most inline-style links, the color of the link should reflect the current condition:

• Nonvisited

• Visited

• Hover (when available)

• Active (mouse down)

In certain cases, the visited state is of no significance. If the information is dynamic, or the entire experience is used so that all links would be “visited” on a typical viewing, that state may be disregarded.

Links in lists use their position in a list, as a series of repeated items, to indicate that they are selectable. To avoid excessive horizontal rules (the separators for the individual line items), you usually should not underline links in lists.

The title for each link should be unique, clearly communicate the information on the target, and be easily scannable.

Additional information, in text or as a graphic, should be included after the link to communicate when an atypical target is presented, as shown in Figure 6-5. When a link leaves a site, loads a new application, or will initiate a file download, indicate this. Since normal links do not have icons, any reasonable icon after a link will usually be interpreted correctly. Text following the link should display the file size of downloadable items, and the type of file, such as “(384 kb PDF)”.

Linked images should be bordered with the same colors as text links, when no other communication is available. When possible, add a description of what will happen to the image, or add a descriptive text link immediately adjacent to the image. Avoid use of simulated text or buttons in the image; the lack of interactivity (such as hover or active states) may confuse users.

![](images/cbdeccbb04a0a47ea86f5551688b94fd3c532016464991461db6b3e47de67146.jpg)  
Figure 6-6. Do not use repeated or unnecessary prefixes, such as “Click here” or “Download,” as shown. Additional information, such as file types, should not be part of the link text. Compare the scannability and readability of this with the example in Figure 6-5.

Do not use links to activate functions. Even within a web page, use buttons and other form elements for action behaviors.

Avoid using generalized text such as “Click here.” Such text is not meaningful, and makes the content hard to scan for the relevant information, as shown in Figure 6-6. Especially in lists, try to use unique but descriptive phrases. Rather than “Click to view the manual,” simply use “View the manual.”

Do not use underlines for any other elements on the page, such as for emphasis. Userdefined styles may still be allowed when editing text in word processing programs, of course.

The Link pattern defines behaviors for the linked text only. Do not change the background for an entire row or other container in which a link occurs or this will become another type of pattern.

Avoid changing the type style for link condition changes, such as hover. Switching to bold, except for a small number of typefaces, will make the text wider, causing strange jumps, confusing the user, and perhaps causing the page to reflow. Other changes may be suitable and appropriate, such as switching from a dotted underline to a solid.

## Button

## Problem

You must allow the user to initiate actions, submit information, or force a state change, from within any context.

The Button is probably the most common element across all mobile devices, and is built into every platform.

## Solution

![](images/753cfe8cadcfb01474c37a6090732b1a241bbb0e2b4ffb699771f95caca5fe4f.jpg)  
Figure 6-7. Buttons are used in conjunction with input fields and selectors. The button submits or commits the selections. When fields or selections are required, a good way to avoid error messages is to disable the submit button. Be sure to label this condition so that users are not confused by it.

Use a Button to initiate an immediate action. A button is not simply a “more important” Link, and should not act as such. Button-like action behaviors may be initiated with an Icon and label pair, if space or other layout or style considerations require it.

## Variations

Standalone buttons will perform an action, or change modes immediately. They will also do the following, with no additional user input:

• Switch from email list view to composing a new message.

• Begin to synch email with a remote server. Click again to stop the process.

In conjunction with radio buttons, checkboxes, or any other user inputs or controls, a Button will commit these user selections; see Figure 6-7. Within websites, buttons are used to submit (or cancel submission of) forms to remote servers:

• With a text field, the Button submits a search.

• With radio buttons, the Button sets the USB connection mode.

• With a set of Mechanical Style Controls, the Button saves changes to the time of an alarm.

Delayed input interrupts the submission to request additional user data. Usually, a modal Pop-Up dialog will be used to retrieve the information. Ellipses follow the text label of the Button to indicate the process will continue, such as:

Share via:

• [Bluetooth…]

• [Email…]

• [SMS…]

• See the Exit Guard pattern for some related examples.

## Interaction details

![](images/6ff6287bb5c3a637c0813576abd8e1a30dde6d563c79c80a2d1797d7c16802a1.jpg)  
Figure 6-8. Buttons may be combined or grouped with icons, which should then be of similar vertical height, as though they are related buttons. Consider the Page design carefully when placing buttons. For certain types of applications, you should place buttons at a regular location on the page or even in an area such as a Fixed Menu

Depending on the action, after the user selects a Button, the page may or may not change. If there is no change (such as with the earlier synch example), you must make the button change state to indicate the process is ongoing, or change the label to the reverse action (e.g., “Cancel Synch”).

Users may select buttons by pressing the “OK/Enter” key (on a five-way pad) when the Button is in focus or by tapping directly on the Button for touch or pen devices. In many cases, especially in Pop-Up dialogs and full screens where an action is key, a button should be in focus by default so that no scrolling is required.

When user entry is required (for in-conjunction buttons), until sufficient entry has not yet been made, the submit action should be made inactive. This should be communicated with text adjacent to the button.

Presentation details  
![](images/6b87815f588232054fcdc3962130fe9a6fa3226395480956dfa13159c16d46c6.jpg)  
Figure 6-9. Graphical icons can be used to support the messaging of the button.

Buttons must be very easy to see and activate (especially for touch/pen devices). Background color and contrast must make the button stand out from the page background appropriately. Remember color-deficit users and glare, and make sure the text on the button has sufficient contrast to be readable.

Buttons should usually be about twice the height of the default page text, to provide room around the label. Smaller buttons can be used for less-important or less-used items, but they should never be smaller than about 120% of the vertical size of the smallest text. Consider click target sizes for touch and pen devices, and do not make selection areas smaller than 10 mm.

The width may be fixed, or it may vary based on the size of the text. Try not to have too much empty space. Vertical size must be the same for equivalent actions, as in Figure 6-8. An “OK” and “Cancel” pair, for example, must be the same vertical size even if you change the width to save space.

Buttons should generally appear to be raised above the page slightly. When a button is selected, it should appear to have been pressed and be level with or below page level slightly. Buttons are momentary-contact items, and this activation display should cease when the user click action ceases.

For scroll-and-select devices, the button in focus will have a thicker border or other indicator. Inactive buttons must be indicated by being grayed out. Be sure to select a sufficiently saturated background and high enough label-to-background contrast that graying out is clear.

Use the writing style already defined for the rest of the OS, your application, or your site. Be consistent with capitalization in all buttons. Be clear about terminology, and avoid labels that require reading. Rarely should buttons say “Submit” or “OK.” Descriptive, freestanding labels such as “Connect” are always better.

For additional clarity, consider using icons inside the button, as in Figure 6-9. Use the most obvious graphic possible, with multiple encoding (e.g., a green check for submit and a red X for cancel). Generally, graphical icons should be to the left of the text, but if direction indicators are used, place the icon to the side indicated.

If graphics are not supported, or cannot be relied on (as with low-end web applications) for your platform, you can use text entities instead. The following table shows a selection of reliable ones.

<table><tr><td>Icon</td><td>Typical use</td><td>Entity</td><td>Decimal</td><td>Hex</td></tr><tr><td>④</td><td>Add</td><td>&amp;oplus;</td><td>&amp;#8853;</td><td>&amp;#x2295;</td></tr><tr><td>⊗</td><td>Cancel/remove</td><td>&amp;otimes;</td><td>&amp;#8855;</td><td>&amp;#x2297;</td></tr><tr><td>√</td><td>OK</td><td>&amp;radic;</td><td>&amp;#8730;</td><td>&amp;#x221A;</td></tr><tr><td>⇐</td><td>Back/previous</td><td>&amp;lArr;</td><td>&amp;#8656;</td><td>&amp;#x21D0;</td></tr><tr><td>⇒</td><td>Continue</td><td>&amp;rArr;</td><td>&amp;#8656;</td><td>&amp;#x21D0;</td></tr></table>

Naturally, more common items such as “<” or even normal characters such as “+” can be used as well.

## Antipatterns

Carefully consider whether a series of buttons should be used to make a choice. A more suitable solution is often another type of selection (such as radio buttons) with the Button used to commit the selection. This also allows adding other behaviors, such as a checkbox to indicate that the selection should be the default from then on.

Avoid making the default button perform an unrecoverable, destructive action. Users must make deliberate choices instead. See the Exit Guard pattern for more on this behavior.

Avoid color schemes that can be misconstrued as being grayed out and inaccessible. Likewise, avoid grayed-out states that are so well designed they look like they are just attractively gray buttons.

## Indicator

## Problem

You must allow the user to initiate actions, submit information, or force a state change, from within any context.

An Indicator is simply a link with an adjacent graphic (or text icon). It can be easily implemented on any platform.

## Solution

![](images/4a64062bad2c6385d81b90c12ccee9b0d42ad4646cc2e670fd579caf5d6c93fc.jpg)  
Figure 6-10. Indicators are text labels with graphics used to indicate that the item is selectable, and what it will do. This pagination example uses arrows to emphasize the “previous” and “next” actions. The icon on the page location indicates that it is also a link, allowing direct access to page controls.

The Indicator pattern, as shown in Figure 6-10, is a type of action initiator between a Link and a Button. You always use indicators with text labels, and they may perform any action: linking, state changes, and commit actions.

There is significant overlap between these three patterns, and the Icon pattern; in some cases deciding which to use depends on consistency and style.

You can use this pattern to express a hierarchical relationship between items. The Indicator would be considered more important than a conventional underlined Link and less important than a typical Button. Use caution with this, and try to use parallel controls for similar types of actions as much as possible. See the Button pattern for some additional discussion of this.

![](images/5aebf2fbe98393e07b326628e2675f5f4c300bd118b3007a0efa47240adf24af.jpg)  
Figure 6-11. Icons in the call history list on the left are used to denote which phone type was used; selecting the item will dial the indicated number. The same list on the right has no direct actions, but will load additional details for each number as indicated by the right arrows to the right of each line item.

Indicators are expressed in a limited number of ways, but can indicate three different types of meaning:

## Content beyond

Explains what type of content will be loaded if the link is followed. This is typically an icon in front of the text label. Examples are the file type (e.g., Acrobat, Word) or types of objects to be viewed (e.g., photos, videos).

## Type of action

Describes the type of activity that will occur when the link is selected. This will usually reinforce the wording, instead of adding additional information, to assist with glanceability. For example, a “Refresh” label can be accompanied with a revolving icon indicating either a reload or a refresh.

## Manner of action

Describes the way the action will be carried out. This is typically in addition to the label, and so adds to the description. The icon should indicate that the action goes forward or backward in the process, opens a Pop-Up, or performs some other type of specific action.

All of these are shown in the examples in Figure 6-11.

## Interaction details

There are few special or innovative interaction methods available for this pattern. The text will be selectable, usually in the exact same manner as the Link.

Whenever it is technically feasible, the indicator icon should also be selectable. As long as the text label indicates focus, on hover-state interfaces, there is no need for you to make the icon change also, although you may if it would assist in clarity or improve the interactivity of the product.

Presentation details

![](images/05dc80beaa40006c36a68366924b8fe951592850c8f0e0a3532a7a607146a857.jpg)  
Figure 6-12. Indicators can be mixed with pure icons, links, and buttons. Use labeled indicators when an icon may not be clear enough, or a text link would not be immediately scannable.

Indicators are almost entirely associated with text; even when the text is positioned alone, or as a part of a list, the graphic should be inline with the text, and therefore immediately to the left or right of the text.

Which position is used will often carry meaning, and so should be carefully considered. If the function is “forward” or “next,” for example, the Indicator icon will be facing to the right. It may be a good idea to place the indicator to the right of the text in this case. The “next” and “back” indicators used alongside text labels in the Pagination pattern are a good example.

Graphical icons are the most common type of Indicator used. When used without a text label, or when the icon becomes the most prominent item (with text supporting it), this becomes an Icon pattern instead. For the Indicator pattern, the supporting icon should not be much larger than the vertical height of the text. See Figure 6-12 and the associated patterns to combine the interactions in one space.

For use of the Indicator in lists, also compare it to the Thumbnail List pattern.

Icons may be of any style, but like the text, they must be consistent and must match the brand and other design guidelines of the site, application, or OS.

Indicator icons may be special text characters, when working in constrained environments. See the list in the Button pattern for some useful, universally available text items. If special typefaces can be loaded, you can use more interesting text icons, often with great efficiency in space, speed, and complexity of the code.

## Antipatterns

Avoid placing indicators above or below the text. Centered below the text, for example, may appear to be the most space-efficient location, but in fact is likely to be perceived as on another line, and either nonsensical or associated with other items on the second line. If this layout is needed, use an Icon instead.

Do not use an Icon or Indicator just to be consistent, or to add visual flair. Ensure that all indicators are accurate, are truthful, and clearly explain their purpose.

Do not use indicators with a clear meaning that they do not actually carry out. A common error is the use of the right arrow to mean “more” when the specific item loads as a Pop-Up, or loads a new application entirely. This should only be used when a “next” page is loaded, preferably by visibly sliding in as a Film Strip item.

## Icon

## Problem

You must provide access to disparate items or functions, in a glanceable and easy-to-select manner.

Icons for selection and display are common, and will be easy to implement on all mobile platforms.

## Solution

![](images/7d453f897f504b6fb8771374cf33cdcbaa059835c5421753fa27489053d4da28.jpg)  
Figure 6-13. Icons are used as shortcuts to highly used items, even within interfaces that are otherwise not icon-centric. This is a typical idle screen for previous-generation smartphones and many current feature phones.

We have used the word icon throughout this book to denote graphical representations of functions or destinations. Here, an Icon can be considered to represent an “Iconic Link,” and differentiates itself from other related drilldown items such as the Indicator link pattern because the icon part is the most prominent item.

Well-designed icons serve as an easily understandable, easily recalled representation of an action or target destination, such as a website or application. They are particularly suitable for Home & Idle Screens, when used as full grids of icons and as small lists of key applications on a more general-purpose idle screen, as shown in Figure 6-13.

Icons are most often encountered as the elements in a Grid, as in Figure 6-14, but you can also use them in other ways, such as in a Carousel when used as part of the page (and generally without 3D effects), for a Fixed Menu, for certain types of Tabs, and many other presentations and interactions.

Variations  
![](images/13a6d231f731ae0db0d9498cdfb4f1efaf42ae1991b6f1fe598c8b17381a22ce.jpg)

![](images/386be845a821df2b2464738c45f3bdc8f161f4311fc4ab28300ccdfb46b248a9.jpg)

![](images/d073074302d957188f3f28d0f6ae50a5c876ec0559ecb41221492b83a7e3c02f.jpg)  
Figure 6-14. Several ways to use icons in a grid, for idle or menu screens. The righthand example includes interactive icons as well.

There are several types of icons, with varying degrees of interactivity.

Fixed icons are composed of an image of the function or target destination. The icon must clearly explain the function or target and not be lost in the background or in other page elements, or be easily confused with other icons.

Status icons change with the current conditions, as shown in Figure 6-15. This may be the result of an external change such as the current weather, a system change such as inbound messages, or a user-initiated state change such as switching from grid to list view.

This change can take any form, but the fixed icon must be preserved as a recognizable basis at all times. Typical methods to accomplish this are:

## Overlay

A brightly colored or highly contrasting badge overlapping the corner of the icon may denote a condition change alone, or carry embedded messaging such as a count of new messages.

## Color or contrast

An existing part of the icon, or several parts, can change color or contrast to represent the current condition indicated. More than one element can change. This is typical of status messages, such as the degree of brightness.

## Change

The basic icon or icon background will remain the same so that it can be recognized, but an element will clearly change. This may be as simple as a cartoon character’s eyes closing to indicate that the service is “sleeping,” or as complex as displaying the current weather conditions and temperature.

Interactive icons have functionality themselves, and do not provide immediate access to any target application, site, or information. Selecting the icon will carry out some behavior directly, such as changing screen brightness or enabling WiFi, as in Figure 6-16. You can even combine these with status icons to provide a way to view more information in the same space; a tap will reveal another icon’s worth of information. Tapping an icon with the current weather iconically could reveal numerical information on temperatures and rainfall.

These types of icons are a subset of the subscreen interactive element known in some circles as widgets, but this word has other meanings, and in this book we use one of those.

## Interaction details

![](images/dd41f5462d6e1a123ef2e72b97bd2fb467568aafadc1675c50ecd02c0da6fe16.jpg)

![](images/92d32c3e74ff8341c29e1a77607a777b4703b081d7c740d99fec2ba0258029f2.jpg)  
Figure 6-15. Simple fixed icons (left) can have status information, such as the notification of five new messages to the right, simply laid on top.

Most icons will load an application, website, settings panel, or detailed information of some sort when simply selected or clicked on. For scroll-and-select devices, the focus condition is indicated but has no other interactive behavior. Feedback should be provided by any other available methods, such as Haptic Output, when available and enabled.

When using an interactive icon, you must immediately display a change and provide any other relevant feedback. If the actual state change will take time, such as enabling WiFi, and taking time to power up and find a network, provide some sort of interim condition before the “on” condition is switched to. These will usually take the form of a small Wait Indicator.

If additional information or settings are available for an interactive icon, double-tap or Press-and-Hold behaviors may be used to provide access to these screens.

Some types of status icons will also not load a new page, but will simply change the state and indicate this immediately by the Icon changing state. Any other state changes, such as a mouse pointer or cursor changing state, must occur at the same moment as the Icon.

Status icons may also behave as normal, fixed icons, displaying current conditions but loading the target page when selected. For example, a calendar icon with the current date and an overlay with the count of remaining appointments is very much a status icon, but selecting it simply loads the calendar application.

Presentation details  
![](images/66f4aea5a80875e321a7af660617f2d06baac614d648037e298bdbdbd3ba5a77.jpg)

![](images/cc7cfdd54db4d8bc821d026fe52a316e4e2c4010d5f6c17230cce4f17c10a991.jpg)  
Figure 6-16. Interactive icons must immediately appear to be interactive, with clear controls and an obvious indication of the state change.

The design of icons is an entire topic, with entire books dedicated to these principles. There is very little difference between the use of icons on desktops, kiosks, and workstations over the past several decades, and their use on mobile devices. Do keep in mind typical mobile requirements such as visibility in all lighting conditions, or under movement.

All your icons should be very similar in size to one another. You may have to follow existing standards, but if you are developing the framework, try to restrict what sizes can be used. When you are making icons for your application, follow best practices for the platform, even if it is not technically restricted.

Icons should generally carry a text label. This will usually appear centered, below the icon, and should not wrap to a second line. Labels to the right or left of the icon will often fall into the Indicator pattern instead. In certain cases, it may work to have the labels truncate instead of taking up additional room. When the icon is in focus, the label may “marquee,” or scroll, to reveal the entire label.

Functions should imply the functionality. Switches, buttons, and other actions contained within the icon should have 3D effects or look like standard on-screen controls. Use formlike controls (e.g., radio buttons) or simulate Mechanical Style Controls, such as switches and buttons. Indicators often work best with shadows and simulated bleed and glow effects as well.

## Antipatterns

Avoid automatic thumbnail or Avatar images for icons. One web page or person will look very much like another at thumbnail size, and a key part of icon design is the design of the outer bounding shape. These may be used in a Thumbnail List and other places where the image supports a text label, but they are not generally suitable for icons.

Information in an icon that looks like data must be real data. Do not, for example, make an icon for a calendar or clock with fixed values for the date or time. Use the status icon style and indicate actual data, or use another icon style.

Try to label each Icon, in all conditions; even if you use them in a carousel, where additional information may be presented with the in-focus item, use short labels for each visible icon whenever possible. Not all icons are clear on first use, so users will have to take time to bring each item into focus before selecting anything.

## Stack of Items

## Problem

You must display a set of closely related items, which can be represented as icons or thumbnails, in a manner implying the hierarchy and providing easy display of the contents.

Rotating and moving images, especially smoothly, requires relatively powerful or specific graphics processing, and will not be available on all platforms. Ensure that you have the technical capability before designing such an interactive method.

## Solution

![](images/4010d8563d5125e07aa95336f6d334659400d6e8cd89aebf88d8a775bb154d44.jpg)

![](images/08e6bffc4b119a17e9a763474071533250cf20f087259e0a45bc1d2da5c86922.jpg)

![](images/afbee27cd5d1cce2e1f4d9502a23e3e723a7a1e8c1aea1b29e736c865a2f69da.jpg)  
Figure 6-17. The “Photos” stack in the left frame is tapped, and the thumbnails move into their final Grid positions as the page behind changes. Note the title changes and the processing icon in the title bar during the transition, as well as the importance of the labels below each stack in this example.

A Stack of Items is a design pattern that is exactly as it sounds. A set of thumbnails are arranged so that they appear to be actual items, such as a pile of photos stacked on top of one another. Only the top one is completely visible, but to make the stack clear, others stick out from the sides. Selecting the top item opens the stack, revealing all the thumbnails and providing further selection or access to each item. See Figure 6-17.

The concept of drilldown for the Stack of Items inherently encompasses two tiers of the hierarchy, instead of only the usual one tier. Opening the stack to reveal the images within is one, and clicking the linked icon to view the image details (or otherwise load the target state) is the other.

At first glance, this pattern appears to be a graphical variation of the various expanding folder views such as the Hierarchical List, and should therefore not be used in favor of the simpler, more common display methods when they will do fine.

The difference is the content; for list displays, the primary displayed item is text, and any graphics are supporting only. With a large collection of images (or similar, graphically representable content), if drilldown is required, use a Grid display using Icon thumbnails of each image to open folders, or use the Stack of Items if the platform will support it.

## Variations

Two basic interaction and display paradigms exist for all interfaces like this:

• The transition from stacked to open takes place on a static screen, without a transition to another space. This requires space for the stack to open into, or that other items on the page move out of the way. When folded, these items may or may not move back to their original position. This is the least common method used.

• The transition from stacked to open takes place at the same time as the underlying page changes. When folded, the stack may be in a relatively constrained area. The unfolded state may then occupy space as it needs, as the available space is dedicated to it. The page transition is obscured behind the stack that is expanding; the user simply will not notice it happening.

The Stack of Items pattern is still relatively new in production devices, so it has not established many common variations. It has been well used in many prototypes, and in large-scale touch devices (such as the Microsoft Surface). If your application is capable of supporting such a pattern, try to take time to explore alternative methods of using this pattern that may tie to others. For example, if sensor-driven tilt is used in the Grid display of items when open, it may be useful to enable tilt when stacked, either for viewing or as a method to open the stack. For other ideas along these lines, see Simulated 3D Effects.

## Interaction details

This pattern represents a simulated physical set of objects, so even with simple tap-only behaviors, it is really most suitable for touch and pen devices. Consider the complete experience carefully before including it in a purely scroll-and-select interface.

Simple selection of the stack (such as a tap for touch and pen devices) will open it and initiate the transition to the expanded state. When you use it with scroll-and-select devices—or the scroll-and-select interface of a mostly touch device—you must include in the highlighted state the entire stack, including the thumbnails that are “sticking out.”

Other interactions—such as drag to fan-open or certain kinesthetic gestures—should only be used if similar gestures are commonly employed in the rest of the OS.

While the stack is unfolding, do not allow selection of individual cards. This will prevent accidental input from the user trying to chase moving items. Do not disable any other functions. Selecting the “back” or “cancel” button (or gesture) will immediately stop the unfold action and reverse the animation to the closed state.

If room allows, place a Wait Indicator in the title bar or other location to indicate this condition; the system may become occupied, or lock up, and this will help to explain the temporary loss of input.

There is no organic provision for collapsing an unfolded set of thumbnails. You must use the device’s default “back” function, or place a dedicated on-screen control, on the screen or as a part of a Fixed Menu or Revealable Menu.

## Presentation details

Show each item that unfolds as a thumbnail. When collapsed, the stack will look like a physical stack of cards, occupying a space only slightly larger than the top thumbnail. Shadows and other effects (as long as they do not interfere with viewing the thumbnails)

should be used to emphasize this. The edges of individual items should be clear in all cases, to assist with differentiating the images from the background. This helps to imply that the items are selectable and not just decoration or parts of the background.

When stacked, the cards should look like a stack, though a messy one, with some cards sticking out from the edge in some manner. Never fold them up so far that only the top thumbnail is visible. The top item in the folder (using whatever method is relevant for the content type) is used as the label for the stack. Sometimes you may want to allow the user to select which item serves as the label or badge for the stack, but generally it will have to be automatically generated, and so may not represent the contents. Be aware of this as a possible pitfall.

Put a text label under the folded stack, as described in the Icon pattern. Individual thumbnails may or may not be labeled, depending on their relevance. Critical differentiators (e.g., video or still photo) may be indicated with icons laid on top of the thumbnail.

## Antipatterns

Do not use this pattern if it cannot be built to operate smoothly and responsively on all the targeted devices.

As with all such simulations and effects, avoid overusing or misapplying this pattern.   
This may result in an unusual interaction, which could be perceived as nonstandard.   
Therefore, ensure that it adds value when used.

Do not use a generic icon/graphic to describe the stack (e.g., iPhone grouping); be sure to indicate it’s a folder very clearly.

Do not present a Stack of Items that simply reloads the page as a Grid. The unfolding action should always be animated to show the thumbnails moving from the stack to the final display location.

## Annotation

## Problem

You must be able to attach additional information to a data point within a dense array of information, without leaving the original display context.

Any interactive infographic that demands such additional information can generally support an Annotation. Layered display is easy to add to almost any platform, but some attention must be paid to precise location ability when used in Infinite Area and similar displays.

## Solution

![](images/9a870b54f4146786f4a0c9a092e43c494d69f986e513c2d3ae9a217b8d3b590e.jpg)  
Figure 6-18. A typical example of a reveal label. When it is originally selected, a small pointer indicator is used alone. When it is selected further, a label with details is revealed, as shown to the right.

High-density information displays, such as maps, charts, and graphs, always carry additional layers of information, which may be best understood by allowing the user to view certain details about a specific point. Conventional methods of drilling in deeper, such as the Link or Button, are unsuitable for finding out about a specific data point, partly because they remove the user from the original context.

Instead, you can employ a special type of widget, exemplified by the pinpoint. An iconic element points to the information selected, and presents (sometimes only after further selection, or in another area of the screen) a label and additional options.

Do not confuse this with a Tooltip. A deliberate action is required to reveal the information. Tooltips, instead, are transient and are initiated by hover or are automatically presented when the system determines the user needs help.

Content within an Annotation is instead discrete information, or may even carry functionality, and is not simply help or explanatory text as in a Tooltip.

## Variations

![](images/9ce1f0d08c6ff10694a66509b2e65167de45701c3e26f8f92862c35d5a735cea.jpg)  
Figure 6-19. A banner attached to the edge of the viewport can also be used as a label. This is most useful for large amounts of information, which would otherwise clutter the display to the point where it would not be seen clearly.

There are numerous ways in which you can make the selection of an item reveal additional details, without entirely disregarding the original context. Many of these, such as split-screen variations, are not yet common enough to be considered patterns, but these three are very common:

## Fixed label

When an area is highlighted by the system, or selected by the user, a label bearing text and/or icons is displayed as a part of the graphic pinpoint indicator.

## Reveal label

When originally selected, either by the user or by the system, a small pinpoint indicator is placed, as in Figure 6-18. This is usually generic, and often has no label, or a very simple one such as a shape, color, or single letter. When the user selects the pinpoint again, it will expand to reveal a larger label. In this mode, the label is functionally identical to the fixed label.

This is especially useful when multiple pinpoints may be needed, such as graphically represented search results. The small label can carry an identifier such as a letter, and the user may then subsequently select details on any individual result, without as much clutter.

## Banner

A small pinpoint indicator is used to mark the location on the data array, as in the reveal label. At another location on the page, usually a strip anchored to the top or bottom of the viewport, is the label text, or graphics, as in Figure 6-19. This is most suitable when a large amount of data must be presented, or a number of selectable options should be selected. In this case, the style and functionality of any Fixed Menu or Revealable Menu used within the OS or application should be carefully considered, and may be reused without modification.

You can use any of these three options in conjunction with one another, within a single interface. For example, when single selections are made, the fixed label is used, and for search results, the reveal label.

## Interaction details

![](images/cc52e7ce6dc18d765b1b83eb60e6f4154746b33edd3e803d3ee068d03ee0d4aa.jpg)  
Figure 6-20. Annotations can be used in nongraphical data sets, such as charts or, as shown here, to provide options for selected text. This also exemplifies how multiple selections may be made within a single pinpoint label.

Selection details are simple and mostly outlined in this pattern’s “Variations” section. Note that the selected information set can be of any type, including maps, graphs, charts, tables, or text, as shown in Figure 6-20.

In some cases, reveal labels may convert from the small to large display when hovered or when the item is in focus, instead of by explicit selection. This is, of course, only suitable for interfaces with a focus separate from selection, such as scroll-and-select and certain pen devices.

When more than one pinpoint is visible, use the reveal label or banner style, and only display the label for the item in focus. This also serves to simplify selection of options from any other menu systems that may be present in the application.

When a reveal label is expanded, make sure it gets out of the way of other actions the user might request. If a selection is made somewhere else on the page, especially somewhere adjacent to the label, it should disappear and revert to a pinpoint only.

Presentation details

![](images/f6a329c77f69e309cb6a3974291b01c502123bb865c3d9684304ebab3c35d0ca.jpg)  
Figure 6-21. The type of pointer used must be selected to comport with the data being indicted. The expanded label can be quite far from the content being pointed out if the indictor is extended properly. Here, a one-dimensional scrolling graph has a pinpoint that indicates a position on the horizontal axis. The intersection point on the graph could have been selected instead, if this is the only data shown on this date.

Pinpoints must be easily selectable. For touch or pen devices, follow best practices for the size of the pinpoint.

For scroll-and-select devices, the pinpoint currently in focus must indicate it is selected, and must clearly differentiate this from any nonselected pinpoints.

The pinpoint must clearly indicate the location in the data set referenced. Use appropriate selection methods:

• Pointers for two-dimensional coordinates

• Lines for positions on one-dimensional graphs, as in Figure 6-21

• Highlights for text, or fields within charts

Pinpoints and labels must clearly indicate that they are not part of the page context. Use borders, shadows, and transitions to make this clear. It is often best to make it appear as though the pinpoint is floating above the image or protruding from the page. You can use certain practices described in the Simulated 3D Effects pattern to emphasize this.

When only one item may be selected, be sure to not imply that there are multiple options, by offering a Button or underlined Link separate from other selectable items. If needed, to clarify the click action, a false button (or link) can be added to the area, as it might be used in Advertising.

## Antipatterns

Labels should never exceed the space available. Do not let them simply float off the page. Label text should not end in ellipses or wrap to a second line. Multiple lines of information may be displayed, but each line should carry its own information.