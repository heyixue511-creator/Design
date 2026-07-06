# Personas, Participatory Design and Product Development: An Infrastructure for Engagement

Jonathan Grudin

Microsoft Research

One Microsoft Way

Redmond, WA 98052 USA

+1 425 706 0784

jgrudin@microsoft.com

John Pruitt

Microsoft Corporation

One Microsoft Way

Redmond, WA 98052 USA

+1 425 703 4938

jpruitt@microsoft.com

## ABSTRACT

The design of commercial products that are intended to serve millions of people has been a challenge for collaborative approaches. The creation and use of fictional users, concrete representations commonly referred to as ‘personas’, is a relatively new interaction design technique. It is not without problems and can be used inappropriately, but based on experience and analysis it has extraordinary potential. Not only can it be a powerful tool for true participation in design, it also forces designers to consider social and political aspects of design that otherwise often go unexamined.

## Keywords

Persona, design method, scenario, user-centered design

## INTRODUCTION

Cooperative design techniques that can be effective in inhouse or custom development contexts are less effective in commercial product or package software development. Traditional “user-centered” approaches have been improved upon in recent years but current practices tend to fall short in several respects: Designers and users are not truly engaged; social and political aspects are filtered out; and complexity and representativeness are difficult to identify and portray. In this paper we discuss personas, a technique that, if used in conjunction with other methods, can draw upon powerful psychological forces to restore these dimensions. The use of this method is rapidly spreading, including in our organization. In this paper we focus on presenting a theoretical case for the method, which may not at first glance appear to be participatory design, and then we discuss our own experience in utilizing this method.

At the PDC ’90 conference one of us presented a paper identifying “obstacles to participatory design in large product development organizations” [15, 16]. Designers of mass-market, commercial software often can’t confidently identify specific users of their software. When attracting hundreds of thousands or millions of people is the goal, finding “representative” participants is a challenge. Organizational barriers are substantial: Designers must look outside their organization, but external parties have little incentive to participate over time, and development schedules rarely accommodate such involvement.

Although sustained user involvement seems desirable, its effect on commercial products is not clear. When an inhouse or custom project does not include participatory design, the resulting problems can be obvious. But how would Microsoft Word, the Mac OS X or Lotus Notes differ had participatory design been extensively used?

## PARTICIPATORY DESIGN IN PRODUCT DEVELOPMENT Early Scandinavian efforts

Early in the participatory design movement, this was not an issue: Platform-independent software was not significant until the 1980s. Systems were built for one organization. In the mid-80s, recognizing the expense of developing for a single organization, participants in the UTOPIA project worked hard to involve a large segment of the newspaper industry. As the work progressed, the researchers on the team saw the potential for a general desktop publishing application, which did not exist at the time [12, 13].

This revealed the complexity of working closely with users on a possible new product. Ehn [13] describes a ‘tradition/transcendence’ tradeoff: A new product may be useful to new users, but not to the current users who have developed skills and conventions around existing tools and practices. The researchers saw a product potential, but worker participants desired a less generally useful system that was more closely synchronized with existing practices. The desktop publishing product was not designed.

In the early 1990s Scandinavian and North American researchers undertook efforts to marry collaborative practices to product development. At CHI ’94 Morten Kyng’s paper “Scandinavian design: Users in product development” described a traditional custom project to support the Great Links bridge construction that also included partners interested in using the research to design products [21]. The PDC ’94 call for participation sought input from those who “investigate the incorporation of participatory design approaches in new areas such as product development.”

## Participatory methods from product developers

Product developers efforts to adapt and extend elements of the participatory design approach include low-fidelity mock-ups and prototyping [14, 20, 24], increased engagement and communication with potential users [19, 25] and an emphasis on site visits and understanding the work context [2]. These methods focused on raising the level of “user participation” above that achieved in traditional laboratory studies.<sup>1</sup>

Although these methods can be useful, elements of the Scandinavian approach were lost in transfers to product development:

• Long-term engagement with particular participants, and the empathy, commitment and deep understanding that such engagement can bring;

• Attention to the sociopolitical and ‘quality of life’ issues that marked much of the early work, including values, fears, aspirations, and so forth.

We contend that the personas approach described below can help restore these elements. Because it supplements other approaches, nothing is lost beyond a manageable investment of time. First, though, we review two other important approaches from the mid- and late 1990s: ethnography and scenario-based design.

## Ethnography and design

Conferences, journals, and books on Participatory Design, CSCW and HCI include numerous reports that focus on applying ethnographic approaches to product development [e.g., 3, 11]. Challenges in bridging ethnographic work and design include fitting the time course of such work to product design cycles and, of equal significance, communicating ethnographic analyses to designers and developers. Addressing this communication challenge is central to the shorter-term contextual design approach [2]. Another challenge is that ethnographies often identify disruptive effects that usually accompany the introduction of a new technology, the tradition/transcendence issue.

## Scenarios without personas

Designers have long used scenarios to organize, justify, and communicate ideas. These often do not involve users [e.g., 5]. Recently, participatory design and human-computer interaction researchers have focused on the use of scenarios to engage users and development team members; see papers in the collections Scenario-based design [6] and Scenariobased system development [18].

We focus on scenarios because they share attributes with personas and at first glance can be more compelling. However, we will argue that scenarios are less effective when not built on personas.

Every reader is no doubt familiar with scenarios in some form, but as a framework consider Carroll’s overview [7]. Scenarios are stories. They have a setting, agents or actors who have goals or objectives, and a plot or sequence of actions and events. His example:

“An accountant wishes to open a folder on a system desktop in order to access a memo on budgets. However, the folder is covered up by a budget spreadsheet that the accountant wishes to refer to while reading the memo. The spreadsheet is so large that it nearly fills the display. The accountant pauses for several seconds, resizes the spreadsheet, moves it partially out of the display, opens the folder, opens the memo, resizes and repositions the memo and continues working.”

## Keep this example in mind.

Carroll notes that scenarios can help designers and analysts focus on assumptions about people and tasks, assumptions that are implicit in the software. Scenarios can encourage reflection during design, they are concrete yet flexible – easily revised, extended or fleshed out. They can be viewed from multiple perspectives, abstracted and categorized. Finally, Carroll notes that they promote a work orientation. Citing participatory design, he says “one can increase (their) effectiveness by couching them at an appropriate level and directly involving users in creating and using them.”

The extensive literature on scenario-based design has little discussion of the “agents or actors.” Little is said about defining an agent or using it appropriately; nothing is said about the values or aspirations of an agent/actor.

The participatory design community has used scenarios heavily to engage “future users.” This includes acting out scenes of current or future envisioned work activities as mutual education about work practices, technology constraints, and new possibilities [19].

Bødker [4] has extended scenario use to include more of a focus on reflection in action, describing three possible roles: to present and situate solutions, to illustrate alternative solutions, and to identify potential problems. Scenarios are clearly better for promoting reflection and discussion among team members and possible users than, say, formal specifications.

But scenarios come with substantial risks and problems. There is often little discussion of the data, if any, on which a scenario is constructed. A scenario constructed by actual workers might be trusted more, but memory is unreliable, people can be guided by a simplified conception of the routine or alternatively by extreme experiences.

Often scenarios are created to justify particular features or technologies. They may include unrealistic assumptions about work practice or technical feasibility. A quarter century of working with scenarios in design has left one of us feeling that scenarios are rarely useful because they are rarely empirically grounded. The most reassuring data would be ethnographic, followed by data drawn from contextual inquiry and analysis, obtained directly from participant-users, derived from demographic or market research, taken from observations of usability studies, or combinations of the above. More often, scenarios are used in place of real data on work practice. Scenarios are not a problem, but how they are used usually is.

Bødker [4] describes an innovative use of scenarios. Two detailed scenarios were constructed around the use of the same proposed technology: a cheery utopian vision and a nightmarish, dystopian vision. These succeeded in focusing discussion on how to design to avoid undesirable outcomes and enhance positive uses. This indirectly illustrates the weakness of a single scenario: It is not anchored to reality strongly enough to be more than an argument.

In a further insight, Bødker notes “It gives a better effect to create scenarios that are caricatures… it is much easier for users and whoever else is going to relate to the scenarios to assess things when they see full-blown consequences… Not that they ‘believe’ in the caricatures, indeed they do not, but it is much easier to use one’s common sense judgment when confronted with a number of extremes than when judging based on some kind of ‘middle ground.’”

Caricatures are engaging, but may not be necessary.

## PERSONAS

Realistic scenarios appear to be a perfect tool for design: They depict the work practices one hopes to support. Their weakness is that they are not engaging. How well do you recall Carroll’s accountant scenario, minutes after reading it? Reread it. Dull. Scenarios are often difficult to reconstruct and hard to extend with confidence. Engagement is important. That is why Bødker argued for caricatures, unrealistic extremes that are more engaging, more memorable.

Personas are a method for enhancing engagement and reality. We are finding them to be a powerful design tool in practice. Persona use does not require eliminating scenarios or any other method: It is a foundation on which to build scenarios and data collection. It is an infrastructure for engagement. It is a means for communicating data that is collected using other user research methods.

Personas are fictional people. They have names, likenesses, clothes, occupations, families, friends, pets, possessions, and so forth. They have age, gender, ethnicity, educational achievement, and socioeconomic status. They have life stories, goals and tasks. Scenarios can be constructed around personas, but the personas come first. They are not ‘agents’ or ‘actors’ in a script, they are people. Photographs of the personas (in our experience, ‘amateur’ volunteers were better than professional models) and their workplaces and homes are created and displayed in public places.

At first glance this could appear to be a step backward, away from the work context and the specific actions we want to support. (Of course, the specific actions are less important than the users’ goals. The accountant did not want to open a folder to access a memo, s/he wanted to get a particular piece of information. Perhaps another solution would have been better.)

But to the extent that personas take a step back, it is to obtain a far more powerful level of identification and engagement that enable design, development, and testing to move forward more effectively.

Cooper [8] presents a case for the use of personas in design. The use of abstract user representations originated in the field of marketing [e.g., 23] but Cooper’s use of personas, their goals, and activity scenarios is focused on design. Cooper’s claims are based on anecdote and on appeals to reason, not on data. He does not describe in detail how personas are constructed. He exhibits a disdain for empiricism, including feedback on design possibilities. But our experience confirms the power of personas, and we and our colleagues have worked on ways to integrate personas with standard methodologies. Personas can be used badly. Our impression is that Cooper, a designer, has very good intuitions, but for most of us a more solid foundation will prove necessary.

Cooper marvels at the “surprising” power of personas, but does not endeavor to explain their power. Below we argue (with the benefit of hindsight, of course) that perhaps it should not have been so surprising. We then provide an overview of how we are employing personas and some tradeoffs and issues that remain to be resolved.

In parallel with Cooper, a few others have promoted the use of abstract representations of users to guide design: user profiles and scenarios derived from contextual inquiry [17, 29] and user classes fleshed out into “user archetypes” [22]. These practitioners, along with Cooper, are clear in positioning these representations as the starting point, around which scenarios are constructed.

## The power of people

Early proponents of participatory design went to such lengths as playing football with workers who would be using (and helping design) software. Can we achieve comparable effects with fictional people, and if so, what is the cost and what are the benefits? What are the risks?

Soap operas, situation comedies, dramatic series. There is no question that fictional people can be extraordinarily engaging. Many viewers fully engage with characters in programs such as As the World Turns and ER.

People in these extremely popular series for the most part resemble normal people. They may look better or be wittier on average, but their appeal is in part that they can be identified with (or against). They are often moderately complex—because we observe them over time, caricature is not essential.

Designers explored the use of shocking, caricatured personas in a short-term study and reported engagement and discussion [9]. But we have found, as did Cooper, that extreme characters and shock are not necessary. One factor is the duration of the exposure. A single film can benefit by having an extreme hero or villain, but this grows dull in a longer series. Characters in a series become more complex, more realistic. Similarly, once established, personas can be an ongoing presence, evolving to reflect data gathered from real people. That said, issues of stereotyping and casting against type in persona construction remain and are discussed in the final section.

Method acting and the value of detail. When an actor prepares for a scene that takes place in, say, the living room of the house the character lives in, one exercise is to create a history for each prop, each piece of furniture. When was this table bought? Which meals are eaten on it? Where did this desk come from? What has the character put in the top drawer? The next drawer? How often is it used? And so on. None of these details are specified in the script. None directly impinge on the scene. But by specifying the detail, an actor may intuitively behave in a more natural, normal way. If one frequently uses a desk one might walk by it or glance at it in a particular way…

Some of this detail may be invented, but many actors spend days or weeks observing and talking with real people who resemble those to be portrayed. A character is fictional but the behavior is based on real data: precisely the goal with personas. If successful, the actor can accurately intuit a character’s behavior in a new situation. A designer, developer, or tester can intuit the behavior in novel situations of the people on whom a persona is based.

Social reasoning and Theory of Mind.<sup>3</sup> Beyond engaging the attention of team members, a detailed persona enables them to draw on experience to fill in more aspects of behavior than are included in a scenario or specification. This utilizes a powerful human characteristic. From birth or soon thereafter, every day of our lives, we use partial knowledge to draw inferences, make predictions, and form expectations about the people around us. We are not always right, but we learn from experience. We continue to extrapolate. Personas evoke this universal capability and bring it into the design process. Faceless accountants lying inert on the page do not.

Thus, well crafted personas are generative. In the case of scenario creation, individuals across a product team can independently generate appropriate and complementary scenarios for seemingly disparate areas of a large, multifaceted product. As Cooper indicates, once a set of personas is constructed and provided with sets of goals, once team members have accepted and assimilated them, then meaningful scenarios can be constructed around them. We differ from Cooper in that we argue that the scenarios, personas, and product designs should evolve in response to ongoing observations of, and feedback from, the real people who inspired them.

## Our experience with personas

One of the authors, along with many colleagues, has been actively using personas and refining techniques for using them for several years. We are preparing a paper detailing our method and experience. A few key points:

• Unlike Cooper, we feel strongly that persona use needs to be complemented with a strong, ongoing effort to obtain as much quantitative and qualitative information about users as possible, to improve the selection, enrichment, and evolution of sets of personas. In our method, persona creation begins with quantitative market segmentation much like that discussed by Weinstein [30]. The highest priority segments get fleshed out with user research including field studies, focus groups, interviews and further market research.

• In a recent effort, persona creation involved a team of about 22 people over a period of roughly two months. Team members included product planners, usability engineers, interaction designers, market researchers, and technical writers. Other efforts have been less intensive, involving one or two people for shorter periods of time. These lighter efforts typically capitalized on existing user research and generated somewhat less detailed personas.

• We utilize a central “foundation” document for each persona as a storehouse for all information about that persona (data, key attributes, photos, reference materials, etc). Figure 1 shows the table of contents for a foundation document. Note that the foundation document is not the primary means of communicating information about the persona to general team members (more on that below). Likewise, foundation documents do not contain all or even most of the feature scenarios (i.e., “walk-through” scenarios are located directly in the feature specs). Instead, the foundation document contains goals, fears, and typical activities that serve to motivate and justify scenarios that appear in feature specs.

<table><tr><td>Overview – Patrick Blakeman (Small Business Owner) Get to know Patrick, his business and family. A Day in the Life Follow Patrick through a typical day. Work Activities Look at Patrick&#x27;s job description and role at work. Household and Leisure Activities Get information about what Patrick does when he&#x27;s not at work. Goals, Fears, and Aspirations Understand the concerns Patrick has about his life, career, and business. Computer Skills, Knowledge, and Abilities Learn about Patrick&#x27;s computer experience. Market Size and Influence Understand the impact people like Patrick have on our business. Demographic Attributes Read key demographic information about Patrick and his family. Technology Attributes Get a sense of what Patrick does with technology. Technology Attitudes Review Patrick&#x27;s perspective on technology, past and future. Communicating Learn how Patrick keeps in touch with people. International Considerations Find out what Patrick is like outside the U.S.</td></tr></table>

Figure 1. Table of Contents for a Foundation Document

• Links between persona characteristics and the supporting data should be explicit and salient. If personas are not perceived as credible, they are not used. Our foundation documents contain copious footnotes, comments on specific data and links to research reports that support and explain the personas’ characteristics. All persona illustrations and discussions link back to these foundation documents so that the team can always access the supporting documentation.

• “Grass roots” persona efforts, when a few people on a team decide to try the method, have typically had less impact than desired. Getting high-level management and key team members to buy into the use of personas is critical. On first encounter, the idea may seem too unscientific, “arty,” to engineers and others. It can take a leap of faith for the first teams in an organization to try it. It is a major step to have team leaders say “We’re all going to do it,” provide people resources for creating and promoting the personas, and a budget for posters, Tshirts, and other materials to keep personas visible.

![](images/721da38543fb8ef761586ece7db97767c23b3e7f04f4aee7b6189c18418786d3.jpg)  
Figure 2. A Persona Comparison Poster

• Communicating about your personas should be multifaceted, multimodal, on-going, and progressively unfolding. While our foundation documents are available to anyone on the team who wishes to review them, they are not the primary means for delivering information about personas. Instead, we’ve created many variations of posters, flyers, handouts and giveaways (e.g., squeeze toys with persona images and information). Figure 2 shows the likeness of a poster comparing high level details of four personas. Additionally, we maintain a detailed web site that includes the foundation documents, supporting research, and a host of tools for using the personas (screening material for recruiting usability test participants, spreadsheet tools, comparison charts, posters and photos, etc). We utilize email to routinely put small bits of persona information in front of the team (e.g., fact of the week, email from the personas – that’s right, we’ve created email addresses for them). Very important are study participants recruited based on personas, with findings grouped and reported by persona. Generally, we think of the persona effort as an on-going campaign.