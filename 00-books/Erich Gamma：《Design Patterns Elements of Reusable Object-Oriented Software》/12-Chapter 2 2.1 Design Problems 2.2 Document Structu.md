## Chapter 2

## A Case Study: Designing a Document Editor

This chapter presents a case study in the design of a ��What-You-See-Is-What-You-Get” (or “WYSIWYG”) document editor called Lexi.<sup>1</sup> We’ll see how design patterns capture solutions to design problems in Lexi and applications like it. By the end of this chapter you will have gained experience with eight patterns, learning them by example.

Figure 2.1 depicts Lexi’s user interface. A WYSIWYG representation of the document occupies the large rectangular area in the center. The document can mix text and graphics freely in a variety of formatting styles. Surrounding the document are the usual pull-down menus and scroll bars, plus a collection of page icons for jumping to a particular page in the document.

## Figure 2.1: Lexi’s user interface

![](images/a91334fad7caeaaa0f9f6dc43a118627f4f4ea9bcfb6aed279fdf41b5cade3bd.jpg)

## 2.1 Design Problems

We will examine seven problems in Lexi’s design:

1. Document structure. The choice of internal representation for the document affects nearly every aspect of Lexi’s design. All editing, formatting, displaying, and textual analysis will require traversing the representation. The way we organize this information will impact the design of the rest of the application.

2. Formatting. How does Lexi actually arrange text and graphics into lines and columns? What objects are responsible for carrying out different formatting policies? How do these policies interact with the document’s internal representation?

3 . Embellishing the user interface. Lexi’s user interface includes scroll bars, borders, and drop shadows that embellish the WYSIWYG document interface. Such embellishments are likely to change as Lexi’s user interface evolves. Hence it’s important to be able to add and remove embellishments easily without affecting the rest of the application.

4 . Supporting multiple look-and-feel standards. Lexi should adapt easily to different look-and-feel standards such as Motif and Presentation Manager (PM) without major modification.

5 . Supporting multiple window systems. Different look-and-feel standards are usually implemented on different window systems. Lexi’s design should be as independent of the window system as possible.

6. User operations. Users control Lexi through various user interfaces, including buttons and pull-down menus. The functionality behind these interfaces is scattered throughout the objects in the application. The challenge here is to provide a uniform mechanism both for accessing this scattered functionality and for undoing its effects.

7 . Spelling checking and hyphenation. How does Lexi support analytical operations such as checking for misspelled words and determining hyphenation points? How can we minimize the number of classes we have to modify to add a new analytical operation?

We discuss these design problems in the sections that follow. Each problem has an associated set of goals plus constraints on how we achieve those goals. We explain the goals and constraints in detail before proposing a specific solution. The problem and its solution will illustrate one or more design patterns. The discussion for each problem will culminate in a brief introduction to the relevant patterns.

## 2.2 Document Structure

A document is ultimately just an arrangement of basic graphical elements such as characters, lines, polygons, and other shapes. These elements capture the total information content of the document. Yet an author often views these elements not in graphical terms but in terms of the document’s physical structure—lines, columns, figures, tables, and other substructures.<sup>2</sup> In turn, these substructures have substructures of their own, and so on.

Lexi’s user interface should let users manipulate these substructures directly. For example, a user should be able to treat a diagram as a unit rather than as a collection of individual graphical primitives. The user should be able to refer to a table as a whole, not as an unstructured mass of text and graphics. That helps make the interface simple and intuitive. To give Lexi’s implementation similar qualities, we’ll choose an internal representation that matches the document’s physical structure.

In particular, the internal representation should support the following:

• Maintaining the document’s physical structure, that is, the arrangement of text and graphics into lines, columns, tables, etc.

• Generating and presenting the document visually.

• Mapping positions on the display to elements in the internal representation. This lets Lexi determine what the user is referring to when he points to something in the visual representation.

In addition to these goals are some constraints. First, we should treat text and graphics uniformly. The application’s interface lets the user embed text within graphics freely and vice versa. We should avoid treating graphics as a special case of text or text as a special case of graphics; otherwise we’ll end up with redundant formatting and manipulation mechanisms. One set of mechanisms should suffice for both text and graphics.

Second, our implementation shouldn’t have to distinguish between single elements and groups of elements in the internal representation. Lexi should be able to treat simple and complex elements uniformly, thereby allowing arbitrarily complex documents. The tenth element in line five of column two, for instance, could be a single character or an intricate diagram with many subelements. As long as we know this element can draw itself and specify its dimensions, its complexity has no bearing on how and where it should appear on the page.

Opposing the second constraint, however, is the need to analyze the text for such things as spelling errors and potential hyphenation points. Often we don’t care whether the element of a line is a simple or complex object. But sometimes an analysis depends on the objects being analyzed. It makes little sense, for example, to check the spelling of a polygon or to hyphenate it. The internal representation’s design should take this and other potentially conflicting constraints into account.

## Recursive Composition

A common way to represent hierarchically structured information is through a technique called recursive composition, which entails building increasingly complex elements out of simpler ones. Recursive composition gives us a way to compose a document out of simple graphical elements. As a first step, we can tile a set of characters and graphics from left to right to form a line in the document. Then multiple lines can be arranged to form a column, multiple columns can form a page, and so on (see Figure 2.2).

Figure 2.2: Recursive composition of text and graphics

![](images/aa2426d33c565c78c346297fffd8750e15e419c2a75b89f9228afc219f8072d3.jpg)  
We can represent this physical structure by devoting an object to each important element. That includes not just the visible elements like the characters and graphics but the invisible, structural elements as well—the lines and the column. The result is the object structure shown in Figure 2.3.

Figure 2.3: Object structure for recursive composition of text and graphics  
![](images/474ccce8228030d3807a5dadf54b43ade2224e292f4dc1d570af6a3525604311.jpg)  
By using an object for each character and graphical element in the document, we promote flexibility at the finest levels of Lexi’s design. We can treat text and graphics uniformly with respect to how they are drawn, formatted, and embedded within each other. We can extend Lexi to support new character sets without disturbing other functionality. Lexi’s object structure mimics the document’s physical structure.