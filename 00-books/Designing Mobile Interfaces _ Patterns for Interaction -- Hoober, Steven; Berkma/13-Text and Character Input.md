# Text and Character Input

## Slow Down, You’re Too Fast!

Some say he was doing it to annoy the writers. He may argue that it was because the adjacent alphabetized keys kept jamming up due to interference when people were typing too fast. For whatever reason, in the early 1870s, Christopher Latham Sholes, a newspaper editor and printer in Milwaukee, continued to redesign his keyboard layout on his early writing machine into ways that seemed nonsensical.

After studying letter-frequency pairs, Sholes, along with the guidance and support of his backer, James Densmore, separated the most commonly paired letters in his latest layout. In 1873, with that layout, he sold the manufacturing rights for his Sholes & Glidden Type-Writer to the company E. Remington and Sons.

In order to impress customers, the workers at Remington made a slight change to the final key layout. They moved the letter R to the top row. This allowed their salesman to impress their customers by typing the brand name TYPE WRITER all from just one row. This became what is known today as the QWERTY layout.

When the QWERTY keyboard was introduced, writers struggled to learn its layout. The key-jamming problem was less problematic; however, typing speed, along with user satisfaction, was immediately reduced. Sales of the typewriter were poor. It wasn’t until 1878, when the Remington No. 2 model was released, which incorporated both lower- and uppercase letters, that sales and performance increased.

## An Improved Design?

For the next 60 years, the Remington typewriter maintained success with little competition. In the 1930s, August Dvorak and his colleagues at the University of Washington were determined to create a new and improved keyboard layout. Dvorak wanted to create a keyboard layout that improved typing efficiency and time.

In 1936, he patented his Dvorak Simplified Keyboard (DSK). His design targeted Sholes’ problems, such as hand overload, unbalanced finger loads, excess finger movements, and awkward strokes (Parkinson 1972). Dvorak claimed through his testing that his design made typing faster, easier, and more accurate.

## Failed Impact

Many critics have discounted Dvorak’s findings that his keyboard improved performance. Some argued that experimental setups and statistical analysis done on the SDK were flawed. In what appeared to be a positive promotion for Dvorak, the Navy in 1944 published a document verifying an increase in typist productivity by an average of 74%. With these results, the US Navy Department had planned to order 2,000 SDK typewriters. But the request was turned down by the Procurement Division of the US Treasury Department, which felt there would be too much financial risk.

## The Status Quo

Whether or not the Dvorak keyboard was more efficient in time and performance, it never gained the popularity the QWERTY layout achieved. People learned to use the QWERTY and dealt with its odd arrangement of letter placement. The QWERTY layout became the status quo.

Today, several cultural variations of the Latin-scripted QWERTY layout exist:

• QWERTZ, widely used in Central Europe and Germany

• AZERTY, used in France and Belgium

• QZERTY, used mainly in Italy on typewriters

![](images/3ac43410e071862170912fb441cda1409061c6d6c636eb89673ecfd128a5d7c1.jpg)

![](images/97285f37c9a7e7e3231703b3dcf67c49b2e365d322280c6dbf4fe39d8b923cd5.jpg)

![](images/c1c9820f7671f3e7893470ddb853432e66d0a4f79be4031822dcf4f85d4ecceb.jpg)

![](images/9904778b2a4c0767cca2721c80bd38eaeedeb6cd55fef80462cb169ef526765e.jpg)  
Figure 9-1. A variety of keyboard layouts, including two tablet methods, a 10-foot UI using remote gestures and prediction, a virtual keypad with entry mode indicator, and a press-and-hold method to get to optional characters.

Note that cultures that are not based on Latin script use keyboard layouts based on their own language alphabet. And even before the typewriter, specialized users had nonalphabetical layouts; typesetters pulled letters from drawers laid out by frequency and size (you need a greater quantity of the letter e due to its frequency of use, so the slot they fit in is bigger), making their layout apparently random.

## Use What’s Best for You

As we just discussed, even though more efficient ways to input text may exist, it’s essential to understand that people will use what they are comfortable with. Some people are comfortable with handwriting, others with keyboard input (Figure 9-2). Some may prefer to use a pencil, pen, or stylus. Default to the most common method they can be expected to be familiar with, and provide options.

## Text and Character Input on Mobile Devices

When designing for mobile devices, understand that your users have different skills, preferences, and expectations when it comes to entering text on a device. If possible, provide multiple input options that they can choose from:

• Use input controls and layouts already familiar to users. See Figure 9-1. Don’t introduce a new layout that requires them to learn an entirely new process.

• Consider the context. Will your users be using the device outdoors, while wearing gloves? If so, a capacitive touchscreen becomes useless. Consider providing pen input or a hardware keypad as well, or instead.

• Consider your target audience and their habits. According to the Neilson Company, teens in the United States in 2010 sent and received an average of 3,339 text messages per month. A study done by Harris Interactive found that 47% of teens can text with their eyes closed (mostly using 10-key devices and triple-tap entry). Another study, done by PEW, found that 72% of adults text, but they average only 10 texts per day, compared to 50 per day by teens.

• Use functions that promote efficient and quicker input. Use assistive technology such as auto-complete and prediction during text entry. On mobile devices, limit the amount of unnecessary “pogo sticking” when using key controls. For example, when you begin entering a URL, consider the benefit of having a key or button labeled as “.com” predicatively appear.

![](images/6fe08b30138795e368500e71625f56170ebf37425474efad0bc58cff3e322686.jpg)  
Figure 9-2. Writing methods can be useful for inconvenient environments, users not accustomed to typing, annotations or nonlinear editing, or ergonomic reasons. Writing with the finger is available on some devices, and may become a pattern eventually.

## Patterns for Text and Character Input Controls

Using text and character input functions appropriately will increase efficiency, performance, and user satisfaction. In this chapter, we will discuss the following patterns:

## Keyboards & Keypads

Provides guidelines for text and numeric entry on mobile devices that use physical and virtual keyboards and keypads

## Pen Input

Provides an alternative input method for users who are less familiar with keyboards or are more comfortable writing in gestures

## Mode Switches

Expands the capabilities of a keyboard or keypad without using up additional screen or hardware space

## Input Method Indicator

Uses explicit indicators to communicate the current mode of input the user has selected

## Autocomplete & Prediction

Provides assistive technology to reduce effort, errors, and time during text entry

## Keyboards & Keypads

## Problem

You must provide a method of text and numeric entry that is simple, is easy, and should be so predictable in behavior that it may be performed by any likely user with little or no instruction.

Keyboards and keypads are built into the device hardware or are provided by the OS. Many platforms, such as the Web, cannot influence input methods, but all must support the available input devices correctly. For some devices, add-on virtual keyboards can be built as well. Some applications may demand a custom keyboard; a typical one is the Dialer, covered separately.

## Solution

The typewriter or computer keyboard, and the telephone keypad, have become so ubiquitous that they are, to most populations, the expected method of entering information. This extends even to devices which are, on their surface, unsuitable for such entry, such as membrane panels and on-screen displays.

![](images/7f50d4dc3ac3bb2ad27ea1d18d195e8e11316041fb78fe621103e8db009c21d4.jpg)  
Figure 9-3. A variety of slide or fold-out keyboards found on mobile phones. These include conventional individual keys with backlight, transparent keys with ePaper labels, and membrane panels. The arrangements of each are different, in a search for the best possible way to use the space, but all remain approximately reflective of their regional desktop computer keyboard.

Though several other input methods exist, none are remotely as common, and this is expected to remain true for the foreseeable future. Therefore, keyboards and keypads will continue to be key components of all interactive devices.

The details of any particular implementation must meet user expectations as closely as possible, within the technical limitations imposed by the device and its interaction methods. See some hardware examples in Figure 9-3. A touchscreen virtual keyboard on a small screen cannot faithfully reproduce a full-size physical keyboard, but adhering to the basic principles will generally impose sufficient order that users will be comfortable and able to enter information without any cognitive burden.

Be aware of regional and cultural norms. Avoid imposing unexpected keyboard or keypad layouts on your users. If you have a global product, make provisions for as many input types as possible. Recognize that some users will have wildly different layouts and character sets, and this can influence your interface in many ways. Accesskeys, for example, if not modified for each language, may work unexpectedly or not at all.

## Variations

Instead of variations, you can consider Keyboards & Keypads to have three axes of variation. Any one implementation combines the attributes from each axis to define the category. Most devices will use multiple modes, which are switched between as the state of the device changes. For more discussion on mode switching, see the Input Method Indicator pattern. For additional details on keypad entry for telephony, see the Dialer pattern.

## Hardware/virtual

The keyboard or keypad may exist as a series of physical buttons, or be represented on the screen of the device. Devices with hardware keys that can be relabeled digitally fall in the middle of this axis and will use attributes of both.

## Keyboard/keypad

Keyboards are those with direct mapping to characters in the native alphabet. Keypads, as shown in Figure 9-4, are for numeric entry and often dialing when on mobile devices. Chording keyboards and some specialized key entry panels fall in the middle of this axis and may use attributes of both types.

## Direct/multitap

Keyboards allow typing words and phrases via (mostly) direct entry; an a is typed by pressing a key marked “a” (or “A”). Multitap is an indirect entry method; an a is typed by pressing the “2” key, which is also labeled “abc”—sequentially until that letter appears. Certain keyboards combine attributes of both of these, but none are currently commercially important.

![](images/8d51916b993d2381832b76de4bbb3f5d98dd284662cd499b6d1be41a57799a18.jpg)  
Figure 9-4. A typical mobile device numeric keypad is coordinated with direction keys and other functions such as Talk and End, soft keys, and so on. This keypad is for use in North America, as the letter labels comply with the NANP standards. Other regions will demand other labels or layouts.

Although these descriptions and the remainder of this pattern focus on the standard implementation, each axis is actually more of a continuum. A single implementation may fall in the middle, such as some nonstandard keyboard/keypad combination layouts. This simply means the same principles apply to even those implementations.

Predictive systems, although associated with 10-key entry, are actually just methods that can be applied to any input method. These are addressed in detail in the Autocomplete & Prediction pattern.

You might think virtual keyboards and keypads are purely for touch interfaces, but they can also be used on scroll-and-select devices. You may find this an especially useful solution if occasional text or character entry is required on devices with no dedicated keyboard or keypad, and no touch or pen input.

When a field which allows free input is selected, display the virtual keyboard largely as described in this pattern. One key or button is always in focus while the keyboard is visible, and scrolling with the five-way Directional Entry pad will move in the corresponding direction. Keys should be in a grid, not offset, so that directional movement is more predictable. Selection will “press” the key and enter it in the field provided. The keyboard or keypad should be “circular” on both axes so that scrolling to the edge will move the selection to the opposite edge, to reduce the already large number of clicks to get to a character. A method must be provided (see Figure 9-5 and Figure 9-6 with the “Done” key) to complete entry and close the virtual keyboard.

## Interaction details

![](images/1577d3bcae93b6b94b8a0c5f1d7aaba7eeea19b635eeb7b182d20e5ccfa321f5.jpg)  
Figure 9-5. Numerous keyboard layouts can be devised to fit the space available, and still provide a meaningful experience for the user. This virtual keyboard is fairly full-size, with number keys, and symbols assigned to each of those. A few have been removed to save space, and a few have been moved slightly. The Mode Shift keys and the Submit key are along the edge, to allow space around them while increasing the effective contact space. Note that the keycaps are in lowercase, since the Caps Lock key is not on.

Interactivity of a key press is generally very straightforward. For hardware, the user simply presses the button. For pen and touch devices, each key is functionally a Button and should have hover and activated states when available. Some input methods may be more difficult. When Directional Entry or Remote Gestures is used, pointing and other focus or effect indicator standards from those patterns must be applied.

Hardware keys should comply with human factors standards for pressure, size, and spacing. Virtual entry systems should have targets no smaller than 10 mm. Certain keys, especially the “Enter” key, space bar, and modifiers, may be placed along the edges of the viewport on flat bezel devices, to increase their effective size. High-use keys, such as the space bar, should be larger to make them easier to find and activate. Keys that can have consequences past a single entry, such as the “Enter” key and modifiers, should have spacing around them to prevent accidental activation. Figure 9-5 shows several of these principles.

The layout and key arrangement should, whenever possible, use common and expected formats. For keypads, use regional standards promulgated by the local telecommunications authorities. In North America, for example, this does not just mean the layout is 1 at the top left, but that the 2 key has the letters “ABC” assigned to it.

![](images/50cf7532f4fcd4948ae5ddfdbddff858d4e076e5fb69c6d37cf162a58cbde2d9.jpg)  
Figure 9-6. For more compressed spaces, keyboards often lose the dedicated number row. You can make up for this by switching modes to a number entry or function key mode. This is a virtual keyboard, so alternative labels are not needed, as long as the mode switch key is clear. The primary symbols on the keyboard are still present, and in mostly the same place; the less-used slash and question mark are moved slightly for space purposes. Each of these has the shift mode labels above, so the user knows she does not need to enter the symbol mode and hunt, but simply presses Shift to get these characters.

You may have to compress your keyboard to fit into the available space, and combine the number row with the top row of letters, as shown in Figure 9-6. Make sure the numbers align to their normal location, so Q will also be 1 when a function modifier is used. Likewise, place all conventional symbols as close as possible to their typical location. The !, @, #, and \$ symbols should be alternatives of the 1, 2, 3, and 4 keys—or the closest equivalent when compressed—for US English keyboards.

Although most keyboards are displayed or built as a single block, a sometimes-seen variant is to provide a split in the middle. Sometimes this is just a structural and visual break, which otherwise does little to the interface, whereas other times it may be so wide that the screen sits between the two halves. Virtual keyboards may also benefit from this, both for space considerations and by considering the ergonomics of the device. It may be better for users to grasp the device firmly; if your device is very large, like many tablets, they will not be able to reach the center of the screen, so a split layout may have advantages.

Multitap keypads are capable of very high-speed text entry for populations familiar with their use. They must be designed to follow standards and work without delay. Pressing a key will cause the first valid character to appear (see the Input Method Indicator pattern for more details). Pressing the same key within a short time frame will display the next valid character in turn, as shown in Figure 9-7. This display is a circular list, and will eventually return to the first character. After a brief pause, when another key is pressed, or when a “next” key is used, the character displayed is committed and further key presses will display in the same manner, for the next space in the field.

![](images/10fc1153f4308ea27e55d73c154c4a19c1de5b522d33d26ec63501ec875c32f7.jpg)  
Figure 9-7. An example of how the multitap (or “triple-tap”) text entry method works

Only enable key repeat on fairly high-fidelity devices. For smaller devices, and those expected to be used in difficult environments, such as most mobile devices, do not allow a key press to enter multiple instances of the character. This will help to prevent accidental multiple inputs due to the user being in a vibrating or bouncing environment, such as typing while in a vehicle.

The behavior of mode-switching keys is covered in the Mode Switches pattern. Despite being on the keyboard, they behave very differently and so must be considered separately. Also be sure to see the Press-and-Hold pattern for details on another way to gain access to alternative entry for a particular key.

Directional Entry keys should almost always be included with any hardware keypad. A five-way pad is naturally included in the device design for a typical keypad-based device. For slide-out keyboards and directional keys, an enter function should be included. This will allow users to scroll and submit entries without leaving the keypad. The enter function is often useful on even virtual keyboards, to prevent accidental inputs from the user shifting his grip or reorienting to change the entry mode.

Be sure to accept input from hardware direction keys and enter keys, even for devices that are otherwise touch- or pen-driven. Don’t be that one application that works differently, and confuses users.

## Presentation details

Key labels must be clear, large enough for users to read, and easy to read in all lighting conditions. Alternative labels (Shift or “Fn” characters) should be in a different (less prominent) color, or in a tint of the primary label color. Alternative labels should be above the primary label. There is no need to display uppercase letters as alternative labels to lowercase letters.

On virtual keyboards, use the label for the current state, to ensure that the state is clear.   
Display lowercase labels unless the Shift or Shift Lock key is activated.

Keys must perform their labeled behavior. Note, for example, that backspace and delete are different functions. Users accustomed to Windows will think “Del” means “forward delete” and not backspace as it is labeled on the Macintosh and some other devices.

Especially for hardware keyboards, the use of symbols may be helpful for special keys, such as “Tab” and “Enter”. However, these icons are by no means universally recognized. Use caution when selecting and designing labels, and use simple text descriptions of the function—or text along with an icon—whenever possible.

## Antipatterns

![](images/8028b680a90ab1971d33b04ca21c72b066763fe8b81f3c4c1bd5759eaaaf952b.jpg)  
Figure 9-8. This keyboard has a “Back” button immediately adjacent to other keys, where it can be accidentally hit. Without an Exit Guard this can cause catastrophic failures, discarding large amounts of user-entered data.

Avoid accidental input:

• Lock keypads when sensors determine they are in pockets, against the user’s face (on a call), and so on.

• In any context, if multiple adjacent keys are pressed within a few milliseconds, this can be assumed to be incorrect, and only the most likely key—by physical mapping or Autocomplete & Prediction—should be accepted, or none at all.

• Staggered keyboard layouts can also help to prevent accidental input or increase the accuracy of filtering.

• Be careful when placing functional keys on the keyboard, and provide sufficient space to avoid accidental input. If required, use an Exit Guard to reduce the risk of losing user-entered data, unlike the keyboard shown in Figure 9-8.

On the other hand, be careful going further to avoid accidental input, such as instituting lockout periods. It can be hard to differentiate fast typing from accidental input.

Use caution with backlight in marginal lighting. It is easy to have the backlight illumination match the key material reflectivity, resulting in the label being entirely invisible. Besides careful coordination of the backlight algorithm, using a color that is different from the key material for the label (e.g., yellow instead of white light on black keys) can alleviate this issue.

Do not use conventional insertion point indicators (such as pointers or vertical lines) during multitap, especially when a character is not committed, as it may not make it sufficiently clear where key presses will take effect. Highlight, underline, or otherwise indicate the actual character space being currently affected.

Be careful when implementing layouts, labels, or input methods that are not absolutely standard. Be sure to test this robustly with users. Inertia (by users and operators) will still impede adoption, even if it is a superior idea.

For physical keyboards, a mode in which a 10-key pad is imposed over some of the keys is rarely well understood by the user. When the keyboard is staggered it is also difficult to use. Usually, the best solution when no dedicated number pad is provided is to simply use the number keys along the top row, and lock them on for the user during numeric entry, such as when dialing a number. Be sure to inform the user with an appropriate Input Method Indicator.

## Pen Input

## Problem

You must provide a text and graphical input method that is simple, is natural, requires little training, and can be used in any environment.

Pen Input requires hardware to be dedicated to the input method. When designing for pen devices, you must consider what input methods will need to be adjusted to work best with them. Many pens have hover states, so this would need to be added to existing touch designs.

## Solution

Writing is a function inherently performed by the use of a tool. Until the development of typing, this was exclusively done with the stylus, then the pen and pencil.

Pen interfaces can be an excellent alternative to keypads or touchscreens when touch is unavailable due to environmental conditions (gloves, rain), when the device is used while on the move, or just to provide additional precision and obscure less of the screen. Pen input used to be the norm for touch-sensitive screens, when relatively low-resolution resistive input was the norm; capacitive touchscreens have moved to direct touch and multitouch inputs, but pens as an add-on to touch are making a slow resurgence.

Text input is particularly suited to pen devices, especially for populations (or cultures) with little or no experience with keyboard entry, when there is no standard keyboard for the data type, or for the aforementioned environmental conditions. In situations where only one hand may be used to enter the text, character entry by pen can often be much faster than the use of a virtual keyboard.

Other systems, including newly developed capacitive screens, can use specialized pens to isolate touch input, allowing the user to more naturally interact with the device by resting his hand on the screen. Mode switching is also available, either automatically or manually, to allow either input method.

Pen input devices may be used for multiple types of interfaces, and will often be the primary or only method for the device. This pattern covers only character and handwriting input and correction. Although any pen input panel should also support a virtual keyboard mode, this mode is covered under the Keyboards & Keypads pattern.

![](images/59e0a74f1e54021825498631530641a9d1ab67d8409156868530a03eb000a73e.jpg)  
Figure 9-9. Word entry with pens will appear in an input panel, occupying part of the screen. Options such as the mode switches and special characters appear as buttons within this panel. Translation candidates appear beneath the written word, and may be explicitly accepted or automatically loaded after a pause.

Pen input for text entry may fall into one of two modes:

## Word entry

Provide an area where users may input gestural writing, as they would with a pen on paper. Printed characters are the most common, but script styles should also be supported. The device will use the relationships between characters to translate the writing to complete words, based on rules associated with the language, and will automatically insert spaces between words. The input language, and sometimes a special technical dictionary, must be loaded. See Figure 9-9.

## Character entry

The input panel is broken up into discrete spaces in which individual characters may be entered. This may be accomplished by simply dividing the word entry area with ticks or lines, or presenting a series of individual input panels. The device will translate individual characters, and will generally disregard the relationships between adjacent characters. The user is responsible for spelling words correctly and adding space between words. The language must be set correctly for the fastest recognition, but alternatives within the language family will also be available (e.g., all accented characters for any Roman language). See Figure 9-10.

A subsidiary version of the character entry mode uses a shorthand, gestural character set instead. This is not required for most languages with current input and recognition technologies, but it may have advantages for certain specialized applications or for the input of special characters or functions.

All available input modes should be made available to the user at all times. The user will generally have to select which mode to use, so you will have to provide a method of switching. This does not preclude development of a hybrid approach, or even simply appropriately selecting which mode is most suitable to the current situation. If a gestural shorthand is available, it should be offered as a part of the natural character input method; both will be accepted, and the user may change the input method per character.

In certain cases, such as where the note taking must be as fast as possible or the user is combining images, formulas, and other data with words, you may provide a mode (or a whole application) that will store the gestures without live translation. Later, the user may select all or part of the gestures to translate. This behavior should follow the pattern covered here when similarities arise, in order to preserve a consistent interface. Portions will, of course, be different.

The finger may also, on some devices, be used to input gestural writing without a pen. Many of the principles outlined in this pattern will apply, but the size of the finger may obscure the screen and make this suboptimal.

## Interaction details

![](images/48b4a97e8befe1571e2b966539912fa25a94c1b927689af8786128cae0f4730d.jpg)  
Figure 9-10. Letter input divides the input panel into discrete entry areas. Each character displays a translated candidate. One way to handle correction is for optional translations to be offered in a list. If the best guess is incorrect, the user may open the list and select another option.

When a field that can accept character entry becomes in focus, the input panel should open to the last-used mode. This mode may be a virtual keyboard, but as the user may switch between the modes, the principle applies.

Whenever the user makes a gesture in the input panel, the path taken is traced as a solid line in real time, simulating pen on paper. As soon as a word (or, for character entry, a character) is recognized, it should be offered as a candidate. The translated characters and words are the same as the candidate words, as discussed in Autocomplete & Prediction; see that pattern for additional details on presentation, the interaction to select alternatives, and user dictionaries.

To provide sufficient space for the user to write, you must allow scrolling within the input panel. When the panel is filled, the system may automatically scroll, or the user may be allowed to scroll manually instead, to enable review and correction. Avoid dynamically adding additional space to the input panel, as this will just obscure more of the screen.

At least two methods are available for actions when input is completed:

## Manual

The user completes his entry in the input panel, and presses a button to load the content into the field. The next field may be entered, or the form submitted.

## Automatic

The system loads characters or words into the input field as they are completed, or after a brief pause, to allow the user to make immediate corrections. This may be used to eliminate the need for scrolling the input panel, as it only needs to support one long word, at most.

Mode switches may either commit all completed characters and words to the input field, or switch them to the new entry mode. As discussed in the Cancel Protection pattern, never discard user-entered information.

You must make some provision for functions which are not visible characters, such as line feeds, the “OK/Enter” key, and the “Backspace” and “Tab” keys. These keys should be visible as part of the input panel. See the Keyboards & Keypads pattern for additional information on key placement; the handwriting area of the input panel may be considered equivalent to the character keys, in this sense. Place these other keys in the proper relationship to one another so that the user may find them easily.

On-screen Gestures may also be supported for the user to more quickly input key functions. However, these will require learning, and so should be used as a secondary method in most cases; continue to provide keys for these functions as well.

Some pens will have buttons that the user can activate to bring up contextual menus or which may be programmed to perform other functions. These are not usually noticed and so should be considered like gestures, and are only shortcuts to functions which can be found otherwise.

A robust method for correction must be designed into the system. Do not require the user to manually delete and rewrite, but build in approval steps, or gestures to correct existing phrases, even when loaded to the input field. A good path is to allow easy conversion from word to character input, to allow correction of characters that could not be recognized correctly. Avoid training, but do make the system learn the user’s input method and accept new words in the dictionary so that accuracy improves over time.

Presentation details

![](images/9c3607b007e90aaafc687cf17635397526861b9405191162c01f1f8b131b6b01.jpg)  
Figure 9-11. Parallax for input on screens manifests as a perceived offset between the surface where contact is made and the actual display area. As shown here, this is because protective overlays, the sensing panel, and other materials cause a gap between the two. When viewed straight on, they line up and there is no problem. However, users will not always view directly perpendicular to the screen, and will notice the difference with pen inputs. This is especially troublesome on larger devices, such as tablets and kiosks, as the user cannot view the entire screen straight on.

Writing is entered into an input panel that appears as a part of the screen. For small screens, this should always be a panel docked to the bottom of the viewport and should automatically open when an input field is placed into focus. For larger screens, the input panel may be a floating area displayed contextually, adjacent to the current field requiring input. This panel must always be below the input field, to prevent obscuring the information.

For very small screens, the input panel may take up essentially the entire screen. In this case, you must take special consideration to display the text that has already been entered in order to provide context to the user.

When input is completed the input panel should disappear to allow more of the page to appear.

Any delays in translation or conversion, especially for Autocomplete & Prediction methods, should be indicated with a Wait Indicator so that the user is aware the system is still working. Besides the usual risk of the user thinking the system has hung, the user may believe the phrase cannot be interpreted, and will waste time trying to correct it.

If the pen can be detected as a unique item, you may place the input panel anywhere on the screen. Otherwise, you must always place the panel to avoid accidental input, usually along the bottom of the viewport. Resistive and most capacitive screens will perceive mul tiple inputs and may not be able to tell the difference between the pen and the user’s hand.

Be sure to continue providing a cursor within any input areas on the screen, regardless of the method used. Within the handwriting input panel, you should use a small dot or crosshair to indicate the current pen position. This is crucial due to miscalibration and parallax, as explained in Figure 9-11. Both are always present in screen-input devices. For touch devices, the finger is so large that the errors are generally not obvious, but pens are very small and so reveal these errors and other phenomena.

When the pen leaves the input area, this cursor will revert to the normal cursor. When the pen leaves the screen and cannot be detected, the cursor should disappear. Do not use the desktop metaphor of “cursor always present,” as that is based on the pointing device used. Mice are relative devices, and always provide input from the last location, so the cursor is critical. Pens (and fingers) are absolute devices, and point wherever they are placed on the screen.

If a hardware Directional Entry key is provided which can move the cursor, this is again a relative pointer, and the cursor may reappear from its last location when this input is detected.

## Antipatterns

Be careful when using a pen for large stretches of input on kiosks or where the user cannot rest his hand or arm. The “gorilla arm” effect can impose fatigue or even repetitive stress injury. Allowing the user to rest his hand or arm on the input device, as well as more casual use or regular changes in the type of entry, can avoid this.

The space taken by the input panel must be considered by the page display. Do not allow important information to be obscured by the panel. For example, do not make it so that the panel must be closed to scroll to the bottom of a form so that the Submit button may be activated. Consider the input panel to be a separate area instead of an overlay so that items may be scrolled into view.

Handwriting recognition can be very fast and may even be approximately as error-free as typing on a keyboard. However, correction methods and other parts of the interface can serve to make the overall experience much slower. Use the methods described here to reduce clicks and provide automatic, predictive and otherwise easy access to mode changes.

Respect user-entered data, and do whatever is possible to preserve it. Use the principles outlined in the Cancel Protection pattern whenever possible. Especially when user input must be committed before being populated, do not allow gestures to be discarded by modal dialogs or other transient conditions.

Separate entry areas are generally no longer required technically and so are not suggested unless there is some specific technical or interface reason that the screen cannot or should not be used. If only one screen or portion of the screen is to be used for pen input, ensure that it is as optimized as possible for this task. Generally, this area may be dedicated to input, and may take on all the behaviors of the input panel as described earlier, when in pen input mode.

## Mode Switches

## Problem

You must provide access to additional and alternative controls, without taking up more hardware or screen space, through the use of mode switching.

Mode switches are simple buttons or similar menu items that are easy to implement on any platform that can support the primary input method, such as a virtual keyboard.

## Solution

Mode switching is a method almost universally employed to expand the capabilities of a keyboard or keypad. A default condition exists and is very usable, but to include variations of characters, to access the full range of symbols, and to repurpose entry (such as numeric keypads to text), mode switches provide almost unlimited extra capabilities.

Mode switches are often poorly implemented, with arbitrary and conflicting controls. These can impede text entry enough that text-related functions are underutilized or alternative entry methods are used, and they can be so obscure that users cannot access certain modes at all.

Be sure to implement the same methods across the entire interface, and whenever possible inherit existing standards in the OS. For example, if press-and-hold is used as a shift lock, do not use a double tap to lock the symbol key instead. Be especially careful to avoid drastic differences between virtual and hardware keyboards, when both are available on a single device.

You can also apply the same principles to switching modes in any interface. However, Tabs are the most common implementation outside of character entry. The types of modifiers discussed here only truly become a pattern when used with Keyboards & Keypads, Pen Input, and related functions such as the Dialer.

![](images/dcd79478578ec66282e67faf5b25a754e48d9e200c3915aa43c4636ecdc87772.jpg)  
Figure 9-12. The neutral condition for all virtual keyboards should display lowercase letter keys, to indicate this is the character that will display when a key is pressed. Mode Switch keys should be clearly different from character entry keys, but not so different that they may be confused as being in a selected mode.

Variations can be discussed best by categorizing them using machine-era analogies.   
Consider the Mode Switch to be a replacement for a hard-wired electrical switch.

## Single-throw

An individual button activates an alternative mode. When inactive, the input panel returns to a neutral state. This concept is important because multiple single-throw switches may be added to the panel, such as “Shift”, “Caps Lock”, and “Symbol” keys for a keyboard. This type of entry is subdivided further; the subdivisions are discussed in the “Interaction details” section.

## Multithrow

An individual button switches sequentially between multiple modes. The number is preset and will not vary arbitrarily, but certain modes may be skipped when locked out. Switching is circular—once the last item has been reached, the next switch activation will return to the neutral state. This switch type is very commonly used on keypads with text entry. One key will be a mode switch, moving between multitap, predictive text, and numeric-only entry, for example. In this manner, the key works much like a “triple-tap” entry key, but as it does not enter data itself, it is a Mode Switch instead.

Both of these variations perform equally well on both virtual and hardware keyboards and keypads, and can be used as the mode selector for Pen Input methods as well.

## Interaction details

![](images/07ef4364cda98936ce287e7b73e6f9e79688b852a091b96b635e8106822b5fb2.jpg)  
Figure 9-13. When a mode is entered in which some keys have no function, these keys should retain their neutral position label, but be grayed out to indicate that they are unavailable. This labeling will keep the user oriented through the change. All other keys should remain unchanged. In most states, this will include punctuation, and in all states, the “Return” or “Enter” key.

Single-throw Mode Switches operate in two modes. “Shift” keys (as shown in Figure 9-14) and the like are activated with a single press and are sticky in the accessibility sense. When the mode switch key is pressed, it remains active for a single character entry keystroke, after which it deactivates and the entire entry panel returns to the default state.

The other mode is for locked modes, such as Caps Lock. When activated, these keys will remain active until the panel is dismissed or entry is no longer occurring. In some cases, these will be dedicated keys and will activate as soon as they are selected or pressed. The other option is to make the lock mode an alternative function of the key. To avoid a mode switch for the key, a secondary activation method using only the mode switch key itself must be used. The most typical are:

## Press-and-hold

The mode will be entered immediately upon being selected or clicked. If the key is pressed for a short time, the mode will switch from sticky single activation to locked.

## Press-twice

The mode will be entered immediately upon being selected or clicked. If the key is pressed again in quick succession, the mode will switch from sticky single activation to locked.

You should determine which method to use by following which practice is most common (if any) in the enclosing OS. You should determine the speed of double-clicks or time for press-and-hold by best practice of the OS.

When the user simply selects the same mode switch (or any another mode switch), it will disable the current mode lock.

![](images/156e76590a07ee07c9c286b80846cfc9ad8624fd71ce16297f7b3b39f644f2fa.jpg)  
Figure 9-14. When Shift (or “caps”) is selected, display the capital letters on each key. Though this is the primary method of communicating the mode switch, the switch button itself should also indicate it is selected. If a full-size keyboard is emulated and two Shift keys are present, be sure to indicate that both are active.

The last mode switch activated takes priority, and disables any other switches that may have been activated before. When deactivated, return the input panel to its neutral position, not to the previous activated alternative mode.

When reactivated, input panels governed by single-throw switches will always open to their neutral mode and disregard the last condition.

Multithrow switches always behave as though they are locks. The input mode will remain in the selected mode until manually changed, or the mode becomes unavailable.

For either switch type, mode switching will be disabled for any required entry modes. For example, if a full keyboard is provided but only numeric input can be accepted, it should be locked to numeric input. A virtual keyboard under the same conditions should display a numeric keypad instead.

Multithrow switches should not allow inappropriate entry types. For example, predictive text should not be allowed on password fields (they are unlikely to auto-complete a secure password, it might encourage easily guessable words, or it may even store a unique password in the user dictionary). The unavailable mode should be skipped; if the normal progression is Abc→ABC→T9→123, for a password field, it would simply be Abc ABC 123.

## Presentation details

![](images/62747394b370bc16b6c661d01bc3a70abf72bc5b61aa08a2697933922d824c4d.jpg)  
Figure 9-15. Just some of the many ways to communicate a shift function. Note that single-character capitalization is not precisely the same as Shift. Be sure to use the expected behavior, and make sure your label matches your behavior.

You must always clearly indicate the current mode. If it is not displayed as part of the OS or integral to a virtual keyboard, you must display it as a part of the field. The lock key should change display in some manner. For hardware keyboards, this is generally only displayed as an Input Method Indicator. Ideally, the key itself would illuminate or otherwise change, but the extra cost in hardware is so often deemed prohibitive that it is not particularly common.

For virtual keyboards and keypads, the mode switch key should always change. This may follow the general OS guidelines for a currently pressed key. The locked mode should be different and may change the icon of the key, or change the state of the “pressed” indication.

In addition, virtual keyboards and keypads should change the individual key labels. When in neutral mode, letters should appear in lowercase (a) as in Figure 9-12. When the “shift” mode is active, they should change to uppercase (A). Lock modes have no effect on these. When a key becomes inactive due to a mode change, the label should gray out or otherwise indicate that it is unavailable, as shown in Figure 9-13.

Labels must match in both reflective (ambient light) and transmissive (illuminated backlight) modes. If the “Fn” key is entirely yellow, to match the yellow function key mode labels on the rest of the keyboard, when illuminated this key must be entirely yellow and the labels on the individual keys must also be yellow. See the improper way to do this in Figure 9-16.

Labels must also be clear and unambiguous. Use caution with iconic labels, and test when possible; some user populations will not understand the symbols, and may only determine the intent by position and familiarity with keyboards. See Figure 9-15.

Mode switches for alternative character entry on hardware keyboards, such as numbers or symbols, should use a color to differentiate them. For example, if letter characters are in white, symbols may be in yellow and numbers in blue. The symbol mode switch key should be labeled in yellow and the number mode switch in blue.

Differentiate the mode keys from character input keys by position, shape, and label. A common method to differentiate secondary modes such as the symbol key is to reverse the colors. In the preceding example, the label text would be in black on a yellow background.

![](images/db87a4ba978fef251e5483f71ddd62c75ef458102e299db28469e2c5b2d0ad08.jpg)  
Figure 9-16. This keyboard uses yellow to identify the function modifiers. The reflective labels, for daylight mode, work very well. The function key is all yellow, and the modifier labels are yellow symbols. But under backlight, while the modifier labels remain yellow, the function key itself is black, with the “Fn” label in white. This disconnect is bad, but the change between view modes is even worse.

Do not implement a “Shift Lock.” Older typewriters had no concept of a Caps Lock, but allowed the Shift key to be locked. This also would type the alternative special characters for symbol and number keys. It is not the expected behavior today on any device, and should never be implemented.

Avoid using multikey combinations for routine controls. Despite their prevalence on desktop computing, they are poorly understood and the smaller keypads of mobile devices (even with a sticky key paradigm) do not support their use well. This does not preclude their use for obscure functions. In fact, the lack of any reason for users to routinely use multikey combinations means they are a good way to support highly specialized or technical functions, such as for system resets.

Use caution with backlight in marginal lighting. It is easy to have the backlight illumination match the key material reflectivity, and the label cannot be seen at all. Besides careful coordination of the backlight algorithm, using a color different from the key material for the label (e.g., yellow instead of white light on black keys) can alleviate this issue.

## Input Method Indicator

## Problem

You must make the user aware of the current mode of the selected input method, and of any limits on selecting modes for a particular entry field.

The Input Method Indicator may be integral with the virtual keyboard, or provided as part of the OS, or may need to be implemented within your application as an individual component, within the page or for each field. When it is not available at the OS level, you are encouraged to build a custom version when input types are critical or misunderstanding would cause errors.

## Solution

When not otherwise immediately apparent, an indicator should be placed on the screen to explicitly indicate the current input mode or method.

On virtual keyboards and keypads, the Input Method Indicator is generally not required as the keyboard itself changes modes and serves as an implicit indicator. No “symbol mode” indicator is needed when the keyboard is filled with symbols. There may be value in attaching field-level indicators.

Explicit indicators are valuable with most hardware keyboards and are most common with hardware keypads, which provide numerous entry modes and methods. Only explicit indicators are discussed here. See additional information about virtual keyboard labels under Keyboards & Keypads and Mode Switches.

When additional types of input-field control are offered, such as selection (for cut/copy/ paste) or highlighting, you can use the same indicator field to indicate this condition. Since character input is not valid during these operations, this is a good use of the space, without having to remove the indicator area entirely.

![](images/1f6cc0237d3e14ff9a580fceb19c41258c528ca84a7bc5c53ed1656127adf500.jpg)  
Figure 9-17. Input Method Indicators may be anchored to the individual fields, as on the left, or attached to the viewport frame, usually in the annunciator row or notification strip, as on the right. Both methods have advantages.

The key variation for explicit indicators is of position. Two key options are available, both of which are compared in Figure 9-17:

## Field

The indicator is adjacent to, and usually attached to, the current input field. This associates input with the area on the screen where input will take effect. Each field may have an indicator, so the user may plan ahead, and have a better understanding of what is a field and expose any variations in advance.

## Viewport

The indicator is locked to the edge of the viewport. This associates the input mode with the device, as only one mode may be used at a time. This may seem to indicate that the edge closest to the keyboard or keypad should hold the indicator, but this is not always true. The area in which alerts and other status messages already appear is instead usually the best choice, and the user will learn to glance here for all status information.

Pen Input panels will have a different set of available modes than are discussed here, but they follow the same principle and always indicate through implicit interaction and layout or explicit indicator which mode is currently selected. Their mode indicator may be best attached to the pen input panel. More on this is discussed in that pattern.

## Interaction details

Input Method Indicators are exactly as the name indicates, and are only indicators of changes carried out elsewhere, such as with Mode Switches. No direct interaction with the indicator is possible, or it becomes another type of mode switch.

Indicators are dual-purpose; they always indicate the current input mode and sometimes are a flag to indicate when a particular mode must be used. When a field with a restricted entry (such as numeric only) is in focus, the indicator will switch to the available mode as well as indicate this.

If a field input restriction exists but more than one mode can meet the needs, the automatic selection can become more complex to design. If the keypad is already in allowed mode, no change will take place. If not, the first or most similar available mode will be used. For example, if symbols are disallowed, the Abc mode should be the first selection, but the ABC, Word, and 123 modes can also be used and switched between.

![](images/924fbfdceb9c488595f03fdb1102adab97250bd7f02979c442cbc8eeb1536552.jpg)  
Figure 9-18. A series of indicators, all characters on the left and with a graphic on the right. Note that predictive text is a subset of other methods, and can be input with its own capitalization. Each text label is internally descriptive. The graphics use the pencil as an anchor, and an icon for individual on continuous entry to indicate character or predictive text. Numerous other schemes are available or can be devised.

Make sure these labels are clearly readable and are obviously associated with the input method. Field-level labels should be attached to the edge of the field in some manner, so they are clearly associated. Tabs hanging off the field are most typical.

You can apply this principle within any interactive design to indicate fields with exceptional entry (such as all-numeric) even if the OS has no universal indicator itself.

Viewport-level label location and design is much more associated with the overall OS design, and especially with the design of the Annunciator Row and any Notifications strip.

Labels must not only clearly explain the current mode, but also should be designed to associate with one another so that changes do not confuse the user. Employ the same symbology and typography, at the same size, color, and overall contrast; if outlined, do not have one mode be a solid. For graphical labels, consider an anchoring icon from which all the indicators are built. Figure 9-18 shows two related languages of icons.

All labels must change immediately upon a switch of the input mode.

Mode labels may disappear when irrelevant, such as when not in focus for field-level indicators, or when no input is available on the page for viewport-level indicators. This may be advantageous if space is at a premium and additional information may be presented. However, there can be advantages in offering the information, so carefully consider the downsides to decluttering techniques such as this before implementing them.

The phone Dialer keypad and some other specialized keypads, such as calculators, generally will not need such indicators due to the lack of a mode change. Dialers, for example, support Accesskeys and sometimes use other shortcuts to return results considering both text and numeric input, but this is not a mode switch. When text entry is allowed for a Search Within pattern on the address book, or for recent calls, these are usually switched to at a higher level within the application, and are not just an entry mode switch.

On the other hand, within the Dialer, do go ahead and use an Input Method Indicator if any confusion may arise from restricting multipurpose input methods. For example, if a hardware keyboard is used but only numeric entry is allowed, the lock to numeric input should be indicated on the screen.

You can extend the indicator methodology to related selection mechanisms if relevant to the interaction model, as shown in Figure 9-19.

![](images/bf6bf407bb2cc68c18f541218ac87a73bfe5d68fc9e4d274b1dbebfe0eb18fce.jpg)

![](images/7e986551490986f9bfcc5e0c41ebde502028a0d06904701f13d2622d6d863e9d.jpg)  
Figure 9-19. Other symbols that replace input methods in function, such as select and highlight, shown here, may also replace the Input Method Indicator when active.

## Antipatterns

Never display a mode label that is unavailable, or prevent input by allowing the user to select an improper mode and then blocking input or displaying errors. Always switch to the best available mode instead.

Do not allow the indictor to scroll off the screen, or be obscured by input panels or modal dialogs. If the indicator cannot be locked to the viewport and made to be always on top, use a field-level indicator instead.

Do not use both field- and screen-level indicators. If field-level exceptions are needed, they should be displayed as field “hints” or as contextual content, not as an interactive control or indicator.

Avoid jargon or brand names for labels unless they are very well known. T9 is an almostgeneric shorthand for predictive word entry. As long as your device uses Nuance/Tegic T9, you may use that label. If you use a homegrown solution (and so are legally barred from using the label “T9”), do not use your abbreviation, and use a generic word or symbol instead.

## Autocomplete & Prediction

## Problem

Whenever possible, you should build in assistive technology to reduce the user’s text entry effort, and to reduce errors.

Even when provided by the OS, you may wish to build your own Autocomplete & Prediction methods specific to the operation of your application, or due to the use of information outside of dictionaries, such as URLs in browser history.

## Solution

![](images/56db59cb81d08d135970a0c035ab0be402dd20f6335b8ba3f942d927d9a234e3.jpg)

![](images/495d10f95a903874bc0f6b552a29c6d89e0bc311ac430053ed0882852122eef4.jpg)  
Figure 9-20. Two versions of the suggestion variation. On the left is a simple list. On the right, the most likely match is at the top of the list, and others are in a scrolling area below.

Auto-completion, predictive entry, and related technologies such as spelling correction have become well-established, highly expected assistive technologies for day-to-day computing. For mobile devices, they have proven to be especially valuable due to their relative difficulty and reduced speed of text entry and especially for complex, technical character entry such as for URLs.

Though many current high-end devices either disregard these features or do not consistently implement them, the same pressures apply to any mobile device. At least one method of assistive entry should be employed universally, across the entire device. If it is not available on the targeted OS, consider if adding this feature is possible and if it would assist or distract the user due to the different interface, and determine the best method for the type of entry taking place.

The actual functionality of any of these features, such as the algorithms used to perform the prediction, is outside the scope of this pattern, but is also crucial to its good operation.

## Variations

![](images/1d8b0e65997d4d581b0d43107cfee2da95b4befef8e27bfa36614524f7995837.jpg)  
Figure 9-21. Completion enters the word directly in place, as with this predictive text example.

A range of related functions, associated with all types of text entry, can be considered under the Autocomplete & Prediction pattern:

## Completion

Entry is automatically completed or modified with the goal to create valid entry with as few keystrokes as possible. This is common in search or URL history, when a list of recent or common results is presented during typing. See Figure 9-21.

## Suggestion

One or several suggestions are displayed for an entry. An action is available to change to the suggestion, often by picking from a list. This is encountered in triple-tap text entry (a Next key is provided to scroll through options). See Figure 9-20.

## Replacement

A word or phrase which is recognized as likely to be a misspelling of an entry in a dictionary will be replaced with the correct version shortly after user entry has been completed. No options are offered.

## Error notation

A word or phrase which is not recognized as an item in the dictionary or does not meet the input criteria (e.g., a URL without a TLD) is indicated as such inline. The most common is underlining misspelled words in free-form text entry. Alternatives may be offered after manual selection (at which point it switches to being functionally a “suggestion” variation), but no automatic action is taken by the system. See Figure 9-22.

In some cases, multiple variations may be encountered at once. This is especially common when an entry is completed in the field with the best match, but suggestions are offered adjacent to the field.

Coupled with this variety of functions are a number of interactive methods. This pattern outlines some of the more fixed points and provides general guidelines, but it cannot be prescriptive about all aspects due to the degree of variation.

Interaction details  
![](images/041fcab01935791894af08348675b1e21d0b466860484fac4224b4ff5cf29d90.jpg)  
Figure 9-22. Error notation, such as this miskeying of a triple-tap entry, simply indicates suspect words without changing them.

The suggestion variation requires explicit acceptance by the user. A selection must be made from the list of candidates for any to be applied. No selection will simply use the characters as typed.

Multiple candidate matches should be offered whenever possible. Allow the user to scroll through them, usually by presenting them as a drop-down-style list, and by using Onscreen Gestures or with the up and down Directional Entry keys. In some cases, and most notably with multitap text entry methods, a key is dedicated (while in the mode) to displaying the next available candidate.

Lists of candidates should often be circular, so scrolling past the end will load the first item again. This is especially critical when a single key is used to display the next option. For certain results sets, such as predictive search or URL completion, the results may be too large for this, or a circular list may imply too few results found. For these, use some principles of the Infinite List to present the arbitrarily large, remotely fetched data. Remember, it’s still a Vertical List, even if a very small one.

For lists, a method to select the candidate in focus must be made available. Avoid using methods that have other meanings when a selection is not being made. For example, if OK/Enter is used to submit the form, it may be confusing or lead to errors if it is used for selection of suggested words also.

“Completion” is an implicit method, and any exit of the word, phrase, or field will commit the last candidate displayed. This includes simply pressing the space bar, period key, or comma key at the end of a word, or submitting the entry to a field. On the other hand, if the user keeps typing, his character entry will be used instead, and the completion disregarded or switched to the next best match.

Many of these methods may be used in concert. Figure 9-23 shows one example.

Presentation details  
![](images/b6bce0066bedc2198ea5534bc391278a6e46ec3e3c7648fe374cbfb44e1b9466.jpg)  
Figure 9-23. The variations may also be combined. In this example, words are completed inline with the best match, and options are shown in a list below much like the suggestion variation. Scrolling is used to select options instead of the “next” key of a conventional word input completion variation.

All automatic behaviors, even inline items such as replacement, must take a brief time to take effect, and have a visual cue to attract the user to the behavior. Many of these behaviors, although helpful, are also destructive and may change the intent of the user entry. You must be careful to inform the user of the change.

Selectable completion text may appear in one of two basic places:

## In place

Text is automatically entered and modified in the actual field where entry occurs. This is almost always used with multitap keypad text entry, but is also the way that auto-correction works.

## Adjacent

The suggestion appears adjacent to the word, either right below the entered text or within the input panel itself. Suggestions for search, and matching candidates for Pen Input systems, are typical examples.

A rare variation is to complete “in place,” but in a field, or location in the current field outside the current focus or cursor location. This is best exemplified by code completion, but can be encountered in certain types of form filling. For example, an appointment creator with start, end, and length-of-event fields will find the three closely coupled; completing any two will automatically fill the third. This may seem to be a simple, one-off interaction trick, but it must follow the principles outlined in this pattern to ensure that the user observes the behavior and gets the benefit from the auto-entry.

In place display should be highlighted while still a candidate, such as for multitap text entry. The entire word is still being changed by the user’s character entry, so this highlighting is a sort of extension of the text insertion point.

Candidate options displayed adjacent are typically offered as multiple selections. One item is always in focus, but others may be made available. These may be presented as a list, which can be scrolled through, or only one may be visible as a “bubble” (much like a Tooltip, or Annotation if directly selectable) before selection is made.

Error notifications, such as spellchecks, should appear as a dashed or dotted underline in a very contrasting color. Red has become the typical color, but you should avoid this if the background, text, or overall theme uses red routinely, and especially if it is used as a link color.

## Antipatterns

Avoid automatic replacement without a method for the user to opt out or disable the feature, either session- or device-wide.

Do not violate the principles of Cancel Protection and allow destructive automatic behaviors without a method to revert or correct the change. For example, whenever automatic replacement is used, be sure to allow a method to revert to the spelling as typed. This may be as simple as automatically disabling auto-correction for any second entry of the same word in the same field (or location in the field), so the user may simply rekey the phrase as intended. This is suboptimal as it requires additional typing, but it is better than rejecting the second entry as well, and frustrating the user further.