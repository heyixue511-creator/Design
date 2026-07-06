# ANDROID DESIGN PATTERNS

INTERACTION DESIGN SOLUTIONS FOR DEVELOPERS

![](images/bf25fe5b0d8174c80b55a66fabc2dfccd38bad9eca1c81871d6d7f2c2c8ed370.jpg)

GREG NUDELMAN

![](images/c470a3cc2a9599c397172c0858cf55e2e623bece6aa08d9bf24453ba0d2defaa.jpg)

![](images/dbe5945cb4cc60cfc2b25d48738f43b613918344e427d5f9bf029f675a10607c.jpg)

Android<sup>™</sup> Design Patterns

## Android<sup>™</sup> Design Patterns

Interaction Design Solutions for Developers

Greg Nudelman

WILEY

## Android<sup>™</sup> Design Patterns: Interaction Design Solutions for Developers

Published by   
John Wiley & Sons, Inc.   
10475 Crosspoint Boulevard Indianapolis, IN 46256   
www.wiley.com

Copyright © 2013 by John Wiley & Sons, Inc., Indianapolis, Indiana Published simultaneously in Canada

ISBN: 978-1-118-39415-1 ISBN: 978-1-118-41755-3 (ebk) ISBN: 978-1-118-43934-0 (ebk) ISBN: 978-1-118-65058-5 (ebk)

Manufactured in the United States of America

## 10 9 8 7 6 5 4 3 2 1

No part of this publication may be reproduced, stored in a retrieval system or transmitted in any form or by any means, electronic, mechanical, photocopying, recording, scanning or otherwise, except as permitted under Sections 107 or 108 of the 1976 United States Copyright Act, without either the prior written permission of the Publisher, or authorization through payment of the appropriate per-copy fee to the Copyright Clearance Center, 222 Rosewood Drive, Danvers, MA 01923, (978) 750-8400, fax (978) 646-8600. Requests to the Publisher for permission should be addressed to the Permissions Department, John Wiley & Sons, Inc., 111 River Street, Hoboken, NJ 07030, (201) 748-6011, fax (201) 748-6008, or online at http://www.wiley .com/go/permissions.

Limit of Liability/Disclaimer of Warranty: The publisher and the author make no representations or warranties with respect to the accuracy or completeness of the contents of this work and specifically disclaim all warranties, including without limitation warranties of fitness for a particular purpose. No warranty may be created or extended by sales or promotional materials. The advice and strategies contained herein may not be suitable for every situation. This work is sold with the understanding that the publisher is not engaged in rendering legal, accounting, or other professional services. If professional assistance is required, the services of a competent professional person should be sought. Neither the publisher nor the author shall be liable for damages arising herefrom. The fact that an organization or Web site is referred to in this work as a citation and/or a potential source of further information does not mean that the author or the publisher endorses the information the organization or website may provide or recommendations it may make. Further, readers should be aware that Internet websites listed in this work may have changed or disappeared between when this work was written and when it is read.

For general information on our other products and services please contact our Customer Care Department within the United States at (877] 762-2974, outside the United States at (317] 572-3993 or fax (317] 572-4002

Wiley publishes in a variety of print and electronic formats and by print-on-demand. Some material included with standard print versions of this book may not be included in e-books or in print-on-demand. If this book refers to media such as a CD or DVD that is not included in the version you purchased, you may download this material at http://booksupport.wiley.com. For more information about Wiley products, visit www.wiley.com.

## Library of Congress Control Number: 2012956395

Trademarks: Wiley and the Wiley logo are trademarks or registered trademarks of John Wiley & Sons, Inc. and/or its affiliates, in the United States and other countries, and may not be used without written permission. Android is a trademark of Google, Inc. All other trademarks are the property of their respective owners. John Wiley & Sons, Inc. is not associated with any product or vendor mentioned in this book.

For Katie and Juliette: Let your dream be the golden compass you live your life by.

## A bou t t he Au t hor

Greg Nudelman believes in designing what works. His first experience with designing for mobile came when he joined the SkunkWorks team that created the original eBay mobile app that today generated more than \$5 billion in revenue.

For more than 15 years, Greg helped craft cross-platform digital experiences for today’s top Fortune 500 companies, non-profits, and startups: eBay, WebEx, Wells Fargo, Safeway/Vons, Cisco, IBM, Groupon, Associated Press, the U.S. Patent Office, and many others.

Greg is the author of Designing Search: UX Strategies for eCommerce Success (Wiley, 2011), which has a solid 5-star rating on Amazon. The book includes 19 perspectives from today’s top names in search (a fact that Greg is particularly proud of).

Greg has contributed chapters and perspectives to the following publications:

■ Mobile Design Patterns (Smashing Media, 2012)

The Mobile Book (Smashing Media, 2013)

Designing the Search Experience, Tony Russell-Rose and Tyler Tate (2013, Morgan-Kaufmann)

■ Search Analytics for Your Site, Lou Rosenfeld (Rosenfeld Media, 2011)

Greg’s work on storyboarding tablet transitions was featured recently in Rachel Hinman's The Mobile Frontier (Rosenfeld Media, 2012).

Greg has authored more than 30 industry articles on mobile and tablet design and digital design strategy for leading industry magazines: Smashing Magazine, Boxes and Arrows, JavaWorld, ASP.NET Pro, UXmatters, and UXMagazine.

He is a FatDUX, Rosenfeld Media, Wiley, and eConsultancy affiliate and workshop leader, and he has taught design workshops at Marquette University, HULT Business School, Associated Press, and Wells Fargo.

Greg is an internationally acclaimed speaker, with repeated appearances and soldout workshops at leading industry events such as Adaptive Path’s UXWeek, SXSW, MobX, IA Summit, WebVisions, Design4Mobile, Search Engine Summit, Enterprise Search Summit, Net Squared Conference, DrawCamp, and SketchCamp.

He is a co-founder of the UX SketchCamp movement with the landmark UX SketchCamp SF 2011 event. Greg’s cross-platform design strategy consulting company, DesignCaffeine, Inc., is based in the San Francisco Bay Area.

## C r e di t s

Executive Editor Robert Elliott

Project Editor Charlotte Kughen, The Wordsmithery LLC

Vice President and Executive   
Group Publisher   
Richard Swadley

Technical Editor Ambrose Little

Vice President and Executive   
Publisher   
Neil Edde

Associate Publisher Jim Minatel

Production Editor Christine Mugnolo

Project Coordinator, Cover Katie Crocker

Copy Editor San Dee Phillips

Editorial Manager Mary Beth Wakefield

Compositor   
Maureen Forys,   
Happenstance Type-O-Rama

Freelancer Editorial Manager Rosemarie Graham

Proofreader Nancy Carrasco

Associate Director of Marketing David Mayhew

Indexer Johnna VanHoose Dinse

Marketing Manager Ashley Zurcher

Cover Image Greg Nudelman

Business Manager Amy Knies

Cover Designer Ryan Sneed

Production Manager Tim Tate

## Ack no w l ed gmen t s

To anyone who's never written a book it is difficult to imagine the blood, sweat, and tears required to finish one. I wish to acknowledge the generous help of my agent, Neil Salkind of Studio B as well as my fantastic team at Wiley: Charlotte Kughen and Ambrose Little. Any inaccuracies in the book are my own and no fault of theirs. Also, I'd like to thank Robert Elliott, from whose creative mind the idea for this book idea was initially born. I also want to acknowledge generous help provided by Kimberly Johnson, who helped decipher and sort out key Android visual design themes. Last, but definitely not least, I want to thank my family for their strong support and continual tolerance during this time of missed family commitments, forgotten appointments, and general mental fog surrounding the focused time of book writing.

## C o n t en t s a t a G l a n c e

Foreword xix   
Introduction xxi   
Part I: UX Principles and Android OS Considerations 1   
Chapter 1: Design for Android: A C ase Study 3   
Chapter 2: W hat M akes Android Different 25   
Chapter 3: Android Fragmentation 41   
Chapter 4: M obile Design Process 55   
Part II: Android Design Patterns and Antipatterns 69   
Chapter 5: W elcome Experience 71   
Chapter 6: H ome Screen 87   
Chapter 7: Search 113   
Chapter 8: Sorting and Filtering 149   
Chapter 9: Avoiding M issing and Undesirable Results 179   
Chapter 10: Data Entry 197   
Chapter 11: Forms 251   
Chapter 12: M obile B anking 307   
Chapter 13: Navigation 347   
Chapter 14: Tablet Patterns 391   
Index 413

## C o n t en t s

Foreword xix   
Introduction xxi   
Part I: UX Principles and Android OS Considerations 1   
Chapter 1: Design for Android: A C ase Study 3   
Launch Icon . 4   
Action Bars and Information Architecture 5   
Tabs . 11   
Dedicated Selection Page 11   
Select Control 12   
Buttons 14   
Search Results 15   
Result Detail . 19   
Bringing It All Together 22   
Chapter 2: W hat M akes Android Different 25   
Welcome to Flatland . 26   
Tap Anywhere 28   
Right-Size for Every Device 30   
Mobile Space, Unbound . 33   
Think Globally, Act Locally 36   
Chapter 3: Android Fragmentation 41   
What’s Fragmentation? 42   
Everything Is in Time and Passes Away 42   
Android Device Trends 43   
Celebrate Fragmentation 53   
Chapter 4: M obile Design Process 55   
Observe Human-Mobile Interaction in the Real World 56   
Your Prototyping Methods Must Allow for Variety in Form Factors 56   
Your User Testing Must Allow People to Explore the Natural Range   
of Motion, Voice, and Multitouch 57   
Touch Interfaces Embody Simplicity and Sophistication 57   
Delight Is Mandatory . 58   
Tell a Complete Story—Design for Cross-Channel Experiences 58   
Mobile Design Case Study 59   
Part II: Android Design Patterns and Antipatterns 69   
Chapter 5: W elcome Experience 71   
5.1 Antipattern: End User License Agreements (EULAs) 72   
5.2 Antipattern: Contact Us Impediments 74   
5.3 Antipattern: Sign Up/Sign In . 77   
5.4 Pattern: Welcome Animation 80   
5.5 Pattern: Tutorial 83   
Chapter 6: H ome Screen 87   
6.1 Pattern: List of Links 88   
6.2 Pattern: Dashboard 92   
6.3 Pattern: Updates . 95   
6.4 Pattern: Browse 99   
6.5 Pattern: Map . 103   
6.6 Pattern: History 108   
Chapter 7: Search 113   
7.1 Pattern: Voice Search . 114   
7.2 Pattern: Auto-Complete and Auto-Suggest 120   
7.3 Pattern: Tap-Ahead 126   
7.4 Pattern: Pull to Refresh 129   
7.5 Pattern: Search from Menu 132   
7.6 Pattern: Search from Action Bar 135   
7.7 Pattern: Dedicated Search 138   
7.8 Pattern: Search in the Content Page 141   
7.9 Antipattern: Separate Search and Refinement 144   
Chapter 8: Sorting and Filtering 149   
8.1 Antipattern: Crippled Refinement . 150   
8.2 Pattern: Refinement Page 153   
8.3 Pattern: Filter Strip 160   
8.4 Pattern: Parallel Architecture 164   
8.5 Pattern: Tabs . 170   
Chapter 9: Avoiding M issing and Undesirable Results 179   
9.1 Antipattern: Ignoring Visibility of System Status 180   
9.2 Antipattern: Lack of Interface Efficiency 182   
9.3 Antipattern: Useless Controls 184   
9.4 Pattern: Did You Mean? 185   
9.5 Pattern: Partial Match 189   
9.6 Pattern: Local Results 192   
Chapter 10: Data Entry 197   
10.1 Pattern: Slider 198   
10.2 Pattern: Stepper 204   
10.3 Pattern: Scrolling Calendar 210   
10.4 Pattern: Date and Time Wheel 215   
10.5 Pattern: Drop Down . 224   
10.6 Pattern: Multiple Select . 228   
10.7 Pattern: Free-Form Text Input and Extract 232   
10.8 Pattern: Textbox with Input Mask 238   
10.9 Pattern: Textbox with Atomic Entities 247   
Chapter 11: Forms 251   
11.1 Pattern: Inline Error Message 252   
11.2 Pattern: Toast Alert . 257   
11.3 Pattern: Pop-up Alert 263   
11.4 Pattern: Callback Validation . 271   
11.5 Pattern: Cancel/OK . 274   
11.6 Pattern: Top-Aligned Labels . 285   
11.7 Pattern: Getting Input from the Environment 293   
11.8 Pattern: Input Accelerators 302   
Chapter 12: M obile B anking 307   
12.1 Pattern: Login Accelerator 308   
12.2 Pattern: Dedicated Selection Page 316   
12.3 Pattern: Form First . 321   
12.4 Pattern: Dedicated Pages Wizard Flow 324   
12.5 Pattern: Wizard Flow with Form . 329   
12.6 Pattern: Verification-Confirmation 334   
12.7 Pattern: Near Field Communication (NFC) 338   
Chapter 13: Navigation 347   
13.1 Antipattern: Pogosticking 348   
13.2 Antipattern: Multiple Featured Areas 349   
13.3 Pattern: Carousel 352   
13.4 Pattern: Popover Menu 358   
13.5 Pattern: Watermark . 365   
13.6 Pattern: Swiss-Army-Knife Navigation 371   
13.7 Pattern: Integration: The Final Frontier 383   
Chapter 14: Tablet Patterns 391   
14.1 Pattern: Fragments . 392   
14.2 Pattern: Compound View 394   
14.3 Experimental Pattern: Side Navigation 396   
14.4 Pattern: Content as Navigation/Multitouch Gestures 401   
14.5 Pattern: 2-D More Like This . 404   
14.6 Experimental Pattern: C-Swipe . 408   
Index 413

## Fore word

The first thing Greg told me when we met was, “You wrote the book I was working on,” referring to the book Mobile Design Pattern Gallery that I had just released with O’Reilly Media (2012). I felt a little guilty at the time, but now I am glad I beat him to it. But not for the reasons you might think.

When I started the pattern gallery, I focused on identifying universal design patterns across the six major mobile platforms. Two years later, the industry is maturing, and only three big players are left, each with their own distinct patterns and principles. Universal patterns are still valuable, but more valuable yet are the deep dives into specific operating systems.

Greg saw this coming and decided to focus on the fastest growing platform, Android, and the most sophisticated release yet, Jelly Bean. His book meets mobile designers and developers where they are most comfortable and expertly guides them towards mastery of mobile user experience.

This book is more of a workshop than a reference book. Greg builds upon the universal design patterns for mobile devices and tablets and the Android UI design guidelines and takes the topic further into hands-on practical applications of the design principles. Each section covers fundamentals, warns of pitfalls and antipatterns, and then puts the lessons to the test by showing in detail how to redesign an existing app. You can and should bring this book to design sessions, and you should share it with your team. You will save countless hours solely from using the patterns in Chapter 7, “Search,” and Chapter 8, “Sorting and Filtering.” By reading and using Greg’s entire book you will tremendously improve all aspects of the mobile experience you will be creating for your customers.

Bottom line, there is no other resource out there that goes to this level of depth on Android application design. I just hope Greg writes a Windows pattern book next.

Enjoy,

Theresa Neil

UX Designer, Start-up Advisor, Author/Speaker

Theresa Neil Interface Designs (www.theresaneil.com)