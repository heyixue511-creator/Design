Chapter 4

# A Pattern Language for Interactive Music Exhibits

“Der Worte sind genug gewechselt,

Laßt mich auch endlich Taten sehn!"

—J. W. von Goethe: Faust

This chapter shows an example of the pattern approach to interaction design, and therefore contains three pattern languages.

The structure of these patterns follows the formal definition given in section 3.1, and the component type descriptions presented in section 3.4.

To present patterns, Alexander [1979] has established a set of typographical rules that make the structure of patterns visible without requiring explicit text labels. This improves readability of the pattern text, and is in line with wellknown design guidelines against excessive labeling [Norman, 1988].

Therefore, the pattern languages in this chapter are formatted in a way that very closely follows these typographical rules used by Alexander [1979]. The rules have been identified and discussed in detail in section 2.3.

The patterns in this chapter represent the experience that the author has gathered in managing the development of the following interactive exhibits, or actibits, and designing their user interface:

1. In the WorldBeat project, an award-winning interactive exhibit about computers and music was created for permanent display in the Ars Electronica Center, a technology and art museum andvenue centre in Linz, Austria. Since many of the patterns reference this system as an example,it is described in more detail in chapter 5.

2. In the Interactive Fugue project, an interactive exhibit was designed to teach basic facts about the classical musical form of the Fugue, asused by composer Johann SebastianBach.The system was implemented and tested with some users, although it has notyet been permanently installed as a public exhibit.

3. In the PersonalOrchestra project, a system was designed and implemented that allows users to conduct various recorded audio and video performances of the ViennaPhilharmonic Orchestra, controllingthe orchestra's tempo and dynamics in real time. The system is on permanent display in the HOUSE OF MUSIC VIENNA, a newly opened major museum and exhibition centre in Vienna.

4. In theVirtual Vienna project, a virtual city tour of Vienna was designed and implemented that leads visitors to music-historically important places throughout Austria's capital. This system will also become a permanent exhibit in the aforementioned HOUSE OF MUSIC VIENNA.

Of course, the patterns also contain references to many other sources to strengthen the validity of each pattern.

Since user-centred design of interactive systems starts with learning about the application domain of a system, the first of the three pattern languages is about this application domain,"music".

Naturally, it does not cover all existing musical styles. Instead, it is the pattern language of all those musical concepts that were used in the first system, WorldBeat, particularly in those parts that deal with blues as musical style. It shows how some basic, but important aspects of the musical knowledge of an experienced blues player can be captured in pattern form.

The second pattern language leads from domain and task analysis to interactiondesign. As it is central to this text, it is the largest of the three languages. It is about HCI, and describes successful solutions to user interface design problems for interactive exhibits, as applied in the various systems listed above.

The third pattern language is about software design solutions forsuch systems. It reports successful solutions in software architecture,software design,and implementation that we used in the various projects.

The languages may seem to be useful only for a very specific area, and indeed they will be of most use for designers of similar systems. The user interface design patterns, however, address interactive exhibits of any kind, not only those dealing with music as their subject area.

Moreover, the recent success of desktop software designed in a much more playful, exhibit-like form than standard applications shows that the guidelines for exhibit design are a very good starting point to create software for other entertainment and work situations. An example of this new type of software is Kai's Power Show (see Fig. 4.1).

For all three languages, the best way to get a quick overview is to have a look at the pattern language graph at the beginning of each language. It shows the names of all patterns inthat language, and their interconnection through context/reference links.

![](images/a2160f9114f2d9d4b333e2b5ee564b9daf66d5216a2a27bbf4a14a3d2ef76b29.jpg)  
Figure 4.1: Kai's Power Show, an application for presentation authoringwith an exhibit-like interface.

## 4.1 Musical Pattern Language

This pattern language describes those important principles of the musical style blues that are used in the WorldBeat improvisation component. An overview of this language is shown in Fig. 4.2. As with all patternlanguages,the patterns are sorted so that the reader is guided from largescale to small-scale principles. In addition, the patterns of this language are arranged from left to right into groups addressing harmonic, melodic, and rhythmical aspects of a piece.

As explained in the last chapter, the application domain is seen as a design domain, making the uniform pattern format suitable for expressing knowledge in that domain. In this case,the task of composing or (more suitably)improvising a blues piece is considered a design activity, creating the music as a result. Even though the actual performing activity will not follow an elaborate,top-down design process, learning how to play blues is simplified by this structuringinto a pattern hierarchy.

Naturally, not all the rules and principles used in blues improvisation are included, but only those that were required for the musical model used in the exhibit. For example, the entire area of vocal performance, where patterns in blues lyricssuch as REPEATED TWO-LINERScould beidentified, has been left out because it is not addressed in the World-Beat improvisation component either.Similarly, basic music patterns unspecific to blues, such as the underlying 4/4 RHYTHM or CHROMATICSCALE, are not included because their concepts are also assumed as given in the exhibit.

![](images/ade484910fee020f44a0b3c51b730ecc40e8d7180abebefaa7a175825a8df84c.jpg)  
Figure4.2: The musical design pattern language used for theWorldBeat improvisation feature.

## M1 BLUES STYLE

![](images/6166564e765a977e481c6862bebbe37d9722da694cf0d1c8d1c534c312687507.jpg)  
Figure 4.3: Railroad workers.

...you are searching fora musical style to play, sing,and improvise in, probably together with other players, without having formally rehearsed anything together.

##

Playing together with others without prior rehearsal is oftendesirable on spontaneousoccasions. But without a common repertoire of defined pieces,it is hard to play well together.

The opening photograph shows a group of Afro-American railroad workers.Suchworking situations created the desire to sing together to easethe workload and coordinate the work. Spiritual events were another source for spontaneous group music. The resulting music was shaped by the African cultural roots ofmanyAmericanslaves, with syncopated beats andpentatonic melodies.

Since jazz has become a mainstream musical style, jazz musicians invariably know the blues style as the root of the entire domain of jazz music. At spontaneous meetings and "jam sessions", a blues is often chosen to start playing together, or when no sheet music is available and no pieces are known by all players. Despite its simple structure, it can create very emotional and appealing performances.

## Therefore:

Use the blues style to start playing together with others. Make sure that its simple basic harmonic form is known by everybody, and agree on tempo, key choice, choruses, and introduction and endings. With that in place, you can start playingimmediately, and still create a coherent musical impression.

![](images/68b30c9ffb6996259b8667f3648328f2aaad9fc9fd199a580a8e86c56cdd7949.jpg)

Choose a suitable set of instruments in your group COMBO INSTRUMENTATION(M2). Use thebasic blues progression oran extension of it—TWELVE-BARPROGRES-SION(M4). Forimprovisation, start with the pentatonic note scale asnotematerial—PENTATONICSCALE(M7), andmake sure everybody knows about the characteristic, swinging playing style—TRIPLET GROOVE(M9). ...

## M2 COMBO INSTRUMENTATION

![](images/eb9f0870aeacfcb07783c4c6fbe37947be19d9720907a7dad4393c1c903b3b42.jpg)  
Figure 4.4: Louis Armstrong's Hot Five: a jazz combo.

.. . you wish to play a blues piece—BLUES STYLE (M1). First, you need to see what instruments will be played together.

##

Too many instruments, especially with unrehearsedperformance, tend to sound too dense. On the other hand, too few instruments may mean that vital harmonic, rhythmic, or melodic parts are not played by anyone.

Early blues music was played using very simple means: vocals and hand-clapping often were enough.

Today, a variety of instruments is used, but some, such as drums and bass, have become standard for rhythmic accompaniment, and instruments such as guitar or piano often add the harmonic information to a piece. Solo instruments such as trumpet, saxophone, etc. take over the role of the vocalist,adding the melodicdimension. However, most combos combine someinstruments fromtherhythmic/harmonic section with some from the melodic section to create a balanced musical spectrum.

From vocals and hand-clapping, to rhythm and solo instruments

## Therefore:

Use a combination of one or several rhythm sectioninstruments, such as drums, bass, piano, or guitar, plus one or severalsoloinstruments,suchasvocals,harmonica, trumpet, or saxophone.

![](images/00bbe64b8551f57145e21eea75d7eb6637a13b2362a70a66c0a86305f668c85f.jpg)

See that the combo takes turnsin improvising—SOLO & COMPING (M3). ...

## M3SOLO& COMPING\*

![](images/1f2d418a04e3e45e9924e5ca6dd900ba4bceac9bafdd17eec5ce906a6db6dc60.jpg)  
Figure 4.5: Jimmy Garrison accompanying John Coltrane.

... you have decided on a combination ofinstruments foryour performance—COMBOINSTRUMENTATION (M2). Now you have to decide when each instrument plays which role in the performance.

##

Improvisation is the key to good blues music, however players need to agree on a "protocol" to avoid a too dense and chaotic musical outcome, where all players solo all the time.

In contrast to symphonic compositions, most blues and jazz performances divide players -into the roles of soloist and accompanying ("comping") players. These roles usually change dynamically during a piece.

Recordings from classic jazz combos often reveal a structure where the melody ("head") of a piece is played first, followed by all players taking turns to improvise over this theme, and completed by a repetition of the head to end the performance.

## Therefore:

Let players take turnsin soloing, includingmelody instruments as well as accompanying instruments. The remaining players stepback musically,and some of them accompany the soloist. Each soloistsignals the next soloist when he is finished.

![](images/8b24783d686407b58d7f884063977c4576a22b0372786755d11ee51453a4014d.jpg)

This is a basic pattern that has no further references within this pattern language.

## M4 TWELVE-BAR PROGRESSION \*

![](images/8e4cd5323d95005e3a5d6dba0910f52ed62e46cc8027a7d91423e15bb60d712f.jpg)  
Figure 4.6: Chord progression for a twelve-bar blues.

.. . you wish to play some blues music—BLUES STYLE (M1). An important choice to make is the sequence, or progression of chords to play.

## ∞

blues depends on improvisation, and should therefore be interpreted as freely as possible, but there is a basic harmonic structure that the players need to know in order to make their piece sound like blues music.

Miller [1978, p. 42] defines the blues harmony as consisting of three 4-bar groups: four bars tonic (I)1; two bars subdominant plus two bars tonic; two bars dominant plus two bars tonic, He also explains that thisisjust the most frequent form, and that deviations are quite common.

Countless blues recordings reflect this basic harmonic structure, and it has carried over to later music as well for example, the choruses in Bill Hailey's well-known Rock Around The Clock.

## Therefore:

Use the simple twelve-bar blues progression as the basic harmonic form of each chorus: four bars tonic—two bars subdominant plus two bars tonic—two bars dominant plus two bars tonic.

$$
1 \pm 1 \pm 1 \pm 1 \pm 1
$$

$$
\vert \overline { { \mathbf { x } } } \vert \ \overline { { \mathbf { x } } } \vert \ \pm \vert \ \pmb { \tau } \vert \ \pmb { \tau } \vert \ \pmb { \tau } \vert
$$

$$
| \textsf { x } | \bot | \textsf { x } | \ I | \ U
$$

$$
\diamond \diamond \diamond
$$

Each musical degree in the above progression typically consists ofa dominantsixth or seventh chord—SIXTH AND SEVENTH CHORDS (M5). The simple progression can be extendedwith inserted transitionsto other chords—CHORD TRANSITIONS (M6). ...

## M5SIXTHAND SEVENTH CHORDS

![](images/e7390a5761ebb0061d8052a0364956cc58e724109ed52190a03c0007a8a51dc1.jpg)  
Figure 4.7: Progression with alternating sixth chords.

….. as overall structure, you have agreed upon a certain sequence ofchords for your performance—TWELVE-BAR PROGRESSION(M4). Now you need to decide how to finestructure that progression.

![](images/955b57ab520ef51d31715a75c8da00d6c8e77aa406d6ce89c6c07bcd15bd928b.jpg)

To create a well-sounding blues piece, you have to stay within the chord structure you have agreed on,but the basic chords of the progression sound simplistic if they are not enriched in any way.

A typical left-hand piano accompaniment for blues music, as shown in the opening picture, uses quarter-note chords that change between includingthe fifth andsixth step, effectively changing the base chord into a sixth chord every other beat.

Blues, like many other musical styles, also often uses minor seventh chords when the current chord is in a dominant function (leading a fifth backwards) to the next chord, such as a $G ^ { 7 }$ before a C major chord.

## Therefore:

Instead of the simple triad chords from the progression, frequently use sixth chords, and use seventh chords if you are about to step back a fifth to the next chord.

![](images/b81bd418222c656092a977e638e60947914bd303aac733d10fbeb9c97c8830b1.jpg)

##

This is a basic pattern that has no further references within this pattern language.

## M6 CHORD TRANSITIONS

![](images/d11eac20cd77191236fa701ed42f96fc8f11c3bd9ff624b644f3150493efb463.jpg)  
Figure 4.8: I-VI-II-V chord transition.

... you have found a basic harmonic structure—TWELVE-BAR PROGRESSION (M4). Now you need to decide if you wish to refine and extend it beyond its basic form.

![](images/666778d11be6e1c5996b7950d92aa1ccea98cf6125794803f87245c0ac9115d8.jpg)

The twelve-bar schema is important to create a piece that sounds like blues, but without changing the schema, pieces will sound very similar.

A technique usedvery frequently to vary chord sequences is to replace a chord by a transition leading to the following chord via a series of fifth intervals. For example, the last two tonic bars in the twelve-bar progression are often replaced by a sequence such as $^ { \prime \prime } \mathrm { I - V I - I I - V ^ { \prime \prime } }$ , lasting half a bar each and leading back to the tonic (I) of the next chorus via a series of downward steps through the fifth circle.

## Therefore:

Replace parts of the twelve-bar progression with more complex chord sequences to create a more complex musical style. Concentrate on replacing chords at the end of each four-bar group, and frequently use a transition that leads back to the following chord via a sequence of fifth steps.

![](images/671be6fb8cfdb31de92ce69ee092a8d504bd4e7e7da8482e6237a36e5bccff66.jpg)

##

This is a basic pattern that has no further references within this pattern language.

## M7 PENTATONIC SCALE \*\*

![](images/2c692d369028728c5007f4bbd4bae9e43feb86d0f58bfddbe880be9240cad0a7.jpg)  
Figure 4.9: Nice Work If You Can Get It.

… . .you want to improvise over a blues piece—BLUES STYLE (M1), so you now want to know which notes in the current key are especially useful as"raw material" for improvisation.

##

Just using the notes of the simple triad chords of the current key is too simple for improvisation. But using all notes in the chromatic scale equally would remove the harmonic context completely.

Most western music is based on the chromatic scale, but uses only a subset of it as material for creating melodies. The remaining note of thescale are used as well, but less frequently and with less emphasis.

Blues music has its roots in African music, where pentatonic scales are the most frequently used [Binkowski, 1988, p. 130]. For example, a C major pentatonic scale contains the five notes C, D, E, G, and A. It contains no semitone steps, which makes it fit well with a wide range of chords.

The opening example shows the refrain of the jazz standard "Nice Work If You Can Get It".Note that the melody only uses the notes G, A, B, D, and E, which is exactly the pentatonic scale over the base key of this piece, G major.

## Therefore:

Use a scale containing the prime, second, third, fifth and sixth note of the major scale in the current chord as your preferred note material for improvisation.

![](images/13cedf394a8a384db245239e7fe0f0575030050bb8fb554f2111480c45ca5e14.jpg)  
The pentatonic scale is also a good starting point to play abassline—WALKING BASS(M10). Fora genuine blues sound,you need to extend the pentatonic scale with additional "blue" notes—BLUE NOTES (M8). . ..

## M8 BLUE NOTES\*\*

![](images/8928fb848204367ac8fff2f69f9aa171ea11887895ba5bca2c74dd820084be36.jpg)  
Figure 4.10: St. Louis Blues.

... you are thinking about themelodicmaterial for blues improvisation—PENTATONICSCALE (M7), and you now want to extend the basic note material.

##

The pure pentatonic scale does not create enough musical tension for a blues piece. But not all other notes canbe used to enrich the scale; additional notes have to support the musical impression typical of blues style music.

African music, as the root of blues, enriches the pentatonic scale with notes that have no direct correspondence in the chromatic scale [Binkowski, 1988, p. 171]: they lie between the flat and natural notes of the third, fifth, and seventh degree. To western listeners, the resultingscale sounds similar to a minor scale, creating a musical impression of sadness or feeling "blue", which gave the blues its name.

Many instruments used in jazzandblues, suchas vocal, bass, and guitar, can produce those notes outside the chromatic scale;other instruments approximate them,usually using the lower of the two neighbouring chromatic pitches. The notes are often slid up towards the next natural note.

## Therefore:

Use the pitches between flat and natural third,flat and natural fifth, and flat and natural seventh of your current scale as blue notes, in addition to the pentatonic scale material. If your instrument can only play chromatic notes, use both notes,frequently sliding from the lower to the upper note.

![](images/c129e94e4aeef1847ec34f6f65fdcbf055ebf5aa9a80eb80ce31e20b27aeb0ea.jpg)  
This is a basic pattern that has no further references within this pattern language.

## M9 TRIPLET GROOVE \*\*

![](images/a4fc9ebc593457281789c60393ea76afdb67c089406c28631635d475cc48db4c.jpg)  
Figure 4.11: Lover Man.

.. . you wish to play a blues style piece—BLUES STYLE (M1). You should use a certain rhythmic feeling when playing, which is particular to jazz music in general.

##

Players need to create a swinging rhythmic feeling. The straight rhythm from other musical styles does not create this effect. At the same time, sheet music cannot include all rhythmic variances, because it would become too complex and unreadable.

Most jazz recordings show the solution to this problem. It is an often triplet shift of the intermediate beat in the rhythm section of a band to make the music "swing". For example, if the drummer's score contains a sequence of eighth notes to play on his hi-hat, he will interpret them roughly as an alternating sequence of 2+1triplet eighth notes to create the swing feeling.Comparative studies of jazz recordings show that most bands actually have their own specific groove timing that helps us recognize them.

## Therefore:

Where the written music contains an evenly spaced pattern of eighth notes, shift every second eighth note in thepattern backwards in time by about one third of its length, shortening it accordingly, and make the preceding eighth note one third longer. Instead of a rhythmic length ratioof 1:1, the resulting pattern are alternating notes with a length ratio of $\begin{array} { c c c } { { \frac { 2 } { 3 } } } & { { : \frac { 1 } { 3 } } } \end{array}$ . Two straight eighth notes have been changed into 2+1 triplet eighth notes. This rhythmic shift creates what musicians call the "laid-back groove" in a performed piece. The actual shift percentage can vary widely, but usually depends on the tempo: the faster a piece is, the less shifting takes place.

![](images/769935007287b16284c192cd74460a05aad2737dbee8d1de42600eb8b6479e1c.jpg)

The bass line can occasionally pick up this groove to make its standard bass pattern more varied—WALKING BASS (M10). For blues music,the rhythmic shift should even more than a triplet, because ofthe slow tempo—BLUES TEMPO (M11). ...

## M10 WALKINGBASS \*

![](images/b03a7f4273ffc42462a3c3fe6cdbf953e9f4dc6d1081e3b62d08e821578c1aa1.jpg)  
Figure 4.12: A walking bass line.

. . . you want to play blues-BLUES STYLE (M1), and you now need to find a suitable bass line for the music.

![](images/aef4d7908a82f03b5f91c53fb05bf7a4223d948fc0a49df0c674e04c8a9261fb.jpg)

The bass needs more note material than what is included in the current harmony chord. But adding arbitrarynotes with large intervals between them leads to a loss of continuity and harmonic context in the music perceived.

A standard bass line used frequently in blues and boogie pieces consists of quarter notes that walk up and down a scale of the first, third, fifth, sixth, and minor seventh degree in the current harmony. It is the most frequently used walking bass line, but can be varied to become more interesting, and to cover other harmonic progressions, as shown in the opening picture: as long as the line uses quarter notes continuously, with the chordroot appearing at the beginning of each new chord, the last quarter before a chord change leading to the next chord root, and other notes from the chord for any notes in between, a suitable accompaniment with a "walking" impression is created [Akkerman, 2000].

## Therefore:

On the first beat of a new chord, play the chord root. On the following beats, play other notes from the chord, such as the third, fifth, sixth, or seventh, depending on the chord symbol. On the last beat before a chord change, however, play a note approachingthe next chord root from a half-step above or below.

![](images/0389a6e3ee7cc1596f241ac65aac15702fd9556395cad37930bdea098c1ef72e.jpg)  
This is a basic pattern that has no further references within this pattern language.

## M11 BLUES TEMPO

## EVERYDAY (I HAVE THE BLUES)

![](images/6bd68448f25ec6df9028c74c8c20996ab339e913b9e48d6ef458b48a1dbf6a63.jpg)  
Figure 4.13: Everyday I Have The Blues.

…. . you have found a way to accompany your blues piece— WALKING BASS (M10). You now have to agree on a tempo.

Blues needs a certain laziness to create the right mood, however, if the tempo is too slow, the music can use its rhythmic continuity and drive.

Typical blues recordings have a tempo ofaround 60–120 beats per minute (bpm). For example, Spencer Williams' classic Basin Street Blues is played at around 100 bpm. The opening example also suggests a"walking blues" tempo.

## Therefore:

Choose a tempo between 48 for a very slow blues, and 128 for a fast, rhythm-and-blues piece.

![](images/a45d8096de3a7588ade41e9a16f7f9afa3e26c84f6589e7910e66cd8690c4961.jpg)  
This is a basic pattern that has no further references within this pattern language.

## 4.2 HCI Pattern Language

This section presents a language of design patterns for human-computer interaction. They address the task of designing interactive systems that are used in public spaces. This scenario requires designers to pay special consideration to the immediate usability of their systems. They need to design for a target group who are typically first-time and one-time users at the same time, and who generally have no professional motivation requiring them to use the system. Overall interaction duration is often within a few minutes only.

Typical systems falling into this category include interactive exhibits at museums and exhibition centres, butalso other public systems that are generally referred to as kiosk systems. These systems can be classified into four groups, according to their main function [Borchers et al., 1995]:

Information Kiosks have the primary goal to provide information in a usually limited subject field. An exampleis an interactivetrain schedule information system at a railway station.

Advertising Kiosks that are installed to present a company or institution or its products and services to the public. Today, the web presence of many companies still falls into this class.

Service Kiosks emphasize the flow of information from the user back to the system—for example, hotel reservation systems.

Entertainment Kiosksmay just help people pass their time, or serve to attractcustomers for a business. However, they often have a secondary function of one of the other kiosk types.

Of course, real systems will often belong to two or more of the above classes, but there is usually a primary goal that should be identified for the system as a whole, or at least for its individual content parts.

The systems that are used as primary source for examples in the following patterns belong to the class of interactive exhibits. They can be classified as entertainment kiosks that have an educational message to be delivered, but which is wrapped into an engaging interactive experience.

The hierarchy of patterns is presented in Fig. 4.14, followed by the individual patterns themselves.

![](images/5a6b1738c15af7cda3172eecbb063a8ed0317cab164c982cadeaf7c89e82f53f.jpg)  
Figure 4.14: The human-computer interaction design pattern language for interactive exhibits and similar public access systems.

## H1 ATTRACT-ENGAGE-DELIVER\*

![](images/d68a9f56c47e34d32e9ff7cade12c8b080d216a4d4954f5f468505cbf60736b6.jpg)  
Figure 4.15: Visitors in the Ars Electronica Center.

….. the prerequisites for interaction design, such as initial user profiling and task analysis, are fulfilled, and you are now starting to design theoverall user experience of your interactive exhibit. You want to decide what the goal of the interaction is, and whatinteraction phases can be distinguished to achieve that goal.

![](images/75a9fca42904c3ce32a78af4e09c011a279194d9aa356581aaacff7a84dc573b.jpg)

An interactive exhibit is mostly used by people for entertainment, but it usually has to fulfil a purpose beyond that. However, the intended usage duration is generally limited because many visitors should be able to experience the exhibit over the course of a day.

The user profile of an interactive exhibit is usually very broad, and users generally have no strong need to use such a system. This means that the initial interest to use such a system must be motivated by the system itself.

Most interactive exhibits, however, are not just for entertainment. Their goal is deliver a "message"—to explain some facts, concepts, or ideas—to the user, through the interaction. Therefore, it is important, after the initial attraction, to keep the user occupied until this message can be delivered.

But once this goal has been achieved, it is important to allow the user to end the session in a planned and positive way. Users generally should not break off in the middle of an interaction because they have become bored, or because they do not know when they will be able to leave the system orderly.

For example, in the Exploratorium, a children's technology discovery museum in San Francisco, each exhibit is labelled with a three-sentence description of the following form:

To do and notice: This part explains briefly what to do with the exhibit,which buttons to push or levers to move, and what to look for in the system reaction. For example, an exhibit on glass fibres would tell the user to press a button to light a lamp, and to observe how the light comes out of the end of a bent glass fibre.

What's going on?The secondsentence summarizes what is happening in the system. In the example, it would explain how the light is reflected by the inside of the glass fibre wall.

So What?The last sentence, probably most important, tells the visitor why this phenomenon is important. In the example, it would explain how glass fibre cables can be used to transmit information very quickly.

These descriptions actually make the attraction, engaging, and delivering phases of the interaction with an exhibit explicit.

Similarly, theWorldBeat system wants to convey an overall message: that computers open up new ways to interact with music. Each of thevarioussub-functions of the system shows a more specific example of this general message: how computers can helpwith conducting, improvising, finding music, etc.The system initially attracts visitors with an interesting yet simple interface that quickly leads to a main selection display of those features. Each feature in turn briefly andexplicitly explains what its “message" is. When the user has explored one of those features, he has taken its specific message with him, and is returned to the main selection page where he can continue exploring the system, or leave the exhibit in a consistent and satisfying way. Nobody explores the system completely; this would also take much longer than the interaction duration as planned by the exhibition centre. Instead, most users explore only a few of the features, but still take the messages from those features with them.

![](images/e2e3c57bebec8e156759437e917091c002cda267c84d6f3f20ff69ccb35193ea.jpg)  
Figure 4.16: The WorldBeat start screen, explaining what to do, how the system works, and what its main message is.

## Therefore:

Design the interaction so that it takes place in three phases: attracting users, engaging them, and delivering one of the "messages"to them which the system wants to convey. Attach an average interaction time to each of those phases so that a typical, successful interaction with message delivery only lasts as long as allowed by the institution for its visitor throughput.

![](images/5a72ed207cde9155b90bb66086d4fc7e79e57ff3128bdeaa146421947087bcb2.jpg)

To get people to have a closer look at your system in the first place, attract them with the initial appearance of your system when they are close to it—ATTRACTION SPACE (H2). To keep them engaged, gradually reveal more interesting features of your system to them—INCREMENTAL REVEALING (H6). If your system has several messages to convey, let the user know when each one is delivered, and offer an option to leave the system—CLOSED LOOP(H9). ...

## H2ATTRACTION SPACE \*

![](images/5dfbec55fb20105233acc88907b2a346f63fa79ebe8462b04baeeaf8a886128a.jpg)  
Figure 4.17: Sample start button design.

.. . you are designing the interactive appearance of an interactive exhibit—ATTRACT-ENGAGE-DELIVER(H1). You are currently looking at the first step, and need to find out what the system should look like when it is first encountered by the user, and how it can fit into its environment.

##

In an environment such as an exhibition centre, many systems are competing for the visitor's attention. To find out about a system'smessage, visitors first have to notice it. However, if a system is too visually active or noisy in its appearance,it can disturb the atmosphere of its entire environment.

When an interactive system is not being used, its appearance in the “idle" state is the first thing that a passing visitor notices. Ifthis impression does not draw the visitor towards the exhibit, he will never find out about what the system has to offer. After all, there is usually nothing that forces a visitor to use any of the stations in an exhibition centre. This is very different from the situation in which, for example, office software is used: there, users need to get a job done, and have their own initial motivation to approach and explore the system.

There are two principal channels that an exhibit can use to increase its noticeability: visual signals, which are directedand therefore onlynoticed if the visitor looks into that direction, andauditory signals,which are undirected and therefore much stronger, since they are noticed by everybody in the vicinity.Strong visual cues such as intensive animation or very large displays can also have an undirected effect, since they draw attention even when they are observed in the visual periphery of the user.

However, a system must not create too much audible noise or visual disturbance,because a sensory “overflow"will irritate users and make them leave the entire environment to escape from such a multimedia chaos. Instead, the systems within such an environment need to coexist to create a positive overall experience for the visitor.

The WorldBeat exhibit (see appendix B) solves this conflict in the following way. Although it is an exhibit about music, it does not create any noise when not in use. Instead, it shows a very simple, and aesthetically pleasing, opening screen that invites the visitor to explore the exhibit. No animation is used, and the impression is quite calm. But its main attraction is created by a different visual cue: a pair of infrared batons is dangling from the ceiling in front of the screen. There is a little light blinking on each baton, barely visible, but just enough to show that the batons are “alive". These batons look interesting, they are something the user has never seen before, and therefore invite exploration. Despite this attractive appearance, the exhibit does not dominate the space around it further than its distance to the next exhibit allows,neither by auditory nor visual means.

Another example is a typical start screen of a video game or kiosk system. These screens often use a specially rendered, three-dimensional, or textured "Start" button (see the opening picture) that the user has to press to enter the system. This button looks much more inviting than the simple word "Start" on a screen, but it also only dominates the space belonging to the display of this particular system.

Naturally, the right level of sensory stimulation depends on the application domain. A video games arcade hall is a good exampleof this point. It often creates a noisy environment withflashing light effects, where the stimuli from neighbouring systems strongly interfere. While this is the environment many players seem to like; it is obvious that it would be far too overloaded to be adequate for studying exhibits in an exposition centre.

In1998,the Techniek Museum Delft created an exhibition called"De Digitale Schoolreis" (TheDigital Class Excursion),which included, amongotherexhibits,a dolphin "Fin-Fin" (an interactive computer character) that children could interact with. Thefact, however, that this dolphin started whistling every few minutes to attract attention to itself soon drove the museum staff crazy; it penetrated the attraction space of an entire floor. This shows that especially audio stimuli can easily become a nuisance, not only in office software, but also in interactive exhibits.

## Therefore:

Define an attraction space around your system that is as large as possible, but without penetratingthe attraction spaces of neighbouringexhibits. Then,make sure that your system does not frequently violate this border. To achieve this, use primarily static visual stimuli in the physical shape and appearance of your interface that look attractiveby their design alone. Avoid excessive animation, and especially frequent undirected stimuli such as audio, because they easily interfere with neighbouring attraction spaces.

![](images/0bd001024609f58e84d8d71ee38daada3c6725fda2fa70a07e466c91a3244635.jpg)

A good way to attract people is to make your system look like something they have never seen before—INNOVATIVE APPEARANCE (H12). However,you should make sure that your system does not scare off potential users because it looks too complicatedto use—SIMPLE IMPRESSION (H5). You can convey a quick first idea of what your system is about by using peripherythatmatches your application area—DOMAIN-APPROPRIATE DEVICES (H11)....

![](images/29596b74f72acccb0d9098a754e2d7c4f06530a3b963ec381609e580f5346204.jpg)  
Figure 4.18: Two museum visitors using WorldBeat together.

... the overall structure of the interaction is in place ATTRACT-ENGAGE-DELIVER (H1), andyou are ready to think about the form in which each of those phases should take place. You may already be considering a setup that sketches the interaction of a single person with your system.

$$
\diamond \diamond \diamond
$$

Museums, exhibition centresand similar public places are usually visited by groups of people. However, most interactive systems can only be used by a single person at a time.

Standard user interface design mostly cares about the scenario in which one person interacts with a computer. The term"Human-Computer Interaction" reflects this attitude, which for many interactive systems is quite acceptable. However, even when the social context of the user and his task are taken into account, it is not normally considered that the actual interaction can take place between two people sharing the same system. Those scenarios are rather dealt with in the discipline of computer-supported cooperative work (CSCW).

The WorldBeat exhibit features not one, but two infrared batons to create musical input in many of its components. For example, the "Instant Salsa"setup, a part of the Joy-Sticks component, lets one user play a rhythmic Salsa pattern by swinging her baton up and down, while the second user can insert trumpet riffs and drum soli into the music by hitting downwards, or pressing the button on his baton. As the opening picture shows, users are having a lot of fun using the system in this way: instead of one user disappearing in a virtual world of interaction with a computer system, where only he knows what is happening, the system fades into the background and becomes a medium for two people to interact with each other, in this case musically Its big advantage over normal human-human cooperation is that it can still augment the cooperation with subtle help, such as matching the notes created by both players onto a common musical scale.

Of course, there are many situations where especially control input cannotreasonablybe shared between people. WorldBeat, for example, only lets one of its two batons control the on-screen pointer used for menu selection and other control input, and only one baton is active in the conducting component (two people conducting at the same time would not make much sense).

Inaddition to this active cooperative use,interactive exhibits should allow additional people to watch what is going on. This not only increases the number of visitors who can, at least in some way, experience the exhibit at the same time,it also helps them to prepare themselves if they are next in line to actively use it. This reduces subsequent learning time in the active usage phase, which also increases active visitor throughput.Moreover, it can attract passers-by who wouldnever stop if all they saw is, say, a person staring into (and occluding) a small monitor.

The CAVE installation in the Ars ElectronicaCenter in Linz, Austria, offers a highlevel ofthis type of cooperative experience: not only the main user, but a dozen additional people, all wearing special digital glasses, can enter a room where walls and floor are large displays creating the illusion of a three-dimensionalreality. While only the main user has a control for moving around this virtual environment, and only his position affords anideal threedimensional view, all other users in the roomcan participate in this experience to a high degree. Other exhibits in this centre, such as a flight simulator,feature large monitors mirroring what the active user currently sees, thereby communicating his experience to bystanders.

![](images/730091eea9dc51aa38c73806576ddc55970d879d559df6ba93c5bf7a3d1afb02.jpg)  
Figure 4.19: Main user and bystanders in the AEC CAVE.

If cooperative experience is not planned, it will occur nevertheless. For example, where exhibits are equipped with headphones, people can often be observed sharing the single headphone set between them, awkwardly huddling together (and bending the headphone dangerously). What they are trying to do is to create a cooperative experience where the designer did not care to plan for one.

## Therefore:

Allow two people to actively use your interactive exhibit together at the same time. Ensure that at leastfive bystanders can watch, listen to, or otherwise passively experience the exhibit while it is being used by somebody else.

![](images/c4f9c0a7111b29b4a9b2ac790e06ffcfd3d08f841e97788af7be8b33cc733684.jpg)  
Cooperative use often involves one user handing control over to the next—EASY HANDOVER (H4). Display size has to be chosen correctly to create the right level of immersion—IMMERSIVE DISPLAY (H13). ...

## H4 EASY HANDOVER\*

![](images/fa0cdcf6ef9a1a3f1e4a336790fdac9a8107f12bcc03c8eafc5d1d0016aa30dd.jpg)  
Figure 4.20: A visitor waiting for her turn to useWorldBeat.

.. . you have found a way to attract users if the system is not presently in use—ATTRACTION SPACE (H2), and how to engage them and convey the system's messages to them CLOSEDLOOP (H9). Now you have to think about the situation when a user wants to "take over"from the previous visitor, a common situation in busy environments.

##

Most interactive systems implicitly assume that each user begins using their system from a start page or initial state. At interactive exhibits, however, one user often takes over from the previous one, possibly in the middle of the interaction, and without knowing the interaction history of the previous user.

Most traditional, desktop-oriented interactive systems can be designed from a point of view where a user initiates the interaction from a defined starting point (for example by launching an application). Moreover, a typical user accesses such a system many times, and already knows something about the system when he accesses it.

In the WorldBeat system, for example, visitors often take the batons from their predecessor while that user is in the middle of interactingwith one of the system features. The two possible actions then (which have both been observed) are either that the new user continues to use the same feature (e.g., conducting), or that he uses the "back" button and chooses a different feature.

WorldBeat supports the first alternative by a design that has no user-specific state. The only state that users can create in a system is the position within the hierarchy of features (e.g., the fact that "conducting" is the currently active feature) and the settings of the controls within this feature (e.g., the solo instrument selected in the improvisation module). No personal data, such as names or digital photos of the user, is created in the system, so the user who takes over has no need to“reset" those values to his own settings.

The second alternative is supported by a "back" button that is available on every page of the system, and that always leads back up the hierarchical menu tree of available features.

In both cases, the new user cannot be expected to have seen the introductory screen explaining how the batons are used. This knowledge, however, is something that the new user has already gathered from watching his predecessor using the exhibit before taking over.

The Virtual Vienna exhibit, which lets users take a virtual tour of the city of Vienna, uses an even more stateless approach. The only parameters that users change by interactingwiththe exhibit are the current geographicalposition within the virtual environment, and the choice of language for the interface. It is not necessary to return to a specific "starting"point in the application to begin using the system, and the language can be changed at any time through a button that is always available.

The HCI pattern collection by Tidwell [1998] contains a pattern BACK TO A SAFE PLACE, which represents a similar idea. It recommends to always supply userswith a simple means of getting back to an initial, known, or otherwise "secure" state if they get lost in the course of interaction.

## Therefore:

Minimize the dialogue history that a new user needs to know to begin using an interactive exhibit. Offer a simple means to return the system to its initial state.If critical,user-specific parameters such as language need to be set by a user, let users change the setting at any time, no matter where they are in the system.

![](images/1b382670698a8a788f51ccddca1d766d52a9612b11f2710afccd1be0ccbac396.jpg)

If your system needs to present a multitude of information units (such as screen pages), arrange them so a new user can quickly find his way back to the main selection— FLAT AND NARROW TREE (H7). Minimize using information forms that depend on language or culture, at least for the basic information necessary to operate the exhibit and set the language—LANGUAGE INDEPENDENCE(H10). ...

## H5SIMPLE IMPRESSION \*

![](images/19f2892a949e1ccca24aa366f3ebbdf25c48ea0a190e88eef348667cd63ad136.jpg)  
Figure 4.21: The WorldBeat exhibit when not in use.

...youhave decided to create an attractive,innovative system—ATTRACTION SPACE (H2). Now you need to find a way to lure people into using your system, and not become frustrated with it.

$$
\diamond \diamond \diamond
$$

Interactive exhibits are supposed toconveyoften complex messages, and show the power and fascination of intricate new technology. However, users of such systems aretypically first-time, and one-timeusers with no time to go through a long learning curve.

The WorldBeat includes a complex variety of innovative hard- and software, such as infrared batons, or algorithms to retrieve songs through hummed queries. Its goal is to convey how computers support new ways to interact with music, so the power of those technologies is part of its message.However, the typical user has never before encountered the system, probablynever will again, andonly intends to spend a few minutes with it to"see what you can do here". Therefore, the system was designed to convey a very simple, inviting system image to the user. It only offers few, non-professional input devices (neither computer keyboard nor piano keyboard), no shortcuts to circumvent the hierarchical navigational structure, and often just one choice where more would have been simple toimplement.

Someoperating systems offer a specific “simple mode" of operation geared towards unexperienced users. It removes access to advanced features from the user interface, simplifying the impression that the system conveys. An example is the Simple Finder option in Mac OS®.

## Therefore:

Make the user interface of your interactive exhibit as simple as possible, and communicate this simplicity visually through the appearance of the system as a whole. Compromise usage efficiency, customizability, andfeaturerichness in favour of a system that is easy to use, no matter how advanced the underlying technology may be.

![](images/6a7e154ee5e19bfc37796995ee414bd47e670f04060f8bb14d94fb194f7442f7.jpg)

To convey a simple impression, try hiding complexhardwarefrom view—INVISIBLE HARDWARE (H14). To combine this initial impression with a rich set of available features, introduce themgradually upon user initiative INCREMENTAL REVEALING (H6). ...

H6 INCREMENTAL REVEALING\*\*  
![](images/3ed4b39f9758598f885ad9d735a2d49cec0f240f952e3db4db87b1e99cb556b3.jpg)  
Figure 4.22: Lists of files in the Mac $\mathrm { O S ^ { \otimes } }$ Finder.

…  you have sketched a design ofyour interface that conveys a simple impression—SIMPLEIMPRESSION (H5), yet your system has more complex features that you wish to offer in order to deliver its message—ATTRACT-ENGAGE-DELIVER(H1). Now you need to balance these two goals of simplicity and complexity.

##

Systems that look complex from the start do not invite users. However, if a systemdoes not offer enough complexity in its interaction possibilities, using it can quickly become boring.

WorldBeat (see appendix B) is structured into a short introductory screen, followed by a simple main selection screen with only names and icons of the main exhibit components (conducting,improvising, etc.)No lengthy texts overwhelm the user.But at this point, he has only scratched the surface of the exhibit. The overall wealth of features is presented in a gradual way: if the user moves the pointer towards one of the component icons, a short explanation appears (first revealing stage). Then, if he selects it, a separate page opens up that explains the component in more detail (second revealing stage), and lets the user try it out.

Most desktop operating systems, such as the Mac OS® shown in the opening picture, offer views onto the file and folder hierarchy thatinitially only show top-level items. Only when the user is interested in the contents of one of those objects does it unfold to reveal the next level of detail of the file hierarchy in this part.

## Therefore:

Initially, present only a very concise and simple overview of the system functionality. Only when users become active—showing that they are interested in a certain part ofthis overview-offer additional information aboutit, and gradually reveal what islying"behind" this introductory presentation.

![](images/a5fbc3fd170f939cb2d5ec8493e4975d56cfe4398e6a071117a2d646e0ffe8d3.jpg)  
Especially for information-oriented systems, a simple hierarchic structure to organize the revealing process is often useful—FLAT AND NARROW TREE (H7). To insert an additional revealing layer, and make the process more continuous, use temporary descriptions showing what the next revealing stage contains—DYNAMIC DESCRIPTOR (H15). ...

## H7 FLAT AND NARROW TREE \*

![](images/4e884df851b8916fe2fcef6f54db896b6241824412fb4236b84e0937078d2069.jpg)  
Figure 4.23: WorldBeat internal menu tree.

…. you have decided about the overall structure of the interaction, and found a way to unfold the initially simple appearance of your system into its full complexity over the course of the interaction—INCREMENTAL REVEALING (H6). Now you should think about the total size of this unfolding structure.

##

Many interactive exhibits consist of a number of "pages" through which the visitor can navigate. However, large information hierarchies, especially unorderednetworks with arbitrarylinks, quickly lead to disorientation.

WorldBeat, whose menu tree is shown in the opening picture, consists of a start page that explains briefly what the exhibit is about, andhow to use the batons, and then leads to a main selection screen where the user can choose one of the six WorldBeat components, go back to the start page, or read the credits for the system. The component pages in turn offer one or more choices to continue further into the respective component, or return to the main selection screen.

The Interactive Fugue exhibit has a similar overall structure. The initial selection page leads to four subpages for its various features, which in turn lead the user through a sequence of subsequent pages to use those features.

The hierarchical organizing principle is ubiquitous in electronic systems anduser interfaces. It is at the heart of the directory structure of the file system of all major operating systems, and replicated in their graphical "folder" view of the file system. It is also a general user interface pattern described by Tidwell [1998] as HIERARCHICAL SET.

If the hierarchy is kept small enough, the current position can be remembered well, and the navigation metaphor be used confidently, even by computer novices. A commonly quoted maximum capacity of human short-term memory and processing isaroundseven chunks of information [Miller, 1956], so this is both a good estimate for an upper limit on the number of entries from which the user can choose at each level. The maximum path length should be even shorter to avoid people forgetting where in the tree structure they are.

## Therefore:

Use a tree-like hierarchy to organize the content of your exhibit. Make the tree no more than 5 levels deep, and put no more than 7 branches into any node.

![](images/f2f3b38ab029e628d7207b7b74543c14c274e4764c8ae5cb41172ae7b12dad43.jpg)

Not all exhibits need to have this hierarchical layout. Systems that aim to convey one specific computersupported experience can use realistic navigation styles— AUGMENTED REALITY(H8). ...