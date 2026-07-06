# THEELEMENTS USER EXPERIENCE

SECOND EDITION

USER-CENTERED DESIGN

FOR THE WEB AND BEYOND

## The Elements of User Experience: User-Centered Design for the Web and Beyond, Second Edition

Jesse James Garrett

New Riders1249 Eighth Street   
Berkeley, CA 94710   
510/524-2178   
510/524-2221 (fax)

Find us on the Web at: www.newriders.com

To report errors, please send a note to errata@peachpit.com

New Riders is an imprint of Peachpit, a division of Pearson Education.

Copyright © 201l by Jesse James Garrett

Project Editor: Michael J. Nolan

Development Editor: Rose Weisburd

Production Editor: Tracey Croom

Copyeditor: Doug Adrianson

Proofreader: Gretchen Dykstra

Indexer: Valerie Perry

Cover Designer: Aren Howell Straiger

Interior Designer: Kim Scott

Compositor: Kim Scott

## Notice of Rights

All rights reserved. No part of this book may be reproduced or transmitted in any form by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of the publisher. For information on getting permission for reprints and excerpts, contact permissions@peachpit.com.

## Notice of Liability

The information in this book is distributed on an “As Is" basis without warranty. While every precaution has been taken in the preparation of the book, neither the author nor Peachpit shall have any liability to any person or entity with respect to any loss or damage caused or alleged to be caused directly or indirectló by the instructions contained in this book or by the computer software and hardware products described in it.

## Trademarks

Many of the designations used by manufacturers and sellers to distinguish their products are claimed as trademarks. Where those designations appear in this book, and Peachpit was aware of a trademark claim, the designations appear as requested by the owner of the trademark. All other product names and services identified throughout this book are used in editorial fashion only and for the benefit of such companies with no intention of infringement of the trademark. No such use, or the use of any trade name, is intended to convey endorsement or other affiliation with this book.

ISBN 13: 978-0-321-68368-7   
ISBN 10:0-321-68368-4

For my wife, Rebecca Blood Garrett, who makes all things possible.

## Table of Contents

Jser Experience and Why It Matters 2   
Everyday Miseries 3   
Introducing User Experience 4   
From Product Design to User Experience Design 7   
Designing (for) Experience: Use Matters 8   
User Experience and the Web 9   
Good User Experience Is Good Business 12   
Minding Your Users 17   
he Elements 18   
The Five Planes 19   
The Surface Plane 20   
The Skeleton Plane 20   
The Structure Plane 20   
The Scope Plane 21   
The Strategy Plane 21   
Building from Bottom to Top 21   
A Basic Dualitó 25   
The Elements of User Experience 28   
The Strategy Plane 28   
The Scope Plane 29   
The Structure Plane 30   
The Skeleton Plane 30   
The Surface Plane 30   
Using the Elements 31   
The Strategy Plane   
Product Objectives and User Needs 34   
Defining the Strategy 36   
Product Objectives 37   
Business Goals 37   
Brand Identity 38   
Success Metrics 39   
User Needs 42   
User Segmentation 42   
Usability and User Research 46   
Creating Personas 49   
Team Roles and Process 52   
The Scope Plane   
Functional Specifications and Content Requirements 56   
Defining the Scope 58   
Reason #l: So You Know What   
You're Building 59   
Reason #2: So You Know What   
You're Not Building 60   
Functionality and Content 61   
Defining Requirements 65   
Functional Specifications 68   
Writing It Down 69   
Content Requirements 7I   
Prioritizing Requirements 74   
CHAPTER 5   
The Structure Plane   
Interaction Design and Information Architecture 78   
Defining the Structure 80   
lnteraction Design 81   
Conceptual Models 83   
Error Handling 86   
lnformation Architecture 88   
Structuring Content 89   
Architectural Approaches 92   
Organizing Principles 96   
Language and Metadata 98   
Team Roles and Process 101   
CHAPTER 6   
The Skeleton Plane   
Interface Design, Navigation Design,   
and Information Design 106   
Defining the Skeleton 108   
Convention and Metaphor 110   
lnterface Design 114   
Navigation Design 118   
lnformation Design 124   
Wayfinding 127   
Wireframes 128   
CHAPTER 7   
The Surface Plane   
Sensory Design 132   
Defining the Surface 134   
Making Sense of the Senses 135   
Smell and Taste 135   
Touch 135   
Hearing 136   
Vision 136   
Follow the Eye 137   
Contrast and Uniformity 139   
Internal and External Consistency 143   
Color Palettes and Typography 145   
Design Comps and Style Guides 148   
CHAPTER 8   
The Elements Applied 152   
Asking the Right Questions 157   
The Marathon and the Sprint 159   
Index 164

![](images/7bc24872af8d70f53e77811535bf17bb9d0912e298c74a6e1e105c74669bf20b.jpg)

![](images/a80c46521149cbd27205647f5cf9b896f872e1ef9d862b3abf1f6b0106a81b0b.jpg)

![](images/52c84813a05ee4c90575d49ee331f518cca7ee872ce564e72447cca22835f079.jpg)

![](images/3b2d39af0231bb491bf91dacaee880f41ccf50e997162f482094c2268dc5561d.jpg)

![](images/0da9eb6a5efc73884371a54d9861b761170554776fba86383b3c7aa0b8655d9d.jpg)

![](images/67fabe8e277673ec093880e4e34ba5165b1aeb9122a05409a9890be813f9bd56.jpg)  
Photo by: Colin Peck

## About the Author

Jesse James Garrett is one of the founders of Adaptive Path, a user experience consultancy based in San Francisco. Since 1995, Jesse has worked on Web projects for companies such as AT&T, Intel, Boeing, Motorola, Hewlett-Packàrd,and National Public Radio. His contributions to the field of user experience include the Visual Vocabulary, an open notation system for information architecture documentation that is now used by organizations around the world. His personal site at www.jjg.net is one of the Web's most popular destinations for information architecture resources, and he is a frequent speaker on information architecture and user experience issues.

## Acknowledgements for the Second Edition

Michael Nolan spent years prodding me to do a second edition. His persistence—and his ingenuity in finally coming up with an offer I couldn't pass up—are the reasons it exists at all.

At New Riders, the team of Rose Weisburd, Tracey Croom, and Kim Scott kept me on track. Nancy Davis, Charlene Will, Hilal Sala, and Mimi Vitetta helped in making things go. Thanks also to Samantha Bailey and Karl Fast for their support.

My wife, Rebecca Blood Garrett, remains my first, last, and most trusted editor, advisor, and confidant.

New additions to the musical score this time around were Japancakes, Mono, Maserati, Tarentel, Sleeping People, Codes in the Clouds, and (especially) Explosions in the Sky. Very special thanks to Steve Scarborough of Maserati for musical guidance.

## Acknowledgements for the First Edition

Don't let the number of names on the cover fool you—it takes a lot of people to make a book happen.

First, I have to thank my partners at Adaptive Path: Lane Becker, Janice Fraser, Mike Kuniavsky, Peter Merholz, Jeffrey Veen, and Indi Young. It is through their indulgence that I was able to take on this project at all.

Then there's everyone at New Riders, particularly Michael Nolan, Karen Whitehouse, Victoria Elzey, Deborah Hittel-Shoaf, John Rahm, and Jake McFarland. Their guidance was essential to this process.

Kim Scott and Aren Howell lent a keen eye and attention to detail to the design of this book. Their patience with suggestions from the author was especially laudable.

Molly Wright Steenson and David Hoffer provided invaluable insight in their review of my manuscript. Every author should be so lucky.

Jess McMullin turned out to be my toughest critic in many ways, and this book is immeasurably improved by his influence.

Thanks are also due to the more experienced authors who gave me advice on how to tackle a project like this and maintain my sanity: Jeffrey Veen (again), Mike Kuniavsky (again), Steve Krug, June Cohen, Nathan Shedroff, Louis Rosenfeld, Peter Morville, and (especially) Steve Champeon.

Others who offered valuable suggestions or simply good moral support included Lisa Chan, George Olsen, Christina Wodtke, Jessamyn West, Samantha Bailey, Eric Scheid, Michael Angeles, Javier Velasco, Antonio Volpon, Vuk Cosic, Thierry Goulet, and Dennis Woudt. They thought of things I didn't, and that makes them the best kind of colleagues.

Musical accompaniment for the writing process was provided by Man or Astro-man?, Pell Mell, Mermen, Dirty Three, Trans Am, Tortoise, Turing Machine, Don Caballero, Mogwai, Ui, Shadowy Men on a Shadowy Planet, Do Make Say Think, and (especially) Godspeed You Black Emperor!

Finally, there are three people without whom this book would never have happened: Dinah Sanders, who at a party one warm Texas night insisted there was someone I had to meet; my wife, Rebecca Blood, who makes me stronger and wiser in every way; and Daniel Grassam, without whose friendship, encouragement, and support I might not have found my way into this business at all. Thank you.