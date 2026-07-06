access to their children without revealing the underlying data structure they use to store them. Because iterators store their own copy of the state of a traversal, we can carry on multiple traversals simultaneously, even on the same structure. And though our traversals have been over glyph structures in this example, there’s no reason we can’t parameterize a class like PreorderIterator by the type of object in the structure. We’d use templates to do that in C++. Then we can reuse the machinery in PreorderIterator to traverse other structures.

## Iterator Pattern

The Iterator (257) pattern captures these techniques for supporting access and traversal over object structures. It’s applicable not only to composite structures but to collections as well. It abstracts the traversal algorithm and shields clients from the internal structure of the objects they traverse. The Iterator pattern illustrates once more how encapsulating the concept that varies helps us gain flexibility and reusability. Even so, the problem of iteration has surprising depth, and the Iterator pattern covers many more nuances and trade-offs than we’ve considered here.

## Traversal versus Traversal Actions

Now that we have a way of traversing the glyph structure, we need to check the spelling and do the hyphenation. Both analyses involve accumulating information during the traversal.

First we have to decide where to put the responsibility for analysis. We could put it in the Iterator classes, thereby making analysis an integral part of traversal. But we get more flexibility and potential for reuse if we distinguish between the traversal and the actions performed during traversal. That’s because different analyses often require the same kind of traversal. Hence we can reuse the same set of iterators for different analyses. For example, preorder traversal is common to many analyses, including spelling checking, hyphenation, forward search, and word count.

So analysis and traversal should be separate. Where else can we put the responsibility for analysis? We know there are many kinds of analyses we might want to do. Each analysis will do different things at different points in the traversal. Some glyphs are more significant than others depending on the kind of analysis. If we’re checking spelling or hyphenating, we want to consider character glyphs and not graphical ones like lines and bitmapped images. If we’re making color separations, we’d want to consider visible glyphs and not invisible ones. Inevitably, different analyses will analyze different glyphs.

Therefore a given analysis must be able to distinguish different kinds of glyphs. An obvious approach is to put the analytical capability into the glyph classes themselves. For each analysis we can add one or more abstract operations to the Glyph class and have subclasses implement them in accordance with the role they play in the analysis.

But the trouble with that approach is that we’ll have to change every glyph class whenever we add a new kind of analysis. We can ease this problem in some cases: If only a few classes participate in the analysis, or if most classes do the analysis the same way, then we can supply a default implementation for the abstract operation in the Glyph class. The default operation would cover the common case. Thus we’d limit changes to just the Glyph class and those subclasses that deviate from the norm.

Yet even if a default implementation reduces the number of changes, an insidious problem remains: Glyph’s interface expands with every new analytical capability. Over time the analytical operations will start to obscure the basic Glyph interface. It becomes hard to see that a glyph’s main purpose is to define and structure objects that have appearance and shape—that interface gets lost in the noise.

## Encapsulating the Analysis

From all indications, we need to encapsulate the analysis in a separate object, much like we’ve done many times before. We could put the machinery for a given analysis into its own class. We could use an instance of this class in conjunction with an appropriate iterator. The iterator would “carry” the instance to each glyph in the structure. The analysis object could then perform a piece of the analysis at each point in the traversal. The analyzer accumulates information of interest (characters in this case) as the traversal proceeds:

![](images/f43b76fb684ff173fd97a45b1e8e004e07e85c17d05e24bf496d44ad9249e44c.jpg)  
The fundamental question with this approach is how the analysis object distinguishes

different kinds of glyphs without resorting to type tests or downcasts. We don’t want a SpellingChecker class to include (pseudo)code like

void SpellingChecker::Check (Glyph\* glyph) {   
Character\*c;   
Row\* r;   
Image\* i;   
if (c = dynamic\_cast<Character\*>(glyph)) {   
// analyzethe character   
} else if (r = dynamic\_cast<Row\*>(glyph)) {   
// prepare to analyze r's children   
} else if(i = dynamic\_cast<Image\*>(glyph)) {   
// donothing   
}

This code is pretty ugly. It relies on fairly esoteric capabilities like type-safe casts. It’s hard to extend as well. We’ll have to remember to change the body of this function whenever we change the Glyph class hierarchy. In fact, this is the kind of code that object-oriented languages were intended to eliminate.

We want to avoid such a brute-force approach, but how? Let’s consider what happens when we add the following abstract operation to the Glyph class:

## void CheckMe(SpellingChecker&)

We define CheckMe in every Glyph subclass as follows:

void GlyphSubclass::CheckMe (SpellingChecker& checker) {   
checker.CheckGlyphSubclass(this);   
}

where GlyphSubclass would be replaced by the name of the glyph subclass. Note that when CheckMe is called, the specific Glyph subclass is known—after all, we’re in one of its operations. In turn, the SpellingChecker class interface includes an operation like CheckGlyphSubclass for every Glyph subclass<sup>10</sup>:

class SpellingChecker {   
public:   
SpellingChecker();   
virtual void CheckCharacter(Character\*);   
virtual voidCheckRow(Row\*);   
virtualvoidCheckImage(Image\*);   
// ... and so forth   
List<char\*>& GetMisspellings();   
protected:   
virtual boolIsMisspelled(const char\*);   
private:   
char \_currentWord[MAX\_WORD\_SIZE];   
List<char\*> \_misspellings;

SpellingChecker’s checking operation for Character glyphs might look something like this:

void SpellingChecker::CheckCharacter (Character\* c) {   
const char ch = c->GetCharCode();   
if (isalpha(ch)) {   
// appendalphabetic character to \_currentword   
} else {   
// we hit a nonalphabetic character   
if (IsMisspelled(\_currentWord)) {   
// add\_currentWord to \_misspellings   
\_misspellings.Append(strdup(\_currentWord));   
  
\_currentWord[0] = '\0';   
// reset \_currentWord tocheck next word   
}   
}

Notice we’ve defined a special GetCharCode operation on just the Character class. The spelling checker can deal with subclass-specific operations without resorting to type tests or casts—it lets us treat objects specially.

CheckCharacter accumulates alphabetic characters into the \_currentWord buffer. When it encounters a nonalphabetic character, such as an underscore, it uses the IsMisspelled operation to check the spelling of the word in \_currentWord.<sup>11</sup> If the word is misspelled, then CheckCharacter adds the word to the list of misspelled words. Then it must clear out the \_currentWord buffer to ready it for the next word. When the traversal is over, you can retrieve the list of misspelled words with the GetMisspellings