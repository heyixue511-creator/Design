## Production Systems

In an information-processing system that consists of data structures and programs, it has usually been easier to devise methods for adding new schemas and other data structures to the existing system than to add new programs. In the early years of AI research, artificial intelligence and simulation programs were usually organized as hierarchies of routines and subroutines. Modification of a program involved modification of one or more subroutines, a task not easily accomplished.

In the past several decades a new form of program structure has become popular: the production system.<sup>12</sup> What commends it, especially for building systems that learn, is the simplicity and uniformity of its structure. A production system is a set of arbitrarily many productions. Each production is a process that consists of two parts a set of tests or conditions and a set of actions. The actions contained in a production are executed whenever the conditions of that production are satisfied. In that sense, the productions operate in complete independence of each other. Productions are usually represented by the notation:

## Condition  Action,

which is reminiscent of the familiar SR pairs of stimulus-response psychology. Although productions are more complex objects than SR pairs, it is sometimes possible to use the latter as a metaphor for the former.

A system to simulate human cognition might be constructed with productions of two kinds: those in which the conditions are tests on the contents of short-term memory and those in which the conditions are perceptual tests on the outside world. An example of a condition of the former kind might be: "If your goal is to enter the house, open the door." Here, the goal of entering the house would be represented by a symbol structure in STM, and STM would be tested for the presence or absence of that structure.

An example of a perceptual production might be: "If the door is locked, use your key." Here the condition is tested in the real world (by determining if the door is locked).

<sup>12.</sup> See Newell and Simon, Human Problem Solving.

A system whose behavior is governed by perceptual productions is sometimes called stimulus driven or data driven; one governed by goal symbols in STM, goal driven. A problem solver that is mainly goal driven will give the appearance of working backward from the desired goal. One that is mainly stimulus driven will give the appearance of working forward from what it knows toward the desired goal. Of course goal-directed systems will usually employ both productions with perceptual conditions and productions with goals as conditions.

Many cognitive simulations have now been modeled as production systems. But what makes production systems especially attractive for modeling is that it is relatively easy to endow them with learning capabilities to build so-called adaptive production systems. Since production systems are simply sets of productions, they can be modified by deleting productions or by inserting new ones. The consequences of such changes may or may not be adaptive, but at least there is no question of how the change is to be made.

## Learning from Examples

In chapters of science and mathematics textbooks that explain new procedures, one almost always finds examples that have been worked out in detail, step by step. In an elementary algebra text, for example, we might find the following:

$$
9 X + 1 7 = 6 X + 2 3 ,
$$

3X + 17 = 23 (subtract 6X from both sides),

3X = 6 (subtract 17 from both sides),

X = 2 (divide both sides by 3).

At each step the algebraic equation is modified and a "justification" given for the modification. The process terminates when an expression is found of the form:

<Variable> = <Numeral>

This, and similar, equations could be solved by the following production system:

If expression has the form, <variable> = <real number>  Halt.

If expression has variable term on right side  Subtract variable term from both sides, and simplify.

If expression has numerical term on left side  Subtract numerical term from both sides, and simplify.

If variable term has coefficient other than unity  Divide both sides by coefficient.

Now a clever student who encountered the worked-out example in the text, but who had not previously acquired a procedure for solving it, could learn one in the following manner. Examining the first two steps in the example, he notices what action has been performed to transform the first line into the second. He also compares the pairs of equations and notices that the term "6X" has disappeared from the right side and the coefficient of X has been changed on the left. By trying the action, he discovers that it produces exactly this effect. Moreover the expression from which the "6X" has been removed is closer in form to the final equation than is the initial expression. He now learns a new production, by taking the feature of the initial expression that is eliminated as the condition for the action. This production is the second one in our production system. By comparing the second and third equations, he similarly infers and acquires the third production, and by comparing the third and fourth equations, the fourth production. Presumably he has already acquired the first production, which represents his understanding of what the ''solution" of an algebraic equation is.

I have omitted from this account some essential details, such as how the student selects the proper degree of generalization for his productions (why "variable term" instead of "6X" in the condition and action of the second production?). But the simplified example conveys the general idea of how an adaptive production system can acquire new skills. This particular scheme has been devised and programmed by David Neves.<sup>13</sup>

A set of highly effective computer tutoring systems in geometry, algebra, and programming (LISP), employing primarily a learning-from-examples paradigm, has been developed by John Anderson and his colleagues and tested successfully in high school classrooms. In the People's Republic of China, the Psychology Institute of the Chinese Acad-

emy of Sciences has developed paper and pencil materials for a full three-year middle school curriculum in algebra and geometry based upon learning from examples rather than lectures or textbook exposition. These materials are now being used successfully in several hundred schools in China. In both cases, the materials were developed by analyzing the tasks to determine what productions the students would need to acquire for effective performance and then what sequence of examples would induce the learning of these productions. These two extensive projects, in the U.S. and China, provide strong evidence for the relevance to human learning of the processes that Neves and others postulated on the basis of computer simulation.<sup>14</sup>

The idea of learning from examples can be extended to a method of learning "by doing." Suppose a problem-solving system is able to solve a particular problem but does it inefficiently after a great deal of search. The path to a solution finally discovered, stripped of all the extraneous branchings in the search, could serve as a worked-out example to which the procedures of the previous paragraphs could be applied. Anzai and Simon have constructed a "learning by doing" scheme of this kind for the Tower of Hanoi puzzle which, by solving the problem several times in succession, gradually acquires an efficient and general strategy.<sup>15</sup>

## Discovery Processes

No sharp line divides learning things that are already known to others from learning things that are new to the world. What constitutes novelty depends on what knowledge is already in the mind of the problem solver and what help is received from the environment in adding to this knowledge. We should expect, therefore, that processes very similar to those employed in learning systems can be used to construct systems that discover new knowledge.

<sup>14.</sup> J. R. Anderson, A. T. Corbett, K. R. Koedinger and R. Pelletier, "Cognitive Tutors: Lessons Learned," Journal of the Learning Sciences, 4(1995):167 207; X. Zhu and H. A. Simon, "Learning Mathematics from Examples and by Doing," Cognition and Instruction, 4(1987):137 166.