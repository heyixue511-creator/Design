# Play asResearch

The Iterative Design Process

ERIC ZIMMERMAN

## Needs and Pleasures

Design is a way to ask questions. Design Research, when it occurs through the practice of design itself, is a way to ask larger questions beyond the limited scope of a particular design problem. When Design Research is integrated into the design process, new and unexpected questions emerge directly from the act of design. This chapter outlines one such research design methodology—the iterative design process—using three recent game projects with which I have been involved.

The creation of games is particularly well suited to provide a model of research through design. In this book's conclusion, Brenda Laurel alludes to the difference between designing to meet needs and designing "for delight"316 LAUREL. While all forms of design partake of both of these categories in some measure, game design is particularly skewed toward the creation of delightful experience, rather then the fulfiliment of utilitarian needs. Although it is true that we can create and play games for a particular function (for exercise, to meet people, to learn about a topic), by and large, games are played for the intrinsic pleasures they provide.

As a form of designed "delight," the process of interacting with a game is not a means to an end, but an end in and of itself. It is this curious quality of games that makes them wonderful case studies for Design Research through the process of design. As a game evolves (through the iterative process outlined below), it defines and redefines its own form, the experiences it can provide for players, and the very questions about design that it can ask. Through this play of design itself, new questions come into being, present themselves to the designers, and sometimes are even answered.

## Iteration Iteration

Iterative design is a design methodology based on a cyclic process of prototyping, testing, analyzing and refining a work in progress. In iterative design, interaction with the designed system is used as a form of research for informing and evolving a project as successive versions or iterations of a design are implemented.

Test; analyze; refine. And repeat. Because the experience of a viewer/user/ player cannot ever be completely predicted, in an iterative process design decisions are based on the experience of the prototype in progress. The prototype is tested, revisions are made, and the project is tested once more. In this way, the project develops through an ongoing dialogue between the designers, the design, and the testing audience.

![](images/6bcb6d81dc280d8320c41e072011a8e39b88216f474264ee9428d13c3d5dc38d.jpg)

In the case of games, iterative design means playtesting. Throughout the entire process of design and development, your game is played. You play it. The rest of the development team plays it. Other people in the office play it. People visiting your office play it. You organize groups of testers that match your target audience. You have as many people as possible play the game. In each case, you observe them, ask them questions, then adjust your design and playtest again.

This iterative process of design is radically different than typical retail game development. More often than not, at the start of

The iterative design process

the design process for a computer or console title, a game designer will think up a finished concept and then write an exhaustive design document that outlines every possible aspect of the game in minute detail. Invariably, the final game never resembles the carefully conceived original. A more iterative design process, on the other hand, will not only conserve development resources, but will also result in a more robust and successful final product.

## Case Study 1: SiSSYFiGHT 2000

Summary: SiSSYFiGHT 2000 is a multiplayer online game in which players create a schoolgirl avatar and then take part in games where 3 to 6 players vie for dominance of the playground. Each turn α player selects one of six actions to take, ranging from teasing and tattling to cowering and licking α lolly. The outcome of an action is dependent on other players' decisions, making for highly social gameplay. SiSSYFiGHT 2000 is also a robust online community. You can play the game at wov..sissyf.ght.con.

In the summer of 1999, I was hired by Word.com to help them create their first game. We initially worked to identify the project's play values: the abstract principles that the game design would embody. The list of play values we created included designing for a broad audience of non-gamers; a low technology barrier; a game that was easy to learn and play but deep and complex; gameplay that was intrinsically social; and finally, something that was in concert with the smart and ironic Word.com sensibility.

These play values were the parameters for a series of brainstorming sessions, interspersed with group play of computer-based and non-computer games. Eventually, a game concept emerged: little girls in social conflict on a playground. While every game embodies some kind of conflict, we were drawn towards modeling a conflict that we hadn't seen depicted previously in a game. Technology and production limitations meant that the game would be turn-based, although it could involve real-time chat.

Once these basic formal and conceptual questions had begun to be mapped out, the shape of the initial prototype became clear. The very first version of SiSSYFiGHT was played with post-it-notes around a conference table. I designed a handful of basic actions each player could take, and acting as the program, I "processed"the actions each turn and reported the results back to the players, keeping score on a piece of paper.

Designing a first prototype requires strategic thinking about how to most quickly implement a playable version that can begin to address the project's chief uncertainties in a meaningful way. Can you create a paper version of your digital game? Can you design a short version of a game that will last much longer in its final form? Can you test the interaction pattern of a massively multiplayer game with just a handful of players?

In the iterative design process, the most detailed thinking you need at any moment is that which will get you to your next prototype. It is, of course, impor-

![](images/54e5865a4714278fcdd0de04ee2200d3d296df5295de9e275fe8e3ce393188de.jpg)

tant to understand the big picture as well—the larger conceptual, technical and design questions that drive the project as a whole. Just be sure not to let your design get ahead of your iterative research. Keep your eye on the prize, but leave room for play in your design, for the potential to change as you learn from your playtesting, accepting the fact that some of your assumptions will undoubtedly be wrong.

The project team continued to develop the paper prototype, seeking the balance between coop-

eration and competition that would become the heart of the final gameplay. We refined the base ruleset—the actions a player can take each turn and the outcomes that result. These rules were turned into a spec for the first digital prototype: a text-only version on IRC, which we played hotseat-style, taking turns sitting at the same computer. Constructing that early, text-only prototype allowed us to focus on the complexities of the game logic without worrying about implementing interactivity, visual and audio aesthetics, and other aspects of the game.

While we tested gameplay via the text-only iteration, programming for the final version began in Director, and the core game logic we had developed for the IRC prototype was recycled into the Director code with little alteration. Parallel to the game design, the project's visual designers had begun to develop the graphic language of the game and chart out possible screen layouts. These early drafts of the visuals (revised many times over the course of the entire development) were dropped into the Director version of the game, and the first roughhewn iteration of SiSSYFiGHT as a multiplayer online game took shape, inspired by

![](images/b7c3ff05ec8d138043fff840c76446f7aa4264b7d34f510a65705c97d580b726.jpg)  
Top and bottom: SiSSYFiGHT 2000 final version

Henry Darger's outsider art and retro game graphics.

As soon as the web version was playable, the development team played it. And as our ugly duckling grew more refined, the rest of the Word.com staff was roped into playing as well. As the game grew more stable, we descended on our friends' dotcom companies after the workday had ended, sitting them down cold in front of the game and letting them play. All of this testing and feedback helped us refine the game logic, aesthetics and interface. The biggest challenge turned out to be clearly articulating the relationship between player action and game outcome: because the results of each turn are interdependent on every player's action, early versions of the game felt frustratingly arbitrary. Only through many design revisions and dialogue with our testers did we manage to structure the results of each turn to communicate unambiguously what had happened that round and why.

When the server infrastructure was complet-

ed, we launched the game to an invitation-only beta-tester community that slowly grew in the weeks leading up to public release. Certain time slots were scheduled as official testing events, but our beta users could come online anytime and play. We made it very easy for the beta testers to contact us and email in bug reports.

Even with this smali sample of a few dozen participants, larger play patterns emerged. For example, as with many multiplayer games, it was highly advantageous to play defensively, leading to standstill matches. In response, we tweaked the game logic to discourage this play style: any player that "cowered" twice in a row was penalized for acting like a chicken! When the game did launch, our loyal beta testers became the core of the game community, easing new players into the game's social space.

In the case of SiSSYFiGHT 2000, the testing and prototyping cycle of iterative design was successful because at each stage, we clarified exactly what we wanted to test and how. We used written and online questionnaires. We debriefed after each testing session. And we strategized about how each version of the game would incorporate the aesthetic, game design, and technical elements of the previous versions, while also laying a foundation for the final form of the experience.

## Case Study 2: LOOP

Summary: LOOP is a singleplayer game in which the player uses the mouse to catch flittering, colored butterflies. The player draws loops around groups of butterflies of the same color, or of groups in which each butterfly is a different color (the more butterflies in a loop, the more points). To finish a level, the player must capture a certain number of butterflies before the sun sets. The game includes three species

![](images/e6e423164eefe53b62125fad4ed3d43ce8645fe7667830aa6e2af5597e821792.jpg)

![](images/53136f6ee746ff673c60bcaebee3576dd4240a0c724762ff3077b171aaae0aa8.jpg)  
Top and Bottom: LOOP early prototypes

of butterflies and a variety of hazardous bugs, all with different behaviors. LOOP was created by gameLab and is available for play at w.wi. 4o.hwwe. om

Initial prototypes are usually quite ugly. Game prototypes do not emphasize aesthetics or narrative content; they emphasize the game rules, which manifest as the internal logic of the game, tied to the player's interaction. Visuals, audio and story are important aspects of a game, but the core uncertainties of game design, the questions that a prototype should address, lie in the more fundamental elements of rules and play.

Another way of framing this problem is to ask, what is the activity of the game? Rather than asking what the game is about, ask what the player is actually doing from moment to moment as they play. Virtually all games have a core mechanic, an action or set of actions that players will repeat over and over as they move through the designed system of a game. The prototype should help you understand what this core mechanic is and how the activity becomes meaningful over time. Asking questions about your game's core mechanic can guide the creation of your first prototype, as well as successive iterations. Ideally, initial prototypes model this core mechanic and begin to test it through play.

LOOP grew out of a desire at gameLab to

invent a new core mechanic. There are ultimately not very many ways to interact with a computer game: the player can express herself through the mouse and keyboard, and the game can express itself through the screen and speakers. Deciding to intervene on the level of player input, we had a notion to cast aside point-andclick or click-and-drag mouse interaction in favor of sweeping, fluid gestures.

The first prototype tested only this core interaction, allowing the player to draw lines, but nothing else. Our next step was to have the program detect a closed loop and add objects that would shrink and disappear when caught in a loop.

Each of these prototypes had parameters adjustable by the person playing the game. The length of line and detail on the curve could be tweaked, as well as the number of objects, their speed and behavior, and several other variables. As we played the game, we could try out different parameters and immediately see how they affected the experience, adjusting the rules to arrive at a different sort of play. This programming approach of building accessible game design tools into

![](images/5ca99a54297acd49eb779a3fd3b0726d7b0eb8da7a70827eea837b91fb4c0771.jpg)

![](images/3c662857d5959c66d572611d7471368bda25550202a124f6fad9d8bab9d863b4.jpg)

a game prototype is a technical strategy that takes iterative design into account.

As the butterfly content of the game emerged, so did debate about the game's overall structure and victory and loss conditions. Did the entire screen need to be cleared of butterflies or did the player just have to catch a certain number of them? Did the butterflies gradually fill up the screen or did their number remain constant? Were there discrete levels or did the game just go on until the loss conditions were met? Was there some kind of time-pressure element? These fundamental questions, which grew out of our core mechanic prototyping, were only answered by actually trying out possibilities and coming to a conclusion through play.

As the game code solidified, the many adjustable parameters of the game were placed in a text file that was read into the application when it ran. These parameters controlled everything from the behavior of game creatures to points scored for different numbers of butterflies in a loop to the progression of the game's escalating difficulty. Thus the game designers could focus on refining game vari-

Top and Bottom: LOOP final version

ables and designing levels, while the rest of the program—screen transitions and help functionality, the high score system and integration with the host site—was under construction.

LOOP followed a testing pattern similar to that of SiSSYFiGHT, moving outward from the game creators to include a larger circle of players. During the development of LOOP, gameLab created the gameLab Rats, our official playtesting "club," to facilitate the process of testing and feedback. In the end, LOOP managed to achieve the fluid interaction we had first envisioned. An entire game evolved from a simple idea about mouse control. That is the power of iterative design.