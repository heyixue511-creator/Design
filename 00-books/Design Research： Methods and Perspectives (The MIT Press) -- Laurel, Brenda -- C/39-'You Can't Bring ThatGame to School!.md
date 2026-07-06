# 'You Can't Bring That Game to School!"

Designing Supercharged! HENRY JENKINS, KURT SQUIRE, & PHILIP TAN

In the mid-1990s, The Doonesbury franchise commissioned a campaign simulation game which allowed players to choose a slate of candidates from more than a hundred actual political figures, map their campaign strategy day-by-day and state-by-state, make ad buys, schedule debates and interviews, manage scandals and determine the outcome based on the electoral college. And when the son of one of our researchers played the game, he instantly made the connection to what his parents were watching on CNN, explaining why Dole and Clinton had scheduled stops in key electoral states. When he took the game to school to play during lunch, the school librarian refused, citing a school policy permitting the use of educational software but not games. Her determination that "you can't bring this game to school" was a shocking reminder of the uneasy relationship between education and popular culture.

Within the games industry, edutainment has become a bad word, suggesting an earnest aesthetic, derivative game play and poor production values. Common wisdom is that educational games fail both commercially and creatively. Most simply try to make drill-and-practice feel more palatable. It's a little bit like serving a spinach sundae: the results are not very good for you and not particularly tasty. The only people who disdain such edutainment as much as gamers are learning scientists. Such games embody theories of learning and knowing—based primarily on rote memorization and behaviorist conditioningthat are at least thirty years out of date. The learning sciences now see learning as occurring in social and cultural contexts and as depending on active processes of investigation, experimentation and interpretation.

If traditional edutainment products have been uninspiring and simplistic, James Paul Gee argues in his book What Video Games Have to Teach Us About Learning [2o03] that educators might benefit from studying how game players learn through game play. As he explains, "When kids play videogames they experience a much more powerful form of learning than when they're in the classroom ... . Each level dances around the outer limits of the player's abilities, seeking at every point to be hard enough to be just doable." To achieve this effect, game designers must be thoughtful about sequencing tasks so that players master what they need to do well step-by-step along the way. The designers also have to make these tasks fun in their own right, so that there is no point where playing ends and learning begins.

The Games-to-Teach Project, a joint effort of MIT and Microsoft, has developed a series of conceptual models of games that bring together what we currently know about pedagogical uses of new media with what we know about games as popular culture. We see tremendous opportunities for, say, using simulation and construction games to engage students in engineering or architectural design processes, using role-playing games to immerse students in the roles of doctors, anthropologists or scientists, or multiplayer games to encourage students to think about what life might be like in Colonial America. Few examples of such explicitly educational games exist today, although we can learn a lot by closing examining games already on the market, such as Sid Meier's Pirates or the Civilization series, which allow students to experiment with "what if" questions about history or to learn geography through mastering contested spaces [Jenkins and Squire 2002, Squire 2000].

Our design work cuts across different game genres, different academic fields, different pedagogical models, and different strategies for integrating games into the classroom [Games-to-Teach Team, in press; Holland, Jenkins, & Squire, 2003]. In a few cases, we have begun to develop playable prototypes to illustrate and test our ideas. This is a case study of one such prototype, Supercharged!, describing our design research and how this process has led us to continually rethink our assumptions about gaming, education, research and popular culture.

## Research Approach: Design Experiments

We are, in effect, studying educational games that do not yet and may never exist. Through this process, we hope to learn more about games' pedagogical potentials, factors driving or inhibiting their adoption, their effectiveness, and the kinds of classroom activities needed to support them. Within learning sciences, design experiments enable us to investigate how complex learning occurs within rich social settings when using innovative materials [Brown 1992, Collins 1992]. Whereas naturalistic research creates better understandings of the world and experimental research builds models of specific variables, experiment-based design research strives to develop an underlying theory and create changes in social practices [Cobb et al., 2003]. These complex research goals often require researchers to employ a variety of research techniques (theoretical, humanistic, historical, qualitative, quantitative, naturalistic, or experimental methodologies).

## First Prototype: Supercharged!

"Have you seen Halo? The real-time Physics are incredible," ranted John Belcher, Professor in Astrophysics at MIT and winner of two NASA Exceptional Scientific Achievement Medals. Belcher creates animations to help students learn Physics and thought that games might make his animations more interactive. Digital visualizations can allow students to see and interact with the normally invisible electromagnetic forces around everyday objects. Yet, as Belcher explained it, students had few compelling reasons—apart from passing the test—for studying his visualizations. A game would allow them not simply to observe the laws of electromagnetism at work, but to interact with them to solve puzzles or overcome obstacles. An electromagnetism game might teach players new ways of thinking about their physical surroundings. Gamers are increasingly experiencing games that distort our perception, helping us to see the world through different lenses [Poole 2001]. Could we use shifts in perception to help students learn to see field lines so that they would anticipate their effects even if, as is normally the case, they are invisible?

![](images/ef8705450f96c83347181b7ff13d658a43b932e222cff377daa8f8085cf176a7.jpg)  
A sample of field line visualization from John Belcher.

In our first pass, we imagined a college student, Alina, seated in the back of a classroom. Alina looks under her seat and notices a comic book. Flipping through its colorful pages, she learns about a superhero whose special goggles allow her to see electrostatic forces. Alina flips over the comic and notices a pair of cardboard glasses on the back of the comic. Using these

glasses, she assumes the powers of the comic book's protagonist and flies off to explore the wacky world of electromagnetism. Such a frame story offered a rationale for why Alina could sometimes see field lines, and we hoped a female superhero who has mastered the rules of physics could help us combat gender stereotypes that often disadvantage girls in the science classroom. Adding to the drama, the superhero could battle her evil physics professor who manipulates electromagnetic forces to his diabolical ends. We imagined the player doing a series of environmental puzzies (ala Half-Life), using electromagnetic principles to solve puzzles.

We encountered several problems: rendering all of the electric or magnetic fields operating in any given scenario—from the Earth's magnetic core to local currents—would tax any computer and ultimately be confusing to the student. The alternative would be to develop a "special-case, single instantiation" game that would be extremely hard-railed; that is, the player's actions would be severely constrained and goals narrowly defined. However, if part of the educational allure of games is their capacity to be sandboxes for players to experiment with ideas, we didn't want our first prototype to be a "point and click adventure on Physics!"

Shortly after we reached this painful realization, we met with Alex Rigopulous, MIT alumnus and CEO of Harmonix Music Systems, developers of Playstation 2 games, Frequency and Amplitude. Rigopulous suggested that we embrace a more stylized approach to the game. Graduate student Walter Holland noted that most of the Electromagnetism syllabus could be boiled down to a handful of laws (Maxwell's equations) that expressed electromagnetism as simple mathematical equations describing forces that would, in turn, lead to motion. A rapid brainstorming discussion ensued where we discussed a relatively simple, abstract game—like Frequency or Rez—where the player was a charged particle flying through abstract electromagnetic worlds. We imagined a fast-paced game

![](images/7a32c25ffa860e1ad971897ee5c75b5fd8d3433af876df89803d8a40fa4acd49.jpg)  
Supercharged! concept art

much like first person pinball where the player flew through mazes changing her charge, placing charges and avoiding obstacles.

Over the next month, three graduate students (Walter Holland, Elliot Targum and Robin Hauck) reinvented Supercharged! Starting with the Xbox controller, we imagined that players could use the triggers to place positive and negative charges, and then the XY buttons to flip their own charge. We

designed levels that forced players to confront important ideas in electromagnetism, such as the inverse relationship of electromagnetic force over distances. We adapted the back-story accordingly, imagining the player as the same plucky college student, but this time sucked into a surrealistic world of electrostatic forces through a science experiment gone awry. We imagined this world as populated by a race of small creatures called Fizzgigs that the player would collect as power-ups as she raced through levels. Undergraduates from The Gibbs School developed concept art for the project, and MIT Undergraduate Deborah Lui developed screenshots and storyboards to communicate basic game ideas.

![](images/6a2549cf9f3e0509e8358414e8de024195dac70c3bf8d60f647d9648842523f1.jpg)  
p3dmouse demo of moving particles

## The End of Pre-Production

Once the original game design document was approved for production, we gathered a team of one graduate and four undergraduate students that would develop the game engine over the summer of 2002. Supercharged! was expected to be the flagship undertaking of the Games-to-Teach project complete with a fully 3D engine, quality animation, narration and music. On the surface, we wanted Supercharged! to look and function as if it might belong in the window of a typical videogame store, not on the backroom “edutainment" shelves of preschool suppliers.

These expectations posed enormous challenges. Commercial games require multimillion-dollar budgets and production timelines of two years or more. We had only enough money to keep five full-time students hired for three months. We recruited undergraduates (Robert Figueiredo, Timothy Heidel, Thomas Wilson and Megan Ginter) and graduate student (Philip Tan) with diverse tastes, skill sets and game preferences. Most members were avid gamers and had appreciable programming experience but had never worked together before nor written a 3D game.

![](images/a03f9c0b15d6314516706b0e89a6047507e66721e4e4ac4ae0659780af948312.jpg)

![](images/d6e6295b3aa66cc36142687de4cb47b4c1e7b80aaadb714d646b83d7889eff01.jpg)  
Left: 3D Concept Art for Supercharged! Right: Concept Art of the Ship in Supercharged!

In weeks, the undergraduates created a working technical demo (called "p3dmouse") that featured dozens of charged dots in 3D space, exerting forces on each other and moving in a real-time, wire-frame 3D engine. This rudimentary code demonstrated a 3D engine running an electrostatic simulation and what charged particles might look on screen (and what the world might look like if you were a charged particle).

Next we revisited Harmonix, where Eran Egozy, an MIT alumnus and cofounder of Harmonix, suggested that we examine middleware tools, which are collections of code designed to facilitate the implementation of commercial games. Criterion Software gave us free access to their RenderWare Graphics libraries and ongoing online support in exchange for publicity. However, RenderWare's technology still required a significant amount of exploration. There were no third-party "RenderWare for Dummies" books and, our tight production schedule (60 days to develop a 3D simulation game) meant that losing even a day to undocumented changes in RenderWare could derail our efforts.

Although RenderWare helped bridge the technological divide between the artists and the programmers, there were other obstacles. Physical distance between artists in Boston and programmers in Cambridge slowed production. Ambiguities in the original design document left the student programmers coding the project to make up parts of the game as they went along. Not surprisingly, the undergraduate programmers prioritized development tasks according to their own personal tastes. After a few weeks, the game lost much of its story and the game mechanic of saving Fizzgigs, but irretrievably inherited a first person-shooter style interface. Ultimately the music (a playfully retro soundtrack by composer

![](images/889e7e250df5a7cc733397a5bd4150f4eeb72aa1abcb20bd62503bd1c9197e6e.jpg)

![](images/50a439c7a86d65b06c710ece7f0cadc4a0e3fb8bfecb3000782fac8194dbb6c9.jpg)

Left: An early build of Supercharged! showing dynamically drawn field lines. Right: A screenshot from a typical "tunnel" level in Supercharged! designed to focus players' attention on the goal.

Jerome Rosen) and script helped restore some of the mood and narrative focus envisioned by the original design document.

Despite these conflicts, the summer came to a close with a playable and extensible game engine. Additional levels were added to extend the playability and challenge of the game throughout the subsequent fall semester. The combination of flight-simulator-like game play with first-person-shooter camera controls resulted in a visceral sense of the forces buffeting charged particles while in continuous motion, which we believed to be a significant achievement in getting physics students to think of electrostatics as an actual physical phenomenon rather than a collection of formulae.

## Initial Play Testing

Throughout the fall of 2002, we brought in college and high-school students see if players could understand the basic game premise and objectives, learn the controls and navigate their ship. We were particularly concerned that students would be able to grasp the game premise within a few minutes, given that the game was intended to be used in classroom settings. We also wanted to ensure that the color palette and interface would not alienate non-gamers or non-science-fiction fans.

We brought 12 college and high-school age students into the lab, exposing each to a random order of our three level types (mazes, tunnels and open flying). The players all preferred the first-person shooter style, maze-like interface, which most clearly communicated the objective of the game (get out of the room successfully). The first-person controls were also the most intuitive. Few, if any, of the players had actually played flying games, and most players found the tunnel levels confining. The players who had already studied electromagnetism quickly made links between the game and Physics concepts.

Although all of the players could navigate through the levels and were able to communicate the basic game controls to the testers, most players had difficulty finding their orientation and the exit. To ameliorate this, we added an introduction

![](images/988abcfd3fbd35da9dbbc4f7906e309c2434f9c00e7f7e8bd08160cce01d31db.jpg)

![](images/3c968c2ff69f4e3ec8565fa1ce9eb72337a01713f976063509d8583ce32d29dd.jpg)  
Left: A "tunnel" level in Supercharged! focuses players' attention on the goal. Right: Mazelike Supercharged! level inspired by Doom.  
cut scene for each level where the camera would preview the goalpost and the game characters would explain scientific concepts. We also added digital indicator, which would always be pointed in the direction of the goal and indicate its relative distance from the player's vehicle.

## Controlled Experiments

In the spring of 2003 eight MIT students enrolled in an electromagnetism course participated in controlled laboratory exercises playing Supercharged! We found that participants had many misconceptions about electrostatic forces. Students who could recite Coulumb's Law would fail to predict how charged particles would

![](images/b21307fd5cf043d1f3665e04bc60effbdcf74b3081c42cc26a9dfd5daa5e71dc.jpg)

interact, particularly over varying distances. We designed new levels specifically to address these beliefs. In level 4, we surrounded the goal with two charged particles so that students could experience how their ship would be sucked to the closer charge instead of flying straight into the goal. In pre-test problems similar to this level, roughly half of the plavers believed that their ship, if negatively charged, would fly straight between the two charged particles into the goal. In reality, the ship would probably travel in a curved line toward the closest charged particle. From these controlled studies, we learned that levels designed to address students' current conceptions about electrostatics could help produce conceptual changes. Students would apply these new understandings to subsequent problems.

Supercharged! level designed to combat students'misconceptions

## Moving into Schools: Field Work

Next, we tested how students played Supercharged! within high school contexts. Our first test site was an urban math and science magnet school. Whereas in the lab settings most students patiently sat through cut scenes and deliberately explored the control schemes, these students rushed through the game. Competitive groups formed as students shouted across the room announcing whenever they beat a level. Post-interviews with students revealed that few students made connections between the game play and Physics content. Clearly, more instructional supports were necessary for Supercharged! to be a viable instructional tool.

Our second set of field studies occurred with 125 middle school students at South Waltham Middle School. We developed a two week curriculum that combined playing Supercharged!, doing guided inquiry activities, and discussing electromagnetic concepts. Students reacted to the game much as in the first trial. The boys continued being engaged until they had "beat the game." Girls were generally less interested in the activity, although the 4 to 5 girls in each class who were engaged with the game played it even more purposefully and longer than the boys. Interviews revealed that girls enjoyed the exploring levels, playing with different ideas and trying different approaches.

Each day the class began with the teacher reviewing game concepts with a video project and setting 2 to 3 goals for students. The teacher created reflection sheets which required students to set goals, devise plans, hypothesize how their charged ship would move and monitor the results. The teacher moved from group to group, observing play and asking students thought questions. The teacher ended class by displaying a game level for discussion.

This study highlights how the game-play experience is only partially determined by the game; it is also a function of the students playing it and the social

![](images/6b38b5ea6313572440a5999b9b125fcd2694614291a50bc3d0313b0e8d605cb2.jpg)  
Teacher draws descriptions of Electrostatic concepts on the board.

context that they construct. The "laboratory” milieu frames activity differently than the classroom. In the lab, students worked through the game in very methodical ways, making connections between the game and pre-post exercises. Even when we had students play the game in pairs, we did not see overt competition. Students knew they were testing a game and behaved accordingly. In contrast, bringing the game into school also brought with it the discourse of gamers. Many boys were competitive against the game and against themselves, challenging one another to see who completed the game the quickest or had mastered the controls. Most of the girls who embraced the game explored its boundaries in nondirected ways.

The final site where we used Supercharged! suggests how participants might shape this social milieu to encourage educationally valuable play. By guiding activity, providing scaffolding in the form of worksheets, and encouraging individual and group reflection, the teacher was able to shape the experience so that the game was a useful tool to support learning. Making a meaningful educational intervention isn't simply a matter of designing educational games; it involves mapping strategies for deploying those games in the classroom, recognizing that every classroom has its own social milieu and that each teacher will adapt the game for their own teaching style.

## Conclusions

Now that Supercharged! v1.0 is making its tour across test sites, our research has shown several different directions that future iterations can take. We have already begun testing simple prototypes of other game genres, such as side-scrolling shooters, that could demonstrate electrostatics ways that are accessible to broad audiences. Early design considerations assumed that the fast-paced game would be played on home computers, but integrating the game into a classroom setting has pushed us towards a slower-paced, more cerebral puzzle game that would provide teachers with more opportunities for instructional intervention.

Watching game-play change across contexts reminds us that educational materials and interventions are not simply adopted by educators, but remade in order to meet local needs. In Understanding Popular Culture, John Fiske draws a distinction between mass culture, which is made by media companies, and popular culture, which emerges as consumers adapt those contents for their own purposes, negotiating their meanings in relation to our identities, social structures and existing semiotic patterns [Fiske 1989]. Similarly, designing an educational game involves the negotiation of designers' identities, existing genres, tropes, and pedagogical assumptions. As the game moves into the classroom, further negotiations occur as teachers and students contest over the meanings of games: are they entertainment or education? Are they a fantasy environment or do their rules apply to real world spaces? Can we stop playing long enough to think through the implications of our actions?

As we move forward, we are building teacher support materials and support communities so that teachers have models of how to use the game effectively in class, have peers to learn with, and engage in the critical reflection of their teaching practice [Barab, Barnett and Squire 2002]. Our hope, however, is that this research will do more than just provide interesting insights but also result in products, processes, and social networks that will transform the social practices of schooling. Building on the work of John Dewey, we argue that the best design research is transformative, its value and validity are tested in social settings where its innovations will have an immediate and tangible impact. We hope to not only develop games that can be brought into the classroom but to also develop teachers who know what to do with them when they get there.