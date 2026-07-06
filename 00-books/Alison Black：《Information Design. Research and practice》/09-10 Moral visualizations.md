# Moral visualizations10

## Rule utilitarianism and the design of information graphics

Alberto Cairo

The recent rapid growth of information graphics and visualization has not been accompanied by a solid reflection about the ethical underpinnings of the craft. Attempts to develop a code of ethics, or to define guidelines that professionals can follow, have been tentative and insuficient. This chapter identifies some key points for a discussion of ethics in visualization. Should visualization professionals adopt consequentialist/utilitarist reasoning to guide their decisions, or should they collectively develop their own deontological rules? Should they start from scratch in this endeavour or borrow principles from journalism, engineering, statistics, cartography, and graphic design? Should an ethics of visualization be based on how to represent information to best enlighten readers, or should it also consider how the data itself is gathered and processed?

When the fear of taking responsibility . . . is greater than the fear of causing harm, we stop becoming designers. We become agents of recklessness. (Monteiro 2013, 17 m 40 s)

On 23 December 2012, in the wake of the rampage at Sandy Hook elementary school, in Newtown, Connecticut,1 The Journal News, a  small suburban newspaper in New York state, published an interactive map of small-gun permit holders (Figure 1, overleaf ). The map unleashed a firestorm of outrage,2 so it was removed in January 2013. What remains online is a series of screenshots.3

On the original map, small colour circles revealed the names and addresses of the permit holders in two of the counties the paper covers, Westchester and Rockland. The story accompanying the map explained: ‘About 44,000 people in Westchester, Rockland and Putnam – one out of every 23 adults – are licensed to own a handgun.’ The point was clear: there are too many guns around here.

## WESTCHESTER COUNTY

This map shows pistol permits registered with the Westchester County Clerk's Office. Residents are reguired to renew the permit every five vears. Zoom in and out for more information and click on a dot to see details of a permit

![](images/e4240e80150f2ac10304b1eb91e1a2530547187468b3991af9a380ae05fed35e.jpg)  
Figure 1 A map of small-gun permit holders in NY’s Westchester and Rockland counties.

Stop for a minute and think: did The Journal News make the right decision, considering that this dataset could have been available to any private citizen through a Freedom of Information Act (FOIA) request? I have asked this question many times to diferent audiences in the past two years. I’ve got diferent responses every time. Here’s a summary:

1 Advocates for transparency, technologists, and many engineers think that the act was right just because the data was already public.

2 Experienced journalists think that The Journal News made the wrong decision mainly because the map has no informative value and the data was not put in proper context. It was not reported on, or edited. Kathleen Bartzen-Culver, a professor from the University of Wisconsin-Madison, wrote: ‘Truth does not come from accuracy alone. It comes from accuracy in context. In this case, the critical context is what was missing from the data.’ Among the many inaccuracies Bartzen-Culver identified, the map didn’t display data on large weapons, such as assault rifles, but just on small arm permits.4

3 Some visual journalists and graphics designers feel that there’s a diference between displaying data on a table or database and transforming those data into a map, as the map creates a much more frictionless experience. Besides, they point out, the Journal used an inappropriate level of abstraction: showing the data in all its granularity, every single data point, was wrong. It would have been better to normalize the data, and display a ratio of permit holders on each neighbourhood.

Regardless of what you think about this case, the outrage that The Journal News provoked reveals that there are at least three levels of questions when it comes to evaluate if an act of visualization is morally right or wrong. These are:

• questions about the data we use;

• questions about how we organize, filter, analyse, and publish those data;

• questions about how we visually represent those data.

Based on these three groups of questions, in the next few pages I will make suggestions for future discussions about visualization ethics. This chapter is by no means all-encompassing. Rather, it should be seen as one template – among many possible ones – for what I believe is a necessary and urgent dialogue.

## Normative ethics and rule utilitarianism

Before proceeding, I’d like to explain how I’ll use a few terms.5

Normative ethical thinking consists of thoroughly and rationally analysing what is morally good or bad. It’s possible to group ethical theories into three large groups: duty ethics, virtue ethics, and consequentialism.

Duty ethics, or deontological ethics, is mainly inspired by the works of Immanuel Kant in the eighteenth century. At the risk of abridging in excess – Kant is a notoriously complex philosopher – duty ethics considers an action morally good if it respects one or more unconditional a priori rules.

Kant is famous for his categorical imperative: ‘Act only according to that maxim whereby you can, at the same time, will that it should become a universal law.’ For a Kantian thinker, lying is bad not because of the consequences that a lie could have, but because lying cannot become a universal law. Lying is bad in principle.

Virtue ethics doesn’t deal with the morality of specific actions, but with the personal traits of the people who perform them. It focuses on improving human character, on imbuing people with noble and desirable traits, as a virtuous person is much more likely than a mediocre one to undertake morally good deeds. Following up with the example proposed in the previous paragraphs, honesty is a highly regarded virtue. It’s not possible for a person to be simultaneously virtuous and dishonest. Therefore, lying is not something that consistently virtuous people do.

Consequentialism, as its name suggests, focuses on the outcomes of actions. There are many kinds of consequentialist ethical theories. Utilitarianism is the most common one.

The most famous advocates for utilitarianism were Jeremy Bentham (1748–1832) and John Stuart Mill (1806–1874), who proposed a principle of utility: an action is morally good if it improves the happiness of as many people as possible, while minimizing side efects. For most utilitarians, happiness is much more than a subjective feeling of personal satisfaction in the present moment. Instead, in one of its most modern formulations, happiness depends on ‘the creation of enabling conditions where people are able to pursue well-being in sustainable ways.’6

Again, going back to the example proposed, lying can be considered morally wrong because it generally decreases the well-being of people (a larger or a smaller group of people, depending on the medium we use to spread it). However, a lie may be morally right if it helps protect human well-being. Imagine that you are a Polish citizen during the Nazi occupation in the 1940s. A family of Jews fleeing from German soldiers knocks on your door, and asks for refuge. You hide them in your attic. A few hours later, a German oficer comes over and asks if you’ve seen any Jews around. What would be the morally good thing to do in this case?

Utilitarianism comes in two diferent flavours. The first one is act utilitarianism, which focuses on the morality of individual actions. The earlier formulations of utilitarianism usually fell on this side. The challenge with act utilitarianism, though, is that it may be quite unrealistic, as it forces you to conduct careful evaluations of the consequences of every action, which is absurd. This is not the only critique utilitarianism has received,7 but it’s a compelling one.

Rule utilitarianism, which is the ethical theory that I’m adopting in this chapter, is similar to deontological ethics in the sense that the morality of an action is judged against a set of rules. But these rules are not a priori or absolute. Rule utilitarians devise rules that are more guidelines than inflexible decrees.

For a  rule utilitarian, for instance, telling the truth is morally good, but not because there’s an a priori rule against lying or because being dishonest is unvirtuous. It’s because we have solid evidence to think that lying decreases the well-being of the people who see, read, and believe our lie, so avoiding lies is good behaviour. We can make up a rule out of that.

But lying is not always bad, as we’ve already seen. When telling the truth conflicts with protecting the lives of other people (another ethical rule that we can derive from evidence,) lying is appropriate.

My reasoning in this chapter is therefore based on the following assumptions:

1 Morally good actions are those that increase the well-being of as many people as possible, either directly or indirectly.

2 Accurate, useful information, presented visually in a compelling way, is likely to increase awareness of relevant matters among the audience the visualization is created for, and improve their understanding and knowledge.

3 Good understanding of relevant matters can inform future decisions, so it is likely to increase the chances of people conducting fruitful, happy lives. That is, understanding can have a positive influence on their well-being.

4 Therefore, it is the obligation of the designer of visualizations to create graphics that (a) are aimed at igniting interest in relevant matters, (b) are based on a thorough and accurate depiction of those issues, (c) are built in a way that enables comprehension. To do this, designers ought to base their decisions on available scientific evidence or, in case that this is not available, on judgements derived from their experience and personal observations.

This is the moral rule – in the utilitarian sense – this whole chapter is based on.

## The data which is used

It’s become a  cliché to say that the increasing amount of data available just a mouse click away has the potential to change society for the better. Mayer-Schönberger and Cukier (2013), Aiden and Michel (2013), and Pentland (2014) describe the great insights that so-called ‘big data’ may yield.

On the other hand, authors like Lanier (2013), Morozov (2013), and Greenwald (2014) have warned against the potential risks that digital, datacentric societies face. Designers of visualizations may want to delve into this critical literature, if only to avoid challenges like the one described at the beginning of this chapter. When dealing with data, we need to ponder the pros and cons of the sources we use and the nature of the data itself.

In To save everything, click here (2013), Evgeny Morozov describes the controversy caused by a website called eightmaps.com. In 2008, California voters passed a ballot proposition to amend the state constitution to ban

same-sex marriages. The oficial name of the proposition was deliciously Orwellian: ‘California Marriage Protection Act’.

Since 1974, the state of California collects and publishes the data of any person who donates \$100 or more to political campaigns. An anonymous designer took this dataset and overlaid it on a Google Map (Figure 2) in which anyone could check the name, address, and employer of every single contributor.

![](images/a562c2800277de97735461126b2fb1ae4721877f4713b557102fe9fc3e66bd58.jpg)  
Figure 2  
Proposition 8 Maps, displaying the information of donors who supported a ban on same-sex marriage in California.  
<http://karmicdragonfly.livejournal. com/459515.html>.

If you’re in favour of banning same-sex marriages, this map will surely strike you as insulting and dangerous. In fact, harassment was one of its consequences. Here’s a quote from a New York Times story by Brad Stone:

A college professor from the University of California, San Francisco, wrote a \$100 check in support of Proposition 8 in August, because he said he supported civil unions for gay couples but did not want to change the traditional definition of marriage. He has received many confrontational email messages, some anonymous, since eightmaps listed his donation and employer. One signed message blasted him for supporting the measure and was copied to a dozen of his colleagues and supervisors at the university, he said.8

Even if you’re in favour of allowing gays to marry, you could perhaps carefully reflect on what Evgeny Morozov argues:

The obvious problem with sites like Eightmaps.com is that, in exploiting our rarely examined admiration of transparency, they can be used to suppress virtually any kind of political cause, regardless of where it falls on the liberal– conservative spectrum. (Morozov 2013, 64)

## And here’s The Dallas Morning News’ Scott Mattiza:

What if a radical fundamentalist group gathered the names and home addresses of donors to pro-gay causes, and created an online map to their homes? Or what if anti-abortion radicals created a map to the homes of Planned Parenthood donors? Is that really the way we want to go in this society? I think not.9

What cases like The New York Journal’s map and eightmaps.com suggest is that visualization designers and data journalists must weigh the consequences of their projects against their informative value. Does revealing the addresses of social conservatives or small-gun owners improve the overall well-being of most citizens? Does that information value compensate for the potential harassment (or even physical danger) that the people located in those maps could face? Just think about it, and don’t stick to your initial intuitions, as they’ll probably be tainted by your ideological biases.

## The way data is processed and published

On 18 May 2014, Nicholas Thompson, editor of the online edition of the New Yorker magazine, posted a  chart on Twitter (Figure 3). The chart shows the percentage change in trafic fatalities in the USA, state by state, between 1975 and 2012, and was originally published by the blog Graphzoo. The diferences between states are striking.

Thompson pointed out that Florida and Arizona are clear outliers – an accurate quote is impossible here, as he erased the tweet after some of his followers criticized him for not paying enough attention. The data in the graphic were not controlled for number of motor vehicles, miles driven

Percentage change in trafic fatalities 1975–2012 TOTAL FATALITIES  
![](images/ab7833e8e35266d82e102d6cbaca318e809b2fa8d2a4504ab360d5fe92447c29.jpg)  
Percentage change in trafic fatalities, 1975–2012. Notice that the author used absolute number of deaths, and didn’t control for number of motor vehicles or miles driven per year.  
<http://graphzoo.tumblr.com/ day/2014/05/10>.

## 168 / Alberto Cairo

per year, or other variables that could have made the comparisons much more meaningful.

I took the liberty to download the data displayed in the original chart and recreate it controlling for vehicles and vehicle-miles. These are variables that can easily be found in the Federal Highway Administration’s website. The results are in Figure 4.

Percentage change in trafic fatalities 1975–2012 PER 100,000 VEHICLES

![](images/193d25900d907205d58a001390794a859c36300c119612c3c60d320928e1a954.jpg)

![](images/e644b68d6228d361542eb4b13428c40f89ef92d0f7ebc76c101251ea62f917cf.jpg)

When we control for number of vehicles, fatalities drop drastically in all states, but when you control for millions of vehicle-miles and limit the comparison to 2000–2012 (data for years before 2000 is hard to obtain,) North Dakota becomes the outlier. Why? I don’t know, but I can try to make an informed guess. Perhaps it’s because, since 2008, that state has been attracting thousands of people to apply for jobs in the booming fracking oil drilling industry. More reporting would be required to do a story about this, of course.

These are the problems in this case:

1 The author of the original chart didn’t act in a responsible manner because she (or he) didn’t handle the data correctly and, therefore, she misled the readers of her blog. She (or he) just got a bunch of numbers and rushed to represent them visually, forgetting a crucial lesson in

Figure 4   
Percentage   
change in trafic fatalities per   
100,000 vehicles (1975–2012) and per million annual vehicle-miles   
(2000–2012).   
Charts recreated by the author.

numerical thinking: a dataset encoded in a visualization may be true and accurate, but that doesn’t necessarily imply that the visualization will be truthful.

2 Nicholas Thompson made a mistake by promoting Graphzoo’s chart among his more than 25,000 followers on Twitter. This is not morally wrong per se.

3 The actual morally wrong action Thompson committed was to delete the tweet with no further explanation. Why? First of all, because a good number of Thompson’s followers arguably saw the chart and walked away with the wrong message. Second, because Thompson didn’t immediately issue a correction, pointing out why the original chart was deceitful.

4 The potential for spreading misinformation is much larger nowadays than it used to be. Because of the pervasiveness of social media, both good and bad information wildfires if its presented in a sensational manner.10 Hans Jonas, in his extraordinary The imperative of responsibility (1984) explains that current technologies extend people’s reach so much that a new kind of moral thinking might be necessary. He wasn’t writing exclusively about information technologies, but his thoughts are relevant to our discussion:

The altered, always enlarged nature of human action, with the magnitude and novelty of its works and their impact on man’s global future raises moral issues for which past ethics, geared to the direct dealings of man with his fellowmen within narrow horizons of space and time, has left us unprepared. . . . The lengthened reach of our deeds moves responsibility, with no less than man’s fate for its object, into the center of the ethical stage . . . Its axiom is that responsibility is a correlate of power and must be commensurate with the latter’s scope and that of its exercise. ( Jonas 1984, 10)

A compelling and shocking chart based on bad data handling, being promoted by someone who has more than 25,000 followers in a popular social media platform. Think of the consequences – potentially rampant misinformation – that such actions can have.

## The way data is presented

The past three decades in visualization have been dominated by what I’d like to call ‘the Tuftean consensus’,11 which enshrines accuracy, clarity, and depth as our supreme values. I’m part of this consensus. After all, I’m

## 170 / Alberto Cairo

a  journalist, and two recent books of mine are titled The functional art (2012) and The truthful art (2016).

I  don’t think that visualization is a  fine art, but should think of itself more as a form of engineering. The process of choosing the appropriate structures and visual shapes to encode data ought to be guided by the tasks that we predict that our audience will try to accomplish with the visualizations we create.

Choosing graphic forms shouldn’t depend on personal aesthetic preferences alone, but on what each graphic form can help people see in the data. A visualization that is built based on what we know about how the human brain processes information will likely render beneficial consequences, such as increased understanding on the part of the audience.

A very simple example: data maps are great at displaying geographic patterns. Scatter plots are very efective at revealing the relationship between two quantitative variables. Therefore, if the goal of a visualization is to help people correlate variables with a high degree of precision, the information shouldn’t be presented as two maps side by side, each encoding one variable. A scatter plot will be more adequate.

However, accuracy, clarity, depth, and functionality are not the only values a  visualization designer should strive for. Let me bring back the three components of the moral rule spelled in section two of this chapter. A good visualization is one that:

1 Ignites interest in relevant issues.

2 Is based on a thorough and accurate depiction of those issues.

3 Is built in a way that enables comprehension.

I believe that those, like me, who write constantly about information graphics and are part of the consensus, often emphasize components 2 and 3 while overlooking 1. This is a problem, as an uninterested audience is an audience that won’t read our visualization in the first place, and will consequently miss its valuable content. Engagement precedes decoding.

Let’s go back to Tufte:

The overwhelming fact of data graphics is that they stand or fall on their content, gracefully displayed. Graphics do not become attractive and interesting through the addition of ornamental hatching and false perspective to a few bars . . . No information, no sense of discovery, no wonder, no substance is generated by chartjunk. (Tufte 1983, 121)

Beautiful words which sound truthful enough. At an abstract level, I agree with them –remember, I’m part of the consensus – but I’d beg to suggest some flexibility. Gratuitous special efects or ornaments, when they don’t occlude the information, can certainly generate a sense of wonder and make a graphic more attractive, depending on who the audience is.

In the past decades, the literature about visualization has been dominated by computer scientists (Wilkinson 1999), statisticians (Tufte 1983;

Cleveland 1985; Robbins 2005), cognitive scientists (Ware 2004; Kosslyn 2006), cartographers (MacEachren 1995), and business intelligence experts (Few 2004). It’s only in the last few years we’ve started seeing popular books written by people who can be considered primarily graphic designers (Malamed 2009; Yau 2011 [Yau is also a statistician], Meirelles 2013).

This state of afairs has led to a  professional environment in which the most widely used sets of recommendations to create efective visualizations are perfect when the audience is made of specialists – again: computer scientists, statisticians, cognitive scientists, and business intelligence folks – but perhaps not that appropriate when the visualization is aimed at the general public.

The diference lies in the fact that an audience made of specialists will likely be interested in the content of a  visualization beforehand, if that content is related to their field. A  statistician designing data-rich charts for other statisticians doesn’t need to put a lot of efort in bringing their attention to the content. But if that same statistician is going to publish her charts in a news website or magazine such as Time or Businessweek, she’ll probably need to add something to the mix. The content itself may not be enough to seduce a good part of the audience.

Let me give you a personal example.

I couldn’t care less about sports. I know almost nothing about soccer, baseball, or football. I’m the kind of person who will never stop to read a visualization about the Olympic games unless there’s something in the style of the graphic, or in its headline, that intrigues me. I’m likely to skip over a graphic like Figure 5, no matter how ‘gracefully displayed’ its content is.

## olympic medals won by countries in the four income levels

Below are 165 of the world’s countries that participated in the Summer and Winter Olympics at least one time between 1992 and 2012. Fewer countries – none of the poorest – win medals.

SUMMER OLYMPICS

165 countries   
56,500 participants

WINTER OLYMPICS

46 high-income countries 41 won medals

47 upper middle income countries 33 won medals

41 lower middle income countries 21 won medals

86 countries   
12,500 participants

31 low-income

39 high-income countries 27 won medals

10 won medals

25 upper middle income countries 4 won medals

16 lower middle income countries 2 won medals

6 low-income

None won medals

But this is not what The Washington Post published on its website in February 2014. This is my own version of their graphic. Instead, they designed an eye-catching three-step animation in which little bubbles bounce around and cluster in diferent ways. Spend some time navigating the graphic, and don’t miss its headline, ‘Are the Winter Olympics for the rich?’12

This is graphic that can get my attention, the attention of someone who would never have bothered learning about this topic if it were not for the quirky transitions, the gimmick, the alleged chartjunk. Therefore, the designers accomplished the first goal mentioned at the beginning of this section. They aroused my interest.

On the other hand, the visualization then doesn’t accomplish the third goal, which is to enable useful operations. The critical task here seems to be to perceive the proportion of countries in each income group which won or didn’t win medals. Try to make that comparison when you reach the third step of the animation. It’s really hard.

Herein lies the challenge that every visualization designer faces, then: how to make a graphic visually alluring without compromising its structure, respecting the integrity of the information, and designing it as a tool for understanding? In a print graphic this challenge can be dificult to overcome, as space is limited, so the priority should always be presenting the information as accurately and clearly as possible. Still, there are strategies the designer can use to make visualizations charming. A small pictogram or illustration that doesn’t get in the way of the data; a riveting headline; a surprising choice of style. If well handled, none of those will necessarily distract readers from the content.

Why do you think it is that The Economist titles a chart ‘Boozing it up when it could just call it ‘Alcohol consumption in selected countries, 2010, litres per adult’? Which one would make you stop and take a look at the chart?13

The analogy with written communication is not gratuitous. Journalists don’t write in the classic,14 matter-of-factly, sententious prose Tufte favours, always seeking just clarity, eficiency, and transparency. They often borrow techniques from fiction literature, they play with words, composition, and style. These don’t always contribute to clarity. In fact, they may even make the text a bit less eficient, from a functional standpoint. Should we think that those techniques will invariably lead to copyjunk, then? Perhaps not, as they do contribute to making stories appealing and pleasant to read – for a certain kind of audience, at least. They are valuable, if they don’t put accuracy and clarity at too much risk.

The balance between generalized visual appeal and clarity/eficiency is much easier to achieve in interactive visualizations. There’s not a reason why we cannot use both Figure 5 and Figure 6, combined into a single project. The bouncing bubbles can entice readers to the graphic; when the bubbles stack side by side, as in Figure 5, they let readers extract useful information.

I’ve called this approach ‘the many-faced infographic’,15 explaining that displaying the same data in multiple graphic forms – maps, charts, diagrams, etc. – can be a worthy strategy, as each of those shapes will let people see something diferent in the data. The consequence? They will be better informed, after having been attracted by the visualization at a visceral level. It’s hard to think of a better reward a designer can receive. Even better, by creating a visual device that both raises awareness of relevant matters and improves understanding and knowledge, the designer will be acting in a morally correct way.

15 ‘The many-faced infographic: Brooklyn, elephants, and the visualization of data’. <http://www.peachpit.com/articles/article.aspx?p=2153471>.

## References

Aiden, Erez, and Jean-Baptiste Michel. 2013. Uncharted: big data as a lens on human culture. New York: Riverhead.

Cairo, Alberto. 2012. The functional art: an introduction to information graphics and visualization. San Francisco: New Riders.

Cairo, Alberto. 2016. The truthful art: data, charts, and maps for communication. San Fransisco: New Riders.

Cleveland, William S. 1985. The elements of graphing data. Monterey, CA: Wadsworth.

Few, Stephen. 2004. Show me the numbers: designing tables and graphs to enlighten. Oakland, CA: Analytics.

Greene, Joshua David. 2013. Moral tribes: emotion, reason, and the gap between us and them. New York: Penguin.

Greenwald, Glenn. 2014. No place to hide: Edward Snowden, the NSA, and the US surveillance state. New York: Metropolitan Books.

Harris, Sam. 2010. The moral landscape: how science can determine human values. New York: Free.

Heath, Chip, and Dan Heath. 2007. Made to stick: why some ideas survive and others die. New York: Random House.

Jonas, Hans. 1984. The imperative of responsibility: in search of an ethics for the technological age. Chicago and London: University of Chicago Press.

Karabell, Zachary. 2014. The leading indicators: a short history of the numbers that rule our world. New York: Simon & Schuster.

Kosslyn, Stephen M. 2006. Graph design for the eye and mind. New York: Oxford University Press.

Lanier, Jaron. 2013. Who owns the future? New York: Simon & Schuster.

MacEachren, Alan M. 1995. How maps work: representation, visualization, and design. New York and London: The Guilford Press.

Malamed, Connie. 2009. Visual language for designers: principles for creating graphics that people understand. Beverly, MA: Rockport.

Meirelles, Isabel. 2013. Design for information: an introduction to the histories, theories, and best practices behind ef ective information visualizations. Beverly, MA: Rockport.

Mayer-Schönberger, Viktor, and Kenneth Cukier. 2013. Big data: a revolution that will transform how we live, work, and think. Boston, MA: Eamon Dolan/Houghton Miflin Harcourt.

Morozov, Evgeny. 2013. To save everything, click here: the folly of technological solutionism. New York: PublicAfairs.

Monteiro, Mike. 2013. ‘Webstock ’13: Mike Monteiro – how designers destroyed the world.’ Talk at Webstock ’13, 11–15 February. Video: <http://www.webstock.org.nz/talks/ how-designers-destroyed-the-world/>.

Parfit, Derek. 2011. On what matters. Two volumes. Edited and introduced by Samuel Schefler. Oxford: Oxford University Press.

Pentland, Alex. 2014. Social physics: how good ideas spread – the lessons from a new science. New York: Penguin Press.

## 174 / Alberto Cairo

Poel, Ibo van de, and Lambè r Royakkers. 2011. Ethics, technology, and engineering: an introduction. Malden, MA: Wiley-Blackwell.

Robbins, Naomi B. 2005. Creating more ef ective graphs. Hoboken, NJ: John Wiley.

Singer, Peter. 1979. Practical ethics. Cambridge: Cambridge University Press.

Tufte, Edward R. 1983. The visual display of quantitative information. Cheshire, CT.: Graphics Press.

Ware, Colin. 2004. Information visualization: perception for design. 2nd edn. San Francisco: Morgan Kaufmann.

Wilkinson, Leland. 1999. The grammar of graphics. New York: Springer.

Yau, Nathan. 2011. Visualize this: the FlowingData guide to design, visualization, and statistics. Indianapolis, IN: Wiley.

Part 2

## Theoretical approaches

![](images/8a2e7ce9fccceba56a682907b9bb02f6fc8c145eb9453bd0c3f6a9f79ee499e8.jpg)