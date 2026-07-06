# Bringing Design to Software / Bringing Design to Software / Edited by TERRY WINOGRAD STANFORD UNIVERSITY and INTERVAL RESEARCH CORPORATION / Preface / Origins / Acknowledgments

> Section: preface | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Bringing design to software (Terry Winograd, (ed.))\Bringing design to software (Terry Winograd, (ed.))\Bringing design to software (Terry Winograd, (ed.))\auto\Bringing design to software (Terry Winograd, (ed.)).md

# Bringing Design to Software

TERRY WINOGRAD

![](images/2d3cbc3fa2aa1d3d90ef4bd6d35b35cb46bfdfbdcb1d9b7c07cc4dbcc02c9622.jpg)

BRINGING DESIGN TO SOFTWARE

# Bringing Design to Software

# Edited by TERRY WINOGRAD STANFORD UNIVERSITY and INTERVAL RESEARCH CORPORATION

with John Bennett, Laura De Young, and Bradley Hartfield

![](images/7f6e7a10f2fe31cab4b3e5fe56d175d8f91b39ee80b47a7ff4584e81e0f2d46c.jpg)

ACM PRESS NEW YORK, NEW YORK

![](images/3c4bf6e4546725917ba1a24f433824a27a74a6cdee4f22c0682edb77bfe981fa.jpg)

ADDISON-WESLEY PUBLISHING COMPANY

READING, MASSACHUSETTS MENLO PARK, CALIFORNIA NEW YORK DON MILLS, ONTARIO HARLOW, UNITED KINGDOM AMSTERDAM BONN SYDNEY SINGAPORE TOKYO MADRID SAN JUAN MILAN PARIS

Text designed by Ron Kosciak.

Cover illustrated by John Gamache.

Cover designed by Meredith Nightingale.

Production supervised by Kathleen A. Manley and Sandra Rigney.

This book is published as part of ACM Press Books—a collaboration between the Association for Computing (ACM) and Addison-Wesley Publishing Company. ACM is the oldest and largest educational and scientific society in the information technology field. Through its high-quality publications and services, ACM is a major force in advancing the skills and knowledge of IT professionals throughout the world. For further information about ACM, contact:

ACM Member Services

ACM European Service Center

1515 Broadway, 17th Floor

108 Cowley Road

New York, NY 10036-5701

Oxford OX41JF

Phone: 1-212-626-0500

United Kingdom

Fax: 1-212-944-1318

Phone: +44-1865-382338

E-mail: acmhelp@acm.org

Fax: +44-1865-381338

E-mail: acm\_europe@acm.org

URL: http://www.acm.org

Many of the designations used by manufacturers and sellers to distinguish their products are claimed as trademarks. Where those designations appear in this book, and Addison-Wesley was aware of a trademark claim, the designations have been printed in initial caps or all caps.

Credits appear on page 310

Library of Congress Cataloging-in-Publication Data

Bringing design to software / Terry Winograd . . . [et al.].

p. cm. — (ACM press books)

Includes bibliographical references and index.

ISBN 0-201-85491-0

1. Computer software—Development. I. Winograd, Terry.

II. Series

QA76.76.D47B745 1996

005.1'2—dc20

95-37554 CIP

Copyright © 1996 by ACM Press, A Division of the Association for Computing Machinery, Inc. (ACM).

All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of the publisher. Printed in the United States of America.

# Preface

Software is an ambiguous word. People who talk about software may be thinking about the structure of program components, about the functionality of an application, about the look and feel of an interface, or about the overall user experience of a hardware-software environment. Each of these perspectives brings along its own context of understanding about what matters, what can be designed, and what tools and methods are appropriate.

Design is also an ambiguous word. Among its many meanings, there runs a common thread, linking the intent and activities of a designer to the results that are produced when a designed object is experienced in practice. Although there is a huge diversity among the design disciplines, we can find common concerns and principles that are applicable to the design of any object, whether it is a poster, a household appliance, or a housing development.

In Bringing Design to Software, our goal is to improve the practice of software design, through thinking about design from a broader perspective, and exploring how lessons from all areas of design can be applied to software. We use the word exploring here consciously; what you will read is an open-ended foray into ideas, rather than a how-to handbook of rules and methods. Software design is still a young field, and we are far from having a clear articulation of the relevant principles. Software design is a user-oriented field, and as such will always have the human openness of disciplines such as architecture and graphic design, rather than the hard-edged formulaic certainty of engineering design.

This book brings a collection of diverse perspectives to bear on the common topic of software design. The authors include software designers, designers in other fields, researchers, teachers, software industry executives, and industry analysts. Each chaptcr, in its own way, addresses two key sets of questions.

1. What is design? What happens in designing?

2. How can we improve software by applying a broad understanding of design to our practices in software design?

In communicating their different perspectives, our authors have designed their texts to address readers who have a variety of professional backgrounds and a variety of reasons for interest in software. Our natural audience is the growing group of people who consider themselves software designerspeople who work day by day to produce new software, interfaces, and user experiences. Ultimately, their work is where, to use a popular phrase, the rubber meets the road. Effective software design requires effective software designers, and we address their concerns in both the discussions and the software-design examples given in brief profiles throughout the book.

The individual designer, however, does not represent the whole story of software design. Software designers work in (and with) organizations that include people who manage software development, market software, develop hardware, write documentation, and perform all the other activities needed to get software to users. A deeper understanding of the design process and of the goals of software design can be valuable to everyone engaged in the software enterprise. Many of our chapters and examples have as much to say to the people who manage design organizations as to the people who work within those organizations.

Looking further outside of the immediate design environment, we have included perspectives that address students and researchers in human-computer interaction. Although this book is not primarily a scholarly analysis, we have included a large number of references, and each author has suggested further readings that ground the discussion in the professional literature. In this book, we raise many more questions than we answer, and the pointers to other writing may help readers to seek and develop their own answers.

Expanding our circle still further, we hope that the book will be of interest to professionals in other design disciplines, such as architecture, graphic design, product design, and urban design. In “bringing design to software," we have included chapters by designers from all these fields, exploring how insights from their own disciplines can be brought to bear on software design. Colleagues from these disciplines may find it valuable to see how they might apply their skills to software design, and to reflect on the nature of their own work.

Finally, a pervasive theme of this book is that one group of people is most important in software design—the users. Although our primary focus is on how to do software design well, the book has much to say about the selection, introduction, and use of software. If every buyer and user of software applications has a well-developed understanding of software design, the industry will be forced to respond with betterdesigned software. We want to reach out to this larger audience of people who care about what software can do for them, and to help make the software that is available to them become more appropriate, more usable, and more enjoyable.

Our goal is to make visible what is common and timeless to design, while looking at the world at hand—the cases and examples that make up the tradition of software design in its short history. We have written to communicate with the reflective designer—someone who is driven by practical concerns, and who is also able to take a moment to step back and reflect on what works, what doesn't work and why.

## Origins

This book developed from a workshop on software design in the summer of 1992, organized by the Project on People, Computers, and Design at Stanford University, with support from the National Science Foundation, Interval Research Corporation, and the Association for Software Design. A group of 30 software designers, graphic designers, industrial designers, researchers, and teachers got together for a lively 3-day discussion on what software design is and might be, and on what we could see emerging in each of our disciplines that would hclp us to define and promote new visions of software design. At the end of that workshop, several of the participants agreed to work together on a book that would merge their individual perspectives into a composite picture of software design. Since then, we have gone through an extensive process of prototyping, debugging, and user testing many versions of this book. The result is an integrated collection of essays and interviews, addressing issues and concerns that are.central to the functionality, usability, and value of software.

## Acknowledgments

In any project of this length and scope, many people contribute their knowledge and skills. We have been assisted by colleagues whose understanding and whose work on this volume are truly remarkable. First, and most obviously, the chapter authors have been diligent in revising their contributions, patient in following the book through its changes of direction, and insightful in their writing and comments. The experience of producing this book has been a challenging dialog, in which they have eagerly and actively engaged.

Numerous people were instrumental in creating the original workshop, including the organizing committee—Bradley Hartfield, Mitchell Kapor, David Kelley, Donald Norman, Donald Schön, Andrew Singer, and Terry Winograd—and the conference director, Cynthia Lewis, with assistance from Barry Polley. The other conference participants (in addition to the contributors of chapters to the book) were Jeanne Bamberger (MIT), Nathaniel Borenstein (Bellcore, currently First Virtual), Larry Bucciarelli (MIT), Robert Carr (Autodesk), Parvati Dev (Stanford Medical School), Laird Foshay (Tabula Interactive), Nick Flor (UC San Diego), Chris Graham (Microsoft), John Hestenes (National Science Foundation), Susan Kare (design consultant), Jason Lewis (vivid), Kyle Mashima (Objective Software), Raúl Medina-Mora (Action Technologies), Gary Perlman (Ohio State University), David Rine (George Mason University), Kurt Schmucker (Apple Computer), Lee Sproull (Boston University), Suzanne Stefanac (Macworld), Susan Stucky (Institute for Research on Learning), Bill Verplank (Interval Research), Patrick Whitney (Institute of Design, Illinois Institute of Technology), Sean White (Interval Research), and Kären Wieckert (Stanford University).

The workshop and much of the subsequent work on the book were supported generously by the Interval Research Corporation. Interval's president, David Liddle, deserves a special note of thanks for his consistent and persistent efforts on behalf of this work and for his support of the development of software design in many other ways. Financial support also came from the National Science Foundation, Directorate for Computer and Information Science and Engineering, grant #CDA-9018898.

Valuable editorial assistance and reviews have been provided by Robert Brunner, Allan Bush, Laird Foshay, Jonathan Grudin, Peter Hildebrand, Barbara Knapp, Donald Lindsay, Mary Miller, Barry Polley, Richard Rubinstein, Suzanne Stefanac, Howard Tamler, Bill Verplank, and Sean White. Peter Gordon of Addison-Wesley and Lyn Dupré have been active participants in the development of the book providing the kind of editorial input that authors hope for and rarely get from a publisher.

Finally, switching from the editorial “we" to an individual “I," I can convey only a small part of the tremendous gratitude and admiration I have for my coeditors, John Bennett, Laura De Young, and Brad Hartfield. Each of them has given the kind of dedication and effort that might be expected of a solo editor. They have labored over chapters, read and commented on drafts, worked through dozens of meetings and discussions, and contributed to the manuscript in every possible way. It is a cliché to say“without them it would not have been possible," but, in this case, the assertion is decidedly true. This book is a group production, through and through.

And now the group expands to include you, the reader, whose active participation we invite. We hope that this book will inspire you to add your own perspective—to speak up in the ongoing dialog about what software is, what it can do, and how we can design it more effectively to suit human needs and concerns.

Terry Winograd <Winograd@CS.Stanford.edu>

with John Bennett <Bennett@PCD.Stanford.edu>

Laura De Young <Laura@Windrose.com>

Bradley Hartfield <BradleyH@HartfieldDG.com>

PALO ALTO, CA

