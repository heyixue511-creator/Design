# Mobile Typography

## Introduction to Mobile Typography

Mobile and small-screen design is largely about communicating information to the user. More often than not, regardless of how exciting and shiny the interface is, this will still be centered on the display of text content.

Mobile typography is about the selection and use of all the type elements within the design. It is only partly about the selection of the correct font and face, and has a great deal to do with selecting display technologies, understanding sizes, and applying conventional design methodologies (size, shape, contrast, color, position, space, etc.) to best employ the type elements.

## Challenges of Mobile Typography

Computer-based type, especially for Internet display, has always been a challenge due to display technologies (resolution), availability of type, color and contrast reproduction variations, and size variations. Mobile devices take these issues, magnify them, and add a spate of unique environmental and use-pattern issues. The primary barrier is of technology, and the primary concern is of readability within the user’s context.

Type originally existed as shapes cut out of metal. When digital typesetting first became commercially viable, this model was followed and these letterforms were turned into vector glyphs, mathematically describing the shape of the character.

Smartphones now generally support this sort of type, and may include many fonts and faces and scale uniformly, allowing almost unlimited display options. Custom type can be included with applications loaded to the device relatively easily, and web-based font embedding is now appearing as well.

Older and low-end devices, including the billions of feature phones in the world, mostly only support “bitmap” fonts. These do not use vector glyphs, but instead draw each character as a small graphic of pixels. For each size or weight, a new set of type images must be loaded. Only a small number of fonts will be loaded, and generally only three sizes will be supported by J2ME applications running on these handsets.

All digital display devices render the final shapes as pixels on a square grid. Even ePaper devices must communicate with the stochastic display device with the same technology. Vector shapes, including type, are “rasterized” to comply with this format, and turned into pixels. Subtle angles and curves can become lost, or appear jagged regardless of antialiasing techniques. See Figure C-1.

![](images/044e7bdb984aef6c1304a96e5c015043bb4ee144abdae8c2540b45b59a457809.jpg)  
Figure C-1. Comparing vector and bitmap (or raster) glyphs.

Although very high-resolution devices make some of the problems hard to see, almost eliminating them, the basic issues persist, and should be considered during design, and selection of proper type.

Technology continues to improve, and both digital foundries and OS makers are regularly implementing new techniques to improve rendering and readability.

## Technology

Although some devices are beginning to allow effectively unlimited type selection, support vector glyphs, and have large amounts of storage and running memory, most mobile devices are still resource- and technology-constrained. General issues of storage on the device, running memory, download times, and cost of network access limit availability of type for mobile application design. As many devices require raster (bitmap) faces, each size is loaded as a complete, different typeface. Most products end up with the device’s default type, or with a very limited set of choices for their application.

Although this challenge will slowly dissolve, it will always be present to some degree. Inexpensive devices, specialist devices (youth, elderly, and ruggedized), and emerging market needs seem to indicate these issues will persist for another several decades at least.

## Usability

Mobiles are used differently from desktops, and even most print use of type. They are closest, perhaps, to signage in that they must be comprehended by all user populations, under the broadest possible range of environmental conditions (e.g., poor lighting) and at a glance. The typical mobile user is working with the device in a highly interruptible manner, glancing at the screen for much of the interaction. The type elements must be immediately findable, readable, and comprehendible.

This is different from the technical challenge in that it is inherent in the mobile device. Users will always interact with their devices in this manner, so it must always be addressed, regardless of the technical implementation.

## An Introduction to Typography

To understand mobile typography, you will need to learn a little of the language and principles of typography in general. Do note that this is a very cursory review of this field. Please use the terms to search for more information, and check the sources listed in the references.

## Baselines and measurements

The basic building block is lines and measures (see Figure C-2).

![](images/9e343d72bddfd8d4b3038a224f5b18e702bbdc2bb5a7288c103e03ffde63d80e.jpg)  
Figure C-2. Baselines, x-height, and some of the other basic ways of measuring type height and vertical position.

The baseline is where all type rides. Note that some round characters can dip below this, but only very little; probably not at all at mobile screen sizes. X-height is the height of the lowercase x, or any lowercase character, excluding the ascenders for those characters. Cap height is the height (more or less) of the tallest ascenders, and of the uppercase characters.

## Letter height and measurements

During the letterpress era, letters were created from cast sorts, or blocks of lead, with the letter being a raised portion in the middle. These sorts were arranged together to form words and sentences. Each metal sort was designed to have a specific measurement. The letter’s height was measured from the top to the bottom of the sort, not the actual letter, which could vary. This standard measurement became known as the type’s point size.

Today, type is still commonly referred to by its size in points. Other related measures are also useful to know, and are increasingly supported by modern mobile device OSes. These are the most important measures:

## Point

One point is 1/72nd of an inch or about .35 mm. It used to be a slightly odd number, but has been standardized with digital typesetting.

## Pica

12 points is one pica. Picas are not used to specify type, but can be used as a larger measure for any other dimensions of layout, such as spacing or column width.

## Em

This is the height of the sort, which is still defined by an invisible box which contains the glyph shape. Although a relative measure (it depends on the typeface and the size of the type being referenced), it is a general unit of measure, and distances and spacing can be referred to in “ems.” Em-dashes are very long dashes.

## En

This is simply half an em. It is mostly encountered not as a unit of measure (though technically it is) but as a definition of a shorter dash. If it takes a short dash, use an en dash, not a hyphen. There are also 1/4 and 1/8 ems, used to define spaces, but they have no special names.

## Twip

Rarely used, but encountered deep in some interactive systems as a scale measure without need of decimals, is the very small twip. This is, properly, 1/20th of a point, but sometimes has other meanings, so be careful when you encounter it.

## Hairline

This is an old printing term, meaning the smallest consistently printable element, and is always a rule such as a line to separate columns. So, it is variable depending on the printing and other reproduction technology available, and not well supported with digital typesetting systems. For digital display, this has no explicit meaning. But the concept is valid, and it would be “one pixel.” Understand the limits of your technology and design to those.

Abbreviations for points and picas can be odd. When alone, “p” is for pica and “pt” is for point, but typographers have a convention (supported by all serious digital design tools still) of “picas” p “points,” as in “3p6,” for example. This may even be encountered as a way to express points without the preceding zero, such as “p6.” Type is always specified as points, such as “72pt.”

## Letterforms and their parts

When choosing the appropriate mobile type, we must understand that each typeface has unique characteristics that affect its legibility across device screen technologies, reading distances, and screen sizes.

In order to create effective message displays that are legible for mobile displays, understanding the basic elements of type is important. The information that follows will assist you when choosing the appropriate typeface for your design:

## Font

The physical character or characters that are produced and displayed.

## Typeface

A collection of characters—letters, numbers, symbols, punctuation marks, etc.

## Glyph

The smallest shape of a character that still conveys its meaning.

## Baseline

The invisible guideline upon which the main body of text sits. Some letters may, of course, extend below the baseline, with descenders. Think g, j, q.

## X-height

The height of the main lowercase body from the baseline. It is usually defined as the size of the lowercase letter x, hence the name. It excludes ascenders and descenders. For body copy in mobile and small-screen devices, the x-height must be between 65% and 80% of the cap height for readability.

## Cap height

The distance from the baseline to the height of the capital letter (and often all ascenders). When measuring to determine a font’s point size, the cap height is used.

## Descender line

The part of a letter that extends below the baseline. The descender line is the guide to which all descenders within the font family rest against. For mobile and small-screen devices, do not use excessive descenders. Avoid exceeding 15% to 20% of the cap height, to avoid excessive leading.

## Ascender

The part of the letter that extends above the x-height. For mobile and small-screen devices, do not have ascenders above the cap height. This is critical for non-English languages, to better support accent marks without excess leading or overlapping type.

## Counters

The negative spaces formed inside characters, such as the shape in the middle of an O. Small type sizes or heavy typefaces may cause counters to appear to fill in and look solid if they are too small, or complex.

## Stress

Adding curvature to the straight shapes of a letterform. This is generally not desired for mobile faces. At best, the small rendered size will simply blur out these subtleties. It could also make it impossible to render sharp letters at small sizes. See Figure C-6.

## Stems

The main vertical or diagonal elements of a character.

## Bowls

The main, generally curved area that forms an enclosed area for a letterform with a stem. Think of the round, enclosed areas on either type of the lowercase a.

Type is composed of letterforms, and very importantly to the readability, the counter forms made up of the white space inside letters (see Figure C-3).

![](images/f31b04edffe4dab8dd3c6328562220c1770dc7cbc4fc48297dfa13164e1f96e9.jpg)  
Figure C-3. Letterforms and counters, or the negative space inside the letterforms.

The space between letters is another sort of counter form, and we will discuss it shortly. Every piece of the letterform also has a name. There are many more of these, but the following list discusses the most important ones for understanding and selecting type appropriate for mobile and small-screen use (see Figure C-4 and Figure C-5).

![](images/9f95da44f05069b14d51f71e7faa6f58a7c118d8728820e13a5ce24551a90c47.jpg)  
Figure C-4. Some of the parts of a glyph (or letterform): the stem, descender, bowl, and crossbar.

![](images/46a889b3549e91d74d1235b20a91f992bae0ef2124b0cea465a04ac977efe856.jpg)  
Figure C-5. More parts of the glyph: the ascender and serif.

![](images/eeb53d3e02fd559eddc44c812efd0b77cd476936fa3edb46e69af72bba1712f1.jpg)  
Figure C-6. Stressed versus nonstressed stems. Dashed lines are straight, so you can more clearly see the curve on the stressed type.

## Serifs

Finishing details at the ends of a character’s main stroke. They extend outward. They are not solely decorative. They also help with our ability to discriminate other characters that make up lines of text. Serif faces are more readable for large blocks of type than sans-serif faces. However, in small mobile type, these may become undetectable, become blurry, and decrease legibility due to the limits of screen pixel technologies.

## Sans serifs

Characters without serifs. For mobile type, sans serif is often the default choice as it works well enough for all uses, at all sizes. For users that have poor vision, you may need to use sans serifs that include more visually distinct characters in certain cases.

## Square serifs

Also called slab serifs, these use heavy, squared-off serifs. Using these may be a good compromise, to ensure that the serifs display at the rendered sizes. Appropriate kerning is important to use for letter discrimination and legibility.

Serifs are available in a few different styles. The basic choices are shown in Figure C-7.

Sans serif (none)

Serif

![](images/1f0ea3d957656bc93d9570f63ab503cf9654437494955d95c740421cabf2768a.jpg)  
Figure C-7. Types of serifs: sans serif without any serif of the conventional type, and a square or slab serif without notable tapers.

For mobile type, sans serif is often the default choice as it works well enough for all uses, at all sizes. Serif faces are more readable for large blocks of type than sans serif faces. If your application is filled with news articles or something similar, consider if a serif face might

work. Square serifs work well, to ensure that the serifs display at the rendered sizes and under difficult lighting conditions. Square (or slab) serif faces are the default faces used in popular eReaders.

All these letterform details matter not just for style, but for legibility and readability. Note that most of the letterform is similar to every other letterform. The bottom half is just a series of undifferentiated legs, as shown in Figure C-8.

## letterform

Figure C-8. The bottom half of each letterform is just a series of undifferentiated legs. The top is where all the readability happens.

So, fairly small portions; mostly in the top half; their ascenders, descenders, counters, and inter-forms are the keys to readers understanding the form and reading the phrase.

## Families and styles

A font family is a group of stylistically related fonts.

A font is a small group of (generally) very similar typefaces, which mostly will vary in weight. A common weight is “bold.” If you have ever heard the term boldface, that’s because it’s a “bold typeface.”

Black is a weight heavier than bold. Roman, Book, or Normal is the default weight. Thin or light is thinner or lighter, essentially the opposite of bold. Numerous other terms are also used, and some fonts have more than a dozen weights.

Weight will, usually, strongly influence the width of the overall type. Readability in long strings can be quite negatively impacted by large blocks of bold text. Very often, other methods (color, shape, position, whitespace) are more suitable for emphasis than bold on small screens. See Figure C-9.

## Weight and width Weight and width

Figure C-9. Weight will usually change the width and readability of type. Be careful when using weight changes as a part of a focus change or other transient state.

Italics are almost script-like faces, both tilted and with additional curves and more decorative serifs. Oblique is the same font more or less just slanted over as a sort of fake italic.

Italics and obliques are not suggested for any purposes on displays with less than about 150 pixels per inch. The angled forms, much like stressed verticals, cannot be rendered sharply. The stairstep effect is noticeable even with type-specific antialiasing techniques. Over about 200 ppi, this begins to become less noticeable, and such types can be used effectively.

Using large blocks of all caps, bold, or italics (or obliques) will result in reduced reading speeds, and lower comprehension. The best results are achieved with mixed case (both uppercase and lowercase) Romans. This can apply even to small passages, such as titles, so if readability is critical consider testing the use of styles such as all-caps titles to be sure they work.

All-caps is sometimes used for emphasis, but this is not always useful, and may provide effectively less emphasis due to reduced legibility.

## Space: Kerning and leading

Proper spacing between characters and lines of type is crucial to readability, but must often be handled automatically for interactive systems. Even well-designed ones must take into account multiple screen sizes and aspect ratios, and sometimes even user-controlled zoom. There is little room for the designer to individually kern letter pairs.

Instead, be aware of the issue, pick fonts that are well designed, and use type display tools that respect the embedded kerning tables and work well for the devices and functions you are designing.

The key spacing attributes are:

## Kerning

The space between any two characters. Ideally, this is automatically generated and follows well-established principles laid out by the type designer, and set forth in a kerning table. See Figure C-10.

## Tracking

The overall intercharacter spacing for a block of text. Tracking has a parent relationship to kerning, if both are defined.

![](images/1dcd78cd666d9446942ca2510267ace0722a903cb4e76868873171a399334caa.jpg)  
Figure C-10. Kerning, showing space between, or space overlapping, individual letterforms.

![](images/16a26533b3e0495bf6e2089c91ccae44db09bbc656e1b25c443294aed6ed1272.jpg)  
Figure C-11. Leading is the vertical distance between lines.

Do not, as a general rule, use monospace faces, where each character takes the same horizontal width, except for specialist reasons, such as examples of code or tables rendered as text, where spacing is crucial to display clarity.

## Leading

Also known as line spacing, or the amount of vertical space from one baseline to the next baseline. Larger leading can often increase readability in poor conditions, such as low light or in motion, but too much can make it impossible to understand that two lines are related to each other. Larger than default leading can be used to make improperly long lines of text more readable, if they are otherwise unavoidable.

This is measured as the vertical distance between baselines (or any like-to-like line). Sufficient room must be provided for the ascenders and descenders to not collide with each other. Additional room must be provided to ensure that lines of type can be read, without forming intercharacter counters in the space between lines. See Figure C-11.

Many typefaces suitable for mobile display have very small descenders to help you eliminate extra leading, and fit more information on a page.

Most languages have some accent characters. These are usually placed above the letterform, occupying the ascender space for lowercase characters, but an above-cap-height space for uppercase characters. Typically, this will require very large leading to enable readability of the accents. See Figure C-12.

Conventional accents are above the cap height...

![](images/9f42661fe69d8a4baae52d501d0ea36dc0d90c00a15b711220790d008e85181a.jpg)  
Figure C-12. Accents above the cap height, and some tricks to avoid this.

This generally is unacceptable for small-screen display, and some faces have special letterforms that fit the accent and character within the cap height. If your application must support accent-enabled languages, consider the effect this will have on your design.

## Alignment

Alignment of type is used as a design tool, and to make the text fit appropriately. All type is “aligned.” Some is justified, but this is a subset. Available types of alignment are:

## Left align

The most common alignment by far. Aside from tabbed-in first lines of a paragraph, and so on, all type is aligned to a single invisible vertical guideline. The type continues to the right until no more complete words can fit, and then it breaks to the next line. The irregular right side makes it also sometimes called “flush left” and/or “ragged right.” Hyphenation can be used to make the “rags” less dramatic, but interactive systems have poor or no automatic hypehnation currently.

## Right align

The opposite of left align, sometimes called “flush right.” Used for special design purposes or to set apart small amounts of type.

## Center

Most used for titles and other items that easily fit the space. For items longer than a line, the same rule about breaking as in left align is used, but there is no straight side, and both edges are ragged. Note that the rags are perfectly symmetrical.

## Justify left

Only really available when optical typesetting appeared, and most successful in the digital age. This uses line-by-line tracking (and sometimes kerning) controls to essentially remove the ragged right side from the left-aligned type by stretching and squeezing the amount of text on one line to make the lines even, or “flush” on both sides. Hyphenation is also heavily relied on to make the lines of more even length. This does not preclude first lines of paragraphs being indented and other spacing for design purposes. How last lines are handled varies stylistically, but usually is allowed to be “ragged,” with the conventional tracking.

## Justify right

Identical to justify left, but flipped so that the ragged last line is on the right.

For narrow columns, texts with long words (such as technical jargon), or systems with poor tracking control (such as those that only adjust interword spacing), distracting “rivers” of whitespace may appear in the text. If this is common, justification may not be suitable.

Do not use monospace fonts and additional spaces to simulate justified paragraphs. This is highly unreadable.

![](images/f6aca45e03c5bb02b1db0e9a18e25efdf7c116e4294f1f36196e57f5558321a1.jpg)  
Figure C-13. Some pointers to selecting suitable mobile type.

## Guidelines for Selecting a Typeface for Mobile and Small-Screen Devices

Research shows that reading from a computer screen is about 25% slower than from paper. Many mobile devices, due to size or environmental complexities, can make this even more challenging. Understand the principles of type and the limits of mobile to help you make appropriate decisions for your content, and your users. See Figure C-13.

Must have:

• X-height between 65% and 80% of the cap height

• Strong counters (or “counter forms”); often, using squared-off shapes for small counters is a good idea

• Unstressed forms; straight, even-width lines

• No excessive descenders; avoid exceeding 15% to 20% of the cap height, to avoid excessive leading

• No ascenders above the cap height; this is critical for non-English languages

Good mobile type should also:

• Be space-efficient. Generally this means narrow, to allow sufficient height for all users to read the characters.

• Not look compressed.

• Be well kerned. Letters should not run together, or have spaces that look like word breaks.

• Have the same, or similar, width for all weights and styles (there is no penalty for using oblique/italics or boldface for emphasis).

• Use subtle serifs when it can be beneficial to the form; consider them for a face, or for some characters of a face.

• Include a true italic. A sloped Roman ensures that hardly any elements are vertical; a true italic can preserve legibility, following the aforementioned rules, while also being different enough to read as “other than body.”

• Be part of a complete family. Serif and sans serif can both be used (titles and body text have different needs), as well as many weights of each, if space is available on the device.

Non-Latin languages will have additional requirements. As always, be aware of regional needs and cultural distinctions.

## Readability and Legibility Guidelines

## Message Display Characteristics and Legibility

Mobiles are used differently from desktops, and even most print use of type. They are closest, perhaps, to signage in that they must be comprehended by all user populations, under the broadest possible range of environmental conditions (e.g., poor lighting) and at a glance. The typical mobile user is working with the device in a highly interruptible manner, glancing at the screen for much of the interaction. The message display is competing with millions of other stimuli in the visual field. Therefore, mobiles must be designed to stand out appropriately, beginning with legibility.

The following is a list of legibility guidelines for mobile devices:

• Avoid using all caps for text. Users read paragraphs in all caps about 10% slower than mixed cases (Nielsen 2000).

• With age, the pupil shrinks, allowing less light to enter the eye. By the age of 80, the pupil’s reaction to dim light becomes virtually nil (Nini 2006). Use typefaces that have more visually distinct characters in certain cases, while still maintaining a desired unity of form.

• Older viewers with aging eyesight can benefit from typefaces that have consistent stroke widths, open counter forms, pronounced ascenders and descenders, wider horizontal proportions, and more distinct forms for each character (such as tails on the lowercase letters t and j).

• Try to use plain-color backgrounds with text, because graphical or patterned back grounds interfere with the eye’s ability to discriminate the difference.

• Sans serif is often the default choice as it works well enough for all uses, at all sizes. Serifs may or may not help with readability, so there is no special reason to use them. Consider using default faces that carry through the sensibility of the OS, such as Helvetica (iPhone’s default typeface). Verdana is also good, as it has a larger x-height and simpler shapes, designed specifically for on-screen readability. There are numerous mobile-specific faces as well.

• Almost all text should be left-aligned, and only items such as Titles should be centered.

• Use typefaces that have strong and open counters (or counter forms). Often, using squared-off shapes for small counters is a good idea.

• Use typefaces with unstressed forms; straight, even-width lines.

• Consider how different pixel densities across mobile platforms affect physical sizes of elements. Using ems to define the size of fonts in CSS may provide ease.

## Message display readability

As we discussed earlier, legibility is determined by how we can detect, discriminate, and identify visual elements. But legibility is not the end to this process of designing effective mobile displays. We must make sure they are readable. When readability is achieved, the user can then evaluate and comprehend the meaning of the display.

Readability is based on the ease and understanding of text. It is determined by whether objects in the display have been seen before. Thus, readability is affected by the message’s choice of words, the sentence structure, appropriate language, and the reading goals of the user (Easterby 1984).

## Reading modes

In September 2004 Punchcut worked with QUALCOMM to develop a typographic strategy with respect to its custom user interfaces within its mobile operating system and applications. In that study, Punchcut determined three modes of reading and understanding behavior that occur within the mobile context (Benson 2006).

These modes consider the duration and size of focus for textual attention:

## Glance

Users are in “Go” mode and they need quick access to frequent and/or critical tasks. Their focus is distracted and minimally on the task at hand. Users rely on shape and pattern recognition in this mode.

## Scan

Users are sorting and selecting, scrolling through lists of choices and options. They apply more focus than when glancing, but not their entire focus.

## Read

Users are reviewing and comprehending information, and apply their entire focus on desired information.

## Language requires context

These three modes are based within the context of the user’s goals. Just like a user’s goals require context, so does the meaning of language derived from the message’s choice of words. Without context, the intended message display’s meaning may become misunderstood.

In our everyday context, we must derive meaning from others’ intentions, utterances, eye movements, prosody, body language, facial expressions, and changes in lexicon (McGee 2001). When context uses more individual pieces, the less ambiguity we will encounter in the message’s meaning.

In mobile devices today, we may not have all of those contextual aids available to help us derive meaning. The mobile user is presented only with the aids the device’s OS, the technology, or the designer’s intention have provided.

## Readability guidelines for message displays

The following guidelines and suggestions should be considered when designing readable mobile displays:

## Vocabulary

– For on-page elements—such as the text of Titles, Menus, and Notifications— use vocabulary that will be familiar to your user. Do not use internal jargon or branded phrasing only familiar to the company and its stakeholders.

– Use vocabulary specific to the task at hand. General and vague titles will create confusion.

– Strive for no help or “FAQs” documentation. With clear enough labels, you can often avoid explaining in a secondary method.

## Images as aids

– Images can provide additional visual aids to reinforce a message’s intended meaning. When needed, use images that are clear in meaning. Do not use images that have arbitrary meanings or require learning.

– Image meanings are socially and culturally created. Even the best icons will not be understood for some users. Using images alone without text labels may result in varying interpretations.

## Overflow or truncation

– Make sure key titles, button labels, soft-key labels, and similar items fit in the available space. Do not allow them to wrap, extend off the screen, or truncate.

– For certain cases, such as lists, tables, and some other descriptive labels, the text may truncate. When possible, do not break words. To indicate the truncation, use an ellipsis character. If not available, use three periods, never two or four or any other number. Sometimes it may be suitable for the word to disappear under the edge of the viewport or some other element instead to indicate the truncate.

– Rarely, the marquee technique may be useful for list items. Text is truncated, flowing off the screen, and when in focus it scrolls slowly so that after a brief time the entire text can be read by the user.

– Long text, in paragraphs, will always wrap using one of the methods described in more in the “Alignment” section.

– If the entire text of a paragraph cannot fit, or is not needed (such as the beginning of a long review) it may begin as a paragraph, and truncate at the end, to indicate there is more content.

## Line length

– From 50 to 60 characters per line is suitable. If you need longer lines, increase leading, but there are limits to how far you can go. At around 120 characters, users might find it difficult to scan that far.

The optimal line length varies around a multitude of factors. These factors include display size, line size, type size, kerning, color, margins, columns, and visual acuity.

– Users’ subjective judgments and performance do not always correlate. Studies have shown that users may prefer shorter line lengths, but may actually read faster with longer lines.

## Typefaces for Screen Display

Back in 1975, AT&T wanted a new typeface to commemorate the company’s 100th anniversary. AT&T indicated that the requirements for the new typeface must fit more characters per line without reducing legibility to reduce paper consumption, reduce the need for abbreviations and two-line entries, increase legibility at the smaller point sizes, and be used for the phone book directory. Matthew Carter, a type designer, got the job and created the new typeface Bell Centennial.

Carter’s new sans serif typeface was more condensed, increased the x-height, and used more space in the open counters and bowls. Aware of the printing limitations, he used letters with deep “ink traps,” which allowed for the counter forms to be open, making them more legible at smaller point sizes instead of becoming filled with ink; this also reduced ink usage, a serious consideration by those who buy ink by the truckload. His typeface was not effective at larger point sizes or on stock paper because the ink traps, little gaps in the corners of the counters, would not fill in and could be seen.

For its intended purpose, at small sizes, on poor paper, it was very effective. A particular typeface often must be selected, or designed, for the specific context. In 1975, available technology, the medium, and users were considered. As designers and developers today, these considerations remain throughout the design process. You need to understand that when choosing a typeface, context of use is key.

• Headlines, especially large ones, will often need to be a different typeface or font than the body copy.

• Italics have been ineffective on digital displays, but very high resolutions will allow their increasing use. Consider them carefully, and understand the difference between a simple oblique version of a font, and a true italic.

• Type can express a hierarchy beyond just size and weight. Should your captions, or bullet lists, use another size, weight, style, or font?

• As in the Bell Centennial example, legibility, readability, and appropriateness are key. If making type small enough makes it illegible, maybe this can be solved with a new font, instead of larger type.

• Show restraint. Designers mock designs with too many fonts as “ransom notes.” There is no hard and fast rule on a number, though.

## Challenges of Mobile Typography Technology Today

Although some devices are beginning to allow effectively unlimited type selection, support vector glyphs, and have large amounts of storage and running memory, most mobile devices are still resource- and technology-constrained. General issues of storage on the device, running memory, download times, and cost of network access limit availability of type for mobile application design. As almost all devices require raster (bitmap) faces, each size is loaded as a complete, different typeface. Most products end up with the device’s default type, or with a very limited set of choices for their application.

## Digital Fonts Today

Digital fonts used today are constrained by the technology display capabilities and the device OS. Most current mobile phones use antialiased fonts. Because of the display’s square pixel layout, antialiasing is used to render some of the pixels’ shades of gray along the edges of the letter. This helps users to perceive the letter as being smooth. Antialiased text is more legible when using larger font sizes for titles and headings; however, using antialiasing text in small font sizes tends to create a blurry image. Consider the mobile display’s capabilities when choosing the font size and font family because they might not be available for that mobile device.

Companies such as Microsoft, Bitstream, Monotype, and E-Ink have introduced their own type of font display technologies to improve readability for such devices. Some of these font technologies are constrained to a specific fixed arrangement of pixel display technology. ClearType, Microsoft’s subpixel rendering technology, is orientation-specific and will not work on devices whose display orientation can change. However, ClearType works very well on LCD displays because of the fixed pixel layout. On some OSes, there may be an “automatic” font setting which detects if the display is an LCD or CRT to turn on or off subpixel rendering.

## Font Rendering Technologies

The following are examples of some of the available rendering technologies used to improve type legibility on digital displays:

• ESQ Mobile Fonts by Monotype Imaging (http://www.monotypeimaging.com) are optimized for smartphone and feature phone displays in addition to other consumer electronics and embedded systems. ESQ Fonts also include WorldType, which offer wide language support on mobile devices.

• Bitstream Font Technology by Bitstream (http://www.bitstream.com) uses Font Fusion and Panorama technologies optimized for resource-constrained mobile devices.

• Apple Advanced Typography, or AAT, is Apple’s (http://developer.apple.com/fonts) advanced font rendering software. It is a set of extensions to the TrueType outline font standard, with similar smart-font features to the OpenType font format.

• ClearType by Microsoft (http://www.microsoft.com/typography/default.mspx) has greater pixel control by turning on and off each of the colors in the pixel. This makes on-screen text more detailed and increases legibility.

• TrueType is an outline font standard originally developed by Apple Computer in the late 1980s. TrueType is common for fonts on both the Mac OS and Microsoft Windows operating systems. TrueType was developed to ensure high control of how fonts are displayed down to individual pixels.

Be aware of display technology. ePaper, for example, is a series of technologies used for electronic digital displays such as eReaders (note that “E-Ink” is but one of many brands, and is not a generic label). ePaper generally relies on reflected, not emitted, light, by suspending particles in a liquid; a charge causes the dark particles to rise and be visible, or bicolor particles to rotate from light to dark (technologies vary) and display dark areas on a lighter surface, much like ink on paper.

Although the stochastic nature of the display elements, contrast and low speed of the display change, make ePaper design very different, current display technologies can only drive them with conventional backplane technology, so pixels are effectively square, as with all other display types.

Although ePaper is a dramatic departure, every display technology has its unique attributes. OLED and AMOLED displays, for another example, are lit-pixel displays (without a backlight). White text on black will, unlike a backlit display, use much less power than black text on white. This may be a key design consideration for those devices.

## Greeking

Greeking is a design term used to refer to using placeholder text or images instead of the real, final text. Sometimes this is important or unavoidable as the real text is not available, or would be irrelevant such as with a sample document.

Design documentation must by nature represent content. Many wireframe techniques use boxes or other greeking methods, instead of using real content, even when it is available. This is a somewhat contentious issue, but our experience in design indicates that the proper choice is crucial in several different facets. See Figure C-14.

![](images/a76be874423c7c8ef794a468a52aa9bd7a378b1e758d3893cb3e4fba877c179a.jpg)  
Figure C-14. The many types of greeking, and some real content for comparison.

Aside from graphical representations of type, another common representation is the classic typographer’s greeking. The entire, original version of it is reproduced here:

Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam quaerat voluptatem. ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?

At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. et harum quidem rerum facilis est et expedita distinctio. nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.

Hanc ego cum teneam sententiam, quid est cur verear, ne ad eam non possim accommodare Torquatos nostros? quos tu paulo ante cum memoriter, tum etiam erga nos amice et benivole collegisti, nec me tamen laudandis maioribus meis corrupisti nec segniorem ad respondendum reddidisti. quorum facta quem ad modum, quaeso, interpretaris? sicine eos censes aut in armatum hostem impetum fecisse aut in liberos atque in sanguinem suum tam crudelis fuisse, nihil ut de utilitatibus, nihil ut de commodis suis cogitarent? at id ne ferae quidem faciunt, ut ita ruant itaque turbent, ut earum motus et impetus quo pertineant non intellegamus, tu tam egregios viros censes tantas res gessisse sine causa?

Quae fuerit causa, mox videro; interea hoc tenebo, si ob aliquam causam ista, quae sine dubio praeclara sunt, fecerint, virtutem iis per se ipsam causam non fuisse. — Torquem detraxit hosti. — Et quidem se texit, ne interiret. — At magnum periculum adiit. — In oculis quidem exercitus. — Quid ex eo est consecutus? — Laudem et caritatem, quae sunt vitae sine metu degendae praesidia firmissima. — Filium morte multavit. — Si sine causa, nollem me ab eo ortum, tam inportuno tamque crudeli; sin, ut dolore suo sanciret militaris imperii disciplinam exercitumque in gravissimo bello animadversionis metu contineret, saluti prospexit civium, qua intellegebat contineri suam. atque haec ratio late patet.

## John McWade wrote in Before and After Magazine 4(2):

After telling everyone that Lorem ipsum, the nonsensical text that comes with Page-Maker, only looks like Latin but actually says nothing, I heard from Richard McClintock, publications director of The Garnet at Hampden-Sydney College in Virginia, who had enlightening news:

“Lorem ipsum” is Latin, slightly jumbled, the remnants of a passage from Cicero’s De Finibus 1.10.32, which begins thus: ‘’Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci veldt…’’ [There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain.]. De Finibus Bonorum et Malorum, written in 45 BC, is a treatise on the theory of ethics; it was very popular in the Renaissance.

What I find remarkable, is that this text has been the industry’s standard dummy text ever since some printer in the 1500s took a galley of type and scrambled it to make a type specimen book; it has survived not only four centuries of letter-by-letter resetting but even the leap into electronic typesetting, essentially unchanged except for an occasional ‘ing’ or ‘y’ thrown in. It’s ironic that when the then-understood Latin was scrambled, it became as incomprehensible as Greek—hence, the term “Greek” for dummy text.

This term has since been expanded to the broader meaning of any false content, even to include simple gray lines or boxes representing type.

## Designing with Words

There are several issues with the use of greeking:

• It is a specialized design language. The styles using boxes or lines especially will not always be understood by consumers of the document. Any confusion, even if solved before implementation, can cause delays, or induce errors in estimation.

• Far too often, the exact same fake content is used over and over again. Every bullet starts “Lorem ipsum,” for example. This does not accurately represent the variety of content that would be encountered, so it is not an adequate representation of the final design.

• Text greeking of the “lorem ipsum” variety is not universally recognized as fake content, so it may have to be explained.

• Latin is not English, and does not have the same cadence, or average length of words or distribution of those words. Letters are also used at different rates, adding to the lack of fidelity with real content.

Many of these issues become worse on mobiles, with small column widths. Greeked text will wrap in ways unlike real content. This is even worse if the real text is in a particular technical language as there are no compound words, and phrasing is not organized in this manner.

The suggestion, therefore, is to use real copy whenever possible. Content either already exists, or will be created for your project. Either get this copy as early as possible (even if it is in draft format) or work closely with the content team to create enough for your mockups.

In the same way you are a design or software professional, writers have a specific skill set that cannot be simulated. I rely on writers whenever possible to help create everything from page titles to button labels. They will do a better job, in less space, than you can do.

## Respect Names and Languages

Although already mentioned within the Ordered Data pattern, it is worth restating here that real names must always be displayed. Use caution when picking names of individuals, products, and locales when providing placeholder or sample content. Make sure there is room for as many of the likely results as possible.

It may be useful to specifically keep long names for various data fields. For names, for example, I have long used a former coworker (who has since returned to Thailand and teaches HCI), Narin Jaroensubphayanont. When you include hyphenated last names, this is really not that overwhelmingly long, even for the United States.

This also points out a crucial lesson in regionally specific information. Different languages have different cadences, so if you’re designing a global application, periodically load a language other than your default. Check local address and name formats to make sure they fit.

## Seriously, no jokes

If you have to make up content for temporary, internal use, there is often an inclination to use pop culture references, or make internal jokes. If you are still doing this, you will be surprised to find out what a bad sense of humor many, many people have.

Designers have been fired and customers have been lost over placeholder copy. Although guidelines could be provided, even around the edges of these there is room to make costly mistakes.

Even seemingly innocuous fake content can cause immense trouble. There are incidents where placeholder phone numbers have made it into production. To look real, they were not 555 numbers or anything else clearly fake, so ended up not being fake but dialing real locations. Two real-world cases:

• The phone listed for a retail store instead resolves to a house. The retired residents, having lived there for decades, received dozens of calls a day and do not want to change their long-held number that has now been published in numerous locations. Lawyers got involved, and it took years to sort out.

• The phone number listed to contact customer care dials an “adult chat” number. This was easily rectified, but offended customers left, or had to be offered apologies from senior management and expensive enticements to remain customers.

Yes, really. These both happened.