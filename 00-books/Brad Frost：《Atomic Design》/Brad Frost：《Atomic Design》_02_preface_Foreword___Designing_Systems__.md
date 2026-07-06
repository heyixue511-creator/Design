# Foreword / Designing Systems / Our paginated past / So what? / Tearing up the page / A manageable strategy / An iterative process / Modularizing content: I’m on Team Chunk / Classy code / Visually repaired / Systematic UI design / UI frameworks, in theory and in practice / Trouble in framework paradise / Design systems save the day / Brand identity / Design language / Voice and tone / Writing / Code style guides / Pattern Libraries / Style guide benefts / Consistently awesome / A shared vocabulary / Education

> Section: preface | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Brad Frost：《Atomic Design》\Brad Frost：《Atomic Design》\Brad Frost：《Atomic Design》\auto\Brad Frost：《Atomic Design》.md

## Foreword

It was 2013, and we huddled with Brad Frost and Jennifer Brook around a sunlit kitchen table in Brooklyn. The four of us had just begun work on a new website for TechCrunch, and we were sketching wireframes in Jennifer’s apartment, wrestling with the new demands of responsive design. Brad pulled out his laptop: “I’ve been playing with a new idea.”

Brad’s screen looked like a webpage had exploded. Bits and pieces of UI foated free of each other, untethered by a unifed design or hierarchy. It looked like a pile of spare parts from a web garage.

Brad fashed his crazy grin and nodded, “Great, right?” The three of us stared back blankly. Somebody coughed.

And then Brad Frost the front-end developer started talking like Brad Frost the chemist. He talked about atoms and molecules and organisms – about how large pieces of design can be broken down into smaller ones and even recombined into diferent large pieces. Instead of visualizing the fnished recipe for the design, in other words, he was showing us the ingredients. And we lit up: this was a shift in perspective, a way to move away from conceiving a website design as a collection of static page templates, and instead as a dynamic system of adaptable components. It was an inspired way to approach this responsive website – and all responsive projects for that matter.

Brad’s new idea was atomic design, and it changed the way we work in this astonishingly multi-device world. By thinking about interfaces simultaneously at both the large (page) level as well as the small (atomic) level, we streamlined our process: we introduced more rigorous thought into the role of every element; we fell into habits that improved the consistency of our UX; and crucially, we started working much faster and more collaboratively. Atomic design was our superpower.

In the early stages of the TechCrunch redesign, there was this moment where we talked about what we wanted the article page to be. Within an hour, Brad had a fully responsive version wired up from his kit of parts. That was the moment we realized just how quickly we were going to be able to move, a powerful case for investing in this clever, modular approach.

Almost four years later, we haven’t looked back. Brad continued to refne his techniques and tools over the projects that followed,

including blockbuster sites for Entertainment Weekly and Time, Inc. We’ve used these lessons to help in-house product teams make sites faster and with higher quality, build massive design systems for organizations looking to centralize their design and development work across international ofces, and much more.

Atomic design gave us speed, creative freedom, and fexibility.   
It changed everything. We think it will do the same for you, too.

This wonderful book explains the philosophy, practice, and maintenance of atomic design systems. And it does so with the cheerful, helpful generosity that so describes Brad himself.

Brad’s energy and big-hearted enthusiasm for the web and its makers are boundless. For years, Brad has worked at the forefront of responsive design technique – and he’s shared everything along the way. His This Is Responsive site is the go-to resource for fnding responsive solutions to any UX problem. His blog and Twitter feeds share his roadblocks and his solutions. When designers and developers follow Brad Frost, they get a fast and dense stream of practical, passionate insight for building beautiful and resilient websites. This book doubles down on all of that.

Given the chance, Brad would knock on the door of every designer and developer to personally deliver his message. We’ve watched with astonishment (and mild envy) as this whirling dervish has barnstormed around the globe to share his advice with hundreds of teams and organizations across six continents. (Atomic design, coming soon to Antarctica!) But even Brad Frost can’t be everywhere at once, and we’re delighted that he’s detailed his ideas with such depth and good humor in this book.

Atomic design is blowing up around the world; it transformed our design practice; and we’re excited for it to bring the same creative combustion to your process, too.

\- Josh Clark and Dan Mall, Brad’s frequent collaborators and his biggest fans

Chapter 1

## Designing Systems

Create design systems, not pages

A long, long time ago, there were these things called books. Remember them? These contraptions were heavy and bulky and made from the pulp of dead trees. Inside these books were things called pages. You turned them, and they cut your fngers.

Awful things. I’m so glad these book things with their razor-sharp pages aren’t around anymore.

Oh, wait…

## Our paginated past

The page has been with us for a long time now. A few millennia, actually. The frst books were thick slabs of clay created about 4,000 years ago, soon replaced by scrolls as the preferred way to consume the written word. And while reading technology has come a long way – from papyrus to parchment to paperback to pixels – the concept of the page holds strong to this day.

The page metaphor has been baked into the lexicon of the web since the very beginning. Tim Berners-Lee invented the World Wide Web so that he, his colleagues at CERN, and other academics could easily share and link together their world of documents. This documentbased, academic genesis of the web is why the concept of the page is so deeply ingrained in the vocabulary of the internet.

## So what?

As we’ll discuss throughout this book, the way things are named very much impacts how they’re perceived and utilized. Thinking of the web as pages has real ramifcations on how people interact with web experiences, and infuences how we go about creating web interfaces.

From the beginning, the page metaphor provided users with a familiar language with which to navigate this brave new World Wide Web. Concepts like bookmarking and pagination helped new web users explore and eventually master an entirely new medium using conventions they were already comfortable with.

![](images/70ff352d8d165f03cc2176b06aac54262e0741ebadf590a560e13e74b4027ac8.jpg)  
Chrome browser displaying ‘This webpage is not available’ message.

The page was – and continues to be – a very visible and helpful metaphor for the users of the web. It also has a profound infuence on how web experiences are created.

In the early days of the web, companies looking to get online simply translated their printed materials onto their websites. But even though these brochure websites ofered a very one-dimensional perspective of what the web could ofer, viewing websites as digital representations of the printed page was easy for creators to wrap their heads around.

But we’re now 25 years into this new medium, and this once necessary fgure of speech has overstayed its welcome. Unfortunately, the page metaphor continues to run deep with respect to how we scope and execute our web projects. Here are just a few examples I hear on a regular basis:

“We’re a startup looking to launch a fve-page website this October…”

“Brad, how long will the homepage take to build?”

“How are we ever going to redesign this university website that contains over 30,000 pages?!”

All of the statements above make the fundamental mistake of assuming a page is a uniform, isolated, quantifable thing. The reality is that the web is a fuid, interactive, interdependent medium. As soon as we come to terms with this fact, the notion of the page quickly erodes as a useful means to scope and create web experiences.

How long will a homepage take to build? Well, that sort of depends on what’s on it, right? Maybe the homepage simply consists of a tagline and a background image, which means it could be done by lunch. Or maybe it’s chock-full of carousels, dynamic forms, and third-party integrations. In that case, maybe the homepage will take several months to complete.

As for the 30,000-page university website, it might be tempting to declare, “Thousands of pages?! Wow, that sounds challenging!” But in reality, those 30,000 pages may consist of three content types and two overarching layouts.

Ultimately, a project’s level of efort is much better determined by the functionality and components contained within those pages, rather than on the quantity of pages themselves.

The page metaphor has served its purpose helping users familiarize themselves with the web, and provided creators with the necessary transitional language with which to create for a brand new medium. But to build thoughtful interfaces meant to be served to a multitude of connected devices, the time has come for us to evolve beyond the page.

## Tearing up the page

Thankfully, the web community is hard at work establishing principles and practices to help us efectively talk about and create for the web. And there’s one concept that keeps popping up in every conversation about how to make successful web experiences: modularity.

Modularity predates the web by a long shot. The Industrial Revolution brought about interchangeable parts and Henry Ford’s assembly line forever transformed the automobile manufacturing process. The earliest cars and components were individually crafted, which led to many safety and maintainability nightmares. Ford broke the automobile down into its component parts and modularized the assembly process. The results spoke for themselves: more uniform, more reliable, safer cars rolled out of the factory, and in record time to boot.

As the machine age became the computer age, computer scientists began practicing object-oriented programming and establishing important modular concepts like separation of concerns and the single responsibility principle. It is from this world that the World Wide Web was born, so it’s no surprise that modular design quickly became a design principle for the architecture of the web.

Slowly, but surely, these concepts found their way into web designers’ workfows. In the early 2000s we saw the introduction of libraries like YUI and jQuery UI that provided developers with a toolkit of widgets and patterns to create more consistent user interfaces.

If modularity has been around for such a long time, why are we talking about it now?

The short answer is that modularity matters more than ever. Right now, our entire industry is drowning in a sea of devices, viewport sizes, and online environments. And things aren’t slowing down anytime soon.

Disruption will only accelerate. The quantity and diversity of connected devices – many of which we haven’t imagined yet – will explode, as will the quantity and diversity of the people around the world who use them. Our existing standards, workfows, and infrastructure won’t hold up. Today’s onslaught of devices is already pushing them to the breaking point. They can’t withstand what’s ahead.

\- The Future-Friendly manifesto

![](images/ea52aa5bb32b2ab493e0e28c7d0a1ceb84e4e3d05613914be554108833f06332.jpg)  
These are just some of the connected devices we need to worry about.

Like it or not, this multi-device universe is our reality. It was hard enough to get our web pages to display consistently in a handful of desktop browsers, but we’re now tasked with ensuring our web experiences look and function beautifully on a dizzying array of smartphones, tablets, phablets, netbooks, notebooks, desktops, TVs, game consoles, and more.

To address this reality while maintaining our sanity, it’s absolutely necessary for us to take a step back and break these giant responsibilities into smaller, more manageable chunks.

And that’s exactly what folks are doing. The spirit of modularity is weaving its way into every aspect of the web creation process and having profound efects on organizations’ strategy, process, content, design, and development.

## A manageable strategy

Every organization is fnally realizing that bulldozing their entire website and replacing it with a New-And-Shiny™ website every three to eight years isn’t (and never was) an optimal solution.

Out with the old! In with the new! It’s certainly an attractive prospect. But even before the launch party confetti is swept up, the calls start coming in. “You moved my cheese!” cry the users, who spent years learning the previous interface and functionality.

When massive redesigns launch with signifcant changes to the experience, users get knocked down what Jared Spool calls the “Magic Escalator of Acquired Knowledge”. Huge redesigns are a jolt to the system, and newly frustrated users have to spend a great deal of time and energy relearning the experience in order to slowly climb back up that escalator of acquired knowledge.

In addition to disorienting users, these monolithic redesigns don’t get to the organizational root of the problem. Without a fundamental change in process, history is bound to repeat itself, and what’s New-And-Shiny™ today becomes Old-And-Crusty™ tomorrow. The cycle repeats itself as companies push of minor updates until the next big redesign, ultimately paralyzing themselves and frustrating users in the process.

Thankfully, even massive organizations are taking cues from the smaller, leaner startup world and striving to get things out the door quicker. By creating minimum viable products and shipping often to iteratively improve the experience, organizations are able to better address user feedback and keep up with the ever-shifting web landscape.

Moving away from Ron Popeil-esque, set-it-and-forget-it redesigns requires deliberate changes in organizational structure and workfow. Which is a heck of a lot easier said than done.

## An iterative process

If I had a quarter for every time I heard some stakeholder declare “We’re trying to be more agile,” I’d be orbiting the earth in my private spacecraft instead of writing this book.

Wanting to be more agile is commendable. But agile is a loaded term, with big diferences between capital-A Agile and lowercase-a agile. Capital-A Agile is a specifc methodology for software development, equipped with a manifesto and accompanying frameworks like Scrum and Lean.

Lowercase-a agile is more of an informal desire to create an efcient process. This desire may certainly involve adopting general principles from capital-A Agile, but it may not involve adopting the Agile process in its entirety. Project manager Brett Harned explains:

We want to be more agile; we’re embracing change, continuing improvement, being as fexible as possible, and adapting as we see ft. The thing is, we won’t ever truly be Agile, as the Manifesto states. That’s okay, as long as we say what we will be.

\- Brett Harned

Organizational structure, client relations, personalities, and so on all play major roles in determining a project’s process. The trick is to fnd the process that works best for you, your organizational constraints and opportunities.

Even though it may be impossible to adopt a truly Agile process, it’s still a sound idea to work in cross-disciplinary teams, get into the fnal environment faster, ship early and often, and break bigger tasks into smaller components. In chapter 4, we’ll detail how to establish an efective pattern-based workfow.

## Modularizing content: I’m on Team Chunk

Get your content ready to go anywhere, because it’s going to go everywhere.

\- For A Future-Friendly Web

Publishing content for the Web used to be a fairly straightforward endeavor, as the desktop web was the only game in town. Oh, how things have changed. Today, our content is consumed by a whole slew of smartphones, dumb phones, netbooks, notebooks, tablets, e-readers, smartwatches, TVs, game consoles, digital signage, car dashboards, and more.

To properly address this increasingly diverse and eclectic digital landscape, we need to dramatically overhaul our perception of content and the tools we use to manage it.

In the future, what I believe is that we are going to have better content management and content publishing tools. We are going to have ways to take well-structured content, welldesigned chunks of content that we can then fgure out how we want to restructure and publish and display in a way that’s going to be right for the appropriate platform.

\- Karen McGrane

Thankfully, this future is starting to take shape. Organizations are recognizing the need to create modularized content to better reach their audience wherever they may be. And content management systems are evolving beyond their web publishing platform roots into tools that can elegantly create and maintain modular content. While sophisticated content management systems have existed for years in the form of custom solutions like NPR’s COPE (Create Once, Publish Everywhere) platform, smart modular thinking is making its way into mainstream content management systems.

## Classy code

Modularity has long been a staple principle in the world of computer science, as we discussed earlier. While this principle existed long before the web was invented, it has taken some time for modularity to become engrained in the minds and hearts of web developers.

Despite being around since 1995, JavaScript, the programming language of the web, frst had to endure some growing pains to mature into the capable, respected language it is today. Now that JavaScript has grown up, developers can apply those tried-and-true computer science principles to their web development workfows. As a result, we’re seeing folks develop sophisticated JavaScript patterns and architectures.

Applying modular programming principles to JavaScript is a bit of a no-brainer, since JavaScript is itself a programming language. But object-oriented thinking is weaving its way into other aspects of the web as well, including CSS, the styling language of the web. Methodologies like OOCSS, SMACSS, and BEM have cropped up to help web designers create and maintain modular CSS architectures.

## Visually repaired

Not only is modularity infltrating the code side of style on the web, it’s revolutionizing how visual designers approach modern web design.

As the number of viewports and environments proliferate, it’s become untenable to produce static mockups of every page of a web experience. As Stephen Hay quipped, presenting fully baked Photoshop comps “is the most efective way to show your clients what their website will never look like.”

That’s not to say static design tools like Photoshop and Sketch aren’t important. Far from it. But it’s the way we use these tools that has changed dramatically. While creating hundreds of full-on comps isn’t realistic, these static tools excel at providing a playground to establish what Andy Clarke calls “design atmosphere”:

Atmosphere describes the feelings we get that are evoked by colour, texture and typography. You might already think of atmosphere in diferent terms. You might call it “feel”, “mood” or even “visual identity.” Whatever words you choose, the atmosphere of a design doesn’t depend on layout. It’s independent of arrangement and visual placement. It will be seen, or felt, at every screen size and on every device.

\- Andy Clarke

Establishing design atmosphere early is critical to a project’s success, which is why designers have found ways to facilitate these important conversations without having to generate full mockups. Designer Samantha Warren developed design artifacts called style tiles, which demonstrate color, type, and texture explorations in a nice encapsulated one-pager. Designer Dan Mall built on Samantha’s idea with a concept called element collages, which demonstrate design atmosphere explorations in an exploded collage of interface elements.

![](images/d76a443401bc097445d269ebb99e9d6b67a244ac0c5d22fafa71eb3ec33b1470.jpg)  
Style tiles, a concept created by designer Samantha Warren, allow designers to explore color, typography, and texture without having to develop fully realized comps.

By breaking visual explorations into smaller chunks, designers save time and efort while avoiding presenting unrealistic, premature layouts to clients. More importantly, these approaches shift stakeholders away from simply reacting to a pretty picture, and instead facilitate crucial conversations about overall design direction and how they relate to the project’s goals. We’ll discuss these concepts in more detail in chapter 4, but sufce it to say the visual design workfow is changing in a big way!

## Systematic UI design

We’re not designing pages, we’re designing systems of components.

\- Stephen Hay

What is an interface made of? What are our Lego bricks? What are our Subway sandwich pieces that we combine into millions of delicious combinations? It’s these questions that we’ve been asking ourselves more and more now that we’re sending our interfaces to more and more places.

A few years ago Ethan Marcotte introduced us to the idea of responsive web design and its three core tenets: fuid grids, fexible media, and CSS media queries. These three ingredients provided a much-needed foundation for designers to create fexible layouts

that smartly adapt to any screen size. Perhaps more importantly, responsive design helped get designers excited about creating thoughtful, adaptable, multi-device web experiences.

As designers quickly discovered, creating multi-device web experiences involves a lot more than creating squishy pages. Each individual piece of an interface contains its own unique challenges and opportunities in order for it to look and function beautifully across many screen sizes and environments.

How can we present primary navigation – typically displayed as a horizontal list on large screens – in a thoughtful way on smaller screens? How do lightboxes, breadcrumbs, and carousels translate to smaller viewports and alternate input types? It’s these questions that led me to create This Is Responsive, a showcase of responsive patterns that demonstrate the various ways a particular component could be executed in a responsive environment.

While This Is Responsive is successful at articulating how these interface patterns can scale across screen sizes and environments, it’s still up to designers and developers to put these patterns into action. And as it turns out, that’s a lot of work.

## UI frameworks, in theory and in practice

Designers and developers are already strapped for time and resources, and they’re now being tasked with making interfaces that look and function beautifully in any environment. That’s a very tall order.

This need to address growing device diversity while still sanely getting projects out the door has given rise to frontend frameworks like Foundation by Zurb and Bootstrap. These user interface frameworks provide designers with a collection of preassembled HTML patterns, CSS styles, and JavaScript to add functionality to interactive components like dropdowns and carousels. In essence, these frameworks are handy tool kits for quickly assembling interfaces.

![](images/9596dea906accd3864b6bca829c818baae13886406157275ca179333bb1a10cb.jpg)  
Bootstrap provides a collection of UI components to speed up development.

And boy are these things popular. As I’m writing this, Bootstrap is the most popular repository on the code-sharing site GitHub, with over 77,000 stars and 30,000 forks. These frameworks’ popularity is a testament to the fact that designers and developers are seeking solid ground to stand on in this ever-complex web landscape.

One of the most attractive aspects of these frameworks is speed. Frameworks like Bootstrap allow designers to get ideas of the ground quickly, rapidly create prototypes, and launch sites sooner. Because the patterns provided by a tool kit are already crossbrowser tested, developers can spend their time on more important tasks rather than beating their heads against a table testing some archaic version of Internet Explorer. And in case designers do get stuck, these frameworks’ communities can provide helpful support and advice.

For freelancers, this increase in speed might mean they can take on an extra project or three, yielding more fnancial stability for the year. And in the startup world – a place where Bootstrap is omnipresent – minimum viable products can launch sooner, leading to faster answers regarding the products’ viability.

So frameworks like Bootstrap are insanely popular design systems that provide well-tested components, resulting in consistent designs and faster launches. What’s not to love? Well, like most everything in life, there are cons right there alongside the pros.

## Trouble in framework paradise

When I was a kid, I’d watch sci-f movies and TV shows with a strange fascination. There was one question I could never quite shake: why are they all dressed the same?

![](images/d1a9caaa8f44e4619100d4912d55ef4f03f5f946ab3e3deccf25e70cd8d8453d.jpg)  
In the future, everyone dresses the same. Illustration credit: Melissa Frost.

I could only guess that given enough time, we solve fashion. “Say, these jumpsuits are pretty snazzy, and comfortable too! Let’s just all wear these from now on.” “Sounds good to me!”

Of course, that’s not how human beings work. We all have diferent tastes, goals, and desires. Variety, as they say, is the spice of life, and fashion, music, and design refect our diverse nature. Yet on the web we tend to fall into the trap of wanting everyone to do things the same way. “Why don’t all browsers just standardize on WebKit?” “Why can’t device manufacturers just use the same screen sizes?” “Always use jQuery!” “Never use jQuery!” “Just use frameworks!” “Never use frameworks!”

Just like the real world, the diverse needs, goals, and desires of web projects lead to a myriad of diferent solutions. Of course, there’s a time and place for everything, and designers and developers need the discernment to know which tools to use and when.

Front-end frameworks are tools that provide a specifc solution and a particular look and feel. While those solutions help speed up development, the resulting experiences end up resembling those sci-f jumpsuits. When everyone uses the same buttons, grids, dropdowns, and components, things naturally start to look the same. If Nike, Adidas, Puma, and Reebok were to redesign their respective sites using Bootstrap, they would look substantially similar. That’s certainly not what these brands are going for. Sure, each brand can modify and extend the default look and feel, but after a while customization means fghting the framework’s given structure, style, and functionality.

In addition to look-alike issues, these frameworks can add unnecessary bloat to an experience. It’s fantastic that frameworks provide plenty of prebuilt components and functionality, but a large percentage of designers and developers won’t adopt every aspect of the framework. Unfortunately, users still have to download the framework’s unused CSS and JavaScript, resulting in slower page loads and frustration.

On the fip side of that coin, frameworks might not go far enough, leading to developers needing to create a substantial amount of custom code to achieve their projects’ goals. At some point, a threshold is crossed where the initial benefts of using a framework–namely development–are outweighed by the time spent modifying, extending, and fxing the framework.

And then there’s the issue with naming. Using a framework means subscribing to someone else’s structure, naming, and style conventions. Of course, it’s important to establish a useful frontend lexicon, but what makes sense for an organization might not be what comes out of a framework’s box. I, for one, would balk at the idea of using Bootstrap’s default component for a featured content area they call a “jumbotron”. How a framework’s naming conventions jive with an existing codebase and workfow should be properly discussed before jumping on board the framework train.

Now that we’ve put frameworks through the wringer, it’s important to take a step back and recognize that conceptually these frameworks are very much on point. It’s an excellent idea to work with a design tool kit that promotes consistency and speeds up development time. While discussing the redesign of Microsoft’s homepage by Austin-based web shop Paravel, developer Dave Rupert stressed the importance of creating and delivering a design system to their client. Dave wonderfully articulated that it’s not necessarily about using Bootstrap for every client, but rather creating “tiny Bootstraps for every client.”

Responsive deliverables should look a lot like fully-functioning Twitter Bootstrap-style systems custom tailored for your clients’ needs. These living code samples are self-documenting style guides that extend to accommodate a client’s needs as well as the needs of the ever-evolving multi-device web.

\- Dave Rupert

It’s not just about using a design system, it’s about creating your system.

## Design systems save the day

So what do robust design systems look like? What form do they take? How do you create, maintain, and enforce them?

The cornerstones of good design systems are style guides, which document and organize design materials while providing guidelines, usage, and guardrails.

As it happens, there are many favors of style guides, including documentation for brand identity, writing, voice and tone, code, design language, and user interface patterns. This book won’t detail every category of style guide, but it’s important to take a look at each to better understand how each style guide infuences the others, and how style guides for the web ft into a larger ecosystem.

## Brand identity

Brand identity guidelines defne the assets and materials that make a company unique. Logos, typography, color palettes, messaging (such as mission statements and taglines), collateral (such as business card and PowerPoint templates), and more are aggregated and described in brand identity guidelines.

![](images/3cb3a238d904088c723df2b0a6126642f48ad80e625a8295d652460545ec1eb4.jpg)  
West Virginia University’s brand style guide.

It’s essential for a brand to present itself in a cohesive manner across an increasing number of media, channels, and touchpoints. How can everyone within an organization speak in one voice and feel part of a singular entity? How do third parties know which Pantone colors to use and how to correctly use the brand’s logo? Brand identity guidelines provide answers to these fundamental questions in one centralized hub.

Historically, brand identity guidelines were contained in hardcover books (remember, those things with the pages?), but as with everything else, brand style guides are making their way online.

## Design language

While brand identity guidelines are fairly tactile, design language guidelines are a bit harder to pin down. Design language style guides articulate a general design direction, philosophy, and approach to specifc projects or products.

To present itself in a cohesive way across a growing range of products and media, Google developed a design language called material design. The material design style guide defnes its overarching design philosophy, goals, and general principles, while also providing specifc applications of the material design language.

![](images/ef747d27dd337c6ab6c9f06ddb38ce8d75af7506fda220e8968110f30d650c55.jpg)  
Google’s material design language.

Design language style guides can (and usually do) incorporate aspects of other style guide categories in order to make high-level concepts a bit more tangible.

Design language guidelines aren’t set in stone the way brand guidelines are. For example, one day Google will likely develop a new design language to replace material design, so while Google’s overall brand will remain intact, the design vocabulary around its products will change.

## Voice and tone

People interact with brands across a huge array of channels and media. In addition to the digital media we’ve discussed so far, brands also operate in print, retail, outdoor, radio, TV, and other channels. When a brand must communicate across so many varied touchpoints, speaking in a unifed, consistent manner becomes critical to a brand’s success.

A brand’s voice stays the same from day to day, but its tone has to change all the time, depending on both the situation and the reader’s feelings.

\- Kate Kiefer Lee

Voice is an elemental aspect of a brand’s identity, so typically brand identity guidelines include some reference to the brand’s voice. However, these guidelines usually aren’t very nuanced, which is why voice and tone guidelines are so important.

![](images/c18532e400eea467503e57fcd8b3678ed6be341ba76e0ca0759b9ce812d9d6dd.jpg)  
MailChimp’s Voice and Tone guidelines

Voice and tone guidelines get into the weeds by articulating how the company’s voice and tone should shift across a variety of scenarios. MailChimp’s brilliant voice and tone guidelines defne how the brand’s tone changes across content types, so that when a user’s credit card is declined, writers know to shift away from their generally cheeky and playful tone of voice and adopt a more serious tone instead.

## Writing

The rise of the web and content-managed websites makes it easier than ever for many people within an organization to publish content. This, of course, can be a double-edged sword, as maintaining a consistent writing style for an organization with many voices can be challenging. Writing style guides provide every author some guidelines and guardrails for contributing content.

Writing style guides can be extremely granular, defning particulars around punctuation and grammar, but they don’t always have to be so detailed. Dalhousie University’s writing style guide provides a concise list of principles and best practices for content contributors to follow.

![](images/462cb3d61a1ad4d166af7db5160a5c8eb13692f0500fe77e3a8e9e382bd1f359.jpg)  
The Economist’s writing style guide.

## Code style guides

It’s essential for teams to write legible, scalable, maintainable code. But without a way to promote and enforce code consistency, it’s easy for things to fall apart and leave every developer to fend for themselves.

Code style guides provide conventions, patterns, and examples for how teams should approach their code. These guidelines and guardrails help rein in the madness so that teams can focus on producing great work together rather than refactoring a bunch of sloppy, inconsistent code.

![](images/9918bf1bda6223dde1a34714e47b19575332cd7de0d3790e4099594f6313aca5.jpg)  
GitHub’s code style guide provides best practices for writing HTML, CSS, JavaScript, and Ruby within their organization

## Pattern Libraries

And now for the main event. Pattern libraries, also known as frontend style guides, UI libraries, or component libraries, are quickly becoming a cornerstone of modern interface design.

![](images/057f0724bd8a6e6021fcf38ceb1c93f5c1acced436894fb147c92666c04f2d0e.jpg)

The rest of this book will concentrate on how to approach interface design in a systematic manner, and detail how to establish and maintain pattern libraries.

## Style guide benefts

Getting UIs to work across a myriad of screen sizes, devices, browsers, and environments is a tall order in and of itself. But once you factor in other team members, clients, stakeholders, and organizational quirks, things start looking downright intimidating.

Style guides are important tools that help prevent chaos, both from a design and development standpoint and also from an organizational perspective. Here’s why style guides are now essential tools for modern web design and development.

## Consistently awesome

Web style guides promote consistency and cohesion across a user interface. This consistency benefts both the people who create these interfaces and also their users.

I recently visited my health insurance provider’s website to pay my bill. In the course of fve clicks, I was hit with four distinct interface designs, some of which looked like they were last touched in 1999. This inconsistent experience put the burden on me, the user, to fgure out what went where and how to interpret disparate interface elements. By the time I got to the payment form, I felt like I couldn’t trust the company to successfully and securely process my payment.

Style guides help iron out these inconsistencies by encouraging reuse of interface elements. Designers and developers can refer back to existing patterns to ensure the work they’re producing is consistent with what’s already been established.

Even third parties responsible for matching their UIs with the look and feel of a company’s internal UIs can make great use of a style guide. Externally hosted experiences like payment portals or localized sites can better match the look and feel of the primary experience by applying the styles defned in the guide.

Making style guides central to your process results in user interfaces that feel more united and trustworthy, which helps users accomplish their tasks faster and empowers them to master the interface.

## A shared vocabulary

What does “utility toolbar” mean? Does everyone understand what a “touch slider hero” is?

As the number of people working on a project increases, it becomes all too easy for communication breakdowns to occur. It’s not uncommon for diferent disciplines to have diferent names for the same module, and for individuals to go rogue and invent their own naming conventions. For true collaboration to occur, it’s essential for teams to speak a common language. Style guides are there to help establish that shared vocabulary.

![](images/c0c9188caa7e6589e4aa7b97f4ce337a70ee71bb99f72e178f1368c8a515dd3e.jpg)  
Giving names to patterns like ‘Blocks Three-Up’ in Starbucks’ style guide helps team members speak the same language.

Style guides establish a consistent, shared vocabulary between everyone involved in a project, encouraging collaboration between disciplines and reducing communication breakdowns.

## Education

In her book Front-End Style Guides, Anna Debenham deftly explains the many advantages of creating style guides, including one of the most crucial benefts: education.

Education is as important as documentation. A style guide can show clients that websites are systems rather than collections of pages.

