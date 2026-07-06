# Field Methods Casebook for Software Design

Edited by: Dennis Wixon Judith Ramey

WILEY COMPUTER PUBLISHING

![](images/76312e134bf1314d3f25a9c051195afd263ff30cb2480d9d0f483ee67019a460.jpg)

John Wiley & Sons, Inc. • New York • Chichester • Brisbane • Toronto • Singapore • Weinheim

![](images/887f9b100d2c91519067a8c1035e6a37b4a6a62d2e484a5bdab5f20aa69940e7.jpg)

Publisher: Katherine Schowalter   
Senior Editor: Marjorie Spencer   
Managing Editor: Micheline Frederick   
Text Design & Composition: Publishers' Design and Production Services, Inc.

Designations used by companies to distinguish their products are often claimed as trademarks. In all instances where John Wiley & Sons, Inc., is aware of a claim, the product names appear in initial capital or all capital letters. Readers, however, should contact the appropriate companies for more complete information regarding trademarks and registration.

This text is printed on acid-free paper.

Copyright © 1996 by John Wiley & Sons, Inc.

All rights reserved. Published simultaneously in Canada.

This publication is designed to provide accurate and authoritative information in regard to the subject matter covered. It is sold with the understanding that the publisher is not engaged in rendering legal, accounting, or other professional service. If legal advice or other expert assistance is required, the services of a competent professional person should be sought.

Reproduction or translation of any part of this work beyond that permitted by section 107 or 108 of the 1976 United States Copyright Act without the permission of the copyright owner is unlawful. Requests for permission or further information should be addressed to the Permissions Department, John Wiley & Sons, Inc.

## Library of Congress Cataloging-in-Publication Data:

Field methods casebook for software design / edited by Dennis Wixon, Judith Ramey.

p. cm.

Includes bibliographical references (p. ).

ISBN 0-471-14967-5 (cloth : alk. paper)

1. Computer software—Development. 2. System design. I. Wixon, Dennis. II. Ramey, Judith.

QA76.76.D47F541996

004.2'1'019—dc20

96-13746 CIP

![](images/19a2c23f53e895c5b826a4d073e437cc505dc32e62c167cd985b993c7703479c.jpg)

Dennis Wixon dedicates this book to JoAnne, Michael, Amy, and Ella.

Judy Ramey dedicates this book to Lindell and Frances Ramey, and the rest of my family in Texas.

Dennis would like to thank John Whiteside for introducing me to usability and teaching me to look beyond the surface of things. I would also like to thank Sandy Jones, Karen Holtzblatt, and Minette Beabes for expanding my horizons on how to understand peoples'work. Finally, I would like to acknowledge my current supervisor Pat Baker for her support and guidance. I have learned much from her.

Judy would like to thank Ernest Kaulbach and other medievalists at the University of Texas who first taught me how to study a culture, and Wayne Verona and the other technical communicators at Texas Instruments Incorporated who taught me that a culture didn't have to be dead to be worth studying. I would also like to thank my colleagues in the Department of Technical Communication at the University of Washington for putting up with me and my lab with such good humor.

We also thank our Marjorie Spencer, our editor at John Wiley, and Margaret Hendrey, our editorial assistant.

Wixon (Ramey) attributes all errors and omissions to Ramey (Wixon).

## Preface

![](images/df3176a9cb3a67208f902e41233557c0718febdd8fe417a45b973bcb70ace125.jpg)

It's not what you know that's dangerous. It's what you know that just ain't so. —Will Rogers

## ASSUMPTIONS AS THE ORIGIN OF DESIGN

Design begins with assumptions about users and their work. These assumptions are either explicit or implicit; they are either well-founded or not well-founded. But, they always exist, and they always guide development. Those assumptions we make about the users and their work can take many forms and exist at many levels. At the lowest level, assumptions can be very explicit: "No one needs more than a VGA screen." At the highest level, they can compress many assumptions into a single assertion: "Our users are knowledge workers." Regardless of the type of assumption, they all share one characteristic: They can be wrong.

## How Do We Know?

How can we be sure that our assumptions are well-founded? Because assumptions can be implicit, an even more basic question is “How do we know what we are assuming?" One way to test assumptions is to build something (a product, a tool, an artifact) and then test it. While that approach is guaranteed to work, it can be expensive. An analogous situation existed when the first iron bridges were built for railroads. The only way to be sure they would work was to drive trains over them and see if they collapsed.

One answer is to reduce the cost of "learning by testing" (through, say, the use of paper prototypes). Another is to look for processes that test our assumptions earlier in the process. Or we can go back even further and look for processes that will help shape the assumptions we make, Field research methods are aimed at generating this kind of upfront understanding. Thus they function best at the early stages of design, where leverage is high. They also function best where we know the least; that is, where we are designing for new markets or for users who are unlike us.

## Why This Book?

This book is intended for the practitioner, and in it we seek to answer three questions:

1. What is field research?

2. Why (when) should I use it?

3. How do I do it?

The form of our answer is a set of case studies. We choose this approach to provide the maximum amount of detail and the greatest range of variety. In our view, detail is important because it gives the practitioner a deeper understanding of the methods in action. Maximum variety means that the cases are more likely to match real situations that you confront. The variety is also reflected in the way the cases are described. Some cases concentrate the nuts and bolts of actually doing field research. Others concentrate on how the data is shared so that it impacts design. Still other cases look at the organizational context in which such work takes place. Others place the kind of applied field research we do in a broader context, such as Ethnography, Participatory Design, or Contextual Design.

## Is This Book For You?

If you've read this far, then the answer probably is yes, but you can get a better sense of what's really in the book by leafing through the chapters and skimming the executive summary included at the beginning of each chapter.

We hope that this book will promote the use of applied field research for product design and the evolution of field research methodology. We believe that these methods represent some of the most effective ways to design from a user's point of view.

## Contents

![](images/a2d0fc2b99d01f51f56c4160435fbeee3ba5f5cbe467cea53741fc9aeedec8dd.jpg)

About the Authors xvii   
Introduction xxiii   
Adaption of an Ethnographic Method for Investigation   
of the Task Domain in Diagnostic Radiology   
—Judith Ramey, Alan H. Rowberg, Carol Robinson   
Executive Summary 1   
Introduction 2   
Objectives   
Overview of Methods: "Grounded" Investigation 4   
Details of the Key Method: Stream-of-Behavior Chronicles   
and Their Analysis 6   
Summary of Selected Results: Interpretive Diagnostic   
Activities 8   
Conclusions 13   
Acknowledgments 14   
Notes 14   
2 Using the CARD and PICTIVE Participatory Design   
Methods for Collaborative Analysis 17   
—Michael J. Muller, Rebecca Carr   
Executive Summary 17   
Introduction 17   
Background 18   
Planning the Study 18   
Conducting the Study 21   
Analyzing and Interpreting the Data 25   
Impacting the Design 29   
Assessing the Cost/Benefit 30   
Reflecting on Our Experience 30   
References 32   
The Ethnographic Interview in User-Centered   
Work/Task Analysis 35   
—Larry E. Wood   
Executive Summary 35   
Background 35   
Guiding Principles and Working Assumptions 36   
Interviewing Strategies 39   
Work Model Validation 48   
Summary 49   
Acknowledgments 50   
References 51   
Example—Interview Analysis and Work Model   
Development 52   
Changing the Rules: A Pragmatic Approach   
to Product Development 57   
—Dennis R. Wixon, Christine M. Pietras,   
Paul K. Huntwork, Douglas W. Muzzey   
Executive Summary 57   
Background 57   
What We Did 63   
What We Learned 71   
Response from Customers 84   
Reflections 85   
Acknowledgments 87   
References 88   
The Delta Method—A Way to Introduce Usability 91   
—Martin Rantzer   
Executive Summary 91   
Background 92   
The Development of the Delta Method 92   
The Method Purpose 94   
The Structure of the Design Group 96   
The Role of Delta in the System Design Process 96   
The Delta Method—In Theory and Practice 99   
Summary 110   
Acknowledgments 111   
References 112   
Exploring the Design of a Sales   
Automation Workstation   
Using Field Research 113   
—Robert C. Graf, Ph.D.   
Executive Summary 113   
Background 114   
Planning the Study 114   
Conducting the Study 116   
Analyzing and Interpreting the Data 117   
Impacting the Design 120   
Assessing the Cost/Benefit 122   
Reflecting on the Experience 122   
Acknowledgments 123   
References 123   
7 Organizational Considerations in   
Field-Oriented Product Development:   
Experiences of a Cross-Functional Team 125   
—David E. Rowley   
Executive Summary 125   
Background 125   
Makeup of a Product Line Team 127   
Acquiring Skills 128   
Gaining Experience 129   
Planning and International Study 129   
Conducting the Study 130   
Introducing Prototypes 133   
Keeping Things in Perspective 134   
Too Many Notes 135   
Opportunities for Improvement 137   
The Product Development Partnership 137   
Assessing the Cost and Benefit 139   
Looking Ahead 141   
Acknowledgments 143   
References 143   
8 A Day in the Life of a Family: An International   
Ethnographic Study 145   
—Susan M. Dray, Deborah Mrazek   
Background 145   
Planning the Study 146   
Conducting the Study 149   
Reflecting on the Experience 152   
Conclusions 155   
Acknowledgments 155   
References 156   
The Challenges of User Based Design in a Medical   
Equipment Market 157   
—Diane S. Brown   
Executive Summary 157   
Background 157   
Why Do Field Studies? 160   
Conducting the Field Studies 161   
Analyzing and Interpreting the Data 168   
Generating Design Requirements 171   
Impacting the Design 172   
Assessing the Cost/Benefit 173   
Reflecting on the Experience 174   
Acknowledgments 175   
References 175   
10 "You've Got Three Days!" Case Studies in the Field   
Techniques for the Time-Challenged 177   
—Kristin Bauersfeld, Shannon Halgren   
Executive Summary 177   
Background 177   
Technique 1: Condensed Ethnographic Interview 179   
Technique 2: Passive Video Observation 181   
Technique 3: Interactive Feature Conceptualization 183   
Case Study 1: Understanding User Processes 185   
A Typical Visit 186   
Conclusion 193   
Future Work 194   
References 195   
11 User-Centered Design in a Commercial Software   
Company 197   
—Stanley R. Page   
Executive Summary 197   
Background 197   
Planning the Study 198   
Conducting the Study 199   
Structuring the Data 202   
Expanding the Focus 205   
Communication Between Teams 208   
Implementing Ideas 209   
Lessons Learned 211   
Conclusions 212   
References 212   
12 Using Field-Oriented Design Techniques to Develop   
Consumer Software Products 215   
—Dianne Juhl   
Executive Summary 215   
Background 216   
Planning the Study 218   
Conducting the Study 220   
Recording and Analyzing the Data 221   
Reporting the Results 223   
Impacting Product Design 225   
Future Work 226   
Conclusion 226   
References 228   
13 Using Contextual Inquiry to Discover Physicians'   
True Needs 229   
—Janette M. Coble, MS; Judy S. Maffit;   
Matthew J. Orland, MS; Michael G. Kahn, MS, Ph.D.   
Executive Summary 229   
Background of the Study 229   
Planning the Study 230   
Conducting the Study 231   
Impacting the Design 243   
Assessing the Cost/Benefit 245   
Reflections 246   
Acknowledgments 247   
References 247   
14 Bringing the Users' Work to Us: Usability   
Roundtables of Lotus Development 249   
—Mary Beth Butler, Marie Tahir   
Executive Summary 249   
Background 250   
Planning our Studies 252   
Conducting the Studies 254   
Capturing, Analyzing, and Interpreting the Data 256   
Benefits of Usability Roundtables 257   
Challenges and Limitations of Usability Roundtables 258   
Future Directions 260   
Conducting a Study: A Case Study 260   
15 An Overview of Ethnography and System Design 269   
—John M. Ford, Larry E. Wood   
Executive Summary 269   
A Brief Overview of Ethnography 269   
Traditional System-Centered Design 272   
From System-Centered to Client-Centered Design 273   
Current Ethnographic Approaches to System Design 276   
Future Trends 279   
References 280   
16 Introduction to Participatory Design 283   
—Aki Helen Namioka, Christopher Rao   
Introduction 283   
Concepts and Features of Participatory Design 283   
History of Participatory Design 285   
Participatory Design Techniques 287   
Conclusion 298   
References 298   
17 Contextual Design: Principles and Practice 301   
—Karen Holtzblatt, Hugh Beyer   
Introduction 301   
Background of Contextual Design 302   
Creating the Project 304   
Understanding the Customer 307   
Consolidation Across Users 318   
Systemic Design 323   
Customer-Centered Design in the Organization 330   
Notes 332   
References 332   
Index 335

![](images/a6104bb0f818b5797b52af215db1d238c8c43b32056ccdb0811398b5b33d93c3.jpg)

## About the Authors

Note: The Authors' biographies are listed in order of the appearance of the author's work within the text.

Judith Ramey joined the faculty of the Department of Technical Communication, College of Engineering, University of Washington, in 1983. In 1989 she founded the UW Laboratory for Usability Testing and Evaluation (LUTE), and since then has served as its director. Through LUTE, she has conducted a number of corporate-sponsored research projects, including the medical imaging study described here.

Dr. Alan H. Rowberg, MD is an associate professor and Director of the Picture Archiving and Communication System (PACS) Section, Department of Radiology, University of Washington Health Sciences Center.

Carol Robinson has a M.S. in Technical Communication and has done usability work for a number of software companies. Currently Carol is a Usability Analyst for Health Systems Technologies, a company that makes software for managed care organizations.

Michael J. Muller is a Work and Usability Analyst in the Collaborative Systems group within the Applied Research organization of U S WEST Advanced Technologies.

Rebecca Carr is a Methods/Training Developer in the Operator and Information Services organization of U S WEST Communications.

Larry E. Wood has a Ph.D. in Cognitive Psychology and is currently a Professor of Psychology at Brigham Young University. For several years he has taught a graduate course in User-Centered Design. His research interests include all aspects of User-Centered Design of software applications.

Dennis R. Wixon is Usability Program Manager for Digital Equipment Corporation. Over the past 20 years, Dennis has worked on interface design and evaluation methodology. He holds an M.A. and Ph.D. from Clark University, and has published numerous papers on interface design.

Christine M. Pietras is a human factors consultant specializing in user interface design and usability evaluation. She is currently developing an interface style guide with a major transportation company. Previously Chris worked at Digital Equipment, where she collaborated in designing business solutions. Chris holds an A.B. in mathematics from Smith College and an M.S. in Industrial Engineering and Operations Research from the University of Massachusetts at Amherst.

Paul K. Huntwork is a consulting engineer at Digital Equipment' Corporation. Paul has lead efforts at Digital to adapt and invent world class methods for use in development of products and systems. Previously Paul worked at Computervision, Control Data Corporation, and the IBM Federal Systems Division where he led prototype-SEI process assessment and maturation drives.

Doug Muzzey is currently MIS Manager for Thermal Dynamics Incorporated, located in West Lebanon, NH. At the time this work was done, Doug was the development manager for the TeamLinks for Macintosh and Team Route workflow products, and sponsored the usability and customer partnering for the TeamLinks product family. He holds a B.S.C.S. (1978) from Florida Technological University and an M.B.A. (1991) from Rivier College.

Martin Rantzer is a system developer at Ericsson Radio Systems in Linköping, Sweden. Before joining Ericsson Radio, he worked at Ericsson Infocom as project manager for the development and integration of the Delta Method. Currently his work includes assessing new concepts and techniques for usercentered system development, and studying how they can be integrated into existing development models.

Robert C. Graf is a usability specialist at Microsoft Corporation. He conducted the current study at Dun & Bradstreet Software Services, Inc., where he managed the Usability Lab. Robert led software design projects and supervised the quality assurance group at Minitab, Inc., a developer of statistical analysis software. He holds a Ph.D. from the Pennsylvania State University in Cognitive-Motor Behavior.

David E. Rowley manages the development of data handling products at Varian Chromatography Systems. He is active in the San Francisco Bay Area chapter of the ACM special interest group on computer-human interaction, serving as chair in 1995-96. He continues to pursue usability engineering techniques that fit into the ever-changing management and quality paradigms facing research and development organizations.

Susan M. Dray, President of Dray & Associates, is a consultant with over 17 years experience, who pioneered in the development of usability methods and user-centered design. She has done both ethnographic and traditional usability studies in the US, Europe and Asia, and consults to clients worldwide.

Dr. Dray received her Doctorate in Psychology from UCLA and is a Certified Human Factors Professional. She held various positions in Human Factors research and consulting at Honeywell and American Express Financial Advisors in Minneapolis, Minnesota, prior to establishing her consultancy in 1993. She is a Fellow of the Human Factors and Ergonomics Society. She edits the Business column of the magazine, Interactions and is also on the editorial board of the international journal Behavior and Information Technology.

Deborah Mrazek is a Certified Human Factors Professional who has been in the field for 13 years. She has performed all aspects of Human Factors Engineering at Rancho Seco Nuclear Generating Station for five years. She was involved in implementing Human Factors programs for HP Computing Systems for four years. She then performed Human Factors Consulting internally for a variety of HP divisions. For the past two years she has been leading the Software Human Factors Team at the HP Vancouver (InkJet Printer) divisions. Currently, she is with the HP Corporate Customer-Centered Quality team, consulting in the area of customer-centered design methods and practices.

She became involved in international usability testing several years ago. She has performed a variety of usability studies in Europe and regularly consults with HP design teams around the world.

Diane S. Brown is a Principal Human Factors Engineer at ATL Inc., where she established the human factors program. She has been working in human factors and user interface design for software and hardware systems for nine years. In addition to human factors training, she received a B.S. in Mathematics and a Master's degree in Biophysics from the University of Utah.

Kristin Bauersfeld recently left Claris to join the Interface Design Group at Netscape Communications Corp. While at Claris, Kristin was responsible for interaction and user centered design on a number of Claris'future technologies and products. Before joining Claris, Kristin worked as a member of the

OpenDoc and PowerTalk Human Interface teams at Apple and at NASA Ames Research Center. She received her M.A. in Experimental and Human Factors Psychology from San Jose State University.

Shannon Halgren joined the Interface Design Group at Claris in 1993 to manage the new Claris Usability Studio. In her position, Halgren is responsible for conducting all facets of usability and user centered design research. Before joining Claris, Halgren worked as a member of the Human Factors Group at GO Corporation, Compaq Computer Corporation, IBM, and Lockheed. She received her Ph.D. in Experimental Psychology-Human Computer Interaction from Rice University in Houston, Texas.

Stanley R. Page is a Manager of Human Factors at Corel Corporation. He has over 11 years of experience in human factors research and user interface design, including five years at WordPerfect and Novell. His degrees include a Ph.D. in Instuctional Technology from Indiana University and a Bachelor of Fine Arts degree from Utah State University.

Dianne Juhl has been with the Microsoft Usability Group since 1992 and with Microsoft Corporation since 1987. Since joining the Usability group, she has worked with various Microsoft product teams to conduct user-centered design projects. Prior to joining the Usability Group, Dianne was the program manager for a client-server project that put the Microsoft Library's catalog on the corporate network and on desktops of Microsoft employees worldwide. Dianne holds a Master of Science degree in Library and Information Science from the University of Washington. She holds a Contextual Design Coach certificate from InContext Enterprises.

Janette Coble is a research associate in the Section of Medical Informatics at Washington University School of Medicine, in St. Louis, Missouri. She holds an M.S. in Computer Science from Washington University and has had training in Cognitive and Experimental Psychology. Her current work includes performing Contextual Inquiry, usability testing of clinical software, and the design of user interfaces. Before joining Washington University in 1993, she worked at McDonnell Douglas Corporation, where she researched and applied object-oriented and user-interface technologies.

Judy Maffitt is a Senior Analyst in Information Systems at BJC Health System in St. Louis, Missouri. She holds a B.S. in Mathematics from the University of Illinois at Urbana-Champaign. Her current work includes the development of procedures, standards, and interfaces for normalizing and transmitting clinical data to a Clinical Information System. Before joining Barnes Hospital in 1987, she worked for Continental Telephone Company (CONTEL) in Wentzville, Missouri, and Hewitt Associates in Lincolnshire, Illinois, where she developed mainframe business applications.

Matthew J. Orland is an Associate Professor of Clinical Medicine at Washington University School of Medicine, and is in practice with specialties in internal medicine and endocrinology. He obtained a B.S. degree in Engineering and Applied Science at Yale University prior to his M.D. degree from the University of Miami School of Medicine. He is currently a consultant to Information Systems activities within the BJC Health System, and is an active participant in the design and development of the clinical workstation for Project Spectrum.

Michael Kahn is the head of the Section of Medical Informatics at Washington University, St. Louis and is Director of Advanced Clinical Information Systems at BJC Health System. Dr. Kahn received his M.D. degree from the University of California, San Diego, did his Internal Medicine internship and residency at St. Mary's (a UCLA affiliate program), and received his Ph.D. degree from the University of California, San Francisco. Most recently, as head of the Section on Medical Informatics, Dr. Kahn's group has developed a number of expert systems for Quality Assessment. In addition, Dr. Kahn leads the Clinical Information Systems group within Project Spectrum.

Mary Beth Butler is Group Manager of Desktop Usability Testing at Lotus Development, where she established the first usability lab. Ms. Butler has a B.A. in Psychology from Brown University, and an M.B.A. from Northeastern University. Ms. Butler serves on the Board of Directors of the Usability Professionals Association.

Marie Tahir is a usability specialist at Lotus Development. She has worked in the software industry for six years. Prior to that, she was an editor at the University of California at Berkeley. Ms. Tahir has a double B.A. in English and Dramatic Arts from the University of California at Berkeley.

John M. Ford received his Ph.D. in Psychology from Brigham Young University in 1993. John is employed by Alpine Media in Orem, Utah, where he works as a project manager and instructional psychologist. His professional interests include interviewing tools and techniques, certification test development, and performance support.

Aki Helen Namioka was first introduced to Participatory Design not through her work as a computational linguist for Boeing Computer Services, but rather through her involvement with Computer Professionals for Social Responsibility (CPSR). In 1993 Aki and Douglas Schuler co-edited the book Participatory Design: Principles and Practices published by Lawrence Erlbaum Associates. The book grew out of the first Participatory Design conference (PDC'90) and featured several conference speakers.

Christopher Rao is a Harvard law graduate, who was a teaching fellow at the Harvard Negotiation Project. He later chose the frontier of the Internet over the divisiveness of law. Currently president of the web publishing firm AD1440, he also teaches business negotiation at University of Washington Extension, focusing on how improved process can reduce inefficiency and stress in negotiating.

Karen Holtzblatt and Hugh Beyer are the developers of Contextual Design, a customer-centered design process extending the Contextual Inquiry datagathering technique.

Dr. Holtzblatt originated the Contextual Inquiry approach to field data collection and has pioneered the introduction of this technique into working engineering teams. She has used customer-centered processes for the past nine years to design and evaluate software, hardware, and business processes.

Hugh Beyer has worked in the industry as a programmer, architect, and consultant for twelve years. He has designed and developed object-oriented repositories and integrated CASE systems, and has developed processes for using customer data to drive object-oriented design.

Holtzblatt and Beyer are co-founders of InContext Enterprises Inc., a firm that works with companies such as Microsoft and WordPerfect, coaching teams to design products, product strategies, and information systems from customer data.

![](images/f2b30019af2732b5de72d9ef3abeff63758f696b6c56b21d081f0e6859ad7242.jpg)

## Introduction

This collection of essays grows out of a workshop on field-oriented design techniques offered by the editors at CHI \`95. The workshop, originally scheduled to take place over one and a half days, grew to two full days, and in fact we even ended up having lunch brought in on both days so that we could continue our discussions uninterrupted. The interest of the participants was sturdy enough to carry them through the preparation of their case studies as chapters in this volume. We also include three chapters that are invited contributions discussing the three most widely recognized forms of field research currently in use in product design: Ethnography, Participatory Design, and Contextual Design.

Design is ultimately tool-making—putting an "enabler" between the worker and the work. Moving from the simplest physical tool to the most complex cognitive tool does not change the basic process: fashioning the idea of the tool out of the “empty space" between the workers and the work, and then refining the idea into the best possible actuality. This process is one of discovery, of filling in the details of the situated workers and work until the ideal shape of the tool is revealed.

We had two main goals in this work:

To provide numerous case studies—actual examples of field research that explore and demonstrate the two aspects of discovering design: doing research in the field and systematically incorporating the findings into the development process.

To look at the research disciplines and perspectives that are the foundations for these case studies—to present in more detail the theoretical frameworks, assumptions, values, and perspectives of the three main schools of thought in field research motivated by product development.

The volume opens with the case studies and reserves the three "framework" chapters until the end. The chapters themselves cluster around seven broad themes: focus on roots in Ethnography and Participatory Design; focus on the development process; two organizational case studies; focus on details of method; examples of Contextual Design; an example of bringing the field into the lab; and finally, frameworks: Ethnography, Participatory Design, and Contextual Design.

## FOCUS ON ROOTS IN ETHNOGRAPHY AND PARTICIPATORY DESIGN

In the first three studies in this collection, the authors describe projects in which they borrowed methods and techniques of field research from established practice in Ethnography and Participatory Design and then modified the methods so as to accommodate the specific demands and constraints of their product-design contexts.

As part of a larger effort to define the requirements for a proposed imaging workstation for diagnostic radiologists, Judith Ramey and her research team at the University of Washington conducted the study reported here (“Adaptation of an Ethnographic Method for Investigation of the Task Domain in Diagnostic Radiology"), in which they combined the ethnographic “stream of behavior chronicle" and the retrospective verbal protocol (also known as “stimulated recall") to capture both radiologists' task performance and their own expert commentary on it.

The method has four phases: first, the team gathered the stream of behavior by videotaping radiologists as they worked in their normal work setting. Then, a member of the team viewed the tape and formulated questions and hypotheses about the work. Next, in a second videotaped session, the team member showed the radiologist the original tape and asked for a running commentary on the work (the "stimulated recall"), into which, at the appropriate points, she interjected questions for clarification. Finally, the team categorized and indexed the behavior on the original tapes for various kinds of follow-on analysis.

The method proved especially useful in uncovering detailed behaviors (marking on films and reports, pointing at and touching films, using the fingers as “calipers," etc.) that the subjects were no longer aware of or were only marginally aware of. These behaviors, which for the subjects had slipped beneath their conscious attention or interest, turned out during the stimulated-recall sessions to be important features of practice and generated numerous specific requirements for the user interface of the proposed system.

The authors describe this method in detail, explain how they analyzed the original videotapes and the commentary tapes, and discuss how the method can be integrated into an overall user-centered design process based on standard human-factors techniques.

The second case in this first group, "Using the CARD and PICTIVE Participatory Design Methods for Collaborative Analysis," by Michael J. Muller and Rebecca Carr of U S West Technologies, describes a project in which the authors were forced to take a longer step from their methodological foundations.

The authors describe a new use for two methods that originally were created to support the classic Participatory Design goal of direct end-user participation in design. Both CARD and PICTIVE rely basically on paper representations of system states that analysts and users can discuss and modify. The investigative team uses the system images provided by CARD and PICTIVE to iteratively exercise, discuss, and critique detailed work scenarios.

However, in the case reported here (in which the goal was to develop a model of the work of directory-assistance telephone operators) the investigators were unable to work directly with the operators. Instead, trainers had to serve as subject-matter experts and spokespeople for the operators. Offsetting this disadvantage, the investigators were able to hold two-thirds of the sessions in or near the operators' work area, so that they could easily role-play the work, observe actual work, or even take live calls themselves.

Thus, what was already known of the users' work was present (in the form of the initial CARD representation), and most of the time the users' work setting was at hand, but the users themselves were not. So, even though the team used tools created within the Participatory Design tradition, the work itself (as the authors explain) was not truly "participatory.

The authors also found that the nature of the operators' work required that they modify their methods. The work under study had a significant noncomputer component: it required social interaction with the customer and significant mental work on the part of the operator. CARD and PICTIVE, however, were tied specifically to representations of system activity. Thus the investigators had to devise new "cards" for these new categories of user activity.

But in spite of the many constraints, this exercise led the team to a much richer understanding—and thus representation—of the mental work of the operators. In turn, this led to a richer understanding that to some extent all workers are knowledge workers, even though their job may be classified in some other way (such as “clerical"). And finally, this effort underlined the power of qualitative, collaborative analysis to illuminate dimensions of work that can be missed by more reductive quantitative analytical methods. The authors close with a discussion of the cost-effectiveness of the effort and consideration of several issues about the robustness and replicability of the study.

In“The Ethnographic Interview in User-Centered Work/Task Analysis," Larry Wood of Brigham Young University describes an approach to interviewing that he developed during a software development project by synthesizing insights from the two fields of cognitive science and ethnography. (The project in question was developing a software application to support ordering telecommunications services on the campus of Brigham Young University. The goal of the interviews was to produce a description of current work practice, derived from practitioners themselves, for use in later stages of the user-centered design effort.)

A key assumption in the development of Wood's method was that the people currently doing the work should be respected as experts at it. Thus, Wood used the insights of cognitive science into the nature of expertise and the organization of expert knowledge, namely: expert knowledge is generally organized hierarchically; it is stored as "chunks" of patterns with associated procedures, and thus can be viewed as "object" knowledge and "process" knowledge; and, to a large extent, it is automatic (or tacit) and thus may be difficult for the expert to articulate.

Armed with this model of expert knowledge from cognitive science, Wood was able to draw from Ethnography interviewing techniques that responded to both the features of expert knowledge and the difficulties of eliciting that knowledge from the interviewee. The method first uses semistructured interviews to elicit object identification (concepts and relationships as expressed in expert terminology). Once interviewers have a reasonable grasp of the experts' object knowledge through interviews, they can go on to develop a more detailed work model (combining and extending object knowledge with experts' process knowledge) by augmenting interviewing with systematic observations of work. The emerging work model is then documented and returned to the practitioners for validation or correction.

In presenting his case study, Wood provides numerous examples of actual questions to ask during the interviews, discusses the role of the interview in the larger design process, and provides extended examples of techniques for documenting the resulting model so that the interviewees can most easily judge its accuracy.

## FOCUS ON THE DEVELOPMENT PROCESS

In the three articles previously mentioned, the authors focused a great part of their attention on describing the methods used and their strengths and weaknesses. In the following two articles, the authors shift the emphasis from methods per se to the design process itself, how it can accommodate or respond to field usability data, and how field research fits into the overall flow of activities.

## FOCUS ON THE DESIGN PROCESS

Working from within a user-centered design process, Wixon, Pietras, Huntwork, and Muzzey were able to use a variety of field research methods, integrated into an overall design process that also featured innovative total quality approaches and prototype testing and evaluation ("Changing the Rules: A Pragmatic Approach to Product Development"). Some of the field research activities were planned in advance, and others were selected to meet needs as they were encountered during the phases of the design process.

In planning the design process for the product (a workgroup application for the Macintosh), the team identified the user interface design as critical to the product's success; therefore, they decided early on that they needed to establish "design partnerships" with a set of customers for iterative feedback. In the first phase of development (definition of the product concept), they conducted Contextual Inquiry and work-based interviews. In the second phase, in which they made decisions about the product's capabilities, they used surveys of customers and Vector Comparative Analysis, a computer-based tool for analyzing the scores customers have given various possible product features. In the third phase of development (design of the user interface), the team returned to field research methods, using Contextual Inquiry and artifact walkthroughs. During the implementation phase, they did userinterface prototype tests and evaluations. Finally, during the formal product test, they conducted tests in which customers used the product for production work. Thus field methods were integrated with a suite of other methods, each used at the point in the process where it would be most effective.

The authors provide extensive reflections on their experience during this design effort. In general, they learned that when they listened closely to what their customers said, they discovered that many of the assumptions that had driven their early thinking were completely wrong; but also by listening carefully, they were able to identify the product functions and characteristics that were "delighters" to their customers.

In "The Delta Method: A Way to Introduce Usability," Martin Rantzer describes a method meant to serve as a framework to link together existing usability tools and practices systematically in order to supplement the early phases of traditional software development. Called the Delta Method, the approach focuses on design of software interfaces (here understood—quite rightly, we might add-to include user documentation), with the goal of supporting the system designers and technical communicators (neither of whom could be assumed to have formal education in human factors or usability) as they carry out the customer and user analysis and the design of a prototype.

Intended both for internal use at Ericsson Infocom Consultants AB of Sweden and for sale to customers, the Delta Method was developed as a joint effort by Ericsson Infocom and Linkoping University. The development process had three phases: method inception, field studies, and analysis. In the first phase, usability activities were identified from the perspective of the academic partners (including such activities as user and task analysis), then adapted to the requirements of industry. This first formulation of the method was then tried out in a pilot project in the field (a commercial project within Infocom). Based on an analysis of the field studies, the method was revised.

Rantzer then describes the features and processes incorporated into the final form of the the Delta Method. The approach is unusual in its emphasis on the importance of user information and hence on the necessity of having technical communicators as part of the team; the other two team groups are the system designers and the customer representatives. The first task is to capture the customer's vision of what the system should be; this vision will then be supplemented and validated iteratively in user and task analysis . Then the group proceeds to conceptual design, formulation of usability goals, prototype design, and usability tests.

Finally, Rantzer describes the process of generalizing the Delta Method so as to make it flexible enough to be useful in a range of different organizations. For example, one finding was the need to tightly integrate the Delta Method activities into the process documents already in use; the familiarity of the larger document aided the acceptance of the new usability activities.

## TWO ORGANIZATIONAL CASE STUDIES

The next two articles in the collection are especially useful in understanding the "politics" of field research in product design—that is, the influences of differing goals in doing the research, the varying needs and goals of the partners in the research, and the susceptibility of the research to larger business decisions.

In "Field Research of Sales Personnel and Processes for the Design of a Sales Automation Workstation," Robert Graf working at Dun and Bradstreet Software, Inc. (DBS) describes field research he did for a new release of an existing system intended to support the internal sales staff. The system, which consisted of a notebook PC, applications, local and central databases, and the hardware and software needed to communicate with the central databases, was intended to increase sales, reduce the cost of sales, and provide better competitive information.

Graf describes the process he went through to clarify the business situation and usability issues to be investigated. When it became clear that user acceptance was a major issue, Graf proposed a field study so that he could get a realistic picture of the realities of the sales process and understand the role of mobile computing in it.

Once in the field visiting satisfied and unsatisfied users of the current release, Graf discovered the need for flexibility; although he had planned to videotape the sessions, the interviewees objected, and thus he and his team found themselves gathering data only through handwritten and typed notes. When he began the data analysis, he encountered difficulty arriving at the best organization of the mass of narrative data; finally, he decided to provide a summary report, three detailed task analyses (one for each of the critical audiences, with a "day in the life" approach), and two business models (a model of the idealized sales process and a model of all the information the sales person needs to do his or her job).

Following on the distribution of the report, the team did a usability inspection of the product that yielded a prioritized list of usability issues to be addressed in the next release. Also, a new organizing concept—the "deal"--was developed to integrate all the various parts of the product. Unfortunately, however, the system did not receive funding for a major redesign. Nevertheless, Graf concludes that this field research did much to provide his organization with a vision of the power of field research.

David Rowley of Varian Chromatography Systems, in "Organizational Considerations in Field-Oriented Product Development: Experiences of a Cross-Functional Team," also provides an organizational perspective on field research, but focuses specifically on issues related to field research done by a cross-functional design team—a team composed of people from different areas within the company (engineers, technical writers, marketing personnel) and tasked with the design of a specific product.

The team whose field research is reported here was responsible for the development of the data-handling product line. The team was made up of applications experts, engineers, marketing personnel, technical writers, technical support staff, and manufacturing staff. Whereas before the adoption of such cross-functional teams only marketing might have visited customer sites, now all of the members of the team have the opportunity direct contact with end users.

This team had had some earlier experience with usability investigations in the form of mobile lab tests, but had not had a systematic way to capture the bigger picture of users in their setting and communicate it back to the rest of the team. In addition to this general goal, the team wanted to investigate the requirements for specific new products. To accomplish these goals, the team decided to use Contextual Inquiry and to capture data on videotape as much as they could. Also, based on their market, they decided to conduct the study in Europe.

Rowley describes in detail how the team arrived at their focus statements for the study, approached the logistics of visiting foreign pharmaceutical labs, conducted the actual visits and interviews, and worked to create a balanced and unbiased picture of the work being supported. He points out that the recommendations for change were documented in the team's change control system, and thus were fed into the standard company mechanisms with no need for special procedural accommodations.

Rowley finds that removing the barriers often found between functional departments results in improved communication and coordination within the team, but the lack of centralization may reduce the scope of the impact of field study findings. That is, while it may be easier to impact the design of a product developed by the team conducting the study, it is harder to effect change in the design of products developed by other teams. Also, the amount of data generated was overwhelming; Rowley recommends a number of changes to their process so as to make the research findings more accessible and manageable.

## FOCUS ON SPECIFICS OF METHOD

The authors of the next three articles give us a detailed view of the nuts and bolts of field research that can often determine its success or failure.

In "A Day in the Life of a Family: An International Ethnographic Study," Susan Dray and Deborah Mrazek report on the field research they did for Hewlett-Packard in response to the challenge presented by having to design for a very different audience from the standard business market: the global home and family market.

In addition to standard marketing information, the design team needed information about how and by whom the product would be used, so that they could optimize its ease of use. To gather this information, the researchers used a number of methods: naturalistic observation, Contextual Inquiry, ethnographic interviews, and artifact walkthroughs. The unifying idea was that, to gain insights into how families use computer technology, they would go to the homes of representative familes in the US and in Europe to see firsthand.

Dray and Mrazek provide substantial detail about the logistics of arranging the family visits and the actual visits themselves. Especially concerning the visits to European homes, they emphasize the importance of the "social" dimensions of the visit, as well as describing the formal data collection activities. They believe that their focus on the social dimensions—providing food, focusing early on the family's children, taking snapshots, etc.—provided the essential credibility and rapport that they needed to gain the committed participation of the families. For their core data collection activities, they asked each family member for a demonstration of typical activities on the computer, they reviewed sample outputs, and they documented the setting (location of supplies, documentation, other equipment, etc.), after which they continued with a less formal discussion and closing. The team then conducted a separate structured debriefing to capture the critical insights of each visit.

The special challenges of doing field research in the medical equipment industry is the focus of Diane Brown's article "The Challenges of User Based Design in a Medical Equipment Market." Brown's employer (ATL, Inc.) builds medical ultrasound imaging systems. Historically, ATL's engineers designed in response to requirements statements and evaluations provided by former users now employed in ATL's marketing department; but, in response to customer complaints, management agreed to create a group focused on usability. After several somewhat unsatisfactory attempts to get information from end users about how to improve usability, the group determined that in order to better support their users'work, they needed to pursue new ways of understanding the context in which the problems were encountered, as well as gain a detailed understanding of what the users were trying to accomplish.

Thus they began to conduct field studies. These studies fell into three different categories: efforts to answer very specific questions about processes, efforts to understand surrounding work tasks so as to incorporate them into the system functionality, and finally efforts to make fundamental changes by rethinking the human-system interaction from first principles. Their chapter focuses on this last effort.

Brown describes in detail the evolution of their approach from the first, unfocused site visits through the process of redefining and sharpening their focus, and choosing new sites to visit based on more specific criteria. At the sites, the team videotaped the work performance. Brown describes in detail the follow-up interviews they conducted with the workers they observed and the transcription and segmentation they performed on the videotapes of the work so as to extract a hypothetical model of the work and terminology. They then correlated the two: after they organized the observations, they reviewed the interview transcript and extracted the goals (what the worker was actually trying to accomplish). To help in the data analysis, the team developed several tools. One, resembling musical notation, allows them to graphically show patterns of work over time. They also began to use Contextual Design methods (see Holtzblatt and Beyer, this volume) to organize and graphically describe their findings.

The author closes with a description of the process of generating design requirements from the data and impacts that the data may have on the design. In reflecting on her experience in doing this field research, she identifies a number of areas where they might improve their processes and tools.

In "You've got three days!' Case Studies in Field Techniques for the Time Challenged," Kristin Bauersfeld and Shannon Halgren then at Claris Corporation describe three field study techniques, adopted from traditional methods, that they designed to work with very short time frames for conducting research, interpret the findings, and apply the results. This effort to do field research was motivated by an opportunity for the Interface Design Group to get involved at the conceptualization phase of design of several new products, a departure from the more typical pattern of coming in at the end to do lab-based usability tests.

The first of these methods is the "Condensed Ethnographic Interview." In this short interview conducted in the user's environment, the users are asked to begin discussing their daily activities; for each regular task of interest to the researchers, the researchers might ask more questions or request a demonstration. The session is videotaped for followup analysis.

In the second technique, "Passive Video Observation," two cameras are placed in the user's setting—one to capture the area view and one (or a scan converter) to capture the user's computer screen. The two images are mixed onto one screen using a video mixer. The taping takes place for about two to three hours, with the user having the ability to turn it off (or off and then back on) if they need or want to. The researchers then collect the equipment and view the session videotape for analysis.

The third technique, "Interactive Feature Conceptualization," is basically a technique that enables users to organize and rate the importance of their own processes and terminology. Based on the condensed ethnographic interview contents, the researchers record all of the mentions of tools, forms, processes, and software features on sticky notes. The user then goes through an exercise of sorting and rating them. The session is videotaped.

The authors provide detailed descriptions of two case studies in which they used these methods and discuss the lessons they learned from the experience.

## EXAMPLES OF CONTEXTUAL INQUIRY ANDCONTEXTUAL DESIGN

Based on several years of use and iterative improvement by Karen Holtzblatt and Hugh Beyer, Contextual Design offers an integrated, systematic whole-process method for getting from the research idea to the design response. A number of corporate design teams have adopted the method; the next two articles report case studies of its use.

Building on a tradition of seeking feedback from users begun in the early years at WordPerfect, Stan Page and his cross-disciplinary team at Novell Inc. undertook to do field research as input for the next generation word processing application ("Contextual Design in a Large Commercial Software Company"). Their focus was purposefully broad: the work practice surrounding the making of documents.

The team, composed of members from development, human factors, documentation, marketing, and usability testing, used the Contextual Design process as taught by Holtzblatt and Beyer. This method was chosen for its special strength in structuring the process of converting research findings into design. (For details of the method, see Holtzblatt and Beyer, this volume.)

When the research effort showed promise, management decided to basically double the effort; the original team was divided in half and new people added to each new team. One team continued the research into the making of documents; the other expanded its scope to include all business work practice. Page describes the way the new participants were trained and the way the two teams organized themselves to conduct their work. He also describes the methods used by the teams to communicate with each other and with the company at large. He underlines the importance of getting the results of the research into new design, and offers examples of features derived from the work (which include Make-It-Fit and QuickTasks).

Microsoft has long been known as both an innovator and early adopter of usability methods; Diane Juhl describes the systematic use of Contextual Design along with a number of field-oriented design methods. Because the team was approaching a relatively new market (the home market) and one of the aims of the products was to develop new software opportunities, the team decided to choose a set of structured field research methods.

The team included members from the sponsoring organizations and the usability team. While the focus of the work was quite specific, it was also broad. As a result, the team generated a large data pool, over 2000 data points, 300 design ideas, and 200 work models. They also developed a list of over 20 typical tasks. This work (combined with the reporting of the results) was completed in 60 days, contradicting the common belief that field research takes a long time.

Reporting such large set of data was a challenge. In addition to traditional approaches of reports and presentations, the team developed a data base of affinity diagram, and have put the work models on line. The data have been extensively re-used in developing business cases, evaluating designs, and creating focus statements for future studies. In reporting their results, the team faced management questions about sample size, succinctness, and quantification of the results. The team is currently working to address these questions in future projects, and will be continuing to refine and develop these methods.

The third case in this section reports on the use of the method (in the form of Contextual Inquiry) in a medical products development effort (Janette Coble, Judy Maffitt, Matthew Orland, and Michael Kahn, "Using Contextual Inquiry to Discover Physicians' True Needs"). This effort was undertaken as the requirements generation task for a clinical workstation intended to support clinicians in viewing test results for their patients from office, home, or hospital. The team chose Contextual Inquiry (CI) because they felt that going to the users' actual environment would be the only way to ascertain the actual needs of the physicians, especially those needs buried in the physicians' tacit knowledge (see Wood, this volume).

After describing in detail the selection of sites to be visited and the conduct of the typical session, the authors describe their process of analyzing and interpreting the data. Following each session, the researchers walked back through their notes of the session and created several different products from the information that they had obtained: a sequence model, a flow model, a context model, detailed observations, a user profile, and an issues list. The authors describe each of these products in detail.

At the halfway point of the research and at the end, the researchers consolidated their findings from all of the sessions by building an affinity diagram. Next, the researchers derived requirements from their observations. After they had formulated the requirements, they returned them to the physicians so that the physicians could rate their importance, and finally they produced a requirements document enriched with insights from the research.

## AN EXAMPLE OF BRINGING THE FIELD INTO THE LAB

The last of the case studies in this volume presents an alternative to going out to the users' environment to gather data; instead, it brings the field into the lab. Mary Beth Butler and Marie Tahir, in "Bringing the Users' Work to Us: Usability Roundtables at Lotus Development," describes a method in which they and their co-workers at Lotus Development Corp. attempt to recreate a portion of the user's environment by having the users bring samples of their work to the Lotus offices. Users sit with product team members around a conference table and use these samples (data files, sample applications, or hard copy printouts) to explain their work.

Seeing the work that users do is considered invaluable to ensuring that product designs meet users' needs. Initial attempts at Lotus to visit users in their workplaces were time-consuming, and were not as productive as the researchers had hoped; usability roundtables have provided them with an effective alternative for learning more about their users' work.

In this case study, the authors describe in detail how the usability specialists in Lotus work with the product developers to plan and arrange the roundtable sessions. The sessions, a form of artifact analysis (a technique used in Ethnography), are focused on uses of specific product features or work patterns. Participants are encouraged to bring along a co-worker, from whom the team might get additional information. As the name implies, the discussion between the user/ participant and the development team members is informal; however, the team does have an agenda of questions that they hope to cover during the course of the roundtable. The moderator (almost always the usability specialist) takes notes during the session and prepares a brief report.

The authors close with an assessment of the benefits and drawbacks of the method, and discuss ways that it might be used in the future.

## FRAMEWORKS: ETHNOGRAPHY, PARTICIPATORY DESIGN, AND CONTEXTUAL DESIGN

Behind these field-research case studies is a background of methodological thought that can be divided roughly into three main schools: Ethnography, Participatory Design, and Contextual Design. The final three articles in this collection explain the evolution of these perspectives and the ways in which they have inspired research methods for use in the process of system design.

Ethnography is the foundation discipline upon which the other field research approaches build. Ethnography is the description of cultures; it emerged as a discipline from social and cultural anthropology. In "An Overview of Ethnography and System Design," John Ford and Larry Wood first describe Ethnography's defining motive—description without bias—and explain its impact on the methods of ethnographers. They then draw out the similarities between the research of an ethnographer and the requirements definition of a system designer, and trace the evolution of the methods that system designers have historically used to try to understand their users' requirements, arriving finally at the current interest in using ethnographic methods.

The great advantage of ethnographic methods is in the insistence on maintaining the perspective of those inside the culture being described. Thus these methods are particularly effective in helping system designers accurately understand audiences about whom they have little or no prior knowledge. Ford and Wood briefly describe several research approaches that are basically specialized types of ethnography intended to support system design: Participatory Design, Contextual Inquiry, Joint Application Design, and PICTIVE (see Muller and Carr, this volume).

Finally, the authors identify several trends to watch for in the evolution of interest in and use of ethnographic methods in system design. The first one is especially intriguing: the development of sophistication about field research goals and methods among the users whose culture is being studied and the reflexive effects it might have on method.

In "Introduction to Participatory Design," Aki Namioka and Christopher Rao describe the evolution of Participatory Design from its Scandinavian roots and provide an overview of its main tenets and practices.

The essential characteristic of Participatory Design is commitment to the primacy of the worker. It believes that the goal of technological development is to build better tools to support workers, and that the workers themselves are the only ones with the expertise to judge how best to improve their work and work setting. Thus the technology designer becomes primarily the implementer of the workers'vision. Participatory Design uses techniques from several closely related approaches to put theory into practice. Ethnography, with its focus on highly contextualized understanding, has contributed a number of perspectives and field-research techniques (see Ford and Wood, this volume). Cooperative design techniques such as role-playing games have been pressed into service. Reciprocal evolution has contributed a focus on the study of work practices with technologies. And Contextual Inquiry (see Holtzblatt and Beyer, this volume) has contributed not only field-research techniques, but also business processes for evolving a design out of the field research findings.

In closing, the authors argue that even though the United States does not have the same strong trade-union tradition as Scandinavia, nevertheless our pragmatism and our long tradition of democracy provide a congenial atmosphere in which to practice Participatory Design.

In "Contextual Design: Principles and Practice," Karen Holtzblatt and Hugh Beyer open with a brief overview of the origins of their method as a response to a challenge to come up with a way to effect fundamental change in products. The core idea that animated the method was that to build radically better products it was necessary to have a thorough understanding of how customers work. This insight led to the first formulation of Contextual Inquiry, built on roots in ethnography, psychology, and systems engineering.

As Contextual Inquiry was exercised in projects over time, its practitioners encountered problems and limitations with its original formulation that led Holtzblatt and Beyer to make a series of modifications and extensions to it, resulting finally in the system of Contextual Design as it is now practiced: "a structured, step-by-step roadmap to guide a team from initial project set-up and field interviews through design and the transition to implementation."

Contextual Design provides a very fully specified step-by-step process for doing field research and converting the results into design. It pays attention to the workgroup dynamics of design teams and to the business realities that constrain design, as well as teaching good practice in doing field research. In the remainder of the article, the authors describe in detail the phases in the process of Contextual Design and the types of outputs developed during each phase (work models, affinity diagrams, consolidated work models, scripts, user environment models, and iterative prototypes, leading to the final design). They close with a brief consideration of the need for continued evolution of the method to respond to new needs and issues as they arise in practice.

## WHERE TO GO FROM HERE

This volume of essays can only open the door on the complex subject of the use of field research in product design, but several points seem especially important to make.

First, and most importantly, being successful in field research can require a fundamental change of perspective. The field researcher must be deeply humble and respectful in the face of the work practice and culture under study. The researcher must also be exhaustive in uncovering, scrutinizing, and containing the effect of his or her own assumptions, biases, and preconceptions about the worker, work practice, and culture. And, when the researcher turns to design, he or she must be careful not to lapse into the kind of “technological colonialism" that leads to improving workers' practice "for their own good." That is, the researcher must first commit to the philosophical position that justifies and animates field research: the culture and the people in it are worthy of respect.

Secondly, the use of field research in product design is very young. A researcher embarking on an effort to incorporate field research methods into his or her toolkit needs to do the homework required— which is to learn as much as possible about method. This means going to the foundation texts in Ethnography and related disciplines; it means following up the excellent references in the essays in this collection; it means going to workshops and conferences that address the topic. Armed with this background in the literature and current practice, one can develop good judgment about appropriate ways to scale and modify techniques to fit the constraints of a given situation.

Finally, as researchers and practitioners we need to develop a sense of community as we take part in the evolution of design practice.

Each of us who has used field research in product design should consider presenting a description of the project at a conference or in an article. Those who have modified an existing method or developed a new one to fit the demands of their design situation should document the new method for others. At conferences, those who are further along can offer workshops and presentations for people just beginning to use these methods.

We hear a lot these days about the need to succeed in an increasingly competitive global market, and the need to enhance the productivity of our workers. We might add to these concerns a desire to empower workers and to create pleasure in work. To help us achieve these goals in system design, we need to know as much as possible about the people and the contexts for which we are designing. We need to ground our designs in workplace realities, and discover better design in the limitations or unmet needs experienced by the user in the user's world. Product development processes built on field research can help us achieve these goals. We offer this collection in the hope that it will stimulate the use of field research and lead to further published discussion.