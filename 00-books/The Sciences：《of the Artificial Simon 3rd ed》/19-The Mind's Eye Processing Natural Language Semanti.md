detailed way upon underlying neurology but can be explained and predicted on the basis of quite general and abstract features of the organization of memory features which are essentially the same ones that were postulated in order to build information-processing theories of rote learning and of concept attainment phenomena.

Specifically, we are led to the hypothesis that memory is an organization of list structures (lists whose components can also be lists), which include descriptive components (two-termed relations) and short (three-element or four-element) component lists. A memory with this form of organization appears to have the right properties to explain storage phenomena in both visual and auditory modalities, and of pictorial and diagrammatic as well as propositional (verbal and mathematical) information.

## The Mind's Eye

The experiments we have been discussing relate not only to visual long-term memory, but also to the Mind's Eye, the short-term memory where we hold and process mental images. In the mind's eye we can often substitute "seeing" for reasoning. Consider the economist's common supply-and-demand diagram, which shows, by one curve, the quantity of a commodity that will be supplied to the market at each price, and by another curve, the quantity that will be demanded at each price. If we notice that the two curves intersect, we can interpret the intersection as the point at which the supply and demand quantities are equal, a point of market equilibrium; and we can read off directly from the xaxis and y-axis of the diagram the equilibrium quantity and price (the x and y coordinates of the intersection). All this processing goes on in the mind's eye, using the information read from the diagram.

Alternatively, we could write down the equations for the two lines and solve them simultaneously to find the same equilibrium quantity and price. Using visual processes and algebraic ones we attain the same knowledge, but by completely different computational paths (and perhaps with vastly different amounts of labor and insight). In many scientific fields, inferences are made with a combination of verbal, mathematical and diagrammatic reasoning certain inferences being reached more easily in one form, others in another. In Alfred Marshall's famous

text book, Principles of Economics, the text is wholly verbal, the diagrams are provided in footnotes, and the corresponding algebra is given in a mathematical appendix, thus allowing readers full freedom to adopt their preferred representation in each instance.

To understand the interplay of these and other modes of human inference, we need to study the computational processes required to reach conclusions in each representation. Currently, this is a very active area of cognitive research.<sup>20</sup>

## Processing Natural Language

A theory of human thinking cannot and should not avoid reference to that most characteristic cognitive skill of human beings the use of language. How does language fit into the general picture of cognitive processes that I have been sketching and into my general thesis that psychology is a science of the artificial?

Historically the modern theory of transformational linguistics and the information-processing theory of cognition were born in the same matrix the matrix of ideas produced by the development of the modern digital computer, and in the realization that, though the computer was embodied in hardware, its soul was a program. One of the initial professional papers on transformational linguistics and one of the initial professional papers on information-processing psychology were presented, the one after the other, at a meeting at MIT in September 1956.<sup>21</sup> Thus the two bodies of theory have had cordial relations from an early date, and quite rightly, for they rest conceptually on the same view of the human mind.

Now some may object that this is not correct and that they rest on almost diametrically opposed views of the human mind. For I have stressed the artificial character of human thinking how it adapts itself, through individual learning and social transmission of knowledge, to the requirements of the task environment. The leading exponents of the formal linguistic theories, on the other hand, have taken what is sometimes called a "nativist" position. They have argued that a child could never acquire any skill so complex as speaking and understanding language if he did not already have built into him at birth the basic machinery for the exercise of these skills.

The issue is reminiscent of the debate on language universals on whether there are some common characteristics shared by all known tongues. We know that the commonalities among languages are not in any sense specific but that they relate instead to very broad structural characteristics that all languages seem to share in some manner. Something like the distinction between noun and verb between object and action or relation appears to be present in all human languages. All languages appear to have the boxes-within-boxes character called phrase structure. All languages appear to derive certain strings from others by transformation.<sup>22</sup>

Now if we accept these as typical of the universals to which the nativist argument appeals, there are still at least two different possible interpretations of that argument. The one is that the language competence is purely linguistic, that language is sui generis, and that the human faculties it calls upon are not all employed also in other performances.

An alternative interpretation of the nativist position is that producing utterances and understanding the utterances of others depend on some characteristics of the human central nervous system which are common in all languages but also essential to other aspects of human thinking besides speech and listening.

The former interpretation does not, but the latter does, provide an explanation for the remarkable parallelism holding between the underlying

assumptions about human capabilities embedded in modern linguistic theory and the assumptions embedded in information-processing theories of human thinking. The kinds of assumptions that I made earlier about the structure of human memory are just the kinds of assumptions one would want to make for a processing system capable of handling language. Indeed there has been extensive borrowing back and forth between the two fields. Both postulate hierarchically organized list structures as a basic principle of memory organization. Both are concerned with how a serially operating processor can convert strings of symbols into list structures or list structures into strings. In both fields the same general classes of computer-programming languages have proved convenient for modeling and simulating the phenomena.

## Semantics in Language Processing

Let me suggest one way in which the relation between linguistic theories and information-processing theories of thinking is going to be even closer in the future than it was in the past. Linguistic theory has thus far been largely a theory of syntax, of grammar. In practical application to such tasks as automatic translation, it has encountered difficulties when translation depended on more than syntactic cues when it depended on context and meaning. It seems pretty clear that one of the major directions that progress in linguistics will have to take is toward development of an adequate semantics to complement syntax.

The theory of thinking I have been outlining can already provide an important part of such a semantic component. The principles of memory organization I have described can be used as a basis for discussing the internal representation of both linguistic strings and two-dimensional visual stimuli, or other non-linguistic stimuli. Given these comparable bases for the organization of the several kinds of stimuli, it becomes easier to conceptualize the cooperation of syntactic and semantic cues in the interpretation of language.

Several research projects have been carried out at Carnegie Mellon University that bear on this point. I should like to mention just two of these, which illustrate how this approach might be used to explain the resolution of syntactic ambiguities by use of semantic cues.

L. Stephen Coles, in a dissertation completed in 1967, described a computer program that uses pictures on a cathode ray tube to resolve syntactic ambiguities.<sup>23</sup> I shall paraphrase his procedure with an example that is easier to visualize than any he actually used. Consider the sentence:

I saw the man on the hill with the telescope.

This sentence has at least three acceptable interpretations; a linguist could, no doubt, discover others. Which of the three obvious ones we pick depends on where we think the telescope is: Do I have it? Does the man on the hill have it? Or is it simply on the hill, not in his hands?

Now suppose that the sentence is accompanied by figure 5. The issue is no longer in doubt. Clearly it is I who have the telescope.

Coles's program is capable of recognizing objects in a picture and relations among objects; and it is capable of representing the picture as a list structure, which, in the example before us, we might describe thus:

SAW ((I, WITH (telescope)), (man, ON (hill))).

I have not tried to reproduce the actual details of the scheme he used, but I have simply shown that a picture, so represented, could readily be matched against alternate parsings of a verbal string and thus used to resolve the ambiguity of the latter.

Another program, completed by Laurent Siklóssy, illustrates how semantic information can aid in the acquisition of a language.<sup>24</sup> The reader may be familiar with the "Language through Pictures" books developed by Professor I. A. Richards and his associates. These books have been prepared for a large number of languages. On each page is a picture and beneath it one or more sentences that say something about the picture in the language to be learned. The sequence of pictures and accompanying sentences is arranged to proceed from very simple situations ("I am here," "That is a man") to more complex ones (''The book is on the shelf").

Siklóssy's program takes as its input an analogue to one of the "Language through Pictures" books. The picture is assumed to have already

"I saw the man on the hill with the telescope"

A syntactically ambiguous sentence;  
![](images/0d0ea30794197ff07dc8e08afb15ed48cd21ddf373fbbeb5e54fbff993bd7b00.jpg)  
Figure 5

been transformed into a list structure (not unlike the one illustrated earlier for Coles's system) as its internal representation. The program's task is to learn, when confronted with such a picture, to utter the appropriate sentence in the natural language it is learning a sentence that says what the picture shows. In the case of the sentence about the telescope (somewhat more complicated than any on which the scheme has actually been tested), one would hope that the program would respond to the picture with "I saw the man on the hill with the telescope," if it were learning English, or Ich habe den Mann auf dem Berg mit dem Fernglas gesehen, if it were learning German.

Of course the program could respond correctly only if it had learned earlier, in the context of other sentences, the lexical and syntactical components required for the translation. A child trying to understand the sentence must meet the same requirement. In other cases the program would use the sentence associated with the picture to add to its vocabulary and syntax.<sup>25</sup>