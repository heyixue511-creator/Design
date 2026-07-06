## Jakob Nielsen

# Designing Web Usability

## Designing Web Usability: The Practice of Simplicity

## © 2000 by New Riders Publishing

All rights reserved. No part of this book shall be reproduced, stored in a retrieval system, or transmitted by any means—electronic, mechanical, photocopying, recording, or otherwise——without written permission from the publisher. No patent liability is assumed with respect to the use of the information contained herein. Although every precaution has been taken in the preparation of this book, the publisher and author(s) assume no responsibility for errors or omissions. Neither is any liability assumed for damages resulting from the use of the information contained herein.

International Standard Book Number: 1-56205-810-X

Library of Congress Catalog Card Number: 99-63014

Printed in the United States of America

First Printing: December 1999

03 02 01 00 99 7 6 5 4 3 2 1

Interpretation of the printing code: The rightmost doubledigit number is the year of the book's printing; the rightmost single-digit number is the number of the book's printing. For example, the printing code 99-1 shows that the first printing of the book occurred in 1999.

## Trademarks

All terms mentioned in this book that are known to be trademarks or service marks have been appropriately capitalized. New Riders Publishing cannot attest to the accuracy of this information. Use of a term in this book should not be regarded as affecting the validity of any trademark or service mark.

## Warning and Disclaimer

Every effort has been made to make this book as complete and as accurate as possible, but no warranty or fitness is implied. The information provided is on an "as is" basis. The authors and the publisher shall have neither liability nor responsibility to any person or entity with respect to any loss or damages arising from the information contained in this book or from the use of the CD or programs accompanying it.

Publisher David Dwyer

Executive Editor Steve Weiss

Development Editor Jennifer Eberhardt

Indexer Lisa Stumpf

Reviewers Michael Chanover Perry Hewitt

Proofreader Bob LaRoche

Cover Design James Tung, Eric Baker Design Associates, NY

Interior Design Elizabeth Keyes

Interior Layout Kim Scott, Bumpy Design www.bumpy.com

## Contents at a Glance

Preface 2   
Introduction: Why Web Usability? 8   
2 Page Design 16   
3 Content Design 98   
Site Design 162   
5 Intranet Design 262   
6 Accessibility for Users with Disabilities 296   
7 International Use: Serving a Global Audience 312   
8 Future Predictions: The Only Web Constant Is Change 346   
9 Conclusion: Simplicity in Web Design 378   
Recommended Readings 392   
Index 398

## Table of Contents

Preface 2455   
Errata   
Book Layout   
Guide to This Book   
Introduction: Why Web Usability? 8   
Art Versus Engineering 11   
The Competitive Bar Is High 11   
About the Examples 12   
A Call for Action 13   
What This Book Is Not 13   
Bad Usability Equals No Customers 14   
Why Everybody Designs Websites Incorrectly 14   
Page Design 16   
Screen Real Estate 18   
Cross-Platform Design 25   
Where Are Users Coming From? 27 27   
Data Ink and Chart Junk   
The Car as a Web Browser 28   
Resolution-Independent Design 29   
Color Depth Getting Deeper 29   
Get a Big Screen 31   
Using Non-Standard Content 31   
Installation Inertia 33   
When Is It Safe to Upgrade? 33   
Helpful Super-Users 35   
Collect Browsers 36   
Separating Meaning and Presentation 36   
Platform Transition 37   
Response Times 42   
Data Lives Forever 43   
Predictable Response Times 44   
Server Response Time 45   
Speedy Downloads, Speedy Connections 46   
The Best Sites Are Fast 46   
Users Like Fast Pages 47   
Understanding Page Size 48   
You Need Your Own T1 Line 48   
Faster URLs 50   
Glimpsing the First Screenful 50   
Taking Advantage of HTTP Keep-Alive 53   
Linking 53   
Link Descriptions 55   
Link Titles 60   
Use Link Titles Without Waiting 60   
Coloring Your Links 62   
Link Expectations 64   
The Physiology of Blue 64   
Outbound Links 6 6   
Peoplelinks   
Incoming Links 74   
Linking to Subscriptions and Registrations 76   
Advertising Links 781   
Style Sheets   
Standardizing Design Through Style Sheets 82   
WYSIWYG 82   
Style Sheet Examples for Intranets 83   
Making Sure Style Sheets Work 4 855 8687 9 9  2 94 7   
Frames   
<NOFRAMES>   
Frames in Netscape 2.0   
Borderless Frames   
Is It Ever OK to Use Frames?   
Frames as Copyright Violation   
Credibility   
Printing   
Conclusion   
Content Design 98   
Writing for the Web 100   
The Value of an Editor 100   
Keep Your Texts Short 101   
Web Attitude 101   
Copy Editing 103   
Scannability 104   
Why Users Scan 106   
Plain Language 111   
Page Chunking 112   
Limit Use of Within-Page Links 115   
Page Titles 123   
Writing Headlines 124   
Legibility 125   
Online Documentation 129   
Page Screenshots 129   
Multimedia 131   
Auto-Installing Plug-Ins 131   
Client-Side Multimedia 132   
Waiting for Software to Evolve 134   
Response Time 134   
Images and Photographs 134   
Image Reduction 135   
Animation 143   
Showing Continuity in Transitions 145   
Indicating Dimensionality in Transitions 145   
Illustrating Change over Time 145   
Multiplexing the Display 146   
Enriching Graphical Representations 146   
Animation Backfires 146   
Visualizing Three-Dimensional Structures 146   
Attracting Attention 147   
Video 149   
Streaming Video Versus Downloadable Video 150   
Audio 154   
Enabling Users with Disabilities to Use Multimedia Content 155   
Three-Dimensional Graphics 156   
Bad Use of 3D 156   
When to Use 3D 159   
Conclusion 160   
The Attention Economy 160   
Site Design 162   
The Home Page 166   
How Wide Should the Page Be? 174   
Home Page Width 174   
Splash Screens Must Die 176   
The Home Page Versus Interior Pages 178   
Deep Linking 179   
Affiliates Programs 179   
Metaphor 180   
Shopping Carts as Interface Standard 188   
Alternative Terminology 188   
Navigation 188   
Where Am I? 188   
Navigation Support in Browsers 189   
Where Have I Been? 191   
Where Can I Go? 191   
Site Structure 198   
The Vice-Presidential Button 198   
Importance of User-Centered Structure 202   
Breadth Versus Depth 203   
The User Controls Navigation 214   
Help Users Manage Large Amounts of Information 217   
Design Creationism Versus Design Darwinism 218   
Reducing Navigational Clutter 221   
Future Navigation 221   
Avoid 3D for Navigation 222   
Subsites 222   
Search Capabilities 224   
Don't Search the Web 224   
Micro-Navigation 225   
Advanced Search 227   
Global Search 227   
The Search Results Page 230   
Page Descriptions and Keywords 231   
Use a Wide Search Box 233   
See What People Search For 237   
Search Destination Design 238   
Integrating Sites and Search Engines 238   
URL Design 246   
Compound Domain Names 246   
Fully Specify URLs in HTML Code 247   
URL Guessing 248   
Archival URLs 249   
Beware of the Os and Os 249   
Advertising a URL 250   
Supporting Old URLs 251   
Y2K URL 251   
User-Contributed Content 256   
Applet Navigation 256   
Double-Click 258   
Slow Operations 259   
Conclusion 259   
Intranet Design 262   
Differentiating Intranet Design   
from Internet Design 265   
Extranet Design 266   
Improving the Bottom Line Through Employee Productivity 270   
Average Versus Marginal Costs 276   
Intranet Portals: The Corporate Information Infrastructure 276   
Get Rid of Email 277   
Intranet Maintenance 279   
The Big Three Infrastructure Components:   
Directory, Search, and News 279   
Intranet Design Standards 280   
Guidelines for Standards 281   
Outsourcing Your Intranet Design 284   
Managing Employees' Web Access 284   
Hardware Standards 285   
Browser Defaults 286   
Search Engine Defaults 288   
Intranet User Testing 289   
Field Studies 290   
Don't Videotape in the Field 292   
Conclusion 293   
Accessibility for Users with Disabilities 296   
Disabilities Associated with Aging 298   
Web Accessibility Initiative 298   
Assistive Technology 299   
Visual Disabilities 302   
ALT Attributes 303   
Auditory Disabilities 308   
Speech Disabilities 308   
Motor Disabilities 309   
Cognitive Disabilities 309   
Search Without Spelling 310   
Conclusion: Pragmatic Accessibility 311   
International Use: Serving a Global Audience 312   
Internationalization Versus Localization 315   
Designing for Internationalization 315   
International Inspection 319   
Should Domains End in .com? 319   
Translated and Multilingual Sites 320   
Language Choice 324   
Multilingual Search 331   
Make Translations Bookmarkable 331   
Regional Differences 332   
International User Testing 333   
Overcoming the Language Gap 333   
How Many Countries Should You Test? 335   
Thanking Your Participants 335   
Methods of Testing 336   
Travel Yourself 336   
Add a Few Days to Your Stay 336   
Remote User Testing 337   
Usability Labs for International Testing 338   
Self-Administered Tests 341   
Conclusion 344   
8 Future Predictions: The Only Web Constant Is Change 346   
Long-Term Trends 348   
The Internet Is Hard 348   
The Anti-Mac User Interface 351   
The Invisible Computer 352   
Information Appliances 353   
Drawing a Computer 353   
WebTV 354   
Designing for WebTV 356   
Death of Web Browsers 362   
Slowly Increasing Bandwidth 363   
Metaphors for the Web 365   
The Telephone 366   
Different Media, Different Strengths 366   
Telephone Usability Problems 368   
Contact Tokens 369   
The Television 370   
Restructuring Media Space: Good-Bye, Newspapers 372   
Media Distinctions Caused by Technology 373   
Conclusion 376   
9 Conclusion: Simplicity in Web Design 378   
Home-Run Websites 380   
Half-Minute Baseball Lesson 380   
User Survey: What Causes Repeat Traffic? 382   
Better Than Reality 383   
Best of Times or Worst of Times? 388   
Mouseclicks Vote 390   
Recommended Readings 392   
Books 394   
Usability 395   
Hypertext 395   
Web Technology 396   
Read My Next Book 396   
Index 398

## About the Author

Jakob Nielsen, Ph.D. is a User Advocate specializing in web usability and a principal of Nielsen Norman Group (www.nngroup. com), which he co-founded with Dr. Donald A. Norman, former vice president of Apple Research. Until 1998, Dr. Nielsen was a Sun Microsystems Distinguished Engineer and led that company's web usability efforts starting with the original design of SunWeb in early 1994. His previous affiliations include the IBM User Interface Institute, Bell Communications Research, and the Technical University of Denmark. Nielsen is the author and editor of 8 other books and more than 75 research papers on usability engineering, user interface design, and hypertext. He is also a frequent keynote presenter at industry conferences. Nielsen is the founder of the“discount usability engineering" movement for fast and simple ways of improving user interfaces. Nielsen's Alertbox column about web usability has been published on the Internet since 1995 (www.useit.com/alertbox) and currently has about 100,000 readers. He is also the usability columnist for Ziff-Davis Network's DevHead and a web design critic for Internet World magazine. He holds 38 U.S. patents, mainly on ways to make the Internet easier to use. Dr. Nielsen's website is at www.useit.com: It's text-only and pretty fast.

## Author's Acknowledgments

I would like to thank the following for help in writing this book or in my web projects over the years: Franz Aman, Claire Amundsen, Rick Brennan, Bruce Browne, Marsh Chamberlain, Kreta Chandler, Debra Coelho, Steve Davis, Kathy Dickinson, Susan Doel, Meghan Ede, Karin Ellison, Susan Farrell, B.J. Fogg, Jonathan Fox, Michael Fuller, Don Gentner, Steve Gibson, Bob Glass, Rich Gold, Dana Greer, Chris Haaga, Melody Kean Haller, Martin Hardee, Perry Hewitt, Mark Hurst, Luice Hwang, Keith Instone, Matthew Johan, Chris Johnson, Hannah Kain, Wendy Kellogg, Erika Kindlund, Teresa Lau, Rick Levine, Judy Lindberg, Noel Lopez, Michael "Mac" McCarthy, Andrea Mankoski, Peter Merholz, Carl Meske, Rolf Molich, John Morkes, Jim Newton, Donald Norman, Larry Page, Judy Potzler, Bill Prouty, Darcy Provo, Janice Rohn,Victoria Ryan, Darrell Sano, Eric Schmidt, Hassan Schroeder, Hasmig Seropian, Will Snow, Jared Spool, David L. Stewart, Rory Swensen, John Tang, Bruce "Tog"Tognazzini, Nirav Tolia, Jeanie Treichel, Elizabeth Waymire, Ron Wilbur, and Debra Winters.

Also, even though I didn't work on many web projects with them, much of my thinking has been influenced by John M. Carroll, Susan Dumais, Dennis Egan, George Furnas, John Gould, Jim Hollan, Thomas K. Landauer, Mary Beth Rosson, Ben Shneiderman, Dennis Wixon, and Patricia Wright.

Jakob Nielsen

## Publisher's Acknowledgements

We'd like to thank Jakob Nielsen, an extraordinary man, for his patience with an, at times, impatient publisher. Thanks also to Hannah Nielsen for her patience with the publisher as we asked her for an ever-increasing amount of Jakob's time near the end of this project. Thank you both for allowing us into your home and into your lives during the completion of this book.

Kudos as well to Kim Scott for an extraordinary job of turning the vision of a well-designed book into a reality. And special thanks to Jennifer Eberhardt.

## A Message from New Riders

Jakob Nielsen is one of the busiest speakers and commentators in the world of high-tech because of his message and the eloquence with which he delivers it. His message is simple—at least on the surface—and is accessible to anyone who will listen (and multitudes do each year): Put USABILITY first. Practice SIMPLICITY.

The challenges and complexities to the put usability first' philosophy of design can begin when ideation turns to planning, and planning turns to implementation. The challenges never stop, and Jakob helps you to understand them and enable yourself to make the continual adjustments necessary to survive and prosper in the‘user-first’ world of the Web.

The best thing about this book, along with what you'll learn about yourself and others who use the Web (and how to improve the usefulness of your website immeasurably), is that Designing Web Usability is flat– out one of the best reads you'll encounter—in technology publishing or elsewhere. Jakob has a gift for communication that enables him to wrap his vision in a lucid, compelling discourse that appeals to academics and lay people, web designers and web users. Designing Web Usability holds this broad appeal because Jakob's message makes so much sense, while being masterfully communicated on so many levels.

Who said you can't have fun while expanding your horizons?

New Riders is honored to have worked with Jakob Nielsen over the past two years as he's written and refined Designing Web Usability: The Practice of Simplicity. We believe it's been well worth the wait. Let us know what you think...

## How to Contact Us

As the reader of this book, you are our most important critic and comtor. We value your opinion and want to know what we're doing right, what we could do better, in what areas you'd like to see us publish, and any other words of wisdom you're willing to pass our way.

As the Executive Editor for the Graphics team at New Riders, I welcome your comments.You can fax, email, or write me directly to let me know what you did or didn't like about this book—as well as what we can do to make our books better.

Please note that I cannot help you with technical problems related to the topic of ois book, and that due to the high volume of mail I receive, I might not be able mmplp  avy ne

When you write, please be sure to include this book's title, ISBN, and author, as well as your name and phone or fax number. I will carefully review your comments and share them with the authors and editors who worked on the book.

For any issues directly related to this or other titles:

Email: steve.weiss@newriders.com

Mail: Steve Weiss

Executive Editor

Professional Graphics & Design Publishing

New Riders Publishing

201 West 103rd Street

Indianapolis, IN 46290 USA

## Visit Our Website: www.newriders.com

On our website you'll find information about our other books, the authors we partner with, book updates and file downloads, promotions, discussion boards for online interaction with other users and with technology experts, and a calendar of trade shows and other professional events with which we'll be involved. We hope to see you around.

## Email Us from Our Website

Go to www.newriders.com and click on the Contact link if you

Have comments or questions about this book

■Have a book proposal or are otherwise interested in writing with New Riders

■Would like us to send you one of our author kits

■ Are an expert in a computer topic or technology and are interested in being a reviewer or technical editor

Want to find a distributor for our titles in your area

Are an educator/instructor who wishes to preview New Riders books for classroom use.

## Call Us or Fax Us

You can reach us toll-free at (800) 571-5840 + 9 + 3567. Ask for New Riders. If outside the USA, please call 1-317-581-3500. Ask for New Riders.

You can fax us at 317-581-4663, Attention: New Riders.

![](images/a239c66804dd1b1605528c523322361300a4690a12e854a2c5cddff7db0e8238.jpg)

## Preface

Enough, already, Jakob. Isn't it selfdefeating to publish on dead trees when you are writing about the Web?"

I am sure that a lot of readers will be asking this question, so let me answer it up front.

One of the downsides of physical book publishing is that we won't be able to immediately reprint and distribute this book should we need to update any errors or technological advances. The Web, however, enables us to provide instantaneous feedback, and so I've created a website at which I'll post corrections. Simply set your browser to http://www.useit.com/errata.

I am a usability expert, so my choice of medium is governed by what is most usable for a given communications goal and not by what is most in fashion at any given time. Of course, the Web is a great communications medium (that's why I am writing about it), and it is well suited for shorter documents with many links (I have many such pages on my website, www.useit.com).The Web is not good for very long documents that need to present a steadily progressing argument.

If you really want to learn about a topic, it is still better to do so by reading a coherent, in-depth treatment of the topic written from a single perspective than to bounce among multiple shorter ideas and different perspectives. In other words, a book is still better than the Web for the goal I want to achieve: to get readers to understand the usability perspective of web design.

Three conditions would have to happen for me to give up writing books:

Computer screens must improve to the point where reading from screens is as fast and as pleasant as reading from paper. I am confident that this will happen around the year 2002 for high-end computers and 2007 for mainstream computers, because such screens have already been demonstrated in the lab.

Web browsing user interfaces must improve enough that it is as easy to navigate the Web as it is to leaf through the pages of a book. I am more skeptical on this count because browser vendors currently seem to invest more efforts on useless multimedia and advertising schemes than on helping users navigate; but even so, we might get useful browsers by the year 2003.

Readers and writers must both adjust to non-linear information spaces, that is, how to write in ways that utilize hypertext and how to read without the safety of mind that comes from making no decisions beyond turning the page. Nothing but time and plenty of experience and exposure to well-crafted hypertexts will make this change happen. Unfortunately, there is a chicken-and-egg problem in that well-crafted hypertexts will not happen until good writers have become skilled in writing hypertext. I expect good hypertext writing to happen in greater quantities as the Web matures, around the year 2001, and the emphasis

## Book Layout

A printed book allows the benefit of sidebars and other twodimensional layouts that are not available on a web page, which is still essentially a onedimensional scroll—just like the Egyptians knew and loved. In a book it is possible to place illustrations and captions in ways that supplement the text better than can be done on the Web. I can't take credit for the page design in this book, but I hope you find it useful.

irrevocably changes from dazzling people with the novelty of a new medium to satisfying user needs. Maybe four years later, in the year 2005, the majority of users will have gained sufficient experience in dealing with hypertext.

Comparing these three bullets leads to the conclusion that hardware technology is the constraining factor and that we have to wait until approximately the year 2007 for books to go away and be fully replaced with online information. Legacy publishers be warned: This will happen.

## Guide to This Book

The book you are reading now is the first of two books on the subject of web usability. I chose to publish two books for two reasons. First, a book does no good if nobody reads it, and I have seen fat volumes sit on the shelf and gather dust too frequently to want to write one myself. A two-inch-thick tome on how to make Excel draw pie charts intimidates people from ever opening the book. They may feel good about owning such detailed wisdom, but they will not read it. Two relatively slim volumes stand a much better chance of being read than a single fat one.

Second, it may not be necessary for all readers to read both books because the different books focus on different aspects of web usability. Having more narrowly focused volumes makes the book more affordable for students and others who only need some of the information. No need to pay extra for a huge publication, half of which you don't need.

These two books attack the problem of usable web design from two angles. This first one is about the“what" of good websites, and the second book is about the “how." Everybody always wants to know the solution right away, so that's what I have concentrated on here.This book explains what is known about the properties of easy-to-use websites. Short preview: Relish simplicity, and focus on the users' goals rather than glitzy design.

This first chapter covers the main areas of web design: page design, content design, and the design of the overall site architecture. The subsequent chapters cover special issues that supplement the general basics with specific

findings for intranets, users with disabilities, and international users. Finally, this volume ends with a view toward the future of the Internet and new developments on the Web.

The second book will cover the "how" of web usability and explain the methodologies that were used to derive the findings that are presented here in the first book. The impatient reader who just wants to know the facts can read this one. If you design sites that follow the rules I lay out here, your sites will definitely be among the easiest to use on the Internet. But to design really great sites requires additional insights that are specific to your project and your customers and their needs. There is no way around collecting additional usability data in your own project. How to do so will be explained in the second book.

Jakob Nielsen

Mountain View, California

11 Art Versus Engineering The Competitive Bar Is High About the Examples

13 What This Book Is Not Bad Usability Equals No Customers

13 A Call for Action

14 Why Everybody Designs Websites Incorrectly

## 1 Introduction: Why Web Usability?

Usability rules the Web. Simply stated, if the custonter can't find a prodoct, then he or she wilt not buy it.

The Web is the üiltimate customerempowering enviromment. He or she who clicks the nouse gets to decjde everything, It is so eavy to go Esewhere; all the-competitors in the world are but a mouseclick away.

Usability has assumed a much greater importance in the Internet economy than it has in the past.

With about 10 million sites on the Web in January 2000 (and about 25 million by the end of the year and a hundred million by 2002), users have more choices than ever. Why should they waste their time on anything that is confusing, slow, or that doesn't satisfy their needs?

## Why, indeed?

As a result of this overwhelming choice and the ease of going elsewhere, web users exhibit a remarkable impatience and insistence on instant gratification. If they can't figure out how to use a website in a minute or so, they conclude that it won't be worth their time. And they leave.

Usability has assumed a much greater importance in the Internet economy than it has in the past. In traditional physical product development, customers did not get to experience the usability of the product until after they had already bought and paid for it. Say, for example, you buy a VCR and discover that it's difficult to set the clock and that you cannot figure out how to program the taping of your favorite shows. Tough luck—the manufacturer is laughing all the way to the bank.

The software industry has slightly more motivation than the physical product industry to improve usability. For software, users typically have access to a support center they can call when experiencing problems. Such support calls are very expensive to handle (estimates range from \$30 to \$100 per call, depending on the complexity of the software), and more than half of the calls are due to poor usability. Unfortunately, the cost of running the support center is usually charged to a different account than the cost of improving usability, so the individual development managers are not overly motivated to ship great user interfaces. Shipping on time is what pays the big bonuses; saving money on the support department's budget next year doesn't.

The Web reverses the picture. Now, users experience the usability of a site before they have committed to using it and before they have spent any money on potential purchases.

The equation is simple:

In product design and software design, customers pay first and experience usability later.

## The Competitive Bar Is High

On the Web, your competition is not limited to the other companies in your industry. With all the other millions of sites out there, you are in competition for the users' time and attention, and web users get their expectations for great usability from the very best of all these other sites. The thinking goes, "If I can get this great service when buying a \$5 paperback book, why can't I get good online service when I spend thousands of dollars with you?" Very good question, by the way.

On the Web, users experience usability first and pay later.

Very clear why usability is more important for web design.

## Art Versus Engineering

There are essentially two basic approaches to design: the artistic ideal of expressing yourself and the engineering ideal of solving a problem for a customer. This book is firmly on the side of engineering. While I acknowledge that there is a need for art, fun, and a general good time on the Web, I believe that the main goal of most web projects should be to make it easy for customers to perform useful tasks.

I describe a very systematic approach to web design, with a sequence of methods anybody can use to discover users' needs and any difficulties they may be having using the site. Treating a web project as a software development project will make it easier to meet schedules and to ensure the quality of the site. In particular, pervasive application of usability engineering methodology throughout your web project will lead to continuous improvement of the site, both with respect to the initial design and subsequent redesigns.

You will find many rules, principles, guidelines, and methods in this book.They all derive from experience of what actually works when real users try to perform real tasks on the Web. Ever since the early years of the Web, I have observed hundreds of users using hundreds of websites— plus, of course, hundreds of other users using many different types of online information systems and hypertext designs since the early 1980s.

I do not claim that every last one of my teachings has to be followed slavishly to the letter in every project.The skilled professional knows when to follow the rules and when to bend a rule or even break it.You must know the rules in the first place before you can consider whether it might improve a specific project to deviate from some of them. Also, a fundamental guiding principle for rulebreaking is that you only do so when you have a really good reason to do so.

## About the Examples

The book has many screenshots of real web designs, and the examples and comments refer to the sites the way they were the day of my visit. Because I have been collecting examples and screenshots for several years, many of these sites will have changed—one would hope that most of them have improved—by the time you read this book. If you go to one of the sites depicted in this book and find that it has changed, that will not invalidate my example. The reason to give examples is not to criticize or praise specific sites, companies, or designers. All designs have their good and not-so-good parts, and sometimes I point out a good part of a bad site or a bad part of a good site. The examples are used to illustrate my general web design principles and methodologies because it is hard to understand abstract theory without concrete examples.

The engineering approach has one major benefit: When you are in doubt about whether to choose one design or another, you can pose an empirical question that can be resolved by gathering real data from your customers. Can people find information faster with design A or design B? Do users rate design A or design B best on a standard customer-satisfaction questionnaire? Pick the one that gets the highest scores and not the one you personally like the best.

Of course, the scientific method can only take you so far. There is still a need for inspiration and creativity in design. A simple usability engineering method that anybody can follow can tell you that users have problems navigating your site or that everybody overlooks the search button on your home page.Taking these results and coming up with a better navigation scheme or a better look or placement of the search button is not simply a matter of following a series of easy steps.You also need some design inspiration to strike. However, remember that innovation is 10 percent inspiration and 90 percent perspiration.The way you get appropríate design ideas (and not just ideas for cool designs that nobody can use) is to watch users and see what they like, what they find easy, and where they stumble.The way to get good design ideas is quite often to follow usability engineering methodology and steep yourself in user reactions and data.

Web usability changes less rapidly than web technology, so the methods and concepts you will learn from this book will be useful to you for many years, even if the implementation of your design will change quite a lot. Many of the principles I present in this book stem from research by myself and others into hypertext and other interactive presentation systems. I, personally, did my first hypertext project in 1984, but others have been at it since the 1960s. Many of these results have withstood the test of time. When methodologies and results from the mid-1980s continue to be useful in the late 1990s, there is every reason to believe that they will continue to hold into the 21st century.

## A Call for Action

If you read this book and put it away, I will have failed. Of course, if you put it away without even reading it, I will have utterly failed, but I trust that the book is sufficiently appealing that you will at least glance through it before consigning it to permanent storage on your bookshelf.

The goal of this book is to change your behavior. I am an evangelist at heart, and I want you to be able to provide better service to your users after you have read my book. There are so many actionable steps that can be taken to make life less miserable for web users. This book is full of specific methods that can be used at almost every stage of a web project to dramatically enhance the user experience. There is no excuse for not using some of these methods because many of them are extremely cheap. There is also no excuse for not planning to include some usability methods in your next web design project because many of them are extremely easy to learn.

After you have read this book, you are ready to take action. Your very next design project can employ usability methods, and only if you do so will you gain any improvements in your site. Reading about usability doesn't make your site better; only doing something about it will help. Remember, you can do it. Anybody can do it. But most web designers blatantly ignore usability and design for their own pleasure (or worse, the boss's pleasure) instead of trying to satisfy user needs. This is good news for you because this book is your secret weapon to making your site better than 90 percent of the Internet—all because 90 percent of the designers don't know (or don't bother to use) the simple techniques I will teach you.

## What This Book Is Not

This is not a book about HTML or how to draw an icon or other web implementation technology. There are many good books that will teach you how to implement websites, so I am not even going to try. In any case, it's much too tough a job to write books about something that changes as rapidly as web implementation details.

You are probably going to have to buy two books (booksellers will love this part): this book to tell you what to do with your site and an implementation book to tell you

## Bad Usability Equals No Customers

In the network economy, the website becomes a company's primary interface to the customer. Indeed, for e-commerce companies the site is the company. The user interface becomes the marketing materials, store front, store interior, sales staff, and post-sales support all rolled into one. In many cases the site even becomes the product itself. Thus, having bad usability is like having a store that is on the 17th floor of a building (so nobody can find it), is only open Wednesdays between 3 and 4 o'clock (so nobody can get in), and has nothing but grumpy salespeople who won't talk to the customers (so people don't buy too much).

how to put that design on the Net. I recommend reading the two books in the order I just indicated. You should read my book first because you should start your web project by finding out what your customers want and good ways of designing a site that works for them. It is dangerous to read books about technology, coding, layout, or illustration techniques first, because most people can't keep themselves from hacking up a few pages as soon as they know how. And these pages and sites usually turn out to be useless if they are built from an understanding of HTML or Adobe Photoshop without a corresponding understanding of web design and user needs.

This is also not a book about Internet business strategy as such, even though there are several strategic considerations discussed throughout. There is no way I can tell you how to run your business on the Internet. One has to know the specifics of each industry and each company to do so.

The book does, however, focus on one big-picture strategic idea: Place your customers' needs at the center of your web strategy. The remaining strategies will differ from company to company, but I can guarantee that any company that makes its site easy to use will have a major advantage over its competitors, no matter what industry it's in.

## Why Everybody Designs Websites Incorrectly

This book is based on observations of usability tests with about 400 users from a wide variety of backgrounds and using a large number of different websites over the last six years. I have also drawn on lessons from the 10 years I worked on usability, online information systems, and hypertext during the dark ages before the Web.

Since I started designing for the Web in 1994, I have made many mistakes. In the beginning I thought these mistakes were simply due to my own limitations (you always tend to blame yourself). I have continued to see most other companies make the same mistakes I made in 1994 and 1995, so I have come to conclude that these problems are inevitable in a company's first web project unless proactive and explicit action is taken to avoid them. One of the main goals of this book is to help others avoid making

these mistakes again and again. After all, those who do not know history are doomed to repeat it. But if you know, you can do better.

Fundamental errors are common on all levels of web design:

Business model. Treating the Web as a Marcom brochure instead of a fundamental shift that will change the way we conduct business in the network economy.

Project management: managing a web project as if it were a traditional corporate project.This leads to an internally focused design with an inconsistent user interface. Instead, a website should be managed as a single customer-interface project.

Information architecture: structuring the site to mirror the way the company is structured. Instead, the site should be structured to mirror the users' tasks and their views of the information space.

Page design: creating pages that look gorgeous and that evoke positive feelings when demo'd inside the company. Internal demos do not suffer the response-time delays that are the main determinant of web usability; similarly, a demo does not expose the difficulties a novice user will have in finding and understanding the various page elements. Instead, design for an optimal user experience under realistic circumstances, even if your demos will be less “cool."

Content authoring: writing in the same linear style as you've always written. Instead, force yourself to write in the new style that is optimized for online readers who frequently scan text and who need very short pages with secondary information relegated to supporting pages.

Linking strategy: treating your own site as the only one that matters, without proper links to other sites and without well-designed entry-points for others to link to. Many companies don't even use proper links when they mention their own site in their own advertising. Instead, remember that hypertext is the foundation of the Web and that no site is an island.

In every one of these cases, the natural way people go about doing web projects based on their non-web experience turns out to be wrong. The Web is a new medium and requires a new approach, as explained in this book.

## 18 Screen Real Estate

## 25 Cross-Platform Design

Data Ink and Chart Junk

• Where Are Users Coming From?

The Car as a Web Browser

Resolution-Independent Design

• Color Depth Getting Deeper

• Get a Big Screen

• Using Non-Standard Content

• Installation Inertia

• When Is It Safe to Upgrade?

• Helpful Super-Users

• Collect Browsers

## 36 Separating Meaning and Presentation

• Platform Transition

## 42 Response Times

• Data Lives Forever

• Predictable Response Times

• Server Response Time

• The Best Sites Are Fast

• Speedy Downloads, Speedy Connections

• Users Like Fast Pages

• Understanding Page Size

• You Need Your Own T1 Line

• Faster URLs

• Glimpsing the First Screenful

• Taking Advantage of HTTP Keep-Alive

## 53 Linking

• Link Descriptions

• Link Titles

• Guidelines for Link Titles

Use Link Titles Without Waiting

• Coloring Your Links

• Link Expectations

• The Physiology of Blue

• Outbound Links

• Peoplelinks

• Incoming Links

• Linking to Subscriptions and Registrations

• Advertising Links

## 81 Style Sheets

• Standardizing Design Through Style Sheets

• WYSIWYG

• Style Sheet Examples for Intranets

Making Sure Style Sheets Work

## 85 Frames

• <NOFRAMES>

• Frames in Netscape 2.0

Borderless Frames

• Is It Ever OK to Use Frames?

• Frames as Copyright Violation

92 Credibility

94 Printing

97 Conclusion

## 2 Page Design

Page design is the most immediately visible part of web design. With current browser technology, users are looking at a single page at a time (or, at most, two or three pages if they have a large screen with multiple windows open). This chapter concerns the usability of the surface appearance of a website: What's on the individual pages?

(Facing page) When visiting MapQuest, most of the screen space ends up being used for distracting machinery that is extraneous to the content the user came for. Of the 480,000 precious pixels on an 800×600 display, only 20% are used for the content of interest to the user (indicated in green on the map). Additionally, 31% of the pixels are used for operating system and browser controls (blue), 23% are used for site navigation (yellow), and 10% are used for advertising. The remaining 16% of the pixels go unused (white) because the coding of this page does not allow it to reformat to fit the window.

Site design, however, is often more important for usability because users are never going to even get close to the correct pages unless the site is structured according to user needs and contains a navigation scheme that allows people to find what they want. These site design issues are discussed in a later chapter, as is the design of the actual content that goes inside each page.

## Screen Real Estate

Web pages should be dominated by content of interest to the user. Unfortunately, we see many sites that spend more screen space on navigation than they do on the information that supposedly caused the user to visit in the first place. Navigation is a necessary evil that is not a goal in itself and should be minimized.

For an interesting exercise, try blocking out the main regions in a web page and count the proportion of pixels used for various purposes. My examples in these images include space used by the browser and operating system. Even though web designers usually cannot influence this space, the users don't care. All users know is that they paid for a certain number of pixels on their monitor and only 20 and 14 percent, respectively, of these pixels are being used to display the content they want.

As with all layout, whitespace is not necessarily useless, and it would be a mistake to design overly compact pages. Whitespace can guide the eye and help users understand the grouping of information. If you have the choice between separating two segments of content by a heavy line or by some whitespace, it will often look better to use the whitespace solution, which will typically also download faster.

![](images/464018fe2c3d06bedd217e020d22ddfbbfe5cb07d3d375cb4e4450492833f3b0.jpg)

![](images/149bf071269f1695a8ff210be442f1d7800873f4254e0610f6ec2c3df9e222a6.jpg)  
www.mapquest.com