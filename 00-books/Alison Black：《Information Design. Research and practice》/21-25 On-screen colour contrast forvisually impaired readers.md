# On-screen colour contrast for25 visually impaired readers

Selecting and exploring the limits of WCAG2.0 colours

Frode Eika Sandnes

Design for the web is challenging because the designer has limited control over how the end result is perceived by the user. Reduced vision is probably the most common impairment among users on the web, and the types of visual impairment vary greatly. A fundamental condition for perceiving visual stimuli is the presence of suficient contrast, which often still leaves users at the mercy of designers. The widely recognized WCAG2.0 accessibility guidelines provide minimum contrast levels recommendations for the web. However, two problems with WCAG2.0 include its mathematical complexity that repels designers and encourages a post-design checklist approach. This paper explores visual contrast and the properties of the WCAG2.0 contrast definition. Simplified contrast calculations are proposed that will sufice for most practical purposes. More importantly, the paper argues for formatively embedding contrast-limit constraints into the design process eliminating the need for post-design checks and unnecessary and exhaustive user testing.

## (In)visibility and (dis)ability

Universal accessibility often addresses users classified has having a technical loss of sight and how the visual content can be replaced using other modalities perceivable through hearing and touch. Still, most users rely on visual contents, even though many users have reduced vision – especially as vision often deteriorates with age (Wood 2002).

A common cause of invisible web content is not related to the users’ vision, but rather that designers hide important functionality. An example of hidden functionality is a menu that is revealed when the mouse pointer is placed above a  certain area of the web page. Users therefore have to explore the user interface. Visible functionality needs to be perceivable by the senses (Norman 1998).

Visible content may become invisible next to competing visual elements. Competing visual elements become noise. Visible content may also become invisible if the organization of the information on a web page does not match the expectations of the user. Users tend to interpret the intended structure of a page and thereby predict the location of the desired target. If the logical structure it not communicated well, more efort is needed to locate the target (Spencer 2011).

## Contrast = diference

Sight can be described as the ability to perceive diferences in the field of view, that is, diferences in the light that is captured by the eyes from various angles. If the eye simply captured a single pixel it would not be able to detect spatial diferences. The only diferences that can be captured with one pixel are temporal variations, that is, changes in the pixel value over time. However, with two pixels it is possible to determine whether the two pixels are equal or diferent.

Humans are incapable of evaluating the absolute intensity of a single light source. For example, it is dificult to objectively evaluate the brightness of a  wall painted in a  single colour. We are able to approximately describe the hue, but we often incorrectly assess the intensity of the light reflected by the wall. This is usually due to a lack of comparison.

Efective visual communication relies on the eye’s ability the detect diferences in light. This is what usually is referred to as contrast. Large diferences result in high contrast, while small diferences result in low levels of contrast. Images, symbols, and text are all dependent on suficient contrast to be visually perceivable.

Text is probably the most significant carrier of information on the web. It is thus important that there is suficient contrast between the characters making up the text and the background on which these characters rest, in order for characters to be perceived. In other words, there has to be a suficiently large diference between the colour vector which is used to define the text and the colour vector that is used to define the background. It is assumed that the colours of both the text and its background are uniform. Given the text colour $\upsilon _ { \mathrm { t e x t } }$ and background colour $\nu _ { \mathrm { b a c k g r o u n d } } ,$ the contrast, represented by their diference, needs to be larger than a minimum threshold t.

$$
t = \left| \nu _ { t e x t } - \nu _ { b a c k g r o u n d } \right|\tag{1}
$$

The perception of colour and brightness depends on the area or viewing angle. Small text requires high contrast, while larger text requires lower contrast levels. This size factor is reflected in the diferent WCAG contrast recommendations for body text and headings. In addition, stroke width also makes low-contrast text easier to read. Ricco’s law predicts this (Hood and Finkelstein 1986), namely that the product of the threshold intensity and the area is constant. Contrast is also related to the luminance intensity and follow Weber’s law (Majumder and Irani 2007), that is, the higher the luminance the larger the diference is needed to detect the diference. This phenomenon is the basis of several image contrast enhancement algorithms.

A  common design approach is to employ a  high level of contrast between the body text and the background, for instance black on white.

The headings may have a  diferent hue with a  lower contrast, often in a tone of colour found in other visual elements of the design to establish a connection between the image and the text.

Although not yet relevant to the web, contrast can also be provided by the surface material characteristics – an efect that is often exploited in the design of physical products. That is, a surface may have areas with a reflective blank surface and matt non-reflective surface, such as some pocket books with matt non-reflective background and book titles in the same colour, but reflective. Although the colour of the text is identical to the colour of the background, the eyes are able to detect the diference because the way the light is reflected diferently in the diferent parts of the surface. Such contrasts are also tactile as they often can be felt with the fingertips.

Contrast is also achieved with shadows and reflective properties of the material such as inscriptions on stone tables and jewellery or coins. Coins have distinct visual patterns although the entire surface has the same colour. Obviously, the visual patterns emerge due to the shadows cast by the surface contours and the diferent reflection angles (Foley et al. 1995).

## WCAG2.0 contrast

Web developers often work with hardware oriented red, green, and blue (RGB) colour vectors, while web designers often work with the HSBcolour model that more closely resemble the human visual system where colours are described according to hue (red, green, yellow, etc.), saturation (the degree of whiteness), and brightness (from bright to black). According to this model contrast can be achieved with diferent hues, different levels of saturation, or diferent levels of brightness. Alternatively, contrast is achieved through a combination of these three types of contrast diferences.

The human eye is most sensitive to diferences in brightness and it is recommended to predominantly rely on brightness contrast as hue and saturation have limited efect for users with colour deficiencies (Knoblauch, Arditi, and Szlyk 1991). A visual design based on brightness contrast is therefore also robust in terms of colour blindness, that is, the design is perceivable by individuals who are unable to distinguish certain hue combinations.

The World Wide Web Consortium (W3C) Web Contents Accessibility Guidelines (WCAG2.0) refer to luminance contrast which combines hue, brightness, and saturation. The most basic level ‘a’ success criterion of the WCAG2.0 guidelines (criterion 1.4.3), recommends that body text should not rely on hue contrast at all. This, for example, means that an arbitrary red and green does not guarantee contrast. It is relatively easy to understand the level ‘a’ criterion and it will not be discussed any further herein. The stricter level ‘aa’ criterion states that the contrast should have a luminance contrast ratio of at least 4.5:1 for body text and 3:1 for headings rendered with larger text. The most strict recommendation, the level ‘aaa’ criterion, suggests a contrast ratio between body text and its background of as much as 7:1 and that the contrast ratio for headings are 5:1.

The level $\mathbf { \dot { a } } _ { }$ criterion ensures that designs are robust to colour blindness. The level ‘aa’ criterion is based on empirical findings for users with a  visual acuity of 20/40 and the strict level ‘aaa’ criterion is based on empirical findings for users with a visual acuity of 20/80.

WCAG2.0 defines luminance contrast according to the standards ISO-9241–3 and ANSI-HFES-100–1988 as

$$
c o n t r a s t = \frac { L 1 + 0 . 0 5 } { L 2 + 0 . 0 5 }\tag{2}
$$

where $L 1$ is the luminance of the brightest colour and $L 2$ is the luminance of the darkest of the two colours. Luminance is defined as

$$
L = 0 . 2 1 2 6 r + 0 . 7 1 5 2 g + 0 . 0 7 2 2 b\tag{3}
$$

The factors r, g, and b represent the linear red, green, and blue colour components. The conversion between linear c and nonlinear components k is based on IEC/4WD 61966–2-1 and (Stokes et al. 1996) as

$$
c = \frac { k } { 1 2 . 9 5 }\tag{4}
$$

$$
\mathrm { i f } k < = 0 . 0 3 9 2 8 , \mathrm { o r }
$$

$$
c = \left( \frac { k + 0 . 0 5 5 } { 1 . 0 5 5 } \right) ^ { 2 . 4 }\tag{5}
$$

if k > 0.03928. The value k is given by

$$
k = \frac { \mathrm { ~ C ~ } } { 2 5 5 }\tag{6}
$$

where C represents one of the three RGB-vector values defined by an 8-bit value in the interval 0 to 255, where 0 represents no contribution and 255 represent the maximum contribution of the given RGB-channel.

This formulation is relatively intricate and does not serve as an inspirational tool for designers with a limited interest in mathematics. Contrast calculators1 are therefore often used for checking contrast levels against the WCAG2.0 guidelines.

## Simplified luminance contrast calculations

The luminance contrast formulation referred to in WCAG2.0 provides more accuracy than is needed for most practical purposes, and a computer or a scientific calculator is needed. This section proposes a simplified formulation that requires fewer steps and only a basic calculator. The alternative luminance computation is derived as

$$
L = \frac { 3 . 2 7 r ^ { 2 } + 1 1 g ^ { 2 } + 1 . 1 1 b ^ { 2 } } { 1 , 0 0 0 , 0 0 0 }\tag{7}
$$

where L is the luminance, $r , g ,$ and b are the red, green, and blue html components, that is 0 to 255. This simplification is achieved ignoring the linear part of the transfer function in Eq. 4, and replacing the power 2.4 with a square and removing the factors in the nominator and denominator. Finally, the constants are factored out. This simplification yields fewer than 1% errors in most cases.

The contrast between two colour vectors is found by simple substitution and refactoring as

$$
\small { c o n t r a s t } = \frac { 3 . 2 7 { r _ { 1 } } ^ { 2 } + 1 1 { g _ { 1 } } ^ { 2 } + 1 . 1 1 { b _ { 1 } } ^ { 2 } + 5 0 , 0 0 0 } { 3 . 2 7 { r _ { 2 } } ^ { 2 } + 1 1 { g _ { 2 } } ^ { 2 } + 1 . 1 1 { b _ { 2 } } ^ { 2 } + 5 0 , 0 0 0 }\tag{8}
$$

where $r _ { _ 1 } , g _ { _ 1 } , b _ { _ 1 }$ is the brightest colour, and $r _ { _ 2 } , g _ { _ 2 } , b _ { _ 2 }$ is the darkest colour. The total error in contrast with the simplified luminance expression is usually between 0 and 7.5%. For example, to compute the contrast between white (255, 255, 255) and red (255, 0, 0) these values are substituted into Equation 8:

$$
\begin{array} { r } { c o n t r a s t = \frac { 3 . 2 7 \cdot 2 5 S \cdot 2 5 S + 1 1 \cdot 2 5 S \cdot 2 5 S + 1 . 1 1 \cdot 2 5 S \cdot 2 5 S + 5 0 . 0 0 0 0 } { 3 . 2 7 \cdot 2 5 S \cdot 2 5 S + 1 1 \cdot 0 \cdot \cdot 0 + 1 . 1 1 \cdot 0 \cdot \cdot 0 + 5 0 . 0 0 0 } = \underline { { 3 , 9 } } } \end{array}
$$

Irrespective of the complexity of the contrast calculations it can be hard to mentally understand the relationship between colour choices and the WCAG2.0 level ‘aa’ and ‘aaa’ criteria. The following sections thus explore the efects colour choices have on remaining available colours in the colour space.

## RGB impact on luminance

Figure 1 illustrates the luminance impact of the red, green, and blue components respectively according Equation 3. Clearly, the green component has the strongest impact on the luminance of a colour of about 70% with its large weighting in Equation 3; the impact of the red component is less than

Figure 1   
Luminance   
impacts of the red, green and blue   
components.

![](images/6f808b4a34364935f6fa6b0526285cc410604e88316125efabfc84620e0b566e.jpg)

a third of green with approximately 20% impact. The blue component has the least impact on luminance with a mere 7%. In other words, humans are better at perceiving changes in green, and least able to perceive variations in blue. Consequently, when selecting colours more efect is achieved by varying the green component, while varying the blue will have the least efect on contrast.

## Exploring contrast as a function of luminance

Figure 2 explores WCAG2.0 colour contrast with a concrete example where the contrast of (a) white, (b) grey, (c) dark grey, and (d) black are plotted as a function of the red component. The WCAG2.0 contrast limits for the ‘aa’ criteria are plotted as horizontal lines in orange, where body text is the thin line (4.5:1) and headings as a thick line (3:1). The ‘aa’ criteria are plotted in green with the limits for body text as the thin line (7:1) and headings as the thick line (5:1). Clearly, the contrast levels are overall larger between red and white (luminance 1) for which most of the red ranges satisfies the ‘aa’ and ‘aaa’ criteria besides the very bright reds.

When comparing red and grey with a luminance of 0.5 (medium bright) nearly half of the red shades satisfy the most strict level ‘aaa’ criteria while only the brightest part of red does not satisfy the level ‘aa’ heading criteria. The contrast curve is reversed when comparing red with black (zero luminance). None of the shades of red satisfied the strict ‘aaa’ criterion for body text and only a small part at the high end of red satisfied the ‘aaa’ heading criterion and the ‘aa’ criteria. A comparison between red and a dark grey with a luminance of 0.08 reveals that none of the shades of red satisfy the ‘aa’ or ‘aaa’ criteria. In simple terms, red gives higher contrast with bright colours compared to dark colours.

## Contrast efects in the colour plane: single choices

The previous example illustrates the efects of colour choices as a function of one colour component. This section explores the efects of colour choices in the colour plane, that is, the efects colour choices has on two of the three colour components. When a given colour is chosen for the text or the background, certain parts of the colour space becomes unavailable as it represents colours with insuficient contrast according to WCAG2.0. The red–green plane is chosen as these components have more impact on contrast than the blue component. A two-dimensional analysis is chosen because it is challenging to simultaneously visualize the entire threedimensional colour space (Gonzalez and Latulipe 2011).

Figure 3 (overleaf ) shows the efects of colour choice in the red–green colour plane. The white area without a grid shows the parts of the colour space that yield insuficient contrast, orange indicates parts of the colour space that satisfy the level ‘aa’ criteria for headings, the yellow area satisfies the level ‘aa’ criteria for body text, and the green area satisfies the strict level ‘aaa’ criteria for body text. Figure 3a shows the efects of selecting black (the bottom left corner). The area on the right side of the red–green plane constitutes colours that satisfy ‘aa’ headings, that is, colours with a green component with a pixel value greater than 125 goes well with black. Colours with a green component greater than 175 all satisfy the level ‘aaa body text criterion. If only using red, a value of 200 or more is needed to achieve contrasts that satisfy the level ‘aa’ criterion for headings. The red–green plane is separated by curved lines, which indicates that combinations of red and green contribute nonlinearly to contrast. Hence, the illustrations confirm that it is hard to mentally comprehend contrast relationships.

![](images/2f52ff809287bde3ba5c5cae35faf2ac4e3048942589856a378e32e717b465d9.jpg)  
a. Red and white (luminance 1)

![](images/3e0022e749abecb48fca45120ec69dab9d5f63bea0cf2c92ffa0e100e9cb47da.jpg)  
b. Red and grey (luminance 0.5)

![](images/a3af45c932a78f1e1cbd4fbb11bfea2eaff23d7a45794f3dd31a4781257832ca.jpg)  
c. Red and dark grey (luminance 0.08)

![](images/1196f8379e2f9387f464307cc83ca2650a76e45824711de96239afb3fb28b518.jpg)  
d. Red and black (luminance 0)  
Figure 2a–d Contrast as a function of luminance. Horizontal lines shows the requirements for ‘aaa’ body text, ‘aaa’ headings, ‘aa’ body text and ‘aa’ headings from top to bottom.

Figure 3b shows that by selecting white (in the top right corner) the situation is reversed. That is, the left side of the red–green colour plane is dominated by low levels of green constitute colours that yield contrasts that satisfy the requirements for ‘aa’ headings.

![](images/10c29f53e9688db8a90008aa98e0ad6f359bf2deea8edf67324904d4a0a18aa9.jpg)  
a. Black (0, 0, 0)

![](images/86a3c2e14111bcb47f42f2dbc335b3ffd578feea3a370848606ed39133586d32.jpg)  
b. White (255, 255, 255)

![](images/e858dfc5c1963a1f7c71f08ebe95e1a87f88478c3f4d7de0c474c76de84bf82e.jpg)  
c. Red (255, 0, 0)

![](images/3862a27553a3d010c3d0a7cb02f65eeba9e1616f90f9b50e67d873e3672cbd36.jpg)  
d. Green (0, 255, 0)

Figures 3c and 3d show the efect of selecting red (in the top left corner) and green (in the bottom right corner), respectively. The area of valid contrasting colours is smaller with red than with green. The explanation for this is that red constitutes medium luminance requiring suficient colour distance towards the low luminance values and high luminance values. Green, on the other hand, is a high luminance colour, which is closer to white. This means that a larger area in the low luminance area of the colour plane yields suficient contrast.

Figure 3a–d Efect of colour choices on contrasts in the red–green plane.

## Contrast efects in the colour plane: double choices

Is it possible to find more than two colours with the property that they all have suficient contrast in relation to each other? This section attempts to answer this question by visualizing the colour plane as a result of two colour choices.

It may be useful to distinguish between colour sets and local colour sets. A colour set is defined herein as a set of colours used such that suficient contrast between these colours is needed. For example, a  text colour and a background colour makes up a colour set. A local colour set is one instance of a colour set used in one part on a web page. However, a web page may contain multiple local colour sets in diferent and disjoint areas of the display real estate. The contrast requirements apply within each set, but not between the sets. Figure 4 shows a colour set with three colours that can be used in any combination and four local colour sets with two colours each.

![](images/77dea18d9d66c36eacd26cc580e73b089ae328651f0e34f0865555de6dab676f.jpg)

Figure 5a shows the efect of selecting black and white, namely that it is possible to select a  third contrasting colour. The area of third colour<sup>text</sup> <sup>text</sup> options that all satisfy the ‘aa’ criterion for headings is significantly large, that is from green components in the range of 125–160 with zero red up to<sup>text</sup> <sup>text</sup> all greens less than 100 with maximum red components. Two small areas also satisfy the ‘aa’ body text criterion, that is the colours in the region (180,  110, 0) and (235, 55, 0). None of the colours satisfy the two ‘aaa’ criteria.

Figure 4 a. A colour set. b. Four local colour sets.

Figure 5b shows the valid parts of the colour space after selecting white and red. This area is smaller, but the proportion of the area that satisfies the ‘aa’ body text criterion is larger. Most of these colours are in the black part of the plane. Figures 5c and 5d show green combined with white and black, respectively.

![](images/ba2111f8f719fa5b57df51cbd0f8baac3ee913a235a3461afaacb3cb691c5e45.jpg)  
a. White (255, 255, 255) and black (0, 0, 0)

![](images/ea799aa798a515f55a433277e69e0a1a3e2a62a9e6e9463e0f07a55e3ac2915f.jpg)  
b. White (255, 255, 255) and red (255,0,0)

![](images/3161e385def20ef36b43a13f3b021494f7b5bcf10dff67b393e73aaba0ac8128.jpg)  
c. Green (0, 255, 0) and white (0, 0 ,0)

![](images/9e17e7f86baf115c664804a3358eb4be31866ffb0fabcfec650b30f317a48bdb.jpg)  
d. Green (0, 255, 0) and black (0, 0, 0)  
Figure 5 a–d  
Efects of two colour choices on contrast in the red–green plane.

The results show that is possible to select up to three colours that simultaneously satisfy the WCAG2.0 ‘aa’ heading criteria, but not more than three colours. It is not possible to select three colours that simultaneously satisfy the ‘aa’ body text criterion or the strict ‘aaa’ criteria. The conclusion is that global colour sets have a maximum size of three and the third colour can only be used for larger text headings.

## Conclusions and implications

WCAG2.0 defines the theoretical minimum contrast recommendation. It is therefore advisable to allow for a certain margin of error. The theoretical minimum recommendation defined by WCAG is static. The developer has limited control over how the end results appear to users. There are several factors at play, such as display characteristics, lighting conditions, and the observer’s vision. Conditions indoors and outdoors are diferent and also vary according to the time of day (Sandnes 2010).

A common question is whether one should always strive to maintain maximum possible contrast. Too much is usually better than too little, but there are situations where too much contrast may pose a  problem. For example, self-luminous white text on a black background may ‘bleed’ and therefore be dificult to read (Bressan et al. 1997). Colour bleeding can be used to explain the use of bright yellow or green text on black background found on information boards in public spaces such as train stations and airports.

There is a general myth that universal accessibility requirements constitute constraints that make accessible websites unattractive and boring. However, the best designers will exploit the available opportunities despite the constraints and be inspired by the challenge. Although guidelines, such as WCAG2.0, impose certain constraints, the possibilities are endless, providing the designers with a large range of possibilities to play with in terms of creating beautiful, exciting, engaging, and innovative designs for the web.

Currently, contrast checks are often performed after design (Alonso 2010), and the WCAG recommendations are technically intricate. Moreover, research show that several common colour picking interfaces are complex to use (van den Broek el al. 2004) and that visual feedback in the tool is more important than the actual colour model used (Douglas and Kirkpatrick 1999). Attempts have been made at generating palettes that help designers cater for colour blindness (Troiano et al. 2008). In a similar manner, it is argued for incorporating WCAG2.0 requirements into the design tools such that the requirements are satisfied throughout the design process. This can be achieved by introducing colour pickers that change according to the chosen colours and only allow the selection of colours that constitute colours that yield suficient contrast.

## References

Alonso, Fernando, José Luis Fuertes, Ángel Lucas González, and Loïc Martínez. 2010. ‘On the testability of WCAG 2.0 for beginners.’ In Proceedings of the 2010 international cross disciplinary conference on web accessibility. New York: ACM.

Bressan, Paola, Ennio Mingolla, Lothar Spillmann, and Takeo Watanabe. 1997. ‘Neon color spreading: a review.’ Perception 26 (11): 1353–1366.

van Den Broek, Egon L., Peter. M. F. Kisters, and Louis G. Vuurpijl. 2004. ‘Design guidelines for a content-based image retrieval color-selection interface.’ In Proceedings of the conference on Dutch directions in HCI (Dutch HCI ’04), 14–18. New York: ACM.

Douglas, Sarah. A., and Arthur E. Kirkpatrick. 1999. ‘Model and representation: the efect of visual feedback on human performance in a color picker interface.’ ACM Transactions on Graphics 18 (2): 96–127.

Foley, James D., Andries van Dam, Steven K. Feiner, and John. F. Hughes. 1995. Computer graphics: principles and practice: in C. 2nd edn. Reading, MA: Addison-Wesley.

Gonzalez, Berto, and Celine Latulipe. 2011. ‘BiCEP: bimanual color exploration plugin.’ In CHI ’11 extended abstracts on human factors in computing systems (CHI EA ’11), 1483–1488. New York: ACM.

IEC/4WD 61966–2-1. 1998. ‘Colour measurement and management in multimedia systems and equipment: part 2–1: default RGB Colour Space – sRGB.’ International Electrotechnical Commission.

ISO-9241–3. 1992. ‘Ergonomic requirements for ofice work with visual display terminals (VDTs): part 3: visual display requirements.’ International Organization for Standardization.

Hood, Donald C., and Marcia A. Finkelstein. 1986.

‘Sensitivity to light.’ In Handbook of perception and human performance, vol. I: sensory processes and perception, edited by Kenneth R. Bof, Lloyd Kaufman, and James P. Thomas, 5–66. New York: John Wiley.

Knoblauch, Kenneth, Aries Arditi, and Janet Szlyk. 1991. ‘Efects on chromatic and luminance contrast on reading.’ Journal of the Optical Society of America A, 8 (2): 428–439.

Majumder, Aditi, and Sandy Irani. 2007. ‘Perceptionbased contrast enhancement of images.’ ACM Transactions on Applied Perception 4 (3): article 17.

Norman, Donald. 1998. The design of everyday things. New York: Basic Books.

Sandnes, Frode Eika. 2010. ‘Where was that photo taken? Deriving geographical information from image collections based on temporal exposure attributes.’ Multimedia Systems 16 (4): 309–318.

Spencer, Donna. 2011. Information architecture. [e-book] Five Simple Steps.

Stokes, Michael, Matthew Anderson, Srinivasan Chandrasekar, and Ricardo Motta. 1996. ‘A standard default color space for the internet: sRGB.’ <http://www.w3.org/Graphics/Color/ sRGB>.

Troiano, Luigi, Cosimo Birtolo, and Maria Miranda. 2008. ‘Adapting palettes to color vision deficiencies by genetic algorithm.’ In Proceedings of the 10th annual conference on genetic and evolutionary computation (GECCO ’08), edited by Maarten Keijzer, 1065–1072. New York: ACM.

Wood, Joanne M. 2002. ‘Aging, driving and vision. Clinical and Experimental Optometry 85 (4): 214–220.

World Wide Web Consortium (W3C). 2008. ‘Web Content Accessibility Guidelines (WCAG) 2.0.’ Last modified 11 December 2008. <http://www. w3.org/TR/WCAG20/>.

![](images/ba98733f1ee1d7758ae3924f0088ba22a0eef3991c2ec1ef948a9850e5911760.jpg)

## Contrast set labelling26

## Theoretical essentials and suggestions for good practice

## Ian Watson

This chapter explores the graphical tools that information designers use to distinguish between the members of sets. Numbers may label the floors of a building, the hours of the day, or the pages of a book. Designers may use words to distinguish the diferent bus stops in a town, letters for the diferent sectors of a train platform, colours for the diferent keys to a building or ofice, and symbols for diferent types of restrooms. (There are other, less commonly used tools, too.) In general, designers use sets of contrasting graphic forms to label sets of contrasting ‘things’ in the real world. Those sets of things often have a built-in topology: the hours of the day form a metaphorical circle, the pages of a book a line, and the gates at an airport may be arranged in a branching pattern. That topology typically makes some labelling tools more appropriate than others. Information designers always need to choose labels that they are sure users will understand. This means that they are partly slaves to convention, but there is also room for a good amount of creativity.

Imagine that you woke up one day and found that all the numbers had disappeared from the houses in your town, the cars parked on the streets, and the pages of all the books you own. While social life would not grind to a halt, its gears would turn more slowly. To help someone find a house, or identify a car, or flip to a particular page in a book, you would need to give them a description rather than an identifier: the red house with the funny-looking roof at the end of the street, the dark green minivan parked on the street that runs by the river, or the page that’s sort of in the middle of the book (a little after the picture of the aardvark).

It’s not that labelling pages, cars, and houses is essential. It isn’t. There are books without page numbers and towns without house numbers, and although automobiles were produced commercially in the 1890s, it was only in 1903 that Britain, for example, started requiring them to carry licence plates (A brief history of registration 2006). But what labels do is to make certain operations on these classes of things more easy. In particular, they help us coordinate the way that diferent people refer to the same thing.

Unlike the words in a language, labels for things are most often consciously created. Their creators, though they may or may not think of themselves as designers, are indeed designing information – and they have the opportunity to reflect on how that might best be done. The goal of this chapter is to review the most common tools that are used to label sets of things, and to show which tools are most appropriate in diferent contexts and circumstances.

When we apply labels, we typically apply them to the members of sets. These sets are made up of items which contrast with each other, and thus we call them contrast sets. The American linguistic anthropologists Harold Conklin (1962) and Charles Frake (1962) were the first to use this term in print. You can recognize a contrast set because it fits the formula ‘X and other Ys’: Hungary and other European countries, Thomas Jeferson and other former presidents of the United States, tuna-and-pickle and other sandwiches on the cafe’s menu. The X is the name of an individual item and the Y is the name of the entire class.

## Labelling tools

Names are a handy and descriptive way of labelling the members of a contrast set. Designers commonly use them to label streets and transport stops, as well as rooms within a  building, groupings within a  school or kindergarten, or the days of the week and the months of the year. Yet their varying length can make them dificult to display, and interpreting them depends on knowledge of the language they are in. As well, they frequently lack any obvious topology: except insofar as it can be put in alphabetical order, a collection of names does not naturally suggest that it might be arranged along a line, circle, hierarchy, or any other kind of shape. When names are used, for example, to label the classrooms in several diferent university buildings, as on one campus the author is familiar with, the name of the room provides no clue to the building it is in or to the names of other nearby rooms.

Numbers are a popular and functional labelling tool that are widely used to label things as diverse as farm animals, the residents of a country, the terminals at an airport, the hours of the day, the hangers in a coat-check room, or the user-facing web pages in a  content management system. Numbers, unlike names, are politically fairly neutral, their length can be standardized, and they have an obvious topology. The most that can be said against labelling by number is perhaps that it is a bit dull.

The letters of the alphabet (whether the Roman alphabet or any other) have some of the same advantages and disadvantages as numbers, yet are more restricted in their range of usability. When used singly, their familiarity and clear linear topology makes them well suited for things like the diferent sectors of a train platform or the notes in the musical octave. But single letters are only appropriate labels for small sets of up to a couple dozen items or so. Identifiers made up of multiple letters can label much larger sets, but we are more used to identifiers made up of multiple numbers than multiple letters. Also, stating a letter-based identifier orally in a  dificult acoustic environment (like over the phone) risks confusing similar-sounding pairs such as S and F. Letters are also less neutral than numbers; combinations of letters sometimes spell out inconvenient things. In some environments it is common to design identifiers which combine both letters and numbers. Letter-number combinations work fine if a label needs to be primarily machine-interpretable (as with computer session IDs) but are more problematic for labels (such as airline ticket reservation numbers) which are also subject to human use; in these cases care should taken to avoid confusion between 0 and O and 1 and I.

Colour is a  popular and useful way of labelling contrast sets, but the number of distinctions available is small and nonstandardized. For example, it is a matter of choice for the designer whether to use just blue, or distinct shades (light blue and dark blue) as contrasting hues. As well, a  surprisingly large percentage of males have variant colour vision and thus dificulty distinguishing colours such as red and green (Kaiser and Boynton 1996, ch. 10). The author has heard the designer Paul Mijksenaar suggest that ‘colour supporting’ for contrast sets distinguished with other labels is sometimes more successful than ‘colour-coding’ where the colour identity must be remembered. For example, in Mijksenaar’s own design, the ten stops on the Airtrain at JFK Airport in New York are primarily distinguished by having diferent names. System maps and signage also colour the stops diferently. The colours highlight the contrast between set members, but knowing the colour is not a prerequisite for recognizing the stop. In fact, the same colour is sometimes used for more than one stop.

Using icons, pictures, and patterns (usually visual or auditory) as labelling tools can be cute, but it is practical only in certain circumstances. One major problem is the lack of conventionalized sets of images or patterns. Whereas users can be relied on to know what graphic forms do and do not count as numbers or letters (or even common colours), users typically have no idea what counts as a member of a set of images or patterns, and may thus have a harder time remembering them or perceiving them on the fly. The author has seen a number of inefective uses of icons in information design: for example, using animal and nature icons to label the diferent levels of the underground Sydney Casino parking garage in Australia (some of the animals were unfamiliar and the set did not clearly replicate the linear topology of the garage), and using smiley faces with a smile, frown, or straight mouth to represent three diferent levels of typical success in cooperation between businesses in the five Nordic countries (the diferences in mouth shape were too minor to be easily visible). However, in environments where users are heavily socialized into the set, icons can be efective. Consider, for example, that the letters of the Roman alphabet and the elements of other writing systems are, at least originally, pictorial ways of labelling sounds with contrasting graphic forms. Or think of the black and red circular icons used to represent product performance levels by the American magazine Consumer Reports. They are opaque to uninitiated users but arguably function well for the many people who read the magazine every month.

## 420 / Ian Watson

In addition, graphic devices such as variations in font weight can be an efective way of communicating contrast within small sets. For example, some airports with bilingual signs use the same font for both languages, but distinguish between them by using difering weights, sizes, or styles. Users master this mapping quickly, and marking languages with a visual distinction probably helps speed sign comprehension and reduce confusion.

Contrast sets are often embedded within each other in hierarchical structures which we can call taxonomies. In such cases two or more ‘levels of labels may be used to refer to the ‘terminal nodes’ of the taxonomy. For example, in a factory, three diferent buildings might be labelled A, B, and C, and the rooms within them might be labelled with numbers. Thus there might be a room 2 in both buildings A and B, whose full labels would be A2 and B2. To make things even more complicated, the room numbers might include the floor number (say, A202 and A302), creating a threelevel system. Taxonomic labels can and often do combine diferent types of labelling tools in the same identifier.

In sum, key issues to consider when choosing tools for labelling a set include:

• the structure, topology, and size of the underlying contrast set;

• how easy it will be to perceive the labels (and the diferences between them) in the environment where they are displayed;

• the degree of contact, training, or habituation that users have with both the contrast set and the labels for it.

## Iconicity

Iconic labels are those where the relations between the members of the label set reflect the relations between the members of the contrast set that they label. Typically, the topology of the label set replicates the topology of the contrast set. In simpler terms, the label set says something about the underlying contrast set. For example, on a typical street, the further up you walk, the higher the house numbers will be. The topology or configuration of the house numbers replicates the topology of the street itself. In Manhattan (and many other American cities), where not just houses but also streets are numbered, there is also an iconic relationship between the street’s number and its geographical position.

Set topologies can be of several forms. There are linear topologies, like streets; circular topologies, like the hours of the day or months of the year; and branching, taxonomy-like topologies, like the gates at many larger airports.

The value of using an iconic labelling style is that users can grasp the system as a generative principle rather than as a collection of individual links. This allows users to predict roughly what a given label refers to or how a given contrast set member might be labelled. For example, if you are standing between two airport departure gates and one is called $\Gamma _ { } { 4 6 } ,$ it is unlikely that the other will be called B2, but it would not be surprising if it were called $\mathrm { C } 4 7$ or $\mathrm { C } 4 8$ . If you are standing in front of house number 700 near the end of a long street, it is likely that house number 2 will be at the other end. These inferences are possible when users understand the way the label topology maps on to the set topology.

Iconicity is a standard information design strategy. In contrast, linguists have long recognized that the words in the lexicon are largely arbitrary, so that the diference between the words dog and cat reflects nothing about the actual diference between dogs and cats. There is, though, a certain amount of iconicity in regular language (linguists have debated its extent for centuries). In information design, iconicity is the rule rather than the exception, partly because of the deliberateness with which its semantic systems are created and their simplicity when compared to language. After all, designers often label particular, concrete instances of things, such as a specific train platform, while words can label actions, qualities, or entire classes of objects.

Related to iconicity is what we could call ‘coordinated labelling’, where a single label set maps on to the same features of multiple contrast sets. For example, in the Faroe Islands in the 1980s, a system was developed in which postal codes, telephone numbers, road numbers, bus route numbers, and ferry route numbers in each part of the islands all began with the same one or two numbers. Formally speaking, the same set of labels was mapped to the islands’ geography in multiple ways. Although the system later broke down, while it lasted this degree of coordination was quite impressive to those who appreciate such things. An example where such coordination is lacking is that European countries have varying rules about which telephone numbers are reserved for mobile phones and which for land lines. Each time they cross a national border, telephone users must relearn which numbers refer to mobile phones (and thus cost more to call). This was surely a missed design opportunity for users, though perhaps a source of revenue for telephone companies.

## Other issues

## Visual identities for entire sets

It is often important to create a design identity (usually a visual one) for entire contrast sets. If you are labelling the platforms at a train station, it is not just important that users see the number 5 when they arrive at platform 5; it is important that they recognize this particular number 5 as a platform number (rather than as marking sector 5 within that platform, giving instructions to train drivers to limit their speed to 5 kilometres an hour, or any of the other things that the number 5 could be used to say). Presenting all the members of a particular contrast set to users in a consistent way

## 422 / Ian Watson

helps users learn what a given labelling device is being used to represent, and it is even more helpful if this is part of a more widely standardized convention. For example, a traveller changing trains at a station for the first time will have an easier time finding their platform if they can rely on their familiarity with the look of platform-number signs at other stations in the same system (such signs might, say, all be square and blue with white numbers in the Helvetica font). In some cases, it can be helpful to display a word that describes the entire set (for example, writing ‘Platform $\boldsymbol { 5 } ^ { \prime }$ or ‘Gate $4 6 ^ { \circ }$ on a sign rather than just $^ { \ast } { } _ { 5 } \cdot { }$ or ‘46’, typically setting the word in a smaller type size than the number). For further reading see Watson (2005, section 3.3).

## Exemplifiers or placeholder labels

It also often makes sense to specify a particular label that will serve as an example or ‘placeholder’ when referring to the idea of ‘any member of the contrast set in question.’ Strings like ‘123456’ are commonly used for numerical labels. In the realm of personal names, ‘John Doe’ is a common placeholder label in English, while Germans often use ‘Erika Mustermann’, and Chinese ‘Zhang San’ (Zhang Three). Such labels are sometimes called metasyntactic signifiers, as they signify the idea of individual members of a contrast set rather than any actual member. By specifying a placeholder label, one hopes to ensure that it will become conventionalized and commonly enough used that one can rely on users not interpreting it as referring to something real. For further reading, see Watson (2005, section 3.7).

## Using multiple labels for accessibility

Design that aims at being as inclusive or multifunctional as possible often labels the same contrast set in several diferent ways at the same time. For example, Braille playing cards list the number and suit of each card both visually and tactically so that both sighted and unsighted players can use them. Product labels at IKEA housewares stores typically include a name (used especially by customers), a stock number (for employees), a barcoded version of the stock number (for machine readability), and an actual description of the product.

## Nametags and wayfinding

Many labels are displayed on or near the contrast set members that they refer to. At the very least, they then serve as a means of confirming that one is indeed looking at that member of a contrast set (like a nametag worn at a conference). Consider the diferent roles of a house number as displayed on the house itself, and as listed in the owner’s entry in the telephone book. Nametag-style labels with an iconic relationship to the underlying contrast set serve as wayfinding aids, as users who understand the iconic principle can use labels to grasp their ‘location’ within the set and predict the location of other members. Such labels ought to be designed in a way which facilitates visibility during navigation. This explains why libraries make an efort to place the call numbers on book spines at the same height, as well as the frustration that comes from searching unsuccessfully for a missing house number on a building. For further reading, see Watson (2005, section 3.4).

## Social aspects of introducing or changing labels

The process of introducing labels for the first time (for a  contrast set that was previously unlabelled) or changing an established set of labels can meet with a considerable amount of resistance from users. After all, labels mediate our cognitive relationship with important features of our environment, and we even integrate them into our feelings of identity. For example, the French government faced considerable opposition when it decided to revamp French automobile licence plates and eliminate the iconic relationship between the plate number and the département of registration (Lichfield 2008), while novelist Salvatore Satta (1987, 89) gives a  convincing fictional description of resentment at the introduction of street names in Nuoro, Sardinia. An awareness of the sensitive feelings surrounding labels can smooth the process of designing new ones. For further reading on this issue see Watson (2005, section 6.5).

## References

A brief history of registration. 2006. Swansea, Wales: Driver and Vehicle Licensing Agency.

Conklin, Harold C. 1962. ‘Lexicographical treatment of folk taxonomies.’ In Problems in lexicography: report (conference publication), edited by Fred W. Householder and Sol Saporta, 119–141. Bloomington: Indiana University [variant title: International Journal of American Linguistics 28

Frake, Charles O. 1962. ‘The ethnographic study

of cognitive systems.’ In Anthropology and human behavior, edited by T. Gladwin and W. C. Sturtevant, 72–85, 91–93. Washington, DC: Anthropological Society of Washington.

Kaiser, Peter K., and Robert M. Boynton. 1996. Human color vision. 2nd edn. Washington, DC: Optical Society of America.

Lichfield, John. 2008. ‘Number-plate revolution sparks an uprising across France.’ The Independent, 16 January.

Satta, Salvatore. 1987. The day of judgment. London: Harvill.

Watson, Ian. 2005. ‘Cognitive design: creating the sets of categories and labels that structure our shared experience.’ PhD dissertation, Department of Sociology, Rutgers University. <http://hdl. handle.net/1946/6366>.

![](images/18ee76ec2977b7beffa8df2ec796ca670c0e628d5e7d665f06a81552a2b54a6f.jpg)

## Gestalt principles27

## Opportunities for designers

Rune Pettersson

The essential thesis in gestalt psychology is that in perception the whole is other than the sum of its parts. Our perception cannot be understood simply by analysing a scene into its elements. What we interpret depends on the relations of these elements to one another. The brain works fast and in a holistic way. We immediately ‘see the big picture’. This chapter presents the gestalt principles that provide the most opportunities for information designers.

## Atention

There are always far more stimuli in our environment that we can see, hear, smell, taste, or feel through touch, than we can notice consciously. We select what we want to hear or see, i.e. pay attention to, and we ignore the rest. Most stimuli remain unheard, unseen, and thus unknown to us. For Stern and Robinson (1994), selection of sensory data is the first step of perception. However, selection of sensory data may also be seen as a part of attention. When we attend to something, we select that information for further processing.

## Perception

While mere sensation is thought to be a lower-level function, perception is thought to be a  function of higher-order areas of the brain. It is the awareness of complex characteristics of stimuli. Sensory organs jointly constitute a perceptual system that, in a natural environment, collects an enormous amount of superfluous data about our environment. In a natural environment, the sensory system normally supplies us with exhaustive, unambiguous data about events occurring there. We are often unaware of the sensory channels that supply us with data. We are merely aware of the external events.

## Perception processes

The concept ‘perception’ is a collective designation for all the diferent processes in which an organism obtains data about the outside world. Perception is the organizing and analysing of the data that we actually pay attention to.

Perception of two- or three-dimensional representations entails fast, holistic, parallel, and simultaneous processing (Sperry 1982). We do not

## 426/Rune Petersson

‘see’ patches of colours and shades of brightness. We look for and recognize patterns, and combine them into meaningful structures. We perceive ‘things’, like apes, books, cats, dogs, etchings, and flowers, while we rely on our experiences, thoughts, and values to interpret, understand, and create meaning from what we see, hear, taste, smell, and touch.

## Perception is subjective

Perception is certainly not an absolute and objective process. It is subjective, and it varies as a result of a number of factors. Individuals difer in how they perceive any given stimulus. Age and gender, cultural, economic, historical, political, religious, and social factors may be important. We interpret new impressions against the background of our previous experience and knowledge. Our experiences change over time, and a stimulus may easily be perceived diferently at diferent times, and internalized knowledge will influence interpretation and understanding.

The perception system strives to obtain clarity. When the system arrives at clarity, then clarity serves as reinforcement, a  reward. An important principle for the designer is to improve the clarity of any message (Winn 1993). Thus the main goal in information design and in instruction design should always be clarity of communication (Pettersson 2015a). We should limit the content to what the intended audience needs, and emphasize what is most important.

## Perceptual constancy

In the real world objects may have similar colours to the ones in the background, and the objects are often partly hidden behind other variously sized objects. The outline of an object is often indistinct. In order to handle such complex scenes our visual system combines visual elements even when they are distorted. We are quick to make the best possible interpretation of the available fragments of data. There is a large degree of perceptual constancy. We can view an object, a picture, a text, or a symbol from various distances and from various angles and still get the same understanding of the content (Pettersson 2015e). You only need to look at a single car passing by to realize the importance of perceptual constancy.

## Visual perception

Our visual system is remarkable. We are capable of perceiving objects in bright light from the sun, and in pale light from the moon. We can also follow rapidly moving objects, like a car passing by. Visual perception is the product of complex interactions among various stimuli. A  number of psychologists view our attempts to establish order as an innate faculty carried out in accordance with certain laws, or principles. These laws, or principles, can be utilized or relied on for information design purposes.

## Gestalt psychology

For verbal language, syntax is the rules for combining words and phrases into well-formed sentences. In non-verbal visual languages, syntax depends upon the spatial arrangements of the visual elements (Horn 1998, 75). Our ideas about good spatial arrangements depend on how our perceptual system works.

Early in the 20th century the three psychologists Max Wertheimer (1880–1943), Kurt Kofka (1886–1941), and Wolfgang Köhler (1887–1967) collaborated on the founding of a  new holistic attitude towards psychology called gestalt psychology, or gestalt theory. Wertheimer started his research on the gestalt principles of perceptual grouping already in 1910, but he did not formally publish anything about his work before 1923 (King and Wertheimer 2005).

The German word gestalt means ‘whole form’, or ‘configuration’. Gestalt psychologists believe that conscious experience must be viewed as a ‘whole form’, and cannot be analysed into its parts. This ‘whole form’ can be an image, a map, a shape, or a thought. Feeling, hearing, and seeing, must be studied together in order to understand their relationships.

The essential thesis in gestalt psychology is that in perception the whole is dif erent from the sum of its parts (Palmer 1999). Because of the characteristics of our mental visual system, visual perception cannot be understood simply by analysing a scene into its elements. Instead, what we interpret depends on the relations of these elements to one another. The brain works fast and in a holistic way. We immediately ‘see the big picture’. Later we may return and attend to some of the separate parts. This explains why a picture may have something new to ofer even when we have viewed it many times.

Maps are good examples of the relationship between the ‘whole’ and the ‘parts’. In a city map the ‘whole’ is the layout of the city, and the ‘parts’ are all the symbols for blocks, buildings, and streets (Lohr 2010). An airport map shows the overall relational layout of the airport as well as the concourses, gates, shops, and terminals.

The observations on which the ‘gestalt theory’ is based, form a basic part of the graphic designer’s craft knowledge (Waller 1987). These principles might be seen as relatively inflexible perceptual rules with consequences for interpretation that act as a fundamental constraint for the graphic designer alongside conventional rules such as the left-to-right direction of the writing system in many countries. The gestalt principles are often referred to as gestalt laws. However, we should really only use the term gestalt principles, since these principles are considerably weaker than one would expect of scientific laws (Palmer 1999).

For recent historical and conceptual discussions on gestalt theory, see Wagemans (2015); for recent discussions on the role of gestalt theory in art, design, and graphic design, see Behrens (1998) and Moszkowicz (2011).

## Organization and perceptual groupings

The gestalt principles, or gestalt laws, were introduced by Wertheimer (1922, 1923), and were further developed by Köhler (1929, 1947), Kofka (1935), and Metzger (1936/2006). These gestalt principles help us organize the world around us in a legible way. They are basic for the syntax in visual languages. They describe and explain the organization of perceptual scenes. The proximity principle was the first principle that Wertheimer demonstrated. This was followed by the principles of similarity, common fate, continuity, closure, and Prägnanz or the principle of good form. There is no definitive list of gestalt principles (Todorović 2008).

Each gestalt principle is supposed to function, as long as all other things are constant (Palmer 1999). Sometimes two, or even several, principles apply to the same grouping of elements. When the principles agree, the efect is stronger. When the principles disagree, the efect is weaker, and one of them will take over. Schriver (1997, 326) noted that gestalt principles are important for document design. Gestalt principles can ‘help us guide the reader’s focus of attention, emphasize certain groupings, and organize sequences of the content’.

Information designers can use several of the gestalt principles as tools in order to make it easier for the intended audiences to interpret the messages in information materials as meaningful wholes, rather than as ambiguous configurations or random individual elements.

The figure and ground organization and the following seven gestalt principles provide most opportunities for designers:

1 similarity principle

2 contrast principle

3 continuity principle

4 proximity principle

5 grouping principle

6 common fate principle

7 closure principle

However, only principles 1–5 are discussed in this chapter.

There are also gestalt principles that are less useful as tools for designers. These principles are not discussed in this chapter: (8) area principle, (9) auditory principles, (10) common region principle, (11) connectedness principle, (12) convexity principle, (13) good form principle, (14) objective set principle, (15) past experience principle, (16) spatial concentration principle, (17) symmetry principle, and (18) synchrony principle.

## Figure/ground organization

Figure/ground perception is a fundamental aspect of field organization. It is however, not always referred to as a gestalt principle, but rather as ‘figure/ ground articulation’ or as ‘figure/ground organization’. The Danish psychologist and phenomenologist Edgar John Rubin (1886–1951) presented his work on figure/ground perception between 1915 and 1921 (Palmer 1999). This was before Max Wertheimer presented his gestalt laws.

Edgar Rubin is especially famous for his optical illusion called ‘the Rubin vase/face’. This illusion is perceived either as a white vase, or as the profiles of two black heads facing each other. The visual system has a strong preference to ascribe the contour to just one of its border regions and to perceive the other side as part of a surface extending behind it (Palmer 1999). The interpretation of the Rubin vase/face fluctuates between the two possibilities even though the image on your own retina remains constant. Rubin’s theories became influential within gestalt psychology, yet he did not want to be included in the group of early gestalt psychologists.

Figure/ground articulation is also known as the figure/ground principle, figure–ground articulation, figure/ground organization, figure and background principle, figure and ground principle, and as the theory of figure and ground. According to this principle we select some elements in a picture as the figure, the object of interest (Figure 1). The remaining parts constitute the ground on which the figure rests. This is one of the simplest perceptual organizations.

Figure 1   
In the illustration to the left we   
recognize a square as a ‘figure’   
against a dotted   
background. In   
the other two   
illustrations,   
the properties   
of ‘figure and   
ground’ cannot   
be sharply   
distinguished.   
However, the three squares are equal, and the distances between them are the same.

![](images/aeb81cc325c6851441b37c5542ec6e0f022dfd19c1f2fe4ec1f6ec8ef4facdc3.jpg)

![](images/8195278baaa2b3a5221ea5d3f56e4caffd596f1f9f7571f225efce5a8dcb339d.jpg)

![](images/2c755e4a3dc2c8fe4acda35adb30aefd31d3322c7ed20868a2875cae0b7cb018.jpg)

We perceive the figure as being in front of the ground, and the ground as being behind the figure. We might be tempted to view figure and ground as a relationship between just two levels (Schriver 1997, p. 307). However, what serves as the ground in one relationship can serve as the figure in another relationship. The figure/ground organization is afected and influenced by several factors, such as: contrast, convexity, meaningfulness, motion, orientation, parallelism, size, enclosure, and symmetry.

Sometimes it may be hard to distinguish between figure and ground, and some structures will be perceived as reversible. Reality and what we see at any given moment will always be separated and diferent. We will perceive diferent things at diferent occasions, both with respect to reality and with respect to pictures. In some cases figure/ground articulation has apparently been based on experience (Peterson and Skow-Grant 2003).

Miller (2007, 11) noted that the animal kingdom is filled with creatures whose colours and patterns help conceal and protect them from their enemies. This animal camouflage helps them to survive. The birth of modern military camouflage was a direct consequence of the invention of the aeroplane (Newark 2007). Aircraft were initially used in the First World War for aerial reconnaissance missions. Their task was to spot enemy artillery, troops, and vehicles. Their own artillery could then direct their fire directly at these targets. All sides formed ‘camouflage units’. Members of staf painted bold disruptive patterns on aircrafts, guns, and tanks. In France several prominent cubist artists were working as ‘camoufleurs’ at the front.

In animal camouflage as well as military camouflage, objects are perceptually subdivided. Their parts are grouped with parts of the surrounding environment. Gestalt principles make it possible for organisms and things that are in plain sight to become efectively invisible and therefore undetectable. In camouflage the intention is to make a figure as much like the background as possible. Information design is the opposite of camouflage.

The graphic designer or the information designer can use the figure and ground principle to facilitate efective perception. The content and message must stand out as clearly as possible from the ground.

For example, the most legible combinations of colours for text are black or dark brown on a  light background. Other combinations may attract more attention but are less legible and, thus, may require larger type. A text can be easy to read in any colour, provided the colour of the background is carefully selected. However, generally speaking, the best text colour is black, which causes good contrast to most background colours.

## Similarity principle

The similarity principle is also known as the law of similarity, and the theory of similarity. According to this principle we tend to perceive and group our impressions of things, all other things being equal, on the basis of the similarity of their properties. Events, objects, and units that look alike, resemble each other, and share similar characteristics and properties, belong together (Figure 2).

![](images/d9dfdc02d4c3725069ce0b04c5b3170529a17115aa17dfaacc12ef4cd01daf47.jpg)

These properties can be brightness, colour, darkness, orientation, pattern, shape, size, texture, or value. We use them to group elements into perceptual units, and the cognitive load on our short-term memory is automatically reduced. Elements that are diferent are not part of the group. One single black sheep in a flock of white sheep tends to be noticed.

The similarity principle is one of the most powerful organizing principles and one of the most useful in information design for facilitating perceptual organization of data. The graphic designer and the information designer can use the similarity principle to facilitate perception

Figure 2   
This illustration   
shows an example of ‘similarity of   
colour’. The four   
circles in each   
group have the   
same shape, and size, and they   
have the same   
distance from   
each other.

by emphasizing both diferences and similarities of diferent parts in a document.

For example, the reader should be able to recognize quickly diferent categories of textual elements within a document. There should be clear distinctions between textual elements such as abstract, captions, footnotes, running heads, headings, subheadings, lists, tables, body text, marginal notes, inline quotations, block quotations, and page numbers.

## Contrast principle

The contrast principle is also known as the contrast law. In nature, as well as in art and design, contrast is of major importance for our perception of a message. In accordance with the contrast law we tend to arrange impressions that form natural opposites in groups. Thereby the impressions are reinforcing one another.

Visual acuity, our ability to discriminate small objects, peaks at about age 22, and then a steady decline starts. This decline is not possible to correct with eyeglasses. At about age 40 the tissues of the eyes get stifer. This condition is called presbyopia or ‘old eyes’. It makes it harder for us to shift the distance of our focus. Thus it is harder to change between reading on a screen and reading on paper. Throughout our lives our lenses become less and less transparent. The result of this increasing opacity is that we require more contrast between a message and its background to see any fine details in images and to read text.

The information designer can use the contrast principle to aid perception. There can be no large without small, and no small without large. It is usually a good idea to include some familiar object, like a hand, a face, a whole person, a car, a house, a tree, or a scale for judging the size of any unfamiliar object.

Many diferent elements in a visual can cause emphasis. Arrows, change in size, circles or ovals around objects, colour against no colour, complexity, detail against no detail, directionality, implied motion, isolation, light against dark, line drawings in photos, line intersections, position or placement of elements, shaded areas, stars, tonal contrast, words, or any other unexpected change or variation out of context will create emphasis. Furthermore, emphasis on the core message is achieved by reducing the number of details in the picture to those that are really essential (Pettersson 2015c). Emphasis may be used to attract, direct, and to keep attention. The most important elements in information material may be emphasized to enhance attention and perception.

For example, we can use colour and colour contrast to enhance perception of a visual message (Dwyer 1985). We should, however, remember that many people sufer from colour blindness. Anomalies of colour vision is much more commonly observed among men than among women, with estimates ranging as high as 10% of the male population (Hartley 1987; Ware 2004) – while only 1% of the female population has anomalous

## Rune Petersson

colour vision. The failure to distinguish between red and green is most common. Both hues are perceived as grey. Unfortunately, red and green are often used as discriminating colours in symbols and in warning signs.

## Continuity principle

The continuity principle is also known as the contiguity principle, the law of continuity, law of good continuation, line of direction, principle of good continuation, and the theory of direction. This principle refers to continuation and simplicity.

When we see two lines crossing in the middle we usually perceive this pattern as two lines crossing (Figure 3).

![](images/fd68f86da3a9bf3378a2d8850fa1a34a506ff7f6fd5cb887b19fc7409e743a43.jpg)

However, it could be two (or even four) opposing angles that are joined together at their apexes. Lines that are moving in the same direction belong together. Events that have a simple and natural relationship to one another also give the impression of being continuous and unbroken. Straight or curved lines, like bold lines, tend to lead the eye along, and even beyond, the line. An arrow or a finger pointed at something leads your eye to it. The information designer can use the continuity principle to aid perception, and to indicate relatedness between elements in a design.

Figure 3 We perceive the left-hand pattern as two lines crossing in the middle rather than as two (or even four) opposing angles joined together at their apexes (right). This is also referred to as ‘line of direction’.

For example, we understand the gradual changes in diagrams, and the rise and fall of the bars in a bar graph.

## Proximity principle

The proximity principle is also known as the law of nearness, and law of proximity. According to this principle we see individual elements but we will perceptually group events, objects, and units on the basis of their nearness and proximity to one another in space or in time. Elements that are close together are perceptually grouped together, all other things being equal (Figure 4).

![](images/ed30af42d00de6b60e980e36af9c7dcc02414ba3eb3df3f9a2ac19289117268d.jpg)

These elements ‘belong together’ and they are processed together. In this way the need to process large numbers of small stimuli is reduced. As a result, perception is faster. As a consequence, elements that are far apart are perceived as separate objects. Spatial proximity is one of the most powerful organizing principles and one of the most useful in information design for facilitating perceptual organization of data.

Figure 4   
We perceive four groups of squares, each with two   
squares. In each   
group the squares have the same   
colour, shape,   
and size, and they have the same   
distance from   
each other.

For example, the information designer can rely on the proximity principle to facilitate perception by carefully grouping headings with their associated body text, and illustrations with their captions. The amount of white space distributed around headings should correspond to each heading’s relative position in the hierarchy of headings and subheadings. A major heading requires more space than a minor heading. The amount of space and the positioning of a heading in that space can be used to emphasize the document’s hierarchic structure ( Jonassen 1982). The distance between a heading and the text below (to which it belongs) should thus always be smaller than the distance between the heading and the body text above (Pettersson 2015d).

## Grouping principle

![](images/7f2713e0841e8d4e07ad7ae03fc5cd155871462290b19806bdae69dd0f80262b.jpg)

The principle of grouping is also known as the law of grouping. Most figures are defined by a boundary. However, the presence of a boundary is not required for the perception of form or shape. When small elements are arranged in groups, we tend to perceive them as larger forms (Figure 5). The principles of common region, connectedness, proximity, similarity, and symmetry all work together to evoke grouping.

## Figure 5

Groups of smaller elements may be perceived as larger figures. Here   
small black dots   
form a square.   
All the dots are of the same colour,   
shape and size,   
and approximately at the same   
distance from   
each other.

Visual grouping into meaningful semantic clusters enables readers to get a sense of the overall structure (Tullis 1997), and it can help the readers to reduce their cognitive loads (Niemelä and Saarinen 2000). Readers will better remember the content and make fewer errors.

For example, the information designer can use the principle of grouping (as well as the above mentioned proximity principle), to facilitate perception and understanding by carefully grouping headings with their associated body text, and illustrations with their captions.

## Summary

Our perception cannot be understood simply by analysing a scene into its elements. What we interpret from a message depends on the relations of diferent elements to one another. Our brains work fast and in holistic ways. We will immediately ‘see the big picture’. In attention and perception the whole is other than the sum of its parts. The information designer can make good use of the gestalt principles in order to improve the possibilities for the intended audience to efectively understand the intended message.

## References

Behrens, Roy R. 1998. ‘Art, design and gestalt theory.’ Leonardo 31 (4): 299–303.

Dwyer, Francis M. 1985. ‘Visual literacy’s first dimension: cognitive information acquisition. Journal of Visual Verbal Languaging 5 (1): 7–16.

Hartley, James. 1987. ‘Designing electronic text: the role of print-based research.’ Educational Communications and Technology Journal 35 (1): 3–17.

Horn, Robert E. 1998. Visual language: global

communication for the 21st century. Bainbridge Island, WA: MacroVU.

Jonassen, David H., ed. 1982. The technology of text: principles for structuring, designing, and displaying text, vol. 1. Englewood Clifs, NJ: Educational Technology Publications.

King, D. Brett, and Michael Wertheimer. 2005. Max Wertheimer and gestalt theory. New Brunswick and London: Transaction Publishers.

Kofka, Kurt. 1935. Principles of gestalt psychology. New York: Harcourt, Brace.

Köhler, Wolfgang. 1929. Gestalt psychology. New York: Horace Liveright.

Köhler, Wolfgang. 1947. Gestalt psychology: an introduction to new concepts in modern psychology. New York: Liveright.

Lohr, Linda L. 2010. Creating graphics for learning and performance: lessons in visual literacy. 2nd edn. Upper Saddle River, NJ: Pearson.

Miller, Jonathan. 2007. ‘Visual subterfuge in the natural world.’ Introduction in Camouflage, by Tim Newark. London: Thames & Hudson, in association with Imperial War Museum.

Moszkowicz, Julia. 2011. ‘Gestalt and graphic design: an exploration of the humanistic and therapeutic efects of visual organization.’ Design Issues 27 (4): 56–67.

Newark, Tim. 2007. Camouflage. London: Thames & Hudson, in association with Imperial War Museum.

Niemelä, Marketta, and Jukka Saarinen. 2000. ‘Visual search for grouped versus ungrouped icons in a computer interface.’ Human Factors 42 (4): 630–635.

Palmer, Stephen E. 1999. Vision science: photons to phenomenology. Cambridge, MA: MIT Press.

Peterson, Mary A., and Emily Skow-Grant. 2003. ‘Memory and learning in figure–ground perception.’ In The psychology of learning and motivation (Advances in research and theory: cognitive vision, volume 42), edited by David E. Irwin and Brian H. Ross, 1–34. San Diego, CA: Academic Press.

Pettersson, Rune. 2015a. Information design 1: message design. Revised edition. Tullinge: Institute for Infology. e-book <http://www.iiid.net/ rune-pettersson-information-design-1-messagedesign/>.

Pettersson, Rune. 2015b. Information design 2: text design. Revised edition. Tullinge: Institute for Infology. e-book <http://www.iiid.net/runepettersson-information-design-2-text-design/>.

Pettersson, Rune. 2015c. Information design 3: image design. Revised edition. Tullinge: Institute for Infology. e-book <http://www.iiid.net/

rune-pettersson-information-design-3-imagedesign/>.

Pettersson, Rune. 2015d. Information design 4: graphic design. Revised edition. Tullinge: Institute for Infology. e-book <http://www.iiid.net/ rune-pettersson-information-design-4-graphicdesign/>.

Pettersson, Rune. 2015e. Information design 5: cognition. Revised edition. Tullinge: Institute for Infology. e-book <http://www.iiid.net/runepettersson-information-design-5-cognition/>.

Schriver, Karen A. 1997. Dynamics in document design: creating texts for readers. New York: John Wiley.

Sperry, Roger W. 1982. ‘Some efects of disconnecting the cerebral hemispheres.’ Science 217 (4566): 1223–1226.

Stern, Richard C., and Rhonda S. Robinson. 1994. ‘Perception and its role in communication and learning.’ In Visual literacy: a spectrum of visual learning, edited by David M. Moore and Francis M. Dwyer, 31–52. Englewood Clifs, NJ: Educational Technology Publications.

Todorović, Dejan. 2008. ‘Gestalt principles. Scholarpedia 3 (12): 5345. <http://www. scholarpedia.org/article/Gestalt\_principles>.

Tullis, Thomas S. 1997. ‘Screen design.’ In Handbook of human–computer interaction, 2nd edn, edited by Martin Helander, Thomas K. Landauer, and Prasad V. Prabhu, 503–531. New York: Elsevier Science.

Wagemans, Johan, ed. 2015. The Oxford handbook of perceptual organization. Oxford: Oxford University Press.

Waller, Robert. 1987. ‘The typographic contribution to language: towards a model of typographic genres and their underlying structures.’ PhD thesis, Department of Typography & Graphic Communication, University of Reading. <http:// www.robwaller.org/RobWaller\_thesis87.pdf>.

Ware, Colin. 2004. Information visualization: perception for design. 2nd edn. Amsterdam: Morgan Kaufmann.

Wertheimer, Max. 1922. ‘Untersuchungen zur Lehre von der Gestalt: I. Prinzipielle Bemerkungen.’ Psychologische Forschung 1: 47–58.

Wertheimer, Max. 1923. ‘Untersuchungen zur Lehre von der Gestalt: II.’ Psychologische Forschung 4: 301–350.

Winn, William D. 1993. ‘Perception principles.’ In Instructional message design: principles from the behavioral and cognitive sciences, 2nd edn, edited by Malcolm L. Fleming and W. Howard Levie, 55–126. Englewood Clifs, NJ: Educational Technology Publications.