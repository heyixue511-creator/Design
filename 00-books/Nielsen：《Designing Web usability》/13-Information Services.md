# Information Services

## ...your source for land, mortage and title search information.

At Datatrace we service counties in the surrounding areas of our offices located in Tampa, Florida; Ft. Lauderdale, Florida; Mt. Clemens, Michigan; and Cleveland, Ohio.

Our headquarters are based in Richmond, Virginia.

These are the services we offer here at Datatrace.

What Datatrace is about.

Automated Title Search System

Ownership Encumbrance Reports

Asset Encumbrance Reports

1099S Services

Check out career opportunities with Datatrace.

## E-mail Datatrace Information Services. ="

Copyright 1996-97 Datatrace Information Services Company Inc.

## Printing

Most of the users I have interviewed say that they print out a good deal of information from the Web. In principle, the Web ought to have made the need to print out information for archival purposes obsolete, but bitter experience has taught users that they cannot rely on retrieving information if they need it at a later date. Sometimes, the remote server will be down, sometimes the webmaster has removed the page, and sometimes the users are simply not able to find the page a second time. Printouts are also preferable if the user has a paper-based filing system with folders or binders for all the information relating to a certain project.

Because it is so unpleasant and slow to read large amounts of text from computer screens, users also often print out long documents to read offline. Additionally, users sometimes print out web pages to give to others to read, perhaps as handouts in meetings or seminars. Better computer screens may eventually reduce the need for printouts, but for the next several years, we must expect many users to continue to want to print out web-based information.

The implication for web design is to provide printable versions of any long documents. Web browsers are slowly improving their print functionality, but one cannot rely on browser companies to produce well-crafted printouts because their main interest is online information. For example, most browsers use the same typeface and font size for online viewing and printing, even though it is known to all typography specialists that the two media require different typefaces. Also, the layout of a document will typically be different: Single-column layouts make for easier scrolling in online viewing whereas two-column layouts are preferred for letter-sized paper.

My recommendation is to generate two versions of all long web documents. One version should be optimized for online viewing by being chunked appropriately into many files using plenty of hypertext links and a screenoriented style sheet. Another version should keep the entire document in one file with a layout that is optimized for printing.

You must limit any PostScript pages to a printable area that will fit on both A4 sheets and 8.5"×11" sheets.

![](images/62336d58a964be60de4f9279b4ecd3aaf19d7dd4c2f0fee6b8049cd04b0ab924.jpg)

Currently, users will need to download the printable version manually, but hopefully browsers will soon start to implement the recommended standard for specifying alternative document versions. One such alternative is indeed the printable version, and it will not hurt to include the appropriate HTML in the HEAD part of documents with printable versions. The code reads as follows:

<LINK REL="alternate" MEDIA="print" HREF="mydoc.ps" TYPE="application/postscript">

Older browsers will simply ignore any specifications of printable alternatives, but future browsers will recognize this code as indicating that any print command should be performed on the alternate file and not on the displayed version of the page.

The printable file should probably be in formats like PostScript or PDF. It is extremely important to denote any such files as being for printouts only, and always be sure to supplement them with links to the same content in HTML for online viewing by users who want to browse or search a small part of the document.

PostScript files should never be read online. PostScript viewers are fine for checking the nature of a document in order to determine whether it's worth printing, but users should not be tricked into the painful experience of actually spending an extended period of time with online PostScript. PostScript and PDF are page description languages that specify exactly how the text should look when printed. Such descriptions do not have the flexibility or cross-platform capabilities necessary for online viewing and interaction. For example, a two-column layout in PDF will look perfect when printed but will be almost impossible to read on a screen that is smaller than the sheet of paper for which the page was intended.

I repeat: Do not torment your users by making important documents available in PostScript form only. Always link to an HTML version for online reading.

Any file that is intended for printing must be able to accommodate the two most common international page formats: A4 and $8 . 5 " \times 1 1 "$ (U.S. Letter). To do so, the width of the page must fit on an A4 sheet, and the height of the page must fit on an $8 . 5 " \times 1 1 "$ sheet because A4 is the narrowest format and $8 . 5 " \times 1 1 "$ is the shortest format. It is recommended to leave a margin of at least half an inch (13 mm) for all four sides of the page to ensure that it will print on all printers and to facilitate photocopying. With half-inch margins, the printable area is $7 \%$ (18.5 cm) wide by $1 0 "$ (25.4 cm) tall; with one-inch margins (preferred), the printable area would be $6 \%$ (15.9 cm) by $9 "$ (22.9 cm).

## Conclusion

Simplicity should be the goal of page design. Users are rarely on a site to enjoy the design; instead, they prefer to focus on the content (which I will discuss in the next chapter). It is also important to ensure that page designs work across a wide range of platforms and that they can be accessed by people who use old technology.

I recommend making sure that all pages work on twoyear-old browsers and two-year-old versions of all plug-ins and other software. Also, make sure that the page design works on small monitors and has acceptable response times when using analog modems.

Some people may say that these limitations impose undue hardship on designers and that only 10 percent of the users actually employ old software and low-end hardware. This may be true, but it is usually a bad business decision to turn away 10 percent of your customer base at the door.

## 100 Writing for the Web

• The Value of an Editor

Keep Your Texts Short

• Web Attitude

• Copy Editing

• Scannability

• Why Users Scan

• Plain Language

• Page Chunking

• Limit Use of Within-Page Links

123 Page Titles

124 Writing Headlines

125 Legibility

129 Online Documentation • Page Screenshots

## 131 Multimedia

• Auto-Installing Plug-Ins

• Client-SideMultimedia

## 134 Response Time

• Waiting for Software to Evolve

## 134 Images and Photographs

• Image Reduction

## 143 Animation

• Showing Continuity in Transitions

Indicating Dimensionality in Transitions

• Illustrating Change over Time

• Multiplexing the Display

• Enriching Graphical Representations

• Visualizing Three-Dimensional Structures

• Animation Backfires

• Attracting Attention

149 Video

• Streaming Video Versus Downloadable Video

154 Audio

155 Enabling Users with Disabilities to Use Multimedia Content

156 Three-Dimensional Graphics

• Bad Use of 3D

• When to Use 3D

## 160 Conclusion

• The Attention Economy

## 3 Content Design

Ultimately, users visit your website for its content. Everything else is just the backdrop. The design is there to allow people access to the content. The old analogy is somebody who goes to see a theater performance: When they leave the theater, you want them to be discussing how great the play was and not how great the costumes were.

Of course, good costume design contributes greatly to making the performance enjoyable and to bringing the author's and director's visions to the stage. But in the end, the play is the important thing.

Usability studies indicate a fierce content focus on the part of users. When they get to a new page, they look immediately in the main content area of the page and scan it for headlines and other indications of what the page is about. Only later, if they decide that the content is not of interest to them, will they scan the navigation area of the page for ideas of where else to go.

Content is number one.

## Writing for the Web

It's the rare case indeed when a book about the Web discusses writing guidelines, which is why I will take the opportunity here. When writing for the Web, you're not only affecting the content, you’re affecting the core user

## The Value of an Editor

What is the impact of violating the guidelines for writing the headline for a news item on an intranet home page? For a company with 10,000 employees, the cost of a single poorly written headline on the intranet home page is almost \$5,000. Considerably more than the cost of having a good home page editor rewrite the headline before it goes up.

I have based the preceding estimate on the following assumptions:

■All employees spend five seconds more than necessary pondering the headline because it is not sufficiently communicative.

W The poorly written headline causes 10 percent of employees to click on the headline even though the story is useless to them.

■People spend on average 30 seconds reading the story before they decide to back out because it's useless.

■The company has 10,000 employees using the intranet.

The value of an employee's time is \$50/hour. (Note that the value of an employee's time should be much more than his or her salary, and account not only for benefits and overhead but also for contributions to the company's bottom line. Therefore, a person who makes \$25/hour usually ends up costing the company \$50/hour, which is the relevant number for figuring out the cost of lost time.)

This little example also shows the basic principles for performing cost-benefit analyses of usability issues. You estimate the various ways in which the design causes people to lose time (or to avoid purchases, if you are discussing an e-commerce design) and multiply that by the percentage of users encountering the problem, as well as the total number of users and the value of their time (or purchases, in the case of e-commerce).

experience because users look at the text and the headlines first. Although it's important to be grammatically correct, it's also important to present the content in a manner that draws in readers.

The three main guidelines for writing for the Web include the following:

■ Be succinct. Write no more than 50 percent of the text you would have used to cover the same material in a print publication.

Write for scannability. Don't require users to read long continuous blocks of text; instead, use short paragraphs subheadings, and bulleted lists.

■Use hypertext to split up long information into multiple pages.

A fourth guideline is more of a process or management rule: Hire web editors. Good content requires a dedicated staff that knows how to write for the Web and how to massage content contributions into the format required by your design standards

## Keep Your Texts Short

Research has shown that reading from computer screens is about 25 percent slower than reading from paper. Even users who don't know about this human-factors research usually say that they feel unpleasant when reading online text. As a result, people don't want to read a lot of text from computer screens. Therefore, you should write 50

## Web Attitude

Although web text should be short, it should not be without personality. Usability studies show that users appreciate some amount of humor and attitude in web pages. Note that "attitude" does not mean screaming or whining at readers, or treating them to a punkish diatribe. What's respected is the presence of a clear voice, perspective, and personality in the exposition. Angry young writers write for each other; most of the web audience tunes them out.

Users have a distinct dislike for anything they deem marketing fluff. The Web is a rather "cool” medium that encourages the use of facts with links to back-up datasheets and detailed numbers. You cannot get away with the superficial hyperbole that may work in television commercials or magazine advertising. When users see pages that have lots of blather in place of facts, they instantly discount the site's credibility.

The correct amount of attitude in a web page is: Not too much, not too little.

![](images/76f2eea82c45c372af6bf2d629f0efc09bcb0d3358fe743336ebdcae16fc5970.jpg)

WELCOME

WHY CHOOSE BAXTER?

WHAT'S AVAILABLE?

detailed search

recertly added positions

return visitor log-in

RECRUITING EVENTS

INTERNSHIPS

FINANCIAL DEVELOPMENT PROGRAM

HUMAN RESOURCES DEVELOPMENT PROGRAM

CAREER SITE FEEDBACK

## Welcome

Hello. I'd like to personally welcome you to Baxter's career site. Weve developed this site in response to the many requests weve received for career-related information.

Baxter employs approximately 41,000 people in approximately 100 countries - a diverse employee population that shares the company's vision to improve the quality of life for people worldwide. We are strongly committed to our employees, professionally and personally, as you'll see in the pages that follow.

![](images/1c395b2665103412df274af7c62ce81928fc0c88735dcaf7269ec9e5144e705d.jpg)  
Mike Tucker Sr. Vice President Human Resources

I invite you to check out our site. Weve taken great care to provide you with a valuable tool that allows you to manage your career search with Baxter. We offer a unique feature -- an on-line résumé form that allows you to maintain your résumé or curriculum vitae on our system for up to one year. You may update your record at any time, and link it to employment opportunities as they become available. Our database is updated weekly. Search it and communicate your interest directly to our staffing representatives.

I hope you visit our site often. If you have comments or questions, please feel free to share them with us using the "career site feedback' link. Thank you for your interest in Baxter.

percent less text—not just 25 percent less—because it's not only a matter of reading speed but also a matter of feeling good. We also know that users don't like to scroll: one more reason to keep pages short.

The screen readability problem will be solved in the future because screens with 300 dpi resolution have been invented and have been found to have readability as good as paper. Such high-resolution screens are currently too expensive (high-end monitors in commercial use have about 110 dpi), but they will be available for top-of-theline computers around the year 2002 and in common use five years after that.

Always run a spelling checker on your pages. Typos have a tendency to pop up where they are most embarrassing, as in DisCopyLabs' assurance that they pay "the strictiest attention to detail." Of course, a spelling checker won't catch mistakes like that shown in the second paragraph, which should read "and to shape" (instead of "and the shape"), or the misuse of the hyphen in the last line of the bullet item.

## Copy Editing

At a minimum, all web pages should be run through a spelling checker. Misspelled words are an embarrassment and may slow users down or be confusing. Many errors will not be caught by current spelling-checking and grammar-checking technology, so it is also recommended to proofread pages carefully for grammatical mistakes and for words that may be in a dictionary—affect and effect but are not the ones intended by the author.

![](images/e3fcc21561d614929205fd7dff332b628b1b96a00151ebcedb4a37676103a3ca.jpg)

## Turnkey Services

![](images/e9b7ad57125aa5199aabcd3397f772b2adcde4153512e9c6f732df11e24ae618.jpg)

Our customers consider us the manufacturing arm of their business. When you rely on DisCopyLabs as your partner, you can be free of the costly, complicated burden of manufacturing and distribution. You won't need to make a major investment in facilities, systems, staff and training. You won't need to pour your precious resources into every manufacturing detail.

Turnkey means we assume all manufacturing responsibility from beginning to end, competently and cost effectively. We work closely with our customers to identify their needs and the shape a comprehensive program, which may include the following:

● Project Management We will oversee your project through every phase from concept to completion, working closely with key people, paying the strictiest attention to detail and fulfilling our commmitment to quality- at no additional cost to you.

www.discopylabs.com

High-end web organizations should go beyond proofreading, however, and employ professional copy editors to go over the text of their pages. Not only can a copy editor correct many mistakes that are overlooked by automated checks, but they can also improve cases of bad or sloppy language. Most important, copy editors have a knack for tightening up writing. Many people—myself certainly included—have a tendency to love their own words and use rather many of them to elaborate on their position. Even for printed materials, a good copy editor can prune language to turn long-winded expositions into concise and tightly argued gems. For the Web, the copy editor's hunting instinct should be unleashed, and he or she should be even more ruthless than normal in tracking down and eliminating extraneous words.

## Scannability

Because it is so painful to read text on computer screens and because the online experience seems to foster some amount of impatience, users tend not to read streams of text fully. Instead, users scan text and pick out keywords, sentences, and paragraphs of interest while skipping over those parts of the text they care less about.

In a study by John Morkes and myself, we found that 79 percent of our test users always scanned any new page they came across; only very few users would read wordby-word.

The following table shows five different ways of writing the same web content for a site about tourism in Nebraska (see facing page). John Morkes and I tested the usability of all five sites, and the table shows how much better each variation was compared with the original text, which served as the control condition in the study.

Skimming instead of reading is a fact of the Web, and it's been confirmed by countless usability studies.Those who write for the Web must acknowledge this fact and write for scannability:

Structure articles with two, or even three, levels of headlines (a general page heading plus subheads—and sub-subheads when appropriate). Nested headings also facilitate access for visually impaired users with screen readers.

<table><tr><td>Site Version</td><td>Sample Paragraph</td><td>Usability Improvement (Relative to the Control Condition)</td></tr><tr><td>Promotional writing (control condition) Uses the “market-ese&quot; found on many commer- cial websites</td><td>Nebraska is filled with internationally recognized attractions that draw large crowds of people every year, without fail. In 1996, some of the most popular places were Fort Robinson State Park (355,000 visitors), Scotts Bluff National Monument (132,166), Arbor Lodge State Historical Park &amp; Museum (100,000), Carhenge (86,598), Stuhr Museum of the Prairie Pioneer (60,002), and Buffalo Bill Ranch State</td><td>0% better (this was the control condition)</td></tr><tr><td>Concise text About half the word count as the control condition</td><td>In 1996, six of the best-attended attractions in Nebraska were Fort Robinson State Park, Scotts Bluff National Monument, Arbor Lodge State Historical Park &amp; Museum, Carhenge, Stuhr Museum of the Prairie</td><td>58% better</td></tr><tr><td>Scannable layout Uses the same text as the control condition in a layout that facilitated scanning</td><td>Nebraska is filled with internationally recognized attractions that draw large crowds of people every year without fail. In 1996, some of the most popular places were: • Fort Robinson State Park (355,000 visitors) • Scotts Bluff National Monument (132,166) • Arbor Lodge State Historical Park &amp; Museum (100,000) • Carhenge (86,598)</td><td>47% better</td></tr><tr><td>Objective language Uses neutral rather than subjective, boastful, or exaggerated language (otherwise, the same as the control condition)</td><td>Nebraska has several attractions. In 1996, some of the most-visited places were Fort Robinson State Park (355,000 visitors), Scotts Bluff National Monument (132,166), Arbor Lodge State Historical Park &amp; Museum (100,000), Carhenge (86,598), Stuhr Museum of the Prairie Pioneer (60,002), and Buffalo Bill Ranch State Historical Park (28,446).</td><td>27% better</td></tr><tr><td>Combined version Uses all three improve- ments in writing style: concise text, scannable layout, and objective language</td><td>In 1996, six of the most-visited places in Nebraska were: • Fort Robinson State Park • Scotts Bluff National Monument</td><td>124% better</td></tr></table>

Use meaningful rather than "cute" headings. Reading a heading should tell the user what the page or section is about because it is too unpleasant to be forced to read the body text. For example, USA Today had a headline in the printed newspaper reading"Twosome tells wired world what's news" Cute, but worthless as a web headline. Luckily, its website rewrote the headline to read "Bringing news to the wired world." Better, though not perfect. My preference would have been something like "Editing news for Web portals' home pages."

Bulleted lists and similar design elements should be used to break the flow of uniform text blocks.

Use highlighting and emphasis to make important words catch the user's eye. Colored text can also be used for emphasis, and hypertext anchors stand out by virtue of being blue and underlined. Any highlighting or background colors must be chosen to look distinct from the link colors; otherwise, users will be confused and will try to click on the highlighted words in the belief that they are links.

## Why Users Scan

More research is needed to truly know why 79 percent of web users scan rather than read, but here are four plausible reasons:

Reading from computer screens is tiring for the eyes and about 25 percent slower than reading from paper. No wonder people attempt to minimize the number of words they read. To the extent this reason explains user behavior, users should read more when, in five years, those high-resolution, highscanrate monitors are available.

The Web is a user-driven medium where users feel that they have to move around and click on things. One test user said, "If I have to sit here and read the whole article, then I'm not productive." People want to feel that they are active when they are on the Web.

Each page has to compete with hundreds of millions of other pages for the users' attention. Users don't know whether this page is the one they need or whether some other page would be better. And they are not willing to commit to the investment of reading the page in the hopes that it will be worthwhile. Most pages are in fact not worth the users' time, so experience encourages them to rely on information foraging. Instead of spending a lot of time on a single page, users move between many pages and try to pick the most tasty segments of each.

Modern life is hectic and people simply don't have time to work too hard for their information. As one test user said, "If this [long page with blocks of text] happened to me at work, where I get 70 emails and 50 voicemails a day, then that would be the end of it. If it doesn't come right out at me, I’m going to give up on it."