# Input and Selection

## The Wheels on the Bus Go Round and Round

I remember as a kid singing the song “The Wheels on the Bus Go Round and Round” on those long bus rides up to summer camp. It was the adults’ secret weapon to pass the time and keep the kids out of trouble, I presume. It went something like this:

The wheels on the bus go round and round,

round and round,

round and round.

The wheels on the bus go round and round,

all through the town.

The baby on the bus says, “Wah, wah, wah;

Wah, wah, wah;

Wah, wah, wah.”

The baby on the bus says, “Wah, wah, wah,”

all through the town….

Well, the rest of the song is outside the scope of this book. But imagine if the song was describing today’s city bus commute instead. It might go something like this:

The wheels on the bus go round and round,

round and round,

round and round.

The wheels on the bus go round and round,

all through the town.

The teen texters on the bus tap “LOL, LOL, LOL;

LOL, LOL, LOL;

LOL, LOL, LOL.”

The teen texters on the bus tap “LOL, LOL LOL,”

all through the town.

The businessmen’s emails go “Clicky, click, click;

Clicky, click, click;

Clicky, click, click.”

The businessmen’s emails go “Clicky, click, click,”

all through the town.

The traders on the bus type “Buy, buy, buy;

Buy, buy, buy;

Buy, buy, buy.”

The traders on the bus type “Buy, buy, buy,”

all through the town.

## Mobile Trends Today

![](images/f3eac8645794d8a2e81bdd270d8b1c8b972ad4184da15a46039177760b42ecdf.jpg)  
Figure 11-1. Forms can reduce the number of steps in a process by adding multiple selections, but they can also end up being dense and unusable. Many select lists, especially, confuse the paradigm and pull the selection mechanism out of the context as well as change the expected behavior.

The landscape of mobile use is defined by user-generated input. In his blog post titled “Data Monday: Input Matters on Mobile,” Luke Wroblewski points out the following:

Web forms make or break the most crucial online interactions: checkout (commerce), communication & registration (social), data input (productivity), and any task requiring information entry. These activities are taking off in a big way on mobile. So getting input on mobile devices matters more each day (Wroblewski 2010).

As Wroblewski notes, the process of filling out fields and forms makes up a large part of our mobile experience, which is why it’s essential for UI designers to make interfaces capable of handling the way users input and submit information.

## Slow Down, Teen Texters!

Take a moment and reflect on some of your most aggravating moments filling out fields or forms on a mobile device. Here is a common scenario that frustrates me:

First, I’m not a savvy texter. I’m amazed by the accuracy and rate at which some people, mainly teens I’ve seen, can engage in a text conversation at a supernatural rate. I’m embarrassed to text whenever I’m next to them. Though when I am forced to input text and characters in a field, such as an SMS, it’s very likely I’m going to make errors.

I constantly enter the wrong characters because my fingers extend past the target size. Positioning the cursor to edit my mistakes is even more maddening. I end up clearing the wrong part of the word or deleting everything I didn’t want to delete. The only reason I continue with these tasks, despite my buildup of dissatisfaction, is because many times a better UI is not available.

If these basic functions of inputting data fail due to an unusable interface, the user will likely not bother with the site or service. That’s a huge risk to take, considering the emerging trends users are engaged in with their mobile devices.

## Input and Selection in the Mobile Space

![](images/38de00db7ad39e75b3489c1d933a25d82db205dedcf8b93f0953ee06839fdf86.jpg)  
Figure 11-2. Gestural interfaces can benefit from simulating physical objects, even for form selections. Make switches actually slide, and use thumbwheel-like spinners to replace short select lists.

For many of us, having to always type characters on a small mobile keyboard is a challenging task. The process is quite error-prone and the keyboard takes a lot longer to use. Luckily, there are solutions we can implement in our designs that will offer a more valuable user experience with less frustration and loss of data.

Here are some recommended tactics to promote quicker, more efficient and less errorprone input:

• Consider using assistive technology such as auto-complete and prediction during text entry. Requiring your user to only type the initial part of the word before the device recognizes the rest can allow for quicker text entry and fewer errors.

• When possible, and only if appropriate, consider using a drop-down list rather than a text field to complete an input. For example, selecting a country or state from a list can be more efficient than having to type it and risk misspelling. Remember, though, to never take your user out of the current context when using a drop-down list.

• Limit the amount of unnecessary “pogo sticking” and selection of key controls. For example, when you begin entering an email, consider the benefit of having a key labeled as “.com” predicatively appear to save the user from typing those additional four characters. Such functions can be offered as on-screen options even when hardware keyboards are used for entry.

• Always keep in mind the principles of Fitts’s Law. The more clicks it takes to make a selection, the longer the process takes to complete. Use appropriate controls to limit the number of steps a user has to take to achieve a desired result. In this chapter you’ll become familiar with spinners and tapes, and when to use them based on the number of incremental choices available.

• Take advantage of any sensors or stored data to assist the application in prepopulating information that can be detected. If the location can be determined, do not ask for it. And remember that absolute precision is not always required; weather reports are regional, so they can use vague senses of location and do not require GPS access.

## Patterns for Input and Selection

Using input and selection functions appropriately provides users with methods to enter text and make selections within a list or field. In this chapter, we will discuss the following patterns:

## Input Areas

Provides a method for users to enter text and other character-based information without restriction.

## Form Selections

Provides a method for users to easily make single or multiple selections from preloaded lists of options. See Figure 11-1.

## Mechanical Style Controls

Provides a simple, space-efficient method for users to easily make changes to a setting level or value. See Figure 11-2.

## Clear Entry

Provides a method for users to remove contents from fields or entire forms without undue effort and with a low risk of accidental activation.

## Input Areas

## Problem

You must provide regions and methods for your users to easily enter text and other character-based information.

Forms and other types of input areas are common features of every platform. Many use web paradigms, so they are simple to understand whether in application or web mode.

![](images/a0c45864253d3b6d3d446803b32d1fba00dafdd3cfb7157361e486f417b61c6d.jpg)

![](images/97cf2eda693dd84b530a5942c6999b3ee225be40305c1a00d000a56f11d0b7dd.jpg)

![](images/858498d22772edb0ec00a18545f8c8f682793ae369537d5e7ee159e37a12e914.jpg)  
Figure 11-3. These three examples show how space can be saved with efficient labeling and hint techniques. However, each compressed item also risks reduced readability and confusion. Field labels inside the form are suitable for single-use forms such as this, but should be avoided when prepopulated information or revisiting of the form is likely. The user may not know what each field is for once the information is entered.

Text and textarea input fields are long-established principles and are heavily used to accept user-generated text input in all types of computing. Mobile is no exception, and employs these elements in several methods, with variations to meet the needs of mobile devices.

The Input Areas pattern is concerned largely with differences between the typical implementations of these web or desktop computing form fields and their most common practices within mobile OSes and applications.

For guidelines on using forms for the mobile web, see existing standards from organizations such as the W3C for the presentation, interaction, and design of these form fields. Of course, the principles outlined here still apply.

## Variations

There are three variations for Input Areas. The differences are based on the amount of required text input by the user as well as limitations of available display space on the mobile device.

## Text

Text fields are single-line entry methods. For mobile, these should usually be restricted to only accepting as much input as can be seen in the form, though exceptions may be made, such as for URL entry.

## Textarea

Textarea fields are multiline entry methods, with fixed display heights. They are often configured to accept an arbitrary (though not infinite) amount of text, and are provided with a vertical scrolling mechanism to display text which does not fit in the field.

## Convertible

In certain cases, such as the numeric entry field for the Dialer, mobile devices may display an entry field that appears to be a text field, but is in fact a textarea field. This variation is used due to the limited space on mobile devices—the field is only as large as is needed at any one time, and expands to additional lines as more text is entered. See Figure 11-4.

## Interaction details

Text Input Areas may only be used while in focus. Focus may be granted by scrolling with Directional Entry keys or by direct selection with a pen or finger. Scroll-and-select devices may require explicit selection of the field by selecting the “OK/Enter” button. This allows the form to be scrolled through quickly, and only when a field needs to be entered will full focus be granted.

While a field is in focus, pressing the “OK/Enter” key (when available) will perform different functions, depending on the context of use. Web forms will work as they usually do for the desktop web. For fields in mobile applications, “OK/Enter” will generally commit the field and will transfer focus to the next field in the form—in a mode ready for entry—or the next item in the list. If no other item is available, the entire form will often be submitted instead.

Whenever content is known to the system, make sure it is prepopulated so that the user does not have to enter it. Prepopulated content is interacted with just as user-entered text, and may be edited, added to, or removed. When large amounts are prepopulated a Clear Entry item should be provided.

![](images/25fde873f3a414a4bdc13efecac63aec91b48259ae825434af20d06403132cff.jpg)  
Figure 11-4. Textarea fields are essentially identical to text fields, except for the height. Convertible fields, as shown here, only occupy space as needed.

The focus of a field must always be very clearly delineated, with border, background, or other effects. Cursors must always be used when fields are editable, to denote the state change and the position of the text insertion point. See the Focus & Cursors pattern for additional details.

You should always use an Input Method Indicator of some sort to denote the available text entry modes.

Though some fields are clear based on context (message composition fields in SMS applications), you will generally need to label each field. Labels adjacent to the field should be to the left or above the field, and must be close enough to make the relationship clear. Use regular alignment and designed grids to ensure clarity.

If space is short, some abbreviations or icons may also be used to save space. Figure 11-3 shows several space-saving options.

To save even more space you can place labels inside the form field itself. You can also use this method when labels outside the field are provided, for hint text to give information on the type or limits of information to be entered in the field. Label or hint text in the field must be clearly differentiated from actual content (whether user-entered or prepopulated). Typically it will be gray, and it may be italicized or a different size to make the difference clearer under all conditions. Content specifics, such as trailing ellipses, may also serve to make this distinction clearer.

Labels or hints in the field are not like prepopulated text, and will disappear when focus is granted. When all content is removed from the field (or none has been entered) and focus is removed, the label or hint text will appear again. The loss of the label or hint text, once the user types, can be a problem, so you should consider if you can live with this interaction.

If hint text is required and the field is not available (due to the label being in the field or the likelihood of prepopulated information), hint text should appear adjacent to the field, either below or to the right.

Whenever possible, validate forms at the field level as they are typed or when the field loses focus (indicating the user has completed entry). Successful validation can be indicated adjacent to the field, near any hint text. Errors in validation, indicating improper entry, should appear in the same location. The relevant hint text, such as field constraints, can be highlighted if space allows.

Antipatterns  
![](images/46106cfefa2978bcc3b1f6bd4d2a7d08d3af14036a4815f9889e2078899d5af2.jpg)  
Figure 11-5. Full-screen entry methods are the default for J2ME and some entire OSes. Aside from simplicity of development, they were originally developed to offer all entry options, counters, and other features in a small amount of space. Today, they are just confusing, as the user is removed from the context entirely. This example typifies one key issue: a large field is exposed for entry that cannot exceed 16 characters.

Do not use full-screen input panels, as shown in Figure 11-5. In several OSes or environments, selection of an input area will display a common full-screen panel by default. This removes the user from any context, makes hints and other text invisible, and makes implied limits (such as the difference between a text field and a textarea field) invisible. Even if you are working in such a platform, there are workarounds, and often fairly easy ones. Be sure to avoid this behavior whenever possible and allow editing of text in the page context.

Form fields, and especially text Input Areas, are among the most prone to frustration and error due to free-form entry. Design carefully to avoid confusion, and use supporting patterns such as Autocomplete & Prediction and the principles of Cancel Protection to make entry more efficient and speedy.

## Form Selections

## Problem

You must support making single or multiple selections from preloaded lists of options. Form Selections, like radio and pull-down lists, are universally supported in a fairly consistent manner.

## Solution

![](images/32728465790bef66d754663af0c48ae9f9033bc3f38cd7bf31da48a0acfb6088.jpg)

![](images/aa6a943953729eeea0ef3172a1130afe9e8048b7758fa4630c96b869489566bc.jpg)  
Figure 11-6. A typical select or “pull-down” element, alongside other form elements. When selected, a pop-up scrolling list appears, from which one item can be selected.

Mobile devices, even more than other computing devices, can use forms to good effect for selection from already-provided information. Careful design choices can reduce user input, improve accuracy, and greatly reduce frustration.

Extending the ease of entry, mobiles have several regularized variations and subtypes of single and multiple selections. Consider the entire range of variants within this pattern before completing the design of any selection mechanism.

For mobile web use of standard forms, see existing standards from organizations such as the W3C for the presentation, interaction, and design of these form fields. When making mobile-specific websites, feel free to also consider use of the other variations outlined in this pattern.

Remember to use sensors, already-entered information, and any other data to prepopulate or make informed assumptions whenever possible. Do not make users enter information they already have, or which the system should know.

![](images/9d60ab566022ce65deb3f56841cfdef9f81ca53429cae30db6ef585a0853fed4.jpg)  
Figure 11-7. Lists are heavily used in mobile devices, either as single-select, where only one click selects and submits, or for multiple selections. Long lists should usually appear as scrolling lists, using the Vertical List pattern, but shorter ones such as the Power key options on the right should more clearly express the actions, by using lists of buttons instead.

Several variations exist, including some that do not appear to be form elements based on conventional web form understanding. These can be categorized into three basic types:

## Single-select

When this is used in conjunction with other form elements, a single item may be selected from a provided list. When all form selections are made a Button or other submission element (such as a soft key) is used to submit the form.

## Select

The drop-down or pull-down list as seen on desktop and web forms can be placed within a mobile application. When selected, it opens as an anchored layer, allowing scrolling and selection. See Figure 11-6.

## Radio

Each item in a list is preceded by a line-item selection mechanism, just like a radio button list in desktop or web forms. These work best for vertical text lists. In other cases they may be unrecognized or not easily associated with a particular item. Compare this with a checkbox in Figure 11-8.

## Multiple-select

When this is used either in conjunction with other form elements or as a list on its own, one, several, or all items from a provided list may be selected. Items already selected (or preselected by the system) may be deselected. When all form selections are made a Button or other submission element (such as a soft key) is used to submit the form. Figure 11-7 shows some of these.

## Checkbox

Each item in a list is preceded by a line-item selection mechanism, just like a checkbox list in desktop or web forms. Used in conjunction with other form elements, these work best for vertical text lists but can be made to work in multiple columns and for other types of selections. For complexly displayed multiple selections, try the next variation.

## Multiple-select list

This is a variation of the Select List pattern, where each item displayed has an associated checkbox, allowing selection and deselection.

## Single-click

When this is used when there is no form, or if this is the only element, a single item may be selected from a provided list. This does not mean it may be the only interactive item on the page. No button is required to submit the form, as the single selection is committed immediately.

## Button list

This is used not for radio buttons, but for actual form-submission types of buttons. A list of these can be provided to choose from. This is only used for short lists, where no scrolling is required and the action is committed immediately.

## Select list

When a longer list is needed, the setting does not take effect immediately, or confirmation of the setting should take place inline (by showing the current state in the same display, refreshed) a Select List, usually a simple text Vertical List, will serve the purpose.

## Interaction details

![](images/89384e29ae26e0936133b90ac2eb4f0b00cca387efd57105d87920bdd6a5b480.jpg)  
Figure 11-8. Radio buttons and checkboxes are most valuable in conventional forms, such as this mixed form, with conventional submit buttons. Some handsets use the soft keys as their default buttons.

Any of the types of Form Selections may be viewed in their passive state at any time, or while not in focus. They may be scrolled through and selected (or deselected, if permissible) while the selection mechanism is in focus.

The definition of focus here may not be entirely clear, but generally it does not concern the end user. For the sake of better understanding, the following (somewhat circular) definition will suffice: any time the list can be scrolled through, it is in focus. Examples may help.

• A drop-down list is not in focus when it appears as a single line. When the field is in focus, it will open to reveal what is functionally a scrolling, vertical Select List. Whenever the field is in focus, for a scroll-and-select device one item within the list will be in focus, and using the “OK/Enter” button will commit the field selection and close the drop down. For touch or pen devices, no items are in focus and pointing at an item in the opened list will select and close the list.

• Any list used inline in the context of a page, such as radio button list, can be considered to be in focus at all times. The individual items are selected in the same manner as for drop-down lists, though the list itself does not change, just the selection mechanism.

• Select lists are mostly used full-page, so the list is much like a drop down in that it scrolls as a complete list. When it is a multiselect list, this works like an inline list and selection only changes the indicator. When it is a single-select list, it is more like the drop-down list and closes the list or continues to the next state.

Whenever content is known to the system or it has been entered by the user previously, it should be preselected in the field. Prepopulated content is interacted with just as a userentered selection, and may be deselected or another selection made.

## Presentation details

Focus of a field and selection item must always be very clearly delineated, with border, background, or other effects. See the Focus & Cursors pattern for additional details.

Selection mechanisms should always appear as their intended function. Use current web standards as a heuristic evaluation for the design of such mechanisms; even if OS standard form widgets are used, ensure that they are understandable to the typical user. Do not mix functions with different appearances, such as allowing multiple selections with selectors that look like radio buttons.

Labels should accompany the field whenever space provides, and may be abbreviated or iconic to save space. Labels adjacent to the field should be to the left or above the field, and must be close enough to make the relationship clear. Use regular alignment and designed grids to ensure clarity.

Labels may be placed inside the form field itself, when there is space inside, such as for a pull-down list. You can also use this method when labels outside the field are provided, for hint text to give information on the type or limits of information to be entered in the field. Label or hint text in the field must be clearly differentiated from actual content (whether user-entered or prepopulated). This is usually by language or formatting; “Select a state...” is clearly different at a glance from “Kansas.”

Labels in the field are generally selection text, but they will be invalid selections. Do not allow them to be submitted (or not have an assigned value, just a label). If hint text is required, such as reasons for entering the information or clarification about what the information means, it should appear adjacent to the field, below or to the right.

Whenever possible, validate forms at the field level, as they are selected, or when the field loses focus (indicating the user has completed entry). Successful validation can be indicated adjacent to the field, near any hint text. Errors in validation, indicating improper entry, should appear in the same location. The relevant hint text, such as field constraints, can be highlighted if space allows.

Validation may also allow automatic selection of items. For example, on an address form, if the user enters a zip code (postal code), the corresponding region information may be filled in as well, before the user can scroll down to fill in the information.

Antipatterns  
![](images/e5b381cd1a730ab916aad242f57e85a67ec893ae5573857074685b45e8a7f97f.jpg)  
Figure 11-9. Full-screen entry methods are the default for J2ME and some entire OSes. Especially for selection lists, they are just confusing, as the user is removed from the context entirely. In this case, the state is a part of a larger address, and the context (shipping) may not be the default case the user considers. Staying in context can prevent errors, mistakes, and confusion.

Do not use full-screen input panels, as shown in Figure 11-9, as the selection mechanism for small components such as pull downs. In several OSes or environments, selection of any input or select field will display the choices as a full-screen panel. This removes the user from any context and makes hints and other text invisible.

Use caution when designing forms if selection mechanisms require odd display methods. Some OSes will not display a pull down as attached to the initiating area, but as a freestanding Pop-Up. Some even do the same for radio button lists. Although there are often workarounds, sometimes there are not, or they would break too far from the OS standards. If this is the case, consider using a different design, such as only selecting one piece of information at a time. A settings page could, instead of a long form, be a list of items, each of which opens a single settings panel.

Never overuse form-style input methods; if a single Select List or Button list is needed, simply allow selection to commit the actions. Do not also make the user select a submit button to commit the action.

Use the right type of selector for the information to be entered. Do not attempt to provide hints on how to multiselect from a pull down, but use a multiselect mechanism (a check box or Select List) instead.

## Mechanical Style Controls

## Problem

You must provide more obvious methods for users to make changes to a setting, level, or value.

Mechanical Style Controls are entirely a matter of design and implementation. Though they really require touch or (possibly) pen input hardware, there are few other absolute requirements.

## Solution

![](images/4cac657e50350c0d86eac50c6e410b56e9d9f831ff0e951aea2b1cb8c04d70a3.jpg)  
Figure 11-10. Spinners and tapes are form elements, and they can be mixed with others, as shown here. Be sure to use the best type of element for each piece of data, but also ensure that the styles interact adequately, so it feels like a single form.

Although some machine-era inputs and outputs forced restrictions based on systematic limits, many were well conceived and grounded in good ergonomic and human factors principles.

Some are simply helpful to use because the mapped interface is very well recognized, or there is no other way to “directly” control the output. Audio output, for example, has no obvious way to simply evoke more sound waves, so a continuously moving volume control is the best available solution.

These can be repurposed for digital input, especially on “direct entry” touch or pen interfaces. You may find they can serve as more compact, graphically oriented variants of certain single-select Form Selections, as shown in Figure 11-10. For their use with other forms, see that pattern.

These types of controls have value, especially over other types of selectors, in three key attributes:

• They are graphically oriented, so they tend to provide information at a glance.

• They provide direct control when using touch or pen interfaces, or very close coupling of the input to the available display methods for scroll-and-select devices, with an implicit scale. Compare this to a simple list of values, which the user must map to a model of the system.

• The manner in which they are controlled is apparent (if well designed), so no instruction and minimal previous knowledge of computers is required. Even for scroll-andselect devices, as long as the user can control the device to this point, he is likely to be able to use the control.

All of these are in opposition to many typical computing forms, which are usable only to those who have become accustomed to them in other contexts. Mobile devices are so pervasive, however, that they are many people’s first exposure to robust computing systems, so more obvious controls are necessary.

## Variations

Although several types of Mechanical Style Controls have been simulated in digital envi ronments, only two distinct classes have really been successful. Each of these, with their subvariations, is discussed in detail here.

Tapes or sliders are vertically or horizontally oriented indication and control mechanisms (Figure 11-12). They are used to control levels, such as for volume or zoom level. Zoom & Scale is in fact a specialized subset of these, with the results displayed live. Display Brightness Controls and volume controls (see Chapter 13) are other common implementations.

## Continuous

A single strip is shown, and the level can be set anywhere on the tape. Generally this just means a large number of increments (e.g., 100), but the setting is smooth and continuous.

## Incremental

The strip is divided into visible increments, and when the indicator is moved, it will jump to (or if smoothly dragged, will only lock at) specific intervals. If there are only eight volume levels, for example, an incremental tape is the right solution.

## Sliding switch

When an incremental tape has only two positions, it is a sliding switch instead. Expressing a toggle as a switch with two positions instead of a form element such as a pair of radio buttons or a single checkbox can be very helpful for many direct-control interfaces.

The term used here is derived from linear “tape” gauges, as for indication purposes they reflect this closely. The closest machine-era term would be sliding potentiometer, but when shortened this can be confused with other interface elements, and it discusses technology too closely.

Spinners, as shown in Figure 11-11, simulate, often with significant visual fidelity, a smalldiameter wheel on a horizontal axis. Only the current setting is visible through a port in the screen, and moving it rotates the wheel in the vertical direction to reveal other settings.

## Click wheel

Like the mechanical thumb wheel, gestures (with finger or pen) up and down are used to move the number directly. This can be combined with the other methods below for all touch interfaces.

## Hardware buttons

When in focus, using up/down buttons or some other hardware control can increment and decrement the value.

## Increment button

A single on-screen button is provided, which increments the value with each button push. This is good for items that are mostly incremented, and for small ranges of values so that mistakes can be fixed by going around. An example is a snooze control on an alarm. Each time the user pushes the button, 5-, 10-, or 30-minute increments are provided.

## Increment and decrement buttons

Instead of one, two buttons are provided, above and below the value indicator. The top one increments and the bottom one decrements.

## Direct entry

When the field is in focus, entry can be typed directly. This is most useful for numeric values, but you can make it work as the live jumping variant of the Search Within pattern for text items.

The term spinner is already somewhat in use. The most generic name for a machine-era device like this would be a thumbwheel, but this implies only the click-wheel style of interaction. There is historically no single, noncumbersome name for such controls.

Rotary dials and other types of continuous, glanceable controls or indicators are not used enough on mobile devices for patterns to have emerged. Many of these are simply unsuitable, due to the interfaces currently available. Rotary controls, for example, rely on a fixed axis of rotation, which is simply not present in touchscreens. It is possible that advanced Haptic Output methods will, in the near future, allow these to work by simulating grasping of an object.

Attempting to use some of these other control types may not be obvious or easy for the end user. Pushing the interface concept can lead to confusion and mistakes in input.

![](images/f05a7f4bd6c318acb9551bc2ea0a05ba1e2afe0ee95719fe8e2dd25871695fc1.jpg)

![](images/da74a1063931ba49ad66deb11eb2063324916e401b5c90c34fd13516419f4acf.jpg)  
Figure 11-11. Two variations of a full-featured spinner, with increment and decrement buttons. On a touch device, these could both support gestural control as well, using the clicky thumbwheel variation. Note that on even the low-fidelity version, the numbers are within boxes that are clearly differentiated from the rest of the interface. The high-fidelity version appears to be split by individual characters, but this is purely for visual display and style purposes; the minutes and hours are changed as a whole set.

## Interaction details

The aforementioned variants are classes, and they provide guidelines, but there are numerous spaces in the middle where new interfaces, perhaps inspired by machine-era antecedents, may be used. Consider the standards used by the OS and the user’s needs to enter data quickly and to protect entry, when selecting one of these methods or designing another one.

Pick the most suitable entry method, even if it induces design inconsistency. A spinner is a terrible way to select from two values, such as a.m./p.m. when setting time. A slidingswitch style of tape would be the obvious replacement, and it has similar direct interaction, so you can make it match the overall style of the interface.

Values do not have to be at consistent intervals. As in the snooze button example, they should be sensible and predictable, but they do not have to be regularly spaced.

Tapes are always dead-end selections. Increasing the level while at the maximum value will have no effect. Spinners should always be circular. Increasing the level while at the maximum value will switch to the minimum value.

Limit the values within a spinner to relatively small numbers of selectable increments. If more than about 15 to 20 are required, use a Vertical List or a Select List, or simply combine spinners by digit. For example, offer to choose the day of the month not with a spinner from 1 to 31, but with two of them, one from 0 to 3 and another from 0 to 9.

In fact, spinners are frequently presented in groups. Another common example is to set hours and minutes, with three to five individual controls to offer reasonable ranges within each control. With this level of direct control, it’s usually best to make sure unrelated items are entirely unrelated, even if they are adjacent. Switching minutes from 59 to 00 will not also change the hour from 3 to 4. In the future, this may change; Haptic Output could make the switch at the end of the range “harder,” due to the simulated linkages, so the user notices they are about to change a related value. This sort of interaction works on mechanical systems, so it may port over to digital environments as well.

Tapes may have an arbitrarily high number of increments if precise selection is not key. Do not try to allow users to make multiple selections. This is difficult even in normal forms on a desktop computer, and better methods, such as the multiple Select List, are available to solve this need.

Especially for scroll-and-select devices, tape orientations should be deconflicted from the remainder of the interface. When presented in a page, where other elements can be selected and scrolling is possible, only horizontal tapes should be used and no selectable items should be placed next to the tape. If the user scrolls to the tape using up/down Directional Control keys, it will become in focus without further selection, and immediate use of the left/right keys will change the level.

Increment and decrement buttons, when on a spinner, are unitary input items. They will not key-repeat. One click is required for each increment. The same behavior is encouraged for hardware keypads as well. Tapes may use key repeat or acceleration, if enough increments are offered to make this valuable. Make sure these work like delete functions on a text form, and do not let the key press leave the field when the end is reached. See the Zoom & Scale pattern for additional details on the use of increment buttons, and indicators of position in tapes.

Only present the coarsest acceptable values within a spinner. For example, when setting time for an appointment, the spinner should only have 15-minute increments. Especially for spinners, you can then allow additional control by offering direct entry of values. When the field is in focus, the keypad can be used to type values directly. This works especially well when coupled with coarse preset values; the user may quickly set most values, and still has the option of using any value when more rarely needed.

For touch or pen devices, allowing direct entry of a numeric value may require a more specific, nondragging touch of the value field in order to display the input panel. Do not open virtual Keyboards & Keypads whenever the selectable element is in focus, as the more typical entry method is to select by dragging.

Custom values are discarded when the field is incremented or decremented. If “17” is entered, and the value is incremented to “30”, when decremented it will display “15”, not “17”.

When larger values are made available by the use of spinners for individual digits, illegal entry must be restricted. For example, if a pair of spinners from 0 to 3 and 0 to 9 allow entry of all days, the month selector may restrict access to a “3” selection in the first field. Likewise, legal selection of that “3” will restrict entry to “0” or “1” in the second digit. Restricted entry should usually involve graying out the value and not allowing it to be selected, although it may still be seen and scrolled to.

![](images/01c344dbc852db7fa57926fdaed3665b28a344e15baa1f3df1ddb46b4d2e9f15.jpg)  
Figure 11-12. Three of the many ways a tape control can be depicted and interacted with. Increment and decrement controls are placed at either end of the bar, but they do not need to be. The current value is either with the pointer or at the end. On the middle version, the value is inside a text input field, so it is easily editable directly. The bottom version increments the tape by dividing it into segments, and the direction of the scale is depicted by icons at each end that may or may not also serve as increment buttons; the pointer will snap to the center of each increment to make that restriction clearer.

## Presentation details

Spinners must be arranged so that they make sense. Groupings must be in conventional format, so hours are to the left of minutes, with a (nonselectable) colon separator, for example. Due to their perception as physical objects, minor errors in position or slow response can be highly confusing to users.

Spinners are often drawn at high fidelity, as though they are literally machinery. Whenever possible, you should try to animate spinners as though the values are painted onto a small cylinder, rotating out of view as the user interacts with it. You can simply slide the items out of view if the 3D effect is not available on your platform. Be aware this will not be as effective, and may cause some confusion when the items rotate back to the beginning of the list.

Ideally, the entire display should be shown as though it is an actual mechanical object, though it may be styled in a shiny, perfect, digital manner. It can also be made to work with simple type and flat colors. Just keep the principles in mind: the background of the value should still be a different color, a border should exist, and the entire element to include increment buttons must be in a single container.

Spinners should snap to displayed values, and never be able to stop with partial values in the window. Slight misalignment at lockup may be tolerated if it is deliberately built and it follows the design ethic of being a quirky, actual machine. But this is not typical, so use it carefully.

Tapes should also be designed as though they are physical items, with a moving selector handle/indicator. Always offer a handle that can be easily grabbed for touch or pen devices. Additional communication of the value can be offered by filling in the background of the strip. The edge of the filled space indicates the position.

Tapes with incremental control must display the increments. You can use any style that is clear, including gaps, ticks, or other types of indicators within or immediately adjacent to the displayed bar. You can also provide a scale, or values for each level, but you will often want to suppress them, as they may be arbitrary. You can also avoid displaying the value of each tick, if the current value of the setting is displayed, attached to a moving indicator, or at the end of the tape.

Use nonvisual responses to inputs whenever possible, and especially for gestural inputs. Clicks should be felt (or if needed, heard) at each increment. For nonincremental values, you can provide a subtler response (very light clicks or a resistant, almost scraping feedback) to indicate that the control is moving and to encourage the perception that these are physical controls being moved. See the Haptic Output pattern for additional details.

## Antipatterns

All Mechanical Style Controls must perform smoothly and respond without delay to user input. Delays will cause the user to attempt a new entry, and built-in input buffers may result in the user accidentally making the wrong selection.

Avoid using variants such as the click wheel, where the display is obscured by the user’s finger, without haptic or audio feedback. Either do not obscure the input, or always allow some other feedback of incrementing.

Other dedicated level-changing keys the user may have become accustomed to, such as the volume control, may also be useful for changing the level of spinners and tapes. However, this advice may conflict with other interface expectations or the OS standards. If the volume keys are reserved for volume only, or are used in some cases to scroll the page, do not use them to change other levels.

## Clear Entry

## Problem

You must provide a control that allows users to remove contents from fields, or sometimes whole forms, without undue effort and with a low risk of accidental activation.

Clear Entry functions are built into some form elements in some platforms, but in others (such as some web browsers) they may be difficult to implement due to restrictions on refreshing data without replacing the entire contents of the page.

## Solution

![](images/b8c1be326c52c2bb3e389ccb35bccf3650332e711aed62fefd54028203074d7d.jpg)  
Figure 11-13. Option menus, such as this contextual menu on a touch device, offer options for dealing with text already. Adding a Clear function may not be natural, but a dual-purpose function with automatic recovery, such as this “Cut all” function, can be a very convenient way to include it. The user is additionally led to develop a mental model that includes this, from her more frequent use of typical editing functions.

Just as text entry on mobiles is difficult, removing already-filled-in values can be as difficult, and even more tedious. Long URLs, or other old, prepopulated or prefilled data may be inaccurate, and it can be very slow to delete all this content. Providing an explicit method to remove the content can sometimes be helpful.

Clear Entry functions should only rarely be used, and can be dangerous, as they may accidentally encourage deletion. But they should be considered for some types of fields and forms. This pattern is in no way meant to condone the common but poor practice of the “Reset” Form button, or to encourage the use of clear functions on every field.

Additionally, the “Reset” Form button does not allow selection of individual fields. Even on touch devices, it can be difficult to use conventional desktop paradigms of selection and deletion, so without additional assistance users have to resort to repeated keystrokes and other time-consuming actions. To make matters worse, certain actions we take as designers to prevent loss of data can make it hard to get around; discarding a text message, for example, often saves the message as a draft and there is sometimes no way to get around this.

A series of functions and tactics should be considered to assist the user with this task, without conflicting with primary tasks and principles of preservation of data.

## Variations

Most Clear Entry functions for mobiles are at the field level, and these almost always empty text Input Areas:

• Explicit functions are controls that must be activated and then, in one step, clear or reset an entire field. The reset function will revert to any defaults, and also means it can be used on any type of input field or function.

• Assistive functions reuse, repurpose, or exaggerate existing features of the interface to assist with field clearing, such as that shown in Figure 11-13.

Form-level clear and reset buttons are discouraged, but they can be useful in some processes. Additionally, do not overlook the possibility that your form may have essentially one field in it. An SMS message composition page can use a “Clear” button at the form level, which functionally will only clear the one field.

## Interaction details

You should not automatically include Clear Entry in every page, or even every project, but you should always consider it. Think of all form design—as you think of all interactive design—in the context of the user. If repeated use of a field is likely, or there is no other way to abandon the information, you may need to add a method to clear the input.

If you are implementing this as an explicit function, simply add buttons adjacent to the field (or within it), or as options available in a menu. These may overlap with the intent of the implicit function by simply offering a “Cut all” function; this has other purposes and in fact loads the clipboard with the data, but also serves to clear the field. Make sure this function is visible enough. Many edit controls are only available via Press-and-Hold or other, low-affordance functions.

One classic implicit function is to simply overdrive the key repeat. The typical user will, when faced with a large delete task, simply enter the field and begin pressing the Delete key. Many will be aware of key repeat, so they will keep the key pressed down if the whole field must be cleared. Key repeat usually has a relatively low maximum speed, to allow for stopping at a specific point. But if this is unlikely, such as in the URL field example or after a longer-than-usual time, the repeat may accelerate, or simply scroll across the entire field.

This may be a very marked acceleration, even to the point where the entire field is suddenly deleted within a fraction of a second. This must always be coupled with behavior that stops key presses at the end of the field, and does not move to the next field in line without the user stopping the action, even if the Back key is used to cycle to the previous in-focus area otherwise. This behavior can be applied to arrow keys when used for selection as well, but is not applied to other keys. This acceleration method should work for both selection and deletion functions.

These variants and examples should not rule out other methods being developed or used. Gestural clear functions are becoming common on Pen Input fields; however, these have not yet developed into a regularized enough set to be considered a single pattern.

For all of these actions, use the principles of Cancel Protection. Explicit cancel guards are not usually needed if the control is well designed, but saved states, or other paths to retrieve the information, should often be developed. URLs can usually be revisited with the existing history functions, and the “Cut all” menu option described earlier does save the cut data to the clipboard; pasting will recover it.

## Presentation details

Label all buttons, menus, and other functions clearly. Rarely can a reset function be a compact button, labeled only with a graphic, due to the potentially catastrophic loss of information. Use text labels when possible.

Be sure to label clearly. “Clear,” “Reset,” and “Cut” are very different actions, with different implications. Do not confuse terms or assume the user base is not savvy enough to understand subtle semantic differences.

Live functions such as high-speed key repeat, or gestures to select or delete functions, must show the action happening in real time. If the screen cannot update at the speed of the actual behavior, do not use the function. Even at maximum speed, the user must be able to release the key and expect to have the cursor stop where he sees it at that moment.

Always use conventional display methods for exaggerated behaviors. Selection at high speeds should use the same highlighting as normal-speed selection, for example.

## Antipatterns

![](images/cfe0e2246b54003f9c9df7813884817cf37a7aa8ef8c24b6d6d268c529ba0ce1.jpg)  
Figure 11-14. Even on the desktop web, the Clear button is massively overused, and causes errors more than it fulfills real use cases. This very small form has no need for such a button, and it is also undifferentiated from the other two, and far too close. Even if identified, it can easily be accidentally activated.

Form-level Clear buttons, if used, must be very carefully placed to avoid accidental activation and should still often use explicit Cancel Protection methods. Do not use the poor convention of the Clear button immediately next to the Submit button at the bottom of every form, as shown in Figure 11-14.