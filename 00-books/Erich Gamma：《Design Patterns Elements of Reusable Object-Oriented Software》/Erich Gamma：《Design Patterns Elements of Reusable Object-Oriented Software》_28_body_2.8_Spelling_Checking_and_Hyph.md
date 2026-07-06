# 2.8 Spelling Checking and Hyphenation

> Section: body | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

## 2.8 Spelling Checking and Hyphenation

The last design problem involves textual analysis, specifically checking for misspellings and introducing hyphenation points where needed for good formatting.

The constraints here are similar to those we had for the formatting design problem in Section 2.3. As was the case for linebreaking strategies, there’s more than one way to check spelling and compute hyphenation points. So here too we want to support multiple algorithms. A diverse set of algorithms can provide a choice of space/time/quality tradeoffs. We should make it easy to add new algorithms as well.

We also want to avoid wiring this functionality into the document structure. This goal is even more important here than it was in the formatting case, because spelling checking and hyphenation are just two of potentially many kinds of analyses we may want Lexi to support. Inevitably we’ll want to expand Lexi’s analytical abilities over time. We might add searching, word counting, a calculation facility for adding up tabular values, grammar checking, and so forth. But we don’t want to change the Glyph class and all its subclasses every time we introduce new functionality of this sort.

There are actually two pieces to this puzzle: (1) accessing the information to be analyzed, which we have scattered over the glyphs in the document structure, and (2) doing the analysis. We’ll look at these two pieces separately.

