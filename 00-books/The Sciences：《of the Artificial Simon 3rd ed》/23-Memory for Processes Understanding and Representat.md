It is probably safe to say that the chemist must know as much as a diligent person can learn in about a decade of study.

## Memory for Processes

Memory has been discussed here as though it consisted mainly of a body of data. But experts possess skills as well as knowledge. They acquire not only the ability to recognize situations or to provide information about them; they also acquire powerful special skills for dealing with situations as they encounter them. Physicians prescribe and operate as well as diagnose.

The boundary between knowledge and skill is subtle. For example, when we write a computer program in any language except machine language, we are really not writing down processes but data structures. These data structures are then interpreted or compiled into processes that is, into machine-language instructions that the computer can understand and execute. Nevertheless for most purposes it is convenient for us simply to ignore the translation step and to treat the computer programs in higher-level languages as representing processes.

We can think of a medical diagnostic system (human or computer) as having a large body of medical knowledge, together with a few general processes for drawing inferences from it. Or we can think of the knowledge as organized in processes, instructing the expert how to proceed with the diagnosis, for example:

If you find that the patient has a high fever, then test for the following additional symptoms.

Similarly, a student's knowledge of geometry could be stored as theorems:

If two triangles have the three pairs of corresponding sides equal, then they are congruent.

or, alternatively, as condition-action pairs (called productions):

Test the corresponding sides of two triangles for pairwise equality; if all are equal, store the assertion that the triangles are congruent.

Whether expertness is stored as data or process, or some combination of both, does not alter what we have said about complexity. The

specialized knowledge and skill can still be regarded as residing in the external environment of long-term memory, to be drawn upon by general processes that control and steer problem-solving search processes like means-ends analysis and recognition that we have already identified in the simpler task environments discussed in chapter 3.

## Understanding and Representation

Efforts to solve a problem must be preceded by efforts to understand it. Here is an example of a puzzle-like task that most people find reasonably difficult:

## A Tea Ceremony

In the inns of certain Himalayan villages is practiced a most civilized and refined tea ceremony. The ceremony involves a host and exactly two guests, neither more nor less. When his guests have arrived and have seated themselves at his table, the host performs five services for them. These services are listed below in the (increasing) order of the nobility which the Himalayans attribute to them.

Stoking the Fire

Fanning the Flames

Passing the Rice Cakes

Pouring the Tea

Reciting Poetry

During the ceremony, any of those present may ask another, "Honored Sir, may I perform this onerous task for you?" However, a person may request of another only the least noble of the tasks the other is performing. Further, if a person is performing any tasks, then he may not request a task which is nobler than the least noble task he is already performing. Custom requires that by the time the tea ceremony is over, all the tasks will have been transmitted from the host to the most senior of the guests. How may this be accomplished?

Before a General Problem Solver (see chapter 5) can go to work on the Tea Ceremony problem, it has to extract from the written statement a description of the problem in terms of constructs that a GPS can deal with: symbol structures, tests for differences between structures, operators that alter structures, and symbolized goals and tests for their achievement. A GPS understands a problem when the problem has been presented to it in terms of such entities, so that its processes for detecting differences, finding relevant operators, applying operators, and evaluating progress toward the solution can go into action.

Now the Tea Ceremony problem really has nothing to do with inns in Himalayan villages. Underneath it is an abstract problem about two classes of objects (participants and tasks), relations between objects (each task is assigned to a participant), an ordering of the tasks (by nobility), and operators (transferring a task from one participant to another). Understanding the problem requires extracting these entities from the natural language text.

## A Program That Understands

A computer program, UNDERSTAND, simulates the processes that people use to generate an internal representation of (to understand) a problem like A Tea Ceremony.<sup>8</sup> UNDERSTAND proceeds in two phases: it parses the sentences of the problem instructions, and then constructs the representation from the information it has extracted from the parsed sentences.

The task of analysing natural-language sentences has already been discussed in the last chapter: it involves inferring from the linear string of words the implied hierarchic structure of phrases and clauses. The UNDERSTAND program accomplishes this in a quite orthodox way, similar to that of other extant parsing programs. The second phase (construction) is more interesting. Here, the parsed sentences are examined to discover what objects and sets of objects are being referred to, what properties of objects are mentioned and what are the relations among them, which of the predicates and relations describe states and which describe moves, and what the goal state is. UNDERSTAND then proceeds to construct a format for representing states and to generate programs for making legal moves by changing one state into another.

For example, in A Tea Ceremony a state could be represented by a list of the three participants, each described by a list of the tasks he is performing. Another list could indicate the ordering of the five tasks by nobility. The legal move program would delete a task from the list of a particular participant (the donor) and add it to the list of another (the

donee), after checking to see that the task was not more noble than others on the donor's or donee's lists.

Since (as was argued in the last chapter) list structures have a quite general capacity for representing symbolic information of all kinds, a program like UNDERSTAND is capable, in principle, of constructing a representation for virtually any kind of puzzle like problem that does not require real-world knowledge for its understanding; for any such problem can be described in terms of objects, their relations, and changes in their relations.

## Understanding Physics

In contrast with understanding a problem like A Tea Ceremony, understanding problems in domains that have rich semantics requires prior knowledge of the domain. Consider the simple statics problem:

The foot of a ladder rests against a vertical wall and on a horizontal floor. The top of the ladder is supported from the wall by a horizontal rope 30 ft long. The ladder is 50 ft long, weighs 100 lb with its center of gravity 20 ft from the foot, and a 150-lb man is 10 ft from the top.

Determine the tension in the rope.

In order to go to work on this problem, a person must know what a coefficient of friction is, that a ladder may be regarded as a lever with a fulcrum and with forces applied to it, that a man may be abstracted to a mass or a fulcrum, and many facts of a similar sort. What distinguishes this kind of problem from A Tea Ceremony is not that it has real-world reference, but that it makes reference to matters that are supposed already to be known.

Gordon Novak has written a very interesting program, ISAAC, that can understand physics (statics) problems like the one described above.<sup>10</sup> ISAAC is able to do this because it has stored in memory information about levers, masses, inclined planes, and the like in the form of simple schemas that describe objects of these kinds and that indicate the kinds of

information associated with them. A ladder schema, for example, looks something like this:

Ladder

Type: ladder

Locations: (of foot, top, other points mentioned)

Supports:

Length:

Weight:

Attachments: (to other objects)

When a problem is presented to ISAAC, it begins, like UNDERSTAND, to parse the sentences of the problem statement. In ISAAC's case, however, more is involved than identifying objects and relations and representing them appropriately. Particular kinds of objects whose meanings are already known (i.e., provided with schemas in ISAAC's memory) must be recognized and identified with their schemas, and the "slots" in the schemas must be filled in with the requisite information. A ladder must be recognized as a lever, and a copy must be constructed of the lever schema specifying the length of the ladder, its weight, its center of gravity, the location of its fulcrum and of the forces impinging on it, and so on.

Having identified the appropriate object schemas and accumulated the appropriate information about them, ISAAC is then able to assemble the individual schemas (describing the ladder, the man, the surfaces on which the ladder rests) into a composite problem schema. Using the latter schema as guide, the program then constructs and solves the equations that are appropriate for describing the equilibria of forces.

ISAAC is prototypic of systems for understanding problems in semantically rich domains. Knowledge of physics is stored in the program in two ways: in the component schemas, which guide the process of generating a representation of the problem state (the problem schema), and in the procedures for generating the equations of equilibrium (the laws of statics which correspond to the processes for creating the operators in a program like UNDERSTAND).

When we compare the two understanding programs, we see that UNDERSTAND has to create its problem representation and operators out of whole cloth, guided only by the information in the problem