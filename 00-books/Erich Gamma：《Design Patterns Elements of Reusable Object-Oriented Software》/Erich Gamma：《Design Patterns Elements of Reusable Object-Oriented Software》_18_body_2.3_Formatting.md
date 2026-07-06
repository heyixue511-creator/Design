# 2.3 Formatting

> Section: body | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》\auto\Erich Gamma：《Design Patterns Elements of Reusable Object-Oriented Software》.md

## 2.3 Formatting

We’ve settled on a way to represent the document’s physical structure. Next, we need to figure out how to construct a particular physical structure, one that corresponds to a properly formatted document. Representation and formatting are distinct: The ability to capture the document’s physical structure doesn’t tell us how to arrive at a particular structure. This responsibility rests mostly on Lexi. It must break text into lines, lines into columns, and so on, taking into account the user’s higher-level desires. For example, the user might want to vary margin widths, indentation, and tabulation; single or double space; and probably many other formatting constraints.<sup>6</sup> Lexi’s formatting algorithm must take all of these into account.

By the way, we’ll restrict “formatting” to mean breaking a collection of glyphs into lines. In fact, we’ll use the terms “formatting” and “linebreaking” interchangeably. The techniques we’ll discuss apply equally well to breaking lines into columns and to breaking columns into pages.

