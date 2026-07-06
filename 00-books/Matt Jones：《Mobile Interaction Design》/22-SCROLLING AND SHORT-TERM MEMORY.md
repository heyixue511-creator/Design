# SCROLLING AND SHORT-TERM MEMORY

Remember, human memory includes a limited amount of working storage – that’s the short-term memory (STM) – and when capacity is reached, it starts to leak, with items being forgotten. Imagine you are reading a document on a small-screen device. The smaller the screen, the greater the burden you will place on STM to keep track of things you need to note – what you can’t see you’ll have to remember. Soon, you will forget something you require and will have to either scroll back to find it again, or make a possibly erroneous guess as to what it was (Loel and Albers, 2001). A vicious cycle will be set up: as you become frustrated with having to repeat work, this frustration will further reduce the effectiveness of your cognitive processing. ■

When the web first began to be widely used, scrolling was seen as a usability disaster even on large screens with only 10% of users ever scrolling to view content beyond the bottom of the screen. Having been familiar with interactive systems that presented content in terms of fixed single screenfuls, they just weren’t used to the notion. Now, of course, everyone is happy to scroll through a web document (Nielsen, 1997a). A clear lesson for small-screen information architecture is that users need to be prompted and trained in any new form of navigation – in the simplest case, making sure users know they have to scroll is a start.

Let’s assume that vertical scrolling is acceptable. To what extent should it be relied on? Whatever the size of display, the answer is not too much – excessive scrolling without some clever visualization of the content will be tedious and disorienting for the user.

An important factor in assessing the viability of scrolling is the degree of effort needed to control the movement through the content. Consider the WebTV device that displayed web pages on a standard television set. Like today’s mobile devices, the amount of information shown within one screen was small compared with standard computers, due to the lower resolution of the TV display and the distance users sat from it. Scrolling through the content required lots of work on the user’s part, with many button pushes. Because of this, the design advice for the device was to make sure that each page of information fitted onto a single screen, with no scrolling (Nielsen, 1997b). Now, on some mobiles where scrolling is still a costly activity, presenting information within one or a limited number of screenfuls is also advisable. However, with many mobiles, the scroll control mechanisms are now sophisticated, so the size of the document being displayed within a scrollable page does not need to be so constrained.

## Goal-led navigation

Often, in mobile situations, users will be accessing content to achieve a goal; in these cases, they are not reading for reading’s pleasure. It is easy to imagine typical goals for handheld users – ‘find nearest motel’, ‘locate the bank with the best exchange rate’, and so on. Again, it is useful to turn to some early work on non-mobile systems which can help give clues as to the effect of small screen sizes on these sorts of interaction.

Remember, then, the work we mentioned in the last chapter on menus. There we saw that if users can see only a very small subset of the choices without scrolling, they can become disoriented.

In another set of studies Ben Shneiderman and colleagues carried out a study involving hypertext materials on limited displays. These documents were similar to simple web pages, in that users could interact with the texts, selecting links as they progressed through the task (Shneiderman, 1987). In one trial, two systems were compared: one group of users used a display size that was 18 lines of text in height, whereas the other group had a display capable of showing 34 lines. No significant differences in time to complete the task were recorded.

Any interactivity (like selecting from menus or following links) does, however, require extra effort compared to conventionally sized screens, so consider reducing the amount of navigation for key tasks, whatever the application.

## EXERCISE 9.1

## WEATHER INFORMATION SERVICE USABILITY PROBLEMS

One mobile, small-screen weather service has the following menu structure:

![](images/d7af5850c0b21f7532fcf8b2a352442413c42297ef814946f062d94cce42ff75.jpg)

So to find today’s weather in a particular location requires two clicks to get to the Region selection list, a further three scrolling actions (on average) and two clicks to get to the City selection list, and six more scrolling actions (on average) through this to indicate the city of interest. The My Weather option is designed as a shortcut and displays the current forecast for the last location viewed; it is dynamically updated each time a new location is accessed from either the Today or Future options. Discuss potential usability problems of this design and suggest improvements. ■

## User Experience

Task performance is one thing, but the way the users feel about the system is also important. It doesn’t matter how fast or efficient an information access scheme appears; unless it is enjoyable and pleasant, than you have lost your user.

In one of the studies we mentioned earlier, while there was little impact on performance between the large and small screens, the researchers did see a difference in the users’ satisfaction. When they asked participants whether they would like to change the size of their display, of those who said ‘yes’ the overwhelming majority (75%) were people who were using the small screen. They wanted a bigger display (Dillon et al., 1990).

How can you make your users feel good about accessing information through the small window available? The key to this is designing schemes that make it obvious that you’ve thought about how best to use the space and control mechanisms at your disposal. The users need to feel you’ve done as much as you could to shape the presentation into an effective one; if, in contrast, they feel they have to put in the effort to make sense of the content, they are likely to become increasingly negative about the service.

## 9.2.2 IMPACT ON BROWSING COMPLEX CONTENT

The studies we’ve just looked at used simple textual content, or textual content supplemented with basic navigation such as limited hyperlinks. In addition, the only scrolling users had to do was vertically, up and down the documents.

Today, though, and increasingly in the future, people can and will access far more complex content from their mobiles. Usually this is in the form of web-type information. Browsers on PDAs and many phones allow users to access content specifically designed for these platforms, as well as to view pages that have not been optimized for small-screen presentations.

How do users cope with these sorts of material on a downsized display? To find out we collaborated with Reuters (the international news content provider) to look at how people performed when completing tasks using web materials and a small screen. The content wasn’t adjusted in any way – we just used the pages as designed for large-screen viewing (Jones et al., 1999b).

We carried out a controlled, experimental evaluation method of the form discussed in Chapter 7, involving two groups of users. One set of participants had to work with a PDA-sized display similar in dimensions to device B in Table 9.1; the other viewed the materials via a desktop-sized screen.

What we saw was that if people try to use content that makes no concessions to the small-screen context, there will be huge usability problems. In fact, in our case, their ability to browse effectively broke down, and the participants resorted to non-browsing strategies. When we questioned users at the end of the trials, we found that most of them ascribed the failures to the small screen.

Of course, knowing that a system is failing is just the start. As in all interaction design, you have to look in detail at what is going on so that alternative schemes can be explored. So, the next question we asked was what interaction behaviors could have led to this poorer performance?

Participants on the small screen had to put in an enormous amount of effort to navigate within the pages. The number of vertical and horizontal scrolling actions carried out was many times higher than those on the large screens. This painful, high-cost page viewing led participants to be disinclined to browse. Indeed, when we looked at the logs of the pages accessed during tasks, we saw that while the large-screen users followed link after link, exploring areas of the site in a classic browsing way, the small-screen ones cautiously probed the information, with their browse-paths being considerably shorter.

Our small-screen users also showed how unattractive browsing was to them by using the site’s search features instead – most of them started every task by using it and employed it twice as many times as the large screen participants. That is, they didn’t want to wade through hard-to-navigate material; they wanted a direct answer.

The log analyses we carried out also showed something else interesting. The overlap between the pages viewed by the large-screen users and the small-screen ones was not high. As the former group were the most successful in completing the tasks we set them, it seemed that poorer link choices were being made by the small-screen bound users. Content that was hidden by many scrolls or page clicks was being overlooked.

## 9.2.3 IMPACT ON SEARCHING

Searching is perhaps the most widely performed computer-based task – we search our email for previously received correspondence, we search the web for anything and everything, and we hunt for photos we’ve taken and stored on our hard-drives.

Web searching in particular is a hugely popular activity, with some search engines reporting hundreds of millions of user queries every day. On the desktop, then, search systems are seen as useful and the most popular ones as reasonably usable. Given this appeal and the emergence of search engines for mobiles, we carried out a follow-up investigation to the browsing studies, to compare search performance on large screens to that on much smaller devices (Jones et al., 2003a).

We took as our focus the versions of a major search engine aimed at the phone market, which was WAP based, and another designed for handheld PDAs. The sorts of question we wanted to answer were ‘‘Does the small screen environment reduce users’ effectiveness and, if so, how?’’ and ‘‘Do users alter their searching behavior when using small screens?’’.

If you’re thinking of building a mobile search interface, there are two elements you need to address:

How to present the search results: as a list? More visually? What summary information do you provide – these are the meta-data or surrogates for the actual content: author, title, keywords?

How to integrate the task of reviewing the results with accessing the content itself: select from list and display full content, as in conventional search engines? Use a technique like RSVP (see Section 10.4.3) to automatically present results one after the other? Provide roll-overs to show snapshots of content without the user having to navigate to another page (see Figure 9.8 for an example)?

The design choices for the WAP and PDA versions we looked at are shown in Figure 9.1. Search results are presented as a list. Each includes some meta-data about the actual page to help a user make choices about which to explore. In the desktop version, with more space available, additional information including a longer summary is displayed for every result.

When a user clicks on a result in the list, the corresponding page is displayed. Often, in the WAP case, this process involves some additional processing by the search engine. This is because the number of web pages explicitly created for WAP devices is still tiny – Google, for instance, estimates that 5 million of the 8 billion pages they index are WAP-based (Google). So that WAP users can access any page indexed, there has to be a transcoding process, taking the standard web page and breaking it up into a series of smaller, linked WAP pages.

To find out how users might fare with these small-scale versions, we asked a group of participants to use them to complete some tourist-style tasks: they had to find out the opening hours of a major art gallery, for example.

The results of this investigation suggest that trying to use a WAP-type device for search might lead to some very frustrating user experiences: in our case, only 36% of tasks could be completed successfully. The picture is more encouraging for PDA-type devices: our users achieved around 80% of the tasks.

For both the WAP and PDA cases, when the users succeeded they did so quickly, with few interactions with the search engine. When they failed, though, they failed badly. We looked through the logs of access and found some explanations for these two distinct patterns of use – quick successes and prolonged, painful failures.

![](images/825eb36aec424b23bda5173968b8224ec5a1672876c27e7b510df1a32a1b8862.jpg)  
FIGURE 9.1  
Using a search engine on a WAP device (top) and a PDA (below). Note that in the WAP case, conventional web pages are split into a series of smaller ones for display

The first thing to note was that small-screen users were making choices from a smaller set. That’s because the default small-screen list length was five and that of the large screen 10; in line with other studies, our users rarely went beyond the second page of the results list. So, on average, the large-screen users were selecting from a set of 20 choices, small-screen users from 10.

As with the browsing study, exploring any search result on the WAP or PDA small screen had the potential of involving a very high cost in terms of time and effort. As Figure 9.1 illustrates, finding information within a conventional HTML page, which is being redisplayed on the smaller interface, can be a tedious and frustrating task. A major cause of failure, then, was the great difficulties users had in navigating the site selected from the search result. Most of their wasted time and effort was spent in becoming increasingly lost within the small window.

Failing users also carried out more search engine interactions: they used a greater number of search attempts for each task, browsed more of the search result list pages, and viewed more of the result pages themselves. The impression was of users ‘thrashing’ to solve the problem. They would carry out an initial search attempt, spend more time scanning the search result outputs, explore a search result, becoming lost and frustrated, and then return to the search engine for another fruitless attempt.

In the unsuccessful cases, often it seems that users were very uncertain about whether a search result they were about to explore was going to be of any use. They then made blind leaps of faith into a usually disappointing unknown.

The successful cases for the WAP and PDA contexts were where the search engine results contained ‘obviously’ good candidates. These results were the ones where even the limited information about the page (title and web address – URL – for WAP; title, URL and limited summary for PDA) was enough to suggest the page was worth exploring.

When we asked users to indicate the main reasons for their having problems with the search interface, for the small-screen versions the size of the screen was identified as the main culprit. For the large-screen version, display space was not a major issue at all. In terms of identifying the most helpful elements of the interface, in all cases, users valued highly any information that helped them judge the potential usefulness of a result.

## 9.3 DESIGNS FOR BROWSING

Now we’ve seen the likely usability problems in browsing and searching content on a mobile device, let’s turn our thinking to making things better. First we’ll consider browsing again, and then we’ll go on to make suggestions about designs for search.

In the studies of small-screen browsing, the content did not accommodate the constraints of limited displays in any way. The results, as we saw, were unpleasant, with users failing to complete tasks, becoming bewildered and frustrated as they struggled with the systems.

If you are a content developer wishing to see your information accessed on mobiles, the message is very clear: you cannot simply expect users to access information designed for the large screen on their small-screen devices. The experience could be awful and users may not tolerate it.

A number of mobile web browsers are emerging that go some way to solving the problems (we’ll see some examples in Section 9.3.2). They take standard content, optimized for large screen viewing, and adapt it to make it more palatable for handheld access. Of course, in adapting the content, the way the user experiences the information will be very different from the way originally intended by the designer.

For some content providers, the quality of interactive experience provided by these solutions will be adequate. Information services that are primarily aimed at a large-screen audience, and that expect infrequent visits by mobile users, need little extra design thought, if these sorts of automatic adaptation systems are available to users. If this describes your situation then all you need to do is to make sure that you structure your content so that these bits of rendering software can do a good job (see Section 9.3.2).

But if you are seriously considering delivering material to mobile users, you should not abrogate your responsibilities by relying on the efforts of a third-party. Rather, your aim should be to ensure that the content that leaves your server is in a form that both fits the display restrictions of its destination and has a design that is consistent with the style and image you wish to present.

The next sections will help you think about how to adjust the content design so it makes better sense on the small screen. You’ll find some helpful guidelines and also some example presentation techniques that live up to the ideals. When you go to develop mobile content, check your information architecture against the guidelines and be inspired by the examples.

## 9.3.1 GUIDELINES

Browsing, as we’ve seen, involves two activities: navigating through the content to find interesting portions, then reading through the material. To support these two tasks effectively on the small screen, the information design should aim to:

allow users to overview the material at every opportunity;

promote focused, direct access; and

reduce scrolling.

## Overviews, Overviews, Overviews

Any technique that helps the user quickly grasp as much of the content as possible, to assess the value it might provide to them, is helpful. What you want to avoid is users futilely spending time perusing material that doesn’t meet their needs: the goal has to be to allow them to see easily whether the content looks promising, without their having to commit to accessing it fully. The sorts of aspect to consider, then, include the following:

Writing style. It is well established that people read differently on the screen compared with how they do so from paper. One important element of online style is the need for conciseness. For small screens, this advice is even more important. Give the reader exactly what they need, neither more nor less.

Summaries. Structural overviews are useful (think outlines, tables of contents, etc.) and summarized content can be effective too. In the latter case, while the default view of the information should contain the key points, the user should be able to reveal further details if they wish.

Skim-reading. People tend to scan online content. This is a rapid process where the reader is trying to identify the main points, assessing relevance and seeking out content they are interested in. One study, for instance, of desktop web use showed that 79% of users worked in this way; with only 16% reading word by word (Nielsen, 1997b). Scanning can be promoted by structuring information effectively into sections and subsections, as well as highlighting important parts using fonts and other graphical effects. On the small screen, getting the font size, spacing between lines and layout of the information right is even more critical in this respect.

## BOX 9.3

## USING KEYPHRASES FOR SMALL-SCREEN SKIM READING (Jones et al., 2004)

Automatic techniques can pick out the keyphrases in a document text. Once spotted, these can be put to use to help a reader skim the information in various ways. The phrases themselves can be highlighted, as in the example shown in Figure 9.2. Alternatively, the sentences or even paragraphs containing the keyphrases can be brought to the user’s attention. ➤

The Wold Newton Family is a group of heroic and villainous literary figures. Science fiction author Philip José Farmer postulated they belonged to the same genetic family. According to Mr. Farmer, the Wold Newton family originated when a radioactive meteor landed in Wold Newton, England, in the year 1795 click here to see a monument to the event. The radiation caused a genetic mutation in those present, which endowed many of their descendants with extremely high intelligence and strength, as well as an exceptional capacity and drive to perform good, or, as the case may be, evil deeds. Popular characters that Philip José Farmer concluded were members of the Wold Newton mutant family include: Solomon Kane; Captain Blood; The Scarlet New Tools Options品自 (a) (a)

The Wold Newton Family is a group of According to Mr. Farmer, the Wold Newton landed in Wold Newton, England, in the year their descendants with extremely high concluded were members of the Wold Newton New Tools Options自 (b)

FIGURE 9.2

Two small-screen views of a document: (a) plain-text version; (b) with two keyphrases picked out in bold, and non-keyphrase text using much lower contrast

Keyphrase extractors assign probability scores against every phrase in a document, the value showing how likely the phrase is to be a key one – from 0 (not at all) to 1 (certain). These values can be used to control the degree of highlighting used, the highest scoring portions being heavily emphasized and less likely keyphrases given less prominence. ■

## Providing Focused, Direct Access

Small-screen users seem to choose and prefer direct access strategies which will lead them quickly to a piece of content. Handheld information designs should accommodate these preferences. Some possibilities are as follows.

Use a navigation scheme that allows users to move purposefully toward finding the content they need. A loosely structured tangle of information will not work well on the small screen. A better model to aspire to is one where the user can drill down into the information, moving from overviews to more detail. While the WAP approach to content structuring has been much criticized, one aspect in its favor in this regard is its use of a transaction model: each card (i.e. screen) of information allows a user to carry out a limited set of actions, leading to the next step of either completing a task or locating some content. However, avoid tedious, clunky structuring (see Exercise 9.1 earlier).

Present users with a small set of paths to content which will allow them to meet the majority of their goals. Whenever one develops content, it is tempting to give access to everything one can; however, this strategy will lead to overwhelmed users. That’s not to say that users should be prevented from accessing anything they want (see the discussion on portals later in Section 9.3.3). What you can do is to hide the extra material (consider, for instance, having options like Other information and More on X).

Provision of a search mechanism: sites which are to be viewed by handheld users must provide one or more search features.

## Reduce Scrolling

It’s clear that users will potentially have to carry out far too many scroll actions when using small-screen displays. Such activity will interrupt their primary tasks. Horizontal scrolling should be eliminated entirely – users should never have to involve themselves in the awkward two-dimensional navigation tasks we saw earlier. To reduce the degree of vertical scrolling, you can arrange content in the following sorts of ways:

Placing navigational features (menu bars, etc.) near the tops of pages in a fixed place.

Placing the most important information toward the tops of pages.

Reducing the amount of material on a page; making the content task focused rather than verbose.

## 9.3.2 SCHEMES

Remember that the purpose of guidelines is twofold. They can provide starting points for design, inspiring the choices you make as you begin thinking about an interaction scheme; and they are a critiquing tool for any prototypes that emerge.

Let’s now turn to some example content presentation schemes which aim at improving the user’s browsing experience on the small screen. Hopefully, you’ll see how these relate to the guidelines we’ve just presented.

We’ve classified the different approaches as being 1D, 1.5D and 2D (one-, one and a half- or two-dimensional) in nature. What we are attempting to do by this is to distinguish between the different levels of layout complexity inherent in a scheme – the 1D schemes focus the user’s attention simply in a vertical manner, whereas the 2D ones structure the content horizontally as well.

The 1D and 1.5D sorts of scheme are especially relevant to the smaller mobile screens of phones, while the 2D is more suitable for the larger, fully-featured ones seen on the likes of PDAs.

## 1D Browsing

To visualize this approach, imagine content being presented along a narrow, vertical film-strip. The user starts reading it from the top and can scroll down it and back up using only a simple vertical control.

Take a look at the screenshot shown in Figure 9.3 – how would you convert this into a linear form? A usable approach could involve moving the main navigation bar on the left of the screen to the top of the page, and then, beneath this, placing the content in order of importance, broken up into blocks. You might also want to repeat the main navigation elements at the bottom of the page as well as throughout the document to allow the user to make selections without having to return all the way to the top. An illustration of how this might look on a small screen is shown in Figure 9.4.

![](images/fc2f6aaee1db9d346dc54a4f89679a864418e70b55f9e9e06ee76e7501ad8f52.jpg)  
FIGURE 9.3  
News website viewed on a large-screen desktop PC

In passing, it’s worth noting that this example of a pared-down presentation is the low-graphics version of a popular news website. One reason the provider allows this view of its content is to make it easier for users with limited eyesight to read it. It turns out, though, that other types of impairment – such as a small screen – benefit from the design too. This is another illustration, then, how the universal access thinking we talked about in Chapter 1 can lead to widely applicable designs.

![](images/089fa6833f1c9a98d8351e8cd865918a22b64cc2f073fd057c4fe994f460c51d.jpg)  
Low-graphics version of the news website exhibits a linear form, more suitable for small-screen viewing

In the above example, the web design team has explicitly thought out how to re-present their material. There are, though, a number of commercial browsers that automatically do this sort of conversion. One of these is the Opera browser for mobiles (Opera); another is NetFront from Access which employs the Smart-Fit Renderer to turn the content into linear form. Figure 9.5 shows how one example website appears when seen through the Opera lens. These sorts of adaptation systems work by identifying components in the content – menu bars, adverts, etc., – and using some heuristics to place them in a more usable sequence.

While the adaptation is an automatic process, you should not assume that it takes away all the design effort. The tool providers advise content developers to be aware of how their transcoding process works and to design with it in mind. Opera, for instance, suggests that you should check your large-screen web designs to ensure that the following appear:

A small set of links horizontally at the top of the page

A further set in a vertical bar on the left of the page

<sub>•</sub> Subsidiary links in an area on the right of the page.

A design that features just a very long list of links in the left-hand navigation bar would not reproduce well using their rendering algorithm approach – the user would be confronted with having to scroll vertically through this long set of links before getting to any of the content itself.

![](images/b901b4424b1309a2cb3a3f2b30837fbeafba877e5182917f688305f3d0ff6db3.jpg)  
FIGURE 9.5  
The Opera mobile browser. Standard web pages are rendered as a vertical film-strip to improve small-screen usability

## 1.5D Browsing

In the 1D browsing approach, viewing all of a page’s content is a simple matter of rolling through the filmstrip. The attractive aspect of this sort of design is that it is easy for a user to grasp how to control the view, and the navigation process places little demands in terms of mental effort.

However, in many cases, where there is a fair deal of content, the process of scrolling through material may take up much user time, as the linear view will fill many screens of the small display.

To cut down on the amount of information presented, you should consider techniques that summarize or hide content. We’ve termed these 1.5D browsing schemes. As you’ll see, with these approaches the information – be it a page or a larger grouping such as a website subsection – is shown to the user using a hierarchical scheme. So, at first, the user sees only an outline of the content, but they can progressively expand their view, seeing more and more detail. We call them 1.5D because, as with the 1D approaches, the basic navigation the user performs is to move linearly through the outlines, but as they expand the content it appears progressively indented along the screen’s horizontal axis.

## Page-level schemes

Orkut Buyukkokten and the Stanford University Digital Library Lab developed the PowerBrowser (Buyukkokten et al., 2000). One of its features is a browsing approach they called accordion summarization; just like the musical instrument it is named after, the content can be expanded or contracted to see more or less detail (Buyukkokten et al., 2001a).

It works by first identifying the structural blocks in the page – called Semantic Textual Units (STUs). A STU might be a bullet-pointed list of items or set of paragraphs or any of a number of other components the system can recognize, using a rule-of-thumb approach. Like the 1D methods, then, the system parses existing web content and finds its building bricks. Unlike the 1D approaches, though, there’s the notion of hierarchical relationships – STUs can be nested within others.

Having extracted the structure of the content, it is then visualized as a hierarchy. STUs are displayed with nesting controls ( , – ) that allow a user to expand or contract the view, respectively. Want to see what’s within a unit? Click the control. The approach protects the user from being engulfed with content – they can overview the possibilities and get more details of the interesting-looking portions.

As we earlier mentioned in the section on guidelines, textual summarization methods are also useful in reducing overload and clutter on the small screen. If you want to consider using summary techniques for your own content, there’s a wealth of approaches you can take. As a taster, consider the following methods demonstrated in the PowerBrowser. In each case, the user gets more and more information each time they click on a summary icon next to each section of text (Buyukkokten et al., 2001b):

Incremental – present first line of text only, then the first three lines, and finally all of the text.

Keyword – present automatically extracted keywords from text, then the first three lines, and finally all the text.

Summary – present the most important sentence (again automatically extracted from the text), and after a second tap present all the text.

Keyword/summary – hybrid of the keyword and summary methods, presenting keywords, then key sentence and finally, after another click, all the text.

These sorts of method can dramatically reduce the amount of scrolling a user has to carry out. Orkut and his colleagues quantified this by taking a number of web pages and viewing them on a phone and PDA-sized screen. Without summarization, the sites filled between six and 324 screens of the phone and between three and 88 on the PDA. After summarization, this dropped down to 1–6 on the phone and 1–4 on the PDA.

When they compared the performance of their system with another small-screen browser that presented the original content in a linear fashion, they found that with their approach the time to complete tasks was much faster, with the number of scrolling actions being substantially reduced. Of course, the method is dependent on there being a good and meaningful structure in the content; on top of this, if the summarized version of each component poorly expresses the information it contains, it’s likely that the user will overlook it, failing to open it up to browse potentially useful material.

PowerBrowser’s purpose was to render large-screen designs in a useful way on the small screen. However, the approaches it illustrates are really good pointers to the sorts of methods that can be used when developing content specifically for the smaller displays on mobiles. Look at the content you want to deliver, then, and think about the importance of each part – does the user need to see this immediately or can we hide it away for them to discover as necessary? Think back to the news site example in Figure 9.4. On the small screen, headlines could be shown to the user initially. Clicking on the headline link might lead to the full story (displayed on another page), but clicking repeatedly on a summary icon could lead to the content being expanded within the current page.

## Site-level schemes

The idea of providing a hierarchical overview can be applied to units of content larger than the single page. Two systems we worked on – LibTwig and WebTwig – used this approach to give overviews of digital library content and entire websites, respectively.

Looking at the digital library case first, you might not know what a digital library is but you have probably used one, accessing articles such as those referenced in this book, or reading back-issues of a magazine, online. In short, a digital library is the web wearing a suit and tie – that is, the material is more formally classified, organized and structured.

Figure 9.6 shows how LibTwig presents digital library content. Users are shown an overview of the categories of information available to them; each of these can be further explored to view any subcategories. This top-down expansion of the table of contents continues until a list of actual documents is shown; selecting one of these presents the content in all its detail (Buchanan et al., 2002).

In WebTwig, our small-screen web browser, there are no categories and subcategories but, rather, sections and subsections of a site. The browser software works by first crawling through the web content, much as a search engine does when it indexes a site, attempting to work out the structure of the information (Jones et al., 1999a). Then the user is shown an overview of all the content, which they can interactively expand and contract. So, for the news website in Figure 9.3, the WebTwig version would initially show a linear list of headings such as ‘Front Page’, ‘Africa’ or ‘Americas’; clicking on any of these top-level sections would display the relevant subsections (e.g. ‘Nigerian party leader steps down’ and ‘Protests at Congo Poll Delay’ for ‘Africa’). The PowerBrowser does a similar job to WebTwig at the site level.

There have been user evaluations of all these three systems which compared performance with the situation when users have to access non-adapted content on the small screen. The results of these studies indicate that users can be faster and more satisfied with the overviews. So, if you have a large amount of information to convey on the small screen, consider using these sorts of dynamic tables-of-content which give users the power to explore the space of possibilities before delving into the detail.

## 2D Browsing

The 1.5D schemes we’ve seen need interface elements both to control the interaction and to display the results of a user’s action. So, the PowerBrowser has the nesting controls and summary icons, and

## Subject

Find:

Search

Agriculture and Food Processing

A Animal Husbandry and Animal Product Processing

A Communication, Information and Documentation

A Development Periodicals and Magazines

A Settlements, Housing, Building - Infrastructure Construction (Roads etc)

A Society, Culture, Community, Woman, Youth, Population

A Women, gender and development, women's organizations

## Subject

Find:[

Search

A Agriculture and Food Processing

Animal Husbandry and Animal Product Processing

Cattle

Other animals (micro-livestock, little known animals, silkworms, reptiles, frogs, snails, game, etc.)

Butterfly Farming in Papua New Guinea

Little Known Asian Animals With a Promising Economic Future

Managing Tropical Animal Resources - Crocodiles as a Resource for the Tropics

## FIGURE 9.6

LibTwig hierarchical overview of digital library content (Buchanan et al., 2002). User can dynamically expand or contract view to see more or less of content

LibTwig uses node control widgets to expand and contract content. These sorts of items use up valuable screen space. In addition, there’s a limit to the degree of overview possible – the font size used for the textual descriptions has to be large enough for the user to be able to read and interact with them.

The 2D techniques we see here, though, use an alternative approach to provide overviews that give access to detail. Instead of being textually oriented, they are visually based, using zooming visualizations.

Increasing and decreasing content magnification is something we’re all familiar with on the desktop. Consider looking at a map: if you need to orient a location to its wider surroundings, you can zoom out; similarly, if you want to read the street names in a specific area, you may have to zoom in. Or take document viewing: you can zoom out and scroll through content, and when you see an interesting picture, say, zoom back in to read the surrounding text.

Mobile map and document viewers that use these sorts of zooming will become increasingly popular. In terms of applying the technique to web content access, an early attempt was the WEST browser (Bjork¨ et al., 1999). Pages of information (which are cards of a WAP deck) are shown to the user as thumbnail images within a single small screen. One of the pages, the one in focus, is displayed in a larger area. The user can change which page is in focus, and the display is dynamically updated, with the new focus becoming enlarged, and the old reduced. Selecting a page causes a complete zoom in onto the content, allowing it to use up the entire screen area.

The researchers also experimented with summarizing the content shown for each thumbnail: in one mode, the system displayed only the keywords for each page; in another, just the navigation links.

In a limited evaluation of the prototype, users were found to enjoy the approach but took some time to understand how it worked. If you develop any novel schemes for accessing content, you may find that when users first see the system they are puzzled by how to operate it. This in itself is not a sign that the approach is flawed – the issue is whether the mechanism can be explained easily, and once they have understood the method whether they can return, over and over, and use it without having to expend a lot of mental effort in using it. The user’s goal is not to gain satisfaction in operating tricky schemes you might provide, but to find and make use of information.

With the increasingly sophisticated graphics processors that are being developed for mobiles, zooming approaches can become more ambitious. The SmartView system, developed by researchers at Microsoft, is an example (Milic-Frayling and Sommerer, 2002). Like the 1D and 1.5D browsers we saw earlier, it also depends on finding a page’s layout structure; however, instead of then turning it into a linear or a hierarchical view, it goes on to use this knowledge in conjunction with a reduced, full view of the web page.

Figure 9.7 gives you an idea of how the technique operates. Each region identified by the system is highlighted, and when a user selects an area – say a menu bar – they are shown a full-size view of it.

Retaining the original designer’s design and presenting it in overview in this sort of way has two main benefits:

Users might be able to quickly spot areas of interest by recognizing structural landmarks – a main content area, navigation bars and so on.

There’s also the consistency between the way the information looks on the large screen and the mobile counterpart. We have excellent spatial memory abilities, so when we look at a reduced visualization of a web page we’ve seen previously on the large screen, we may be able to use this knowledge of how the content is organized within the page. Bonnie MacKay saw this effect in action when she tested the GateWay system which is similar to SmartView.

One problem with SmartView, identified by other Microsoft researchers, is that in many cases it is difficult to make out the detail in the parts of a page without zooming in (Baudisch et al., 2004).

![](images/3aa0b326a47f2dfba7ede2db62e70cb97484fc2c6fe6b5ee93301bca27a61b08.jpg)  
FIGURE 9.7  
SmartView browsing techniques (Rodden et al. 2003)  
Left hand image shows reduced view of complete web page; right hand, the zoomed-in detail of one of its components

This can lead to the user having to ‘hunt-and-peck’ in their search for the portion of content they want to view: they zoom into one area, find it doesn’t contain what they are looking for, return to the overview and repeat this process (perhaps several times) until they find what they need.

The GateWay system reduces this problem by using roll-over boxes to give a preview of the detail (see Figure 9.8) (MacKay et al., 2004). The Microsoft team, though, demonstrate a more radical solution they call Collapse-to-Zoom (Baudisch et al. 2004). As well as allowing users to zoom into an area of a page, this also gives them the opportunity to strike out areas that don’t look interesting to them. If you want to read only the main text, you might remove navigation bars, pictures and adverts, for instance. With each component removed, there’s more space for the rest of the content to be redisplayed. After each deletion, the content is reconfigured, the remaining elements filling the display with the removed items being represented as small tabs on the edges of the display (the user can select these if they want the respective content to be added back into the picture).

These 2D techniques and the 1.5D ones tend to use a touchscreen and stylus. The approaches, though, are amenable to other types of control mechanism. Imagine then using a joystick control to navigate between the different sections of a SmartView type presentation; one button click could then activate the zoom-in, and another the return to the overview.

![](images/affd0ebb027057abadb01f976175578a423c42ce12790ee0013d94661b27e227.jpg)  
FIGURE 9.8

GateWay browser (MacKay et al., 2004). As in the SmartView system (see Figure 9.7), browser gives visual overview of web page on small screen. Pop-ups act as magnifier lens to give detail

## EXERCISE 9.2

## WEBSITE REDESIGN

Get a pad of PDA-sized Post-it notes, and create a prototype redesign for a website you’re familiar with – your corporate intranet or university site, for instance. Create ➤ a sequence of screen layouts for the main page and a range of the other content and functionality supported by the site.

Comments: first think about the sorts of information users will want when mobile – what can you leave out or de-emphasize in the mobile version? Is there anything missing which would be useful in this new context? Then consider the guidelines and schemes we’ve been looking at and apply them in your redesign. ■

## 9.3.3 PACKAGING CONTENT

Many mobile users will want specific types of information or to be able to access particular resources which are important to them. So, they might want to read a news digest, get some sports information and perhaps view entertaining content. In the business context, their goal might be to access information – from product details to company address books – that can support them while they are away from the office.

Recognizing this, there are a number of techniques that can bring sets of content to the user in a consumable way.

## Portals

This very common approach involves providing users with a choice of resources via a (usually, at present, not simple) set of menus. Apart from sorting out menu structuring, portal providers need to think about how limited the selection should be. For many providers, their instinct is to establish a ‘walled garden’ – users can access only the resources placed before them; they cannot stray to locate alternatives, or if they can, the process is complex. Be careful: there is nothing more frustrating for a user than thinking the system is nannying them. A more pleasing approach for users is to complement these ‘approved’ selections with easy ways for them to find and add additional sources. Give users access to a web search engine, then, and allow them to set up links to their own favorite sites.

## Channels

Channels are carefully selected sets of content, with a strong sense of brand, that are automatically updated and brought to the user’s device. Instead of the user having to hunt for information, the latest content is pushed to their device. Channel technology had its debut on desktop devices several years ago but the success was very limited – users seemed to prefer the freedom of more interactive information access provided by conventional web browsers. However, the idea looks like a better fit for the mobile market, where the costs – in terms of user effort and bandwidth charges – of extensive browsing seem more of a deterrent.

On the mobile, some channels might contain very limited, focused information, leading to interactions which are more ‘glancing’ than browsing in nature. A commercial example is illustrated by the wristwatch-style devices, developed by Microsoft, that provide micro-content such as weather forecasts and news headlines. Just as you might steal a glance at your watch to look at the time, you can do the same to get a quick information update. As the Microsoft manager for these technologies, Chris Schneider, notes (Evers, 2003): ‘‘This is not for reading the newspaper, but for the micro moments in people’s lives, providing perhaps a paragraph of information.

## RSS (Really Simple Syndication)

Like most people who use the web, you probably have regular sites you return to, over and over again. Visiting them to see what’s new or updated can take up a fair bit of time. What if you could see a summary of all the updates to these sites, conveniently displayed on a single page? That’s what RSS is designed for. The scheme works like this: websites publish summaries – called feeds – of their updates, then a piece of software on the user’s device (often called a feed-reader or news-aggregator) gets all the summaries from the sites a user subscribes to, and displays a timely digest. Many users then simply read the summaries without visiting the sites themselves, but if they really want more detail they can easily navigate to the content itself. RSS and related schemes are becoming a desktop phenomenon; you can expect to see its popularity rise on mobile devices, too.

## 9.4 IMPROVING SEARCH

In Section 9.2.3, we saw how users can get into difficulties when using a small-screen device to carry out searches. They can have problems choosing the best search results to pursue and are most effective when there are obvious good leads. If you are designing a mobile search interface, two of your goals should be, therefore:

to allow users to quickly assess the value of the set of results and to spot any particularly useful hits. If they would be better off trying another set of search terms, they should realize that sooner rather than later; and

to help them make good decisions about which results to pursue. Go for fully informed interaction – avoid them having to make guesses about possibly useful material.

Let’s consider each of these goals, in turn.

## 9.4.1 ASSESSING SETS OF RESULTS

A simple improvement on the small-screen schemes seen in Section 9.2.3 would be to increase the number of results shown on each page, say from 5 to 10. Because people tend to review only the first couple of results pages produced by a search engine, pages with smaller numbers of items will lead to fewer possibilities being considered. Furthermore, extended page-to-page navigation, as we saw in the browse case, is not something users want to engage in, so displaying more information on each page is beneficial.

A more sophisticated way of helping users to see more results while not overburdening them with navigation activities is, once again, to exploit the power of overviews. Instead of giving users a simple list of search hits, the individual results can be grouped together and the overall topics or categories they fall under can be shown to the user. One system that does just this is the Scatter/Gather scheme explored in Cutting et al. (1992). Here, similar documents are automatically clustered together. Key terms are then extracted from each cluster and a summary of these terms is displayed. Users can gain an understanding of the topics available by scanning the cluster descriptions.

Computationally neat while the idea is, a problem with automatic clustering is that the descriptions chosen for the clusters can be difficult to interpret. So, a more promising approach is to group documents into pre-existing, meaningful categories. Many search engines already provide browsing of categories to access their content. In Yahoo!, for instance, users can select from top-level categories such as Entertainment, Government and Health, and browse further subcategories to help them gain an understanding of the sorts of material available.

Susan Dumais – an information retrieval expert responsible for the desktop search innovations at Microsoft – and colleagues illustrated the value of such an approach on conventionally sized displays (Chen and Dumais, 2000). Their system automatically categorizes web search results against an existing hierarchical category structure. In an attempt to make good use of the screen space, the system displays the all-important first page of results in a way that gives an overview of how the results are distributed across the categorical structure. Only a top-level category view is shown, and just the top 20 results are given. The user can expand and contract categories to see more of the hierarchical structure and how the results relate to it, and additional matches can also be displayed on demand. A user study showed that users not only liked the new approach but were 50% faster at finding information than in a simple ranked-list scheme.

## BOX 9.4

## SEARCH AND THE QWERTY EFFECT

Despite many interesting interface research innovations over the past 10 years, as far as search engines on the large screen go, list presentations still predominate. There seems, then, to be a QWERTY effect. QWERTY keyboards were designed to slow typists down, in the days when physical typewriter mechanisms could cope with only limited typing speeds. Despite many keyboard layout innovations that would potentially improve the typing experience, QWERTY remains. It’s hard to overthrow a well-established interaction style. While novel search approaches have made little headway for desktop use, radical designs may be received more readily in the mobile market where conventional ways of presenting information just do not fit. ■

## EXERCISE 9.3

## SEARCHING FOR EMAIL ON A SMALL-SCREEN DEVICE

Imagine a user with hundreds of emails stored on their mobile device. How would you help them find particular emails?

Comments: on a large screen, a list of search matches which the user can reorder flexibly, sorting by say sender, subject or date received, can be a very effective approach. But on a small screen, where only 5–10 emails are visible and much scrolling is required, this could become unviable. You could make use of the user-defined mail folders (e.g., Meetings, Deliverables, Admin, etc.), presenting the emails that match a query in relation to these. For the items already assigned a folder by the user, this is trivial to do; emails still in the inbox, though, could be automatically classified by comparing their contents with those already classified by the user. The small screen may be big enough to show all the folder labels (and counts of relevant emails held within them) without the user having to scroll. ■

## BOX 9.5

## SMALL SCREENS AND CATEGORY SEARCH

The LibTwig system we discussed earlier uses a category-based overview approach to show the user the results of their queries. As with browsing, the outline view not only limits the amount of scrolling required to make sense of the search results, but provides context information which might help users make decisions about which alternatives to pursue.

![](images/c38ee78960d0723ca850e3f1b8b6d2c69b003163c6ee611d1a91563da5b87da0.jpg)  
FIGURE 9.9  
LibTwig outline view of search results

For example, in Figure 9.9, the user has entered a query ‘snail’ and is shown there are several top-level categories (including ‘Agriculture and Food Processing’ and ‘Animal Husbandry and Animal Product Processing’) that contain ‘snail’ documents. On expanding the first category, the user sees that two such documents are within the ‘Better Farming series of FAO and INADES’ subcategory. Finally, on further expanding this subcategory, they are shown the document links themselves (see right-hand screenshot). ■

## 9.4.2 JUDGING THE VALUE OF INDIVIDUAL RESULTS

What about helping a user decide whether to explore a particular search result? Knowing what topic or category a result relates to, as in the examples above, of course helps in this value assessment. The Cluster Hypothesis says that most ‘real’ matches to a user’s search could be grouped under a common heading; matches that are not in this category are probably less relevant (van Rijsbergen, 1979).

Providing category information, though, is just one of the ways to help users make good choices on the small screen. Another involves making use of keyphrases automatically identified from the candidate documents. Figure 9.10 illustrates the idea: the left-hand display shows a list of search results with the title for each document given for each item. On the right, in contrast, there’s the same list of documents but this time each is described by a number of phrases extracted from the documents themselves. In an experiment, this derived presentation was seen to be as effective as the title display in terms of enabling users to work out what a document was about (Jones et al., 2004).

![](images/ee8e097c381e0932a40eb5d75a51ae21981efe1b578bb0a0d23490546ea3f971.jpg)  
FIGURE 9.10  
Search result presentations: (a) titles of documents; (b) keywords extracted from the same documents

The information conventionally provided for a search result (e.g. the title, URL) could then be advantageously complemented with these sorts of extra item mined from the content. Giving users extra clues about the real content of a hit could guide them more effectively to the documents they actually need. Indeed, information extracted in this way and displayed in the result summaries could provide the answers without the user having to access the source at all, as an SMS search system described in Box 9.6 illustrates.

## BOX 9.6

## SMS SEARCH (Schusteritsch et al., 2005)

The Google text message search illustrates how text-mining techniques can be used to give users direct answers to their queries. A user sends an SMS message to the Google server containing their query terms and then receives one or more text messages back in return. Each message consists of details extracted from pages aimed at providing the information the user needs. No further interaction is required by the user. ➤

![](images/fa38f9c025ea4fd8c9e282553bb304c31c31cf3b9d7d47014aea94e59eb453c8.jpg)

Keyphrase approaches are useful not just for web-like document search tasks. Summaries of emails could be useful for the small-screen context; see, for instance, AmikaNow (AmikaNow). There is also potential for use in managing a user’s local mobile information space.

Let’s think about that second case – the management of information held on the device itself. Conventional desktop and laptop computers already have vast long-term local storage capabilities (for example, the laptop computer used to write this chapter has a hard disk capacity of 18 Gb). Mobile small-screen devices are also beginning to provide storage for large quantities of local information: it’s easy to find PDAs with 1 Gb local storage, and 60 Gb digital music-come-information storage players are also commonplace.

So, people already can carry lots of information with them on their mobile devices. In cases where this includes documents they have created themselves – presentations they are working on, reports they are editing and the like – techniques like the keyphrase one will become more important. That’s because it is more likely that the documents on these devices will have ‘poor’ author-specified titles/descriptors. For example, take a look at the contents of a folder from one of our laptop folders, shown in Figure 9.12. Some titles are obscure (e.g. ‘p3-churchill’), general (e.g. ‘Overview’), coded (e.g. ‘30070372’) or vague (e.g. ‘ideas’). Over time, and in the context of thousands or tens of thousands of documents, the contents of these files might be hard to discern from the titles alone. Additional surrogates such as keyphrases, both while browsing available files and when using the device’s search engine, might be essential.

Whatever information you decide to give the user about search results, you should do so as concisely and directly as possible. In the WAP search version considered earlier, only the first few words of each result can be seen at first with, after a delay, horizontal marquee scrolling used to show the remaining portions. A better design might have involved wrapping the full text of every result over several lines on the display, so the user could read the complete titles immediately. When we looked at displaying news headlines for a mobile service, we found that this non-auto-scrolling presentation was more effective than alternatives (see Figure 9.13).

<table><tr><td colspan="5">Name Size Type Date Modified</td></tr><tr><td>trademarks</td><td>1 KB</td><td>Text Document</td><td></td><td>14/06/2005 5:19 p.m.</td></tr><tr><td>currentTOCJune05</td><td></td><td>49 KB</td><td>Microsoft Word Docu...</td><td>13/06/2005 6:15 p.m.</td></tr><tr><td>FulTOC-forcopyedit</td><td></td><td>51 KB</td><td>Microsoft Word Docu...</td><td>13/06/2005 5:10 p.m.</td></tr><tr><td>mid-for-copyedit</td><td></td><td>462 KB</td><td>EndNote Library</td><td>13/06/2005 9:59 a.m.</td></tr><tr><td>wordcounts</td><td></td><td>14 KB</td><td>Microsoft Excel Works...</td><td>7/06/2005 10:54 a.m.</td></tr><tr><td>TechreviewsResponse</td><td></td><td>41 KB</td><td>Microsoft Word Docu...</td><td>2/05/2005 1:22 a.m.</td></tr><tr><td>mid</td><td></td><td>458 KB</td><td>EndNote Library</td><td>15/04/2005 3:03 a.m.</td></tr><tr><td>permissions_MID</td><td></td><td>39 KB</td><td>Microsoft Excel Works...</td><td>8/03/2005 10:25 p.m.</td></tr><tr><td>PERMISSIONSFORM-MID</td><td></td><td>38 KB</td><td>Microsoft Word Docu...</td><td>8/03/2005 9:32 p.m.</td></tr><tr><td>PERMISSIONSFORM</td><td></td><td>24 KB</td><td>Microsoft Word Docu...</td><td>8/03/2005 9:26 p.m.</td></tr><tr><td>coveringletter</td><td></td><td>104 KB</td><td>Microsoft Word Docu...</td><td>23/02/2005 11:33 p.m.</td></tr><tr><td>coverforboxes</td><td></td><td>24 KB</td><td>Microsoft Word Docu...</td><td>22/02/2005 7:58 p.m.</td></tr><tr><td>Mobile Interaction Design</td><td></td><td>20 KB</td><td>Microsoft Word Docu...</td><td>22/02/2005 7:13 a.m.</td></tr><tr><td>FulITOC</td><td></td><td>55 KB</td><td>Microsoft Word Docu...</td><td>22/02/2005 6:22 a.m.</td></tr><tr><td>overviewTOC</td><td></td><td>34 KB</td><td>Microsoft Word Docu...</td><td>22/02/2005 6:21 a.m.</td></tr><tr><td>Overview</td><td></td><td>25 KB</td><td>Microsoft Word Docu...</td><td>17/01/2005 10:19 p.m.</td></tr><tr><td>ideas</td><td></td><td>1 KB</td><td>Text Document</td><td>29/07/2004 10:32 p.m.</td></tr><tr><td>p115-tractinsky-VISUALBEAUTY</td><td></td><td>803 KB</td><td>Adobe Acrobat Docu...</td><td>24/02/2004 8:53 a.m.</td></tr><tr><td>因 p3-churchill</td><td></td><td>832 KB</td><td>Adobe Acrobat Docu...</td><td>19/01/2004 2:38 a.m.</td></tr><tr><td>因 30070372</td><td></td><td>337 KB</td><td>Adobe Acrobat Docu...</td><td>19/01/2004 2:30 a.m.</td></tr><tr><td>MIDrethink</td><td></td><td>28 KB</td><td>Microsoft Word Docu...</td><td>12/01/2004 4:55 a.m.</td></tr><tr><td>~$Drethink</td><td></td><td>1 KB</td><td>Microsoft Word Docu...</td><td>12/01/2004 4:55 a.m.</td></tr><tr><td>因 p370-ohshima</td><td></td><td>478 KB</td><td>Adobe Acrobat Docu...</td><td>5/01/2004 11:59 p.m.</td></tr><tr><td>notsure</td><td></td><td>370 KB</td><td>EndNote Library</td><td>1/01/2004 8:36 p.m.</td></tr></table>

FIGURE 9.12

Contents of a personal folder taken from a laptop  
![](images/afddf03f3e5ffd07bf81507b91d6867dc5217b77abeffb9f97f2aa308ad95e53.jpg)  
FIGURE 9.13

News headline presentation on the small screen: (a) horizontal, marquee scrolling approach (text moves to left to reveal full headline); (b) complete headlines presented using wrapped text. Second approach was seen to be more effective in user studies (Buchanan et al., 2001)