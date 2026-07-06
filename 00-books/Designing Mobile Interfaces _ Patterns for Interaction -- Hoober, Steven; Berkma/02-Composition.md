# Composition

## A Little Bit of History

To many people the year 1440 signifies a major shift in global communication. It was during this time in Mainz, Germany, that a goldsmith by the name of Johannes Gutenberg invented one of the most important industrial machines of the modern period: the printing press.

The printing press’s use of movable type was inspired by earlier uses found in China and Japan as early as the 7th century. During this time, printers used a method of block printing, which involved a carved piece of wood used to print a specific piece of text.

Further advances took place in the 11th century. A Chinese alchemist, Bi Sheng, invented a process called movable type. His process consisted of having individual Chinese characters carved on blocks of clay and glue. These blocks were arranged on a preheated piece of iron plate where they were pressed on paper. Bi Sheng’s process was not without limitations, however. The process was slow and was not advantageous for large-scale printing, and it relied on clay blocks, which created problems with the adhesion of ink.

## A Revolution Has Begun

Gutenberg’s invention advanced the process of movable type further, and consisted of individually cut or cast letters, sorted onto composing sticks, locked up into galleys, and then inked and impressed into paper. This, the invention of modern typography, marked the birth of mass printing. It allowed information to move from merely permanent and portable to the first mass-media product. It allowed for perfect replication, standardization, and affordable books for the middle class.

## Composition Principles

![](images/8b9d1e1ef35eb11857f0de30524bd126b0bf513e40386e531009c5315499875a.jpg)  
Figure 1-1. Just some of the variety—and similarity—of Annunciator Rows, Notifications, Menus, and other device-wide features built into mobile device

The invention of the letterpress not only allowed for mass production of existing content, but made it so easy that there was demand for more content. And with that content was a need for well-understood page composition principles, not just those handed down secretly by cloistered monks transcribing old works.

So composition became a process of assembling a layout that consistently arranged components and content on a page. These rules were repeated on all other pages, creating a recognizable system of component relationships that were understood by social reading norms.

This helped readers to understand why a composition element was arranged within a specific part of the page. Readers could then expect to find that same element on all other pages within the rest of the book.

These composition principles made books usable for the first time. Mass consumption meant the addition of scientific texts, and reading for entertainment, and portable books that could be read anywhere, by anyone. Literacy rapidly grew as well, from less than 30% to more than 90% in the 20th century. Users adapted to the technology as much as the technology adapted to them.

As type principles became standardized, so did binding, type and page sizes, and then margins and gutters. Page numbers, titles, and chapters on each page followed over time.

These standards became promulgated as best practices, and were implemented as grids (to which everything was aligned) and templates, which were used on every page to make volumes feel like single works.

Using templates is essential in mobile design. As designers, we want to create our layouts based on cultural norms of reading conventions and how people process information. We also want to create information that is easy to access and easy to locate. Our users are not stationary, nor are they focused entirely on the screen. They’re everywhere, and they want information quickly and to be able to manipulate it easily.

## The Concept of a Wrapper

Throughout this book, we discuss patterns from which you can make the very specific templates that you can use for any particular product or project.

The templates that are used across a product, on most every page of a website or application, we call a wrapper because they enclose (wrap around) all the other components and the content.

Considering design from the wrapper down allows:

• The designer to organize information within a consistent template across the OS

• Information to be organized hierarchically on a page

• The user to identify the organization structure, quickly increasing learnability while decreasing performance error

Grids are also important to consider in design, but they are unique to each project and are beyond the scope of this book. They are discussed in many general design books and web tutorials; if you are not already familiar with the principles, you can use print or desktop web principles too.

## Context Is Key

![](images/11e4a9958d977d78d6fd1be3426400532918e75ebda85f8fb7c9ad12b4ba6db1.jpg)

![](images/a49d8fab815d15280591e91303a904a4909bd833334ad9c524fd76d74a97e32e.jpg)

![](images/534c74d163abe6976359c619a5fc2034685ccab579d6e1e8827207a91978be4f.jpg)  
Figure 1-2. The lock screen on this device is as informative in presentation, and gestural in interaction, as the rest of the experience. Even notifying the user of an error on entering the code is organic to the design. Apply your interface and interaction paradigms as broadly as possible.

Wrappers must be designed based on the content and the context of their use as much as any other part of the product. A wrapper for a mobile phone application will be quite different from that for a portable GPS, or a kiosk. When determining which information belongs in the wrapper, you must decide on a multitude of things regarding context of use:

• The technological, functional, and business requirements and constraints

• Where the context of use is occurring

• The goals of the users

• Which tasks are needed to achieve these goals

• What types of information must be displayed to achieve each goal or task

## Patterns for Composition

Using appropriate and consistent wrappers will create mappings and affordances that will allow for positive user experiences. Figure 1-1 shows a selection of key components. Within this chapter, we will discuss the following patterns based on how the human mind processes patterns, objects, and information:

## Scroll

When information on a page exceeds the viewport, a scroll bar control may be required to access the additional information. Scrolling of information should almost always occur along one axis, except in rare cases.

## Annunciator Row

This displays the status of hardware features on the top of each page. The status of functions that may be displayed is radios, input and output features, and power levels.

## Notifications

When an alert requires user attention, a notification will occur in some form of visual, haptic, or audible feedback. These notification displays must allow for user interaction.

## Titles

Pages, content, and elements that require labels should use titles. These titles should be horizontal, be consistent in style, and follow guidelines of legibility and readability.

## Revealable Menu

This type of menu displays additional menus that are not immediately apparent. A gesture, soft key, or on-screen selection will cause these menus to immediately display on-screen.

## Fixed Menu

This type of menu presents an always-visible menu or control that is docked to one side of the viewport. This menu is consistently placed throughout the application. These interactive controls are most likely icons with textual coding.

## Home & Idle Screens

These screens are used as display states when either a device is turned on or an application has exited, timed out, or returned to a device-level menu display.

## Lock Screen

Mobile devices use this display state to save on power consumption. When necessary, the application’s sleep state may become locked to protect the security of the data the user has input. Additional user interaction is required to exit out of the lock screen, as shown in Figure 1-2.

## Interstitial Screen

This type of screen is used primarily as a loading process screen during device or application startup. Wait indicators may be used to show loading progress.

## Advertising

When advertising is used within a mobile application, the advertisement must be distinct and must not affect the user experience. Obtrusive advertising could prohibit the user from achieving his task-based goals. Advertising must adhere to the specific guidelines set by the Mobile Marketing Association (MMA).

## Scroll

## Problem

More information is in the page or element than can fit in the viewport. You have to provide a method to access this information.

Usually, the OS provides this function. Certain behaviors will occur automatically, but in application design especially, you may need to customize your interaction and interface to work in the best possible manner.

![](images/74025caa39999442d57e93c128cfd617aa15132a0f8aeeaf1cf34d76e593d5de.jpg)

![](images/b15b521bc401d4e4f9ed63b5afa8dc3621d5090cdc19db9fa84f9fc8771c4ffd.jpg)  
Figure 1-3. Scroll indicators may be complete bars, or simple indicators floating over the content.

Scroll bars (Figure 1-3) have long been used in information display systems of all sorts. For mobile, you will display them to indicate the scrollable axes, and the relative position within the scrollable area.

Due to the scale of mobile devices, as a general rule you should not allow the scroll bar to be manipulated directly. Instead, allow the content to be grabbed directly by a gesture, or make the entire area movable via dedicated Directional Entry keys.

You will find that scroll behaviors are key to interaction with mobile devices. As with all the patterns around page Composition, Scroll will be mentioned in most of the patterns in the rest of the book. It is especially relevant to the list and list-like Display of Information patterns:

• Vertical List

• Infinite List

• Thumbnail List

• Fisheye List

• Carousel

• Grid

• Film Strip

Although scrolling does occur in other patterns, do not confuse it with other patterns, such as Infinite Area. That pattern does not use scroll bars due to the arbitrarily large data set presented.

## Variations

Whenever possible, you should make sure scrolling takes place on a single axis. This is why the whole set of patterns based around Vertical Scroll exist. When the situation demands, such as for zooming in to content which otherwise fits the area, you can also offer a secondary scroll axis. Keep the secondary axis in mind throughout the design process; it may help you to understand how to avoid behaviors that may lead to confusion or cause the user to become lost when scrolling.

![](images/ae765d220747c79cbaa5ddd518e337a013269b5e14dcf0ff52464496639454aa.jpg)  
Figure 1-4. A thumbnail may be a better way to indicate location within a large area, and may also be used to jump to other regions. Here, a full desktop-view website is in the corner, while a zoomed-in view of a small portion occupies the rest of the viewport. An indicator on the thumbnail indicates the current position and relative size.

In rare cases, both axes of movement may be equally important. When zooming in on images, for example, the information is equally important in all directions.

Regardless of whether you are making a single-axis scroll or just selecting a primary axis, vertical scrolling is usually the easiest for users to understand and use. This is a result of language, where text uses horizontal space inefficiently, so additional items must be displayed in the vertical axis. See the Vertical List pattern for more discussion. This also means users are most familiar with vertical scrolling items, and so react best to them, though this may change over time.

Using the horizontal axis is occasionally useful for certain kinds of data, but is most useful when you must present a subsidiary scrolling area. If you have a vertically scrolling page of information, you can provide areas which allow for scrolling horizontally. This can provide additional clarity, and removes conflicts around in-focus scrolling that we have all encountered. (Think of what happens when you encounter a large form area in the middle of a web page.)

Whenever possible, you should display scroll indicators. Try to solve space and clutter problems with options presented in this pattern, and not by removing the indicators entirely.

For multiaxis scrolling especially, you can instead provide a thumbnail of the entire available area, as shown in Figure 1-4. This is usually, but not always, in addition to the scroll bars. The thumbnail shows the current viewport as a subset of the total area.

## Interaction details

Only allow items that are in focus to scroll. For scroll-and-select devices especially, be sure this is clearly communicated and strictly enforced. See the Focus & Cursors pattern for a discussion of communicating focus.

For scroll bars on touch or pen devices, it is almost always best to not allow the scroll bar itself to be directly manipulated. Handset-size devices are too small, so this would encourage accidental input on the screen. Instead, the entire page is scrolled by gestural movement. Use care with detection of gesture to avoid selecting items on the page.

When designing for devices with larger screens, you may be able to add actionable scroll bars. Often, these still are distractingly large, so you may want to make them appear only conditionally. A similar function, suitable for many sizes, is discussed in the Location Jump pattern.

Scroll-and-select devices will use a scroll key pair, or more often a five-way pad of some sort. Scrolling may be by item (line by line, or jumping link to link) or by moving a pointer on the screen. When you use a pointer, do not allow it to get too close to the edge of the screen; scroll when one-third to one-fourth of the way across. Of course, at the limits of the displayable information, it may approach the edges in order to select all items in the screen.

For item scrolling, do not allow the user to jump past content. For example, when viewing a web page, if the primary method jumps link to link, when there is a large area of content with no links, temporarily suspend this and scroll a few lines at a time so that all content can be seen.

You can also provide item scrolling as a secondary method. If you have set the Up and Down scroll keys to move line by line, the unused Left and Right keys may be set to jump from link to link.

When using the five-way pad, users should always be able to press and hold in one direction for a short time to accelerate scrolling. The absolute speed depends heavily on the amount of content. Scrolling must be slow enough to allow the user to see his current position; otherwise, he will not know when to stop scrolling. This is extremely expected behavior, and so is noted when not included.

For touch and pen devices, inertia scrolling has also become expected behavior. If the user’s finger (or pen) initiates a drag action, and departs the screen while still moving, the screen will continue scrolling at the departure speed until it is stopped by another form of input. It is usually best if you configure this to simulate friction so that the scrolling gradually slows over time, but do not overdo this deceleration if the list is very long.

If a thumbnail of the total content is provided, this may also be interactive. For touch and pen devices, tapping another area of the thumbnail will jump to that area. For scroll-and-select devices, Accesskeys may be provided to allow jumping to a region of the displayed area.

You can also use Kinesthetic Gestures, such as tilting the device, to scroll pages. These are not very common, so there are few standards regarding their implementation, and users must generally be instructed in their use.

![](images/3556a1f53b8d34183b71980a209b65d34fd42c6e35b7bcae810d2d0cdd565a2b.jpg)

![](images/6c5162b57992d25f932cd9415d3d14df01cdee17f3fc43888d1e3d6cfd337e80.jpg)  
Figure 1-5. Two types of two-axis scrolling. For items like images where both axes are equal, scroll bars must be equally easy to see and use. Make sure they are not obscured by options menus and other items, as shown to the left. For information oriented mostly along one axis, the other axis is secondary, and the scroll bar may be obscured as needed. On the right, the soft keys are not always visible, but they do sometimes occlude the horizontal scroll bar.

## Presentation details

Scroll indicators are not usually used in mobile devices to enable scrolling, but to:

• Provide an affordance (communicate the function) that the area is scrollable

• Convey the current location within the total content

• Indicate the relative amount of information the viewport displays, as a ratio of the total content

Always be sure to display an indicator of position. This may be hidden for full-screen views, when other information is hidden. But be sure to display the scroll position indicators whenever the user is interacting with the content, and especially whenever the user is scrolling.

Scroll bars may be made very small, or be obscured by other elements in some cases, as in Figure 1-5. Effective, visible scroll bars can be as small as two pixels wide: a single pixel line defines the outside of the bar, a single pixel line defines the inside, and a different colored area is for the current position. Naturally, this depends on the resolution of the display, so larger bars will be needed for very high-resolution displays due to the small pixels; for devices where the screen may overscan (such as for TV output) or the bezel is large enough, it may occlude the screen.

You can also eliminate the scroll bar itself, and just use the scroll indicator alone. A small tab can be anchored to the edge of the screen, protruding into the content a small amount. This must be larger (at least 5 to 10 mm wide), but since it floats on top of content, it doesn’t take any actual room from the display area, unlike a traditional scroll bar.

The position of the scroll indicator within the viewport indicates the position of the viewport relative to the total scrollable area.

The height of the scroll indicator, in either case, should reflect the ratio of the viewport to the total scrollable area. For scroll bars, this should use the viewport as the 100% scale, so if very little is outside the viewport, the scroll indicator is almost as large as the viewport. For indicators without scroll bars, the size of the indicator must often remain relatively small to avoid obscuring information; a relative size change may still be possible, but will not be as effective at communicating the relative scale to users, or might obscure too much content.

When you have a scrolling area displayed, but it is not in focus so the scroll actions will have no effect, be sure to communicate this to the user. Generally, simply removing the scroll indicators will do, but often the secondary value of the indicator (position and size) is still useful. When displaying a Pop-Up layer, simply graying out the scroll bar in the parent window may or may not be sufficient. Additional changes to the scroll indicators may be needed.

## Antipatterns

Do not allow users to become lost in the scrollable area. Especially be sure to not allow scrolling single-axis lists so far that no content is visible.

Consider anchoring secondary axis scrolling to an edge when scrolling on the primary axis. Two-dimensional scrolling is often very difficult to achieve with precision.

If you have to use multiaxis scrolling to show the information, do not assume it will be easily understood. Try it out, and add additional help or more prominent scroll indicators as needed.

Whenever possible, avoid vertically scrolling areas within other vertically scrolling areas. For example, a form text area within a page will, when it is in focus, stop the page scroll and grant all scrolling to itself until it has scrolled all the way to the bottom, then may allow the page to regain scroll focus. This is confusing, and often leads to errors. Avoid it instead.

For touch and pen devices, avoid drag-and-drop interfaces, or other interactions that require dragging an element within a scrollable area. If required, consider multifinger On-screen Gestures or Press-and-Hold interactions as a method to initiate a mode switch.

Be sure to support all the available input methods for the devices you will support. Touch and pen devices which also have five-way pads must be able to be entirely used (as far as scroll and selection goes) with the five-way pad. If there are multiple types of hardware for your target audience, be familiar with all of them, and do not just design for your handset.

When scroll indicators are used on an Infinite List, the location and relative size must reflect the total size of the available data. Do not allow the scroll indicator location to be based on the currently loaded data, and therefore to constantly change as new data is retrieved. You can do this by getting a count of the total number of items, and loading empty containers of the full size; only load data into them when demanded, instead of loading the container as well.

## Annunciator Row

## Problem

You must provide an easily discovered display of the status of important hardware features such as battery level and network connections.

The OS provides Annunciator Row features, but you may usually modify or suppress the Annunciator Row within applications.

Solution

![](images/3df7ab83e9f513c7cd29a510d952545edfa691b63696b3e15b827fdb907ed4e1.jpg)  
Figure 1-6. The Annunciator Row is a strip anchored across the top of the viewport. Note that the scroll bar stops at the Annunciator Row, as it does not scroll.

Annunciators are lights, gauges, or sounds that indicate system status. Annunciator lights and panels date to the dawn of electrical devices.

The term was carried over to electronic design, and then to mobile OS design. Though the same feature is often referred to as a “status bar,” this typically implies some overlap with the concept of Notifications, which we will discuss in the next pattern instead.

A bar, as shown in Figure 1-6, is displayed along the top of every screen with a series of iconic representations of the status of the device. You should always use common representations and placement of icons, so your users can understand the key indicators on any device without having to learn the specifics of every device.

## Variations

The Annunciator Row is present on all screens. It may only disappear or be of lower prominence when other controls disappear as for full-screen game play or video playback.

Certain devices may not require using the space for constant reminders of system status messages. Appliances such as eReaders do not necessarily need an Annunciator Row as their battery life is very long, and network access is needed only intermittently. The status messages will still be needed, and you may be able to solve this with something like Notifications repurposed to display such information when it becomes critical instead. See that pattern for details on this functionality.

Kiosks and other devices where the user does not have full control of the device also may not need to display an Annunciator Row to general users.

## Interaction details

Annunciators are notifiers only. You should generally not allow direct interaction with the items.

For touch and pen devices, it may be desirable to allow the user to select the Annunciator Row as a whole, in order to get more information, or to provide access to settings. You may also accomplish this by combining it with the Notifications area.

## Presentation details

You should plan to display the default Annunciator Row on every screen. Make a careful, deliberate choice whenever hiding to regain screen real estate or to declutter the screen. Hiding the status icons is generally appropriate for video playback, most games, and many slideshows or similar interfaces. Browsers and readers of ebooks, PDFs, and the like may also benefit from hiding the Annunciator Row once reading or scrolling begins.

The Annunciator Row is generally displayed as a row of icons—as in Figure 1-7—laid out on a strip of color, gradient, or other background imagery to separate the icons from other, generally interactive display elements. Scroll bars do not intrude into the Annunciator Row as it does not move, but remains fixed at the top of the viewport.

Many devices allow the Annunciator Row to be modified. In general, you should restrict these modifications to display changes, such as switching out the background color, and changing icons to match. You can also use this modification as a half-measure, when completely hiding the status messages might not be the best option. For example, camera applications often use great amounts of battery power, so you could display the battery icon, but no others in order to leave more room for the live preview. If you do this, use the conventional position of the battery icon, simply leaving out all others.

![](images/3a1692993de349873acf63941274f17c36e11b2d16fca773c352d7354418d795.jpg)

Figure 1-7. Common icons for the vast majority of conditions shown in the Annunciator Row. All items are enabled and at maximum graphical mode. This is an example; some are in conflict with one another, so this would never be seen. From left to right: Mobile network, WiFi, Bluetooth, NFC Airplane mode, Audio level, Locked, Clock, Network activity and speed, Voicemail waiting, Synch, Location, USB connected, and Battery status.

Within the row, the status messages are displayed as icons, with as few words or numbers as possible. Use common, universally understood or industry-standard icons whenever available.

Icons do not indicate the presence of a feature, but the status of that feature. No display means the icon is not functional, and displaying the icon means it is enabled. Optionally, disabled features may be displayed as grayed-out icons. This can be beneficial to communicate the availability of some features. Use caution to ensure that these are clearly disabled under all lighting conditions.

Whenever possible, you can add additional status messages to the icon, such as bars of signal or battery level, as shown in Figure 1-8. Use simple changes and well-understood signaling such as tall = more and red = bad.

![](images/0842150f9cf9376e55056af5e1057b3e605ba7dc72835b5a74aa80510da206f6.jpg)  
Figure 1-8. A series of exemplary statuses for the battery, from full to empty, then charging. Using the exclamation point in the icon is clearer than blinking the icon, and is a second code for users or conditions where red is not visible. The power plug icon is clearer to many users than the often-used lightning bolt.

For certain features, whose presence is assumed, you must include explicit measures of their disabling or failure. For example, when no signal is available, the mobile network will have an error “X” in place of the signal bars.

Items are grouped by basic functionality. A conventional order has arisen, from left to right:

• Radios:

– Mobile networks

– WiFi

– Bluetooth enabled, and active

– NFC or contactless payment enabled

– IrDA or other nonwired networking as available

– Airplane mode

• Input and output:

– Volume, vibrate, or silent mode

– Screen or keyboard locks enabled

– Network activity

– Network speed

– Message Waiting Indicator for voicemail, unless this is displayed by the notification area instead

– Synch status or activity

– Location services enabled; may or may not indicate when GPS is active

– USB cable connected

• Power:

– Usually a single item, which changes based on charge level and state (e.g., being charged)

– A second battery indicator, as may be displayed on those now-rare devices with outboard (piggyback) or secondary batteries

The time of day (and sometimes the date) is also present, but may be in any of several places in the row. The most common is centered, followed by right-aligned. Time is always displayed, even on those few devices without an otherwise permanently visible Annunciator Row.

Naturally, features not included with the device are not given space in the display. Some items may share space, and the highest-priority feature or the one with the most important message is displayed.

## Antipatterns

Don’t let the order or size of the row, or the details of the icons, change with different screens. Use one layout and one type of icon in all situations.

Don’t reinvent the wheel. Reuse existing good design concepts so that users do not have to relearn your icons. How many of those in Figure 1-9 are immediately understandable?

![](images/fb7313b17aad230c9ecf3d95bed68c71e74e91d073be13d0e89f21100193a529.jpg)  
Figure 1-9. These are just some of the many ways battery charge level is depicted on mobile devices. Many are quite unreadable. Try to pick simple, easy-to-understand symbols, and reuse common icon styles from existing products and best-in-class examples.

Except when notifying users of special conditions in places where the rest of the bar is suppressed (e.g., battery on a camera screen), do not pick and choose which items to show. Always show the same set in the same manner.

Avoid explanations that are jargon-laden. The percentage of usable battery is not nearly as useful as an estimate (even a bad one) of time remaining on a battery.

Avoid animations as sole explanations. Mobiles, and especially the status area, are often only glanced at. Blinks will instead be seen as solid on or off at a glance.

## Notifications

## Problem

You must provide a method to notify the user of any notifications, of any priority, without unduly interfering with existing processes.

The OS generally provides notification features, but they can sometimes be overridden. If you’re building a notification-sending application, it must correctly interact with the system. Certain applications and sites can also call for their own notification processes that have nothing to do with the OS notification system.

## Solution

![](images/5871d0fe40c308ef2a820132113fb4ecdf3e2229729303ae147af9530c13458a.jpg)

![](images/5c7939d7a702dccac66c1f6411f28fc8504276479e718bec15996c29e443df45.jpg)  
Figure 1-10. Since mobiles generally have limited space, and notifications must usually be assumed to be secondary to the current process, even a dedicated notification area should be out of the way. When the notification area is selected, allow users to access more information, as on the right, where each item is described further.

A single, consistent notification method should be provided across the entire OS. Make sure this method does not interfere with any processes the user is currently involved in. The user must be able to act on or dismiss the notification very easily.

When notifications are restricted to a specific subset of a device, such as an application, make sure they follow the same principles and do not conflict with the OS-wide notifications.

Multiple notifications must be able to all be displayed in a single view, so no notification obscures another.

## Variations

Multiple variations of this pattern are available.

A dedicated notification strip or area may be used, with a portion of the viewport dedicated to notifications. This may be partly or completely hidden when no notifications are present, but will fade in, slide up, or otherwise appear when notifications are present. Figure 1-10 shows one example of this. The selection of any notification item will display the item in the application that hosted the notification. This may be difficult to use for scroll-and-select devices, so it will be most commonly encountered on touch and pen input devices.

Notifications may be combined with the Annunciator Row, as shown in Figure 1-11. This is, in fact, very common on basic and legacy devices, where the envelope icon means new voicemail or SMS messages have arrived. Additional notifications may be added to this area as well. These legacy utilizations are not Notifications as far as this pattern is concerned, as they are not generally interactive; the user must take separate action to dial into the voicemail system or open the text messaging application.

![](images/aca73afd1e9834e58335cf5b0d12b9d92a00a14743c4d3a941382ebdc6ddd238.jpg)  
Figure 1-11. The Annunciator Row commonly houses notification icons, as on the left, but may also be used as a method to access details or view the items. On the right, the user has tapped or pulled the Annunciator Row down to reveal a notification area.

Especially for touch and pen devices, the Annunciator Row may include a notification area. You may place as many notification icons in the Annunciator Row as will fit. When it is opened, a complete list of all the current notifications will be revealed.

For scroll-and-select devices, and certain other cases (if there is no good place to put a notification area, or if the Annunciator Row is unsuitable for repurposing), a simple Pop-Up dialog box—as shown in Figure 1-12—may appear over the current context whenever a notification appears. This is a special case of the Confirmation dialog, which should be seen for behaviors and layout.

Currently, regardless of the other notification paradigms, incoming voice calls use a completely unique notification method, and automatically launch the phone application fullscreen. This is a holdover, and may not be a permanent condition. Some OSes already seem to be addressing this by placing a “current call” icon in the Notifications area when in another application. Selecting the Notifications area allows the user to see certain details regarding the call, and switch to it rapidly. Using any of the aforementioned notification methods could provide a suitable a method of informing the user of the incoming call, and of accepting or declining it.

## Interaction details

A key attribute of the Notifications pattern, as distinct from the Annunciator Row pattern, is the ability to directly interact with the alert. The user must be able to see each item individually within the notification method, and select it for viewing (or other suitable actions), or be able to dismiss it.

When more than one current notification is available, the method must support the ability to show all of them at once. If the Confirmation dialog style is used, for example, a special version must be made where a list of all the notifications is displayed instead, and selecting one will open a new dialog with the details and actions of that item alone. Within this list, batch operations, such as dismissing all notifications, should also be available.

![](images/631824bf1e9a6e3bfbbc823f06d012aab2407f0c0bbf0b348c767886a5cca056.jpg)  
Figure 1-12. Pop-Up notifications are used when other methods are inappropriate due to interaction limitations, or other spaces are occupied with too many other functions.

When the Annunciator Row is used to access notifications, tapping or dragging the row will reveal the list of notifications. You should choose a method for the reveal gesture that is based on other gestures used in the OS, so it is discoverable and understandable when described and demonstrated.

Various actions must be available for any notification item, or for a single notification Pop-Up. See the Confirmation pattern for details on the dialog especially. Consider which actions might be helpful in reducing the number of steps the user must take. For example, instead of just “Read” and “Dismiss” buttons for a new SMS message, a “Reply” button could be added, if the message summary is enough to elicit a response. This will allow the user to act immediately. Use caution not to add too many options, cluttering the selections and reducing the size of displayed information and options.

When a notification is acted upon (e.g., the new text message is read), suspend any current operations or actions and save all user-entered data. When the action, application, or process initiated by acting on the notification is completed, return to this previous condition.

## Presentation details

Fixed notification areas most commonly appear as a strip along the bottom of the viewport, to differentiate them from the Titles and Annunciator Row elements. The area should be at a fixed location within the viewport, and should not scroll. Scroll bars will not overlap the area when it is displayed. Individual notifications will be displayed as line items, or may be grouped by category, with counters indicating the number of notifications for each category.

Smaller devices, such as most mobile handsets, cannot dedicate this space, so they most often collapse the notification area to an icon or other small area within the Annunciator Row.

Labels for each notification item must be clear and comprehensible. Always state the service or application initiating the notification; usually, an icon will be sufficient for this. If a summary of the message cannot be displayed (such as for voicemail, or an MMS message with no text), do not display jargon or difficult-to-parse information such as the sender’s phone number; use clear descriptions instead, such as “New voicemail.” Whenever possible, display relevant information; look up senders of SMS/MMS messages in the address book and, when found, display their name instead of the phone number.

If summary information can be provided, such as the content of a text message, this may also be displayed. This is a rare case where marquee text, which scrolls within the available space, may be used to good effect. Text messages are short enough that such text display tends to be readable, and allows the user to read the entire message rapidly, without opening the messaging application.

Additional information may also be derived from the notifying application, or other handset services. For the case of a new SMS message, any avatar icon for the user may also be displayed, to assist in understanding what is being sent at a glance.

To keep the list of notifications from becoming too long, you should usually cluster them. Instead of a single line for each notification, display one line for all SMS messages, one for all email, and so on. Each line then has a counter of the number of items within it. The OS may limit the behavior you can implement with this. For example, you may not be able to reveal individual notifications, and you may have to load the application sending the alert.

For most notification types, you should also blink the LED and sound Tones and Haptic Output (vibration). These must be customizable so that the user can determine which types are critical enough, and they must follow the system-wide output settings to respect silencing. See the relevant patterns for additional details.

## Antipatterns

Do not display notifications serially. If more than one is received at a time, use a multiplenotifications method, instead of showing one single notification after another.

Do not allow notifications to prevent access to other systems, even temporarily. The notification system must allow individual notifications as well as all current notifications to be dismissed.

Most media-centric activities, such as video playback, should not be interrupted by notifications. Very high-priority notifications may still interrupt, but must either pause playback or be very nondisruptive so that playback can continue during the notification.

Never display notifications to external display devices, such as TVs or projectors attached to the device.

Be sure you understand and follow the OS’s method of notification and of marking messages or other notifications as having been read or accepted by the user. Dismissing a message from view in the notification area may or may not mark it as read in the application sending the notification. There is, as yet, no consistency in this regard, so no pattern can be determined at this time.

## Titles

## Problem

You should always label each key element to make context or process completion clear. Titles are a key part of all OSes, applications, and web standards, but it is always up to you to include them in the design in the appropriate manner.

## Solution

![](images/4864174eb3c77ef465360fbda5a5625f0cb65b2149498a8b70960927bda0037f.jpg)

![](images/bd97bc6ab97603dfb338ac26080ad4f3799cfb55b1724ebfae00dded7b7ec4d0.jpg)  
Figure 1-13. Titles should always be attached to freestanding elements, such as pages, windows, or pop ups. Follow the OS design guidelines for the use of title bars.

Pages and elements or content sections within a page should almost always be labeled.   
Pop ups and other freestanding elements should have titles similar to the page-level title.   
Figure 1-13 shows both of these.

You should make a special point to use Titles in a consistent manner. Consider the size, location, content, and type style. The simplest method for the page level, especially for applications, is a straightforward title bar. We show this in almost all the diagrams in this book.

## Variations

Titles are always horizontal, and any top-level title should be boxed, or otherwise separated out to make it clear that it is a key element.

Subsidiary titles are also text, but the text can be stylized as needed (bold, color, etc.) or additionally include boxes, rules, indents, or other graphical treatments to differentiate them from the remaining content, and to more clearly communicate their hierarchy.

If the OS calls for it, you should make the title of the running application display in a special title style. If so, there is no need to repeat the application name within the page title area. In some cases, the application title bar may disappear shortly after the application is loaded.

Interaction details  
![](images/9687af5c54ef5be7b17ae53b009e418a19fc4952a12bd0290f712a7a14462997.jpg)

![](images/cd46491261e1801c446f9d7061fb8f0c7e358944e594397931f0c9782c3a56a4.jpg)  
Figure 1-14. Page titles can be selected, by tap or drag usually, to reveal alternative information or functions. Here, within a web browser, the page title can be selected to show and edit the URL, and perform other browser functions.

Titles are not required to have any interaction.

A typical interaction for titles of modules or sections is to make the title a link to another page.

The title bar of a full-viewport page can be used to reveal additional information (tap or drag down to reveal functions such as URL entry for a web browser, as shown in Figure 1-14) or as an anchoring element for very long pages (tap to return to the top of the page). These are generally only useful for touch and pen devices; for scroll-and-select input, having to scroll past the title is generally additional effort to be avoided for secondary functions such as this. If needed, place them within option menus.

## Presentation details

Whenever possible, you should follow OS guidelines for title design. Though naturally this applies to applications, even web design should follow these guidelines when they can be targeted to the OS level. Even if significant changes are required for unique branding of your product, make title bars of similar typeface and style, size, shape, and position to the rest of the OS. For example, if the OS uses white title bars and black text, you can easily use a black bar and yellow type, and it will look consistent enough if the size, style, and position are identical.

Titles can include icons. Try not to be needlessly repetitive. When available, use a more specific icon instead. For example, in a Pop-Up, don’t repeat the application icon, especially if the window behind it is clearly visible. Either display nothing, or use the space for icons that indicate the state, such as an error triangle if there’s an error.

![](images/7a9b8bf8d9138211a00048060c01dede966444a89d36930385c865fd56712399.jpg)  
Figure 1-15. Build all content with a hierarchy and title sections to follow, and express this to the end user.

It is best to get professional writing resources. If this is not possible, obtain a style guide, define a communication style for the product, and stick to it. Use similar language for all descriptive titles.

• Use the same voice and, when practical, tense.

• Use a single name for your product, when it has to be referred to at all.

• Use consistent capitalization (sentence or title case). If parts of the product are considered proper names, make sure everyone has the list of these names.

Design the whole product around a simple hierarchy, and stick to it. Avoid going too deep; past about three or four levels usually becomes confusing, and it will be difficult to differentiate titles. Indenting is a common way to help express a hierarchical relationship. You might think that most mobile devices are too small to use this effectively, but don’t worry, only a few pixels of indent can communicate this well. Compare this to the way a Hierarchical List is designed, and how it communicates the relationship between parent and child elements. See the examples in Figure 1-15.

Just like H-level elements in HTML (H1, H2, etc.), similar title and other display hierarchies are built into native OS development kits. Often, as with semantic web concepts, these have default attributes assigned, which can be useful when building the product and can add value to the user experience. Even if additional styles are imposed, you should try to use these basic attributes as the first definition level.

When titles are links, make this clear and follow conventions used in the rest of the application or site. Additional hints may be needed; even if color normally denotes a link, this may not be clear enough for titles which are often a different color from the content text anyway. Icons or underlines may be needed.

## Antipatterns

Avoid jargon, or exposing internal processes. Avoid excessively harsh error messages, and other things which may confuse or annoy typical users. Even for certain special professions and hobbies, your customers will generally not understand your internal processes and organization. You have to explain this to them instead, in their language.

Do not repeat content. If the application is described adequately, do not keep restating the application name in subsidiary page or Pop-Up titles.

During testing, and periodically as maintenance, be sure to check all content. Often, only mockups or the primary path is inspected, but alternative paths and errors must be as clear, consistent, and well described as any other parts of the product.

## Revealable Menu

## Problem

You often will not be able to fit all functions for a page on the screen. A method must be provided to access these optional functions.

Often, the OS should dictate the general style of the menu structure, if only because users will become familiar with the style of interaction. However, there is generally much leeway in implementation, if variation from this is desired or called for.

## Solution

![](images/4e590be5c9b7d8aa0a83140a5a926ac65f2b3adaf516687ff128383a4ed5065a.jpg)  
Figure 1-16. Soft keys are very common still, revealing menus from tab labels based on pressing adjacent hardware keys. When one is open, the other provides a method to exit. The same paradigm can be used without the hardware keys on touch and pen devices by directly selecting the tab labels.

When the user selects a key, selects a small on-screen element, or performs a gesture, an option menu is displayed with content relevant to the current state of the application.

Soft keys (hardware buttons tied to on-screen labels, typically on feature phones) are the archetypical version of this. Single actions that take place from a soft key (such as Cancel) are not a Revealable Menu since they are visible, and might be considered a Fixed Menu. There are many cases where the two menu access systems overlap, or switch back and forth depending on context.

Note that some devices use more than one menu scheme, for different purposes. For example, one may present options for the current application, and another may provide access to the running-applications list for the entire device.

Do not confuse display of this menu with the display of a Notifications list, and be sure the two do not conflict with each other.

![](images/77dc5c284adbeba50cde4022d54d29ab3d941cf3d0fcf949ae8d5c9a86147b2d.jpg)  
Figure 1-17. Menus can be of different types, here displaying fewer items, but also being more touchfriendly, and leaving more of the original context visible.

## Several variations of this pattern exist:

• The soft-key style uses one or more hardware buttons (or a portion of the touch/pen area outside the display) to reveal an option menu. When closed, these may or may not display a tab and label indicating their presence. Compare Figures 1-16 and 1-17.

• Soft-key-like on-screen displays always display a tab or button, usually along the bottom edge of the viewport. The closed state is always visible as this is the method used to access the function.

• Gestural menus, as shown in Figure 1-18, generally have no on-screen visibility. When the user swipes from an edge, the menu acts as though it accompanies the gesture, and moves into the viewport at the same speed. This is generally nonpersistent, and when the pen or finger leaves the screen, the menu collapses. Selections must be made in the same pen/finger-down gesture as the original reveal. Releasing while an action is in focus selects that action.

• A fourth variation combines gestural menu reveal methods with the on-screen button. When activated, the menu appears via another action such as sliding in from one side, or being revealed to be behind another component (such as by hiding an otherwise-present virtual keyboard). Other methods such as the Peel Away can also be used, but may be difficult to communicate to the user.

Items within the menu often reveal submenus, or lists of additional features. These may either follow the same principles as the top level of menu and appear as an attached subset, or appear as a freestanding menu, usually as a Select List or Grid of items in a Pop-Up dialog.

## Interaction details

Treat opened menus as modal dialogs. For touch and pen devices, selection outside the menu area may, if desired, clear the menu instead of being ignored. This is especially true if the menu, when open, does not obscure the background. However, you should not allow users to select items in the parent window while the option menu remains open.

![](images/af8313e33caee4215a6d2ca93a121bc86261f3045b80726f1077521330d117c5.jpg)  
Figure 1-18. Menus can be made to appear with a drag action, relying on no buttons or on-screen indicators. However, users will have to be taught this action somehow, so it is often unsuitable unless it is used across the OS, and there is supporting marketing or training can be tolerated.

All opened menus must have a method to be exited. The typical methods are as follows:

• You can use the dedicated hardware “Back” key. When present, this is the preferred method, as the user will be accustomed to using it for similar functions.

• A spare soft key or on-screen tab (even if it is normally another key, or another selectable menu) will change to “Cancel.” This key must be included in the items available for selection, and is not locked out due to the modality of the option menu itself.

• A close function may be added to the menu, either as a selectable menu option (usually the last one) or as a desktop-like close button in the corner. Both have certain pitfalls. The menu item must be clearly different, using a common icon. Also, a dedicated close button must be carefully placed to avoid accidental activation of it or adjacent items.

• The function that launched the menu may be used as a toggle. When it is available, and not obscured by the opened menu, selection when the menu is open will close the menu.

• Lastly, for touch or pen devices, you may make it so that selection outside the menu may dismiss the menu.

For devices with five-way pads, opened menus should be able to be scrolled through. Regardless of the input mechanism, selection of a single item will close the menu and initiate the action, which may change states, cause a different modal dialog to appear, load an entirely new page, or even exit the application. For vertical menus, see the Vertical List pattern for additional details on interaction and presentation.

If the selected item itself has options, a subsidiary menu will be opened, as shown in Figure 1-19. For vertically scrolling menus, this is usually presented as a visible child, adjacent to the primary menu, and is itself a modal dialog; the previous menu cannot be directly selected. For scroll-and-select devices, submenus can also be entered by scrolling to the right. For horizontally arranged icon menus, typically there is only one “More...” type of option which opens a Pop-Up dialog with a Vertical List, usually a Thumbnail List where the thumbnails are also icons.

To exit a submenu, scroll to the left or press the “Back” button or “Cancel” tab, whichever is available. This will only close the submenu, returning focus to the parent selection item, and not the entire option menu.

For any hardware menu keys or soft keys, pressing and holding the key can perform a different action. This action is usually a different kind of reveal menu, and may be associated with a soft key which normally does not open a Revealable Menu, and should have a relationship to the original key label to aid in discovery and recall. For example, within a browser, a soft key labeled “Back” could open a history menu when held down for a few seconds.

Presentation details  
![](images/8edd61044bd4d86c80db78ac1b8cc72a4a34fe687d45416f4c28c8c786b39a14.jpg)

![](images/350b48dd5cc49f9a1ec6ca84bbb3a06934ff56bc1ece01c19bf7ce84f715ce46.jpg)  
Figure 1-19. Submenus or additional options can be displayed from any menu scheme. Icon menus, such as gesture menus or the icon bar menu on the left, usually should open a separate vertical dialog. Soft-key-type menus, such as that on the right, usually display them adjacent to or overlapping the main menu.

In almost all cases, you should make the closed menu initiators or indicators, such as soft-key tabs, locked to the viewport. Do not allow them to scroll off the page. Visible tabs should always be visible, but may be hidden temporarily for media playback or otherwise to give more room to the primary content.

If your design has no on-screen menu visibility, and no dedicated button is provided, consider adding a visible component at page load, or during a training period when the device is first accessed to train the user that the feature exists.

Option menus, however they are initiated, must immediately appear. If animation is used to open the menu (e.g., it slides in), the beginning of the animation must start immediately. Since the menu may be partly obscured by the user, especially for touch and pen devices, Haptic Output (vibration feedback) of the action should also be considered. The menu should appear to emerge from the tab or button, overwriting the area.

Within the opened menu, display items as text, and use supporting icon elements only when there is room. See the Indicator pattern for more details on using icons along with text in lists. Most soft-key-like menus are vertical and designed for text density, so they do not work well when displaying an Icon for each item, but this is very suitable for other menu types.

Options that cannot be used should be grayed out to make them appear inaccessible. Leaving them in the list is helpful as it teaches the user what sorts of actions are available in the list, and preserves the position for additional consistency.

Display indicators for Accesskeys (keyboard shortcuts) for each item with an associated Accesskey. Do not display these for devices that do not have hardware keyboards or keypads.

You should place indicators of some sort next to items which can reveal additional menu items. Submenus may occlude the main menu if space is limited, or may hang off to the side. They should usually obscure the main menu in some manner to make the focus item clearer. Submenus should contain a Title, or the selected parent element must be highlighted and point to the submenu to serve as a label for the menu.

## Antipatterns

Modal design, such as the entire principle of a Revealable Menu, can be difficult to communicate, especially if OS standard implementations are not used or the user is not accustomed to the platform. Carefully consider the whole concept, how to ensure that the menu can be launched, and how many controls can be modeless instead.

Within the menu, only allow access to options that can be used. If all options are selectable, error messages will be displayed which could otherwise be avoided.

Soft-key orientation, or which side gets which key, should follow the standards of the OS or the operator. These are usually not set at the device level, but are universal for all devices using the OS, or all devices the operator overlays. Most application frameworks allow specifying something like “primary” and “secondary” as soft-key identifiers; use these instead of “left” and “right” to ensure that your application complies with the standards of the device on which it resides.

Avoid too many menu levels. Generally, due to screen size and complexity, only one submenu level should be provided.

## Fixed Menu

## Problem

You have to provide access to options or controls across the application, but a Revealable Menu is already in use, or would be unsuitable due to lack of controls or conflicts with other key interactions.

Often, the OS will dictate the general style of the menu structure. There is usually much leeway in implementation, if variation from this is desired or called for.

## Solution

![](images/bede4537a8ef9d15fca69a97826080eb0a2d543092ecbb531d4735a4d17d84b1.jpg)  
Figure 1-20. The fixed menu is always visible, and does not restrict access to the rest of the page elements.

An always-visible menu or control set is docked to one edge of the viewport, as shown in Figure 1-20.

Regardless of the OS-wide standard, you should often use a visible menu for media players, cameras, and other applications where a key set of controls or options should be visible at all times. Any time your users require immediate action, or you must avoid a learning curve (discovering a Revealable Menu), a Fixed Menu is a good solution.

When you can also use the menu to indicate position in the system, such as that an icon exists for each page, this is instead a set of Tabs, and not a menu.

Note that you should use this pattern only if it happens across the entire OS or an entire application. Controls on a single screen, such as zoom, pan, and playback functions for a weather radar image, are simply controls. Playback controls for a video player, which are the same in all modes of the application, are a Fixed Menu.

For game play, video playback or other full-screen displays such as readers may call for suppressing the Fixed Menu. It may be replaced with a Revealable Menu that opens in the same position.

## Variations

Use the Fixed Menu to display a simple list of available options. These are generally displayed as a horizontal bar, so usually you should display each option as an individual Icon, each with an associated text label.

These may be used as the primary menu structure, but are often used in concert with a Revealable Menu, in which case they must be deconflicted. Both are best when placed along the bottom of the viewport. However, if the closed paradigm for the Revealable Menu has visibility, this may need to be changed, the visible tabs may need to be minimized in some manner, or the Fixed Menu may need to float higher up or be attached to a different side of the viewport. This may cause the Fixed Menu to be arranged vertically or horizontally.

On touch devices, the bottom of the viewport provides an additional advantage in that it may be easier for the user to reach, and for submenus to open, and so will not be obscured by the user’s hand.

Pure text lists are also sometimes used, and generally follow the desktop metaphor (File, Edit, View, etc.), and so are always horizontally arranged. You can only use this successfully with a sufficiently large display. Avoid letting functions fall off the screen, as is shown in certain Tabs.

A Fixed Menu may include all options or controls required, or may offer subsidiary or additional lists of options.

![](images/71fbd4982a2fb3fb9f056cbabf1551da6d0226f6749ac940702b8f2e73ed11cb.jpg)  
Figure 1-21. Additional menu options, or long lists of subsidiary options, generally are displayed in modal dialogs as on the left. Simple options, or single interactive elements, may simply reveal themselves as controls sliding off the main menu bar, as shown with the slider on the right.

Fixed menus are either used for pen and touch devices, or used when the page content does not have to be interacted with directly, such as with video playback; the controls are the primary interaction method.

Fixed menus are not contained in a modal dialog, so you can offer interaction with the entire page’s content, as much as needed. If it is not accessed as a matter of course, such as for video playback, this does not change the general state of the interaction. Other controls may also exist on the page, and are accessible at any time.

For devices with five-way pads, opened menus should be able to be scrolled through. Touch and pen devices use direct selection of the items in the menu. For controls, drag and other gestural actions (such as to change zoom level or jog to another portion of a video file) may also be supported.

Selection of any single item will initiate the action, which may load a new page, change states of the current content, cause a modal dialog of options to appear, or even exit the application. When the options in a subsidiary dialog are simple, they should be docked to the original selection. If you must prevent obscuring of the primary content, or if selection inherently disrupts other primary functionality, these subsidiary menus may be press-and-hold items; with touch or pen devices, press the menu item, then drag over to the selection and release when it is in focus.

If you must place more items in a menu than can be fit to the main menu, a subsidiary menu will be opened. This is typically a Pop-Up dialog with a Vertical List. When practical, to comply with the iconic presentation of the main menu, you may draw this as a Thumbnail List, where the thumbnails are also icons. Figure 1-21 shows two variations of this.

Presentation details

![](images/8aa2543b01c4623c304237d0d804c7ca62fd672dd3e53a454061ab7ca6b0409f.jpg)

![](images/e672d8ec0e06f1c8c429d905e63d2469643924ef3d765288158e5e0960622ef7.jpg)  
Figure 1-22. A fixed menu may be the only menu visible on the screen, as on the left, or may need to be moved or modified to work with other menus, such as the soft-key-like Revealable Menu on the right.

You should always lock the main menu to the viewport, and prevent it from scrolling off the screen. Do not allow the scroll bars to overlay the menu, to make this clear. Usually, to comply with the expectations for menus on mobile devices, the scroll bar is along the bottom edge, though it may be along one side to avoid conflicting with a Revealable Menu or along the top (below any Annunciator Row) to follow a desktop application paradigm. Keep in mind the issues of interaction conflict and obscuring described earlier when placing the menu anywhere except the bottom edge. See Figure 1-22 for two typical examples.

The menu is present in all screens and states of an application, but may be hidden temporarily for media playback or otherwise to give more room to the primary content. This hiding follows that of other fixed on-screen elements, such as scroll bars, Titles, or the Annunciator Row. Since they reappear by general interaction or after a time, and no explicit retrieval of the menu action is available, this does not convert the menu to the Revealable Menu pattern.

## Antipatterns

If hiding is routinely employed to retrieve on-screen space taken up by a Fixed Menu, reconsider the selection of this pattern. It is likely that a Revealable Menu is more suitable instead. Carefully consider the importance of consistency across the interface and the OS.

Do not stack multiple fixed menus on top of one another. Avoid having fixed menus immediately adjacent to other interactive bars of the same shape, such as a Notifications area. If this is the only suitable solution, prevent accidental activation through the use of gesture. You may make the items of the Fixed Menu tappable, but require a drag gesture to open the Notifications, for example.

## Home & Idle Screens

## Problem

You must display a default set of information and actions once the device has started, and to return to when all other user activities are exited or completed.

The device OS will provide this, but certain aspects can be modified, or widgets may be loaded by the end user which must integrate with the operation of the Home & Idle Screens correctly. Many of the same principles can be used for freestanding applications when the landing page offers enough functions or is used so often by the customer as to be functionally their home screen.

## Solution

![](images/cc5a5927b3f88b5979cdcd96936fe6d4948e751c8f0e8edfb42844d93dd45f31.jpg)

![](images/4f3403373eea8b77d474b28a53e08f009e0e8d9655d251d084cf3ad7ffe2e660.jpg)  
Figure 1-23. Two key types of Idle Screens are the informational screen (generally associated with simple scroll-and-select devices) and the multipage iconic home screen, long used for PDAs and now associated with all touchscreen handsets.

All mobile devices have an Idle Screen, originally used when the device was not doing anything (it is idle). This is used as a launching point or when the user is not specifically asking anything of the device. You can consider it to be similar to the Desktop on a computer, or to a web portal. Especially for smartphones and other, more capable devices, it provides a method to access all the applications, services, and information stored on the device, and can often be deliberately accessed by the user without exiting applications expressly for this purpose. Lately, it has been called a “home” screen quite often, and some OSes reinforce this to the end user by using the term, or a house icon, on the device or within the GUI.

If you are designing kiosks, or other, more constrained interfaces which present a smaller number of fixed options, the default screen is still considered an Idle Screen. It is just simplified due to the regular influx of new users and the relatively low number of options offered.

Do not confuse the Idle Screen with the Lock Screen or any other seemingly default screen. If the user must act to get to information or perform basic functions, it is not a Home or Idle Screen.

## Variations

Most devices mix several design methods, in order to achieve all the needed goals.

The Idle Screen is the single screen that is loaded when the device is powered on, or when all applications are exited.

The Home Screens, often notably plural, encompass all the device-level menus that contain links to the applications. The Idle Screen is invariably one of these Home Screens.

Idle Screens generally follow one of two patterns, both of which are exemplified in Figure 1-23:

• The Idle Screen is largely occupied with status information and may have little or no direct access to applications.

• The Idle Screen is the center one of a series of related screens with icon-based representations of many or all of the applications loaded onto the device, generally displayed as a Grid with the Film Strip pattern used to move to and between other Home screens.

Status on the Idle Screen has traditionally used fixed elements, or those with only limited customization. Widgets are now supported on many devices, which may vary from an interactive Icon to display or interactive elements that occupy a large portion of the screen.

Some applications may appear to be continuous with the drilldown method of access. Settings, for example, should usually be considered an application, but the interface and interaction may be so seamless that the user is unaware she has left the Home Screen drilldown and entered the Settings application.

Additional features may be integrated into the Home & Idle Screens, such as lists of running applications, displayed as thumbnails of the user’s current state or as a list of icons. Some of these additional uses of the Home Screens expand the interactivity to provide access via gestures perpendicular to the primary access. Rare or experimental versions use the features shown in the Simulated 3D Effects pattern to expand the home screen in yet another dimension. You can see that there is no clear limit on the variations that may emerge in the future.

![](images/39e145299307af9cc5b69ed9b9b992ac65f5d22aa3cea56f3348e0d5fdb729c6.jpg)  
Figure 1-24. Multipage home screens allow scrolling between each screen like a Film Strip. Position in the screens should be indicated and, while scrolling, should animate. Option menus, whether fixed or revealable, disappear during interscreen scrolling.

Idle screens with status information are mostly for viewing. There may even be no direct interaction. If you are working with a simple scroll-and-select feature phone driven by a five-way Directional Entry pad, you will assign key directions to actions or to launch applications. The defaults are often printed on the face of the device hardware, but may be changed in settings. For these scroll-and-select devices, the five-way pad has no scrolling functions on the Idle Screen.

Other devices with this type of Idle Screen are generally arranged so that vertical scrolling will move between calendar or notification items, and horizontal scrolling will move between application shortcuts. If you add touch or pen control to these basic interfaces, these items may also be directly selected, and will launch a full application view.

Multipage home screens use the concept of a single page larger than the viewport. You can consider this to be a Film Strip pattern, as shown in Figure 1-24, and use it to access as many screens as desired and which the device can support. These are mostly suitable only for touch and pen devices. Scrolling between screens may not be clear or easily understood, if you try to make it available on scroll-and-select devices. However, when hardware Directional Entry is available, be sure to offer scrolling control, so users incapable of employing the touchscreen can still manage to use the device.

Additional information is almost always available via a list of all applications on the device. These are often represented as a vertical Thumbnail List, but may continue using icons as the primary label, in a Grid format. Items should be hierarchically ordered, ideally with user control over folder names and contents, to organize the information as needed. If a single list of all applications is shown, ensure that it is in an easily understandable order, such as alphabetical. See Figure 1-25.

Very often, contextually intelligent mobile devices should be presenting the last-used state to the user at all times. For example, if you are designing an eReader, you should present precisely the last reading state when the user returns to the device, even after a power cycle. While a “Home Screen” will still exist, it will be viewed much less often in this case and may be considered a Settings page instead. The same principles outlined here should still be used, however.

Regardless of your device, consider building interactive methods that avoid the Idle Screen, and allow continuous use of the device. Home & Idle Screens encourage “pogosticking” from one application, to the idle screen, to another application. Running application lists should be made available from within all applications, for example. You may even be able to use the same interaction method to access the list from all contexts.

Presentation details  
![](images/0290489252d9cd0d2eb2ff6e2edf1e2761ee5bd75b78f46a644b7243cbee8a0b.jpg)

![](images/d91ec7bb73400111c693fd499c7b3f67d52ded4372e9b1b3206988ba5e3e4b07.jpg)  
Figure 1-25. A path must be provided to get from the Idle Screen (even if it is a multipage Home Screen) to the remaining Home Screens, to view all available applications and options. Within the list view, folders are displayed differently from individual applications or other leaf-level items.

Home Screens should be distinctly different from application screens. It should be clear to the user when he is on a Home Screen, and especially clear when he is on the Idle Screen. One key method is to have no Title on the Home Screen and rigidly enforce the use of titles on all other screens.

When using a folder structure to organize items in the Home Screens or related drilldown lists, make the structure apparent. You should make sure all folders carry a folder-like icon, even if additional graphics are attached to it.

When on a drilldown menu Home Page screen, title all screens after the main screen. Usually, this will follow the title of the icon or link used to load it, and should be accompanied by the same icon. See the Title pattern for more details on the use of labels and icons.

Multipage Home Screens must have a Location Within widget to indicate which of the pages is currently in view. If you have more than three Home Screens, you should probably use a Location Jump widget, possibly integrated with the Location Within, to provide access to the far screens with greater speed.

For multipage Home Screens, the backdrop should scroll at a slower speed than the icons, labels, and widgets in the front layer. This simulation of parallax makes the screen appear to have depth, and the movement of the background helps to act as a wayfinding device for the user to better understand her position on the screen. Although the user can change the background, the default backgrounds should encourage these behaviors, and have depth built in, or appear to be slightly out of focus. They should not have truly repetitive elements, so users may become familiar with the various areas of the image.

## Antipatterns

Ensure that users can understand the paradigm by which your Home & Idle Screens operate, without training. You should provide clear and easy access from the Idle Screen to the list of all applications, and to any menus of options.

Avoid violating device UI paradigms for the Idle or Home Screens. For example, the very common practice of disabling the scrolling function and making the directions correspond to shortcuts on the Idle Screen can be difficult to understand and learn. Users can experience a cognitive dissonance when switching between the two behaviors, which slows them down.

You must carefully design the method you use to add, remove, or move items from the Home & Idle Screens, to encourage user customization. The most common of the reasonably usable methods for smartphones involves press-and-hold to switch to an editing mode. However, users do not seem to recognize this as a universal feature yet; even when they are familiar with it on one platform, when they switch to another, they generally do not attempt to use the feature immediately. Hopefully, a standard will emerge or users will become more accustomed to exploring interfaces to discover interactions without clear affordance.

## Lock Screen

## Problem

Mobile devices must enter a lock/sleep state to reduce power consumption, to prevent accidental input, and sometimes to prevent unauthorized input. You must provide a screen to communicate this state clearly, provide key information, and assist with unlocking methods.

The device OS will provide a default lock screen, but some can be replaced or customized. Many full-screen modes, such as that for video playback, can circumvent sleep timeouts. Certain applications such as alarm clocks or navigation assistants may also benefit from entering a night mode which provides limited information. You may wish to provide a custom low-power sleep or lock screen for these experiences.

## Solution

![](images/4b3b21b3e045d52bf1e27bf45515c2e4c8d61b98348c7f925faf4192ca529c84.jpg)

![](images/81b4463d2ce6ebe7b7dbd64267fc13afa7f434b48ce97b77dd6ed680c488c76b.jpg)  
Figure 1-26. Two types of Lock Screens, clearly indicating they are locked, showing key information and indicating how to unlock the device (date, time, and system status above the rule have been removed for clarity).

When the device is locked or sleeping, a Lock Screen or sleep screen will be displayed. You should display key information about the device, or the context which provided the lock function, such as events, alerts, time and date, and instructions on how to unlock the device.

Lock screens are useful to prevent input, and power consumption is a real issue, but many lock screens go overboard. Backlight should be minimized or removed, but display drivers left on. In the past, most every device had a retroreflective screen, which could be read in ambient light. These are less common, but almost every screen can be read at least a little when looked at carefully.

Additionally, many devices have an excessively high minimum brightness. You can often access the display hardware more directly to provide a “super dim” mode for darker environments, or to reduce consumption without turning off the display entirely.

Pixel-illuminated technologies, such as OLEDs, provide other possibilities, now being exercised well on a few devices.

## Variations

The Lock Screen is displayed immediately after a deliberate (user-initiated) lock, or when waking from sleep but not yet unlocked. A similar screen is the sleep screen, which often has no display at all. These can, and should, still display some information.

Certain newer technologies, such as OLED, have no backlight. Clever design can illuminate just a few pixels, at low power, and display all relevant Lock Screen information at a very low power level, combining it with a sleep screen.

Screens displayed when the device is off but charging and similar special types of screens are comparable enough to Lock Screens to be considered the same pattern. You should display any useful information available to the device. For example, if date and time are stored at a low enough level to be accessed at this point (and they usually are), display that information as well as the battery status message.

![](images/8fd60ebba60c330ef5bbe33479da78fb146991ee4088af99638da5f6d7fad12d.jpg)  
Figure 1-27. A sleep screen, set up for an OLED device, with very few pixels illuminated. This presumes the device still differentiates Sleep from Lock, so the moon icon denotes sleep, and makes no mention of how to unlock

## Interaction details

Locking may occur based on an activity timer, or by deliberate user activation. Both systems are usually enabled. Deliberate user locking should use a hardware lock key, which may be a short tap of the Power key. You should not rely on menu selections and key combinations to activate Sleep or Lock state as they are cumbersome and will be unused.

If your device has a very low consumption display, or does not rely on batteries, consider whether a lock screen timer is needed at all. eReaders, for example, should generally just stay on the last page, indicating they are locked by adding an icon in the corner, but allowing viewing of the basic content. You should still provide a Lock Screen, for when the user deliberately chooses to hide what is on-screen, for example.

Some convertible devices (flip or slide form factor) only operate when open. These form factors will immediately lock when closed.

Unlocking may be accomplished via key input, screen interaction, or hardware state change (flip or slide). Figure 1-26 shows two of these. Most devices will require exiting the sleep screen first, and may only unlock once the unlock method is displayed on the Lock Screen. Many devices can use any of several methods, such as key input or sliding the keyboard open.

Unlock key input is usually a key combination (two keys must be held down simultaneously for a short time) or a key pattern (two to four keys must be pressed in sequence). These are not codes, but you may replace them with Sign On methods if additional security is required.

On-screen unlocking for touch and pen devices uses a simple gesture, such as a drag action, which cannot be easily reproduced by accident. The Lock Screen may be combined with the Sign On pattern to create a Secure Lock Screen. Unless on a high-security device, or required by policy, you should make this level of security a user-enabled feature, and not required or default.

Locking does not imply exiting or suspending applications. Even activities such as voice calls may continue when the Lock Screen or sleep screen has activated. You must carefully consider whether to allow the user to unlock without interrupting the process, and to display relevant information about the ongoing activity.

Certain actions may also be allowed to take place without exiting the Lock Screen. An ongoing voice call may be terminated, for example. You may design a widget that allows SMS messages received to be viewed and actually answered from the Lock Screen. These must be designed so that they are unlikely to be activated by accident either by context (no ongoing call should be loose in the pocket, so End cannot be pressed by accident) or by requiring unlock-like action precision to initiate (responding to an SMS message requires tapping a small “respond” area, within a short time after receipt, and all other actions are disregarded).

## Presentation details

![](images/784503bab0a09c6784f411f966b2d9e140462811d634b538e15bfe9bfd26f892.jpg)  
Figure 1-28. Notifications and other actions may appear on the Lock Screen, or even allow limited interaction. Various methods are available, from gestures to small targets and limited time, to allow interaction without sacrificing security.

On the Lock Screen, you will display the time of day, the complete Annunciator Row, and any information or gesture targets to instruct or assist the user in unlocking. You should also indicate—usually with a lock icon and with text (“Phone is locked”)—that it is a Lock Screen. This should also be apparent by the lack of conventional controls such as soft-key tabs or menus, and from the lack of the Home & Idle Screens icons or widgets. By default, you should display the backdrop from the center panel of the Home & Idle Screens, but users may customize this to be a different image.

The sleep screen should display much the same information, but especially the time. Unlock methods will be suppressed, unless the device can be unlocked directly from the sleep screen. Ensure that the display can be seen and used most efficiently by the display technology available. If you are relying on retroreflectivity, make sure the items are of maximum contrast, and larger than usual. You should make the clock, for example, as large as will fit on the screen. For OLED screens, use outlines, and reduce the maximum pixel brightness, as shown in Figure 1-27. For ePaper, do not display the time at all unless a partial screen refresh can be reliably accomplished, without undue power drain.

You may also display additional information about alerts or notifications, such as that shown in Figure 1-28. The conventional Notifications methods should be used, except insofar as they might interfere with the operation of the Lock Screen, or could not be viewed without access which would be difficult without unlocking the device. For example, a large Pop-Up dialog on a touchscreen might cover the unlock gesture area; a smaller item may need to be developed for the Lock Screen.

Certain system messages may demand special screens. When the battery is dead, for example, the screen displayed should still follow the concept of a Lock Screen and sleep screen. If the clock is available, you should display the time and date as well. Display the Annunciator Row even though everything will be disabled. Replace the unlock instructions with critical battery or charge state information instead.

## Antipatterns

Mobiles are 24/7, always-on devices for their users. Do not dim the screen and/or cut the display by default. Consider the actual power drain, and other ways in which you can meet your requirements.

Consider all available display devices. If there is an external output for use with TVs or projectors, don’t just send the same signal, but something more suitable to the large display. Avoid displaying details of notifications by default (to preserve privacy), and do not display the Annunciator Row as that is about the device, not the display. Also, move the display elements around to prevent burn-in.

Do not make the Lock Screen display or interactions, including unlocking, too different from the design and interaction paradigms used on the rest of the device. If your device is touch-centric, do not rely on a complex hardware button method to unlock the screen.

Avoid using key combinations to unlock which may disrupt ongoing functions. I have devices that use the End key to control all sleep states. The only way to wake them up is by tapping the End key—which also hangs up an ongoing call. Once the device has gone to sleep, there is no way to mute, switch to speaker, or initiate a three-way call. Avoid these sorts of conflicts at all costs.

## Interstitial Screen

## Problem

A delay is encountered before a requested screen can be loaded. You cannot or should not continue presenting the information previously displayed.

Interstitials exist in all types of interactions, from starting the device to waiting for results in web applications.

## Solution

![](images/712ff88663405efdc560291f13dcf085df446cdead27bac910aa987319f05632.jpg)  
Figure 1-29. Interstitials display the context as a title and by saying what is being loaded, and they indicate activity with a moving progress bar or a spinning general loading indicator. If the process can be canceled, allow this with a button or, as shown here, a soft key.

You should use the Interstitial Screen pattern when:

• There is a technical limit that prevents display of the previous context. This is commonly encountered when starting the device, or when applications are loaded.

• Within an application, site, or process, the content presented will change enough that a clean break is required. Switching users, or changing or initiating information filtering (including some searches), are the types of situations that can cause this.

The interstitial is primarily a loading process screen. Whenever possible, you should use a Wait Indicator that occupies a small portion of the screen, or is within a Pop-Up dialog, to indicate a delay. See the Confirmation pattern for more on these, and Figure 1-29 for a simple example.

Whenever there is a sufficient delay and available space on the screen, you may also add Advertising to it without undue interference with the process.

Variations

![](images/b5a51d5cd95ea1b9f83f5c4117a31ba439d25b1419c86938385c2d7686097d5b.jpg)  
Figure 1-30. When loading an application especially, the entire screen can be taken up with branding, and the loading indicator overlaid on top of this. Be sure text titles are still loaded, and make every effort to use a progress bar and percentage or time remaining.

Only two types really exist.

The first type is the loading screen, which you can use when an app is loading or some other major change in state occurs. This screen is about context change, and you should very clearly label the service being loaded, to include major branding. There is more tolerance for vague timing, and simple “Loading” indicators—as shown in Figure 1-30—may be tolerated.

Try to avoid these, and load actual content as quickly as possible. Often, it is possible to rapidly load the last state (even as just a screenshot) or preserve the screen from which the change was initiated. You may load a Wait Indicator on top of this, which prevents access to the actual content, but it can trick the user into believing a speedier load process has occurred due to the amount of content on the page, and the customization. Many strategies to avoid loading an Interstitial Screen can only be implemented if supported by the OS, however.

The second type is the in-process screen, displayed when a delay is encountered inside an application, site, or process. You should strive to preserve context (by labeling and branding the existing application or service), and inform the user how brief the delay will be. In many cases, the key reason you use the Interstitial Screen is to indicate to the user how hard the service is working, so it is clear the user-submitted action was accepted, and to emphasize the value of the service.

For example, many search systems work well when displaying results on the same screen as the screen on which the terms were entered. However, if the search takes more than a few seconds, and if there is much competition in the space, there may be value in adding an Interstitial Screen to emphasize the power of the search taking place instead. Excessively fast searches can even be perceived by users as cheating, and the result viewed with some suspicion.

## Interaction details

![](images/19f4ea9441d08f6b9c0e17c8e30ce325b198f632f9869a5bdc70a2695e882720.jpg)  
Figure 1-31. If space allows, and the addition will not add confusion, advertising can be placed on the Interstitial Screen. Provide for interactivity with the ad whenever possible.

The Interstitial Screen is usually described as a required step, and does not have any interaction itself. Key device features such as the ability to switch applications or exit back to the Idle Screen should not be disabled.

If you display the screen as part of a system update, or something else where interruption could cause irreparable harm, clearly communicate this, and set this expectation before initiating the process. For situations like this, whenever possible, prevent disallowed actions such as power-off by disabling the buttons, as well as describing the function.

When the process may be canceled, you should load an on-screen button or soft-key tab (depending on the device) with this function clearly labeled. When the user selects it, the user will return to the last stable screen. Ensure that this screen, if part of a process, has an easy method for changing the path or exiting the entire process or application.

When you choose to display advertising on an Interstitial Screen, as in Figure 1-31, it should be as interactive as possible. Allow the user to select the ad to view details, purchase the product, and so forth. Load the ad link into a new application (a new browser window, or the application store) so that the ongoing process is not interrupted. If possible, communicate this (possibly with another interstitial!) when the remote site is loading.

## Presentation details

Branding should also be included. At least include an icon in the title bar, but the entire screen may be occupied with branding for loading screens, and in other cases.

Wait Indicators of one type or another should be used. See that pattern for details, and be as specific as possible.

Describe what is being loaded, and why. Much like “Submit” is too vague a button label, always say “Finding the best deals for you” instead of just “Loading.” If the screen is being displayed due to a critical system process, and features such as application switching are disabled, clearly communicate this.

When you provide a cancel function, the button or soft key should be labeled “Cancel,” or an equivalent label or icon should be used across the OS to denote the current screen or process is to be canceled. Although this may seem needlessly generic, and therefore in conflict with the labeling statements just made, this function is well understood by users when consistently implemented.

Additional spaces may be occupied with Advertising. However, ads must be clearly differentiated from the other messaging, so users are not confused by an apparent change in context, even if they glance away from the beginning of the screen being loaded. Simply labeling a message with the word Advertisement or similar is not an effective method of differentiation.

The advertising should not interfere with the user’s understanding of the application. Advertising should almost never animate, while the loading indicator will, to imply activity. See the Advertising pattern for some discussion of display methods.

## Antipatterns

Unless deliberately using a business model with a paywall, do not load interstitials purely to display Advertising.

Avoid using an Interstitial Screen for every loading condition. As much as possible, avoid locking during loading, use nonmodal Wait Indicators, use Pop-Up indicators, or load information fast enough so that it doesn’t need any indicator.

## Advertising

## Problem

You must place advertising into an application, site, or other service.

Advertising is heavily used in all aspects of mobile, from SMS messaging all the way to being integrated with the device OS.

## Solution

![](images/e673e396b51d466874a0ed9563ddc62b3498432aeb5a9179d869c891820fb09e.jpg)  
Figure 1-32. Advertising may be within the page, so it scrolls with content, or locked to the side of the viewport, and so does not scroll.

Many sites, applications, and even entire mobile services are ad-sponsored. If you must place advertising into a product, you must not try to hide the ads, nor make them so prominent that they damage the user experience. Generally, advertising is key to the business, and must be made as a necessary function of the product. Integrate advertising correctly, and well, or the product will be discontinued.

Advertising in mobile must be:

• Clearly differentiated from the content

• Clear, readable, legible, and able to be interacted with

• In the same place, and used in the same way, on each screen and in each state

• Unobtrusive enough to not interfere with the interaction of the actual product

• Easily actionable, so users can take advantage of the offer

## Variations

While numerous graphic variations are possible, you really only need to consider two key methods:

• Ads may be loaded within the content of the page, so they scroll with the page. These are usually near the top and bottom of any particular page, associated with the masthead/title and any links or functions in the footer. For very large pages, there may be additional advertising at key breaks in the middle of the page as well.

• Ads may, alternatively, be docked, or fixed in the viewport. This is an especially useful solution for applications with multitier access, where payment removes the whole layer. The rest of the screen scrolls as normal, but this element is locked to the edge of the viewport, much like a Fixed Menu.

Figure 1-32 shows both of these options. Advertising in text, such as information appended to an SMS message, is not discussed here, but the basic principles still apply.

## Interaction details

Your advertising should always be selectable so that the user may get more information or purchase the product. Make sure this link loads in such a way that it does not interfere with the existing process, such as by opening in a new browser window or launching the application store.

For tiered services, in which an ad is displayed for low-price or free access, you should provide a link immediately adjacent to the ad that allows the user to upgrade to the paid, ad-free version.

When designing for scroll-and-select devices, avoid placing advertising in such a way that the user must scroll past it to get to the actual functions or content.

## Presentation details

You must become familiar with the standards of advertising. Banners should always display in standard sizes. Ad providers can then use existing ad units, and do not need excessive production details, as they can follow standards published elsewhere. In most cases, you can just follow the sizes and other specifications published by the Mobile Marketing Association (MMA). Figure 1-33 summarizes these standards; complete specifications are available at http://www.mmaglobal.com/mobileadvertising.pdf.

![](images/602faf056e9261f2300042591e219d4dbd4589cb1786ff1b8cd2094eb5004080.jpg)  
Figure 1-33. The sizes of standard MMA banners and their suggested common screen sizes.

Only for very large devices, especially tablet-size devices, will you need to use other sizes. These will often be provided by others (such as ad services) or the smaller common desktop sizes can be used instead. Of course, the MMA tries to stay on top of trends, so it will continue to expand its offerings over time.

Display the ad in a manner that clearly differentiates it from the actual page content. There are three basic ways to accomplish this, each illustrated in Figure 1-34:

• Place the ad on a shaded, tinted, or colored background. Usually, the background should extend the full width of the page.

• Separate the ad from the rest of the content with rules, which must run full-width, or in a closed box larger than the ad.

• If the ad is slightly smaller than the screen width (by using one size smaller than the suggested size for the screen), use different alignment than the content. If content is left-aligned, right-align or center the advertising.

![](images/87e17cbf46d79ddcc3003043e603de0ce92d4dffc4fbf262f799de13013e2c62.jpg)  
Figure 1-34. The three methods of differentiating an ad from the surrounding content.

When your ad is in a docked area, it should usually be docked at the bottom, and is considered to be one layer above the content. A Revealable Menu will overlap the advertising when open. The ad may be placed at the top when fixed menus are used, or when closed reveal menus would interfere with display. Advertising may be seen as a strip immediately above a Fixed Menu, and this can work, but it can become cluttered, and runs the risk of accidental activation.

Advertising may be integrated with the content, such as in a list of results. The advertising should not be counted as a line item, and so will not be numbered or included in result totals, nor should it use the guidelines covered in the rest of this pattern to visually differentiate it from the rest of the content. Typical uses of this are to have the first and last items in a page of results be sponsored.

When you display advertising in a list of other items, consider the available space and do not overload it with content. Although three sponsored links above a list may be acceptable on a desktop device or large tablet, it may be totally unsuitable on a small handset. The small viewport can also be used to add additional ad spaces; an extra ad can be provided in the middle of the same list. Interrupting about every one and a half screens can provide a useful break to the scrolling.

The ability to select the ad should be clear. Provide a link or button in the ad whenever possible. If there is insufficient room for this, use the current interactive standard method to indicate a link, such as underlined text or a border on the image.

## Antipatterns

Mobile is generally so task-focused that failures in advertising—that make it too obvious or confuse it with the content—may cause an immediate loss of customers. Even casual activities such as gaming generally draw the user’s focus, so an overly intrusive ad will result in dissatisfaction. Follow the guidelines here (and on the MMA website listed earlier).

When conducting user research, be sure to include real ads and do not carefully pick them to match the design. Borrow from competing sites if necessary, but get realistic advertising or your test will be invalid.

Do not make ads too large, making the content difficult to read. This is especially key for small screens using docked advertising space. If this could be a problem, switch to the inline style.

There is almost never a reason to place a text label such as “Advertising” next to the banners. The design should be able to communicate this. If it doesn’t, fix the design instead of wasting space with labels.

You should almost never animate advertising. This will distract from the core content of the application or other process. If animation is absolutely required, use it very carefully and sparingly.

Make sure advertising in scrollable areas does not induce false bottom errors, making the user believe he has reached the end of the page content prematurely.

Do not use custom sizes for any banners. Advertisers will generally not go to the effort of making new sizes. All services you sign up for require that you abide by their guidelines, so your revenue base will be severely limited.

## Summary

## Wrap-Up

We just saw that a page is the area that occupies the entire viewport of the mobile screen during its current state. Within the page, a composition contains and organizes the appropriate components and content within that viewport. Mobile displays range in size, and on smaller devices, screen real estate is valuable and every pixel is important. Therefore, you should be aware of how little or how much room these components use when you are planning the UI layout. Mobile users want information access on the spot. So information that is displayed without hierarchy and structure will likely cause user tasks to be delayed or to fail.

When incorporating the page patterns into your design, consider:

• User needs, tasks, and reading goals based on context of use

• Principles of page layouts based on theories to ensure that the users can quickly identify the structure of the content

## Pattern Reference Chart

The pattern reference chart in the following subsection lists all the patterns found in Chapter 1. Each pattern is accompanied by a general description of how it can apply to a design problem while offering a broad solution.

Cross-referencing patterns are common throughout this book. Design patterns often have variations in which other patterns can be used due to the common principles and guidelines they share. These cross-referenced patterns are listed in the following charts.

## Chapter 1, “Composition”

This chapter described the composition as being a template, which contains or houses all the components and elements within a page. This allows the content to be consistently organized across the device’s OS, allowing users to have an easier time navigating, searching, and accessing it. The ability for the user to quickly recognize the content’s organizational structure will increase user learnability and satisfaction while decreasing performance errors.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td>Other patterns to reference</td></tr><tr><td>Scroll</td><td>More information is in the page or element than can fit in the viewport. A method of access to this information must be provided.</td><td>Scroll bars are displayed to indicate the scrollable axes, and the relative position within the scrollable area. Due to the scale of mobile devices, as a general rule scroll bars cannot be manipulated.</td><td>Infinite Area Vertical List Infinite List Accesskeys Directional Entry</td></tr><tr><td>Annunciator Row</td><td>The status of important hardware features such as battery level and network connections must be able to be discovered by the user with little or no effort.</td><td>A bar is displayed along the top of every screen with a series of iconic representations of the status of the device. Common representa- tions and placements of icons are used so that users can understand the key indicators on any device without having to be familiar with</td><td>Pop-Up On-screen Gestures Notifications Icon LED</td></tr><tr><td>Notifications</td><td>A method must be provided to notify the user of arbitrary notifications, of varying priority, without unduly interfering with existing processes.</td><td>the specific device. A single, consistent notification method is provided across the entire OS. This method does not interfere with any processes the user is currently involved in, and can be acted upon or dismissed very easily.</td><td>Annunciator Row Pop-Up Confirmation Titles LED Tones</td></tr><tr><td>Titles</td><td>Every key element should be labeled to make context or process completion clear.</td><td>Pages and elements or content sections within a page should almost always be labeled. Titles must be used in a consistent manner, in terms of size, location, content, and style. The simplest method for pages is a straightfor- ward title bar.</td><td>Haptic Output Voice Notifications Notifications Vertical List Infinite List Thumbnail List Fisheye List Carousel Grid Select List Confirmation Sign On Exit Guard Timeout Windowshade Pop-Up</td></tr><tr><td rowspan="5">Revealable Menu</td><td rowspan="5">Not all functions for a page can or should be presented on the screen. A method must be provided to access these optional functions. options or controls across the</td><td rowspan="8">By selecting a key, selecting a small on-screen element, or performing a gesture, an option menu is displayed with content relevant to the current state of the application. controls or options should be visible at all times.</td><td>Fixed Menu Vertical List</td></tr><tr><td></td></tr><tr><td>Pop-Up</td></tr><tr><td>Thumbnail List</td></tr><tr><td>Select List</td></tr><tr><td rowspan="9">Fixed Menu There is a need for access to</td><td rowspan="9"></td><td>Accesskeys</td></tr><tr><td>Icon</td></tr><tr><td>Button</td></tr><tr><td rowspan="6">An always-visible menu or control set is docked to one edge of the viewport. This is often used for media players, cameras, and other applications where a key set of</td><td>Revealable Menu Annunciator Row</td></tr><tr><td>Titles</td></tr><tr><td></td></tr><tr><td>Vertical List</td></tr><tr><td>Pop-Up</td></tr><tr><td>Icon Button</td></tr><tr><td rowspan="6">Home &amp; Idle Screens</td><td rowspan="6">A default condition must be available for display once the device has started, and to return to when all other processes and applications have exited.</td><td>All mobile devices have an Idle Screen, originally when the device</td><td>Lock Screen</td></tr><tr><td>is not doing anything (it is idle).</td><td>Grid</td></tr><tr><td>This is used as a launching point</td><td>Film Strip</td></tr><tr><td>or when the user is not specifically asking anything of the device.</td><td>Thumbnail List</td></tr><tr><td></td><td>Icon Link</td></tr><tr><td rowspan="5"></td><td></td></tr><tr><td rowspan="5">Mobile devices must enter The Lock Screen is displayed a lock/sleep state to reduce immediately after a deliberate power consumption, to (user-initiated) lock. Key informa-</td><td>Pagination</td></tr><tr><td>Location Within</td></tr><tr><td>Sign On</td></tr><tr><td>Annunciator Row Home &amp; Idle Screens</td></tr><tr><td>and date, and instructions on how Notifications</td></tr><tr><td rowspan="5">Interstitial Screen</td><td rowspan="5">this clearly, and assist with unlocking. A delay is encountered before a requested screen can be loaded. The information previously displayed cannot or should not be displayed.</td><td>tered when starting the device, or</td><td>Pop-Up On-screen Gestures</td></tr><tr><td>The interstitial is primarily a</td><td></td></tr><tr><td>loading process screen. Use it</td><td>Wait Indicator</td></tr><tr><td>when there is a technical limit that prevents display of the previous context. This is commonly encoun-</td><td>Confirmation</td></tr><tr><td>Advertising</td><td>Pop-Up</td></tr><tr><td rowspan="5">Advertising</td><td rowspan="5">Advertising must be placed in an application, site, or other service.</td><td>when applications are loaded. Sometimes a necessary function</td><td>Revealable Menu</td></tr><tr><td>of the product, advertising must</td><td>Fixed Menu</td></tr><tr><td>be integrated correctly, clearly differentiated from the content,</td><td>Link</td></tr><tr><td></td><td></td></tr><tr><td>readable, legible, and able to be interacted with.</td><td>Button</td></tr></table>

## Additional Reading Material

If you would like to further explore the topics discussed in this chapter, check out the following appendix:

Appendix C, “Mobile Typography”

This appendix provides additional information on appropriate use of message display characteristics, including typography, legibility, and readability guidelines, as well as further information on today’s mobile display challenges and capabilities.