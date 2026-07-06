# The Five-Minute Learning Curve

With the exception of Jeff Rulifson and Larry, everybody at PARC was extremely wedded to the NLS interface that was developed in Engelbart’s team. Jeff was the least wedded to it, perhaps because he had come up with it.

“Why is everybody so excited about this interface?” Larry said to Jeff, who laughed.

“I don’t know, because it was never designed!” Jeff replied, “When they implemented the system, they didn’t have a user interface; they just knew what they wanted it do.”

Jeff kept asking what the user interface was going to be.

“Well, I haven’t designed that yet,” was the reply, “I’ll do that later.”

Jeff was assigned the task of testing the system, so he took the procedures in the language.There were commands like delete, left parenthesis, character number, right parenthesis, so he made something that was absolutely literally the same thing, only intended for the programmers testing the software. They all started using it and learned it, and then they started getting excited about how you could type the letters on the keypad by using binary code.What started as a testing language acquired a mystique; although it was never designed for end users and never analyzed scientifically, its aficionados grew to believe that it was an ideal interface for a system to augment the intellect. Perhaps it was. The trouble was that it was really hard to learn, and they admitted that.

Larry set out to prove that you could learn something in a day. He developed a little text-editing program that he called “Mini Mouse.” It didn’t use the NLS keypad at all and only used one button on the mouse. Before doing it he decided that he wanted to observe a user, and used a technique similar to his “guided fantasy.” He describes working with a secretary who had just started at PARC and was not yet influenced by the programs that were being used:

I sat her down in front of a screen, and did what’s now called a

“blank screen experiment.”

“Imagine that there is a page on the screen, and all you’ve got is this device that you can use to move a cursor around, and you can type,” I said. “You’ve got to make some changes to this document. How would you do it?”

I gave her a paper document with lots of markups on it for reference, and asked her to imagine that is was on the screen. She just designed it right there!

“I would point there, and then I would hit a delete key,” she said.

To insert, she would point first and then start typing. She’d never been contaminated by any computer programs before, so I wrote all this down, and I thought, “That sounds like a pretty good way to do it!” Later I also tested other new people like that and got similar kinds of results. I wrote a report about this. Up to that time, Bill English had been extremely skeptical about what I was doing. He seemed offended that I was challenging the “perfect” NLS editing language, but when he read my document a light went off, and he came to me and said, “This is really good!”

In the past, the programmers at SRI and PARC had thought that usability tests would be extremely expensive and time consuming and had done very few of them. Larry felt that he had to demonstrate that testing did not have to be difficult or expensive, so he built Mini Mouse in Smalltalk, like a typewriter. It turned out to be so easy to use that they could take people who were walking by in the building, and ask them to try it, and they were able to learn to operate it in five minutes—compared with a week to get comfortable doing comparable tasks using NLS.

## Double-click, Cut, Paste, and Cursors

The Mini Mouse triumph earned Larry the freedom to work more independently and to focus on text-editing software.When the gauntlet was thrown down by Ginn to help them with a publishing system, he was only too pleased to take on the task. He found Tim Mott, and they became partners in creating a new state of the art for text editing and graphic layout, as described in Tim Mott’s interview. Larry tells the story of inventing the doubleclick:

When I had written up Miki Mouse, which was going to be the next thing after Mini Mouse, I was trying to decide what to do with all this hardware. We had three buttons on the mouse. I really wanted it to be a single-button mouse, because I wanted to be able to use other things like tablets, touch screens and light pens, and you couldn’t do that with a multibutton design. Another reason was that when people were using the software, they thought of the mouse as being held by the pointing hand, with the other hand being for commands, either on the keyboard or on the five-key keypad. I thought if we could separate that out really cleanly we would reduce the common mistake of hitting the wrong button on the mouse. One in five times it was, “Oops, hit the wrong button.” This was why you had to practice a lot to master NLS, as so often you hit the wrong button.

“Maybe we could use the first button to select the cursor location between characters,” I thought, “and the second button to select a word, and the third to select a sentence or something.” I was with Tim and said, “I really don’t like this, because I’d really rather just have one button.”

One morning he came in and said, “I’ve got it; double-click! You click twice in rapid succession in the same place to get a word, and three times to get a sentence.”

“Twice maybe, but not three times, surely!” I said. I gave him all the reasons that it wouldn’t work, but when I closed my eyes and tried to envision it: “Yes it just feels right,” I had to admit, “doubleclick to select a word; it just feels right.”

We had already been implementing Gypsy at that point, and some of it was working enough so that we could try it. We brought in the secretaries and had them try it, and everybody thought it was good. There were lots of detailed technical arguments from the programmers, but basically it became a good thing right away.

One day Larry saw a novel way of handling “delete” and “insert” that had been developed by Pentti Kanerva, who was a software expert at Stanford University. It was done by first selecting what you wanted to delete and then saying escape-dreturn for delete, and then by moving the cursor where you wanted it and then saying escape-o for “oops,” which meant “undo last delete.” If you made a mistake, you just hit L, which meant insert, and it inserted whatever was in the buffer wherever the cursor was. The cursor was likely to be where it was before, so it came back.

![](images/80cf4e7da03f00a49776e0211da6612889f978632388a99b6d249ff2cb7dbd56.jpg)

The magic of this idea was that if you moved the cursor somewhere else after you said delete, it would move it there, so you didn’t need a move command. When Larry was working on Gypsy, he remembered that and thought that he could use it to avoid a special mode for moving.The trouble was that it was not good for copying, because you would need to copy it to the buffer.

We were doing this for a publisher, Ginn and Company, and we were planning to implement “cut” and “paste” to move things around in the document.

“Why don’t we use the same words, cut and paste, for this process of delete and insert,” I said to Tim, “and that way if you want to copy, you can say copy and paste.”

Tim agreed, so we named our commands, cut/paste and copy/paste. Because of that, I seem to have the reputation for originating cut-and-paste, but it was really Pentti Kanerva’s idea that I renamed and reduced the number of keystrokes from six to two.

There was no cursor in NLS: you just pointed at things and they became the first item (character, word, and so forth) or the last item of the selection. Every system that had a cursor took a character and either underlined it or showed it in reverse video; normally if you were doing white on green, you’d show green on white. The problem with that was that if you moved the cursor somewhere and started typing, it wasn’t clear where the character would go. The way it worked in most systems was that the character that you had inverted would change as you typed, so you would overtype things. If you wanted to insert, you had to go into a mode, like control-i or an insert key, and then everything you typed would get inserted before the character. Larry found in experiments that a lot of people expected it to go after the character, and some people were just confused. He didn’t want something you had to learn; he wanted it to be obvious. He was puzzling about this, and brought it up it during a meeting at PARC.

A few days later he bumped into Peter Deutsch in the hallway, who was not a user interface guy in any way; he was more of a systems guy.

“I think I have a solution to your problem of insertion for the cursor,” he said. “Put the cursor between characters, not on a character.”

“That’s a nice idea, but how do you know which character you mean?” Larry said.

“Well, if you click on the right half of the character, the cursor goes after it, and if you’re on the left half of the character, it goes before it.”

“Oh, of course, that’s so simple. It’s the answer.” Larry thought,“I just need a way to show that there’s this place between characters. In this publishing system they’re used to using this caret mark to show that something needs to be inserted, so I can use that.”

He started playing around with the caret mark, and finally came up with a caret that would work, overcoming the space management problem, and in the early systems they used a little caret mark as the symbol. Later, Dan Ingalls came up with the idea of just doing a vertical line between characters and implemented that for Smalltalk. They made it easier to see by making it blink on and off, to avoid confusion with a vertical bar. Larry tried other alternatives to make it more visible, for example curling the top and bottom like a sideways H, so that it didn’t obscure the character you were looking at, was easy to find on the screen, and had a clear meaning. The vertical line was the design that survived.

## Smalltalk Browser

Larry had been trying to get into Alan Kay’s group from the moment he arrived at PARC. As a result of the success of the Gypsy project, he was given the chance, and he started working on Smalltalk. He describes his delight in working for Alan and how he was challenged to design a browser:

Alan was always a great research manager; he would always challenge us, and would never be satisfied with anything. He was very good at rewarding people and acknowledging their work.

He would say things like, “We still don’t have a good way to query databases,” or “We still don’t have a good way to deal with animation.”

One of his favorites was, “You know, you can go to a library and you can browse the shelves, but we don’t have any good way to browse.”

Diana Merry, who had converted from being a secretary and become a Smalltalk programmer, said to me one day, “You know, we still don’t have a good way to browse.”

“I’m so tired of hearing that, Diana,” I said, “Alan says that every month, and I’m so tired of it! It isn’t such a hard problem.”

“Well then, go do it!” she said.

“If I do it, will you promise never to say this again?”

She assured me that she wouldn’t, so I had to figure out how to browse. I was thinking of graphical metaphors with books on bookshelves, and then thought that maybe I should start with something closer to home. We programmers are always trying to understand other people’s code, scrolling through big files of source code all the time trying to find stuff, and we don’t know what it’s called, so we can’t use the search command. I thought that if I could figure out a way to browse through code, we could maybe generalize it to work for other things too, plus it would be a cool thing to have for myself, so I decided to build a code browser.

I think this is one of those things that a lot of designers do. You just kind of close your eyes and vision, what would it look like? Instead of putting the secretaries in front of a blank screen, for a programmer’s tool, I’m designing for myself, so I can be the subject.

Close your eyes. Blank screen: what does it look like? Smalltalk had classes of objects, and methods, which were routines or procedures.

“Okay, I’ll have a text list of classes, and then when I click one of them, somewhere it’ll show all the methods,” I thought. “Then when I click the method, it’ll show me the code for that method. Then I can scroll through the lists, and browse around. That’s pretty simple!”

I got a piece of paper and drew it out and had the usual width problems with lack of room for three columns, so I put the two lists of classes and methods across the top, to allow a full width window for the code. It was a window broken up into three pieces, so I’ll call them “panes,” so we can have windows and panes. Each pane will have its own scroll bar so you can browse before you pick one to see the code. While we’re at it, once you’re looking at the code, I might as well let you edit it, using the standard Smalltalk editing facilities of drag through, cut-and-paste and all. I built it in somewhere between one and two weeks; it was one of those “Aha” kind of things, and it immediately started getting used by everyone. There were over a hundred classes and over a hundred methods; Dan Ingalls made a big improvement to it by dividing them into categories, so we ended up with four panes across the top. That became the classic Smalltalk browser.

This was the first browser design. It was a welcome change for Larry to design something for himself as a software engineer. He had become so wedded to the ideas of participatory design and user testing, that it seemed surprisingly straightforward to be designing for the user in the mirror. He went on to use the Smalltalk browser to build a point-and-click debugger and inspector. Other people have used the same metaphor to browse around databases. Although Web browsers are fundamentally more like Engelbart’s NLS, which used links to jump between documents, frames in Web browsers resemble Larry Tesler’s browser panes from 1976.

## The Brain Drain from PARC

Around 1980, lots of people started leaving Xerox PARC.<sup>15</sup> At the beginning, when PARC was founded, the most inventive minds in technology had been attracted by the promise of creating something that would change the world and by the chance to work with and learn from each other. They had been together long enough to be strengthened by their collective experience, and many of them were itching for the opportunity to see their ideas move from research to reality. Xerox was struggling to maintain dominance in the copier market, as Japanese competitors were overtaking them at the lower end of the market and gradually moving up.The only part of the research at PARC that Xerox really took advantage of was the laser printing technology, and although that produced enough revenue to justify the investment in the research center many times over, it was increasingly clear to the people there that concepts for the “office of the future” were on hold. There was also a sense of opportunity in Silicon Valley, as the venture capital firms were starting to fund new-start companies for the development of products rather than just for chips. It was natural for all those brilliant researchers to want to take the next step in their careers, so they were looking around.

As it happened, Larry Tesler,Alan Kay, and Doug Fairbairn all resigned from Xerox on the same day, for three different reasons, to go three different places, without knowing one another’s plans. Larry was headed for Apple, where he started in July 1980. He had participated in the famous demo of PARC technology to Steve Jobs and the team from Apple and was getting to know more about them:

I was blown away by the Apple people. I had been trying to convince people at Xerox about my belief in the future of personal computers, but the Apple people appreciated everything in the demo that I thought was important. I agreed with all the things that they said should be done next.

“They think more like me than the PARC people do.” I felt, “I’m in the wrong place! I should join a company like Apple.”

Two years before I joined Apple, when the company had only thirty employees, a friend had dragged me along to a company picnic, but they still seemed to me like a bunch of hobbyists. Between the picnic and the demo, they had hired all these computer scientists and software engineers who were very sophisticated.

“These guys really know what they’re doing,” I thought, “and they want to do the right thing!”

When I got to Apple, I said once again, “What I want to work on is publishing systems,” but they asked me first to work on Lisa. They put me in the research group consisting of three people: Bruce Daniels, who was a systems guy; David Hough, who was a numerical analyst; and me.

“I don’t really understand what kind of research we’re going to do,” I said after I had been there a week. “We don’t have time to do research. Apple is not ready to do research. It’s too early in the history of the company.”

They agreed, so we went to the management.

“We’ve just dissolved our research group,” we said, “so you should just put us in the Lisa group.”

They did, so I started talking to Bill Atkinson about what I thought should be different. Bill was a neuro-psychologist by training, with a great combination of psychology, design (he’s now a photographer), and programming. He was a great integrator; he was a sponge. At first I didn’t think he was hearing people’s ideas, but he was processing them and synthesizing them in a wonderful way. It would be great to be inside Bill Atkinson’s brain!

This was the start of a great collaboration between Larry Tesler and Bill Atkinson. They formed a tight bond and creative partnership and went on to design some of the most significant and long-lasting interactions in the world of desktops and windows. An interview with Bill Atkinson follows in chapter 2, and he and Larry tell some of these stories together.

My PC

![](images/a5ca945388637a5efe5cc1c74bc6fae74c08da00886157fbd2f573981e65c74e.jpg)

![](images/6c4a30063c02000c37392b08e0b69030cfa70c7485712ba8d1bf0dd0c49701d0.jpg)

Bill went home; in one night he developed the entire pulldown menu system! Everything! He hadn’t just moved it to the top of the screen; he had the idea that as you scanned your mouse across the top, each menu would pop down, and they would ruffle as you went back and forth, and appear so that you could scan them all. . . . He’d thought up the whole thing in one night! I can’t imagine what happened that night.

Larry Tesler, interviewed in 2003, talking about Bill Atkinson in 1982

The desktop and mouse are the dominant designs for the personal computer. In chapter 1, we looked at the invention of the original concepts at Xerox PARC and the roots of the design thinking that defined the interactions. This chapter follows the development of the designs for the first versions that were affordable enough to be personal, with Apple Lisa and Mac, and then examines two significant steps forward with the first Microsoft mouse, and the desktop design for Mac OS X.

We look first at the parallel paths that led to personal computers. The low-cost road built on the typewriter as an interface to the computer, leading to the IBM PC, and remained dominant until the Macintosh arrived.The high-cost road started with the superior interface of the desktop and mouse but remained too expensive for commercial success until the cost of the components fell far enough to allow the breakthrough from Apple.

Bill Atkinson was the architect and designer of most of the precedent-setting software that made Apple so successful; he talks about his partnership with Larry Tesler, as together they invented many of the concepts that define the desktop. As a condition of the Xerox investment in Apple, Steve Jobs negotiated the rights to use the technology in the Xerox mouse, but he found that the design was still very expensive and not yet reliable. The story of the development of the first affordable mice from Apple is told— and the controversy over the number of buttons that would make the interactions easiest to learn and use.

![](images/1778e8af0c2b5ec52aadd62efc99a74f771a884c9fd9aced0d6782c87c22dad4.jpg)

In 1987 Microsoft decided to try to set a new standard for the design of mice; Paul Bradley, the industrial designer of the first Microsoft mouse, describes how they achieved some significant advances. Bill Verplank worked with Paul on the human factors for the mouse; before that he had contributed to the interaction design for the Xerox Star and has fostered connections between screen design, human factors, and computer science. He explains his point of view about designing interactions with a combination of words and drawings.

The design of the desktop seemed to be going nowhere in the eighties, and it took the return of Steve Jobs to Apple to shake out a new approach. Cordell Ratzlaff was responsible for the design of the versions of the Macintosh operating system (OS), from Mac OS 8 to Mac OS X, and he tells the story of the first major change in a decade, with the design of Mac OS X.

## The Low Road or the High Road?

Interactive computing started with Whirlwind, the supercomputer of its time, which was conceived in 1945 for antiaircraft tracking and by 1951 was working well enough to use. Whirlwind had two kinds of interactions, a Teletype interaction, and an interaction through a display and a pointing device. This led to two parallel paths; the first was to cost-reduce the Teletype interaction, a road that was initially attractive because it led to cheaper and more accessible machines. The second path pushed the limit of designing the human-computer interaction, developing the display and pointing device until the value of using a desktop and a mouse was proven, and it became the dominant design. The low road and the high road stayed parallel for a while, with the IBM PC winning while price was the most important issue. As soon as the costs came down enough, the graphical user interface won out. By the time Windows 3.1 arrived, the victory of the high road was apparent.

The low road built on the Teletype interaction, following the path of least resistance. It was much less demanding for the technologists, as they could build directly on the history of the powerful computing machines that were already normal in the industry, from ENIAC to IBM equipment, and cost-reduce the hardware to offer lower prices and better performance to their customers.That led to time-sharing through a series of machines, and to the LINC computer in 1962, the first attempt to build a personal machine that was not time-shared.That eventually led to the Apple II (1977) and the IBM PC (1981). The Teletype interaction evolved to become a “Glass Teletype,” with alphanumeric characters on a monochrome screen. The human operator was thought of as a component in the system, and trained to do the bidding of the machine. This was the low-cost road, and the commercially dominant one during the eighties.

The Apple II was one of a flurry of hobbyist machines that were inexpensive enough to make computing accessible for the enthusiastic people who wanted to write their own programs and plug together the hardware themselves. The key to it being a personal machine was the price, making it available to people who did not think about it as a tool for work, paid for by the company or the university, but rather as a plaything for evening and weekend tinkering.

The IBM PC was a renegade product within IBM, put together at a skunkworks.The founders set up a separate shop at the IBM plant in Boca Raton, Florida, far away from the corporate procedures and politics. In order to get the new product out really fast, they bought most of their components from outside IBM, including the operating system. CP/M was their first choice, but the president was out hang gliding on the day that they visited the West Coast to talk to him, so they went to see Bill Gates instead, who didn’t actually have an operating system but knew where he could get one. He picked one up and then licensed it to IBM. The PC had neither a desktop nor a mouse, but it did have the right price to appeal to legions of buyers in the purchasing departments of big companies. It also had sound basic ergonomics, with a keyboard that was profiled to match the format of the Selectric Typewriter, and good tactile feedback. The screen had clear fonts that showed up strongly against the dark background.There was no proportional spacing, just a character-based interface with a blinking cursor—nothing fancy, but it would do the rudimentary jobs once you had learned how.

The path to the high road came from the mouse. The most obvious link between Whirlwind and the future graphical user interface (GUI) was a pointing device. Once you had one, you could use it for choosing commands from menus. This allowed you to move from recall to recognition, so instead of having to remember all of the commands on the computer in a particular instance, all you had to do was recognize the one you wanted.

The high-cost road combined the display and a pointing device, leading to the desktop and the mouse. At first this seemed very difficult to achieve and impossibly expensive, unless you could justify it with something as important as the defense of a nation. “Personal computer” had the same sound then that “personal nuclear reactor” would have now, because computers were things that filled rooms. To most people, the idea of being able have a computer like this for yourself seemed ridiculous, but then there was Moore’s law<sup>1</sup> to consider. Moore’s law said that the stuff you could get on a chip, and hence the power of the computer, was going to double every eighteen months. If you asked,“How many years before I can afford to have one myself ?,” the law gave you an astonishing answer of ten years or so. That meant that you could build machines that were very expensive at the time with the capabilities that you wanted, and then watch the costs follow the Moore’s law slope right down. The personal computer arrived via the low road, but the value of the desktop and the mouse did not take long to dominate, as they offered better interactivity.

## Apple Lisa and Mac

At Xerox headquarters there was growing concern. A lot of money had been invested in Xerox PARC, and suddenly there were inexpensive computers on the market, including the Altair, Commodore PET, and Apple II. The arrival of VisiCalc and WordStar in 1979 gave people who wanted to try a spreadsheet or a word processor a reason to buy an Apple II. The Xerox management was starting to get a little nervous, saying: “They’re calling these things personal computers, but I thought that’s what we were doing.These things are \$800 and ours are \$10,000, and we’re worried.”

They put together a task force and sent some people out to PARC, but the prevailing opinion there was that the new machines were only toys. Xerox knew that they could never manufacture Altos cheaply, because of their union contracts and the way they’d built their machines, so they decided to invest in Apple.The idea was to start with an investment and perhaps buy Apple after a while, thus learning about cheaper manufacture methods, and possibly have Apple do the manufacturing of a commercial version of the Alto. It was a \$1 million investment.

Apple was heading toward a hot initial public offering (IPO), with everyone wanting to invest, so as a condition of the investment, Steve Jobs was able to negotiate access to some of the PARC technology, including the mouse. A lot of the people at PARC were very upset about giving rights to Apple, worrying about the cumbersome speed with which Xerox moved, but several demos were arranged, which are well preserved in books<sup>2</sup> and legend. The significance of the transfer of ideas from Xerox PARC to Apple has been greatly exaggerated, as Apple created new and different products starting largely from scratch, but several people left PARC to go to Apple, and took their experience and beliefs with them.

Both Lisa and Mac were very different from Star—full of new interactive features and dramatically less expensive to manufacture. Lisa was a wonderful accomplishment of interaction design, crafted over a period of four years by a team of twenty people in applications software engineering and user interface design. Like the Star, it was document-based rather than application-based, a regression that was forced on the design of the Macintosh to achieve the reduction in cost. You saw the documents, and the applications were just the things that backed different document types, resulting in a more coherent system than if you had to load applications individually. Lisa was full of innovations, including the header bar and pull-down menu structure that is characteristic of the version of the desktop that we use today.An extraordinary collaboration between Larry Tesler and Bill Atkinson<sup>3</sup> was the source of this invention, which is recounted in the interviews later in this chapter. Lisa was a multitasking operating system, but it was too big to run on the Mac 128, so the Mac had to sacrifice many of the most valuable features.The Mac made up for this in design flair; the software was developed by a small team of only ten people, inspired by the design leadership of Bill Atkinson. It shipped only eight months later than Lisa. The price point was right, and it was Mac that made Apple successful, with Lisa failing commercially but providing the important interaction design precedents.

## Microsoft Windows

Microsoft was quite vulnerable at that time, as Apple had the superior design, but Apple was restrained by the dilemma of having very high premiums for the Mac hardware. If they had licensed their operating system for use on the PC, the PC hardware would have been a lot cheaper than the Apple hardware. For the very uncertain return of making its software available for the PC platform, Apple would have given up the well-defined high margins it had and probably would have been forced out of the hardware business.

Microsoft had DOS as its operating system and tried to do a version of Windows, but the screen was too crude, so Windows 1

![](images/ae37a2b913cf3f79ddcb05898ffe58387169581c176a7250f9fc7bb355c95d19.jpg)

<sub>Original</sub> <sub>Windows</sub> <sub>packaging</sub> •

<sub>Windows</sub> <sub>1.01—file</sub> <sub>list</sub> <sub>and</sub> <sub>menus</sub> •

<sub>Windows</sub> <sub>1.01—Notepad</sub> <sub>text</sub> <sub>editor</sub> •

<sub>Windows</sub> <sub>1.01—calendar</sub> <sub>current</sub> <sub>day</sub> •

Windows 1.01—goodbye via ALT-F4

and Windows 2 were unsuccessful. Windows 3 was hardly any better. At last,Windows 3.1 was good enough, and was suddenly widely adopted. By the time Windows 95 was launched, Microsoft was in a very dominant position and the desktop and the mouse were the universally accepted paradigm for personal computers.

After Steve Jobs was pushed out, John Sculley took over the leadership of Apple.The company sued Microsoft over the use of the interface, and after long and expensive litigation the courts decided in favor of Microsoft.The judge’s decision was based on a precedent about functional versus visual copying; he said that Windows did not look exactly like Mac.The litigation may have distracted Apple from pushing ahead with innovations and improvements that would have ensured their lead. Microsoft’s domination was consolidated, and Apple nearly went under, just recovering when Steve Jobs returned. He pushed forward to develop Mac OS X and inspired his team of industrial designers to create captivating products.

Photo Author

![](images/2470adc97fc54eb0c7cfed3a669f396f42d26afb9b71a85e28097fc2edc2a347.jpg)

Bill Atkinson

Since 1995, when he retired from General Magic, Bill Atkinson has been pursuing his passion for nature photography full-time. The basement of his home in the hills above Silicon Valley is full of sophisticated equipment for photography and color printing. He has published a book<sup>4</sup> of photographs of polished slices of rock that glow with the most amazingly vivid colors, in designs as rich as any Kandinsky. His love of perfection comes across in every detail of this work. He has researched and published color profiles for accurate printing; he has taught the art of printing to the most famous nature photographers in the world; and he has photographed the very best samples of rocks from the collections of gem and mineral specialists. In 1978 Bill was a graduate student in neuroscience at the University of Washington when he got a call from Apple, suggesting that he visit. Steve Jobs persuaded him to join, saying, “If you want to make a dent in the world, you have to come to the place where it’s happening!” He was hired as the “Application Software Department,” and went on to lead the development of the software for Lisa and Macintosh, and to design MacPaint and HyperCard. He was a leader and inspirational designer at Apple for twelve years, during which time Apple grew from thirty people to fifteen thousand. In 1990 he branched out with two friends to found General Magic, based on a notion called Telecards, “Little electronic postcards that would fly through the air and, like magic, land in a loved one’s pocket.” Bill Atkinson designed several of the interactions that define the desktop.

![](images/8a72a28ff750d9366ea3f6b3eb17293216ce4f5c5ed2ca18c24c5d878bd4df30.jpg)