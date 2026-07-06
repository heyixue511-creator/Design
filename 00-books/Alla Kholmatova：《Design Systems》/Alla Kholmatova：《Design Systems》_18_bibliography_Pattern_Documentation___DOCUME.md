# Pattern Documentation / DOCUMENTING FUNCTIONAL PATTERNS / Name / Purpose / Example / Variants / DOCUMENTING PERCEPTUAL PATTERNS / Specify Usage, Not Only the Building Blocks / Polaris Colors / Cross-Reference Styles / Show Relationships between the Elements / Color hierarchy / Workflow / PROCESS FOR ADDING NEW PATTERNS / Nordet Trello backlog / CRITERIA FOR ADDING NEW PATTERNS / PEOPLE AND RESPONSIBILITIES / ALIGNING FACETS OF THE SYSTEM / Tools / KEEPING THE PATTERN LIBRARY UP TO DATE / KEEPING MASTER DESIGN FILES UP TO DATE / PATTERN LIBRARY AS THE SOURCE OF TRUTH / The Future Of Pattern Libraries / Conclusion / Further Reading And Resources / OTHER RESOURCES / Copyright Information / Image Credits

> Section: bibliography | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Alla Kholmatova：《Design Systems》\Alla Kholmatova：《Design Systems》\Alla Kholmatova：《Design Systems》\auto\Alla Kholmatova：《Design Systems》.md

## Pattern Documentation

Although many things can be documented alongside each pattern, trying to cover everything right away is not feasible, especially for smaller teams.

To see tangible benefits sooner, start with a lightweight overview of the main patterns. Once you have a simple foundation, you can improve the pattern library over time, by adding features and information the team needs. Here are some of the points to consider when documenting functional and perceptual patterns.

## DOCUMENTING FUNCTIONAL PATTERNS

To make documentation focused and easily scannable, start with the basics:

name•

purpose•

example (visual and code)•

variants•

## Name

Throughout the book I’ve tried to emphasize the importance of a well-chosen name. A good name is focused and memorable, and embodies the purpose of the pattern. Ideally, someone should be able to glean the purpose from the name, without needing to read the description. To help make the page more scannable, names should be prominent and stand out from the rest of the content.

Each pattern’s name is prominently displayed in IBM’s Carbon.

Each pattern’s name is prominently displayed in IBM’s Carbon.

## Purpose

When browsing a pattern library, most people skip descriptions, especially long ones. That’s why they should be focused and to the point: typically, one or two sentences explaining what a pattern is and what it’s for is enough. Although this seems like a simple task, in practice capturing the purpose of a pattern concisely and accurately is not easy. Too often we come up with vague descriptions that don’t have a lot of practical value.

Take a look at how the team at Sipgate initially described a component called “Showcase”:

“Use Showcase to present multiple types of information with a media file.”

Even though factually correct, it doesn’t communicate the purpose of “Showcase”, which makes it more likely to be misused or duplicated. Later, the team adopted a new practice for defining a pattern’s purpose, and writing descriptions. Here’s how it was applied to another example:

“Fact Grid is a shortlist of facts or bits of interesting information. Use Fact Grid to give the reader an immediate impression about the upcoming content.”

This second description is much more effective at communicating what the pattern is for. You might even be able visualize the “Fact Grid” just by reading these two sentences.

Additionally, there are design and content recommendations for making the pattern achieve its purpose in the most effective ways, such as “Maximum of 3 lines per fact” or “Maximum of 12 facts.” Collaborating with a content discipline can be invaluable for defining these rules.

Fact Grid in Sipgate’s pattern library.

Fact Grid in Sipgate’s pattern library 23

## Example

A good example helps to enhance the understanding of the pattern’s purpose. In Marvel’s style guide, examples are self-documenting and show multiple variants and use cases. The UI copy in the pattern helps guide usage further.

In Marvel’s style guide, examples make it easy to see how different popovers behave.

In Marvel’s style guide, examples make it easy to see how different popovers behave.

A lesser example doesn’t help to communicate the purpose. Nothing in the way “Billboard” is presented in FutureLearn’s library suggests that it’s a “prominent promotional element.” Making small adjustments, such as changing the default copy and the background image could help express its purpose more clearly.

“Billboard” in FutureLearn’s pattern library is less than inspiring.

“Billboard” in FutureLearn’s pattern library is less than inspiring.

A living instance of a pattern, with component code alongside it, is usually preferred — it can show responsiveness, interactions and animation. But in some cases a static image or a GIF is more helpful, particularly when you need to show a specific behavior or a state that can’t be recreated in a living example.

Carbon uses a combination of live and static examples to illustrate specific behaviors.

Carbon uses a combination of live and static examples to illustrate specific behaviors.

## Variants

Presenting variants alongside one another, as a suite, makes it easier to see at a glance what is available within the purpose. Not only that, we need to know how the options are different from one another. Although Office Fabric helpfully presents all the variants, it doesn’t explain the differences between them.

Variants in Office Fabric

Variants in Office Fabric.

Compare it with Carbon’s presentation, which clearly states the purpose of each variant.

Types of date pickers and the differences between them clearly explained in Carbon.   
Types of date pickers and the differences between them clearly explained in Carbon.

Similarly, Atlassian’s design guidelines describe when to use each type of button (although, from my point of view, some of the copy, such as “Use when you have nothing to prove,” could benefit from being more precise).

Button variations explained in Atlassian’s design guidelines Button variations explained in Atlassian’s design guidelines.

There are many other aspects that can be important to document, such as:

Versioning of components. If products supported by a pattern library get major• upgrades, some components can benefit from documenting changes in the API or UI elements, relative to previous versions. The same goes for obsolete elements and their replacements.

Team members. Listing people involved in the creation of the pattern, like the Sky• Toolkit example below, can give people a sense of ownership, and also helps<sup>24</sup> with future development.

People involved in Sky Toolkit

Related patterns. Shopify Polaris helpfully shows alternatives if the pattern is• <sup>25</sup> not quite what you’re looking for. This can reduce the chance of patterns being duplicated.

Related patterns

Depending on your team’s needs, there are many other bits of information that can be included. In his article “Taking The Pattern Library To The Next Level” Vitaly Friedman shared two checklists: one for the patterns to document, and another for the things to include alongside each pattern.<sup>26</sup>

## DOCUMENTING PERCEPTUAL PATTERNS

When documenting perceptual patterns, the focus tends to be on the buildings blocks — color palette, typographic scale, and so on. But as we saw in the previous chapter, it’s also important to know how those properties are used and how they work together. Here are a few tips and examples.

## Specify Usage, Not Only the Building Blocks

Representation of color doesn’t have to be limited to a list of variables. In its color palette, the GOV.UK style guide helpfully specifies the usage of color for text, links,<sup>27</sup> backgrounds, and other roles.

Color palette shows patterns of usage in the GOV.UK style guide.

Color palette shows patterns of usage in the GOV.UK style guide.

The dos and don’ts format can also be useful, particularly when there’s an expected misuse. In Shopify Polaris , both indigo and blue are primary colors used for<sup>28</sup> interactive elements. Stating explicitly that blue shouldn’t be used for buttons is helpful in this case, as it would be reasonable to assume otherwise.

## Polaris Colors

The typography section of the US government’s web standards shows type pairings<sup>29</sup> and their recommended usage. Expandable examples demonstrate typographic treatments in context.

US government web standards include pairings and their recommended usage.   
US government web standards include pairings and their recommended usage.

## Cross-Reference Styles

Although we separate styles and components to make them easier to work with, in practice they’re closely interlinked. Even if there are duplications, referencing styles at the module level, as well as separately, is useful. A button has many styles that define what kind of button it is (color, shape, style of label, transitions, spacing, and so on). At the same time, some of those styles can be applied to other objects — menus, links, toggle controls. Sharing styles is what makes those objects feel like they belong to the same system.

In Carbon, the styles of a specific module, such as color, are shown on a separate tab.   
The usage of colors is also documented separately. In Carbon, colors are referenced at both the module level and all together.   
In Carbon, colors are referenced at both the module level and all together.

Take another example: interactive states. Typically, we see them documented only at the module level: here’s a button and its hover state. But it is also useful to see all the states together, at a glance. How does the hover state apply to secondary links? To icon buttons? To ghost buttons? To tab controls? Why in some cases does the outline change to solid, and in others the color value changes?

Showing interactive states for FutureLearn in one grid allowed us to define the overarching rules for interactive states and apply them consistently as more interactive elements were added.

30 Some of the interactive states in FutureLearn’s pattern library are shown together.

## Show Relationships between the Elements

To be effective, perceptual patterns should interconnect and work together. By showing the relationships (between colors, between typography and spacing, between voice and tone and the visuals), you help make the whole system more connected.

The same color values can have entirely different effects when applied in different proportions. As Michael McWatters noted, with too much or too little red, TED can feel like a different brand. The color chips in the Open Table style guide make the<sup>31</sup> hierarchy of colors clear.

## Color hierarchy

Typography and spacing are also closely interlinked. Large, higher-contrast typography requires more white space. Smaller text can get lost in the same amount of space if you don’t compensate by reducing the padding. Even if you have a limited selection of predefined spacing options (such 8px or 16px units), different designers might have different preferences — some prefer more generous white space, others like it cosier. The values might be consistent, but that doesn’t mean that the visual density will be.

To help guide the density and contrast across the product, in FutureLearn’s interface we tried to show the relationship between typography and spacing.

Spacious modules have high typographic contrast (large heading in proportion to• the body font size) and generous spacing to balance out the high-contrast typography.

Regular modules form the majority of sections on FutureLearn. They have the• default heading and spacing.

Compact modules have headings only slightly larger than the body copy.•

Some of the section types for FutureLearn.

Some of the section types for FutureLearn.

Those settings also reflect the purpose of the modules. High-impact promotional sections benefit from high-contrast typography. On the other hand, modules with a supporting function tend to be more compact.

Finally, in the vast majority of today’s pattern libraries, styles are displayed on separate pages. I see this as a limitation. Perhaps the next generation of pattern libraries can show them in more connected ways. Like mood boards or element collages, styles could be presented in a way that shows how they work together, and that highlights signature patterns and the relationships between various elements.

## Workflow

Teams with effective pattern libraries have systematic approaches ingrained in their workflow. How, exactly, varies across companies. Some teams, like Airbnb, have strict and precisely specified processes with powerful tooling. Others are much more informal.

## PROCESS FOR ADDING NEW PATTERNS

One of the foundational aspects to agree on is how the new patterns will be added to the system. The team at Nordnet follows a simple three step process:<sup>32</sup>

Submit a design to the UI kit folder on Dropbox.1.

Discuss the inclusion of the pattern as a team.2.

Document any included designs inside the UI kit. Add the new design to the Craft3. Library which will automatically roll out to the entire team.

The team meet every fortnight to discuss new submissions. They go through a Trello backlog and decide if a module should be approved for inclusion or archived.

## Nordet Trello backlog

A similar workflow is adopted by the teams at Shyp (using GitHub for adding and<sup>33</sup> reviewing the patterns), FutureLearn, and many others. The process doesn’t have to be strict but it’s important to have something in place that enforces, in some way, a regular review of patterns.

To make sure the format of submissions is consistent, some teams find it useful to have a standard template with simple guidelines, such as name, description, author, and date. At FutureLearn, submissions come directly to the pattern library rather than the master design file, and there is an informal guide for writing a description for a pattern. It consists of three questions: What is it? What is it for? How does it achieve its purpose?

## CRITERIA FOR ADDING NEW PATTERNS

A common problem teams have is a lack of agreement on what constitutes a design pattern. A way to manage this is to have shared criteria for adding (and also updating and removing) patterns.

The two most common approaches are:

Every new element on the site is also automatically added to the pattern library.• This works if you’re strict with accepting patterns to the system. There should be a process which checks if a similar pattern exists already, or if an existing one can be modified (such as regular review of new patterns as a team). Without those processes, the risk is ending up with duplicated patterns.

Elements are added only when they’re reused. Some teams add modules only on• the second, or even third use. The idea is that an element has to prove itself as a pattern before being added to the system, which helps to keep the pattern library lean. With this approach it’s important to have visibility of everything being created and effective communication across teams. A log of undocumented patterns should also be kept, so the team has full visibility of what’s available, even if it’s not in the pattern library.

It’s also possible to base your decision on potential reuse. At FutureLearn, the specificity of a component’s purpose is used as a criterion. If an element is defined in a generic way, it is more likely to be reused in the future. In this case, it is added to the pattern library. If a new component has a specific purpose (such as a seasonal promo, a module related to a specific event, and so on), it can be treated as a one-off.

When following this rule, the whole team should take care in how they define components and not make something specific unless absolutely necessary. If someone introduces a one-off, they should share it and explain why it is specific. Occasionally

someone else will find the module useful for their needs. In this situation, we’d redefine the pattern as more generic and add it to the library.

## PEOPLE AND RESPONSIBILITIES

Another aspect to consider is the practicalities of updating documentation, particularly if there’s no dedicated team.

If contributions come from everyone, you have to be strict at making sure they’re added to the library. For instance, adding a component can be a part of the story for creating it. The designer and developer who create a pattern are responsible for adding it to the pattern library. As we saw in chapter 6, this model doesn’t work for every team. Sometimes you need a person or group of people responsible for curating and maintaining the pattern library, even if everyone contributes to it.

If there’s a dedicated design systems team, it’s important to agree on their role, as well as the process for managing contributions. A systems team can have the role of a curator or a producer, and many companies use a combination of both.

Curator. Contributions for new patterns come from all over the organization. The• systems team defines the ways in which internal teams contribute, including setting requirements and the review process. If a submitted pattern doesn’t meet the standards, the team encourages the designers and developers who created it to change it, rather than making the change themselves. The team at Atlassian follow this model.

Producer. With this approach the design systems team creates the majority of• patterns. They’d typically work closely with the product designers in different teams and hold open meetings where others can ask questions, give feedback, or propose missing patterns.The systems team accept submissions from across the company, but they have the final say over what is included, adjusted or removed. Airbnb uses this approach.

When choosing a direction, consider your organizational structure, team culture, and specific product needs. The curator role is usually suited to distributed teams with looser system structures, whereas producers are more common in stricter and more centralized systems.

In both cases it’s important that the systems team are seen as partners, rather than police.

“We want to collaborate with teams as early as possible when they’re thinking about developing new patterns and components. Our relationship with product teams should be a partnership, rather than a situation where someone goes away and does a bunch of work and then we either approve or veto it. If that happens, we’re not doing our jobs very well.”

— Amy Thibodeau, UX lead, Shopify

## ALIGNING FACETS OF THE SYSTEM

Code, design and the pattern library are facets of the same system. Treating it that way makes it more robust, because the system is supported from multiple angles. This doesn’t necessarily mean that the patterns must be fully synchronized. What’s important is that the team practises the same approach across the facets — to naming, structure and understanding of the purpose.

The Carbon design team tries to be as consistent as possible across their Sketch design kit, component library and the code.

In the Carbon design system, names and folder structure are consistent across the three facets of the system.

In the Carbon design system, names and folder structure are consistent across the three facets of the system.

Designers at Nordnet use atomic design to organize folders in their Sketch kit. They even follow BEM naming conventions for their design files, to help developers and designers talk the same language.<sup>34</sup>

When design and code are aligned conceptually, synchronization between them is easier to achieve. It’s also easier to find the tools that fit with your workflow.

## Tools

Keeping the pattern library in sync with production code is one of the main challenges. Teams use different approaches — from manual copy-and-paste, to making a pattern library part of the production environment (Lonely Planet’s Rizzo is an example of the latter). Many tools help to achieve it. Here are some of the most popular ones.

## KEEPING THE PATTERN LIBRARY UP TO DATE

Some of the easiest to implement are CSS documentation parsing tools, such as KSS . They all work in a similar way: comments in the CSS provide a description<sup>35</sup> (which is pulled into the documentation programatically); running a script generates the markup for the pattern library. Parsing tools are relatively simple but limited in functionality. They can also lead to duplicate markup, which can make maintenance more time-consuming.

Among more powerful tools are style guide generators, such as Pattern Lab by Brad<sup>36</sup> Frost, Dave Olsen and Brian Muenzenmeyer. Pattern Lab comes with many useful features, such as responsive preview and support for multiple languages. It’s predominantly suited to larger sites with multiple templates, particularly those that practice atomic design methodology.

Fractal by Mark Perkins is one of the more lightweight and flexible tools which is<sup>37</sup> gaining popularity. Fractal helps build and document a pattern library, and integrate it into your project. One of its main advantages is that it’s flexible and unopinionated — Fractal can work with any templating language and organizational structure.

Full synchronization between the pattern library and the code is extremely difficult to achieve, and companies manage it with varying degrees of success. The ways teams prioritize synchronization also varies:

“It’s always slightly off-sync. If it’s too perfect, it’s not going to work. Our design language, as any language, is constantly evolving. We change details and patterns and we add patterns. We constantly build products. So at any given time there are many versions of the design language. We embrace this fact and design a system which can deal with these imperfections.” — Jürgen Spangl, head of design, Atlassian

In stricter systems and centralized organization it is more important, whereas companies with looser structures are more tolerant to having it out of sync.

## KEEPING MASTER DESIGN FILES UP TO DATE

Designers practicing a systematic approach currently tend to use Sketch as their<sup>38</sup> main tool (largely thanks to the features such as text styles, symbols and artboards, which seem to be well suited for a design system workflow). Teams typically have a master file which contains a UI kit with some or all of the core components and styles. Product designers tend to work from their own files, pulling elements from the master as needed.

The challenge is making sure that the master kit always has the latest patterns. There are many tools to help achieve that — from the lightweight to more comprehensive solutions.

Abstract is a version-controlled hub for your design files. You can create branches,<sup>39</sup> commit explorations, and merge changes. Abstract makes it easier to keep one single source of truth for your design files, including a master UI kit. Another popular tool is Invision’s Craft . Craft is a set of plug-ins for Sketch which syncs the UI kit to anyone<sup>40</sup> who has the plug-in installed. A Craft library can be saved on Dropbox.

More comprehensive options include UXPin , Brand.ai and Lingo . These tools<sup>41</sup> <sup>42</sup> <sup>43</sup> allow you to create and manage a pattern library without having to use code. Naturally, they don’t provide as much flexibility as a custom-built pattern library, but many of them have useful features, such as interactivity of components, Sketch plug-ins for keeping<sup>44</sup> files up to date, integration with Slack that pings a channel when the library is updated, and more.

## PATTERN LIBRARY AS THE SOURCE OF TRUTH

With pattern libraries gaining the “source of truth” status, in some companies it has become somewhat less important to keep master UI kits perfectly up to date. At FutureLearn, the master Sketch file (updated and shared via GitHub) only contains the core granular elements that don’t tend to change (typography, buttons, navigation, and so on). Designers use the pattern library as the main reference for up-to-date patterns, Sketch or Photoshop are used mainly for exploratory work. Because the majority of the components are defined and named, more and more often the team can get by with paper sketches, without needing detailed design specs.

Thanks to design systems and pattern libraries, design and engineering workflows are moving toward each other. There are a lot of experiments in this area , such as tools<sup>45</sup> for generating Sketch files directly from a web page, and importing real data. In the near future we may not have to worry about keeping UI kits in sync, as they could be generated any time from the pattern library.

## The Future Of Pattern Libraries

Tools should accommodate the natural workflow of the whole team. Only then will everyone take ownership, and contributions to the pattern library will be evenly distributed. FutureLearn’s library didn’t have the capability for designers to update descriptions of modules, which in some way reduced their responsibility. Front-end developers were under more pressure to keep the documentation updated, which at times felt like a burden. In the future I hope to see pattern libraries accommodate multidisciplinary workflow. They could become environments where all disciplines could contribute to discussions around design patterns and help define their purpose.

With tools getting better, pattern libraries and a systematic approach to design will continue affecting designers and developers deeply. Many teams are seeing the changes already. Something that used to take days of manual work can be done in minutes — no more detailed design specs, no more reinventing the same solutions again and again. At first, this might seem threatening (Will we have jobs in years to come? Does it take away from the creativity and craftsmanship on the web?). But perhaps the opposite is the case. Design systems free our time and energy to solve bigger and more meaningful problems, like understanding our users better and making design languages more inclusive.

2. https://docs.google.com/

3. https://www.wework.com/

4. http://smashed.by/plasmads

5. http://smashed.by/atlassianpl

6. http://smashed.by/bbcgel

7. http://carbondesignsystem.com/

8. http://smashed.by/rizzopl

9. http://smashed.by/marvelpl

10. http://smashed.by/officefabricp

11. https://www.lightningdesignsystem.com/

12. https://polaris.shopify.com/

13. http://smashed.by/skycomponents

14. https://style.eurostar.com/

15. http://smashed.by/atomicdesign

16. http://smashed.by/ceasefire

17. http://smashed.by/clearfractal

18. http://smashed.by/predix

19. https://medium.com/@lewisplushumphreys

20. http://smashed.by/plasmads

21. https://www.futurelearn.com/pattern-library

22. From email correspondence with Amy Thibodeau, UX lead at Shopify, August 2017

23. https://design.sipgateteam.de/

24. http://smashed.by/skytoolkit

25. http://smashed.by/polarisnav

26. http://smashed.by/pattern2doc

27. http://smashed.by/govuk

28. http://smashed.by/polariscolor

29. http://smashed.by/usgov

30. http://smashed.by/flstates

31. http://smashed.by/opentable

32. See “Super easy Atomic Design documentation with Sketch app” by Ross Malpass.

33. http://smashed.by/shyp

34. See “An Atomic workflow for design & development at Nordnet” by Ross Malpass.

35. http://warpspire.com/kss/

36. http://patternlab.io/

37. http://fractal.build/

38. https://www.sketchapp.com/

39. https://www.goabstract.com/

40. http://smashed.by/craft

41. http://smashed.by/uxpin

42. https://brand.ai/

43. https://www.lingoapp.com/

44. https://www.lingoapp.com/sketch/

45. http://smashed.by/airbnbds

## Conclusion

In programming and design, Christopher Alexander’s pattern discipline has become one of the most widely applied and important ideas. It is now influencing how many of us think about design systems. But there’s an essential feature we may still be missing from Alexander’s original idea: the moral imperative to create systems that make a positive difference to human lives.

In his keynote speech for OOPSLA in 1996, Alexander emphasized<sup>1</sup> that at the root of the architectural pattern language there’s a fundamental question: will these patterns make human life better as a result of their injection into the system? Even if not all of them will have that capacity, there should be at least a constant effort to achieve it.<sup>2</sup>

Many aspects of our lives can now be managed online, from buying groceries and paying bills, to finding a date or completing a degree. As architects of design systems, we play an important part in shaping the digital world. Pattern language gave us a format for thinking about design — and it also gave us a challenge: do the patterns we create have a positive impact on human life? How do we know if they do? How do we continuously test that?

It is hard to carefully consider these questions, when you are given a task to optimize the number of clicks, or encourage people to spend more time on a site. Even with the best intentions, a lot of what we create on the web is designed for short-term commercial benefit, rather than bringing real value to everyday lives: patterns designed to get users hooked , patterns biased towards some population<sup>3</sup> groups, patterns that encourage people to spend time and money in ways they might regret later.

On the other hand, we don’t always consider, for instance, what happens to all our digital accounts and information when someone passes away, how the designs we create improve someone’s quality of life, or how inclusive and empathetic our systems really are.

The pattern language for the web we’re creating is powerful. It has the capacity to influence not only the digital world, but the physical one. We owe it to ourselves, and the people who use our products, to constantly consider and challenge the shape this language takes, and be thoughtful in what we contribute to it.

## Further Reading And Resources

These three books are a great source of knowledge and inspiration for anyone interested in design systems. I kept referring to them again and again while writing this book.

C The Timeless Way of Building by Christopher Alexander<sup>4</sup>

• Thinking in Systems: A Primer by Donella Meadows<sup>5</sup>

How Buildings Learn: What Happens After They’re Built by<sup>6</sup> Stewart Brand

See also:

How to Make Sense of Any Mess by Abby Covert• <sup>7</sup>

Front-end Style Guides by Anna Debenham• <sup>8</sup>

Atomic Design by Brad Frost• <sup>9</sup>

Responsive Design: Patterns and Principles by Ethan Marcotte<sup>10</sup>

Inclusive Design Patterns by Heydon Pickering<sup>11</sup>

## OTHER RESOURCES

Design Systems Slack Team , created by Jina Anne<sup>12</sup>

Design system articles by Nathan Curtis• <sup>13</sup>

Style Guide Podcast , hosted by Anna Debenham and Brad• <sup>14</sup> Frost

Design Systems Newsletter , curated by Stuart Robson• <sup>15</sup>

Responsive Web Design Podcast , hosted by Karen McGrane• <sup>16</sup> and Ethan Marcotte

Website Style Guide Resources• <sup>17</sup>

Thank you for reading. This book is really just the beginning of a conversation about design systems. I’m keen to continue it beyond the book, and would be happy if you’d email me at alla@craftui.com with your thoughts and stories. ❧

1. ACM Conference on Object-Oriented Programs, Systems, Languages and Applications.

3. See “How Technology is Hijacking Your Mind — from a Magician and Google Design Ethicist” by Tristan Harris.

4. http://smashed.by/timeless

5. http://smashed.by/thinksys

6. http://smashed.by/howlearn

7. http://smashed.by/makesense

8. http://smashed.by/fesg

9. http://smashed.by/atomic

10. http://smashed.by/rwdpatterns

11. http://smashed.by/inclusivedesignpatterns

12. http://smashed.by/dslack

13. http://smashed.by/nathan

14. http://styleguides.io/podcast/

15. http://smashed.by/dsnl

16. http://smashed.by/rwdpc

17. http://styleguides.io/

# Copyright Information

## Image Credits

Chapter 1, Visual Loudness Guide: http://smashed.by/visualloudness

Chapter 1, NASA’s Graphics Standards Manual:

http://smashed.by/nasastandards

Chapter 1, Whitney Museum of American Arts:

https://www.experimentaljetset.nl/

Chapter 4, The Washington Examiner 2012 Campaign Site:

Samantha Warren, http://styletil.es/

Chapter 4, Element collage for RIF: Dan Mall, http://danmall.me/

Chapter 5, Minions and Gru: Despicable Me, ©Universal Pictures

Chapter 6, Puma City, LOT-EK: “The Box” by Sibyl Kramer

Chapter 6, Greendo, Keita Nagata: http://www.designboom.com

Chapter 6, Basket Apartments, OFIS architects:

http://www.archdaily.com and http://www.ofis-a.si/