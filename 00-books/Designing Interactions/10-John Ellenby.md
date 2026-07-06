# John Ellenby

## Developing the First Laptop

While John Ellenby was at PARC he got to know Alan Kay and appreciated the promise of the Dynabook concepts. At the same time, he was worried by Alan Kay’s goal of developing machines for children. John was pragmatic enough to know that the initial price point would be too high for normal kids for anything as innovative as Alan was describing.The starting point had to be the customer with the most money and the most demanding need. Here is his description of the conversation that inspired the laptop:

I was meeting with a guy in the government. He was actually in the executive office of the White House. He said, “I really like the Alto, John. I really like the Dover laser printer. I really like this gateway to the ARPAnet. I really like that. It’s really good. I get emails this way, and documents this way, and the documents fly backwards and forwards, and this is really terrific and I really love it!”

And I said, “Well, do you have anything that you don’t like?” “Well, I don’t use it!”

“What do you mean? You said you like it.”

“I learnt enough about it very quickly, it’s very simple to use. I’ve got my secretary using it, and she’s a bright person, and she’s the one that uses it.”

“Is that how you think it’s going to go forward?”

“No. Let me tell you what I want. I want all this capability of your beautiful Alto, and I want it in half your briefcase.”

And he went and grabbed my briefcase, which I actually still have. It was a classic one for a Xerox executive—leather, with a solid wooden liner. I said, “This briefcase? That’s hard!”

He said, “I want it to go in half that briefcase, because I carry papers around.”

“Do you think you are typical of people?”

“Yeah, let me tell you. My job as a senior member of this establishment is to go to where the problems are. It’s not my job to hang around in the office. I have staff here. I call them on the phone, I get to them by fax, I send them telexes: do this, do that, and they do it. My job is to go to where the problems are, so I want a computer, a real computer (he actually referred to it as an RFC— you can guess what the F is for), I want a real something-or-other computer to carry around with me that has the communications, has all the capabilities of the Alto, but is downsized for me to carry.”

Boy, that was a real opening for me, because at Ferranti I’d been looking at the technology of flat panels and the technology of microprocessors, and nonvolatile storage, and I was projecting out when all of those would come together into something that you could carry. Because I had lots of people that wanted them for fire control and process control—somebody who wants to go out and look at the process and also look at the thing that’s controlling it. So to be able to link, and ideally by wireless, with something tablet like.

It was the briefcase that did it. It had to fit in the briefcase; not just inside, but in half of it! That became the design brief for developing the GRiD Compass computer. It was a seemingly impossible challenge that appealed to John’s imagination and set him going with boundless energy and determination. He had seen the components used in computers steadily shrinking, but if you piled them on a table they would still amount to a volume that was probably double that of the briefcase, not half. He would have to attack each individual component, either completely reconfiguring the item for a new shrunken configuration or thinking of a lateral solution that would allow him to use a completely different item.

First he had to start a company to do this, so he left Xerox in January 1980 and started structuring the dream team to make it possible. He gathered key Silicon Valley figures for his board, successfully raised money, and put together an amazingly talented team of founders for GRiD Systems.The company was structured in the best Silicon Valley tradition of attracting people of the highest caliber by offering an exciting challenge and founders stock.They would then be motivated to dedicate their lives to the success of the company, working long hours and doing everything themselves to begin with, with the expectation of becoming the highest officers in the company when the product proved its value.There were key players in charge of R&D, manufacturing, marketing, and experts in electronic hardware, software, and physical engineering and design. John transformed himself as he got the company going. In three months he changed from a freeliving and easygoing person to someone who was dedicating every second of his life to a single purpose.

One of the challenges was to find a way to hold the data and avoid the bulky disk drives that were being used for machines like the Alto. The Alto certainly sported a beautiful high-resolution display and mouse for interacting with the software, but the rest of the machine was huge and clumsy, too large to fit on top of a desk, let alone in a portable unit. John called it the “Gzunda.”

I called mine Gzunda, which no one understood. In Britain Gzunda is the potty you put under the bed. People said, “Why Gzunda?”

I said, “Well, it goes unda the desk.”

It occupied the whole of the desk, so you had to sort of cramp your way in. You had to dedicate a large part of your office to this box. Much of it was taken up by a big Diablo disk drive that held almost nothing at all, but in those days, that was all we could get. The processor was big and chunky, and the screen and everything else needed a lot of work.

The answer was to use bubble memory, a nonvolatile storage component from Intel. This could then be combined with modem access to remote data, to be provided from servers at “GRiD Central,” and each individual customer could have access to a larger file capacity than the 256K of bubble memory that was built into the laptop.The modem was also an essential part of the communications solution, but modems were big then too.

![](images/fed174d3f6a90c6f8a52725efb86e7f14fbc9e4a5c97eb0593ea25e47621bf74.jpg)  
<sub>Alto</sub> •

We managed to get a modem built. We went and met with Racal Vadic. We said we wanted a 1,900-baud modem, and they said, “Oh yeah, we make those. We’ll go get one.”

They brought this thing out that’s twice the size of a shoebox. We said, “Yes, we want a 1,900-baud modem, and we want it to use only 55 watts, and we want it to be this size,” showing them something the size of two packets of cigarettes.

“No way! Absolutely no way.”

“Well, we’ve spec’d it out, we have to have a 1,900-baud modem, so either you’re going to do the work for us, or someone else is gonna do it.”

“No, no, we can’t do that!”

Our hardware guy was sitting across the table from his counterpart in Racal Vadic, who gave him this wink, and we thought, “This guy had obviously figured out that, yes, with a monolithic, they know how to do it.”

So we engineered a sort of around-the-corner discussion with this guy, and sure enough, they could do it. It was a wonderful example of the Valley working.

The electronic components were starting to look somewhere close to feasible. They settled on the Intel 8086 processor. The details of the size tradeoffs would drive the physical design, with the most obvious questions being the size and weight. The first question for the component arrangement was which half of the briefcase to fill; a blockish volume could fill the left or right half, and a large flat arrangement would fit in the top or bottom half. The large flat alternative was advantageous for the keyboard and display—and an elegant proportion.

The first keyboard was too wide and too thick, so they developed a layout that still had the QWERTY arrangement but made do with fewer additional keys. They then found a vendor who was be willing to develop a thinner construction that still had good human factors of key travel and snap action for tactile feedback. The first display that they found was too small, using a limited number of characters on five lines, so that the amount of information that you could see was disappointing. They eventually found a prototype of a bright electroluminescent display of tiny golden yellow squares, developed by Sharp in their labs in Osaka, with individually addressable pixels rather than an array of characters. John describes the negotiations with Sharp:

The small screen that we had for the launch was an amazing screen; it was done for us by Sharp. We found it through a wonderful Japanese guy called Glen Fukuda, who came in and said, “I don’t know anything about electronics, but this is exciting, and I understand you need a screen, and where would you go? Obviously Japan. And where would you go in Japan? Well, let’s go talk to these companies.”

He did a bit of research. It was wonderful to work with this guy. He convinced Sharp Corporation, who were working on electroluminescent panels in the lab, to come and meet with us. I think it was Mr. Okana, who was the head of all research at Sharp Corporation, who came out first. He came to my house in Palo Alto and had to walk under this enormous oak tree. It had been raining, and the rain was still dripping from the oak tree. Afterwards his translator told Glen Fukuda to give the message to Mr. Ellenby that Mr. Okana, “Visited, knew the future, and raindrops fell, even though it was not raining.”

I still get goose bumps when I think of that. This guy was head of Sharp’s research. He had decided some time back to take the money that they would have used for a huge show of all the Japanese electronics companies and create this research laboratory for the EL panel and other advanced components. There was this wonderful moment when Sharp committed to build the electroluminescent panel for us. It was gorgeous, a wonderful, beautiful orange; I’d never seen anything like it.

The six-inch diagonal seems tiny now, but it was amazing to find such an excellent flat display at the time, which supported bitmap graphics as well as characters. Sharp built a factory especially to manufacture it for GRiD.All this was very new at the time, as there was not yet even an Osborne, an IBM PC, or an Apple Mac, let alone a pervasive Internet.

![](images/d77f7954bc91069012acec98ad7b2bc00e1ed10b26c897a2add82638ce003b6e.jpg)  
John Ellenby with the GRiD Compass computer at launch IBM PC

The power supply needed to deliver a whopping eighty watts, and was a huge brick at the beginning, so they worked on breaking it down and integrating it with the main printed circuit board to reduce the volume.

The first calculation for the weight was over eleven pounds, enough to stretch your arm if you carried it around for long in a briefcase that already had papers in it. The founders of the company were equipped with sets of weights, and asked to adjust the amount that they carried around in their briefcases so that it was starting to hurt, but without being completely intolerable. They came to a consensus that there was a dramatic cross over point at eight pounds, so that became the weight specification.

John wanted a repair service that would benefit from the overnight shipping offered by Federal Express, so that customers could send back a faulty machine and have it returned to them with a two-day turnaround.This set a standard for a drop test that was more demanding than the accidents that were likely if the machine fell off a table or was dropped by someone carrying it. They rented an impact recorder to find out how much rough handling the shipping would entail and sent it by Federal Express to Washington and back. When it returned, they unfurled the chart paper of the recorder in a long snake across the floor of the office. They saw the 20g impact (twenty times the force of gravity) when the recorder was collected from the office and tossed into the truck. They saw about the same impact when it was loaded on to the plane at the airport, but the big shock was at three in the morning when it was put through the automated sorting system at the central office of Federal Express in St. Louis. There it saw 60g, the equivalent of dropping it from three feet onto a concrete floor.This then became the specification for the robustness of the enclosure, a demanding mechanical engineering challenge. They chose to design the enclosure in die-cast magnesium, for the combination of strength and lightness, succeeding in meeting the specification and creating an amazingly tough machine. It was sent up in the space shuttle and used on Air Force One as a result.

The GRiD Compass computer was launched to the public at the Office Automation Conference in the spring of 1982 and was highly acclaimed. The price was double that of the luggable machines, so the market was limited to cases where high value was attached to small size, prestige, performance, and durability. The plan was to sell the products to large companies, so that the individuals could gain access to company-wide information on the road, connecting in to the “GRiD Central” server with the built-in modem. The most common users were expected to be sales and business executives. This audience did prove to be the mainstay for the company, but the business climate for computers was dramatically altered when IBM unveiled their personal computer in August 1981, and by the time the Compass was out, the world was moving fast toward MS-DOS and PC-compatibles. GRiD OS had a set of central common code that was very compact and supported a spreadsheet, a text processor, a terminal emulator, a message/email solution, and a draw program—all with a consistent user interface. They also had a universal file system structure so that a call from a program would go directly to the data, wherever it was. It could be in RAM, ROM, bubble memory or local disk, external local disk, out over wire at “GRiD Central,” or over the GRiD server within a client company.These were strong advantages, but not enough to resist the surge of demand for IBM PC compatibility, so John decided that the next version of the Compass would have to run MS-DOS, and it would be needed fast.

In order to do an MS-DOS machine, we had to do an IBM-compatible machine that ran MS-DOS. I remember going up to visit with Bill Gates; Charles Simonyi was up there at the time. Charles and I had worked at Xerox together. We showed them what we were doing, and Bill says, “This is great. Of course we’ll do a special version of MS-DOS for you.”

I could have reached across the table and given this guy a kiss.

![](images/64cc671f9f02af11f9e777589a0d030fff64fa594d1adfc4d745aad1e6098d37.jpg)

![](images/4e44b7b025860fbfb17048f8b5400b21a5d6266b9396a4d9d8b10247bcc65877.jpg)  
<sub>Pictures</sub> <sub>of</sub> <sub>GRiD</sub> <sub>Compass</sub> <sub>in</sub> <sub>space</sub> •

![](images/a3872ae6bbc674f2c18e4b2c0f0ac96fb09bfd80ff57522a95b8970406a39635.jpg)

The speed with which the GRiD team created the new version to run both GRiD OS and MS-DOS probably saved the company, which avoided the fate that had overtaken Osborne. The extraordinary toughness of the design also gave the unit an appeal for intelligence agents and soldiers, and soon GRiD was doing a thriving business in Washington. John talks about soldiers playing games:

We were selling a lot of GRiD computers to the armed forces. We had this wonderful game called Flak Attack. These tanks shot at each other and at airplanes—a great game. You selected the device and fired the gun by hitting the spacebar. We had a lot of equipment with the ninth infantry division in Fort Lewis, Washington. They bought a whole lot of GRiDs because they were developing mobility concepts— how can you move fast, run around in ATVs—a pretty exciting outfit. They took them out to the Yakima firing range and used them out there, which is sort of high deser—very cold at night, very hot during the day, very dusty. They were charging around with their GRiDs, and several GRiDs came back. I thought that this was a problem. It turned out that all of them had broken space bars. We thought, “Have these guys been playing Flak Attack?”

They were getting carried away. Whack! Whack! They’d actually been smashing the spacebar like proper infantry men should. You know, FIRE, FIRE, FIRE, FIRE! So that was a relief.

Once I was in Fort Lewis, in the officers’ mess. I was talking to one of the senior officers there, and he said, “The officers won’t use this stuff. It’s going to be used by the staff sergeants. We’re kind of the executive level here.”

He was a bit full of himself. There was a guy from what I think was a special forces unit standing there. I asked him afterwards, “You think officers will be using it?”

“Absolutely. They’re going to be some of your biggest users. Let me show you.”

And he took me out into the rec room that was part of the officers’ mess, and it had this row of video games. And there were all these young officers . . . “NNEEAAAOOO! CLICK CLICK CLICK!” There was Atari, all this stuff, all these fire, fire, bang, bang, bang games.

The basic design for the GRiD Compass computer stayed the same for more than ten years. There were many different components, with larger displays using plasma and LCD technology, floppy disk drives, and of course all of the electronics. The way in which the screen folded over the keyboard for carrying was one of the innovative features protected by patent, and it was this feature that generated income for GRiD, by licensing the design to other laptop manufacturers such as Toshiba and Sanyo. This geometry remained the dominant design for laptops until the components had shrunk enough to fit them around the keyboard and display, so that a clamshell arrangement became possible without a volume projecting out of the back behind the hinge.

The interaction design advances in this first laptop included the physical interaction of the shape and size, the folding geometry, and achieving a tolerable weight for carrying. The operating system was also very innovative, building on many of the concepts that had come out of Xerox PARC in the seventies. Jeff Hawkins, the founder of Palm and Handspring, worked at GRiD just before the launch of the Compass.

The GRiD OS was far ahead of anything anyone had conceived of at the time. We had a graphical OS—although without a mouse, but it was a graphical OS—scalable fonts, and a lot of the other concepts that later took hold in the computer industry. It was a true multitasking operating system, it was small, it was fast; it just was leagues ahead of everything else. We had email running on it way before anyone in the business had even heard of email; it had servers; it really had all the technology.

The precedent was set for laptops to follow, but it was Jeff who created GRiDpad, the first tablet PC and the next step toward Palm.

Photo Author

![](images/248f6790c2145845fe741db1dc942cb7d8dd0f61f4156efb160ff4eb44eb525d.jpg)

Jeff Hawkins

Jeff Hawkins has two sides to his life: one is designing mobile computers, and the other is working on brain theory. The side that is focused on the design of mobile computers led him to develop the first tablet PC, the GRiDpad, and then to found Palm Computing. At Palm, he was responsible for a series of products from the PalmPilot up to Palm V. He then went on to found Handspring, continuing with the evolution of designs with the series of Visors, and culminating with the Treo platform. The other half of his persona, dedicated to understanding the science of the human brain, has led him to start Numenta, where he is developing a new type of computer memory system modeled after the human neocortex. This technology is based on the ideas in his book On Intelligence,<sup>12</sup> which expounds an overall theory of how the brain works, and its implications for the design of computers. He sums it up as, “What makes humans special first and foremost is that we can model the world and we can predict the future; we can imagine the future. How the brain does this is what I detail in the book.” This double passion has helped Jeff to clarify his strategies for success as an entrepreneur and designer of handheld computers, while at the same time developing a point of view about neuroscience that has caught the attention of prominent scientists. Jeff went to Intel after studying electrical engineering at Cornell and was attracted to join GRiD Systems in 1982, working as part of the launch team for the Compass computer. He was there for ten years, except for a twoyear break to study neuroscience at UC Berkeley.

![](images/5d0fd53e08989a5c665116d6068e9223f0d14ff04c7ccfdd494d497b3f412d97.jpg)

![](images/b4d9077b12fda3de7445da050879ea8b1417bb21cb802e470d8a7071b2fcbbb7.jpg)

![](images/b0c6e72e8f929e589384798281f0ad4099a43c3c4d4a9a48ee4fa74f03872073.jpg)

## Jeff Hawkins

While I was away at UC Berkeley, I conceived of the idea of doing a tablet computer. I was getting interested in pattern recognition, handwriting recognition. It’s easy to put two and two together—a portable computer with stylus interface. It wasn’t even my idea, but I saw the potential of it and said, “This is something we can do.” I came back to GRiD in 1988 on the premise that I was going to develop the first tablet computer for them. I became the manager of the GRiDpad, the software suite and all the applications that came with it.

Jeff Hawkins, 2004

## GRiD

When Jeff Hawkins arrived at GRiD Systems in the spring of 1982, the Compass computer was designed but not yet launched, so he joined as part of the launch team, working on sales and marketing to put together training materials and write demo programs:

It was very exciting because GRiD was a startup company, and they were inventing the first real laptop, a real innovation at the time. I became involved in figuring out how to sell the product, which was challenging. It was a beautiful machine, but it was very expensive. In 1982 dollars, it was \$8,150. I will remember that price forever, as it was an incredible amount of money.

We were trying to sell a laptop to business executives, when at the time no businessperson used a computer or knew how to type. This turned out to be one of the biggest problems we had. The keyboard was something that your assistant or your secretary used; it was associated with word processing. Business people were afraid to use anything with a keyboard: they didn’t want to be seen using it;

they didn’t want it in their office, because it made them look like their secretary. One of the largest obstacles, besides the price of the product, was just getting over people’s expectations about what a business tool is and what a computer is and how business people use it. When you think back on it, it was amazing that it was difficult to get business people to use a laptop computer.

GRiDtask was a programming language that I developed as a marketing tool, to help people put together demos. I started making it more powerful to give it control of the computer, and to make it do anything you want. Soon our sales people were putting together applications for customers, using it as a sales tool. I was in marketing at the time I was doing this, so no one from engineering was looking over my shoulder. I had unfettered access to do whatever I wanted, and I created a very powerful tool. This became a language, which really became the heart and soul of much of what the company did from a software perspective going forward.

Jeff spent four years working hard with the marketing team at GRiD, struggling to sell the first laptop computer to customers who were not quite ready to pay so much for something that they thought their secretaries should use. The experience served to educate him about the nature of mobile computing, but at the same time he was hankering to learn more about neuroscience, and in 1986 he decided to leave GRiD to become a full-time graduate student in biophysics at UC Berkeley. He remembers the day he resigned:

John Ellenby was the founder of GRiD. I said, “John, I’m leaving, I’m going to go become an academic, I’m going to Berkeley.”

And he was really smart. He said, “Well, maybe you should just take a leave of absence. You might come back. You never know.”

I said, “I’m never going to come back, but fine, I’ll take a leave of absence.”

I left for a couple of years, but even when I was at Berkeley, I continued consulting for GRiD.

Jeff never really escaped the lure of developing mobile computers, or the excitement of working in Silicon Valley startup companies. It was during the two years that he was studying at

Berkeley that he came up with the idea of a tablet computer with a stylus interface.

While I was away at UC Berkeley, I conceived of the idea of doing a tablet computer. I was getting interested in pattern recognition, handwriting recognition. It’s easy to put two and two together: a portable computer with stylus interface. It wasn’t even my idea, but I saw the potential of it and said, “This is something we can do.” I came back to GRiD in 1988 on the premise that I was going to develop the first tablet computer for them. I became the manager of the GRiDpad, the software suite and all the applications that came with it.

Jeff was not the only individual with entrepreneurial visions of tablet computers. In fact, there was a flurry of new startup ventures at that time. As far back as 1983, Convergent Technologies had come out with a tablet computer called the Workslate<sup>13</sup> that was only 81⁄2 x 11 x 1 inch, but it only had a small display and no stylus input and never found the right applications to make it successful.

By the time Jeff was ready to go back to work, there were several very interesting ventures under way in Silicon Valley. One option for Jeff was to join a startup company called Go:

The whole tablet computer market was messy. We had the company Go, which took the high road. It had a whole new operating system, high-class hardware, high-class backers, and so on. I went and interviewed with them, because I didn’t have to go back to GRiD, as I could have gone anywhere I wanted. I said, “Well, if there’s a company formed to do this, I’ll go check them out.”

I met with Go when there were five people there. I immediately sensed that they had too grandiose plans. They were going to change the world, do all this stuff. Startup companies struggle, and you have to be more focused.

The physical design for Go was elegant,<sup>14</sup> and they made a significant advance in the use of gestures for commands, so that the stylus could be used not just for handwriting and sketching, but also to trigger actions without relying on a pull-down menu structure. Jerry Kaplan chronicled the development of this attempt to start from scratch with a pen-based interface in his book Startup:A Silicon Valley Adventure Story,<sup>15</sup> including his loudly voiced challenge to Microsoft that he would dominate the future of computing. He had gone through \$75 million in investment funding over a six-year period before he lost control of Go to AT&T.

![](images/78f39c1c6b1c876ac7207d2b9ce42d54992d932fbe3e08fa5c5878bddfc490f2.jpg)  
• <sub>Apple</sub> <sub>Newton</sub>

Momenta was also a high profile startup company, funded by venture capital in the expectation that a general purpose market would emerge for tablet computers. They built a pen-based interface on top of a Windows PC but were unable to stay the pace of improvements in the underlying PC from competitors like Compaq, IBM, and Sony. The design was innovative in the use of the stylus for directional flicking as well as clicking and tapping.They introduced a command structure<sup>16</sup> based on a flying menu that appeared at the tip of the stylus when you tapped, and offered a menu of choices selected by flicking the stylus in one of eight directions.

Apple was another possible opportunity for Jeff, as by this time the research program that led to the Newton was well under way:

I had heard rumors that Apple was working on something like this; this was before the Newton came out. I talked to them, but at the time they didn’t want to tell me what they were up to, so I had no idea that they were developing a completely new operating system. I thought the idea of porting the Mac OS onto a tablet was a more likely direction. In fact, when we were at GRiD, we approached Apple several times, trying to convince them to work with us on doing it, because we felt they had the best software platform for doing this. At that time, they weren’t interested. I had an opportunity to pursue it further, but I had two solid options at GRiD and Go.

I decided to go back to GRiD, as I knew that I would be in charge of the whole thing there, and that was more fun for me. GRiDpad was focused on simple form filling. GRiD was an existing company that was trying to survive; we were much more pragmatically focused. We were looking at vertical applications that we knew we could sell. I think GRiD had the most success of any of the new ventures. GRiDpad came out in the fall of ‘89, a little bit before the other tablet

computers. We built a business, I think its peak was around thirty million dollars a year, which was leagues ahead of what anyone else was doing in sales, but that’s because we were very focused on vertical markets.

The shakeout in the pen computing and tablet computing area was not long in coming. It is typical in any emerging market that people get ahead of where the real business is. This was a situation where there was such confidence in the potential for pen computing to become the next wave of general-purpose machines that speculation fueled the investment in new ventures, and a lot of money was lost when sales turned out to be limited. It also got out of control because there was a big rivalry between Go and Microsoft, which stepped up the level of investment in both companies, but the business just wasn’t there. Jeff believes that the problem was that these products were trying to replicate paper, putting them in competition with paper and books, a situation he has always tried to avoid:

I think paper is just this wonderful medium; it’s been honed for a thousand years. It’s really great! To try to do what you do with paper, with just drawing—line width, sketching, and so on—it’s very hard to get a good experience. Where the tablet type of computer really shines is where you’re not trying to capture the paperness of paper, but you’re trying to get the electronic or the back end of it. Form filling is a great example, because actually forms are pretty hard to do on paper. You never have the right space, it’s hard to know where to put things, there’s not enough room for instructions. So, there’s an example where an electronic version of a paper equivalent would be better. But in terms of the general idea that I’m going to sketch, draw and have a free-flowing paperlike experience—I’m skeptical about that.

Similarly with electronic books. Paper in books is just wonderful. It’s a beautiful medium. It’s superior in many ways to any sort of electronic form, especially if you’re trying to create something in a similar form factor. Also for the readability of text. Paper is amazingly good for different light angles and brightness and so on. It’s hard to get that on today’s digital technology.

![](images/7f7d0781c4f7b0b60be37a3191b4d5ce73a9086f551861fd9c562ee1c23b69ad.jpg)

In 1992, after building GRiDpad into a successful business, Jeff decided to see if he could develop a product that offered the best of both the laptop and tablet, in a project called the GRiD Convertible:

Instead of the normal laptop, where the display hinges down and covers the keyboard with the display hidden, we had a very clever design—well, I thought it was clever—where the display was up, and it had this double hinge and it came back; it had a nice mechanism to it. We brought that to market, but what we found out is that people don’t really want a laptop and a tablet combination. It wasn’t that the technology wasn’t ready, it just turned out that fundamentally it didn’t seem that this was something that people really wanted to do.<sup>17</sup>

This was a surprising but hard lesson, which stayed with Jeff ever since, making him skeptical about the efforts that Microsoft is making in the new millennium to boost the tablet PC. At this point we step aside and turn to Bert Keely, the “architect of tablet PCs and mobility” at Microsoft, to understand the ideas and interactive advantages that Microsoft is betting will make the tablet PC come into its own.

Photo Nicolas Zurcher

![](images/bcfbf879742367943af9f3e9e43b0c4e08f21be1a7aabafac8494930b0b23af8.jpg)  
Bert Keely

“The essence of what I’m trying to bring to the personal computer, you should probably think of as a ‘tablet mode,’ that is, the easy option of using the computer with one hand, even when you’re holding it with the other. While speech, touch, and buttons will all have a role, the pen is the most exciting tool with which to do that in the current generation of PCs.” When Bert Keely graduated from Stanford with an engineering degree, he went to a startup called Convergent Technologies, where he spent eight years developing desktop work stations. He first latched on to the concept of a handheld computer in 1988, when he joined John Ellenby to develop rugged devices for the police, fire service, and military markets at Agilis,<sup>18</sup> but the company was short-lived. Next he joined Silicon Graphics to develop work stations for design and scientific applications. It was there that he built an advanced prototype for a magazine page display with a powerful workstation behind it; the information, he thought, should be at the center of manual interactions. Silicon Graphics decided against taking this concept to market but gave Bert the opportunity to shop it around, leading him to a dialog with Bill Gates at Microsoft. He joined Microsoft in 1998, working first on software for electronic books, and then on a skunkworks tablet PC project, designed to help people take notes silently and intuitively in face-to-face meetings; this was launched as a service pack on top of Windows in 2002. Since then, Bert has been leading the efforts at Microsoft to improve the design of the tablet PC, earning the title of “architect of tablet PCs and mobility.”

![](images/f438afeaeaaa6bc3f8f0f23e20c5b6bda804d8d108073e7d45fa3620174b7820.jpg)

## Bert Keely

The breakthrough will come when mainstream users find themselves thinking, “Oh, there are lots of situations in which I just use tablet mode, because of the physical freedom I get. I don’t mind the fact that a keyboard can enter more words per minute than handwriting can, as I prefer tablet mode most of the time!” With the second service pack for Windows XP, some users are already there.

Bert Keely, October 2004

## Displays

When Bert Keely arrived at Microsoft in 1998, he brought with him a wealth of knowledge and experience of displays and highresolution graphics, so the first question he was asked to address was,“What can we do to improve the visual characteristics of onscreen reading, to make the display more like paper?”

He suggested a project to see if they could take advantage of all those little subpixels on the display and went on to develop ClearType, a program that takes advantage of the red, green, and blue subpixels, to smooth the fonts and create the best word shapes on screen. He explains how this works:

Anti-aliasing is the process of saying, “Okay, I don’t have an edge that directly represents the edge of the character, so what I’m going to do is kind of smear the edge I do have. I’m not going to have white on one side and black on the other side of that edge, I’m going to have grey on both sides of that edge.” ClearType starts by using the edges within the pixel, the edge between the red and the green

![](images/60608e7d6a95dcd9422b0fe818c72d3e03e3e788e54d8a96b92b6bbf195ea03e.jpg)

• <sub>Close-up</sub> <sub>of</sub> <sub>pixels</sub> • <sub>XY</sub> <sub>error</sub> <sub>between</sub> <sub>pen</sub> <sub>tip</sub> <sub>and</sub> <sub>cursor</sub>

stripe, and the edge between the green and the blue stripe, and adds anti-aliasing within the pixel.

As the eye has very different sensitivity to red, green, and blue, it turns out that it’s not a simple matter of smearing; we had to adjust the luminance values. Then because the human eye is much more sensitive to luminance edges than it is to color edges, we were able to take advantage of the eye’s willingness to accept some color error in order to create much sharper fonts.

A challenge for the design of displays for pen-based computers is to precisely align the sensed location of the pen with the actual location of the pen.The ideal would be to eliminate the displayed cursor and just have the pen tip represent itself, but this is hard to achieve.

More important than parallax, what you actually see on most tablet PCs is just a pure XY misalignment between the position of the pen tip and the coordinate the digitizer is reporting, either because of a lack of linearity or a lack of calibration. People commonly call this parallax, but it’s not a depth issue, it’s an XY error issue. Actual parallax, which means a perception of depth difference between where the tip of the pen is and the image plane, is not as big a factor. Notice when you’re looking at an angle down into a swimming pool, the foreshortening of the image actually translates it nearer to your line of sight through the surface.

What you want is to have the digitizer be accurate enough to really sense the location of pen tip and then let the user just think in terms of positioning it. When they see an onscreen object, they should be able to point at it directly with the pen tip, the way they did when they were three or four years old, learning how to draw with a crayon. They shouldn’t have to worry about positioning some direct but slightly indirect cursor.

## Portability

A stylus input should be designed to let you interact with your computer with only one hand.This in turn promotes portability, as you can be holding the computer with the other hand while you stand or walk around, or you can be sitting at a table and have your hands on something else, like some food or some documents that you are looking at, and use the computer at the same time.

The cell phone is something you carry with you all the time—WYATT, as Bert says.The personal computer can become something that you want to have with you at least most of the time, because it carries your whole digital world. Bert sees PCs becoming the second device for each person in a family to carry with them, so that the phone and the PC become digital companions:

Your family pictures, your music, your calendar, your contacts, your recent email threads, the documents that you’re reading, other things that you might have looked at recently that you want to get back to, every Web site you’ve seen since you bought that computer, all of this stuff; having your whole digital world on hand is something that the PC lets you do, because it’s fundamentally visual. You find yourself, when you go to dinner, a meeting, or an outing in a car, thinking, “Well, if I’ve got every street on the United States on that thing, and I’m comfortable with the user interface because I’ve figured out how to use it, that’s going to be the handiest way to carry maps, and all my visual information.

![](images/d1cb9b051bddd918fc77cf84ac365747efe71b4e5551bd8831ade1aed2121e96.jpg)  
<sub>Standing</sub> <sub>use</sub> •

![](images/da8d5825534c51aeb3fb39a5d3a611aef2afeab5765ea6ef49a0e0e262948ac4.jpg)  
• <sub>Drawing</sub>

## Pen and Paper

The metaphors of desktop and window were originally helpful to the novice users of PCs, because they made the behavior of objects in the abstract digital world relate to the familiar experience of the physical world. The personal computer has evolved a lot since then, and one can argue that the design has outgrown the metaphors. The actual behaviors of the electronic objects have more meaning to the user than the simulation of a physical world that now seems archaic; many children start playing with computers when they are two or three years old, probably before they have ever seen a file folder. Bert believes that the pen-based computer will grow up in a similar way, starting by trying to simulate pen and paper, and then evolving unique characteristics that have special advantages in the digital context.

The main uncertainty is whether it will take off in the first place, as there has to be an immediately recognizable value for people to make the leap from the laptop to the tablet. Jeff Hawkins is skeptical about this potential, in spite of the fact that he developed the first successful tablet, but he stayed clear of simulating paper by concentrating on form-filling applications. Bert Keely is much more ambitious and hopeful, and he bases his optimism on the unique value that pen-based computing offers. He sees the tablet supporting single-handed interaction, and hence operation when standing, or in social situations. He also believes that the ability to capture thoughts in a free-form fashion is unsurpassed with the pen.You can sketch and enter text with one hand with a fluency that you have been developing from childhood. It is impossible to do that with just a keyboard, or with voice input, and it is difficult to do it with a combination of keyboard and mouse.

Bert was experimenting with pen-based inputs when he was still working at Silicon Graphics:

We were focusing on how to make the pen and the finger great pointing devices, and great devices for capturing thoughts. That was because essentially we wanted to work directly with the display, and we knew that we needed a pointing device. The graphical user interface had clearly proven itself. We knew that the pen was excellent for capturing thoughts, and the finger was probably the most natural and most convenient thing to use for just reaching out and touching some piece of information.

The classic thought with regard to the electronic pen is that you want to make it look and feel and behave as much like a pen on paper as you possibly can. Now, the reality is that there are many different types of pens that behave very differently on paper, and pencils of course, and there are also many different types of paper. So, there’s quite a range of “pen on paper feels” that people can become accustomed to.

In the end, I think it’s going to remain a user preference. Some people love the feel of a fountain pen, and they even like the sound that a fountain pen makes. The feel of a fountain pen is literally a piece of steel scratching across fiber; that’s a very rough, very highfriction feel. The essence of a ballpoint pen is that you’re rolling almost frictionless, but if you press hard, you get the tooth of the shaft that’s actually trapping that ball, so you get a little bit of that scratch. The feeling of a pencil, of course, is one of graphite being deposited on the paper. One thing about a pencil is that the static friction is low, but there’s lots of sliding friction, because you’re actually pulling that pencil apart. So, what is the static friction? What’s the sliding friction? What’s the ratio between those two? What is the sound that the system makes? All of those are factors in “emulating” pen on paper.

Today we have a few coatings that can be placed on glass or on plastic that really do a good job of establishing the kind of “stiction” that makes a person feel comfortable tapping, and makes them feel more or less comfortable writing. We still have lots of experiments going on with regard to the kind of sliding friction that’s best. Once a person becomes accustomed to less friction and to the efficiency of movement that the slipperiness brings, they tend to like it and find that going back to paper starts to feel a little more tedious.

With a pen-based user interface you have the opportunity to leverage motor skills, which go far beyond the motor skills of moving a bar of soap around, which is essentially what it’s like to use a mouse. When we design for the pen and finger, we are trying to leverage the fundamentals of being able to do expressive things with your hands.

![](images/b37e98f81a9490a27d7f0e8515b1625a5e836f1069a8e329466539bef97f3954.jpg)  
<sub>From</sub> <sub>keyboard</sub> <sub>to</sub> <sub>stylus</sub> •

![](images/926ba9f1796e94929f750bad44b1bc3ae77463b491499bd0c83d7d39db72c300.jpg)  
• <sub>Handwriting</sub> <sub>recognition</sub>

Successful handwriting recognition may be a basic requirement for the tablet PC market to really take off. Microsoft is making a huge investment in what they call “Ink Analysis,” or the recognition of shapes within ink marks on paper or tablet. They are also studying the context in which particular strokes are being created, looking at the text to the left and the text to the right, and using those as part of the decision of what to elevate in the list of candidates. Analysis of the vocabulary of the individual user can also narrow the possibilities effectively, allowing the system to make better guesses about what each scrawl might represent.

Bert thinks that Microsoft is making good progress in handwriting recognition, but his optimism about the future of tablet computers is also based on the combinatorial advantages of using a stylus:

Something that you only find out when you’re using a pen as a text input device and also using it as a pointing device is that the interleaving of pointing and writing happens so fast that you really are able to compose as quickly with a pen as you can with a keyboard. This isn’t a function of handwriting recognition being an equal number of words per minute. This is a function of handwriting recognition, plus pointing, plus correction, plus placing your cursor, selecting, dragging text around, reformatting, and undoing. You’ve got this combination of things you’re trying to do, some of which is text input and some of which is pointing. When you can do that in a fraction of a second back and forth between the activities, it’s really astounding.

Using handwriting or voice recognition software gets very frustrating if there is even a very small proportion of errors, as it is annoying to have the flow of your consciousness interrupted by the need to make corrections. Many people attribute the failure of the Apple Newton to the lack of reliability of their handwriting recognition. Artificial intelligence (AI) promised to solve these problems but failed badly in the twentieth century, leaving the keyboard, and hence the laptop, in a dominant position. Jeff Hawkins had been studying how the brain works in parallel with his work on tablets and he thinks that it was his knowledge of “consciousness” in a literal neuroscientific sense that led him to take a lateral approach to handwriting recognition. We now return to him, as he describes the development of the PalmPilot and Graffiti handwriting recognition software.

![](images/89ae90863114aa862d321ddd0651a1436cf4b1c9de7f1688822d47cabb3cbf15.jpg)