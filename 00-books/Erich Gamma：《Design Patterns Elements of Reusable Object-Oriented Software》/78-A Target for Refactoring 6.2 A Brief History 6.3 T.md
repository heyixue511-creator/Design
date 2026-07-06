Object-oriented design methods are supposed to promote good design, to teach new designers how to design well, and to standardize the way designs are developed. A design method typically defines a set of notations (usually graphical) for modeling various aspects of a design, along with a set of rules that govern how and when to use each notation. Design methods usually describe problems that occur in a design, how to resolve them, and how to evaluate design. But they haven’t been able to capture the experience of expert designers.

We believe our design patterns are an important piece that’s been missing from object-oriented design methods. The design patterns show how to use primitive techniques such as objects, inheritance, and polymorphism. They show how to parameterize a system with an algorithm, a behavior, a state, or the kind of objects it’s supposed to create. Design patterns provide a way to describe more of the “why” of a design and not just record the results of your decisions. The Applicability, Consequences, and Implementation sections of the design patterns help guide you in the decisions you have to make.

Design patterns are especially useful in turning an analysis model into an implementation model. Despite many claims that promise a smooth transition from objectoriented analysis to design, in practice the transition is anything but smooth. A flexible and reusable design will contain objects that aren’t in the analysis model. The programming language and class libraries you use affect the design. Analysis models often must be redesigned to make them reusable. Many of the design patterns in the catalog address these issues, which is why we call them design patterns.

A full-fledged design method requires more kinds of patterns than just design patterns. There can also be analysis patterns, user interface design patterns, or performance-tuning patterns. But the design patterns are an essential part, one that’s been missing until now.

## A Target for Refactoring

One of the problems in developing reusable software is that it often has to be reorganized or refactored [OJ90]. Design patterns help you determine how to reorganize a design, and they can reduce the amount of refactoring you need to do later.

The lifecycle of object-oriented software has several phases. Brian Foote identifies these phases as the prototyping, expansionary, and consolidating phases [Foo92].

The prototyping phase is a flurry of activity as the software is brought to life through rapid prototyping and incremental changes, until it meets an initial set of requirements and reaches adolescence. At this point, the software usually consists of class hierarchies that closely reflect entities in the initial problem domain. The main kind of reuse is white-box reuse by inheritance.

Once the software has reached adolescence and is put into service, its evolution is governed by two conflicting needs: (1) the software must satisfy more requirements, and (2) the software must be more reusable. New requirements usually add new classes and operations and perhaps whole class hierarchies. The software goes through an expansionary phase to meet new requirements. This can’t continue for long, however. Eventually the software will become too inflexible and arthritic for further change. The class hierarchies will no longer match any problem domain. Instead they’ll reflect many problem domains, and classes will define many unrelated operations and instance variables.

To continue to evolve, the software must be reorganized in a process known as refactoring. This is the phase in which frameworks often emerge. Refactoring involves tearing apart classes into special- and general-purpose components, moving operations up or down the class hierarchy, and rationalizing the interfaces of classes. This consolidation phase produces many new kinds of objects, often by decomposing existing objects and using object composition instead of inheritance. Hence black-box reuse replaces white-box reuse. The continual need to satisfy more requirements along with the need for more reuse propels object-oriented software through repeated phases of expansion and consolidation—expansion as new requirements are satisfied, and consolidation as the software becomes more general.

![](images/2663a52ef504f34cbd3c0fd1debb0f12df6bba7353ebc4d841a59f6566bcda97.jpg)

This cycle is unavoidable. But good designers are aware of the changes that can prompt refactorings. Good designers also know class and object structures that can help avoid refactorings—their designs are robust in the face of requirement changes. A thorough requirements analysis will highlight those requirements that are likely to change during the life of the software, and a good design will be robust to them.

Our design patterns capture many of the structures that result from refactoring. Using these patterns early in the life of a design prevents later refactorings. But even if you don’t see how to apply a pattern until after you’ve built your system, the pattern can still show you how to change it. Design patterns thus provide targets for your refactorings.

## 6.2 A Brief History

The catalog began as a part of Erich’s Ph.D. thesis [Gam91, Gam92]. Roughly half of the current patterns were in his thesis. By OOPSLA ’91 it was officially an independent catalog, and Richard had joined Erich to work on it. John started working on it soon thereafter. By OOPSLA ’92, Ralph had joined the group. We worked hard to make the catalog fit for publication at ECOOP ’93, but soon we realized that a 90-page paper was not going to be accepted. So we summarized the catalog and submitted the summary, which was accepted. We decided to turn the catalog into a book shortly thereafter.

Our names for the patterns have changed a little along the way. “Wrapper” became “Decorator,” “Glue” became “Facade,” “Solitaire” became “Singleton,” and “Walker” became “Visitor.” A couple of patterns got dropped because they didn’t seem important enough. But otherwise the set of patterns in the catalog has changed little since the end of 1992. The patterns themselves, however, have evolved tremendously.

In fact, noticing that something is a pattern is the easy part. All four of us are actively working on building object-oriented systems, and we’ve found that it’s easy to spot patterns when you look at enough systems. But finding patterns is much easier than describing them.

If you build systems and then reflect on what you build, you will see patterns in what you do. But it’s hard to describe patterns so that people who don’t know them will understand them and realize why they are important. Experts immediately recognized the value of the catalog in its early stages. But the only ones who could understand the patterns were those who had already used them.

Since one of the main purposes of the book was to teach object-oriented design to new designers, we knew we had to improve the catalog. We expanded the average size of a pattern from less than 2 to more than 10 pages by including a detailed motivating example and sample code. We also started examining the trade-offs and the various ways of implementing the pattern. This made the patterns easier to learn.

Another important change over the past year has been a greater emphasis on the problem that a pattern solves. It’s easiest to see a pattern as a solution, as a technique that can be adapted and reused. It’s harder to see when it is appropriate—to characterize the problems it solves and the context in which it’s the best solution. In general, it’s easier to see what someone is doing than to know why, and the “why” for a pattern is the problem it solves. Knowing the purpose of a pattern is important too, because it helps us choose patterns to apply. It also helps us understand the design of existing systems. A pattern author must determine and characterize the problem that the pattern solves, even if you have to do it after you’ve discovered its solution.

## 6.3 The Pattern Community

We aren’t the only ones interested in writing books that catalog the patterns experts use. We are a part of a larger community interested in patterns in general and softwarerelated patterns in particular. Christopher Alexander is the architect who first studied patterns in buildings and communities and developed a “pattern language” for generating them. His work has inspired us time and again. So it’s fitting and worthwhile to compare our work to his. Then we’ll look at others’ work in software-related patterns.

## Alexander’s Pattern Languages

There are many ways in which our work is like Alexander’s. Both are based on observing existing systems and looking for patterns in them. Both have templates for describing patterns (although our templates are quite different). Both rely on natural language and lots of examples to describe patterns rather than formal languages, and both give rationales for each pattern.

But there are just as many ways in which our works are different:

1. People have been making buildings for thousands of years, and there are many classic examples to draw upon. We have been making software systems for a relatively short time, and few are considered classics.

2. Alexander gives an order in which his patterns should be used; we have not.

3 . Alexander’s patterns emphasize the problems they address, whereas design patterns describe the solutions in more detail.

4 . Alexander claims his patterns will generate complete buildings. We do not claim that our patterns will generate complete programs.

When Alexander claims you can design a house simply by applying his patterns one after another, he has goals similar to those of object-oriented design methodologists who give step-by-step rules for design. Alexander doesn’t deny the need for creativity; some of his patterns require understanding the living habits of the people who will use the building, and his belief in the “poetry” of design implies a level of expertise beyond the pattern language itself.<sup>1</sup> But his description of how patterns generate designs implies that a pattern language can make the design process deterministic and repeatable.

The Alexandrian point of view has helped us focus on design trade-offs—the different “forces” that help shape a design. His influence made us work harder to understand the applicability and consequences of our patterns. It also kept us from worrying about defining a formal representation of patterns. Although such a representation might make automating patterns possible, at this stage it’s more important to explore the space of