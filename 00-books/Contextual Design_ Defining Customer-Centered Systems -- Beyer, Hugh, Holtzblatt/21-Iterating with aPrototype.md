# Iterating with a Prototype

19

he only reason for building a paper prototype is to support the conversation between user and designer about how to modify the proposed system to fit the user's work better. To do this well, the prototype must be easy to build, represent the user interface well enough to communicate it to a user, and be easy to modify in the field to support the design conversation. The process in Contextual Design is to validate the User Environment Design to ensure it's consistent; design a UI that represents the User Environment and mock it up in paper; interview customers using the paper mock-up in their own work context; interpret those interviews in the design team; make changes to User Environment Design and UI to respond to the issues; and repeat until the design stabilizes.

The original work on low-fidelity mock-ups was done at Aarhus University (Ehn and Kyng 1991). Since then, many others have modified the basic concepts to software (Muller 1991). Our approach builds on the concept of a low-fidelity prototype, but puts it in the context of a contextual interview in which the prototype can be tried out, discussed, and modified in partnership with the user.

## BUILDING A PAPER PROTOTYPE

Ease of building is a primary requirement of paper prototypes. Remember that part of the goal is to make it easy to try out design options with users; if it's too hard to build the prototype, people will be less willing to use them as design tools. Off-the-shelf stationery supplies, especially Post-its in all their varieties, are the basic components of a paper prototype (Figure 19.1).

![](images/905e1c641721388f73d8769b02c8f22bc4d2ffaba8089269fd4e7948995fd606.jpg)  
FIGuRE 19.1 A paper prototype for the configuration management windowing UI. The column headers and triangle to set sort order are on separate pieces of paper to suggest that they are clickable. The real UI might make them three-dimensional. The blank list will be filled in during the interview with configurations the user works with.

The key for a successful prototype is to put everything that might have to move during the interview on its own Post-it. This includes pull-down menus, buttons, and the objects of a direct manipulation interface. The interviewer will write in the content of the interface with the user's own data during the interview, so any example content should be on a removable sheet. The interviewer will take extra sheets to write the new contact on.

If the system mixes hardware and software, use other kinds of props in addition to the paper mock-up. Pens make good bar code scanners, pen boxes make good PDAs, and stationery boxes make good laptops.

Post-its on the laptop and PDA boxes represent their interfaces. Use these whenever the form factor of the physical device matters.

The final paper prototype represents the structure and the behavior of the proposed user interface. It's rough and handwritten, but legible—the user needs to be able to read it. The prototype should cover the whole system. Focus areas that aren't worked out yet are a blank Post-it with a title bar in the prototype. This gives enough structure to discuss the place with the user should it be wanted. Organize the paper so that all the parts for a win-

A good paper prototype is clean but looks like it can be changed

dow are together, with extra parts that appear on demand on a separate sheet. Put the windows in order of expected use, and you're ready for an interview.

## BUILDING A PAPER PROTOTYPE

The screen: Use a 9 × 12-inch sheet of card stock as the background to represent the screen. This gives you a slightly rigid base to the prototype, which is useful when manipulating the parts in the field. The slightly larger size gives you more flexibility in laying out a complex prototype.

Windows: Use an 8¹/2 × 11-inch sheet of paper or the largest size Post-it as a window. The larger size lets you lay out a more complex window but also occupies most of your card stock screen (much as real windows do). In the interview, watch for issues caused by multiple overlapping windows.

Decorate windows with a title bar and any permanent contents. Draw a menu bar and write in the names of pull-down menus. Draw scroll bars if any.

Pull-down menus: The name of the pull-down menu goes on the window because it's always visible. The contents of the menu go on a 2 × 3-inch Post-it. Write the name of the pull-down menu at the top. In the interview, keep the menu to one side, and put it on the window when the user clicks on it in the menu bar to simulate pulling it down. Any pull-right submenus go on their own Post-its—you'll pull them out when needed in the same way.

Tool palettes and button bars: If they are permanent, draw the space for them on the window but put each tool or button icon on its own Post-it (cut these small by hand). In the interview, you'll want to talk about what needs to go on the bar or palette, and having them on their own Post-its makes it easier to reconfigure them. It also makes them appear more manipulable and inviting to press.

If you're designing a floating palette, put the whole thing on its own 2 × 3-inch Post-it. Either draw the tools on it directly, or put them on their own small Post-its if you want to design exactly what goes on the palette.

Radio buttons, check boxes, controls: Draw right on the window.

Dialog boxes: Use smaller-sized Post-its for these—3 × 3-inch or 3 × 5-inch. Treat them just like windows, drawing on permanent content and using separate Post-its for things that may change.

Window contents: For most windows, the bulk of the contents will be the user's own data—the information she would expect to see if she were using the application in her own work. It's okay to fill in dummy data while building the prototype to work out what the screens will really look like, but take a blank version to the interview. When you're there, you'll tailor it to them.

Special techniques: The more interesting your design is, the more you'll want to extend these basic techniques to represent your design. Drag-and-drop is easy if you put the element you want to drag on its own Post-it, so the user can pick it up and move it. If you want to represent an overlay of information—like annotations on a document—cut overhead transparency film and draw and stick Post-its on it. If you're designing a tabbed interface, use Post-it flags to represent the tabs. Play with the medium. Anything that represents your intent and isn't too complicated to create or use is fair game.

## RUNNING A PROTOTYPE

## INTERVIEW

A paper prototype interview is very similar to a contextual interview in attitude, but very different logistically. The mechanics of handling the paper prototype make it a different kind of interview to run. But like a contextual interview, the attitude is one of inquiry, probing into the reasons for the user's actions and generating a sense of shared discovery, co-interpretation, and co-design. The same principles that guide Contextual Inquiry guide a prototyping interview.

## CONTEXT

In a contextual interview, you stay grounded by staying close to the ongoing actions and real past events of the user's work. You can't do real work in a paper prototype, but you can stay grounded in real events. Either replay a real past event, or alternate between doing a real task and replaying it in the prototype:

User: I like this "change" concept you have. Keeping all the parts of a logical change together is a big problem for us.

Designer: When was the last time you ran across that?

U: Just last week, when I was putting in a bug fix to our system.

D: Let's replay that situation in the prototype. What were the different parts of the system you had to change?

U: Well, there was the bug report; then there were two modules, PROA.C and PROB.C; and there was my description of the change that we're all required to do.

D: (writing furiously) Like this?

U： Right.

D: (putting the list on the prototype in the right place) Okay, let's do it.

The designer writes new data into the prototype to show the data associated with the real event. This keeps users interacting with the

prototype, either touching and changing it themselves or telling the designer how to manipulate it. Don't let users drift into generalities—if they start talking about what they would like in a system, pursue a real story to see how the changes would play

Follow a single case— don't do a demo

out. As they act out the story, invent fixes to the system to support them better. One design team working on a portable device drove around with their user. When she bought gas, she said, “"And now, I pay for it with this thing," and she pretended to plug it into the pump. Having the device in her hand, it was easy to invent new uses for it.

## PARTNERSHIP

The partnership between user and designer is around co-design of the prototype. As the user works with the prototype, both user and designer will discover problems. When the user raises problems or suggests different ways to do things, the designer modifies the prototype to represent the suggestion. The designer also gives design options to the user by suggesting several alternative solutions to a problem they’ve run into.

Users are never wrong: change the prototype to meet their expectations

There will often be points where the user's expectations don't match what the designer intended: "Oh, that change' thing lets me submit a

change proposal, right?" In such cases, always pursue the user's interpretation first: "Right, what do you think would happen?" Start co-designing this new possibility immediately. You're not committed to the design that you and the user come up with, but by exploring it you can find out what they are thinking.

You may discover a whole new issue or approach that you hadn't thought of before. You'll take the design you work out back and integrate it properly later—or at least the ideas underlying the design. Once you've explored this other avenue and come to a natural stopping point, you can return to the prototype you designed: "That was interesting. But remember back here, when you first saw this change' thing? Suppose I told you it kept the parts of a change you make together?" This is also the right way to handle the user's design ideas. If they are limited by their experience or skills—if everything they suggest is a tabbed dialog box or a menu—pursue their idea until you see what they are trying to get at. Then you can draw on your wider range of options to come up with cleaner or more inventive solutions. In this way, you'll see both what the user had in mind and, when you share them, his reaction to your ideas. You'll also give the users more technology ideas that they can incorporate and apply themselves.

## INTERPRETATION

When the user reacts to some aspect of the prototype or to the designer's ideas, the goal is to find out what they expected and why the pro-

Find out why a design does or doesn't work for the work totype or suggestion doesn't match. It's okay to discuss their ideas. It's important to understand what they want and why, not just the specific idea they propose (Figure 19.2).

User: This list of what's changed in this configuration isn't useful. I need to see the exact files, not just the developer's description attached to each change.

Designer: That tells you whether to trust the change?

<table><tr><td colspan="5">Aullify ioyitonatin</td></tr><tr><td>Litli</td><td>Crictor</td><td colspan="3">Dite</td></tr><tr><td>B 4.1 ltist</td><td></td><td colspan="3"></td></tr><tr><td>teclio Dwi i</td><td> Siith</td><td colspan="3">tui-</td></tr><tr><td>Chine feitiuri</td><td>frit Siulus</td><td>2twi-</td><td rowspan="4">Hadtue  — aut Si ous Marue =— ret Sun s</td><td rowspan="4">Cine ilTure thiuges</td></tr><tr><td>lue+2l</td><td>TuceDoi</td><td>1-tui6</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td rowspan="2"></td><td rowspan="2">Mhtue 5- Sue Faa</td></tr><tr><td></td><td colspan="2"></td></tr></table>

FiGuRE 19.2 A paper prototype of the "Qualify Configuration” focus area.

U: Right. If I'm surprised by what files they've touched, or if they've touched a couple of modules that are real complex, I know to be careful.

D: So how might you fix it?

U: Well, I don't know.. . Maybe double-click to see a list of contents?

D: That could work. Or we could give you a little triangle like Macintosh's finder. Click the triangle and see what's in the configuration. Or we could add an area to see contents and update it when you pass the mouse over a change—

U: I like that. That way I can scan up and down looking for who changed a particular module or get a fast look at everything that's changed. Let's do that.

D: You need to see exactly who changed what?

U: Oh yeah. Some of our modules are real rat's nests. If they weren't changed by the one or two people I trust, I'll be real careful of them.

In every case, you're looking to understand the structure of the user's work and how it matches the prototype, but you'll be talking in the language of the UI. So in this example, designer and user talk about "double-click" and the "little triangle." But the solution they settle on is the one that matches the work. The data the designer will take home is structuralthat what matters to the user when looking at a changed configuration is to see what changed and who changed it. The particular UI idea might work, or it might be replaced by a better way of seeing into a configuration. As long as the user's intent is met, the UI designer is free to think up a better mechanism.

It's important that you keep open to the user's reaction (verbal and nonverbal) and that you be willing to respond by changing the

prototype promptly. One designer took out a prototype with two alternative interfaces, one of which (her favorite) merged two focus areas in the User Environment Design and was based on a calendar. When that one was placed in front of the first user, she visibly recoiled and said, "Oh no, I don't want that—that's much too complicated." On another

project, one user was given an interface that simply didn't match what she was trying to do. She did her best to make it fit her job, but it wasn't until the designer created a new window (and new focus area, though the designer didn't say so) that the prototype started to click.

## Focus

As we discussed above, the User Environment Design represents the team's claim that this system will improve the user's work practice. The focus of a prototyping interview is to test that claim and fix the system when it's wrong.

Keeping to this focus is hard because it's easier for people to assimilate changes and see them as a minor adjustment than to recognize a challenge to the basic structure or assumptions of the system. It's important for the designer to be looking not for validation, but for the ways in which the system fails. Taking this attitude makes it more likely that designers will recognize a fundamental challenge.

The User Environment Design gives designers a way to listen that also makes it easier to break existing assumptions. With the User

Environment Design behind them, designers can tell whether a suggested change affects only the UI or whether it's really challenging the structure of the system. When the User Environment Design was created and when the prototype was reviewed, designers identified specific tests to check for during

Focus on testing structure irst: ignore pure UI problems

the interview (we'll discuss this more below). Where the team considered alternative designs, the prototype tests the chosen option; if the user has problems with it, the designer can design in the alternative on the fly and see if it fares better.

Finally, focus keeps the conversation on the right level of design. Early in the process the prototypes test structure, not the UI. If the user suggests changes to the UI—a new icon, a different word—the designer just writes them in. They don't need to be discussed—they aren't in the focus—but the user does need to be heard. Later, when the prototypes are intended to test the UI, the designer will discuss and suggest alternative UI mechanisms. The same is true if the entire focus of the project is to clean up an existing product's UI—the prototyping interviews will focus on UI issues from the beginning.

## THE STRUCTURE OF AN

## INTERVIEW

Interviewing around a paper prototype has very much the same structure as a normal contextual interview. The difference is that after the initial discussion, you move to working with the prototype.

## SETUP

Prototype interviews, like any Contextual Inquiry, need to be set up in advance so that everyone knows what to expect. Users can be people who the team has talked to already or entirely new users—it's usually best to do a mix. Interview two or three customers with a prototype, then review the feedback from them and redesign the prototype

Introduce the "Let's pretend" situation

before going out again. If you continue to bring in new users, the pool of customers interviewed over the course of the project will continue to grow. In this way, some large projects have worked with 50–100 users over the course of the project.

It's especially important to make sure a prototype interview is set up with the right roles and that they are doing the work the prototype supports. The user needs to have current or recent examples of doing the work that they can replay in the system, or there's no way to test the prototype with them. In setting up the interviews, find out what the users are doing, and make sure the work you care about is covered.

For the team, the designers who will interview need to be familiar with the User Environment Design and the paper prototypes. Review the prototype as a team and identify tests—issues that the prototype will test because of the way the prototype was designed. Perhaps the designer put lots of buttons and other interface components on the screen—then you'll find out if the user is prone to being overwhelmed. Perhaps the designer added a strong visual element that separates what should be one focus area into two—then you'll test whether dividing the focus area works. Whatever the issues are, note them along with the design choices you decided to test in developing the User Environment model. These will refine your focus for the interviews.

## INTRODUCTION

Start by introducing yourself and the focus of your design, including the kind of work the design supports. It's not necessary to describe the design itself at this point. You just want to start the user thinking about the kind of work you'll want him to do.

Then find out about the user, the work they do, and the particular tasks they have to do or have done recently. At this point you're looking for a hook to get you into the prototype. You're looking for all the different situations, current or in the recent past, that your system would support. You may not find one; it's possible that this person simply isn't doing the work you support right now. But that's rare if the interviews are well set up. Usually, you'll find a couple of situations that are good candidates for re-creating or doing for the first time in the prototype.

## TRANSITION

Once you've found a set of appropriate situations to re-create, choose one to start with and transition to the prototype interview. Bring out

the prototype and introduce it. Give a brief summary of the screen they start with: "Here's a window that lets you choose a configuration of the system to base your development on." Do not do a whole walkthrough of the window. As you introduce it,

Map new concepts to the user's experience and data

write in the specific data for the user—get the names of the configurations they might actually have seen given the work they've done. If they have no configuration management system, so they never created or named configurations explicitly, talk to them about how they have organized their development. Look for ways in which the configuration concept would have been useful to them, and agree on the configurations they would have created in their recent development. Name them, and write them into the prototype.

The amount of discussion needed to introduce the system depends on how much change you're introducing to the work: if it's small, you

can go right into the prototype; if large, you'll have to introduce your approach.“This product organizes the software development process by tracking the different modules, keeping developers from getting in each other's way, and making stable versions of the

Don't give a demo of the new system

whole system as the basis of development and for release. What's unique about it is that, instead of treating every modification to a file as independent, it treats all the modifications that accomplish a single fix or implement a single feature as one change." That would be sufficient to introduce the customer to what you’re building.

## THE INTERVIEW

Once you have the prototype out and ready, move the user into interacting with it. If you're reproducing a recent event, suggest that he do his work in the prototype, and you'll play CPU, making the system work like it should. Or get them to start interacting with the prototype by

Be the online help: one or two sentences only

Ground the interview by replaying specific events

inviting them to explore, describing what they see and what they think it will do. Change the mock-up as they run into problems: add and redesign parts to fit their needs. Give them a pen so they can modify parts of the prototype themselves. Some users will dive right into doing their work; others will want to poke around and explore the different parts of the system. Let them follow whichever style is natural for them.

If the user asks for an explanation of some part of the system, you can give them a one- or two-sentence description. This is an important place to listen for the "no." If you get a blank stare and have to keep elaborating on the explanation in hopes that they will get it, you have a concept that doesn't work. If your user can't figure out what a "configuration" is, or can't understand how they might use it to organize their development, it's too big a mismatch with their current practice to be useful. Adopting the system will require huge amounts of retraining.

Always run prototype interviews in pairs; it's too hard to try and manage the prototype, interact with the user, and keep notes at the same time. The notes of a prototype interview are critical to reconstructing it with the team later—it will be hard to recover the sequence of events from just the prototype, and an audiotape misses too much. It usually works best to assign one person to be notetaker while the other runs the interview and manipulates the prototype. It's usually not necessary to videotape the interview. Video can be critical if you are communicating back to a design team that is not going on their own customer interviews and doesn't really understand them. Video can also be critical if you are looking at problems in the detailed interaction with the UI. Otherwise, we've found the extra effort of videotaping gets in the way of rapid and frequent prototyping.

While running the interview, if you're replaying a past event, keep referring to that event to keep the interview grounded. Ask how the user would expect the system to respond, and when he says something you didn't expect, design on the fly, extending the design you have and pulling in parts from other focus areas when they're useful (Figure 19.3).

![](images/f3ae9e9130c3a6c4c8e31353c0d9c0036a7f2b0637b4c5c0661db57ee9aaed8b.jpg)  
FiGuRE 19.3 A paper prototype of the "Select Base Configuration" focus area.

User: Oh, I just used V5. That's the version the bug was reported against, so I started there.

D: Okay, here's our interface to let you specify the base configuration. What do you do?

U: I guess I type the name in here. (Indicates the text entry field)

D: Go ahead.

U: (Writes "V” with a pen on the field) Now what happens?

D: What would you expect?

U: Probably the list changes so it's just the configurations that begin with “V."

D: Oh. Okay, that's what happens.

U: (Writes “5”) There's only one “V5,"so now I hit the "Okay” button and I'm done.

D: Didn't you show me you also had a V5.1?

U: Oh yeah. Well, the exact match should show up first on the list and be selected, so I can still just press "Okay.

This isn't the design that was originally intended—the team didn't think about using the "name" field as a simple query filter—but it fits with the design. The user assumes an "Okay" button rather than pressing RETURN or "Select," and the designer doesn't bring it up that's a user interface question that isn't in her focus right now. This is an example of following a user's design to see where it goes. At this point the designer could back the user up and suggest the original design: "Suppose I told you that this is just a text entry field for choosing a configuration by name?" That would allow her to test the team's design after seeing what the user had in mind.

But the designer won't return to her team only with a UI tweak. What she's discovered challenges their User Environment Design:

## Use the UI conversation to see structural issues

should there be a “Find configuration"focus area separate from the “Select base configuration" focus area at all? The user's idea suggests that some level of quick query can and should be integrated right into "Select base configuration." Perhaps there's no need

for "Find configuration." It makes sense as a separate focus area only if querying is so complicated that just forming the query is a separate kind of work. Do users ever really need to form such complicated queries, especially if all they are doing is choosing one configuration to work with? So our designer moves the interview forward by discussing the need for real queries and probing for how this user specifies configurations——looking for cases when a simple search by name would not work. Because she is in the User Environment Design conversation with the team, it's easy to guide the interview to answer questions about structure.

## WRAP-UP

The final wrap-up of a prototype interview is a simple summary of the key points that came up during the interview. Summarize the points, and if it's useful, summarize any parts of the prototype you didn't get to for a quick reaction. But this won't be contextual data, so don't spend a lot of time on it. Finally, check the emotional aspect. Ask: Does he

like it? Would he buy or recommend buying it? How much would he pay for it? You're not looking for a real committed figure here. You're looking for à sense of how valuable they think the system really is and also the unarticulated expectations and threshold fig-

Check the sales point: do they love it?

ures that lie behind how they think about cost. You'll get a response that incorporates any excitement generated by the interview—by playing with and manipulating the design. In this way, the response is better grounded than you might get from a focus group or demo.

This is the general pattern of a prototype interview. If you're tracking an ongoing task rather than replaying an old one, the user will

alternate between doing some real work and then redoing it in the prototype, but otherwise the pattern is the same. Designer and user discuss the prototype, using the task to drive the conversation. From time to time they elaborate on some idea of the user's, then come back to the prototype as

Don't create scripts—let the user's real work be the script

designed. The designer uses her knowledge of the User Environment Design and technology to drive the interview. If you can recognize when the user is challenging some aspect of the User Environment Design, you can probe for details immediately, instead of having to wait for another interview.

Later in the design process, when you trust the structure in the prototype, concentrate more on the user interface and on enforcing the limits of a real system. When the user tries to do something the design doesn't allow, instead of taking it as an opportunity for codesign, act like a real CPU: beep at him. See if he can figure out how to make the system work given the limitations you're building in.

Follow the task the user is doing or re-creating until it's done or has moved beyond the scope covered by the prototype. Then choose another situation to follow that will exercise any parts of the prototype that haven't been touched yet. Usually, you won't get to all the parts of the prototype and that's okay; end the interview after two or three hours and save the rest of the prototype for the next user.