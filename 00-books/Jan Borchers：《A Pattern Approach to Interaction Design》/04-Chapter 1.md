# Chapter 1

# Introduction

"Press Ctrl + Alt + Delete to log on."

—Microsoft Windows NT®opening screen.

## 1.1 Why User Interfaces Matter

Human-Computer Interaction, or HCI, deals with the interface between people and computer systems:

"In human-computer interaction knowledge of the capabilitiesand limitations ofthe human operator is used for the design of systems, software, tasks, tools, environments, and organizations. The purpose is generally to improve productivity while providing a safe, comfortable and satisfying experience for the operator."

[Helander et al., 1997, p. xi]

A working group of the Special Interest Group for Computer-Human Interaction (SIGCHI)ofthe Association for Computing Machinery(ACM) has published recommendations for a human-computer interaction curriculum [ACM SIGCHI, 1992]. Fig. 1.1 shows their graphical overview of the field, which conveys an idea of the scope of HCI in research and practice.

![](images/17fe7c8bffb91f57a7f8a9455ccdc27d85d0a9a6fa03222a48e225ced714c51e.jpg)  
Figure 1.1: The ACMSIGCHIHCI Design Curriculum [ACM SIGCHI, 1992].

There are numerous reasons why the quality of a user interface is critical to the success of an interactive system [Shneiderman, 1998, pp.16 ff.]:

• life-critical systems require rapid and error-free performance of the operator;

• office, home and entertainment applications require ease of learning, low error rates, and subjective satisfaction to compete in the marketplace;

• new exploratory,creative, and cooperative systems need to fulfil high user expectations,ideally by having the computer vanish;

• systems need to accommodate human diversityin terms of physical, cognitive, and perceptual abilities, cultural and personality differences, especially catering for elderly or disabled users.

Moreover, there is a strong businesscase for human factors: Attention to those factors, and a careful, iterative design of the user interface of a system, can reduce development time and cost, the need for updates, and improve the success of the product in the market [Klemmer, 1989, Chapanis, 1991, Landauer, 1995]. With the advent of the World-Wide Web, e-commerce, public information terminals and similar systems,the numberof first-time, one-timeusers increases, which makes careful user interface design even more critical to the success of such systems. For example, IBM recently gained a 400% increase in online sales (and an 84% decrease in help button usage) after redesigning their web site according to usability principles [Tedeschi, 1999].

Creating the user interface portion of an interactive system is no minor task. A survey by Myers and Rosson [1992] reported that, on the average, 45% of the design and 50% of theimplementation time for interactive applications were devoted to their user interface.

## 1.2 Interdisciplinary Design and Its Problems

It should be obvious that successful design of an interactive system requires people from various disciplines to work together in a team.

"GUIDELINE: The most successful designs result from a team approach where peoplewith differing backgrounds and strengths are equally empowered to affect the final design."

[Tognazzini, 1992, p. 57]

Key disciplines in this respect are software engineering, human interface design, and the application domain in which the system is going to be used. Other disciplines regularly involved include marketing, technical writing, graphic design, and others.

A studyby Jeffries et al. [1991]showed that human interface designers delivered the highest return on investment of any member in a software team, finding three to four times more problems in a software package within the same or shorter time than simultaneously conducted user tests, software engineers checking guidelines, and software engineers doing a cognitive walkthrough of the design.

To ensure that an interactive system solves problems that the intended users actually have, and that its interface uses the native terminology and concepts of the application domain, the design team must identify the prospective users and become familiar with their activities [Newman and Lamming, 1995, p. 91]. This "user-centred" approach to design [Norman and Draper, 1986]may involve consultation of experts of the application domain, or actual prospective users,to acquire this knowledge. This user involvement is usually essentially a one-way communication in which the designers extract information from users by means of surveys, questionnaires, interviews, and user tests.

A more active participation of users throughout the design process is suggested by the schoolof participatory design. There is no single, encompassing definition of this approach, but its central goal is that “.. . the ultimate users of the software make effective contributionsthat reflect their own perspectives and needs, somewhere in the design and development lifecycle of the software." [Muller et al., 1997, p. 258]. This recent article also gives an excellent overview of participatory design practice; for a more detailed treatment of the subject, see, for example, Schuler and Namioka [1997].

A major problem of interdisciplinary design is effective communication. Users do not understand the technical jargon ofsoftware engineers or human factors people. Similarly, the design professionals initially usually have only a vague knowledge of the concepts, methods, and terminology of the application domain,andthey have difficulties understanding them when users explain these issues to them.

As Kim [1990] points out, disciplines are like cultures: to work together, they must learn to appreciate one another's language, traditions, and values. However, people within a discipline often have troublecommunicating what they knowto outsiders. This is especially problematic for user interface, design because to succeed, it requires many disciplines to cooperate as outlined above: HCI needs to communicate.

If this communication fails, the result is that the methods, paradigms, and ultimately the values of each profession are not understood, and consequently cannot be respected, by the other disciplines. Any method that simplifies this mutual understanding would benefit the design process, and the resulting product.

## 1.3Capturing Experience

Another important goal of any design team is to capture the reasons for design decisions, and the experience from past projects, to create a corporate memory of design knowledge.

Such a repository can have many benefits:

• It helps avoid repeating errors of previous projects;

• it can introduce new team members to a project;

• and it can be used for training and education of newcomers to the field.

Therefore, it has a strong business case, as leaving employees otherwise often take most of the memoryand experience from their projects with them, and the enterprise cannot refer to that knowledge anymore to handle similar problems in subsequent projects more efficiently.

A common approach to expressing such experience is in the form of design guidelines. However, they usually fall into one of the following two categories:

• Abstract guidelines, such as the four design process principles by Gould et al. [1997] or the Eight Golden Rules of Interface Design by Shneiderman [1998, p. 74], are valuable in principle, and they can be applied easily to judge a design a posteriori. It is usually easy to pin down a bad design to the breach of one or several of those rules. However, these guidelines do not suggest constructively how to solve a design problem when the designer is faced with it. They also do not create a vocabulary of applicable solutions, and therefore do not solve the"language" problem.

• Concrete guidelines, such as the Macintosh Human Interface Guidelines [Apple Computer, 1992] or the OSF/Motif Style Guide [Open Software Foundation, 1992], are too much tailored to the use of a certain set or toolkit of user interface objects. This renders them obsolete relatively quickly,unless the designer takes upthe extra work of tryingto extract the "timeless" qualities from those specific guidelines.

Even the comprehensive analysis of the field of participatory design [Muller et al., 1997] does not list any methods geared towards capturing general design experience, or design lessons learned during a project.

## 1.4 A Pattern Framework

To solve the problems outlined above, this book suggests a unified framework to express design experience. It is especially suited to HCI, but also to software engineering, and to the application domain of a project.

The underlyingmodel is formally structured in a hypertext graph notation, to conveya clear understanding of the structure, and to simplify computer support for handling complete instantiations of this framework.However, since the format is intended to support cooperation within the design team, humanreadabilityremains paramount and was not sacrificed for formalism.

The framework is based on the idea of languages of design patterns. Put simply, a design pattern is a structured textual andgraphical description of a proven solution to a recurring design problem. A pattern language is a hierarchy of design patterns ordered by their scope. High-level patterns address large-scale design issues and reference lower-level patterns to describe their solution.

The concept originatedin urban architecture [Alexander et al.,1977, Alexander,1979], but has been adapted quite successfully to software engineering, although some of its basic aspects were lost in the process (see chapter 2).

This book extends the notion of pattern languages to two newfields: Firstly, to the discipline of Human-Computer Interaction. Here, design patterns are shown to be a very suitable tool to capture user interface design experience.

Secondly, and an entirely new concept, the pattern language approach is carried over to the application domain of the project. Concepts from the discipline in which the software will be used are also expressed as design patterns ordered into a pattern language.

The pattern frameworkhas been used in a series of design projects dealingwith interactive exhibits. Pattern languagesfrom the software engineering, HCI,andapplication domains of those projects are presented in this book, as well as the design of a sample authoring and browsing tool to work with pattern languages.

## 1.5 How This Book Is Organized

## The rest of this work is organized as follows:

Chapter2 gives an overview of the history of pattern languages in architecture and software engineering, summarizes the state of the art of pattern languages in HCI, and gives requirements for a pattern-based approach to interaction design.

Chapter3 introduces the central idea of this text, the interdisciplinary patternlanguage framework to capture and express design experience inHCI,software engineering, and the project's application domain. It gives a formal hypertext model of design patterns and pattern languages, embeds it into an established usability engineering lifecycle model, anddiscusses how this frameworkcan be used to support design, training, and education in interactive systems design.

Example Chapter 4 presents an example of this framework, drawn from the author's project experience. It includes a pattern language about HCI design forinteractive exhibits drawn from a series of such projects, a pattern language about music as used in the WorldBeat exhibit, and several software engineering patterns drawn from those interactive music systems. The HCI pattern language presented here applies to a wide range of scenarios, such as designing public interactive multimedia kiosks and similar systems.

Chapter 5 evaluates the framework proposed. It compares it with the initial set ofrequirements, shows results of a peer review of a typical pattern from one of the languages, examines the design and success of resulting pattern-based systems such as the WorldBeat exhibit, and evaluates the use of the framework in subsequent projects and in education. It also presents the design of PET, a Pattern Editing Tool to write, review, and use pattern languages.

Chapter 6 summarizes the main contributions of this work, and concludes with directions for further research.

After the bibliography, appendix A lists online references made inthe text. Appendix Bshowsasample run of the WorldBeat exhibit that is frequently referred to throughout the text. Finally, a List of Figures andCredits lists the images used in the book and their sources, and the Index contains important terms with pointers to relevant pages in the text.