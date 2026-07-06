# Chapter 1. Don’t make me think!

KRUG’S FIRST LAW OF USABILITY

Michael, why are the drapes open?

—KAY CORLEONE IN THE GODFATHER, PART II

People often ask me:

“What’s the most important thing I should do if I want to make sure my site or app is easy to use?”

The answer is simple. It’s not “Nothing important should ever be more than two clicks away” or “Speak the user’s language” or “Be consistent.”

It’s...

## “Don’t make me think!”

For as long I can remember, I’ve been telling people that this is my first law of usability.

It’s the overriding principle—the ultimate tie breaker when deciding whether a design works or it doesn’t. If you have room in your head for only one usability rule, make this the one.

For instance, it means that as far as is humanly possible, when I look at a Web page it should be self-evident. Obvious. Self-explanatory.

I should be able to “get it”—what it is and how to use it—without expending any effort thinking about it.

Just how self-evident are we talking about?

Well, self-evident enough, for instance, that your next door neighbor, who has no interest in the subject of your site and who barely knows how to use the Back button, could look at your Home page and say, “Oh, it’s a \_.” (With any luck, she’ll say, “Oh, it’s a \_\_\_\_\_. Great!” But that’s another subject.)

Think of it this way:

When I’m looking at a page that doesn’t make me think, all the thought balloons over my head say things like “OK, there’s the\_\_\_\_\_. And that’s a \_\_\_\_\_. And there’s the thing that I want.”

![](images/298e151922644233102022215d35651646ccdc464d6d49fbea10c5e853a7a550.jpg)

On the left of the page, list of product categories are displayed with accessories selected and the user thinks "OK. This looks like the product categories..." The content pane displays different computer deals and accessories and the user thinks "...and these are today's special deals." Laptops, bags & Cases and Monitors are labeled with the user's thought "Laptops, Memory…There it is: Monitors. Click."

But when I’m looking at a page that makes me think, all the thought balloons over my head have question marks in them.  
![](images/cd891b65b12872b6c3747631433ba3832c7c0c7c28667ea1302ac16fee9bfc12.jpg)  
In the webpage, the user looks at the content and thinks "Hmm. Pretty busy. Where should I start?" In the content, the user looks at a link and thinks "Hmm. Why did they

call it that?" The user looks at two sections titled "Commentary" and "Other Top   
Stories" and thinks "Those two links seem like they're the same thing. Are they really?" The user looks at "Commentary" section and thinks "Can I click on that?" The user   
looks at a dropdown box with "Stock Quotes" selected and thinks "Why did they put that there?" On the left, the user looks at a list of links given and thinks "Is that the navigation? Or is that it over there?"

When you’re creating a site, your job is to get rid of the question marks.

## Things that make us think

All kinds of things on a Web page can make us stop and think unnecessarily. Take names, for example. Typical culprits are cute or clever names, marketing-induced names, company-specific names, and unfamiliar technical names.

For instance, suppose a friend tells me that XYZ Corp is looking to hire someone with my exact qualifications, so I head off to their Web site. As I scan the page for something to click, the name they’ve chosen for their job listings section makes a difference.

![](images/1afa5a85e8a17deadbb55877ea51c61e054803f24c6b87c7a4dd44d662d9c87b.jpg)

At the left section, Jobs button is shown and the user thinks "Jobs! Click." In the middle section,

Employment Opportunities button is shown and the user thinks "Hmm. [Milliseconds of thought] Jobs! Click." In the last section, a button "Job-o-Rama" is displayed and the user thinks "Hmm. Could be Jobs. But it sounds like more than that. Should I click or keep looking?"

Note that these things are always on a continuum somewhere between “Obvious to everybody” and “Truly obscure,” and there are always tradeoffs involved.

For instance, “Jobs” may sound too undignified for XYZ Corp, or they may be locked into “Jobo-Rama” because of some complicated internal politics or because that’s what it’s always been called in their company newsletter.<sup>1</sup> My main point is that the tradeoffs should usually be skewed further in the direction of “Obvious” than we think.

<sup>1</sup> There’s almost always a plausible rationale—and a good, if misguided, intention—behind every usability flaw.

Another needless source of question marks over people’s heads is links and buttons that aren’t obviously clickable. As a user, I should never have to devote a millisecond of thought to whether things are clickable—or not.

![](images/ecaee91df0878ec1cd838368ec13865a28ba29b198be0b68f979e93dd9db9171.jpg)

At the left section, Report button is shown and the user thinks "Click." In the middle section, a text "Report" is shown in bold and the user thinks "Hmm. [Milliseconds of thought] I guess that's the link. Click." In the last section a text "Report" is shown in non-bold font and the user thinks "Hmm. Does that do anything?"

You may be thinking, “Well, it really doesn’t matter that much. If you click or tap it and nothing happens, what’s the big deal?”

The point is that every question mark adds to our cognitive workload, distracting our attention from the task at hand. The distractions may be slight but they add up, especially if it’s something we do all the time like deciding what to click on.

And as a rule, people don’t like to puzzle over how to do things. They enjoy puzzles in their place—when they want to be entertained or diverted or challenged—but not when they’re trying to find out what time their dry cleaner closes. The fact that the people who built the site didn’t care enough to make things obvious—and easy—can erode our confidence in the site and the organization behind it.

Another example from a common task: booking a flight.

![](images/05ee3384a5e0d012e22d50ea40778c5d593b92b20477014b092538df7d357de3.jpg)

IIn the first section, FROM option with City or Airport field and Depart date field and TO option with City or Airport field and Return date field. The user thinks "Let's see. "City or Airport." I'll put in the city names." In the next section, "bos" is entered in the "FROM" field with the suggestion box displaying "Boston, MA, US (BOS)" and the user thinks "Types "bos." Oh, good. It knows Boston. Picks Boston from the dropdown." In the next section, "BOS" is

shown in the "FROM" field and the user thinks "But why does it just put BOS after I pick   
Boston?" In the next section, "ny" is entered in the "TO" field and the user thinks "I'm sure it'll   
know "ny"… Types "ny" and fills in dates, then clicks "Find Flights." In the last section, "ny" is   
entered in the "TO" field with an error message "Please enter a valid 'TO' City or Airport code" and the user thinks "Why doesn't it recognize New York?"

Granted, most of this “mental chatter” takes place in a fraction of a second, but you can see that it’s a pretty noisy process, with a lot of question marks. And then there’s a puzzling error at the end.

Another site just takes what I type and gives me choices that make sense, so it’s hard to go wrong.

![](images/546db259606d0d106dc2da30fd6262dc81b5d56071ec8e2869247b79eba0789f.jpg)

In the first section, "bos" is entered in "FROM" field with the suggestion box displaying choices of airports and train stations and the user thinks "Starts typing "bos" and gets a list of choices." In the next section, "BOS- Boston Logan International" is selected in the "FROM" field, "ny" is entered in "TO" field with the suggestion box displaying few choices and the user thinks "Starts typing "ny" and gets a list of choices." In the last section, "NYC - New York City" is selected in the "TO" field and the user thinks "Good."

No question marks. No mental chatter. And no errors.

I could list dozens of things that users shouldn’t spend their time thinking about, like

Where am I?

Where should I begin?

Where did they put \_\_\_\_\_?

What are the most important things on this page?

Why did they call it that?

Is that an ad or part of the site?

But the last thing you need is another checklist to add to your stack of design checklists. The most important thing you can do is to understand the basic principle of eliminating question marks. When you do, you’ll begin to notice all the things that make you think in the sites and apps you use. And eventually you’ll learn to recognize and avoid them in the things you’re building.

## You can’t make everything self-evident

Your goal should be for each page or screen to be self-evident, so that just by looking at it the average user<sup>2</sup> will know what it is and how to use it. In other words, they’ll “get it” without having to think about it.

<sup>2</sup> The actual Average User is kept in a hermetically sealed vault at the International Bureau of Standards in Geneva. We’ll get around to talking about the best way to think about the “average user” eventually.

Sometimes, though, particularly if you’re doing something original or groundbreaking or something that’s inherently complicated, you have to settle for self-explanatory. On a selfexplanatory page, it takes a little thought to “get it”—but only a little. The appearance of things (like size, color, and layout), their well-chosen names, and the small amounts of carefully crafted text should all work together to create a sense of nearly effortless understanding.

Here’s the rule: If you can’t make something self-evident, you at least need to make it selfexplanatory.

## Why is all of this so important?

Oddly enough, not for the reason people usually cite:

![](images/d187a62e4238a5f0f9dc54f4269b37953e490f427a894d80c86018dab68f8494.jpg)

It’s true that there’s a lot of competition out there. Especially in things like mobile apps, where there are often many readily available (and equally attractive) alternatives, and the cost of changing horses is usually negligible (99 cents or even “Free”).

But it’s not always true that people are fickle. For instance:

They may have no choice but to stick with it, if it’s their only option (e.g., a company intranet, or their bank’s mobile app, or the only site that sells the rattan they’re looking for).

You’d be surprised at how long some people will tough it out on sites that frustrate them, often blaming themselves and not the site. There’s also the “I’ve waited ten minutes for this bus already, so I may as well hang in a little longer” phenomenon.

Besides, who’s to say that the competition will be any less frustrating?

## So why, then?

Making every page or screen self-evident is like having good lighting in a store: it just makes everything seem better. Using a site that doesn’t make us think about unimportant things feels effortless, whereas puzzling over things that don’t matter to us tends to sap our energy and enthusiasm—and time.

But as you’ll see in the next chapter when we examine how we really use the Web, the main reason why it’s important not to make me think is that most people are going to spend far less time looking at the pages we design than we’d like to imagine.

As a result, if Web pages are going to be effective, they have to work most of their magic at a glance. And the best way to do this is to create pages that are self-evident, or at least selfexplanatory.

## Chapter 2. How we really use the Web

## SCANNING, SATISFICING, AND MUDDLING THROUGH

Why are things always in the last place you look for them? Because you stop looking when you find them!

—CHILDREN’S RIDDLE

In all the time I’ve spent watching people use the Web, the thing that has struck me most is the difference between how we think people use Web sites and how they actually use them.

When we’re creating sites, we act as though people are going to pore over each page, reading all of our carefully crafted text, figuring out how we’ve organized things, and weighing their options before deciding which link to click.

What they actually do most of the time (if we’re lucky) is glance at each new page, scan some of the text, and click on the first link that catches their interest or vaguely resembles the thing they’re looking for. There are almost always large parts of the page that they don’t even look at. We’re thinking “great literature” (or at least “product brochure”), while the user’s reality is much closer to “billboard going by at 60 miles an hour.”

![](images/ab443a4ee21ccb1156e80eb8c7a04f7922b90306c9c0f32700e539108ed6267f.jpg)

In the first page, sections at the top are labeled "Read," middle of the page labeled "[Pause for reflection]," and bottom of the page is labeled "Finally. Click on carefully chosen link." In the

second page, the top section is labeled "Look around feverishly for anything that a) is interesting, or vaguely resembles what you're looking for, and b) is clickable" and the middle   
section is labeled "As soon as you find a halfway-decent match, click. If it doesn't pan out, click   
the Back button and try again." In the first page, zigzag lines representing the reading pattern of   
the user are shown throughout the text. In the second page, only a few areas are covered by the zigzag lines.

As you might imagine, it’s a little more complicated than this, and it depends on the kind of page, what the user is trying to do, how much of a hurry she’s in, and so on. But this simplistic view is much closer to reality than most of us imagine.

It makes sense that we picture a more rational, attentive user when we’re designing pages. It’s only natural to assume that everyone uses the Web the same way we do, and—like everyone else —we tend to think that our own behavior is much more orderly and sensible than it really is. If you want to design effective Web pages, though, you have to learn to live with three facts about real-world Web use.

## FACT OF LIFE #1: We don’t read pages. We scan them.

One of the very few well-documented facts about Web use is that people tend to spend very little time reading most Web pages. Instead, we scan (or skim) them, looking for words or phrases that catch our eye.

The exception, of course, is pages that contain documents like news stories, reports, or product descriptions, where people will revert to reading—but even then, they’re often alternating between reading and scanning.

Why do we scan?

We’re usually on a mission. Most Web use involves trying to get something done, and usually done quickly. As a result, Web users tend to act like sharks: They have to keep moving, or they’ll die. We just don’t have the time to read any more than necessary.

We know we don’t need to read everything. On most pages, we’re really only interested in a fraction of what’s on the page. We’re just looking for the bits that match our interests or the task at hand, and the rest of it is irrelevant. Scanning is how we find the relevant bits.

We’re good at it. It’s a basic skill: When you learn to read, you also learn to scan. We’ve been scanning newspapers, magazines, and books—or if you’re under 25, probably reddit, Tumblr, or Facebook—all our lives to find the parts we’re interested in, and we know that it works.

The net effect is a lot like Gary Larson’s classic Far Side cartoon about the difference between what we say to dogs and what they hear. In the cartoon, the dog (named Ginger) appears to be listening intently as her owner gives her a serious talking-to about staying out of the garbage. But from the dog’s point of view, all he’s saying is “blah blah GINGER blah blah blah blah GINGER blah blah blah.”

What we see when we look at a page depends on what we have in mind, and it’s usually just a fraction of what’s there.

![](images/ebeca0bd549dbfe45c0a1d268b51011317a1969c2be0dd38acd2bf54bfa969b7.jpg)

In all the pages, the homepage of biztravel.com is shown. In the first page, none of the text is blurred. In the second page, all the text is blurred except the options for booking a trip and vacation and the associated information. The user thinks “I want to buy a ticket.” In the last page, all the text is blurred except the “Track My Miles” option and associated information. The user thinks “How do I check my frequent flyer miles?”

Like Ginger, we tend to focus on words and phrases that seem to match (a) the task at hand or (b) our current or ongoing personal interests. And of course, (c) the trigger words that are hardwired into our nervous systems, like “Free,” “Sale,” and “Sex,” and our own name.

## FACT OF LIFE #2: We don’t make optimal choices. We satisfice.

When we’re designing pages, we tend to assume that users will scan the page, consider all of the available options, and choose the best one.

In reality, though, most of the time we don’t choose the best option—we choose the first reasonable option, a strategy known as satisficing.<sup>1</sup> As soon as we find a link that seems like it might lead to what we’re looking for, there’s a very good chance that we’ll click it.

<sup>1</sup> Economist Herbert Simon coined the term (a cross between satisfying and sufficing) in Models of Man: Social and Rational (Wiley, 1957).

I’d observed this behavior for years, but its significance wasn’t really clear to me until I read Gary Klein’s book Sources of Power: How People Make Decisions.

Klein spent many years studying naturalistic decision making: how people like firefighters, pilots, chessmasters, and nuclear power plant operators make high-stakes decisions in real situations with time pressure, vague goals, limited information, and changing conditions.

![](images/8e37dc808c5cf48f571a78fd698b19c3c61eb2053fbbdfe91d5b344074019752.jpg)

Klein’s team of observers went into their first study (of field commanders at fire scenes) with the generally accepted model of rational decision making: Faced with a problem, a person gathers information, identifies the possible solutions, and chooses the best one. They started with the hypothesis that because of the high stakes and extreme time pressure, fire captains would be able to compare only two options, an assumption they thought was conservative.

As it turned out, the fire commanders didn’t compare any options. They took the first reasonable plan that came to mind and did a quick mental test for possible problems. If they didn’t find any, they had their plan of action.

So why don’t Web users look for the best choice?

We’re usually in a hurry. And as Klein points out, “Optimizing is hard, and it takes a long time. Satisficing is more efficient.”

There’s not much of a penalty for guessing wrong. Unlike firefighting, the penalty for guessing wrong on a Web site is usually only a click or two of the Back button, making satisficing an effective strategy. (Back is the most-used button in Web browsers.)

Weighing options may not improve our chances. On poorly designed sites, putting effort into making the best choice doesn’t really help. You’re usually just as well off going with your first guess and using the Back button if it doesn’t work out.

Guessing is more fun. It’s less work than weighing options, and if you guess right, it’s faster. And it introduces an element of chance—the pleasant possibility of running into something surprising and good.

Of course, this is not to say that users never weigh options before they click. It depends on things like their frame of mind, how pressed they are for time, and how much confidence they have in

the site.

## FACT OF LIFE #3: We don’t figure out how things work. We muddle through.

One of the things that becomes obvious as soon as you do any usability testing—whether you’re testing Web sites, software, or household appliances—is the extent to which people use things all the time without understanding how they work, or with completely wrong-headed ideas about how they work.

Faced with any sort of technology, very few people take the time to read instructions. Instead, we forge ahead and muddle through, making up our own vaguely plausible stories about what we’re doing and why it works.

It often reminds me of the scene at the end of The Prince and the Pauper where the real prince discovers that the look-alike pauper has been using the Great Seal of England as a nutcracker in his absence. (It makes perfect sense—to him, the seal is just this great big, heavy chunk of metal.)

![](images/21dbdb30d76ea812ead44de8e1f488b9c7032d58b76b26929c62416acb4dac62.jpg)  
The Prince and the Pauper (Classics Illustrated)

At the top, a text box reads: AND THEN THERE WAS ONE MORE POINT TO CLEAR UP. At the top, a text box reads: AND THEN THERE WAS ONE MORE POINT TO CLEAR UP.

A kid on the left says “One thing puzzles me, Tom. How did you happen to remember the location of the Great Seal?” The kid on the right says “I used it every day without knowing what it was, your Majesty! It was a handy nut-cracker.” A text box at the bottom reads: “THE END.”

And the fact is, we get things done that way. I’ve seen lots of people use software, Web sites, and consumer products effectively in ways that are nothing like what the designers intended. Take the Web browser, for instance—a crucial part of Internet use. To people who build Web sites, it’s an application that you use to view Web pages. But if you ask users what a browser is, a surprisingly large percentage will say something like “It’s what I use to search...to find things” or “It’s the search engine.” Try it yourself: ask some family members what a Web browser is. You may be surprised.

Many people use the Web extensively without knowing that they’re using a browser. What they know is you type something in a box and stuff appears.<sup>2</sup> But it doesn’t matter to them: They’re muddling through and using the thing successfully.

<sup>2</sup> Usually a box with the word “Google” next to it. A lot of people think Google is the Internet.

And muddling through is not limited to beginners. Even technically savvy users often have surprising gaps in their understanding of how things work. (I wouldn’t be surprised if even Mark Zuckerberg and Sergey Brin have some bits of technology in their lives that they use by muddling through.)

Why does this happen?

It’s not important to us. For most of us, it doesn’t matter to us whether we understand how things work, as long as we can use them. It’s not for lack of intelligence, but for lack of caring. It’s just not important to us.<sup>3</sup>

<sup>3</sup> Web developers often have a particularly hard time understanding—or even believing—that people might feel this way, since they themselves are usually keenly interested in how things work.

If we find something that works, we stick to it. Once we find something that works—no matter how badly—we tend not to look for a better way. We’ll use a better way if we stumble across one, but we seldom look for one.

It’s always interesting to watch designers and developers observe their first usability test. The first time they see a user click on something completely inappropriate, they’re surprised. (For instance, when the user ignores a nice big fat “Software” button in the navigation bar, saying something like, “Well, I’m looking for software, so I guess I’d click here on ‘Cheap Stuff’ because cheap is always good.”) The user may even find what he’s looking for eventually, but by then the people watching don’t know whether to be happy or not.

The second time it happens, they’re yelling “Just click on ‘Software’!” The third time, you can see them thinking: “Why are we even bothering?”

And it’s a good question: If people manage to muddle through so much, does it really matter whether they “get it”? The answer is that it matters a great deal because while muddling through may work sometimes, it tends to be inefficient and error-prone.

On the other hand, if users “get it”:

There’s a much better chance that they’ll find what they’re looking for, which is good for them and for you.

There’s a better chance that they’ll understand the full range of what your site has to offer —not just the parts that they stumble across.

You have a better chance of steering them to the parts of your site that you want them to see.

They’ll feel smarter and more in control when they’re using your site, which will bring them back. You can get away with a site that people muddle through only until someone builds one down the street that makes them feel smart.

## If life gives you lemons...

By now you may be thinking (given this less than rosy picture of your audience and how they use the Web), “Why don’t I just get a job at the local 7-Eleven? At least there my efforts might be appreciated.”

## So, what’s a girl to do?

I think the answer is simple: If your audience is going to act like you’re designing billboards, then design great billboards.

## Chapter 3. Billboard Design 101

## DESIGNING FOR SCANNING, NOT READING

If you / Don’t know / Whose signs / These are You can’t have / Driven very far / Burma-Shave!

—SEQUENCE OF ROADSIDE BILLBOARDS PROMOTING SHAVING CREAM, CIRCA 1935

Faced with the fact that your users are whizzing by, there are some important things you can do to make sure they see and understand as much of what they need to know—and of what you want them to know—as possible:

Take advantage of conventions

Create effective visual hierarchies

Break pages up into clearly defined areas

Make it obvious what’s clickable

Eliminate distractions

Format content to support scanning

## Conventions are your friends

One of the best ways to make almost anything easier to grasp in a hurry is to follow the existing conventions—the widely used or standardized design patterns. For example:

Stop signs. Given how crucial it is that drivers see and recognize them at a glance, at a distance, in all kinds of weather and lighting conditions, it’s a really good thing that all stop signs look the same. (Some of the specifics may vary from country to country, but overall they’re remarkably consistent around the world.)

![](images/767e1e5b422f41ca1eb3fd8bd8a40302cd75ba658b99fd5019147f7a7b42e74b.jpg)

The convention includes a distinctive shape, the word for “Stop,” a highly visible color that contrasts with most natural surroundings, and standardized size, height, and location.

Controls in cars. Imagine trying to drive a rental car if the gas pedal wasn’t always to the right of the brake pedal, or the horn wasn’t always on the steering wheel.

In the past twenty years, many conventions for Web pages have evolved. As users, we’ve come to have a lot of expectations about

Where things will be located on a page. For example, users expect the logo identifying the site to be in the top-left corner (at least in countries where reading is left-to-right) and the primary navigation to be across the top or down the left side.

How things work. For example, almost all sites that sell products use the metaphor of a shopping cart and a very similar series of forms for specifying things like your method of payment, your shipping address, and so on.

How things look. Many elements have a standardized appearance, like the icon that tells you it’s a link to a video, the search icon, and the social networking sharing options.

![](images/23f433da09b33b0bdf381275c3062f8fb575410fd125651ca22c228cf81c52ee.jpg)

Conventions have also evolved for different kinds of sites—commerce, colleges, blogs, restaurants, movies, and many more—since all the sites in each category have to solve the same set of problems.

![](images/1df3aa0651cf707ec52b0f6dca828171c12bc3f9a3d1e955ffdbe1a068e46ab7.jpg)  
SomeSlightlyIrregular.com  
Below the header, links are shown for navigation. At the top right, a search box is placed. On the left, content is shown. At the bottom, comments section is given. On the right, categories, archives and other additional information are given.

![](images/eea467179c285abf9dafae8f5a60496630046d1fb3d7776c9eed8ff57e7a1f17.jpg)  
cityislandmovie.com  
At the top, links are shown for navigation. At the center, content is shown. At the bottom, additional information is given.

These conventions didn’t just come out of thin air: They all started life as somebody’s bright idea. If an idea works well enough, other sites imitate it and eventually enough people have seen it in enough places that it needs no explanation.

When applied well, Web conventions make life easier for users because they don’t have to constantly figure out what things are and how they’re supposed to work as they go from site to site.

News10アラファ外ト元議長の骨からポロニウム検出。暗殺の可能性高まる11/0704:20

天気

連続動画

注目キーワード[メニュ一表示問题][みず于暴力団融资][原発][米盗聴疑惑]

NEW「三越伊勢丹」も不適切表示、他の百貨店(にも拡大

![](images/c1c5d267c91782c2d3092f8b4989a5dc2646b375f3dad70662c5eaadb23d93ec.jpg)

大手百貨店の三越伊勢丹ホールディングスは、グルーブの百貨店などにあるレストラン14店で、メニューと違う食材を使った料理を提供していたことを明らかしました。不適切な表示は、小田急、そごうなどの百貨店にも広がっています。

##

ニュ-ス索

##

![](images/a6eb3e832e568267900383f425b91383bc01454d41d6240aaee29fb5730d9f60.jpg)

## 2TBSニュース番組ダイジェスト配信中

![](images/592655f69f2da9a438ac0bf6149edcd828f4b2c9bfd0a7b1dc0d53cfeb3b271d.jpg)

## NEW日本人初の船長·若田さん、きよう宇宙へ

![](images/d7b16659b15af976e78137f2a4593ea032454272692732d17e412ab90d56b93f.jpg)

日本人で初めて国際宇宙ステーションの船長を務める若田光一さんが、日本時間7日午後の...

## NEW猪木議員、金正恩氏の後見人·張成沢氏と会談

![](images/12939ee18440df690a47a0a3b5f5ae625308dc9cd38236d38489d2b85f9650c3.jpg)

北朝鲜を訪問中のアン外二才猪木参議院完議員らが、金正恩(キム・ジョン)第一書記の.

## NEW「特定秘密保議法案」きょうから国会審議

![](images/4db90ad6976ace6ebf35a7931061a0e55ac7230bca01b88141db244a1c489bd4.jpg)

![](images/7304dd251e12079ccbc24524f1b0f294c0984d8d872b25122eaf1391a38cc293.jpg)

政府が指定する特定秘密を漏らした公務員らへの罰則を強化する特定秘密保護法案は、きょ...

NEW山西省連続爆発事件、共産党本部狙た計画的犯行か

![](images/37f88b6fb9b8ff54279486ccb27307380a135e2b699bf451fcb11b89a4ed2666.jpg)

6日、中国·山西省の共産党本部ルで起きた連続爆発事件です。爆彈がビル周辺の数か所.

## 社会

## >>一览へ

薬ネ卜販壳、23品目“3年間安全調查後”解禁

福島第一原発4号機を公開、燃料取り出しへ高い一ドル

「もんじゆ」で核物質管理に不備、原子力機構に厳重注意

NEW温室効果ガスの平均濃度、過去最高值を記録

一転食材偽装を認める、「三笠」運営会社の社長辞任へ

安愚楽牧場「和牛商法」、関連会社などを提訴へ

NEW表示通正化対策、消费者庁が業界3団体に要請文

「嵐」など芸能人の偽サイ販売、容疑の親子らを3人逮捕

大阪・川に少年突き落とし、遠体は下着姿

歌舞伎町のホスト変死、何者かが暴行か

## 政治

NEW小学校の4階から小6男児転落、意識不明の重体

NEW「特定秘密保護法案」きょ3から国会審議

日本版NSC法案、衆院特別委で可決

自衛隊が離島防衛演習、冲縄·宮古島に地対艦ミサイ儿展開

岸田外相、中国·韓国との民間交流が重要という認識示す

「婚外子」退産相続の民法改正案、自公が成立目指す

原発事故の対応見直し、国が積極的関与へ

## 経済

>>一览へ

NEW「三越伊勢丹」も不適切表示、他の百貨店にも拡大

NEW東武鉄道系ホテルでもメニュー表示と異なる食材を使用

食材“虚偽”問題で注目、「成型肉」とは？

Want proof that conventions help? See how much you know about this page—even if you can’tOne problem with conventions, though: Designers are often reluctant to t k advantage f them. <sup>understand</sup> <sup>a</sup> <sup>word</sup> <sup>of</sup> <sup>it—just</sup> <sup>because</sup> <sup>it</sup> <sup>follows</sup> <sup>some</sup> <sup>conventions.</sup>Faced with the prospect of following a convention, there’s a great temptation for designers to try reinventing the wheel instead, largely because they feel (not incorrectly) that they’ve been hired Below the header, links for navigation are displayed. At the top right, search box is given. At<sub>to do something new and different, not the same old thing. Not to mention the fact that praise</sub> <sup>the</sup> <sup>center,</sup> <sup>content</sup> <sup>is</sup> <sup>shown.</sup> <sup>At</sup> <sup>the</sup> <sup>bottom,</sup> <sup>additional</sup> <sup>information</sup> <sup>is</sup> <sup>placed.</sup>from peers, awards, and high-profile job offers are rarely based on criteria like “best use of conventions.”

![](images/e26724c2e575ef647d6773b9cffea3196dc10780412ee445ca491b5420ddcc09.jpg)

Occasionally, time spent reinventing the wheel results in a revolutionary new rolling device. But usually it just amounts to time spent reinventing the wheel.

If you’re going to innovate, you have to understand the value of what you’re replacing (or as Dylan put it, “To live outside the law, you must be honest”), and it’s easy to underestimate just how much value conventions provide. The classic example is custom scrollbars. Whenever a designer decides to create scrollbars from scratch—usually to make them prettier—the results almost always make it obvious that the designer never thought about how many hundreds or thousands of hours of fine tuning went into the evolution of the standard operating system scrollbars.

If you’re not going to use an existing Web convention, you need to be sure that what you’re replacing it with either (a) is so clear and self-explanatory that there’s no learning curve—so it’s as good as the convention, or (b) adds so much value that it’s worth a small learning curve.

My recommendation: Innovate when you know you have a better idea, but take advantage of conventions when you don’t.

Don’t get me wrong: I’m not in any way trying to discourage creativity. I love innovative and original Web design.

One of my favorite examples is Harlem.org. The whole site is built around Art Kane’s famous photo of 57 jazz musicians, taken on the steps of a brownstone in Harlem in August 1957. Instead of text links or menus, you use the photo to navigate the site.

![](images/94d988ea4f8dba25ae5efb5184436c01dc8ba8ecbc6c2d8b503c81143b1f2b7b.jpg)  
Clicking on any area of the photo...  
identifies the people there and...  
lets you click on them to see their bios.

In the first page titled “Clicking on any area of the photo…,” a group photo is shown with a section highlighted. In the second page titled “identifies the people there and…,” the photo is zoomed to show the highlighted group and the group is described in the content. In the third page titled “lets you click on them to see their bios,” the photo is zoomed to show a single person and his biography is displayed.

Not only is it innovative and fun, but it’s easy to understand and use. And the creators were smart enough to understand that the fun might wear off after a while so they also included a more conventional category-based navigation.

![](images/64eec6524c9e1048d71f4e2d7bdcff7a31304e43539e8ba7be332846c414340c.jpg)  
You can also browse the musicians by name, instrument, or jazz style.

In the first page, Artists option is selected in the browse pane on the left. In the content pane, the names of artists in the group photo are listed. In the browse pane of the second page,   
Instruments option is selected. In the content pane, the instruments and their artists are listed. In the browse pane of the last page, Jazz styles option is selected. In the content pane, different Jazz styles and their artists are listed.

The rule of thumb is that you can—and should—be as creative and innovative as you want, and add as much aesthetic appeal as you can, as long as you make sure it’s still usable.

And finally, a word about consistency.

You often hear consistency cited as an absolute good. People win a lot of design arguments just by saying “We can’t do that. It wouldn’t be consistent.”

Consistency is always a good thing to strive for within your site or app. If your navigation is always in the same place, for instance, I don’t have to think about it or waste time looking for it.

![](images/47cc231dee632ebff205d74fd24129ac678bfa7799398734716cb7eec42df4c9.jpg)

But there will be cases where things will be clearer if you make them slightly inconsistent. Here’s the rule to keep in mind:

## CLARITY TRUMPS CONSISTENCY

If you can make something significantly clearer by making it slightly inconsistent, choose in favor of clarity.

## Create effective visual hierarchies

Another important way to make pages easy to grasp in a hurry is to make sure that the appearance of the things on the page—all of the visual cues—accurately portray the relationships between the things on the page: which things are most important, which things are similar, and which things are part of other things. In other words, each page should have a clear visual hierarchy.

Pages with a clear visual hierarchy have three traits:

The more important something is, the more prominent it is. The most important elements are either larger, bolder, in a distinctive color, set off by more white space, or nearer the top of the page—or some combination of the above.

## Very important

A little less important

Nowhere near as important

Things that are related logically are related visually. For instance, you can show that things are similar by grouping them together under a heading, displaying them in the same visual style, or putting them all in a clearly defined area.

Things are “nested” visually to show what’s part of what. For instance, a site section name (“Computer Books”) would appear above the titles of the individual books, reflecting the fact that the books are part of the section. And each book title in turn would span all the elements that make up the description of that book.

![](images/8ff9229596b6723dc68ce0dd53f08aceff5b1a5c43bf76865c01f87c23394e9f.jpg)

There’s nothing new about visual hierarchies. Every newspaper page, for instance, uses prominence, grouping, and nesting to give us useful information about the contents of the page before we read a word. This picture goes with this story because they’re both spanned by this headline. This story is the most important because it has the biggest headline and a prominent position on the page.

![](images/974f703794791c6e6caff57e21f97ee2682ac402a935464c8393c13d00d59d4a.jpg)

In the first section, the content is given in 4 columns under a title and labeled “The headline spanning these four columns makes it obvious that they’re all part of the same story.” In the second section, the title is in larger font size than the first section and labeled “The size of this headline makes it clear at a glance that this is the most important story.”

We all parse visual hierarchies every day, but it happens so quickly that the only time we’re even vaguely aware that we’re doing it is when we can’t do it—when the visual cues (or absence of them) force us to think.

A good visual hierarchy saves us work by preprocessing the page for us, organizing and prioritizing its contents in a way that we can grasp almost instantly.

But when a page doesn’t have a clear visual hierarchy—if everything looks equally important, for instance—we’re reduced to the much slower process of scanning the page for revealing words and phrases and then trying to form our own sense of what’s important and how things are organized. It’s a lot more work.

Parsing a page with a visual hierarchy that’s even slightly flawed—where a heading spans things that aren’t part of it, for instance—is like reading a carelessly constructed sentence (“Bill put the cat on the table for a minute because it was a little wobbly”).

![](images/b8e7623364f2d5e5c4d399c0aa7e5e1741d9b44438954e1f5eeb527b7ea2944f.jpg)

This flawed visual hierarchy suggests that all the major sections of the site are part of the Computer Books subsection.  
![](images/459cffeddb69429663230de9fc5b7887e85a87dcbc6fb132ef5f316b9116672b.jpg)  
Putting the heading where it belongs makes the relationship clearer.

Even though we can usually figure out what the sentence is supposed to mean, it still throws us momentarily and forces us to think when we shouldn’t have to.

## Break up pages into clearly defined areas

Ideally, on any well-designed Web page users can play a variation of the old TV game show \$25,000 Pyramid.<sup>1</sup> Glancing around, they should be able to point at the different areas of the page and say, “Things I can do on this site!” “Links to today’s top stories!” “Products this company sells!” “Things they’re eager to sell me!” “Navigation to get to the rest of the site!”

<sup>1</sup> Contestants had to get their partners to guess a category like “Things a plumber uses” by giving them examples (“a wrench, a pipe cutter, pants that won’t stay up...”).

Dividing the page into clearly defined areas is important because it allows users to decide quickly which areas of the page to focus on and which areas they can safely ignore. Eye-tracking studies of Web page scanning suggest that users decide very quickly in their initial glances which parts of the page are likely to have useful information and then rarely look at the other parts—almost as though they weren’t there. (Banner blindness—the ability of users to completely ignore areas they think will contain ads—is just the extreme case.)

## Make it obvious what’s clickable

Since a large part of what people are doing on the Web is looking for the next thing to click, it’s important to make it easy to tell what’s clickable.

As we scan a page, we’re looking for a variety of visual cues that identify things as clickable (or “tappable” on touch screens)—things like shape (buttons, tabs, etc.), location (in a menu bar, for instance), and formatting (color and underlining).<sup>2</sup>

<sup>2</sup> People also rely on the fact that the cursor in a Web browser changes from an arrow to a hand when you point it at a link, but this requires deliberately moving the cursor around, a relatively slow process. Also, it doesn’t work on touch screens because they don’t have a cursor.

This process of looking for clues in the appearance of things that tell us how to use them isn’t limited to Web pages. As Don Norman explains so enjoyably in his recently updated usability classic The Design of Everyday Things, we’re constantly parsing our environment (like the handles on doors) for these clues (to decide whether to pull or push). Read it. You’ll never look at doors the same way again.

![](images/45b0018b7817c77e695d4b93597deb4b210185367e19038e0c529c1318c456ca.jpg)

Easily identifying what’s clickable on a page has waxed and waned as a problem since the beginning of the Web.

![](images/c4271040d265247f39ccd692135d54cd99dc569e6de963110902c7dfbbf862db.jpg)

Above the year 1995 in the timeline scale, an underlined text link “book a trip” is shown with a   
submit button. Above the year 2000, a link with a button “Click here to CONTRIBUTE!” “Be   
One Voice That Matters!” is underlined. Above the years 2005 and 2010, a site structure with unique colors for clickable text is shown. Below the year 1995 on the timeline scale, a text “Paleozoic era. Most sites are designed by developers, using stock HTML text links and buttons. Obviously clickable, but boring” is shown. Below the year 2000, a text “The Wild   
West. Frustrated by Web limitations (few fonts, ugly underlines), print designers use images of   
text as links. It’s often hard to tell what’s clickable” is placed. Below the year 2005, a text “The Golden Age. CSS provides an elegant solution: Use one color (and no underlines) for all clickable text. Users get it, life is good” is displayed.

It’s currently resurfacing as an issue in mobile design, though, as you’ll see in Chapter 10. In general, you’ll be fine if you just stick to one color for all text links or make sure that their shape and location identify them as clickable. Just don’t make silly mistakes like using the same color for links and nonclickable headings.

## Keep the noise down to a dull roar

One of the great enemies of easy-to-grasp pages is visual noise.

Users have varying tolerances for complexity and distractions; some people have no problem with noisy pages, but many find them downright annoying. Users have even been known to put Post-its on their screen to cover up animation that’s distracting them while they’re trying to read. There are really three different kinds of noise:

There are really three different kinds of noise:

Shouting. When everything on the page is clamoring for your attention, the effect can be overwhelming: Lots of invitations to buy! Lots of exclamation points, different typefaces, and bright colors! Automated slideshows, animation, pop-ups, and the never-ending array of new attention-grabbing ad formats!

The truth is, everything can’t be important. Shouting is usually the result of a failure to make tough decisions about which elements are really the most important and then create a visual hierarchy that guides users to them first.

Disorganization. Some pages look like a room that’s been ransacked, with things strewn everywhere. This is a sure sign that the designer doesn’t understand the importance of using grids to align the elements on a page.

Clutter. We’ve all seen pages—especially Home pages—that just have too much stuff. The net effect is the same as when your email inbox is flooded with things like newsletters from sites that have decided that your one contact with them has made you lifelong friends: It’s hard to find and focus on the messages you actually care about. You end up with what engineers call a low signal-to-noise ratio: Lots of noise, not much information, and the noise obscures the useful stuff.

When you’re editing your Web pages, it’s probably a good idea to start with the assumption that everything is visual noise (the “presumed guilty until proven innocent” approach) and get rid of anything that’s not making a real contribution. In the face of limited time and attention, everything that’s not part of the solution must go.

## Format text to support scanning

Much of the time—perhaps most of the time—that users spend on your Web pages is spent scanning the text in search of something.

The way your text is formatted can do a lot to make it easier for them.

![](images/7a17f72ab526e5ed82c6478f6cb3a2bf82b6bdf2e0f10d33cb8009955c434fae.jpg)  
Which one would you rather scan?

In the first page, there are no headings and the entire content is left aligned and given in the same font except 3 words. In the second page, there are 2 headings and the content is given in multiple fonts and alignments.

Here are the most important things you can do to make your pages scan-friendly:

Use plenty of headings. Well-written, thoughtful headings interspersed in the text act as an informal outline or table of contents for a page. They tell you what each section is about