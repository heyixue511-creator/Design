# CHAPTER 7 EVALUATION

## OVERVIEW

7.1. Introduction

7.2. Classifying evaluation

7.3. ‘Quick And Dirty’

7.4. Conceptual model extraction

7.5. Direct observation

7.6. Interviews

7.7. Questionnaires

7.8. Non-user methods

7.9. Experimental evaluation

7.10. Considering context – evaluating mobile systems

7.11. Complementary evaluation

7.12. Conclusion

## KEY POINTS

■ Evaluation is an essential part of the design process.

■ Choosing the correct evaluation technique depends on the type of results required, user availability and equipment availability.

■ As they can be used in different contexts, evaluating mobile systems is more complicated than evaluating desktop-based systems.

■ At present, methods for the effective evaluation of mobile systems are an open question but a mixture of laboratory and context trials is recommended.

## 7.1 INTRODUCTION

Evaluation is about humility. No matter how good you think your design ideas are, there will always be something you didn’t consider – users are just so ingenious at doing what you didn’t expect them to do (see Figure 7.1).

![](images/46619e039daf4fad3bb7a66ef8ed355e318d3c2227a8a3eb8cda59b7325e22f5.jpg)  
FIGURE 7.1  
Users doing the unexpected with technology

Within the field of human–computer interaction there exist many approaches to evaluating systems. Mostly, these have been adapted from social science and psychology to fit the constraints of a technology development process – we have already discussed ethnography, a technique adapted from sociology and social anthropology. In this chapter we will look at other techniques, paying particular attention to how they may be applied in the mobile context.

There are many excellent books looking at different evaluation techniques. One of the most comprehensive is Interaction Design (Preece et al., 2002), which also covers the more practical aspects of applying the techniques and their relative strengths and weaknesses. However, we’re not interested in studying evaluation for its own sake. Instead we shall look at how evaluation can be applied in the design process.

Furthermore, the evaluation of mobile systems is different from that of desktop computers. We shall examine why mobile systems are different and which desktop evaluation techniques apply in the mobile context.

## 7.2 CLASSIFYING EVALUATION

It is important to evaluate your work as soon, and as often, as constraints allow. In Chapter 5 we looked at ethnographic techniques, some of which are designed to evaluate design ideas by observing real users in a real context. In this chapter, we are interested in evaluating actual designs, rather than design ideas. To evaluate actual designs, we need the design to be available in some concrete form – the prototypes discussed in the previous chapter. This chapter will therefore follow the structure of the last, starting out with how to evaluate low-fidelity prototypes and ending up with conducting scientifically rigorous evaluations of high-fidelity prototypes.

Besides the fidelity of the prototype involved in the evaluation, there are other factors to consider when selecting an evaluation technique:

On whom? You might think that all evaluations will require the participation of the end-users; this is not so. Sometimes evaluation will not involve users at all and may be conducted by usability experts instead. Alternatively, you may not be able to recruit actual end-users and simply use a surrogate end-user.

Where? Again, many evaluations take place in a controlled laboratory environment, but this is not so common with mobile systems. Sometimes evaluations will take place in a user’s place of work, or even in an outdoor context.

Results. Different evaluation types will inform the design process in different ways. This can range from purely anecdotal descriptions to help form initial ideas, through to complex statistical analysis giving quantitative proof of how good a system is.

To aid your decision on which is most appropriate, each evaluation technique we present will be described in terms of the dimensions listed above.

## 7.3 ‘QUICK AND DIRTY’

Conducted by: End-users

Equipment: Low-fidelity prototype

Results: Anecdotal and unstructured

Where: Informal setting

The first evaluations you will conduct are on the initial design ideas themselves. As such, the goal is to get rapid, broad-brush feedback on the design, rather than painstakingly explore a design space. This type of evaluation is essentially a form of ethnography, which goes under the unfortunate name ‘Quick and Dirty’ (Hughes et al., 1995). This is to distinguish it from the more formal types of ethnography discussed in Chapter 5.

To conduct this type of evaluation, you should meet with end-users informally and simply ask them what they think of the design. Show them the prototype and jot down any ideas or concerns they have. In our research, we talk about this type of evaluation as a brain-damage check – in design meetings we can get carried away and this type of rapid user test makes sure that our ideas are sensible and relevant.

## 7.4 CONCEPTUAL MODEL EXTRACTION

Conducted by: End-users Equipment: An interface sketch Results: Qualitative Where: Controlled setting

Mobile computing opens the opportunity to develop entirely new types of application for which users will have no precedent. This is daunting to the interface designer, as it is not possible to exploit familiar metaphors and ideas which the user may be comfortable with already. The goal of this technique is to extract how users interpret a completely new interface, given their existing mental models of how interfaces should work.

For example, when developing the first digital cameras for HP, Dray & Associates had to conduct considerable conceptual model extractions, as most consumers had no idea what a digital camera could do. They used low-fidelity prototypes of the screen on the camera and asked users what they thought the symbols were for. Most were clear, apart from the icon in Figure 7.2(a) – one person suggested it was a mode for taking pictures of skyscrapers! It was, of course, the icon to show how many pictures had been taken (placed on a stack). Eventually, the design team struck upon the idea of having a ‘messy stack’ as seen in Figure 7.2(b). It was soon discovered that the new symbol unambiguously triggered the correct mental model of a stack of photographs.

![](images/aba94322ac4290d53867ce566a404616f6218f132bd6fc4f7b2814944ebf0747.jpg)  
FIGURE 7.2  
Conceptual model extraction for digital camera icons

## EXERCISE 7.1

## CONCEPTUAL MODEL EXTRACTION

It’s interesting to see how something that is abundantly obvious to you can confuse others. Take an iconic menu you are familiar with, perhaps the root menu on your cellular handset. (If you don’t have access to such a menu, use one of the images of menus in Chapter 8.) Print or photograph that menu and show it to someone not familiar with the interface. Explain where the menu is taken from and have them explain the meaning of each icon on the screen. Chances are they will not be able to interpret them first time off.

Just as an aside, our research group often debates the worth of a conceptual model extraction. The argument against it is that understanding a symbol or icon is not so important, as once the association is learnt, it doesn’t really matter what symbol is used. Do you think this is a valid argument? ■

## 7.5 DIRECT OBSERVATION

Conducted by: End-users

Equipment: An interactive prototype

Results: Qualitative

Where: Controlled setting

Another way to evaluate an interface is to watch people using it. This is hardly a stunning insight, but it turns out to be trickier than might be suspected. To illustrate this point, imagine the following situation:

You sit the user down with the prototype, asking them to complete some task to see how they perform. The user starts by clicking on what looks to you to be a random sequence of buttons, but seems to make perfect sense to the user. You become agitated (‘‘What is this person thinking?’’). You start to think about how to change the interface and are startled by a sudden noise as the computer crashes. What happened? How did the user do that? You were so lost in thought you didn’t notice what happened. Now you are angry with yourself and the user for crashing your prototype. The user reacts badly and loses self-confidence. When the prototype restarts, the user is loath to click anything and defers to you, asking what they should do next. Eventually the session is abandoned as a failure.

This is clearly a pathological example, but illustrates some key points that need to be addressed in any observation, namely:

How to find out what the user is thinking without interrupting their flow

How to record observations

How to stop yourself biasing the evaluation

How to make sure that the user has a pleasant experience and does not feel that they are little better than a lab rat.

## 7.5.1 FINDING OUT WHAT USERS ARE THINKING

Essentially we want the users to verbalize what they are thinking as they complete the tasks. One solution to this might be to ask the user to speak aloud what they are thinking throughout the period of the evaluation. This technique is called think-aloud and was developed by Erikson and Simon (1985). Unfortunately, there are two key problems with speaking aloud in this way: firstly, it’s embarrassing, and secondly, most people forget to speak after a while.

## BOX 7.1

## THINKING ALOUD

To have some idea of just how hard it is to ‘think aloud’, try this experiment. The next time you drive your car, speak aloud the driving decisions and maneuvers you’re ➤ making as if to a driving instructor in the seat beside you. (You may have done this already, since the technique is common to many driving examinations throughout the world.) As you start to speak, you’re very self-conscious. It’s embarrassing to be telling the world these mundane thoughts. (Thankfully, due to the advent of cellular phones, you can reduce the embarrassment by placing some headphones in your ears, whereupon other drivers will think you’re talking on a hands-free kit.) Then, after a while, you will simply forget to speak. Something will happen, something that requires your full attention, and when you’ve finished dealing with that, you will default to your natural behavior and forget to speak out loud. ■

To overcome these problems, a form of think-aloud called constructive interaction has been developed (Nielsen and Mack, 1994). In this instance, two users work through the task at the computer simultaneously. As they need to communicate their ideas with each other, talking about what they are thinking becomes a perfectly natural task. A variation on this technique replaces one of the real users with a trained facilitator who continually challenges the real user, asking them to explain their actions more fully. This variant, however, leaves the evaluation open to biasing by the facilitator, and it is probably safer to stick with two real users.

## 7.5.2 HOW TO RECORD OBSERVATIONS

Really, the first question to ask yourself is not how, but what – what is it you want recorded? Is it important to see the user’s face or would audio alone suffice? Perhaps you are watching for a very specific event, in which case is it sufficient to keep a simple tally? In most circumstances, observers opt for video almost by default.

## Reasons for Video

The main reason to take a video recording is not so much to capture the user’s face, but rather to capture what they are doing on screen. Often the user is interacting with the software too rapidly to understand their actions during the experiment session. Recording the output from the screen allows you to go back and analyze what happened after the event. The screen analysis can be augmented by an audio recording of what the user is saying (assuming you are employing some think-aloud protocol) or possibly by a recording of the user’s face to give some indication of their emotional state.

In our research group, we have a portable system which allows us to record the output from the screen (via a gizmo called a scan converter) and the user’s face (using a standard camcorder). These two signals are then mixed together (using a mixer with picture-in-picture capability as in Figure 7.3) so that they can be viewed simultaneously.

While some evaluations will require this type of observation, we would urge you to avoid it if possible. Watching hours of video containing nothing but mouse movements rapidly becomes very tedious. Instead of recording events from the video after the fact, decide beforehand what type of events you wish to monitor and take note of these during the experiment – see the section below on coding sheets. This is not to say that video recording should be disregarded altogether. For instance, selected parts of the video can still be used to help jog the user’s memory in any subsequent interviews, or to show interesting findings to the rest of the design team.

![](images/2e96318dcad2e04f3ec5bfb068022a4ba8840838056f7ed5dde8bc2b5ccc5375.jpg)  
FIGURE 7.3  
Left: the researcher looking for events from a mixture of signals incorporating (on the right) the mobile device screen and the video camera

## Note Taking

A much less technical approach to recording events in an observational experiment is to use a pen and paper to take notes. Note taking in its simplest form consists of writing a description of what is happening as it happens. The major drawback of this method is that the observer must take their eye off the subject in order to record the event, and may miss something while writing. One may overcome this problem through training to write without looking at the paper, but it still may not be possible to write quickly enough to record every event. Alternatively, you can have a team of people making records which can be correlated at the end of the session. This solution is expensive, however, in terms of paying observers and also in time spent in correlating results. Fortunately this type of note taking is only really needed for pure ethnographic observations, where the observers have no idea of what they are looking for and it is only after the observations have finished that it becomes clear what the important events are. For most evaluations, the researchers have some idea of what they are looking for before the observations occur. For example, one might be interested in how many times users need to refer to the help system. To record this, the observer need only make a tick for each occurrence. Usually, observers are watching for more than one event, so they draw up a coding sheet which consists of a number of columns, where one column represents each event they are watching for. Observers can then place ticks in the relevant column, or write down the time when each event occurred. A typical coding sheet is shown in Figure 7.4. If you are going to do some observations, then it is still worth learning how to write without looking at a page as, no matter how good your coding sheet is, users are bound to do something unforeseen which you wish to record.

Recently, software versions of coding sheets have become available for PDAs. Observers can configure the software before the experiments start, where the PDA screen shows one button per target event. When the event occurs, the observer taps the button and the PDA records the event, along with the time when it occurred. At the end of the experiment, the results can be automatically uploaded to a PC for the data analysis phase. The only downside to using a PDA is that it’s difficult to make unstructured notes – it’s probably easier to bring a sheet of paper along with the PDA rather than trying to train yourself to be able to enter text reliably on a PDA without looking at the screen.

<table><tr><td rowspan=1 colspan=1>Time H</td><td rowspan=1 colspan=1>elp button |</td><td rowspan=1 colspan=1>Ask for help</td><td rowspan=1 colspan=1>Undo |</td><td rowspan=1 colspan=1>Apply to all</td><td rowspan=1 colspan=1>Check design decision</td><td rowspan=1 colspan=1>Open new editor</td></tr><tr><td rowspan=1 colspan=1>0:00</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0:01</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>_</td></tr><tr><td rowspan=1 colspan=1>0:02</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0:03</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0:04</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0:05</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0:06</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0:07</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0:08</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0:09</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0:10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0:11</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0:12</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

FIGURE 7.4  
Coding sheet for usage of a graph editor

## Automatic Logging

The best option of all is to have the prototype automatically log all interaction by the user. This way, your work during the experiment is greatly reduced and there is less chance of your inadvertently biasing the experiment (see the next section). Obviously this will only work on a hardware prototype capable of recording the interaction. This was certainly an issue for us in conducting some of our evaluation on rich media browsing (see Chapter 10) as we were pushing the computing resources of the PDA to the very limit. The time taken for the device to update the log file was too much of an overhead.

Assuming that the hardware is up to the task, some thought should be given to which events you are interested in recording. If you have access to the source code of the software you are evaluating, then it becomes possible to create a customized log containing just those events you are interested in. Thinking about our earlier example of recording when the help system is accessed; we could modify the code for the ‘Help’ button so that it wrote a time value to a log file on the computer. If you do not have access to source, then the next best solution is to run some form of spyware which records every event the user generates. Just as with observing on paper, having the computer record every event means that a lot of time is wasted at the end of the experiment sifting out the relevant information. (Actually, there are specialist pieces of software such as Theme – http://www.patternvision.com/ – which use AI (Artificial Intelligence) techniques to spot patterns in observational data and help point out correlated events. It is our opinion, however, that this type of software should only be used as a last resort, as it is not always easy to detect which correlations are relevant to the experiment and which are not.)

## Integrating Note Taking

To aid in the results analysis phase of an experiment, there is software available to synchronize the recorded notes with the video of the screen and user. This greatly reduces the effort of reconciling data from a number of sources. If the notes are to be integrated, then they must obviously be captured or translated to digital format. As early as 1989, Wendy Mackay described a system called EVA (Mackay, 1989) which allowed users to view a video feed and annotate it with notes – observers created a button for each event type they were interested in before observation started, and then clicked the relevant button during evaluation. More recent systems, such as the Observer from Noldus, allow the integration of data, including notations taken on PDAs.

## 7.5.3 HOW TO NOT BIAS THE EXPERIMENT

Despite the supposed dispassionate nature of scientific research, we’re all human and keen to see our designs succeed. Users also try to produce the result they believe the experimenters are looking for – this ranges from mild forms, such as the Halo Effect (Thorndike, 1920), through to the alarming results of Milgram (1974), where subjects willingly electrocuted people at the request of the experimenter. (Don’t worry – the experiment was designed to see how far subjects would go in obeying an authority figure when taking part in an experiment. The person being electrocuted was actually an actor and the subjects were asked to apply increasing amounts of current. The experiment measured when people would stop administering the current.)

You could attempt to hide your feelings and make sure you presented the evaluation in such a way as to give no clue about what is expected of the user. Even better, one could hire a dispassionate facilitator to run the evaluation in your stead. However, even if we do manage to completely mask our feelings, or use a dispassionate facilitator, the mere act of observation changes subjects behavior. This was first discovered as part of an experiment at the Hawthorne Plant of the Western Electric Company which was keen to investigate the effects of employee productivity in an office where the environmental factors were altered – different lighting, humidity levels, etc., were tested. The puzzling thing was that no matter how the environmental factors were altered, productivity improved. After some investigation, the team discovered that the subjects had become dispirited in their work and perceived themselves as unimportant to the company. However, the researchers interest in their work gave them the perception that their work was important, so their productivity increased!

Therefore, when conducting an observation, one should withdraw from the subject as far as possible, but not so far that is no longer possible to make worthwhile observations. If expenses allow, camcorders and scan converters can be used to facilitate remote observation. In fact, one need not go to that much expense. We have conducted remote observation experiments using a monitor splitter lead (this attaches at the back of the PC and drives two monitors simultaneously) and a microphone on a very long lead.

## 7.5.4 HAPPY USERS

Most people react negatively to being observed – they become self-conscious and lose confidence.   
This is clearly undesirable.

Before inviting anyone to take part in an observation, it should be made abundantly clear that it is the system you are testing and not their performance. You should explain what will happen, what will be expected of the user and how much time it will take. Only then should you ask them to take part. If the user is willing, it is a good idea to draw up a participant consent form. Ours is based on that used by Dray & Associates (Dray, 2001) and contains the following headings:

Purpose of study. What you are doing and why.

Information you will collect. Explaining what will be recorded and, most importantly, what will happen to that information afterwards – users would be upset to see some of their more hapless moments recorded on video and made freely available on the Internet. You could state that you may use anonymized video or audio to show to your manager or display at a technical conference.

Non-disclosure. The system you are asking the user to interact with may be commercially sensitive and require protection.

Freedom to withdraw. Allow people to pull out or request a break at any time.

Questions. State that the user may ask questions at any time.

Payment. Normally users are paid for participation of this nature. The amount is up to you, but you should tell them explicitly up-front what this amount will be.

With reference to the problem of user-biasing discussed above, there are issues around how much should be revealed to the subjects about the true nature of the experiment. Quoting Milgram’s experiment again (Milgram, 1974), his results would obviously have been meaningless had he told the subjects that they were not actually electrocuting the actor. However, are the results from this work worth the emotional trauma experienced by the subjects? A more recent example from mobile computing is reported in Jakob Nielsen’s Alertbox column (Nielsen, 2004). In this instance, researchers were keen to see why mobile phones were so annoying. They had two actors hold a conversation in a place such as a restaurant or train station, after which researchers interviewed bystanders to see whether they were annoyed. The experimenters then repeated the process, but this time using only one actor speaking their half of the original conversation into a cellular handset. The researchers discovered that hearing half a conversation is more annoying than hearing a full conversation but, again, was this result worth inconveniencing the bystanders?

Most universities and research institutions have an ethics committee which determines whether the value of an experiment’s results outweigh the inconvenience to the subjects. This approach started in medical faculties where the issue is, literally, life and death, but is now accepted practice with any group conducting experiments on people. So before you rush headlong into user evaluations, check whether the institution you study at or work for has such a policy.

## 7.6 INTERVIEWS

Conducted by: End-users

Equipment: An interactive prototype

Results: Qualitative

Where: Controlled setting

Interviewing is a common technique for getting users to reflect on their experience in their own words. This can be less expensive than ethnographic observation, as the design team need only record and review a few hours’ worth of interview material as opposed to what could be days’ worth of recorded observations. As with other forms of evaluation which require direct interaction with the user, the value of the session depends a lot on the quality of the interviewer. A good interviewer will be able to put the interviewee at ease, let them express their point of view without being influenced, and be able to detect and follow up on any interesting points made in the course of conversation. Furthermore, a good interviewer can build trusted relationships with the subjects, thus easing the way to conduct further interviews. Whilst experienced interviewers will naturally direct the questioning to pursue the most interesting issues, it may be worth creating a script of questions for those interviewers with less experience.

Conducting interviews as an alternative to observation can lead to information being missed. People are fantastically bad at explaining and deconstructing how they achieve a given task. Tasks that are repeated frequently are chunked together and become secondary to the user, but may prove vital for a system designer. (Think of changing gear in a manual car. When you started driving, you had to think about the clutch, accelerator and gearshift separately, requiring a lot of concentration. Once you had learned to drive, gear changing became a single action, allowing you to do it while changing radio channels and chatting to a passenger.)

From our experience, interviews have greatest value when conducted in conjunction with some form of observation, either ethnographic or laboratory based. Often in observation you will see the subject perform some action which seems incredibly strange to you, but makes perfect sense to them. Asking the users about that incident can lead to very interesting insights into where their mental model diverges from yours – see Box 7.2.

## BOX 7.2

## ‘THE LONG WAY ROUND’

When conducting the experiments for the new menu interface described in Chapter 8, one user ignored the rapid access system of the new handset completely and simply scrolled to the desired function using the down arrow. In one instance this took 74 key presses! (As we were using key presses as a metric to evaluate the efficacy of the new system, this was very worrying.) At the end of the experiment, we interviewed the user and asked why they had adopted this strategy when it was clearly slower than using the numeric keys. He replied that using the down arrow he did not have to think about what key to press next – although slower in terms of key presses it was guaranteed to arrive at the desired option (eventually). Relying solely on the video recording of the session, we would never have had this insight. ■

## 7.7 QUESTIONNAIRES

Conducted by: End-users

Equipment: An interactive prototype & questionnaire

Results: Qualitative & Quantitative

Where: Anywhere

Another popular technique for garnering user opinion is the questionnaire. This technique is popular as it has the potential to reach a very wide audience, is cheap to administer and can be analyzed rapidly. Of course, it can never be as flexible as an interview and requires a lot of effort to design, especially if the user is completing it with no external help. Designing a good questionnaire is a complicated process, especially if the results are to be reliable.

There are a number of standard questionnaires for conducting interface evaluations. One of the most popular is QUIS – Questionnaire for User Interaction Satisfaction (http://www.lap. umd.edu/QUIS/) – developed and refined by the Human–Computer Interaction Lab at the University of Maryland. Many more can be found at Gary Perlman’s site (http://www.acm.org/ perlman/question.html) (Perlman, 1998), but none are designed specifically for evaluating mobile systems. This almost begs mobile interaction researchers to create their own questionnaires, but this task can be a lot more complex than it first appears.

At the outset, one must be very clear exactly what you want to find out. Do not simply include questions just in case they may be useful – this will end up wasting your time and the time of the respondents. Also remember that you will need to ask the respondent some information about themselves. Again, this should be limited to just what you need to know about them (e.g. experience of similar systems, age, visual acuity, etc.) but avoid personal questions that have no benefit to your research (e.g. do you really need to know their name?).

Once you know what you want to ask, you need to pose the questions in a way that is unambiguous to all possible respondents. This is no small task. There are a number of standard forms of questions that one might employ to help guard against ambiguity and increase the value of the data. These include

Open-ended, e.g. ‘‘Did you enjoy using the system?’’

These are the least formal and are an invitation for the respondent to give an unstructured opinion. The responses to this type of question can be interesting, but are obviously hard to analyze.

Scalar, e.g. ‘‘I was able to enter text easily: Disagree 1 2 3 4 5 Agree’’

This is an example of a Likert scale, which offers a more quantitative way of assessing a respondent’s opinion or attitude than can be achieved through an open-ended question. Typically these scales have five to seven options, but ranges from three to nine options are not unknown.

One form of scalar questions are semantic scales, which let a respondent decide where their opinion lies between two diametrically opposed views, e.g.

Happy - - - - - - - - Sad

Multi-choice, e.g. ‘‘What base would you like on your pizza? (tick one):

 Thin  Thick  Cheese rim’’

This is the simplest form of multi-choice where the user should select one option from a limited list. Of course, in some instances we may want more than one selection, e.g.

‘‘Please select your pizza toppings by ticking appropriate boxes:

 Tuna  Chicken  Corn  Brie  Cheddar’’

Sometimes, we may want to know more about the choices people select, in which case we can introduce ranking, e.g.

‘‘Please select your pizza toppings by writing ‘1 in the box beside your favorite topping, ‘2 beside your next-favorite, etc.:

 Tuna  Chicken  Corn  Brie  Cheddar’’

Having told you how to design your own questionnaire, we must now caution you against it. Two key problems are:

Reliability. Can you guarantee that the questionnaire will give the same results when completed by similar types of people?

Validity. Are you sure that the questions you set are measuring the effect you think they are measuring? Can you be sure that the respondents are interpreting the questions the way you intended them to?

There is a lot to be said on the topic of questionnaire design which falls outside the scope of this book. For a full discussion on the pros and cons of using questionnaires in usability evaluation, try reading Jurek Kirakowski’s thoughtful discussion (www.ucc.ie/hfrg/resources/ qfaq1.html). If you’re keen to develop your own questionnaire, then books such as that by Anastasi (1982) give very detailed accounts of how to produce questionnaires that give rigorous results.

## 7.8 NON-USER METHODS

Testing with real users is expensive and time-consuming. This has led to the development of user-less user testing. It may seem counter-intuitive, but research in disciplines such as psychology gives us insight into how the human mind works. We can therefore predict how any human would react to an interface without having actual users present. Consequently, this type of evaluation is often called ‘predictive’.

## 7.8.1 HEURISTIC EVALUATION

Conducted by: Usability experts

Equipment: An interactive prototype

Results: Qualitative and quantitative – usually a ranked list of problems

Where: Controlled setting

Heuristic Evaluation is a technique created by Jakob Nielsen (Nielsen, 1994) as a way of structuring expert evaluation of an interface. The basic idea is that the experience of interface designers is distilled into a number of design heuristics against which the interface is evaluated by a usability expert. Nielsen proposed the following 10 general heuristics, found on his website (http://www.useit.com/papers/heuristic/heuristic list.html):

1. Visibility of system status. The system should always keep users informed about what is going on, through appropriate feedback within a reasonable time.

2. Match between system and real world. The system should speak the users’ language, with words, phrases and concepts familiar to the user, rather than system-oriented terms. Follow real-world conventions, making information appear in a natural and logical order.

3. User control and freedom. Users often choose system functions by mistake and will need a clearly marked ‘emergency exit’ to leave the unwanted state without having to go through an extended dialog. Support undo and redo.

4. Consistency and standards. Users should not have to wonder whether different words, situations, or actions mean the same thing. Follow platform conventions.

5. Error prevention. Even better than good error messages is a careful design which prevents a problem from occurring in the first place.

6. Recognition rather than recall. Make objects, actions, and options visible. The user should not have to remember information from one part of the dialog to another. Instructions for use of the system should be visible or easily retrievable whenever appropriate.

7. Flexibility and efficiency of use. Accelerators – unseen by the novice user – may often speed up the interaction for the expert user such that the system can cater for both inexperienced and experienced users. Allow users to tailor frequent actions.

8. Esthetic and minimalist design. Dialogs should not contain information which is irrelevant or rarely needed. Every extra unit of information in a dialog competes with the relevant units of information and diminishes their relative visibility.

9. Help users recognize, diagnose, and recover from errors. Error messages should be expressed in plain language (no codes), precisely indicate the problem, and constructively suggest a solution.

10. Help and documentation. Even though it is better if the system can be used without documentation, it may be necessary to provide help and documentation. Any such information should be easy to search, focused on the user’s task, list concrete steps to be carried out, and not be too large.

Ideally, there would be at least five experts to conduct independent heuristic evaluations of the interface. Each expert compiles a list of ranked usability problems, paying attention to the issues of the frequency of the problem (common or rare), the impact on the users (can they overcome it easily?), and the persistence of the problem (will the problem crop up in multiple situations or is it quite localized?).

Having conducted quite a few of these evaluations ourselves, one has to be careful in how the findings are reported. As heuristic evaluation is designed to discover faults in the design (and not laud its positive aspects), the output from the process can be interpreted by the designers as an assassination of their work. To balance this, we suggest that when you spot a problem, you also suggest a solution. Being creative in this way can change the tone of the report, making it more palatable and causing less alienation from the designers. Also, as someone who has received these reports on their cherished designs, we appreciate it when the evaluator lists which particular heuristic is being violated, to show that the assessment is based on a rational evaluation and not personal opinion. If you are concerned about how to pitch an evaluation and manage your relation with the design team, Marine’s article ‘Pardon me, but your baby is ugly . . .’ (Marine, 2002) offers some further hints on how to defuse any personal feelings by keeping the evaluation focused on the wider context and not on the designer’s decisions.

One problem, noted by Nielsen and others, is that these general heuristics may not be appropriate for every class of interface. In their book Interaction Design, Preece et al. (2002) note that there is, as yet, no accepted list of heuristics for evaluating mobile devices. Some work (Vetere et al., 2003) has been started in this direction, using ideas from CSCW to provide heuristics which evaluate the contextual dimensions of mobile applications. Developing these heuristics for a domain as new as mobile computing is a large task. The first set of heuristics for assessing desktop systems (Smith and Mosier, 1986) was based on 944 evaluations! As we have seen from Beck’s work into evaluating mobile systems (Beck et al., 2003), mobile computing has some way to go before we can form heuristics from this depth of experience.

Another form of expert evaluation is cognitive walkthrough. In this instance, the expert evaluator will walk-through a particular task, seeing if the user’s goals can be met by the information and functionality provided by the interface. One variation on cognitive walkthrough is ‘contextual walkthrough’ as proposed by Po (2003). Po proposes that the cognitive walkthrough be conducted in the same conditions as those experienced by the end-user (hence the ‘contextual walkthrough title). While the idea is sound, Po found no significant difference between conducting the cognitive walkthrough in the lab or in the end-user context. However, it should be noted that this result was based on a single study and further work may prove the validity of the approach. Alternatively, it may be the case that any benefit to the evaluators in terms of being located in the target context may be undone by the distractions of the same context

There are other forms of expert evaluations, such as consistency and standards inspection. We will not dwell on these as they have little application to mobile computing at the present time. (Both methods compare new interfaces to accepted standards or conventions, neither of which exists for mobile systems as yet.)

## 7.8.2 NO PEOPLE WHATSOEVER

Conducted by: Theoretical model

Equipment: A formal specification of the interaction characteristics of the device

Results: Quantitative

Where: Anywhere

Building on cognitive psychology research, some HCI evaluation techniques dispense entirely with the user and rely on an idealized model of how people think. Early successes in this field include GOMS (Goals, Operators, Methods and Selectors) which is able to predict interaction problems for expert users conducting limited tasks (Card et al., 1983). GOMS is a very simplified model, but even a model as simple as KLM (Keystroke Level Model) (Dix et al., 1998) can yield interesting results – KLM simply looks at the time taken to find, select and press interface buttons. In fact, we used a very simple keypress-count type of evaluation for pre-testing our ideas for the menu replacement system in Chapter 8. This helped us accept and reject designs, before investing the effort in creating the final interactive prototype for user testing.

One criticism of these models is that they don’t take into account anything other than expert users in limited situations (a typical example would be ATM usage). For mobile computing, this type of simplified evaluation is never going to have much relevance. Fortunately, as cognitive psychology has evolved over the years, so have the models of how humans work and interact with their environment. In particular, connectionist models show great promise in predicting how context will affect user performance. One example of this is through the work of Nunez (2002) to show how environmental factors in the real world affect a user’s sense of ‘presence’ within a virtual environment. From observational experiments, Nunez builds a cognitive model that shows which factors would increase presence (e.g. reading a book on the subject of the VE before entering it) and which would detract from it (e.g. lack of ambient sound). While the model may be too complex for many designers to use directly, it should help predict what types of evaluation are useful and what types of incident to watch for during evaluation. Sadly, this work is at too early a stage to have much impact outside the rather specialist research community.

## 7.9 EXPERIMENTAL EVALUATION

Having arrived at the stage of an interactive prototype, it’s time to ask whether your system offers any improvement on those that have gone before. Users may rave about the system subjectively, but does it offer any functional advantage? Can you give some quantitative measure of just how much ‘better’ your system is?

Shneiderman (1998) describes this type of evaluation as a ‘controlled psychologically oriented’ experiment. Others call it simply ‘experimental evaluation’ (Preece et al., 2002; Dix et al., 1998). Regardless, the underlying idea is to bring the rigors of the scientific method to the field of interface evaluations.

The scientific method is a standard adopted across all experimental science disciplines to determine objective truth, i.e. a truth that is independent of any prejudices, biases or belief structure. The practical outworking of this lofty statement is a process for conducting experiments to ensure that the results are as accurate as they possibly can be. This process is detailed below, along with an example from our research to help clarify the issues.

## Experimental Process

Conducted by: End-users

Equipment: Interactive Prototype

Results: Quantitative and scientifically rigorous

Where: Usually laboratory based

## 7.9.1 HYPOTHESIS

Before you can do any type of experiment, you have to think about the term ‘better’. In what sense is your system better? Take the example of a new form of text entry for a PDA. Is it better in that it allows users to enter text more quickly? Or is it less error prone than previous methods?

Let’s say that we’re interested in the time it takes users to enter text – we’re not so concerned about accuracy, as the primary application will be sending short messages to friends. Time now becomes our dependent variable, in other words, time is the value we are trying to measure (less time means a ‘better’ solution). If all we do, however, is simply measure how long it takes users to enter data, we have not learnt very much. Instead, we want to know whether our system is faster than existing ones, and therefore we need to record the time it takes users to enter text with our system as compared to some other system. As we can change which system to give to a user, the system becomes an independent variable – we are free to choose it at will. So we can now run an experiment in which we manipulate the independent variable (system) to see what effect it produces in the value of the dependent variable (time).

We’ve just described the simplest type of experiment possible, where there is one independent and one dependent variable. If we wish to increase the number of independent variables, then the experiment will rapidly become more complex. Returning to our example, we might want to measure each system under outdoor and indoor conditions. This means that we need to conduct four separate sets of experiment: System A inside, System A outside, System B inside and System B outside. The complexity grows geometrically and experiments rapidly become unmanageable.

Increasing the dependent variables simply means that we measure some other factor for each user. (For example, we may wish to use a questionnaire to measure each user’s subjective experience of the system.) In this instance, the measurement adds little to the complexity of the experiment, but may mean that it will take longer for the subject to complete the session.

Having thought about the variables in your experiment, it is now time to state the objective of your experiment in terms of these variables. This is important, as the results from the experiment must be testable in a clearly defined way, so that there is no ambiguity about what you are measuring and what that measurement will mean. Normally, this statement is known as a hypothesis and takes the form of a prediction about the impact that changes in the independent variable will have on the dependent variable. In our case, that might read something like ‘‘Subjects will be able to input text more quickly using system A than using system B.’

Having formulated the hypothesis, we now have to think a little about the statistical analysis that we conduct at the end of the experiment. The goal of this analysis is to state (with varying degrees of certainty) whether or not the altering of the independent variables did indeed influence the result. Thanks to the wacky world of statistics, the best way to prove the hypothesis correct is to disprove the opposite of the hypothesis! The opposite of the hypothesis is called the null hypothesis. For example, the null hypothesis for our example would state that the users of both systems will take the same time to enter text. So, if the results of the analysis do indeed show that there is a difference in time between the two systems, we can reject the null hypothesis. This means that the original hypothesis was correct.

If you’re starting to get nervous about these statistical terms and have no interest in conducting your own analysis, please don’t worry. The point of this discussion is to provide you with enough knowledge so that you can converse with statisticians and interpret the answers they give you. If you’re interested in conducting your own analysis, then books such as Howell (2001) provide an excellent introduction.

Designing sensible hypotheses with testable results can be a challenge. Even after many years of experience in this type of testing, we still present our experimental designs to the rest of our research group. Inevitably there is some factor we forgot to take into account, or some flaw in the design which we had overlooked. Psychologists, more so than pure statisticians, are especially good at this type of experimentation and evaluation. For that reason, our research group at the University of Cape Town employs two consultant psychologists to help us with the design and analysis of this type of evaluation.

## 7.9.2 THE USERS

We’ve managed to tighten up on the definition of what it means for a system to be ‘better’ but have yet to think about the subjects who will take part in the experiment. In many research papers, the researchers follow the path of least resistance and recruit students from whichever faculty or organization the researchers are based in. This makes perfect sense for the researchers, especially academics, as students are readily available at little cost (free food is often enough to entice them) and can be coerced into taking part in the experiment as part of their course requirements. However, unless the system you’re building is aimed at students, this is a terrible idea.

In order for your evaluation to hold any weight, it’s essential that the subjects you recruit for your experiment are representative of your target user group. They should have the same age profile, similar levels of literacy, and similar amounts of exposure to computer technology. Returning to our example of text entry on a PDA, we should be testing our system with typical PDA users – busy executives needing to manage large amounts of information. And here we see precisely why recruiting students for experiments is so seductive – busy executives would need a large financial incentive to make it worth their while to set time aside and participate in an experiment. I used to work for a marketing research group which ran various focus groups for new products and would recruit users to match a specific profile. This was highly specialized work which we would often have to outsource to recruitment agencies. When one has paid the bill for the recruitment agency and paid the participants a commensurate amount for their time, this rapidly becomes an expensive process. (Just as a word of warning, it may look as though a marketing focus group is the same as an evaluation, but the goals of each group are very different. Marketing agencies can certainly help with recruiting subjects, but you’re better off running the sessions yourself. Siegel (2001) has written a thorough account of the benefits and pitfalls of using marketing agencies as part of the evaluation process.)

So, having decided on who you need, the next question is how many subjects you need. Some people, looking for an easy escape, will latch on to the work of Nielsen (2000b) which seems to suggest that five users are sufficient. However, this interpretation confuses quantitative scientific experimentation with the heuristic testing we discussed before. In heuristic testing, we’re simply looking at user performance whilst interacting with the target system. In scientific experimentation, we’re testing new ideas and adding to knowledge in a quantitative, rigorous way. So Nielsen’s argument is that five people are sufficient to reveal the majority of problems in a given interface. (Actually, it’s worth noting that a lot of people are cross with Nielsen and his five-user rule (Bevan et al., 2003). The debate still rumbles on for now, so please use the rule with caution.) If, on the other hand, you’re running an experiment to prove your hypothesis is true, you need many more than five users.

Dipping our toe into the murky waters of statistics once more, we discover that we need sufficient data to make sure that the results we measured did not happen by chance. In this case, data equates to users. For example, if we recruited only one person, the effect we observed may be down to some strange character trait of that particular user. If we have two users, then it’s less likely that two people will share the same strange character trait, so our results become more reliable, and so on. Depending on the statistical measure you use, the number of subjects you need will vary. However, if you don’t wish to wade further to determine an exact number, using 10 people per condition is a good rule of thumb (Dix et al., 1998). (A condition relates back to the independent variable story. If we did a direct comparison of system A and system B, we would need 10 people for each system, i.e. 20 subjects. If we were interested in performance outside as well as inside, then we now have four conditions – system A inside and out, system B inside and out – and 40 subjects! This could be alarming, but we will shortly see how clever experimental design allows us to reuse the same person in more than one condition, cutting down on the number of actual people we need to recruit.)

One final note on selecting users for mobile computing evaluations is that for evaluation of cellular handsets, the potential user group is so large and diverse that it may not be possible to find a sample that is representative of the user population. Unless a large budget is available, other forms of user evaluation may be more appropriate.

## 7.9.3 TASKS

So, we have the question we want answered and we have the subjects to help answer that question, but what are the subjects actually going to do? Every observational experiment of this nature requires the subjects to perform some task with the interface. This can be whimsical, highly structured, or downright boring. The important thing is that the tasks chosen for the experiment should be representative of those in the real world. For example, when designing the tasks for our text entry system, we could pick our favorite novel and have the subject type in a selected paragraph. This might be fun, but it’s unlikely that anyone will ever want to write a novel using a PDA. Instead, a better task could be constructed by collecting existing (non-private) notes from other PDA users and collating these into a task list.

Besides being representative, tasks should not bias the experiment one way or the other. For example, if one of our text entry systems was particularly fast at selecting non-alphabetic characters, we could bias the experiment in favor of that system by picking messages with lots of punctuation or numbers in them. This issue of biasing was particularly difficult for us to counter when running the experiment described in Chapter 8.

## 7.9.4 EXPERIMENT DESIGN

Having derived the tasks, you next need to consider how to allocate users to the various conditions. Let us return to the simplest form of our experiment, where we are interested in the time taken to enter text using system A as opposed to system B. Should we, for instance, have 10 users enter text first with system A and then with system B? Statistically this would be valid as we have data for 10 users in each condition. Experimentally, however, this arrangement would cause all sorts of problems. For example, as the users worked with system A, they would become more skillful at text entry so that the times for text entry with system B would be much lower – regardless of system, performance for the second half of the experiment would be improved. Or, it may be the case that fatigue comes into play and the second system is always the slowest. This is called a learning effect, where the order in which users are exposed to conditions affects the final result.

In order to counter the learning effect, there are two things we can do. The first of these is to recruit 20 people and allocate 10 to each condition. In this way, we can be sure that there is no learning effect, as the users only ever see one system. Technically, this is known as a between-groups experiment. While it removes the learning effect, between-group experiments require more subjects (in this case, twice as many). Also, one must take extra care of how subjects are distributed between the groups – each group should be a representative sample of the user population.

An alternative to between-group studies are within-group studies. Here, users are exposed to more than one condition. To counter the learning effects discussed earlier, however, the order in which the conditions are presented is different for different users. So we would take 10 users, five of whom would use system A first and the other five system B first. Within-group studies have the benefi that you need to recruit fewer people and you have exactly the same user profile for each condition.

Let’s say we decide on a within-group experiment for our simple evaluation of systems A and B. We then wish to extend the experiment with the indoor and outdoor comparison. If we remain with the within-group experiment, we now have four conditions which must be randomized. This results in 16 possible orders in which conditions may be presented (A outside, A inside, B outside, B inside; A outside, A inside, B inside, B outside; etc.). Is this a problem? Well, we might possibly recruit six more people so that we have one subject for each possible ordering. However, we’re now expecting each subject to complete tasks in four different conditions. This could take a long time, which is unfair to the subjects in two ways: firstly to expect them to spend so long completing the experiment, and secondly, the longer the experiment takes each subject to complete, the more we risk invalidating the results due to subject fatigue.

One common solution to this problem is to use a combination of within and between studies. So, for the experiment above, we could recruit 20 people, 10 of whom would be allocated to do evaluations outside and 10 inside. For each group of 10, five would use system A first and five system B first. Alternatively, it’s just as valid to allocate 10 people to system A and 10 to system B, then have five people from each group start outside and five start inside. Either way, these arrangements give you a good compromise – you need recruit only half the people needed for a pure between-groups study and you won’t overburden your subjects.

Finally, one should also be aware that learning effects may occur with the order in which tasks are presented to the user. If the tasks are placed in the same order for every user, then it is possible that the order affects the final result. For example, if one of the text entry systems uses previous input to predict future input, the order of the tasks may be critical to the performance of the prediction algorithm. An easy fix to this problem would be to present the tasks in a random order for every subject.

## 7.9.5 CONDUCTING EXPERIMENTS

Experiments of this nature are usually conducted in a usability lab in isolation from the experimenter. All the rules we discussed above for conducting informal evaluations apply here: how to record observations, how not to bias the outcome, and how to treat your subjects. Also, this type of evaluation can be accompanied by some form of post-experiment questionnaire or interview to give qualitative insight, along with the quantitative result.

## 7.9.6 EXPERIMENTAL RESULTS

As we stated earlier, the purpose of the experiment is to gain a quantitative insight into how much ‘better’ a system is. Please note that all the statistical analysis tells us is how confident we can be that the observed effect is down to the independent variables and not random chance. The statistics do not say whether the system is truly better. For example, in the text entry example, the analysis may tell us that we can be 95% certain (for statisticians, anything less is random chance) that users of system A take less time to enter text than users of system B. Great! However, the statistics do not say how much faster. The difference may be as little as 1 millisecond! So, while your results are significant in a scientific sense, they may have little practical impact.

## 7.10 CONSIDERING CONTEXT – EVALUATING MOBILE SYSTEMS

When evaluating a desktop system, the process is simplified by the fact that, chances are, the situation in which the system will be deployed (an office somewhere) is the same situation in which the usability evaluation will take place (an office somewhere). Even if the computer is to be employed in some other context (an air traffic control center, say), the system will remain in that context once deployed.

For mobile devices, the context will always be changing. Furthermore, it is not just the environmental context that changes, but the social and technological ones too. This has profound consequences for evaluation, as the device should really be evaluated in each likely context of use.

## BOX 7.3

## WHAT IS CONTEXT?

Dix et al. (2000) divide context in a very similar way, but split technology context into ‘infrastructure’ (network, etc.) and ‘system’ (other devices, etc.). Their context taxonomy is aimed at informing and inspiring design. For our work in evaluation, we have not found this extra subdivision to be particularly useful. ■

## 7.10.1 PHYSICAL CONTEXT

For physical context, we need to overcome the problem of observing how the device is being used and, if we are able to observe, the associated problem of recording those observations. One way we have been able to record on-screen interaction is to use the Remote Display Control for PocketPC (a free download from Microsoft). This broadcasts the on-screen image of a PDA across a WiFi network. So, provided the PDA stays within network range, it is possible to capture user interactions. Any interesting parts of the screen capture can then be replayed to the user to elicit comments as part of the post-evaluation debrief. An alternative for cellular handsets, which are currently not able to broadcast on-screen interaction, is to use custom video cameras, such as the Mobile Device camera provided by Noldus (see Figure 7.5). This can hardly be described as unobtrusive, but does at least allow the designers to see what is happening on screen. (Chances are the designers have a better view of the screen than the user.) Using technologies like these, we can then deploy users in a particular physical context (e.g. in a poorly lit, noisy environment) and see how well they are able to perform with the device.

![](images/ebcaf68b9cc1cf61e181a310a551c35c2cb9756b8da912bc714b5daf83d2859d.jpg)  
FIGURE 7.5  
The mobile device observation camera

For example, to assess the impact of their mobile shopping mall guide, one research group recreated a floor of a shopping mall within their building (Bohnenberger et al., 2002). Although they didn’t recreate the store interiors, they recreated navigational constraints of a mall to see whether the guide was of value.

## 7.10.2 TECHNOLOGICAL CONTEXT

By technological context, we mean the context of the technology available to the user of the mobile application. Usually, this will refer to the networks available, but may also refer to other resources, such as the availability of external monitors, keyboards, etc. This is especially relevant when conducting evaluations of prototypes which use technologies other than those deployed in the final product. This problem was discussed at length in Chapter 6, looking, in particular, at the Buck used to mimic the technology of the Handspring Treo. When conducting evaluations, one must be sure that the evaluations conducted with the prototype technology still hold for the technology used in the final device.

One problem not discussed in Chapter 6 is assessing the impact that different network technologies can have on mobile applications. For whatever reasons, it may not be possible to conduct evaluations using the network infrastructure available to the end-user. In our research, we’ve built a number of applications for cellular handsets. However, we cannot afford the exorbitant fees charged by the cellular networks, so we fake the network using our WiFi infrastructure. Of course, the bandwidth of such a network is much higher than that offered by cellular networks, which may give unreal expectations about the final system performance. This cuts both ways, as one system we tested using this technique failed because the bandwidth was too high! The network was pushing data packets to the device which crashed because it could not process the data quickly enough. If we had used a cellular network, it would have run perfectly well.

Another insight we’ve had in switching applications from WiFi to cellular networks is that user enthusiasm drops off when they are required to part with their own money for network access. A good example of this is the text-worm system we developed which allowed university students to SMS their lecturer during the course of a lecture session (Jones and Marsden, 2004). Students were willing to pay for the SMSs during the first few sessions, but cost considerations meant that usage rapidly dropped off. As technology develops to provide us with devices which support both GSM and WiFi networks (see Box 7.4), it may be the case that this type of project becomes viable.

## BOX 7.4

## CHEAPER WIRELESS ACCESS

There is currently a move by handset manufacturers to produce handsets which can roam between WiMax, WiFi and GSM networks. This is an interesting development as it makes perfect sense for the handset manufacturers, but there is no incentive for the networks to provide these handsets to customers as it will inevitably decrease their traffic. ■

## 7.10.3 SOCIAL CONTEXT

Social context can be a lot trickier to engineer than the physical or technological context. In fact, engineering a social context is tantamount to an oxymoron – ‘‘Ok, Mr Smith, can you please feel frustrated for 10 minutes whilst using the device, and then feel relaxed and try the task again.’’ This is why ethnography, and other longitudinal study techniques, like diaries, are essential for evaluating mobile devices within social contexts – which is why we spent so long on the topic in Chapter 5.

Not only is it essential to evaluate ideas you think will work in a social context (just in case nobody likes them), it’s also worth testing crazy ideas that fail every other test just because they may make sense socially (SMS springs to mind here).

## EXERCISE 7.2

## UPDATED HEURISTICS

Having just read the section on context, flick back to Section 7.8.1 on heuristic evaluation. Read through the list of heuristics presented there and, based on your understanding of context, add some more heuristics for mobile devices to the list. While you are at it, are there any heuristics in the original list you think should be removed or deleted? ■

## 7.10.4 OTHER CONTEXTS

So far, we’ve discussed three forms of context: physical, technological and social. There are many other ways to think about context which may be more helpful in the evaluation (and design) of mobile devices. Dey (2001), for example, looks at several classifications of context and proposes that context may be defined as information that can be used to determine the situation of an entity. Entities are defined as objects, places or people that are relevant to the interaction between a user and an application, including the user and the application. This is a great way to define context for thinking about how an application should fit into a context, but reduces a rich environment to a meager set of interactions between artifacts. Just be careful not to get locked into a mindset of thinking about the technology first and the users second (take a look at Box 7.5), or thinking that the context is more important than the user – Jameson (2001) has some ideas about how to model users and context in a complementary way.

## BOX 7.5

## CONTEXT AWARENESS

One of our colleagues, Professor Edwin Blake, was asked to create a computer vision system which could recognize the tracks of animals in a game reserve. The thinking was that the computer could process the image and infer the context from cues such as GPS location, time of day, type of foliage nearby, shape of print, etc. – a solution know as ‘context awareness’. Not only is this a mammoth piece of computation, but it ignores the fact that the park employs very skilled trackers who are able to read the context instantaneously. So, rather than build an application which would never be as good as a human at reading context, he did some ethnography of the situation and discovered that he could use computers to aid the trackers with recording their insights into context. The result of the project was a GPS-enabled PDA which allowed the trackers to log their observations more accurately than before and ➤ upload these to a central park management system. By seeing context as an artifact of technology, it is unlikely this system would ever have been built.

Part of our research philosophy is that ‘people know best about people’. So while we support context-aware computing to the extent that the computer knows things unambiguously (e.g. time and location), we steer clear of other forms of context awareness (e.g. user’s mood or animal behavior). ■

## 7.11 COMPLEMENTARY EVALUATION

So, if we have to evaluate mobile systems, can we use the techniques developed for desktop systems, or do we abandon them in favor of those that take into account the changing context? Sadly, it would seem that both types of testing are essential for mobile systems.

The value of both types of evaluation is highlighted in Brewster’s research (Brewster, 2002). He was developing a system for mobile devices which used non-speech sounds to improve accuracy of selecting on-screen buttons. After conducting initial trials in a laboratory, he discovered that sound augmentation did indeed increase the usability of the buttons for data entry tasks. To test this in context, he repeated the experiment, the only difference being that the subjects had to walk along a path outside while completing the tasks. While the augmented system still outperformed the control system, there was a significant reduction in the amount of data entered (32% less).

This research shows us two things:

Lab-based evaluations can predict performance of an interface ‘in-context’.

Context-neutral testing provides only partial evaluation information – it’s not a replacement for testing in context.

From this, one might be tempted to infer that contextual testing is sufficient; after all, the laboratory testing only replicated the finding of testing in context. However, there is still value in laboratory-based testing.

In all scientific disciplines, laboratory testing has been used to provide a controlled environment within which the researcher can isolate the effect of different variables on the test subject. This still holds true in the development of mobile computing. At the outset of the research, the designer uses context-neutral evaluation techniques to assess the impact of design decisions before introducing new variables in the form of a dynamic context. Having optimized the design so far as possible, testing can then begin in the target context.

Another reason for adopting this approach is purely pragmatic: it’s a lot cheaper to conduct context-neutral evaluation. Better to sort out any problems using relatively inexpensive studies than arranging the logistics required for contextual testing.

Finally, it’s worth noting that mobile computing is a relatively new discipline. A consequence of this is that there is no widely agreed method for conducting evaluation studies. This is highlighted by Beck et al. (2003), who conducted a survey of major mobile HCI publications between 1996 and 2002. They discovered that of 114 papers, only 50 had some evaluation component. Of those 50, most used evaluation techniques developed for desktop systems. Work like that of Brewster (2002) is extremely rare.

Having said that, one should not be too quick to dismiss the evaluation techniques used to evaluate interfaces in static (constant context) devices. Our approach, and that of Brewster, is to use these standard static techniques early in the design process and then conduct contextual evaluation only when the standard techniques have yielded a positive outcome.

## 7.12 CONCLUSION

As we stated at the start of the chapter, we’ve taken a pragmatic approach to evaluation techniques, as we believe this will provide the greatest value. If your evaluation requirements lie outside the techniques we discussed, or you’re not sure which technique to use, there are many resources available to help you. One of the best places to start is the CHARM website (http://www.otal.umd.edu/charm/) provided by Ben Shneiderman’s research group, which lists all the major evaluation methods and links to the relevant resources. Almost any textbook in HCI will discuss some of these evaluation methods – of these, Preece et al. (2002) does the best job. The classic text in this field, however, is a collection of papers edited by Nielsen and Mack (1994) which remains the standard to date.

To a large extent, evaluating mobile systems remains an open question. As Abowd and Mynatt (2000) noted, ‘‘we see relatively little published from an evaluation or end-user perspective in the ubicomp community.’’ For them, evaluation remains one of the major challenges for mobile computing systems. This is a sentiment echoed by Banavar and Bernstein (2002) who state that ‘‘. . . the development of effective methods for testing and evaluating the usage scenarios enabled by pervasive applications is an important area that needs more attention from researchers.’’ So don’t be put off that you may not be doing the ‘correct’ sort of evaluation; for the time being, no one is completely sure what a ‘correct’ evaluation of a mobile system really is.

## SUMMARY

In this chapter we have selected those evaluation methods that have proven the most useful to us in evaluating mobile systems. We have also categorized these techniques and given guidelines on when each technique is most appropriate. However, we do not aim to be the definitive guide on how to conduct evaluations of interactive systems. Rather, we strive to give you an overview of the methods, where they fit in and how they might be used. If you are interested in following up on a specific method, there are links in the resources section. What we have tried to do is point out the added challenges of evaluating a mobile system and why evaluations developed for desktop systems may fall short.

## WORKSHOP QUESTIONS

Think about how you would feel to be observed using technology over a long period. Bearing this in mind, draw up a sample consent form for experiment participants, based on that outlined in Section 7.5.4.

Do you think it is possible to conduct user evaluations without actual users? To what extent, then, are non-user techniques useful?

Do you think scientific experiments have any place in the scheme of commercial product development?

## DESIGNER TIPS

It may seem like a good idea to design your own evaluation questionnaire, but this is a subtle art best left to experts.

Unless you’re an expert in statistics already, it is much easier to use a psychologist to help you design an experiment and perform the final statistical analysis.

Heuristic evaluation is very popular, especially with commercial clients, as it’s quick and doesn’t require actual users. However, until some effective mobile heuristics are developed, it’s a potentially flawed way to evaluate mobile systems.

Don’t be seduced by context-aware computing – computers can know about physical and technological contexts, but not social context.

## PART III DESIGN GALLERY – DIRECTIONS AND GUIDELINES

CHAPTER 8 CONTROLLING COMPLEX FUNCTIONS 223   
CHAPTER 9 INFORMATION ACCESS 247   
CHAPTER 10 BEYOND TEXT – USING IMAGES   
ON MOBILE DEVICES 289   
CHAPTER 11 IMPACTING THE COMMUNITY; IMPACTING   
THE WORLD 315