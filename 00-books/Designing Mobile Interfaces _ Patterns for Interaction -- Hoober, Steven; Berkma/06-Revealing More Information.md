# Revealing More Information

## It’s Not Magic!

The audience stares, transfixed, at the man on the stage, hoping to catch a glimpse of his strategy. The man waves a black top hat around, showing its form and lack of contents to the interested spectators. Next, he places a red silk handkerchief in front of the hat. Shouting “Voilà!,” the man drops the cloth and reaches into the hat. As the audience “Oohs!” and “Aahs!,” a white rabbit hops out of the magician’s hat.

## Context Is Key

Magic tricks are exciting because we are challenged to figure out what just happened and how it fooled us. We’re left to ponder and to discuss with one another the magician’s strategy and skill. This curiosity of what and how information is revealed is entertaining to us.

But guessing is not acceptable when designing mobile interfaces. On mobile devices especially, we want to eliminate the confusion. Our users are not stationary, nor are they focused entirely on the screen. They’re everywhere, and they want information quickly and to locate, identify, and manipulate it easily.

## Understanding Our Users with Norman’s Interaction Model

Magic confuses us because it takes advantage of our cognitive processing abilities.

Donald Norman tells us there are two fundamental principles of designing for people (Norman 1988):

• Provide a good conceptual model.

• Make things visible.

A conceptual model, more commonly known today as a mental model, is a mental representation—built from our prior experiences, interactions, and knowledge—of how something works. It’s our representation of how we perceive the world.

The second principle, “make things visible,” is based on the idea that after we have collected, filtered, and stored the information, we must be able to retrieve it in order to solve problems and carry out tasks. Norman indicates that this principle is composed of smaller principles such as mapping, affordances, constraints, and feedback.

![](images/623c1f7f1cadfa925fc408ec188483d6a67e388a75239a431f0b297a83711347.jpg)  
Figure 4-1. Pop-Up dialogs, regardless of what they look like, are used to present any controls or information the user might need, within the context of the parent page or data object. If you want to move a photo or edit an address, a Pop-Up where the image or contact is visible in the background is often the best way to do it.

## Mapping

Mapping describes the relationship between two objects and how well we understand their connection. On mobile devices, we’re talking about display-control compatibility. On a mobile device, controls that resemble our cultural standards are going to be well understood. For example, let’s relate volume with a control. If we want to increase the volume, we expect to slide the volume button up. If we want to read more information in a paragraph, we can scroll down, click on a link, or tap on an arrow. Problems occur when designs create an unfamiliar relationship between two objects. On the iPhone, in order to take a screenshot, you must press and hold the power button and home button simultaneously. This sort of interaction is very confusing, is impossible to discover unless you read the manual (or otherwise look it up, or are told), and is hard to remember.

When designing mobile interfaces:

• We should use our knowledge of cultural metaphors. We understand that an “X” icon, when clicked, will close the page or window with which it is affiliated.

• We should use proximity. Make sure the display and control you are using have a proxemic relationship. In other words, an indicator whose function is to expand or reveal more information must be close enough to the information it will affect.

## Affordances

Affordances are used to describe that an object’s function can be understood based on its properties. For example, a handle on a door affords gripping and pulling. The properties of the door handle—its relative height to our arm’s reach, that the cylindrical shape fits within our closed grasp—make this very clear. If an object is designed well and clearly communicates its affordance, we don’t need additional information attached to the design to indicate its use, such as signs and labels.

When designing mobile interfaces:

• We expect all buttons to do something and change a display’s state.

• We should consider that physical buttons afford pushing, pulling, or turning.

• We should consider that screen buttons afford touching, selecting, and clicking.

• Depending on context, images, words, and graphics may afford selecting.

• If we cannot recognize that an object is supposed to reveal more information, the user will ignore it, assume it is decoration (and therefore not functional), or not understand how to interact with it. Interfaces that have no affordances, such as interfaces that require gestures but have no indicators at all, are a real concern in this area.

## Feedback

Feedback describes the immediate, perceived result of an interaction; it confirms that action took place and presents us with more information. In a car, you step on the accelerator and that action has an immediate result. The feedback is that you experience the car moving faster. On mobile devices, when we click or select an object, we expect an immediate response. Feedback can be experienced in multiple ways: a button may change shape, size, orientation, color, or position, or very often a combination of these. A notification or message may appear, or a new page might open up. Feedback can also appeal to other senses using haptics (vibration) or sounds.

When designing mobile interfaces:

• Be sure to design actions that result in immediate feedback. This will limit confusion and aggravation while making the user’s experience more satisfying. Delaying feedback can even result in the user performing other actions and spoiling the process.

• Create a change of state (contrast, color, shape, size, sound) that is measurably differ ent from its initial state.

• Use confirmations when user data could be at risk of being lost. See Chapter 3 for more information.

## Constraints

Restrictions on behavior can be both natural and cultural. They can be both positive and negative. You may remember playing with a toy consisting of different colored plastic shapes and a cylinder with those shapes as cutouts on the cylinder’s surface; the idea was to fit the yellow cube, for instance, through the square cutout in the cylinder; the red triangle through the triangle cutout; and so on. The cube would fit through the square cutout, but not the triangle cutout, and so forth. The size and shape of the objects are constraints in making the correct fit. This is an example of natural constraints (though still learned). Cultural constraints are applied to socially acceptable behaviors. For example, it’s not socially acceptable to steal from someone or throw your friend’s phone out the window to get her attention.

When designing mobile interfaces:

• Use constraints to reduce or prevent user error. When you accidentally press Delete instead of Save, you should be provided a constraining confirmation message that requires your action.

• Use constraints to fit content and interaction to the size of the viewport, and the device.

• Use constraints so that unimportant buttons become inactive but remain visible.

Norman’s Interaction Model is a framework that you should refer to when using patterns to reveal more information. For a better understanding of his model, refer to his book, The Design of Everyday Things (Basic Books).

## Designing for Information

A good way to start thinking about the topic of interactive design is that it is about displaying information. A discussion of detailed information architecture is beyond the scope of this book. However, interaction design as it pertains to presenting detailed information and results is well within the scope of our discussion.

Displaying detailed information requires an understanding of the user, his context and goals, and the information available. In many cases, information should not be hidden behind a link or other action, and should be immediately available; how useful would the clock on your mobile be if it was behind a “Current time” menu item?

If this seems extreme, consider many of the systems we encounter every day, and that are regularly griped about. For example, say you’re checking on an airplane flight. Once you sign on, most airline websites still require that you click on your itinerary and so forth to simply find out whether the flight is on time—even if you only have one flight stored under your identity.

But much other information is of a second-tier nature, and demands user input to be displayed. You must decide:

## How to access the information

Access methods, such as links, are discussed in Part III, in Chapters 5 and 6. The patterns in this chapter are almost entirely used for “drilldown” or getting further information, but explicit decisions must be made about the information architecture and must be understood by the project team if they are to make the right decision.

## How to display the information

Display may be of two different types:

## Display the full page

Full pages are generally part of a process, and the user should ideally not have to go back to the previous page in order to view other information. Doing this repeatedly can be perceived as bouncing back and forth confusingly (i.e., pogo sticking). However, for processes where large amounts of content will be entered or consumed, it is the correct method.

## Reveal in the context

For information that can be understood through just a quick glance, or to help the user decide how to proceed, the information should be revealed quickly and easily within the context. A Pop-Up is a contextually revealed item, because the dialog is visibly a child of the page from which it was spawned.

Sometimes the simple facts of the information available will demand full-page presentation of information where the user’s context and tasks may otherwise demand that it be displayed in context. Use access and display widgets carefully to provide access to the information, or reconsider whether the information architecture can be redesigned to make this simpler.

## Patterns for Revealing More Information

The most common method of revealing information, that of displaying another page entirely, is not covered in these patterns, simply because there is very little to say about it. Linking widgets and the many display patterns, such as those listed in Chapter 2, cover these functions. In some cases, patterns listed in other places offer alternative methods, and these will usually be cross-referenced within the pattern. For example, Windowshade is very similar to Fisheye List and the two may both be used for the same purpose when implementing the same product on different platforms.

The patterns detailed in this chapter are concerned with specialized methods of presenting more information, which have no other uses (Lynch 1960):

## Windowshade

This pattern is used when a displayed element must be able to easily reveal a small or medium amount of additional information, without leaving the current context or page.

## Pop-Up

This pattern is used when a displayed element must be able to easily reveal a small or medium amount of additional information, while remaining associated with the current context or page. See Figure 4-1.

## Hierarchical List

Use this pattern when a large set of information must be presented. The information is hierarchically ordered, and this structure is relevant to the user.

## Returned Results

When users have explicitly requested subsets of information, the narrowed data set that results must be displayed in a meaningful manner.

## Windowshade

## Problem

You are displaying an element that must be able to easily reveal a small or medium amount of additional information, without leaving the current context or page.

Although the Windowshade pattern is built into many application frameworks, it will require scripting in web browsers, and so will not work in some older or low-end devices.

![](images/7f2b8c6fdb637ef115a13d5bca45a2badfe11321976f7c22032ff625f9fbd72a.jpg)  
Figure 4-2. The apparently normal Vertical List on the left reveals itself on the right to be a Windowshade list when an item is selected and the line item expands to reveal additional information. The arrow icons give a hint as to this extra information.

Items are provided with an indicator to imply that more information is available, generally by defining upper and lower bounds or by enclosing the indicator in a box. When selected, this area expands vertically to display additional information or interactive elements, as shown in Figure 4-2, including additional links and input or form areas.

The term windowshade implies that there is a small container that expands downward (similar to a roll-up window shade in a house). Other terms are used to describe these, but this one is unique and is the least ambiguous.

Do not confuse this with the Fisheye List. Windowshade requires an explicit action from the user to open. It may be used as an alternative to the Fisheye List for devices without a hover state, such as those where touch/pen is the primary or only interface.

## Variations

The basic interaction is very simple, and limited. The available variation is in the selection of the bounding area and indicators of the action itself. Three basic types exist:

• The title of a section may be used as the only visible item. When expanded, this becomes a title bar forming the top of the expanded area.

• For pages or other areas that are relatively strictly vertically oriented, top and bottom bounds can be defined around an area. Any number of summary items may be in this area, and when selected, the bottom bound slides down to reveal even more information.

• Similarly, for design purposes or because the whole width is not occupied by the content, the summary information is in a complete box of some sort. When expanded, the bottom of the box slides open in a downward direction. When open, the box is still complete, and contains the entire expanded content.

You must explicitly and deliberately select a model during design of either one-open (all others close when one Windowshade is selected and opened) or all-open (the user can open or close as many as she wants). There is no absolute answer; it depends on the type of information and how the user interacts with it. Lists, for example, should usually be one-open, but the visually similar faceted search options list should be all-open.

Horizontally expanding items are plausible, but you should use them only when the overall design of the element—or preferably of the entire OS—is arranged along this axis. Some desktop websites use vertical labels along the sides, and when selected they open to reveal the content of that section. A mobile interface could operate in the same manner.

Interaction details  
![](images/934a901f1ad5329af6cc1a172fc6e89bddc34791bf61029389e2490674d54289.jpg)

![](images/b2d0744c718e71eeed015f33890c71b32f488b13f82cb4f08744c5e73ed4c98b.jpg)  
Figure 4-3. A boxed title element becomes a larger boxed informational area when it is a Windowshade.

Interacting with a Windowshade should be very simple. Selecting the closed area using whichever method is available and preferred by the user will expand it.

If you have placed several elements in the closed state, the expansion function must be a clearly defined single Icon, Link, or Button. Selection of other items in the closed state will therefore still be allowed, such as going straight to a new page from another link in the closed state. Use this carefully, and leave plenty of room around the controls to avoid accidental activation.

You should always make a control available to close the expanded area. This should almost always be the same control as the open control. It may be an explicit control, or when it is a bounded area such as the title bar, the closed content area at the top of the expanded area. See the two states in Figure 4-3.

No automatic scrolling should take place during opening. The area will expand downward, even if it goes out of the viewport. You should make an exception if almost none of the expanded area is visible. To make it clear that the action has occurred, the page may scroll up enough to reveal that additional information has been made available.

Presentation details  
![](images/3f4a5ea4846f92d38d5f2ddf0e68f6bae58e00a785dcb653e4105a3f82f2d7aa.jpg)

![](images/1abac345b9a4fb3ff37be6cd89eb665ca3bd3d961b323b999062c524241496c2.jpg)  
Figure 4-4. Windowshade modules can be used for narrower layouts, not just full-width.

You can expand any element using this pattern, even those much smaller than the viewport, as shown in Figure 4-4. Be careful to never expand an item in such a way that it is much larger than the viewport.

Except as described earlier, do not scroll or move the title or other elements that are visible in the closed state when the area expands. This acts as an anchor for the user to understand what has happened to the display. For this reason, most Windowshade areas use a title alone for the closed state label.

An indicator should be adjacent to the title or integrated into the closed state label. Down arrows and “Expand” text are typical. These indicators (whether graphics or text) will change to indicate the state. When they are open, you should change the state, to an Up arrow or “Hide” text, for example.

Design any bounded areas, whether lines or boxes, to be clearly perceived as boundaries, and not just background design elements. They must function this way both when expanded and when collapsed.

![](images/fb0173fc96ee921e5c32b70e9306b66749047543b36aaadd34e63f2877fefd8b.jpg)  
Figure 4-5. Do not use Windowshade without indicating a bounding area around the expanded area, or the collapsed area, for that matter.

Avoid use of this pattern without sufficient bounding of the labeled area. Do not simply expand titles, links, images, or other general areas (see Figure 4-5).

Don’t break bounds when opening an area. If a box expands, make sure there are sides for the entire vertical space, not just the closed state, then gaps, then a bottom.

Use iconography or other indicators to make it clear the item will expand in place. Generic links or “more info” indicators may cause confusion as to the expected action; as a result, you will reduce the rate of clicking items, or users will not immediately understand they are on the same page.

When possible, use animation of any sort to indicate the opening action. Even if this is a stand-in, and displays only an empty box during the opening (then fills with content when open), this is better than the entire box simply appearing. Users may otherwise believe they are viewing a different page, or a Pop-Up.

Try to avoid areas that expand to be larger than the viewport. If larger expanded areas are used, this may cause confusion regarding what section of the page is revealed, especially if the Windowshaded items are routinely opened and closed.

## Pop-Up

## Problem

You must display a small or medium amount of additional information, while remaining associated with the current context or page.

Pop-Up dialogs are built into pretty much every mobile platform, and for many other methods they can be used to build custom versions. Many of these have enough built-in functionality that they may be misapplied, so use them carefully.

## Solution

![](images/4eece1916226a5a1d89aee5811c4f9ff8c34705b0107ba1e99cd0eb7029065ac.jpg)  
Figure 4-6. A typical floating Pop-Up, with functions such as buttons inside the window.

A Pop-Up is a child “page” that is smaller than the viewport and that appears on top of the parent page or displays context that spawned it.

For mobile, these should almost always be “modal,” with the Pop-Up having exclusive focus. Elements on the parent cannot be accessed without dismissing the Pop-Up.

The parent can be seen behind and around the Pop-Up, but should be clearly disabled.

## Variations

Pop-Ups may be free-floating, with space around all sides as in Figure 4-6, or may be anchored to one side of the viewport or parent window, as in Figure 4-7. Anchoring to the top is useful when the Pop-Up is related to a condition in the Annunciator Row or another top-margin item, such as the URL strip of a browser. Anchoring to the bottom is most useful when on a device with soft keys, or soft-key-like on-screen buttons, which will be used in place of button actions within the Pop-Up itself.

The content of a Pop-Up may be absolutely anything, including all the other types of content or interaction described in the rest of this book.

If room allows, and there is value (viewing content on the parent, or providing access to other on-screen elements such as virtual keyboards), the Pop-Up may be moved around the screen.

For larger devices, such as tablets, or in rare cases for handset-size devices, you may find that a nonmodal or “semimodal” Pop-Up is the best choice. This means the parent window can be interacted with, or clicking outside the dialog dismisses it. You have to base this decision on the expected use of the entire system, such as the relationship between the content on the parent window and the Pop-Up. Whatever choice you make, try to enforce it rigidly across the entire application.

Interaction details  
![](images/fa1596402221578b02917aeab0bf517d697beb5ba4652c95afecd63a7a0b5b3f.jpg)  
Figure 4-7. A Pop-Up anchored to the bottom, with soft keys logically and visibly attached to it. Simple forms, such as sign-on, can reside in Pop-Ups.

Only allow one Pop-Up to be open at a time. This is easily solved by simply not allowing access to the parent, but since this is sometimes possible, it is a good principle to keep in mind.

Opening a Pop-Up can be allowed via a typical Link, or as a result of other user or system actions. There is no universally recognized design method to launch or make the user aware that the action will load a Pop-Up. Within an application or service, however, try to use Pop-Ups consistently so that the user can learn which items load new pages, and which pop up instead.

Always allow your Pop-Up to be dismissed. Even for a step within a required process, the Pop-Up should be able to be dismissed, so the user may view his context and take other actions that may only be allowed within the full page. Dismissal may be via a dedicated function such as a “Close” icon in the corner of the dialog, or as a part of the primary content such as a “Cancel” button adjacent to the submit functions. If a dedicated “Back” function is provided, this should usually dismiss the dialog also.

Actions the user must take within a Pop-Up should be considered “page-level.” Whether the user is agreeing that he has been presented with information, is confirming a condition, or is submitting form information, use buttons (or button analogs such as soft keys) to commit the action. Buttons imply page submission or major action, so the dismissal of the Pop-Up will be expected.

Avoid scrolling within a Pop-Up. Long text elements, such as legal agreements, should be in full pages, and not Pop-Ups. Selection lists within Pop-Ups may scroll, however. They may work best with only portions of the Pop-Up scrolling, instead of the entire frame. This will allow any submission buttons to be revealed at all times, making the presence of actions clear, even if the actions are forbidden until scrolling has occurred.

A Select List is often used to select large numbers of items, even in a Pop-Up dialog. The single-select variant is most useful as you can use a single action to make the selection and you do not have to have additional controls fixed in the dialog or elsewhere in the viewport.

When the device OS uses soft keys or soft-key-like on-screen buttons, you can place buttons that control actions in the Pop-Up in there. This is nice because you do not have to fit these two buttons inside the smaller window. If additional actions are required, they may be loaded in any way needed, such as buttons in the Pop-Up, as a single Select List, and so on. Use the soft keys for primary supporting actions, such as “Cancel,” as shown in Figure 4-8. Avoid disregarding soft keys entirely, for consistency of the interface.

Presentation details  
![](images/49cb71cac60fdeb6f9c20f9b01ed62e0d48d87b5875d682e7dda8596dc83490e.jpg)  
Figure 4-8. A floating Pop-Up with associated soft keys. A scrolling list of selectable items or actions is within the Pop-Up.

Make sure the Pop-Up is clearly defined as not being a portion of the page. Use OS-level framing and other treatments to make this clear. Shadows are another valuable way to differentiate the Pop-Up.

Control items especially, including close buttons, and soft keys should appear similar or identical to the OS standard controls. This way, users will not have to learn a new interface language.

Controls should also be as clear as possible so that Cancel, Accept, and Close buttons or functions are immediately obvious to the user and require no interpretation.

The state change of not just loading the Pop-Up but also obscuring the parent is also critical to communicating this. The parent should usually be overlaid with a white tint or black shade that allows the user to view the content, but is different enough that it is clear the content and interactive elements are superseded by another.

When the Pop-Up is nonmodal or the content of the page is key to making choices within it, the background should not be obscured. Be sure there is sufficient border, shadow, or other treatment on the Pop-Up to ensure that it is clearly recognized as a different element, on top of the page.

![](images/a160958588cb224a3a7c765d79feb1ebb784e80c876e785ae26e385ddb05a64d.jpg)  
Figure 4-9. Do not let a Pop-Up spawn another Pop-Up. Generally, Pop-Up windows only work when modal, so anything that can cause more than one to appear is bad.

For small devices especially, such as handsets, consider ways to avoid using Pop-Ups. Generally, there are other solutions. Many mobile browsers and OSes do not deal with Pop-Ups well, and may display them poorly or confusingly.

For devices with soft keys or soft-key-like on-screen buttons, avoid use of buttons within the Pop-Up. Anchor to the bottom of the screen (or whichever side has the buttons) and use those instead.

Do not allow a Pop-Up to spawn (be the parent for) another Pop-Up (see Figure 4-9).

Do not overuse Pop-Ups by including navigation, tabs, and so on. Present the single information or interactive concept, and then allow the Pop-Up to close when the user dismisses it or the task is completed.

Do not display a Pop-Up exclusively to present advertising. If an Interstitial Screen or Advertising is required, use a full-screen display instead. However, actual content, even if heavily branded or ad-funded, is reasonable as long as it is relevant to the page in some way and was requested by the user.

## Hierarchical List

## Problem

You must present a large set of information. The information is hierarchically ordered, and this structure is relevant to the user.

Arrangement of information is a purely design-oriented task, and except for some interactive methods that may be difficult to accomplish on nonscripting browsers, this may be used anywhere.

## Solution

![](images/095e66f0de9d9d70b3afc106a7b8ce261ed2dfaf55fa79f8da6e8f4c5bbb8eaf.jpg)  
Figure 4-10. A Hierarchical List that is folded, with no children visible.

A Hierarchical List can display hierarchically ordered information in a comprehensible and quickly accessible manner. The parent-child relationships are exposed visually (Figure 4-10), and users may fold and unfold the list to view only the parts they need (Figure 4-11).

Displays of this type can be supported by even very simple interactions, with vertical scrolling only, and in surprisingly narrow spaces.

The depth of the list (the number of tiers included) is arbitrary, but it depends heavily on the size of the display area and the complexity the user is willing to endure. Typically, more than three tiers is quite complex, and it may be worth it to consider redesigning such lists just from an architectural point of view.

The user’s exploration of this hierarchy, by opening and closing items, is critical to her understanding of the relationships. Do not reveal too much for the user, and allow exploration. When the ability to expand and collapse items is not available for technical reasons, consider other methods to display the information.

![](images/87b3b7bf5d5f719cc5bdbcaf04f6525a802ce54455bb90bf9a608b80d56c1e9a.jpg)  
Figure 4-11. A Hierarchical List opened to one tier. Note the counters on all parent categories, indicating the number of immediate children.

You may load a Hierarchical List that is either closed or open when first displayed to the user.

Closed lists only display the top tier, as a simple vertical list. The user must select a parent item to reveal any children within.

Open lists reveal a portion of the list when first loaded. This may be the expected location, the current location within a system, the last location used, or other relevant sections. Do not reveal arbitrary sections just to communicate that the list opens.

A key variation is in the methods of revealing (or hiding) child list items. This will have serious impacts on design and the information architecture (and sometimes even the organization of the data repository). These options are discussed in detail in the following sections.

![](images/6984712d4f21a39c5d5d5479c87e881d4a64e933021d34e9cf7ba8558820ca9b.jpg)  
Figure 4-12. A Hierarchical List comparing the “single” (left) and “dual” (right) parent methods. In the latter, the parent is only used to reveal children, and the first item in the child list contains details of the parent level.

Hierarchical Lists are types of lists, and usually are variants of the Vertical List. They may encompass most any other subvariant, and include features from the Select List, Thumbnail List, and so on, as needed.

You should consider ordering the list so that any item which is a parent to others is displayed “twice.” An example might help make this clearer:

## • Trees

– All Trees

– Deciduous

– Coniferous

• Shrubs

• Grasses

Here, the boldface items are currently selected items. By selecting “Trees” I have opened the subsidiary categories so that they may be selected as well. However, there is sometimes confusion over which tier is selected when the level below is opened. This solves that by giving a landing page, or default selection of “All Trees.”

Indicating a parent category like this is not always required or possible, depending on the data set, and in cases where the second listing of the parent element is not needed. For example, if selecting a US state and the list is by region, there is no value in selecting a region alone. The region parents may, on selection, only open or close to reveal the child states. The two variations are shown in Figure 4-12.

An interaction commonly used when not including parent items at subsidiary levels is to use dedicated reveal functions and allow the user to fold and unfold the list items directly. This decouples the opening and selection, but can induce other issues with comprehension. Consider the data set and users carefully.

In this case, selection of a parent again will collapse or hide the child listing of that parent.

For lists where the “reveal” action is separate from the list item itself, selection of the item title will typically select or load more information (depending on the user task). Selection of the reveal item will immediately display the children of that item.

Selection of the “hide” action (the reveal becomes a hide when open) will collapse or hide the indicated child listing.

## Presentation details

![](images/a597f9a2298106a6517e4804fe018e6463b16d97ff7853109dd1395a60738392.jpg)  
Figure 4-13. Other common indicators that an item in a Hierarchical List is a parent (and may be opened) are + and − symbols. Note that in most cases, an icon for the leaf node is also used.

Make sure you have a good understanding of the hierarchical relationship of all items before you begin designing. Use position as the primary indicator of the hierarchical relationship between items. Top-tier items will be left-aligned; the second tier indented slightly; and so on.

Indicators should be present to make clear that the list may be opened. Arrows or plus symbols (Figure 4-13) are most common. In many cases, the indicator will reside in the left column, and indenting will correspond to the width of the indicator. Text indicators such as “More...” can be useful in small quantities, but they take up much more room than graphics for small screens, and for larger quantities the repetitiveness can make them difficult to scan.

Indicators of position and action in the Hierarchical List are basically just a repeated, very well-ordered version of the Indicator pattern. See that pattern for guidelines on position, shape, and interaction details.

![](images/5c287f5fc010cfcd67db88ebaa80f6e9cec1f57454d82cbec64275adb03ea760.jpg)  
Figure 4-14. A Hierarchical List with lines depicting the relationships between tiers.

A count of items within a parent category can be very useful to both indicate that there are additional items, and—for some data sets—to help the user decide which categories to explore. These line-level counters are not quite the same as Pagination or Location Within widgets, and are more like yet another Indicator of the “content beyond” type.

When a set of child pages is revealed, the indicator should change state to indicate that it can be used to close or hide the list.

Additional indicators of hierarchy may be useful, such as type weight (bold for parents, especially when not selectable), color, and size. An optional but well-used method is to provide guidelines among and between list items at different tiers, as shown in Figure 4-14.

## Antipatterns

Use caution with excessively complex interaction methods. Simple devices that require option menu selection, or actions that are difficult to discover, such as unique gestures, may impede use of the list.

Likewise, avoid trying to express overly complex list hierarchies of information with simple lists like this. Generally, after more than about three tiers of information, the relationships between the levels of information become too complex to be immediately understood.

Avoid opening too much of the list on entry. On smaller screens especially, it may be unclear how the list is ordered, or the parent-child relationships may be unclear at first glance.

Consider the task at hand, and the user’s need to understand the system. Many data repositories are hierarchical, but the architecture may be unimportant to the user. Do not reveal internal process, organization, or jargon unless needed by the end user.

Do not force an informational hierarchy on a data set just to use this display method. The user will adopt a mental model of the system or information that is incorrect, or will never understand the information at any level.

Avoid using too many interaction methods alongside the Hierarchical List. For example, a Fisheye List may seem like a good way to provide some extra information before opening, but will likely add confusion. Items such as this that act in another axis are especially prone to adding confusion.

## Returned Results

## Problem

When users have explicitly requested subsets of information, you must display the narrowed data set that results in a meaningful manner.

Returned results may be suitably displayed with page refresh, and with any method you wish, and so can work just fine on any platform.

## Solution

![](images/dfd67439d0962eec8fb687a798ef78937c6f6ef212a5868cd416830d96fabd92.jpg)

![](images/ab0b02f4b69f71dfdeb48e7dd25e35eb96b9f5112d5a9b11a4111b141373e34c.jpg)  
Figure 4-15. A Returned Results list may be simple, include several lines of information (left), or use display methods such as the Fisheye List to solve display density problems.

You will show the Returned Results as an ordered list or other array. This may be a page, or as a Pop-Up displayed over other contextually relevant information (such as a map or graph).

In some cases, part or all of the information subset may be implicit or automatic, such as repeated searches and the use of sensors such as GPS as some of the input.

## Variations

The most common type of Returned Results is a simple Vertical List. Additional information, such as the order of results, relevance, and domain, must be presented as well. Addons may also be used when relevant, such as a Fisheye List or Thumbnail List, as shown in Figure 4-15.

You may also wish to present the information contextually, as an overlay or add-on to other information visualizations. This may include very small amounts of information, suitable for placing in an Annotation. These results will themselves be points, and may appear over maps, graphs, charts, and similar visualizations.

In certain cases, you might want to present prioritized information within the same display type. This may be customized information (e.g., stock information when searching for a company), or paid placement results. See Figure 4-16.

Even if multiple information types are offered, the most relevant display type should be presented by default.

## Interaction details

![](images/cd53b99a5d653270bf674131ed48aec2415a4f220406cb9220b92f5d26fcf009.jpg)

![](images/1ed1c207278c69272255e96a88993a9ab3732f43377489f0e9d637ce38d1dbc6.jpg)  
Figure 4-16. Returned Results may be accompanied by sponsored results (right) or other targeted information such as a graph of stock prices when searching for a company (left). Note that sponsored results are not included in the numbered listing.

Typically, items in the Returned Results list will need to be selected, either as choices for another process in order to view more details, or to start a process (such as navigating to the selection).

The selection mechanism may be the entire item, or a specific portion of the item display area. Be sure to use the correct type of selection and selection indicator for the process; choice selection will be different from viewing details.

Pagination or Location Within controls and indicators should always be used for list-type displays, and may be relevant for contextual display.

You can display multiple types of results on one page, as overlays, adjacent to one another, or as easily switchable alternative displays. For example, if a visualization overlay is used, the results may be more useful for some users as a list. Subsequent or related displays may be shown as adjacent panels of a Slideshow, as Tabs, or in other ways that allow the user to quickly flip between data sets.

Modifications to the parameters that resulted in the display of results (such as a text search string) should be easily accessible. They may be on the screen, available as options, or available for direct modification by going “back” to the previous screen. All parameters used, even those that were not directly selected by the user on the initial display of results, should be available for modification; see the Sort & Filter pattern. Less often, you may wish to use the Search Within widget to further modify the result set.

Presentation details  
![](images/c444b125a43fe6129b06077af15bab6547d5fc991767a4c0258524a197d75c7e.jpg)  
Figure 4-17. Returned Results laid over contextually relevant information: for the map (left) a point in two-dimensional space, for the graph (right) a vertical line representing values on a single axis, such as time.

Display the reason the results have been shown, generally as a title. If search results are being displayed, the search terms must be printed on the screen.

Number the results so that an order is clear. For devices with support for Accesskeys, make sure the numbers cannot be confused with the accesskey labels. Color, alignment, and treatment (e.g., light blue and italics) are generally sufficient ways to differentiate.

When space is available, and the relevance parameters can be clearly communicated, you can display the relevance as additional information with each result. This may be a relevance factor (a percentage is typical), by listing terms that are relevant, or by listing a summary of the information that is most relevant to the result. In addition to this, you can also include the implicit relevance of display methods such as position on a map. Distance from your location, or other physical measures, are similar, and you should display them in the same manner.

If the domain is not entirely restrictive (searching only internal documents) or entirely nonrestrictive (the whole Internet is available), an indicator of some sort must be placed by each result. Types of documents, when not all the same, should also be displayed, so the user is aware before he attempts to view a movie or download a file.

When information is displayed contextually, it should appear as an Annotation, as in Figure 4-17, with a pointer indicating the precise location in the contextual system, and a head that may be selected for information or contain a label of the item.

Paid placement results must be differentiated from the other results. They should not, for example, be numbered with the other results, and you should not count them in the total results in the Pagination or Location Within information.

Availability of the item for selection must be indicated. Whether the entire displayed area for the item is selectable, or only certain portions are selectable, an indication of selectability should be present. Each type must be differentiated so that links to view further details appear as links, and selection for a process appears as a choice.

## Antipatterns

Avoid error conditions for valid entry of information. Displaying errors for no results will dissatisfy users, so solve the problem for them. Options include:

• Expanding the search parameters; for local search, change the distance until results appear.

• Correcting misspellings, but not unless there are few or no results.

• Using common, similar searches to replace results.

• When no results must be displayed, making it clear that none was returned. Do not excessively obscure this message with paid placement, or other helpful information.

In all cases, inform the user of the results display of the changes, and offer an easy method to see the original results.

Use paid placement very carefully. Advertising revenue is a way of life for many products, but make sure items within the results list are at least slightly related to the original intent of the returned results list. Do not use paid placement “results” as a replacement for no returned results. When users figure this out, they will have less faith in all the results.

Avoid making parameters too difficult to discover, understand, or modify. Try to explicitly state all parameters, even if they are available via other interfaces; for example, results on a map may have the radius constrained by the zoom level of the map, but this may not be clear unless it is also available as a search term, or explicitly stated on the results display.

## Summary

## Wrap-Up

As you learned, components are sections of a page that may take up the entire viewport, occupy a smaller section, or even appear modally in front of other displayed elements. In this part of the book, you became familiar with specific component patterns and how to use these patterns appropriately to display and organize information. When used effectively, these patterns will allow mobile users to have an interactive experience that is enriching and satisfying. When incorporating these component patterns into your design, consider:

• The user’s needs and his task-specific goals

• How the user’s mental model and cognitive processing abilities will influence the design of the mobile interface

• The fact that the design must be visible, provide appropriate feedback, and use constraints to prevent and/or minimize human error

• That the context of use will dictate how, why, and what information is going to be accessed and interacted with

## Pattern Reference Charts

The following pattern reference charts list all the patterns found within each chapter described in this part of the book. Each pattern has a general description of how it can apply to a design problem while offering a broad solution.

Cross-referencing patterns are common throughout this book. Design patterns often have variations in which other patterns can be used due to the common principles and guidelines they share. These cross-referenced patterns are listed in the following charts.

## Chapter 2, “Display of Information”

This chapter described the importance of displaying information based on the user’s mental model and how we organize this information cognitively. Failure to abide by these principles will most likely cause the user to become lost, confused, frustrated, and unwilling to continue. To prevent this, this chapter explained research-based frameworks, tactical examples, and descriptive mobile patterns to use.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td>Other patterns to reference</td></tr><tr><td>Vertical List</td><td>Display a set of informa- tion, usually text or a text representation, that uses horizontal space inefficiently.</td><td>Rather than using horizontal space inefficiently, display a set of information vertically using an entire allocated space.</td><td>Infinite List Thumbnail List Select List Location Jump Search Within</td></tr><tr><td>Infinite List</td><td>A Vertical List is called for, but the information set is very large and is not locally stored, so retrieval time is inconveniently long.</td><td>Reveal small amounts of vertical information at a time because the information set is very large, and not locally stored.</td><td>Sort &amp; Filter Titles Vertical List Thumbnail List Select List Location Jump Search Within Sort &amp; Filter</td></tr><tr><td>Thumbnail List</td><td>A Vertical List is called for, but additional graphical information will assist in the user's understanding of items within the data set.</td><td>Use a Vertical List with additional graphical information to assist in the user's understanding of items within the data set.</td><td>Wait Indicator Vertical List Select List Infinite List Carousel Grid</td></tr><tr><td>Fisheye List</td><td>A scroll-and-select device is targeted, and a Vertical List is called for, but small amounts of additional information can be displayed that would assist in the user's task.</td><td>When a scroll-and-select device is targeted and a Vertical List is called for, this can be used to reveal small amounts of additional information that can assist in the user's task.</td><td>Titles Vertical List Windowshade Pop-Up Pagination Location Within</td></tr><tr><td>Carousel</td><td>Present a set of information, most or all of which consists of unique images, for selection.</td><td>Display a set of selectable images, not all of which can fit in the avail- able space, but that can be scrolled through using many methods.</td><td>Titles Pagination Location Jump Grid</td></tr><tr><td>Grid</td><td>Present a set of information, most or all of which consists of unique images, for selection.</td><td>Display a continuous array of selectable images, only some of which can be seen at once due to the limited size of the device viewport.</td><td>Simulated 3D Effects Pop-Up Slideshow Location Jump Pagination Position Within Carousel Stack of Items</td></tr><tr><td>Film Strip</td><td>Present a set of information that is a series of screen-size items or can be grouped</td><td>A series of screens are displayed as a continuous strip, with small spaces or markers between them.</td><td>Carousel Fixed Menu</td></tr><tr><td rowspan="3">Slideshow</td><td>into screens for viewing and selection.</td><td>When a screen is centered, it fills the entire viewport. When scrolled,</td><td>Revealable Menu Pagination</td></tr><tr><td></td><td>part of two screens and the divider can be seen at the same time.</td><td>Location Within</td></tr><tr><td>Present a set of images or similar pieces of information for viewing and selection.</td><td>Each image is presented full- screen, with a function to transi- tion to the previous or next image</td><td>Pagination Location Within</td></tr><tr><td rowspan="6">Infinite Area</td><td>Complex and/or interactive visual information must be</td><td>in the series. The \entire data set is considered</td><td>Film Strip Infinite Area</td></tr><tr><td>presented to the user. The information can be presented as a single image that is so large it must be routinely</td><td>to be a large, two-dimensional graphic, and smaller subsets can be viewed as though “zoomed in" to portions of the larger image.</td><td>Simulated 3D Effects On-screen Gestures Wait Indicator</td></tr><tr><td>zoomed in to so that only a portion is visible in the viewport.</td><td></td><td></td></tr><tr><td>Selections, either individual or multiple, must be made</td><td>A method of selection, of the line item, or by adding checkboxes</td><td>Vertical List</td></tr><tr><td>from a large, ordered data set.</td><td>to the elements displayed, can be added to almost any display</td><td>Grid Confirmation</td></tr><tr><td></td><td>method, such as the Vertical List, Grid, or Carousel.</td><td>Wait Indicator Titles</td></tr></table>

## Chapter 3, “Control and Confirmation”

This chapter described appropriate control and confirmation patterns that can be used on mobile devices to prevent costly human error resulting in loss of input data. When human error may occur, you can incorporate modal constraints and decision points as preventive measures. When considering confirmation controls, consider the user’s context of use, because an overuse of these constraints and decision points during low-risk situations will cause user frustration by increasing processing time and mental load, and delaying or stopping the task.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td>Other patterns to reference</td></tr><tr><td>Confirmation</td><td>A decision point is reached within a process where the user must confirm an action, or pick from among a small</td><td>Present choices contextually— usually as a modal dialog—and simply and clearly communicate the consequences of the choices.</td><td>Exit Guard Pop-Up Wait Indicator Titles</td></tr><tr><td>Sign On</td><td>number of disparate (and usually exclusive) choices. A method must be provided to confirm that only autho- rized individuals have access to a device, or a site, service, or application on the device.</td><td>Consider whether your specific situation requires explicit authenti- cation. Mobiles should only require authentication for first-time entry, or for very high-security situations. Mobile-like multiuser devices such as kiosks will also require</td><td>Pop-Up On-screen Gestures Titles</td></tr><tr><td>Exit Guard</td><td>Exiting a screen, process, or application could cause a catastrophic (unrecoverable) loss of data, or a break in the session.</td><td>authentication. Present a modal dialog that delays the user from exiting immediately (the app or function is kept open in the background), informs the user of the consequences of exiting (loss of data), and requires the user to make choices, at least confirming the exit or returning to</td><td>Wait Indicator Pop-Up Titles</td></tr><tr><td>Cancel Protection</td><td>User-entered data or subsidiary processes would be time-consuming, difficult, or frustrating to reproduce if lost due to accidental user- selected destruction.</td><td>the session. Processes must be designed to protect user input. Methods must be provided to recover previous and historical entry.</td><td>Clear Entry Autocomplete &amp; Prediction Hierarchical List Input Areas</td></tr><tr><td>Timeout</td><td>High-security systems or those that are publicly accessed and are likely to be heavily shared (such as kiosks) must have a timer to exit the session and/or lock the system after a period of inactivity.</td><td>Try to avoid the use of Timeout as a solution to load and for security. If sessions must expire due to the method by which they have been built, consider making this transparent.</td><td>Pop-Up Sign On Exit Guard Titles</td></tr></table>

## Chapter 4, “Revealing More Information”

This chapter described how to appropriately design to reveal more information. As a designer, you need to become aware that your users, devices, and networks all have limits. Screen size will limit the amount of information that can be displayed at a time. A device’s OS will limit processing and loading times. Our memory limits cause us to filter, store, and process only relevant information over a limited period of time. If we disregard these important principles, we can expect the mobile user to encounter performance errors, dissatisfaction, and frustration.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td>Other patterns to reference</td></tr><tr><td>Windowshade</td><td>A displayed element must be able to easily reveal a small or medium amount of ad- ditional information, without</td><td>Items are provided with an indica- tor that more information is avail- able, generally by defining upper and lower bounds, or by enclosing the indicator in a box. When se-</td><td>Fisheye List Pop-Up</td></tr><tr><td rowspan="2">Pop-Up</td><td>leaving the current context or page.</td><td>lected, this area expands vertically to display additional information or interactive elements.</td><td>Titles</td></tr><tr><td>A displayed element must be able to easily reveal a small or medium amount of additional information, while remaining associated with</td><td>A Pop-Up is a child &quot;page&quot; that is smaller than the viewport and that appears modally on top of the parent page or display context that spawned it.</td><td>Annunciator Row Titles Exit Guard Link</td></tr><tr><td>Hierarchical List</td><td>the current context or page. A large set of information must be presented. The information is hierarchically ordered, and this structure is relevant to the user.</td><td>Display hierarchically ordered information so that it is compre- hensible and quickly accessible. The parent-child relationships are exposed visually, and users may fold and unfold the list to view</td><td>Advertising Fisheye List Vertical List Select List Titles</td></tr><tr><td>Returned Results</td><td>When users have explicitly requested subsets of informa- tion, the narrowed data set that results must be displayed in a meaningful manner.</td><td>only the parts they need. The displayed page will show Returned Results in an ordered list, or displayed over other contextu- ally relevant information (such as a map or graph).</td><td>Vertical List Thumbnail List Fisheye List Select List Pagination Location Within Accesskeys Titles</td></tr></table>

## Additional Reading Material

If you would like to further explore the topics discussed in this part of the book, check out the following appendix:

## Appendix D, “Human Factors”

This appendix provides additional information on our human sensation, visual perception, and information-processing abilities.