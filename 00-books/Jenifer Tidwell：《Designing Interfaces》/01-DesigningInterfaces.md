# Designing Interfaces

![](images/613b9b0bcf76618cbbe76cf743a1ade8c2a5f14ae7d6c162c701f9a4456458e9.jpg)

## Designing Interfaces

Despite all of the UI toolkits available today, it's still not easy to design good application interfaces. This bestselling book is one of the few reliable sources to help you navigate through the maze of design options. By capturing UI best practices and reusable ideas as design patterns, Designing Interfaces provides solutions to common design problems that you can tailor to the situation at hand.

This updated edition includes patterns for mobile apps and social media, as well as web applications and desktop software. Each pattern contains full-color examples and practical design advice that you can use immediately. Experienced designers can use this guide as a sourcebook of ideas; novices will find a roadmap to the world of interface and interaction design.

Design engaging and usable interfaces with more confidence and less guesswork

■ Learn design concepts that are often misunderstood, such as affordances, visual hierarchy, navigational distance, and the use of color

Get recommendations for specific Ul patterns, including alternatives and warnings on when not to use them

Mix and recombine Ul ideas as you see fit

Polish the look and feel of your interfaces with graphic design principles and patterns

"Anyone who's serious about designing interfaces should have this book on their shelf for reference. It's the most comprehensive cross-platform examination of common interface patterns anywhere.

-Dan Saffer author of Designing Gestural Interfaces (O'Reilly) and Designing for Interaction (New Riders)

Jenifer Tidwell is a writer and consultant in interaction design, information architecture, and pre-design analysis. She has designed and built user interfaces for companies such as Google and The MathWorks.

Designing Interfaces

Designing Interfaces Second Edition

Jenifer Tidwell

## Designing Interfaces, Second Edition

by Jenifer Tidwell

Copyright © 2011 Jenifer Tidwell. All rights reserved.

Printed in Canada.

Published by O’Reilly Media, Inc., 1005 Gravenstein Highway North, Sebastopol, CA 95472.

O’Reilly books may be purchased for educational, business, or sales promotional use. Online editions are also available for most titles (http://my.safaribooksonline.com). For more information, contact our corporate/institutional sales department: 800-998-9938 or corporate@oreilly.com.

Editor: Mary Treseler

Indexer: Lucie Haskins

Production Editor: Rachel Monaghan

Cover Designer: Karen Montgomery

Copyeditor: Audrey Doyle

Proofreader: Emily Quill

Interior Designer: Ron Bilodeau

Illustrator: Robert Romano

## Printing History:

November 2005: First Edition.

December 2010: Second Edition.

Nutshell Handbook, the Nutshell Handbook logo, and the O’Reilly logo are registered trademarks of O’Reilly Media, Inc. Designing Interfaces, the image of a Mandarin duck, and related trade dress are trademarks of O’Reilly Media, Inc.

Many of the designations used by manufacturers and sellers to distinguish their products are claimed as trademarks. Where those designations appear in this book, and O’Reilly Media, Inc. was aware of a trademark claim, the designations have been printed in caps or initial caps.

While every precaution has been taken in the preparation of this book, the publisher and author assume no responsibility for errors or omissions, or for damages resulting from the use of the information contained herein.

## Contents

Introduction to the Second Edition . . xi   
Preface. . xv   
1. What Users Do . . 1   
A Means to an End 2   
The Basics of User Research 4   
Users’ Motivation to Learn 6   
The Patterns 8   
Safe Exploration 9   
Instant Gratification 10   
Satisficing 11   
Changes in Midstream 12   
Deferred Choices 12   
Incremental Construction 14   
Habituation 14   
Microbreaks 16   
Spatial Memory 17   
Prospective Memory 18   
Streamlined Repetition 19   
Keyboard Only 20   
Other People’s Advice 21   
Personal Recommendations 22   
2. Organizing the Content:   
Information Architecture and Application Structure . 25   
The Big Picture 26   
The Patterns 29   
Feature, Search, and Browse 30   
News Stream 34   
Picture Manager 40   
Dashboard 45   
Canvas Plus Palette 50   
Wizard 54   
Settings Editor 59   
Alternative Views 64   
Many Workspaces 68   
Multi-Level Help 71   
3. Getting Around: Navigation, Signposts, and Wayfinding . 77   
Staying Found 77   
The Cost of Navigation 78   
Navigational Models 80   
Design Conventions for Websites 85   
The Patterns 86   
Clear Entry Points 87   
Menu Page 90   
Pyramid 94   
Modal Panel 97   
Deep-linked State 100   
Escape Hatch 104   
Fat Menus 106   
Sitemap Footer 110   
Sign-in Tools 115   
Sequence Map 118   
Breadcrumbs 121   
Annotated Scrollbar 124   
Animated Transition 127   
4. Organizing the Page: Layout of Page Elements. . . 131   
The Basics of Page Layout 132   
The Patterns 140   
Visual Framework 141   
Center Stage 145   
Grid of Equals 149   
Titled Sections 152   
Module Tabs 155   
Accordion 159   
Collapsible Panels 163   
Movable Panels 168   
Right/Left Alignment 173   
Diagonal Balance 176   
Responsive Disclosure 179   
Responsive Enabling 182   
Liquid Layout 186   
5. Lists of Things . 191   
Use Cases for Lists 192   
Back to Information Architecture 192   
Some Solutions 194   
The Patterns 197   
Two-Panel Selector 198   
One-Window Drilldown 202   
List Inlay 206   
Thumbnail Grid 210   
Carousel 215   
Row Striping 220   
Pagination 224   
Jump to Item 228   
Alphabet Scroller 230   
Cascading Lists 232   
Tree Table 234   
New-Item Row 236   
6. Doing Things: Actions and Commands . . 239   
Pushing the Boundaries 242   
The Patterns 245   
Button Groups 246   
Hover Tools 249   
Action Panel 252   
Prominent “Done” Button 257   
Smart Menu Items 261   
Preview 263   
Progress Indicator 266   
Cancelability 269   
Multi-Level Undo 271   
Command History 275   
Macros 278   
7. Showing Complex Data:   
Trees, Charts, and Other Information Graphics . . 281   
The Basics of Information Graphics 281   
The Patterns 294   
Overview Plus Detail 296   
Datatips 299   
Data Spotlight 303   
Dynamic Queries 308   
Data Brushing 312   
Local Zooming 316   
Sortable Table 320   
Radial Table 323   
Multi-Y Graph 328   
Small Multiples 331   
Treemap 336   
8. Getting Input from Users: Forms and Controls. . . 341   
The Basics of Form Design 341   
Control Choice 344   
The Patterns 356   
Forgiving Format 357   
Structured Format 360   
Fill-in-the-Blanks 362   
Input Hints 364   
Input Prompt 369   
Password Strength Meter 371   
Autocompletion 375   
Dropdown Chooser 380   
List Builder 383   
Good Defaults 385   
Same-Page Error Messages 388   
9. Using Social Media. . . 393   
What This Chapter Does Not Cover 394   
The Basics of Social Media 394   
The Patterns 398   
Editorial Mix 398   
Personal Voices 402   
Repost and Comment 406   
Conversation Starters 410   
Inverted Nano-pyramid 413   
Timing Strategy 416   
Specialized Streams 419   
Social Links 423   
Sharing Widget 426   
News Box 430   
Content Leaderboard 434   
Recent Chatter   
10. Going Mobile . . 441   
The Challenges of Mobile Design 442   
The Patterns 448   
Vertical Stack 449   
Filmstrip 452   
Touch Tools 454   
Bottom Navigation 456   
Thumbnail-and-Text List 459   
Infinite List 462   
Generous Borders 464   
Text Clear Button 467   
Loading Indicators 468   
Richly Connected Apps 470   
Streamlined Branding 473   
11. Making It Look Good: Visual Style and Aesthetics . . 477   
Same Content, Different Styles 479   
The Basics of Visual Design 488   
What This Means for Desktop Applications 496   
The Patterns 498   
Deep Background 499   
Few Hues, Many Values 503   
Corner Treatments 507   
Borders That Echo Fonts 509   
Hairlines 513   
Contrasting Font Weights 516   
Skins and Themes 519   
References . 523   
Index . . 527