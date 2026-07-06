# Summary and Further Research

"Mit Eifer hab' ich mich der Studien beflissen; Zwar weiß ich viel, doch möcht' ich alles wissen.

—J.W. von Goethe: Faust

This chapter will briefly sketch the motivation for this work, and then summarize its main original contributions to the research field of HCI design patterns.

## 6.1 Motivation

The quality of a user interface is crucial to the success of interactive systems. Good user interface design, however, requiresexperts fromhuman-computer interaction,software engineering, and the application domain of a software project to collaborate in an interdisciplinary design team. Communicationbetween thesedisciplinesis oftendifficult, as is capturing their design experience forfollow-up projects, corporate memory, trainingand education. This work has suggesteda new pattern-basedframework for tackling these problems.

## 6.2 Main Contributions

To this end, the first contribution of this work is a comprehensive introduction to the concept of patterns as introduced in the 1970s by the architect Christopher Alexander, who defined pattern languages as hierarchies of textual descriptions of successful solutions to recurring design problems in urban architecture.

This is followed by an overview of how the idea has been adopted by software engineering, and an exhaustive survey of the history and state of the art in the field of design patterns in human-computer interaction. It includes interesting findings on early references to Alexander's work by major HCItexts that previously have generally been overlooked, and outlines the results of all known workshops, as well as most individual efforts, on the subject that have begun to evolve since the HCI pattern movement has gained momentum around 1997.

The author has also actively participated in, and to some degree organized, the discussion and definition process in the still relatively small, but very active and now quickly growing, HCI patterns research community. He was a member of the first workshop on interaction patterns held at a conference from the PLoP (Pattern Languages of Programming) series at ChiliPLoP 1999, connecting as an HCI researcher to people from the software engineering patterns community,and authored the resultingreport [Borchers, 2000a].

The next two pattern workshops at major HCI conferences, INTERACT'99 and CHI 2000, were co-organized by the author. The latter event in particular includedvirtually all individuals who had been doing major research in the HCI patterns field. These workshops and their reports have led to an increased visibility of this field within HCI and software engineering,and iteratively improved basic concepts such as a definition of HCI pattern languages, their goals, structure, and contents. These contributions are reflected in this work, although they were mostly included in the survey section for sake of clarity.

Another significant contribution of this work is the formal specification of the structure of a pattern language, which is independent of the domainthat the language may address. The definition is refined by adetailed discussion of the meaning of the individualpattern constituents and their composition. It should be kept in mindat this point that these "languages" are not programming languages, but rather hierarchies of patterns, which aretextual descriptions of successful design solutions.

The definition has been used to apply the pattern concept not only to HCI, but also to software engineering and particularly the application domain of software projects. While there is a large body of work available about software patterns,applying the principle to the application domain of an interactivesoftware design process has only been undertaken by few research projects.

In particular, the present work is the first to suggest a crossdisciplinary method to use patterns in the design process of interactive systems in a structured and uniformway.The method is embedded into a widely known model of usability engineering, making it more practical for application.

The languages contained in this book not only serve as proof of the soundness of the pattern-based approach, but also stand as original contributions in their own right. The HCI pattern language is the most comprehensive, and captures crucial design help for the growing field of interactive exhibits. It is important to see that with the advent of public information kiosks, more playful desktop software, and the World-Wide Web, the need for exhibit-like design primarily for first-time and one-time users with short interaction times has spread far beyond the obvious museum scenario.

The musical pattern language illustrates how to capture knowledge from the application domain of a project, but also represents the first time such knowledge has been gathered, structured, and presented in this format.

The software design patterns capture some of the techniques used by the author in building interactive music systems.

To illustrate the feasibility of computer tool support for working with pattern languages, the Pattern EditingTool PET, a prototypical software environment, was designed, based on an initial analysis of target groups, their tasks, and typical usage scenarios.

Finally, many of the systems implemented as part of this work represent important contributions. The awardwinning WorldBeat exhibit shows how computer support can open up entirely new ways of interacting with musical data. It gives a glimpse of the future in which home users, for example, may be able to hum the first notes of a symphony to start its playback from their audio equipment, then pick up a baton and not only conduct with the music but actually control the orchestra. It also shows that some musical patterns can be cast directly into software structures with an appropriate user interface, enablingusers to learn about musical concepts by interacting with them. Subsequentexhibits such as Personal Orchestra have extended the degree of realism in musical interaction, while others, such as the Interactive Fugue and Virtual Vienna, have shown the more general validity of the pattern-based approach, and particularly the HCI design pattern language developed.

But above all, they have shown that the pattern-based approach can lead to interactive exhibits creating a more intuitive, effective, and enjoyable user experience, which captures some of the characteristics of Alexander's Quality Without a Name.

## 6.3Further Research

The obvious next steps are to refine and extend the existing pattern languages, particularly the HCI pattern language for interactive exhibits. Several patterns could use additional successful examples and more pieces of empirical evidence, and new patterns can easily extend these languages in many directions.

It would also be interesting to apply the pattern principle of this text to another entirely different application domain,in order to underline the general validity of this approach.As outlined in the approach, that domain hasto show some aspects of a problem-solving or "designing" activity to be feasible for this approach. It has to be pointed out, however, that the pattern approach has in fact already been applied to a multiplicity of new domains, as indicated in the survey in chapter 2.

Another obvious next step is to refine the design of PET, and implement amore complete authoringenvironment for working with pattern languages in the format defined bythis work. Such asupport system could helpauthors to structure their writing process more easily, and it could help readers to create various views onto the pattern data, according to their own needs and preferences regarding subject area, detail, format, and presentation. In an effort stemming from the CHI 2000 workshop, we are currently looking at an improved XML definition of patterns that is based on the formal definition presented in chapter 3.

Finally, at a patterns workshop of the British HCI Group in London in November 2000, participants have formed a Task Group for HCI Design Patterns, lead by the author, within the International Federation of Information Processing (IFIP). This offers organizational and financial support for future activities, such as HCI pattern writers' workshops, collaborative publication efforts, an online journal, or a networked repository of peer-reviewed HCI patterns.

In recent years, the field of HCI design patterns has gained momentum, and it appears that this format is now beginningto gain acceptance within the HCI community. This work will be the first book publication on this exciting subject, and it will be interesting to see in what ways the field adopts and builds upon the ideas presented here.

This Page Intentionally Left Blank

## Bibliography

ACM SIGCHI. Curricula for Human-Computer Interaction. ACM Press, New York, 1992.

GreggAkkerman. Professional keyboard studies,2000. http://members.aol.com/gakkerman/index.htm.

Lauralee Alben, Jim Faris, and Harry Sadler. Making it Macintosh: Designing the message when the message is design. Interactions,1(1):10–20, January 1994.

Christopher Alexander. The Timeless Way of Building. Oxford University Press, 1979.

Christopher Alexander. Keynote Speech, OOPSLA'9611th Annual ACM Conference on Object-Oriented Programming Systems, Languages and Applications(October 6- 10, 1996, San Jose, California), 1996. (Conference video).

Christopher Alexander, Sara Ishikawa, Murray Silverstein, Max Jacobson, Ingrid Fiksdahl-King, and Shlomo Angel. A PatternLanguage: Towns, Buildings, Construction. Oxford University Press, 1977.

Christopher Alexander, Murray Silverstein, Shlomo Angel, Sara Ishikawa, and Denny Abrams. The Oregon Experiment. Oxford University Press,1988.

Apple Computer. Macintosh Human Interface Guidelines. Addison-Wesley, Reading, MA, 1992.

Lon Barfield, Willie van Burgsteden, Ruud Lanfermeijer,Bert Mulder, Jurriënne Ossewold, Dick Rijken, and

Philippe Wegner. Interaction design at the Utrecht School of the Arts. SIGCHI Bulletin, 26(3):49–79, 1994.

Lawrence W. Barsalou. Cognitive Psychology: An Overview for Cognitive Scientists. Tutorial Essays in Cognitive Science. Lawrence Erlbaum Associates, Hillsdale, NJ, 1992.

Elisabeth Bayle, Rachel Bellamy, George Casaday, Thomas Erickson, Sally Fincher, Beki Grinter, Ben Gross, Diane Lehder, Hans Marmolin, Brian Moore, Colin Potts, Grant Skousen, and John Thomas. Putting it all together: Towards a pattern language for interaction design. SIGCHI Bulletin, 30(1):17–23, January1998.

Kent Beck and Ward Cunningham. Using pattern languages forobject-orientedprograms. Technical Report CR-87-43, Tektronix, Inc., September 17,1987. Presented at the OOPSLA'87 workshop on Specification and Design for Object-Oriented Programming.

Joachim-Ernst Berendt, editor.Die Story des Jazz. Vom New Orleans zum Rock Jazz. Reinbek, Hamburg, 1978.

Bernhard Binkowski, editor. Musik Um Uns. J. B. Metzler, Stuttgart, 1988.

Jan Borchers, Oliver Deussen, and Clemens Knörzer. Getting it across: Layout issues for kiosk systems. Proceedings of the Workshop on W3-Based Online Kiosk Systems, WWW'95 Third InternationalWorld-WideWeb Conference, Darmstadt, 1995. Reprinted in SIGCHI Bulletin, 27(4):68– 74, October 1995.

Jan Borchers, Oliver Deussen, Arnold Klingert, and Clemens Knörzer. Layout rules forgraphical web documents. Computers& Graphics 20(3):415–426, May-June 1996.

JanO. Borchers. WorldBeat:Designing a baton-based interface for an interactive music exhibit. In Proceedings of the CHI 97 Conference on Human Factors in Computing Systems (Atlanta,GA, USA, March 22–27, 1997), pages131– 138,ACM, New York, 1997.

Jan Borchers and Max Mühlhäuser. Design patterns for interactive musical systems. IEEE Multimedia,5(3):36-46, July-September 1998.

Jan O. Borchers. Designinginteractive music systems:A pattern approach. In Human-Computer Interaction: Ergonomics and User Interfaces. VolumeI of the Proceedings of the HCI International '99 8th International Conference on Human-Computer Interaction (Munich, Germany, August 22–27, 1999), pages276–280. Lawrence Erlbaum Associates, London, 1999.

Jan O. Borchers. CHI meets PLoP: An interaction patterns workshop (at ChiliPLoP'99 Conference on Pattern Languages of Programming,Wickenburg, AZ, March16–19, 1999). SIGCHI Bulletin, 32(1):9–12, January 2000a.

Jan O. Borchers. A pattern approach to interaction design. In Proceedings of the ACMDIS2000International Conference on Designing Interactive Systems (New York, August 17–19, 2000), pages 369–378. ACM Press, New York, 2000b. To be reprinted in Communication In Design, special issue ofAI&Society International Journalof Human-Centred Systems and Machine Intelligence,Springer-Verlag, London, 2001.

Jan O. Borchers, Sally Fincher, Richard N. Griffiths, Lyn Pemberton, and Elke Siemon. Usability pattern language: Creating a community. Report of workshop at IN-TERACT'99 (Edinburgh, Scotland, August30–31,1999); to be published.

Jan O. Borchers, Richard N. Griffiths, Lyn Pemberton, and Adam Stork. Pattern languages for interaction design: Building momentum. Report ofworkshop at CHI2000 (The Hague, Netherlands, April 2–3, 2000); to be published.

Mark Bradac and Becky Fletcher. A PatternLanguage for Developing Form Style Windows, chapter 19,in Martin et al. [1998].

George Casaday. Notes on a pattern language for interactive usability. In Proceedings of the CHI97 Conference on Human Factors in ComputingSystems (Atlanta, GA, USA, March22–27, 1997), Extended Abstracts, pages 289–290, ACM, New York, 1997.

Alphonse Chapanis.The business case for human factors in informatics. In Brian Shackel and Simon Richardson, editors, Human Factors for Informatics Usability, pages 39– 71. Cambridge University Press, 1991.

James O. Coplien and Douglas C. Schmidt, editors. Pattern Languages of Program Design, volume 1 of Software Patterns Series. Addison-Wesley, Reading, MA, 1995.

Matthias Dannenberg. Die Interaktive Fuge: Ein Patternbasiertes Musikexponat. Master's thesis, University of Ulm (Diplomarbeit), 1999.

Peter Denningand Pamela Dargan. Action-centered design. In Winograd [1996], chapter 6, pages105–119.

Alan J. Dix, Janet E. Finlay, Gregory D. Abowd, and Russell Beale. Human-Computer Interaction, 2nd edition. Prentice-Hall Europe, London, 1998.

J. C. Dobrian. MAX Reference Manual. Opcode Systems Inc., Palo Alto, CA, 1995.

Thomas Erickson. Interaction pattern languages: A lingua franca for interaction design? UPA'98 Usability Professionals' Association Conference (invited talk), Washington, DC, June 24, 1998. http://www.upassoc.org/html/download/patterns.ppt.

Richard E. Fairley. Software Engineering Concepts. McGraw-Hill, New York, 1985.

Sidney Fels, Kazushi Nishimoto, and Kenji Mase. Musikalscope: A graphical musical insrument. In Proceedings of the International Conference on Multimedia Computing and Systems ICMCS'97 (Ottawa,Ontario, June 3–6 1997), pages 55–62,IEEE Computer Society,1997.

Erich Gamma, RichardHelm,RalphJohnson,and John Vlissides. Design Patterns: Elements of Reusable Object-Oriented Software. Addison-Wesley, Reading, MA, 1995.

John D. Gould, Stephen J. Boies, and Jacob Ukelson. How to design usable systems. In Helander et al. [1997], chapter 10, 1997.

Åsa Granlund and Daniel Lafrenière. A pattern-supported approach to the user interface design process. Workshop report, UPA'99 Usability Professionals' Association Conference (Scottsdale, AZ, June 29-July 2, 1999), http://www.gespro.com/lafrenid/Workshop\_Report.pdf, 1999a.

Åsa Granlund and Daniel Lafrenière. PSA: A patternsupported approach to the user interface design process. Position paper for theUPA'99 Usability Professionals' Association Conference (Scottsdale, AZ, June 29-July 2, 1999), 1999b.

Stephan de Haas. Softwarearchitektur?! EinVergleich mit dem Bauwesen. OBJEKTspektrum, 6:60–70, 1999.

Neil Harrison, Brian Foote, and Hans Rohnert, editors. Pattern Languages of Program Design 4. Software Patterns Series. Addison-Wesley, Reading, MA, 1999.

Martin G. Helander, Thomas K. Landauer, and Prasad V. Prabhu, editors. Handbook of Human-Computer Interaction. Elsevier Science, Amsterdam, 1997.

International MIDI Association. MIDI 1.0 detailed specification, document version 4.1. Technical report, IMA, Los Angeles, 1989.

Hiroshi Ishii and Brygg Ullmer. Tangible bits: Towards seamless interfaces between people, bits and atoms. In Proceedings of the CHI 97 Conference on Human Factors in ComputingSystems(Atlanta, GA, USA, March 22–27, 1997), pages 234–241, ACM, NewYork, 1997.

Michael Jacobs. All That Jazz. Reclam, Stuttgart, 1996.

S. Janko, H. Leopoldseder, and G. Stocker. Ars Electronica Center: Museum of the Future. Ars Electronica Center, Linz, Austria, 1996.

Robin Jeffries, James R. Miller, Cathleen Wharton, and Kathy M. Uyeda. User interface evaluation in the real world: A comparison of four techniques. In Proceedings of ACM CHI'91 Conference on Human Factors in Computing Systems, Practical Design Methods, pages 119–124, 1991.

Scott Kim. Interdisciplinary cooperation. In Brenda Laurel, editor, The Art of Human-Computer Interface Design, pages 31–44. Addison-Wesley, Reading, MA, 1990.

Edmund T. Klemmer, editor. Ergonomics: Harness the Power of Human Factors in Your Business. Ablex, Norwood, NJ, 1989.

Wolfgang Köhler. Gestalt Psychology.G. Bell and Sons, London, 1930.

Wolfgang Köhler.Gestalt Psychology:An Introduction to New Concepts in Modern Psychology. Liveright, New York, reissue edition, 1992.

Thomas K. Landauer.TheTrouble with Computers: Usefulness, Usability, and Productivity. MIT Press, Cambridge, MA, 1995.

M. Lee, G. Garnett, and D. Wessel. An adaptive conductor follower. In Proceedingsof theICMC'92International Computer Music Conference. International Computer Music Association, San Francisco, 1992.

Robert C. Martin, Dirk Riehle, and Frank Buschmann, editors. Pattern Languages of Program Design 3, volume 3 of Software Patterns Series. Addison-Wesley, Reading,MA, 1998.

Gerard Meszaros and Jim Doble. A pattern language for pattern writing. In Martin et al. [1998].

George A. Miller. The magical number Seven, plus or minus two: Some limits on our capacity for processing information. ThePsychological Review, 63:81–97,1956. http://www.well.com/user/smalin/miller.html.

Manfred Miller. Blues. In Berendt [1978], pages 41–61.

Max Mühlhäuser, Jan O. Borchers,Christian Falkowski, and Knut Manske. The Conference/Classroom of the Future: An interdisciplinary approach. In Proceedings of the IFIP Conference on the International Office of the Future: Design Options and Solution Strategies (Tucson, AZ, April 9–11, 1996), pages 233–250. Chapman & Hall, London, 1996.

Michael J. Muller, Jean Hallewell Haslwanter, and Tom Dayton. Participatory practices in the software lifecycle. In Helander et al. [1997], chapter 11.

Brad A. Myers and Mary Beth Rosson.Survey on user interface programming. In Proceedings of ACM CHI'92 Conference on Human Factors in Computing Systems, Tools and Techniques, pages 195–202, 1992.

Marc Nanard, Jocelyne Nanard, and Paul Kahn. Pushing reuse in hypermedia design: Golden rules, design patterns and constructive templates. In Proceedings of the Ninth ACM Conference on Hypertext, HypermediaApplication Design, pages 11–20, 1998.

William M. Newman and Michael G. Lamming. Interactive System Design. Addison-Wesley,Wokingham, England, 1995.

Jakob Nielsen. Usability Engineering. Morgan Kaufmann, San Francisco, 1993.

Donald A. Norman. The Psychology of Everyday Things. Basic Books, New York, 1988.

Donald A. Norman and Stephen W. Draper.User-Centered System Design: New Perspectives on Human-Computer Interaction. Lawrence Erlbaum Associates,Hillsdale, NJ, 1986.

Open Software Foundation.OSF/Motif Style Guide Release 1.2. Prentice-Hall, 1992.

Steven Pemberton. Flags are not languages. ACM SIGCHI Bulletin, 30(1):96, 1998.

R. Rich. Buchla Lightning II. Electronic Musician, 12(8):118– 124, August 1996.

Dirk Riehle and Heinz Züllighoven. A Pattern Language for Tool Construction and Integration Based on the Tools and Materials Metaphor, chapter 2. Volume 1 of Coplien and Schmidt [1995].

Gustavo Rossi, Alejandra Garrido, and Sergio Carvalho. Design Patterns for Object-Oriented Hypermedia Applications, chapter 11. Volume 2 of Vlissides et al. [1996].

Gustavo Rossi, DanielSchwabe,and Alejandra Garrido. Design reuse in hypermedia applications development. In Proceedings of the Eighth ACM Conference on Hypertext, Hypertext Design, pages 57–66,1997.

Daniel M. Russell and Mark Weiser. The future of integrated design of ubiquitous computing in combined real & virtual worlds. In Proceedings of ACM CHI 98 Conference on Human Factorsin Computing Systems (Summary), volume 2 of Late Breaking Results: Suite: The Real and the Virtual: Integrating Architectural and Information Spaces, pages 275–276, 1998.

Douglas Schuler and AkiNamioka, editors. Participatory Design: Principles and Practices. Lawrence Erlbaum Associates, Hillsdale, NJ,1997.

Ben Shneiderman. Designing the User Interface, 3rd edition. Addison-Wesley, Reading, MA, 1998.

Norbert A. Streitz, JörgGeißler, Torsten Holmer, Shin'ichi Konomi, Christian Müller-Tomfelde, WolfgangReischl, Petra Rexroth, Peter Seitz, and Ralf Steinmetz. i-LAND: An interactive landscape for creativity andinnovation. In Proceedings of the CHI 99 Conference on Human Factors

in Computing Systems (Pittsburgh, PA, USA, May15–20, 1999), pages 120–127. ACM, NewYork, 1999.

Bob Tedeschi. Good website design can lead to healthy sales. New York Times, August 30, 1999.

Jenifer Tidwell. Interaction design patterns.PLoP'98 Conference on Pattern Languages of Programming, Illinois, extendedversion at www.mit.edu/\~jtidwell/interaction\_- patterns.html, 1998.

Bruce Tognazzini. TOG on Interface. Addison-Wesley, Reading, MA,1992.

John Underkoffler and Hiroshi Ishii. Urp: A luminoustangible workbench for urban planning and design. In Proceedings of the CHI 99 Conference on Human Factors in Computing Systems (Pittsburgh, PA, USA, May 15–20, 1999), pages 386–393, ACM, New York, 1999.

Martijn van Welie. A structure for usability based patterns. Pattern collection and position paper at the CHI 2000 Workshop on Pattern Languages for Interaction Design: Building Momentum (The Hague, The Netherlands), April 2000.

John M. Vlissides, James O. Coplien, and Norman L. Kerth, editors. Pattern Languages of Program Design 2, volume 2 of Software Patterns Series. Addison-Wesley, Reading, MA, 1996.

Terry Winograd, editor. Bringing Design to Software. Addison-Wesley, Reading, MA, 1996.

Polle T. Zellweger, Susan Harkness Regli, Jock D. Mackinlay, and Bay-Wei Chang.The impact of fluid documents on reading andbrowsing: An observational study. In Proceedings of the CHI2000 Conference on Human Factors in Computing Systems (The Hague, Netherlands, April 1–6, 2000), pages 249–256, ACM,New York, 2000.

This Page Intentionally Left Blank