# CHAPTER 4 INTERACTION DESIGN

## OVERVIEW

4.1. Introduction

4.2. Designing what? Designing how?

4.3. Understanding users

4.4. Developing prototype designs

4.5. Evaluation

4.6. Iterative development

4.7. Multiple viewpoints

4.8. From interaction design to deployment

## KEY POINTS

■ Interaction design creates a plan specifying the user needs in terms of required functionality, how this functionality is to be accessed and controlled, the presentation of content, system state, help and feedback information, and the way the system is to integrate with other resources in the user’s context.

■ This plan is used by software engineers as they code the application. It should influence broadly – from data structure design to screen layout planning.

The process involves watching people in order to understand user needs, developing prototypes using design skills, guidelines and case studies, and being humble as these are evaluated and seen to fall short, and to need refining. Each of these activities will be carried out repeatedly.

■ Users should be involved at all stages of the process. Identifying representative users of the services can be more difficult than in desktop system development.

The interaction design team ideally should draw on a range of skill sets – computer science, marketing, graphic design, sociology and psychology are all important.

## 4.1 INTRODUCTION

Most of the approaches we’ve reviewed up to now are really focused on making things. A helpful view of the interaction design process is that it’s about making sense of things (Dykstra-Erickson et al., 2001). As we have seen, products ‘make sense’ to users when they do something useful, do it in harmony with the rest of the things in the user’s life and have a well-articulated, strong identity.

The purpose of this chapter is to give an overview of the processes involved in interaction design, drawing out the common types of approach and technique. If you are already an interaction designer, some of what we say will be familiar, but do read on as there are additional considerations and strategies in the mobile context that we highlight. If you are new to the field, what follows is a nutshell description of the entire interaction design discipline, showing you how things fit together and relate to the wider development process. In the three chapters that follow, we will look in much more detail at how you might successfully deploy an interaction design process in mobile development; look out for pointers in this chapter to further details in the book.

## 4.2 DESIGNING WHAT? DESIGNING HOW?

What is this ‘interaction’ that’s being designed? Well, it’s not purely something the technology ‘does’ – the interactive facilities the device or service provides. Nor is interaction just a property of the people who use it – the ways they react to or perceive the system. Rather, it’s about the relationship between the technology and users in the wide context that they are placed within.

In working towards an effective interaction design, you will be involved in three main types of activity:

Understanding users – having a sense of people’s capabilities and limitations; gaining a rich picture of what makes up the detail of their lives, the things they do and use.

Developing prototype designs – representing a proposed interaction design in such a way that it can be demonstrated, altered and discussed.

Evaluation – each prototype is a stepping stone to the next, better, refined design. Evaluation techniques identify the strengths and weaknesses of a design but can also lead the team to propose a completely different approach, discarding the current line of design thinking for a radical approach.

Clearly, there are many variations on these general phases (see, for example, Preece et al., 2002). In the later chapters that look at the activities in detail, we will concentrate on the issues, approaches and case study examples that are most illuminating to the mobile context.

Each of these activities may well draw on some of the techniques touched on in the previous chapter. So in understanding users, you might consider using an emerging technology to provoke responses about future needs, and a starting point for new concept prototypes could be previously successful services.

Interaction design, though, is distinguished in two ways from other development methods. Firstly, in terms of the breadth of its vision: as we’ve said, it’s not just about the technology or people, but about building infrastructure that will improve the way life is experienced and lived. Secondly, coming back down to earth, in order to live up to this ideal it’s also about being completely grounded and guided by an understanding of the impact of design choices on people who will end up using the systems.

Unlike some of the other strategies, interaction design is also intensively participative and collaborative. That is, you will work with many different stakeholders – engineers, industrial designers and, crucially, representatives of the user community – all throughout the project.

It’s also an evolutionary process – ideas will come, fail and fade, and be replaced by better and better proposals. You will learn that one design is never enough, and failing is a constructive rather than a destructive experience.

## BOX 4.1

## INTERACTION DESIGN DEFINED

At first glance, ‘interaction design’ might appear to be a modern, web-age replacement term for more familiar, decades-old terms such as ‘usability engineering’ and ‘human–computer interaction’. In fact, though, it has been in use for quite some time – IDEO designers used it in a 1995 article, describing activities that had been going on for 10 years (Spreenberg et al., 1995) – and it has a distinct set of concerns.

Giving a short, pithy definition of interaction design, though, is not easy. It’s been used to describe activities involved in creating things from e-commerce websites to GPS navigators, and by people who come from a range of backgrounds including the arts, industrial design and marketing.

Jenny Preece, Yvonne Rodgers and Helen Sharp, in a textbook on the subject, define it this way:

... designing interactive products to support people in their everyday and working lives. (Preece et al., 2002, p. 6)

Two key words in their definition are ‘products’ and ‘everyday’. ‘Products’ reminds us that in many cases, the goal is to get consumers to buy the results – interaction designers do not just work on in-house, corporate core systems where the end-users have little choice but to take what they are given. ‘Everyday’ further emphasizes the broad remit – the products that designers envision will assist people to do all sorts of things that are important to them, like shop, care for their health, further educate themselves and pass leisure hours in pursuing a hobby.

For outsiders, and people starting to learn about interaction design, the danger is to see the activity as one concerned only with providing a ‘skin’ to the product – an activity performed only after the more important work of coding which constructs the skeleton and guts of a system. But, while apologizing for repeating ourselves, we stress that interaction design does not equal interface design. Interface design is about the ‘statics’ – screen layout, how you communicate content and system control information – like the scenery in a play. Do interaction designers need to address these things? ➤

Absolutely, but they come later. What’s important upfront are the dynamics – first understanding the key needs of the user and then constructing the way the system cooperates with the user.

Continuing the play metaphor, interaction design is about the acting on the stage, how one scene moves to the next, the relationships between the central characters and the themes the playwright is trying to communicate. Shakespeare, in As You Like It, wrote: ‘‘All the world’s a stage, And all the men and women merely players.’’ It’s not too fanciful to suggest that the job of an interaction designer is to create places for people to play out their lives (remembering to ensure these places and lives reflect reality and not fantasy); or, as Terry Winograd eloquently puts it, interaction design is about the construction of ‘‘the ‘interspace’ in which people live, rather than an ‘interface’ with which they interact’’ (Winograd, 1997). ■

## 4.3 UNDERSTANDING USERS

Anything you can learn about your users will help you produce better designs. Some of the knowledge you need is already out there – biologists, psychologists, sociologists and anthropologists have carried out many experiments and field studies, providing useful insights into what humans can do and cope with. We’ll be bringing together some of the most important findings specifically for mobiles in several of the chapters that follow. You’ll also need to go and carry out your own first-hand investigations, doing field studies, running focus groups, and performing interviews. (Chapter 5 explores the range of approaches in detail.)

## 4.3.1 FROM BIOLOGY TO PSYCHOLOGY

A few years ago, a UK private healthcare organization ran a TV advert detailing some of the incredible complexities and abilities of a human body: the number of times the heart beats in a lifetime, the number of neuron connections in the brain, the reaction times in danger. The advert ended with the slogan ‘you are amazing’.

Developing a design attitude that considers users as ‘amazing’ is much healthier than some of the ideas that have tended to dominate interactive technology developments in the past: users have been seen at best as simple folk who need things to be made ‘friendly’ or ‘easy’; at worst as characters full of ‘weaknesses’, like vagueness, illogicality and emotion (Norman, 1994).

If you know what makes people ‘amazing’, even at the basic biological level, your mobile design choices can be better informed. Developers of the tactile interfaces we encountered in Chapter 1, for example, are exploiting the human skin’s ability to perceive very rapid stimulations.

You also need to get beneath the skin, understanding what goes on inside your user’s head when they interact. This sort of knowledge comes from cognitive psychology, a science focused on mapping out how humans process and respond to the world. Cognitive psychologists have developed theories addressing lots of aspects relevant to system design, like visual processing, human memory and learning.

Let’s consider, as an example, knowledge of human short-term or working memory. This memory is the mental piece of scrap paper we use as we complete our goals. Experiments have shown that this memory is small – it can store something of the order of five to seven chunks of information – and it rapidly decays.

While such facts are interesting in themselves, how are they relevant to an interaction designer? Such insights can be particularly helpful when making specific design choices at a detailed level. So, if you didn’t appreciate the limitations of short-term memory, you might produce a design that overloads the user; when this happens, people make mistakes. Take menu-based voice interfaces for telephone systems, in which a remote system speaks a series of options and the user responds with key presses. If you give users too much to think about, in terms of either the number of options or the process of selection (‘‘press 1 to forward, 9 to delete, 3 to play, . . .’’), they will forget choices and make incorrect selections.

## EXERCISE 4.1

## DESIGN FOR THE ELDERLY

In many of the main markets for mobiles, populations are aging with life expectancy increasing. While the current generation of older people might not be attracted by advanced mobile services, future older users (including you!) who have grown up with the technology might be an important segment of the market. However, little work has yet been done on design for this group.

What distinct attributes should be accommodated when designing for this group?

Take a mobile interface you are familiar with (e.g. the main options menu on your phone) and critique its design with respect to the needs of older users. Then, show the interface to an elderly person and ask them to comment on it. Compare their remarks with your critique.

Comments: you should consider both physical and cognitive attributes. For example, vision might be impaired, dexterity reduced, and memory less able. There are also issues relating to leisure time (this group has more), disposable income (usually less, though in some cases considerably more), and key concerns (family, status quo, health and security, for instance). ■

## 4.3.2 FIELD STUDIES

Understanding general human characteristics is important, but getting to know your particular group of users is vital. To do this, you can use a set of techniques to observe and probe the people and situations of interest.

In human-watching terms, no-one gets closer to the action than an anthropologist. Being an anthropologist is about being completely immersed in a community, often spending a large amount of time with the group being studied. The aim is to document the detail of the way the group is organized, relates and develops.

For interaction design, a branch of anthropology called ethnography has been gaining prominence for some time; initially the techniques were used to study complex work practices like air traffic control, but they are highly applicable to mobile design.

The anthropologist has become a must-have employee of many companies:

. . . corporate anthropology is now mainstream, particularly among technology firms. Indeed, when he was informed that IBM Research had hired Ms Blomberg as its first anthropologist in December 2002, Paul Saffo of the Institute for the Future exclaimed ‘‘Just now? How embarrassing.’’ (Economist, 2004a)

Ethnographic methods focus on producing an account of what is going on in real situations by observing the moment-by-moment behavior of people interacting with others and their environment over extended periods of time. The ethnographer collects first-hand, eyewitness evidence of how people do their work or leisure in the actual setting, rather than in artificial environments such as a laboratory or focus-group interview room.

Just how immersed and intense studies can get is highlighted by Allison Woodruff and Paul Aoki’s report on their study into the use of push-to-talk mobile phones (Woodruff and Aoki, 2003). Woodruff lived with four of the participants and joined them in many of their social and work activities for a week. She eavesdropped on conversations (audible through the phones’ loudspeakers), recorded over 50 hours of conversations and ended up with a corpus of over 70 000 words of dialog between the participants.

Such intense effort is immensely rewarding. After a period of observation, you come back full of anecdotes and an overview of the field setting. You’ll have many ‘a-ha’ moments when things suddenly make sense. You can also give some authentic reactions to design proposals the team generates; you know what it’s like to be the user (Button and Dourish, 1996).

One way to understand the ethnographic process, and the way it links into the bigger design process, is to think of front-line war reporters and studio news anchor people. The ethnographer is the war reporter; the design team members, back at home, are the news anchors.

Reporters have to respond to spontaneous ‘live’ questioning by news anchors, but they also need to be able to step back and provide a considered overview of the situation for viewers. So, the ethnographer’s job is to portray the action in a vividly colorful way both in responding to design team questions and by providing an account resulting from careful reflection.

As Button and Dourish note, the activity is less one of data collection and more of a writing-up, presenting descriptions and explanations of what was observed. As an interaction designer you will be well aware of the need to involve the user, but relying only on their subjective rationalizations of their behavior probably won’t give a full account of the situation. The explanations they offer might well be influenced by what they think you want to hear, or what they would like to believe about themselves. Your job, then, is to provide objectivity out of subjectivity. You will be fully involved with people, watching them, talking to them, looking at the documents and other artifacts they use, meanwhile stepping back and asking ‘‘what does all this action mean?’’.

While ethnography is a core, field-study activity, as we will see in the next chapter there are other in-situ methods you can use.