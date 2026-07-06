# The Rise of Interactive Graphics

What makes something simple or complex? It's not the number of dials or controls or how many features it has: It is whether the person using the device has a good conceptual model of how it operates.

—Donald A. Norman, from Living With Complexity

In the summer of 1996, Don Wittekind, a visual journalist who picked up some programming skills in a technical position at the Atlanta Journal-Constitution, got a phone call from Leavett Biles, the graphics director at the South Florida Sun-Sentinel, one of the major newspapers in the state. Biles was spearheading a major transformation in the newsroom, which involved the production of more video, audio, and motion graphics content.

He told Wittekind, “I know about you. I want you to come down here and produce multimedia informational graphics.

“But, Mr. Biles," Don replied, puzzled, “I have no idea how to make multimedia informational graphics.

“Nobody does," said Biles. “We’re gonna invent them."

So they did. In the next decade, thanks to a multimedia gallery called The Edge, the Sun-Sentinel would become one of the pioneers in producing interactive visualizations and motion graphics, first using technologies such as Adobe Director, and later, Macromedia Flash (Adobe bought Macromedia in 2oo5). As primitive as they appear to us today, some of their early interactive graphics, such as the one on fire ants in Figure 9.1, were eye-openers for many professionals.

![](images/f46504e57f90b58d7b15ee066ddb041ecdab2cadff92655dcd340c394a6e0907.jpg)  
Figure 9.1 Fire Ant Attack. The South Florida Sun-Sentinel, published in 1996. One of the earliest examples of news interactive graphics (http://www.sun-sentinel.com/broadband/ theedge/sfl-edge-t-fire-ant,0,324587.flash).

Similar moves were made by other media organizations, such as the Chicago Tribune, which used rising stars like Andrew DeVigal and Steve Duenes (both at The New York Times at this writing) to develop online news graphics. What all of them remember very clearly is the excitement of entering uncharted territory of play buttons and moving arrows rather than plain old ink, paper, and still pictures.

I cherish those early days myself. In the beginning of 2ooo, I was hired by El Mundo, a Spanish national newspaper, to produce interactive graphics. Like Don

Wittekind, I was clueless about interaction or animation. All I had was a short career in print visual journalism. I accepted the offer anyway. One reason was that the director of El Mundo's online operation was Mario Tascón, someone I had admired since my college days. Mario had been infographics director of El Mundo between 1991 and 1998. The quality of the work his department put out had inspired publications worldwide. Mario also hired Rafael Höhr, a talented designer who has recently became the graphics director at London's Sunday Times.

Compared to the infographics and visualization wonders you see nowadays in news websites such as The New York Times, The Washington Post, MSNBC, and The Guardian, our efforts at the beginning of the century look crude and naïve. But at the time, they were breakthrough. We were devising new ways of telling stories. I still remember the blast I felt when I learned how to program a very simple calculator of the Body Mass Index for an infographic on stomach-reduction surgery (Figure 9.2), and when I first used audio in a very rough 3D animation (Figure 9.3). Those were good times, indeed.

![](images/53ac0e72b83569ae5bf286a625e94917d98f98cb8dade3e0925ac1e05050fdee.jpg)  
Figure 9.2 Stomach-reduction surgery and Body Mass Index calculator (http://www.elmundo.es/elmundosalud/documentos/2004/02/estomago.html).

![](images/571a4783ddf754e814a34d671735a1253325b2e651e943040b0cf7b6b66223a2.jpg)  
Figure 9.3 NASA's Deep Impact mission. Crashing a probe against a meteorite (http://www.elmundo.es/elmundo/2004/graficos/dic/s4/deepimpact/index.html).

## Early Lessons on Interaction Design

Before 2ooo, those of us who got into interactive news infographics learned by trial and error. Many of us had little idea of the rich tradition of research in related areas such as human-computer interaction and software engineering. As I would later discover, interaction design is not limited to the digital world: Some of the classics in the literature focus on the functionality of physical devices. Learning the basics from them can save you a lot of headaches, so let me take you on a quick tour of the concepts.

The Design of Everyday Things by Donald A. Norman, originally published in 1988, is a perfect starting point. It's not a book about interactive graphics, but about how we deal with common stuff such as door handles and coffee makers. Donald Norman is an advocate of putting the user's needs ahead of the designer's aesthetic concerns. The principles he proposed are directly translatable into guidelines for infographics.

## Visibility

The more visible the functionality of an object, the easier it will be for users to create a mental model of what they can obtain from it. Norman encourages designers to take advantage of“natural mappings” or physical analogies to the real world. If something is important in your graphic, highlight it in such a way that readers can sense its relevance and how it operates.

For instance, if you are designing buttons, make them mimic physical buttons. The first couple of buttons in Figure 9.4 don'tlook like buttons, do they? The second pair is better because it simulates the patterns of highlights and shades of objects in relief. But its functionality is not obvious at first glance. We have to read the words “next” and “previous” to understand what will happen if we click them. An arrow is more effective if what we want someone to intuitively understand what will happen if he clicks on it.

![](images/ec865b762cebc094360bc0794456122920b7bab8902333087ea3fdb5a453ec05.jpg)  
Figure 9.4 If you want your readers to be able to identify buttons in your graphics, make them look like buttons.

The principle of visibility is related to what Norman calls perceived affordances. The shape of an object must visually suggest what it “affords." You can understand this by taking a look at the controls of my bike in Figure 9.5. Its brakes are activated by handles that, due to their curved shape, adapt to my hands, inviting me to pull them. The overall design of the device gives me further clues about how to make it work: sit, put your feet on the pedals, and push them to make that metal serrated wheel rotate. The consequences of this are clear: If you want readers to press, pull, push, or spin virtual objects on a computer screen, design those objects so as to suggest that they are pressable, pullable, pushable, and spinnable.

![](images/c6cedc930203e480509fca37bae4d001528a12b9e7fb19c1e598172de671270f.jpg)  
Figure 9.5 Most of the controls on my bike are intuitively understandable, even the baby seat that I am never able to install without hurting my fingers.

The principle of visibility is relevant not only for the design ofinterfaces, but also for the organization of visual elements in graphic design. Imagine that you are working on a piece on the killing of Osama bin Laden in Abbottabad, Pakistan. You wish to create a step-by-step explanation and include a 3D illustration' of the compound where he lived.

Then you add rollover buttons that readers can use to explore the steps of the operation, as the first two pictures show in Figure 9.6. The buttons are visible. But does this approach make sense? Of course not. If a piece ofinformation is indispensable to understand the whole story, it should always be visible, not hidden behind a layer of interactivity. Unfortunately, this is what happens in many interactive visualizations: Readers are forced to keep clicking to reveal data that should be visible at all times.

## Feedback

For every action, readers should perceive a reaction, a response that indicates that the operation they were trying to achieve has been successful (Figure 9.7). This reaction could be a visual cue, a subtle sound (so long as it's not repetitive and annoying), or a response that appears instantly on screen. If a reader clicks a button and nothing happens immediately, it will seem that the button is not working correctly.

Bin Laden's Compound in Abbottabad, Pakistan  
![](images/ea5e34d97428cd319ba2ae93cbdbcf5909a23934dddc18845f4fd07040c5c4eb.jpg)

Bin Laden's Compound in Abbottabad, Pakistan  
![](images/81a874cbd5f458fe53e36cbb7433cd3df44ad933fd614139754ce28012197b90.jpg)  
Step 3 Osama bin Laden is killed on the third floor of the compound.

Bin Laden's Compound in Abbottabad, Pakistan  
![](images/3dc5cae93ff0c59256d166a9b4d306410e041fd9d9680f24d55b24b0ef2c0482.jpg)  
Step 3 Osama bin Laden is killed on the third floor of the compound.  
Figure 9.6 Two takes on a hypothetical graphic about Bin Laden's death. Does it make sense to force readers to click or roll over the buttons to get important information? Wouldn't it be better to make those steps visible all the time, or make them show up in order, as this is a step-by-step explanation?

![](images/a6cd301bbe93d75b9f8293fd4c8ce82427b28e8709e8d1844f3d06e15e11b65b.jpg)  
Figure 9.7 Make sure that readers receive clues when they interact with your graphic.

## Constraints

Think of an interface as a mediator between users and a goal. As such, interactive graphics designers must think not only about what they will offer their readers, but also how they will orient their navigation. Any infographic can offer just a small amount of interactive possibilities, depending on what we want users to achieve with the graphic or extract from it. To avoid confusion, the designer consciously imposes limits.

Think about a scroll bar, for instance. You can only manipulate it up to a point and in one direction, vertical or horizontal. In Figure 9.8, in one of the infographics included in a big multimedia documentary project made by students of mine at UNC-Chapel Hill, the reader can rotate 3D illustrations of whales to see them from different angles, but only horizontally.

Another example of constraint happens when we disable buttons so readers won't be able to click on them by mistake and miss important information. In Figure 9.9, in an animation that belongs to the same project, the “next” button disappears when it is not needed, suggesting that you have reached the end of a scene.

## Consistency

A rule in traditional graphic design states that entities of similar nature should look alike. That is, elements of the same kind—whether they are headlines, body copy, footnotes, or whatever—should always be designed with the same typefaces, size, and style. The same can be said of the design of interfaces.

It is also advisable to place your buttons in the same screen position, because learning how even the most simple interface works takes time. You don't want to force readers to hunt for the “zoom” button because you’ve moved it to a different location.

![](images/4f0bdabda8afdd05bf9c472325d5cb65da31d447c801806dbb3543de746d5bcf.jpg)  
Figure 9.8 The Great Whales of the Atlantic, by Alicia Parlapiano (UNC-Chapel Hill). This graphic is part of the multimedia documentary South of Here, about the Patagonia region, in South America (http://www.southofhere.org).

![](images/d205dc242a12b4f8fce3b0c16def6bf20c2f6b65c192fc7e3342e3eb312babd6.jpg)  
Figure 9.9 The Ozone Hole, by Wilson Andrews (UNC-Chapel Hill). This graphic is also part of the multimedia documentary South of Here (http://www.southofhere.org).

Interface consistency can also be sustained throughout a series of graphics. For instance, if I put screenshots of some of my old projects for El Mundo side by side, as in Figure 9.1o, you will see that their interfaces are pretty similar. Once a reader learns to navigate one of those graphics, he or she will be able to navigate others with no effort.

## Structuring Interactive and Animated Infographics

In 1996, Ben Shneiderman, a professor of computer science at University of Maryland, defined what he called the Visual Information-Seeking Mantra: “Overview first, zoom and filter, then details on demand." This deceptively simple organizational principle was originally conceived to be used in the visualization of data for analysis, but, taking its meaning in the broad sense, it can be applied to any kind of graphical presentation of facts and phenomena: First, present the most important figures or the most relevant points. Then, allow readers to dig into the information, explore, and come up with their own stories.

Some of your infographics will necessarily be linear; that is, each step of the presentation will depend on understanding the previous one. Think about the visual reconstruction of a terrorist attack or an explanation on some new scientific device. Other graphics will be non-linear, giving readers choices for navigating the information using buttons, scroll bars, and other means. In either case, as shown in Figure 9.1i, you would introduce the topic using a clear headline and a short intro. Don't throw tons of data at readers if you don't explain first what it means.

Interaction designer and consultant Jenifer Tidwell identifies several techniques for navigating and browsing information graphics:3

• Scroll and pan.

• Zoom.

• Open and close.

• Sort and rearrange.

• Search and filter.

MAsA Spece con Hooacn popa aico: Ancts Laroem

![](images/6bdeeb8ce6807cedf1a743a098c1c476b09fe759c4d54e6062026cc2b1975ef9.jpg)  
l'urte: NASA Apenctas Kceco: Pable Gerséors Anerte Curple mail

![](images/d4f6a0aded89ec0642aeade35c2570a053bdc3b4d72c5d68fa164740aa3189e0.jpg)  
Icanng (A( a.k Ioodos) (canag rae Pro, Ccior Aber C'aire le-

![](images/bf3e904c3970e0461d6e6f8292e44b4b9d2f8e59ee0d18eaf1025e014b042d58.jpg)

![](images/6d3f3f441a66629dd3b21e6965454682d1d9f6a4ada91aef8b5f408e76717336.jpg)

![](images/ff05cf57970ce3549f6633582dfa9a3dbb832cc467ce332dd7ef6b3e31613331.jpg)

![](images/ca77e86c20f9ed923f425659f63e82a50261809a9e36655fd85b96eedd5909ce.jpg)  
Figure 9.10 Assorted screenshots of infographics I made for El Mundo, between 2001 and 2005. Because I used a very similar interface for each, readers can navigate each new graphic easily.

![](images/197847eb4f633e0d5fa7c92677279867b0ccc727f1531f132eee37cb4b64fb46.jpg)

![](images/e81a740f32172128b068728bbb95b43eaf10eabdb7f3c3941105e5ead3281cd6.jpg)  
Figure 9.11 Examples of linear and non-linear structure.

## An Altered Landscape

![](images/9b3741a5c61261999c1d75e269bf7ee84a5e4cb9104c4410d82a94be574bb15f.jpg)  
Note: Figures for Obama and McCain may not add up to 100%. Source Daily Kos Elections

Figure 9.12 An Altered Landscape. Reprinted with permission of The Wall Street Journal. Copyright © 2012 Dow Jones & Company, Inc. All Rights Reserved Worldwide (http://online.wsj.com/article/SB10001424052702304444604577338403379964394.html).

You can see almost all of these at work in the interactive graphics in Figures 9.12, 9.13, and 9.14, all published by The Wall Street Journal.

The most common use of the scroll and pan technique is the vertical scroll on a website that allows you to see the part of the page that doesn't fit on the screen. On an interactive map, the pan tool allows you to move around until you find the area of interest. But you can use this simple tool in more creative ways. In Figure 9.12, for instance, the horizontal scroll lets you compare a map of Pennsylvania before and after its districts were redrawn by Republican legislators. The graphic is built on Google Maps, so you can pan around and zoom in and out, in case you are interested in seeing the neighboring states.

Figure 9.13 shows other techniques at work, including the open and close technique. The graphic is a database of ioo counties in the United States with the greatest numbers of veterans of the Afghanistan and Iraq wars. The data is presented on a map and in a table. Focus on the table first. By default, it is organized by veteran population, starting with the largest concentration.

Where Are the Veterans of Iraq and Afghanistan? San Diego, which hosts large Marine Corps and Navy facilities, is home to more Iraq and Afghanistan vets than any other county in the U.S: 38,000 out of 1.4 million who have served in tha wars. See the 100 counties across the U.S. that are home to the most veterans from Operation Enduring Freedom, Operaton iraqi Freedom and Operatíon New Dawn. Seiect a county in tha table to changa the map and see military bases in the area. Click map to see details on bases.  
![](images/eb9ffd7ed2ae9de9cd8b55129a01fa60b027846067eeb0df1232f4f12a546d2f.jpg)  
Figure 9.13 Where Are the Veterans of Iraq and Afghanistan? Reprinted with permission of The Wall Street Journal, Copyright © 2012 Dow Jones & Company, Inc. All Rights Reserved Worldwide (http://online.wsj.com/article/ SB10001424052702304636404577300272621321602.html).

What if you want to see only the veterans in one state? You would have to sort and rearrange the table by clicking on the top tabs. You can reorganize by county, by alphabetical order, by state, or by veteran population. You cannot search for specific counties, though. That would have been very nice, as some readers may be interested in comparing two or more different areas. Although it can be done with the current interface, it would take some work.

In Figure 9.13, you can also open and close new windows. If you click on the counties on the table or on the map, a text box will appear containing the veterans' base names, the military branch they belonged to, and other details.

Figure 9.14 is an interesting case. It is a huge infographic showing how different companies compare in areas such as revenue per employee, net income, and cash. You can add and erase companies from the mix, rearrange them, sort them by industry, and search for one of them. Every time that you complete one of these operations, the line charts on top change their scales to fit the newcomer.

## Recession and Rebound

Most big U.S. companies emerged from the recession more productive, as measured by revenue and net income per employee, end holding more cash. This chart lets you see how individual companies fared on those meesures during the recession and recovery. Employment levels vary across industries, so companing revenue per employee for companies in different industries may not be meaningfut. The trend from 2007 through 2011 may indicate how a company navigated the downtum and its atermath.

![](images/ea70b362cd6c72eb54c75e234fabe4b983a31114c1bf7f5fda21d139187b6e5b.jpg)

<table><tr><td rowspan="2">Previous Next Last First 1 2 3 4 5 Company name</td><td colspan="4">Search names or ticker symbols Click the cotumns to sort, and click in the table</td><td colspan="2">Search:</td></tr><tr><td></td><td>Revenue per</td><td>Net income per</td><td>Net income per</td><td>Cash 2011</td><td>Change in</td></tr><tr><td></td><td>Revenue per employee 2011, in thousands</td><td>employee % change 2007-11</td><td>employee 2011, in thousands</td><td>employee % change 2007-11</td><td></td><td>cash. 2007. 2011.In milllons</td></tr><tr><td>HOST HOTELS &amp; RESORTS INC</td><td>$22,931.51</td><td>1.80%</td><td>$69.77</td><td>-100.00%</td><td>$862</td><td>$309</td></tr><tr><td>HCP INC</td><td>$11,737.32</td><td>87.45%</td><td>$3,665.93</td><td>-4.80%</td><td>$75</td><td>$58</td></tr><tr><td>AMERISOURCEBERGENCORP</td><td>$7.788 11</td><td>34.01%</td><td>$68.60</td><td>65.20%</td><td>$1,826</td><td>$718</td></tr><tr><td>CONOCOPHILLIPS</td><td>$7,746 95</td><td>47.26%</td><td>$417.32</td><td>18.70%</td><td>$8,361</td><td>$4,905</td></tr><tr><td>VALERO ENERGY CORP</td><td>$5,741 82</td><td>46.12%</td><td>$95 25</td><td>-60.80%</td><td>$1,024</td><td>-S1,471</td></tr><tr><td>EXXON MOBIL CORP</td><td>$5,688 54</td><td>17 76%</td><td>$500.12</td><td>-0.50%</td><td>$13,068</td><td>$21,432</td></tr><tr><td>TESORO CORP</td><td>$5,811.67</td><td>40 44%</td><td>$101.11</td><td>-1 70%</td><td>$900</td><td>$877</td></tr><tr><td>VENTAS INC</td><td>$5.380.91</td><td>-63 05%</td><td>$1,111.28</td><td>-79.10%</td><td>$122</td><td>$40</td></tr><tr><td>HEALTH CARE REIT INC</td><td>$4,632.90</td><td>133 42%</td><td>$706 53</td><td>1.10%</td><td>$233</td><td>$203</td></tr><tr><td>MARATHON OII CORP</td><td>441791</td><td>1420 79%</td><td>SARR A?</td><td>561 80%</td><td>C493</td><td>$706</td></tr></table>

Figure 9.14 Recession and Rebound. Reprinted with permission of The Wall Street Journal, Copyright © 2012 Dow Jones & Company, Inc. All Rights Reserved Worldwide (http://online.wsj.com/article/SB10001424052702303772904577332493399116320.html).

## Different Kinds of Interaction

When I started doing online information graphics, I spent quite a bit of time trying to conceptualize the different kinds of interactive experiences my team and I were offering to our readers. We were allowing them to click, scroll, open and close new windows, and move around the scene in some cases. Would it be possible, I wondered, to categorize those techniques based on how the user might experience the interface's capabilities?

Professors Yvonne Rogers, Helen Sharp, and Jennifer Preece provided an answer.⁴ They proposed four broad styles ofinteraction that can coexist in a single website or, in our case, an information graphic or visualization.

## Instruction

In the most basic and common kind of interaction, the user tells the infographic to do something by means of pressing buttons, typing commands, or double-clicking the mouse. Even using this simple style of interaction, you can come up with very creative results. Figure 9.15 offers an example, a segment of a multimedia documentary project I participated in with several of my colleagues and students from UNC-Chapel Hill; the University of Santiago de Compostela, Spain; and the University of Los Andes, Chile.

In the infographic, readers not only see how a traditional Spanish musical instrument—the zanfona—works, but they can also play it. The students who created the graphic interviewed an artisan who designs zanfonas, and then a folk musician who was asked to play every single note with his instrument. The students recorded the sounds and programmed the interactive presentation.

## Conversation

This kind of interaction allows the user to have a dialogue with the presentation, as if he is having a conversation with another real person. It's not something that we see in information graphics and visualization very often, but I envision a future in which I can change the parameters of a calculator such as the one in Figure 9.16 by talking to my cell phone, instead of typing and clicking.

![](images/a3ab6f35b1c0e74151a3dc54a21b721e137b102d6b5c7b896e2552ba2e4b990c.jpg)  
Figure 9.15 The Ancient Way,“Music is in our blood." This infographic allows the viewer to play a traditional Spanish instrument by means of his or her keyboard (http://theancientway.jomc.unc.edu/portal.htm).

Figure 9.16 “Is It Better to Buy or Rent?" One of my all-time favorite New York Times interactive presentations. Try to input your own data into this simulator and have fun comparing them to other scenarios at http://www.nytimes. com/interactive/business/buy-rentcalculator.html.  
![](images/13d31038406dd1a425d65ed17634033941d490728f4cbb2e37896aba34293b90.jpg)

## Is It Better to Buy or Rent?

Whether renting is better than buying depends on many factars, particularly huow fast prices and rents rise and how long yoa stay in yonur home. Compare the costs of larying and renting a hoane in the calculator below. Click the Aovanced serruos button to change smputs such as your rate of return on iovestroents, condo/ccmamon fees and your tax bracket.

![](images/3f5a8ebb39896cb05d11e8d9aba8c899c346a321b4fc2d05b1433bdd572995ac.jpg)

If you stay in your home for 6 years, buying is better.

It will cost you \$10,460 less than renting, an average savings of \$1,743 each year.

## Mehodoiogy

The cotculator keeps a nunmng taéy of he mcst common exparses of ownana and menting. If alro fakes wto aocount something knaw as last cpportunity cpsts — far examr'e the ralurn you could have eamed by imweshng your money tnstead of spending rt on a down payment. The catculator assumes that Iim prolt you wowld have made in your mivestrenls woud da texed as long-em cacital gauns and adusts the botom Iine acconfingly The calculstor tabuleles loet opportunty costs for al parus of the buyng and renSng sioenarios.

<table><tr><td>Buying</td><td>Spent in Heard</td><td>Cumumre spern Srom years 1 to 6</td></tr><tr><td>PUACHASE COSTS</td><td></td><td></td></tr><tr><td>Down peymant</td><td></td><td>34 400</td></tr><tr><td>Clomng corts</td><td></td><td>6,380</td></tr><tr><td>VEARLY COSTS</td><td></td><td></td></tr><tr><td>Montçoga caymanr</td><td>7.988</td><td>47.504</td></tr><tr><td>Anncipal</td><td>2,439</td><td>12,813</td></tr><tr><td>Interest&quot;</td><td>4.543</td><td>34 751</td></tr><tr><td>Candaraammon lees</td><td>0</td><td>à</td></tr><tr><td>Propory tares&quot;</td><td>2.092</td><td>11,S52</td></tr><tr><td>unices</td><td>1325</td><td>7,570 •</td></tr><tr><td>Ronovnbans</td><td>988</td><td>5.533 t</td></tr><tr><td>Mantenance</td><td>968</td><td>5,533</td></tr><tr><td>Nomeower&#x27;s imuranca</td><td>891</td><td>6,091</td></tr><tr><td>LOSTOPPORTUNITYCOSTS</td><td></td><td></td></tr><tr><td>Down paymensinmtual coss</td><td>1.559</td><td>9,170</td></tr><tr><td>Tearly costs</td><td>2510</td><td>7,315 •</td></tr><tr><td>SÉLLING COSTS</td><td></td><td></td></tr><tr><td>Closing costs</td><td></td><td>11.622</td></tr><tr><td>Ramaving amdpai</td><td></td><td>124,787</td></tr><tr><td>T (W any) on pal)</td><td></td><td>0</td></tr><tr><td>Procbets fam rome save</td><td></td><td>-193.709</td></tr><tr><td>YEAR 6 TOTALS</td><td>$18,402</td><td>s13,718</td></tr></table>

## Buying

Purchase costs are the costs you tncur whan you go to the closng for the home you are purchasing This incudes the down payment and typcal dosng costs

Yeariy costs ane recurring monthy or ysarty expenses These ictude morigage payments, condo feas (or other communty Inng lees), nimnovabgn costs, mantanance costs proptty Lanes and homeowner's nsurance Propenty taxes. the Indanest part of the morigage paryment, and in some ceses, a portion of the aommmon charges, are tax deducsbis Tha resulaing tax savngs is acoountand lor in sach Hsm's toteks. The morigage paymant amcunt increases sach year for the larm of the loan becausra the tax cradt shnniks sach year as the interest portar of the payments becorea Emater.

Lost opportunity costs are brackad for the irial purcnuase cools and for te yearty costs. The former wil gvie you an kou of hrov much you could have made tf you had kavested the down poyment instead of buyang your home

Selling costs are the costs ycu incur wnen you go to the cosng for the homse you are seting. Thas inoudas the broker's commission and other fees, as wes as the resmaining pmnopal balance that you pay to your morgaga bare 'Proceeds from home sare' rs the morey tha! you nsoalve from the canson who as buytng your tome This amount is equar tar the value of the home that yoar and as shown as a negasve number since iIis not something that you spand money an, bul rathar,  is money you recewva If your cumulatve buyrg total s neuatve, t actuatly means you huive done vory was you made eoough of  profit thuat not only coveved the cost ol your home, but aíso al ol your yeaty oparatng expensas

<table><tr><td>Renting</td><td>Spentn 6</td><td>Cumuatve spert from years 1 10 6</td></tr><tr><td>NOTIAL RENTING COSTS</td><td></td><td></td></tr><tr><td>Rent deposxt</td><td></td><td>1,100</td></tr><tr><td>Brokarsfte</td><td></td><td>0</td></tr><tr><td>YEARLY COSTS</td><td></td><td></td></tr><tr><td>Rent</td><td>15.302</td><td>e5 383</td></tr><tr><td>Renmer&#x27;s &#x27;nurarde</td><td>202</td><td>1127</td></tr></table>

<table><tr><td>LOSTOPPORTUNITYCOSTE</td><td></td><td></td></tr><tr><td>Rent depostinda costs</td><td>t</td><td>2441</td></tr><tr><td>Yeary ccss</td><td>2.579</td><td>7 424</td></tr><tr><td>LEAVING YOUR RENTAL</td><td></td><td></td></tr><tr><td>Retum of rem depost</td><td></td><td>-1,100</td></tr></table>

## Rending

Intial costes sre the rent sscunty depost and, f apolicabie thet proker's fee.

Yearty costs are the montier nernt and tha cost of renter's inunance

Lost opportunity costs sne calculened euch year for both your inutal costs and your yearty costs

Leaving your nertal s equal lo the rent seaxity decost. hypicatly retumed to a nenter at the end df a leere

By Kerwn Quesy ard Arom Tee Send Feedtact

0r4 wm Mond/sEcy

<table><tr><td></td><td>HoWord V MY/Ron Bas</td><td></td><td>J020091</td><td></td><td></td><td>SteSs gA Sa L BE A</td><td></td><td></td><td></td><td></td><td></td><td>50L/2</td></tr><tr><td>2012 The Now York Tnes Comoes</td><td></td><td>FAMI</td><td>YoNL Ad ChoneE</td><td></td><td colspan="2"></td><td></td><td>FersSe taS Caacs s e Cortac U VtrUn</td><td></td><td></td><td></td><td>Ao</td></tr></table>

## Manipulation

Think of your computer's desktop: You create folders and then drag them around, place them inside other folders, choose their colors, sizes, and even appearance. Generally, we allow manipulation when we let readers change the structure and appearance of what is presented to them so they can achieve certain goals.

Applying this style to infographics can be fun. Figure 9.17, created by my team at El Mundo, offers an example. Back in 2o05, soaring real estate prices in Spain caused such a problem that the government decided it should take action. Thousands of young working couples couldn't move out of their parents' homes because home prices were so steep.

Qué se puede hacer con 25 m²  
![](images/80af031803b765c61b6f5066d2b9536a6fcf0d610b18d740463ac37c5b6826b2.jpg)  
Fuente: Elaboración propia  Gráfico: David Alameda, Xaquin G.V.  e-mail

Figure 9.17 “What You Can Do in 25 Square Meters,’ from El Mundo. Furnish your apartment and see if you and your partner still fit in (http://www.elmundo.es/elmundo/2005/ graficos/abr/s2/casa\_25.html).

The government vetted a plan to invest in the construction of apartments that were between 27o and 39o square feet. Politicians in the opposing party called the idea a joke: It would be hard enough for a single person to live in such a small space, much less a couple, they argued. And what if that couple decides to have children? After all, low fertility is a challenge Spain has faced for the past 2o years.

My colleagues David Alameda and Xaquín González decided that we could engage readers by letting them see for themselves how difficult it is to furnish such a tiny apartment. In the graphic, you select the pieces of furniture you want to buv, and then drag them around until you find an arrangement that lets you walk between the couch and the TV set to reach the bathroom. No easy task, I assure you.

## Exploration

I am not a hardcore videogame player, but I still remember the crazy amount of hours I spent playing Wolfenstein 3D, the 1992 videogame that created the firstperson shooter genre, popularized later by blockbusters such as Doom and Quake. What made that game so addictive was the feeling that you were in charge of the action. You were not represented in the story by a cartoony hero running around on the screen. You were the hero. You held that gun and shot it at hundreds of aggressive (and, yes, cartoony) Nazi bullies.

The kind ofinteraction these games apply is called exploration, and it can be used in information graphics with interesting results. See Figure 9.18, an interactive graphic made by my student Vu Nguyen for a documentary project on the city of Arequipa, in Peru. Arequipa's historical buildings have a very characteristic architectural style, so Vu decided to let readers navigate inside some of them. The 3D models in the graphic can be rotated and, once you enter one of the rooms, you can spin a 36o-degree picture as if you were in the middle of it.

## How to Plan For Interactive Infographics

I often say that a person who admires a lot of people is fortunate, but the person who has the luck of working alongside those whom he admires is privileged. I have been privileged. Many years ago, I was hired by the newspaper I used to read as a college student (El Mundo) and, in the summer of 2o07, I had the opportunity to participate in a project published by the newspaper to which I subscribe to today, The New York Times.

You will learn about The New York Times graphics desk in the next section, so I will skip an in-depth explanation about how this award-winning department functions. To end this chapter, I am going to focus on a specific piece that I helped develop, after having been invited to spend a couple of days in the newsroom by the head of infographics, Steve Duenes. The graphic, shown in Figure 9.19, is an example of what I think is the best way to approach a complex endeavor: Do research, plan, correct, execute, deliver.

![](images/fb82c257e1248452d8dadd460d2d3790ce932a7eb57d738e19e84657e5070449.jpg)  
Figure 9.18 Arequipa's Baroque Architecture, an infographic by Vu Nguyen that is part of the White City Stories student documentary project (http://whitecitystories.jomc.unc.edu/).

My role in this project was to aid with the research, planning, sketching, and storyboarding for a couple of days. Joe Ward, Graham Roberts, Shan Carter, and John Branch designed the graphic after I left. The whole process of putting the animation together took one week.

Spanish tennis player Rafael Nadal was among the highlights of the 2007 U.S. Open. The Times had defned the focus for the graphic before I arrived in New York. Through the years, Nadal had been adapting his game to different kinds of

The Master of Clay Takes Aim at the Fast Courts A look at Rafacl Nadal's approach on threc of thc gamc's surfaccs.

![](images/1f8b139ec1f7e1a6c3a1cd47335d2673a5533c89e94807f8b1e165cf9d5cba8a.jpg)

The Master of Clay Takes Aim at the Fast Courts Alook at Rafael Nadal's approach on three of thc game's surfaces.

![](images/5c399c1f0c7a03285f0ab5bebed2c2be662d620a9f6fa8cb81012153b10bf497.jpg)  
Figure 9.19 “The Master of Clay Takes Aim at the Fast Courts," an infographic on Rafael Nadal and the U.S. Open for The New York Times (http://www.nytimes.com/ interactive/2007/08/25/sports/tennis/20070827\_NADAL\_GRAPHIC.html).

surfaces. In Spain, he became accustomed to clay courts, which are called “slow": When the ball hits the ground, the clay deforms and, because of friction, absorbs a considerable proportion of the ball's momentum (the energy the ball carries, so to speak). On a clay surface, balls bounce off slowly and high, so players tend to use a defensive game and stay behind the baseline.

But the surface at the U.S. Open is a “fast” surface: hard, with a concrete foundation. When the ball hits the ground, the friction is less than on a clay surface. The bounce is lower and much faster, because the amount of momentum the surface absorbs is negligible.

I find that fascinating. Personally, I couldn't care less about sports, something that my Spanish and Brazilian colleagues and basketball-crazed UNC students used to find amusing. I don't even care about soccer. But I do love getting into the scientific, technical side of sports. Working on this graphic, I learned a lot when I interviewed University of Pennsylvania professor Howard Brody. After studying high-energy nuclear physics, Brody started doing research on the physics of sports. He has written three books on the science of tennis.

My phone conversation with Brody was enlightening. While talking to him, I scribbled my thoughts. You can see one of the pages in Figure 9.2o.

The next step was to organize how the information would flow in the infographic; that is, how many steps it would take to explain everything. I drew a very rough storyboard and wrote plenty of notes underneath each frame (Figure 9.21). At the same time, I produced still pictures for a second storyboard, one that would help me visualize what the graphic would look like (Figure 9.22). For those panels, I used Illustrator and Maya, a 3D design tool.

When I saw the project published a few days after I left, I was impressed. The structure was pretty close to the one on the rough storyboard, and the look was similar to the one on the second set of sketches. But the team at the Times had very much improved the original ideas. That's the reward you get when you have the privilege of working alongside such a talented group of people.

![](images/620d6857f9f31ba805692299ef749f6ccf80d3d98eb810e0c9e5cf0ae10e645b.jpg)  
Figure 9.20 One of the many pages that I filled with notes for the project on Rafael Nadal.

![](images/af5c71f3dd2385f365637be3fd7ecd143ac954e6d5fcae183da54d34cc3484a7.jpg)  
Figure 9.21 The first page of the storyboard for the Nadal project.

This is a Headline  
![](images/ebdbae2c491a261f0799c582b5037cbc1045097c1851f6fc749cb3350e89675e.jpg)

This is a Headline  
![](images/6600eff1132aaab03a32e675a1a761861bdd2b2dcb7bf09215d2252044ed450e.jpg)  
Figure 9.22 Two panels of the second storyboard for the Nadal infographic.

![](images/864ed1e960c64387b7d2844572d30266850fccd7be324b8a0caf12a968b9c545.jpg)

![](images/c5b7a26e7b4bfd0d901bafb2f53d5b41ee37728aa61f60c5023598148580da9c.jpg)