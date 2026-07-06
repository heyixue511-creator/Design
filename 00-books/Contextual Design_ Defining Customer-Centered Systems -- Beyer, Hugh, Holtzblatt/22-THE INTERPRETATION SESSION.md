# THE INTERPRETATION SESSION

The last part of a prototype interview is parallel to a contextual interview: the interviewers bring the data back to a design team and replay the interview for them so that everyone can see what happened and offer their different perspectives. This interpretation session is focused narrowly on identifying the issues raised by the interview.

Issues are captured on Post-its by the recorder, one point per Postit. Points to capture are any new aspects of work practice that haven't been seen before, validations of design elements that worked for the user as designed, problems that got in the user's way, places where the structure of the system didn't help him get his work done, and any user interface validation and problems.

Most of the data from an early prototype interview will be structural issues for the User Environment Design. Capture these and stick

them directly to the affected part of the User Environment Design. There will be some issues for the user interface, even though this is not the primary focus——the issues are captured and can be dealt with as the interface is refined. Any issue that has to do

with presentation, layout, or wording is a UI issue. There will also be some issues for the work models. These include any points that capture new aspects of work practice that aren't properly represented on the existing models. Rather than try to update the models in the meeting, it's easier to capture the issue and stick it right to the model in question. If there's any disagreement about where an issue goes, move it upstream—put it on the User Environment Design in preference to the UI and on the work models in preference to èither. This whole session is good practice in separating conversations, as each conversation has its own model and its own place on the wall.

Throughout the interpretation session, the primary task is to see behind the user's reaction to the UI to understand the work issue. If the user was overwhelmed, was that because the focus area wasn't clean, the design didn't match his work, or was the UI for that part of the system unnecessarily complex? Examine the user's actions and words to understand what his reaction meant to the design.

## ITERATION

When a design has been tested with two to four users, it's time to iterate it. The issues raised by the users are grouped so related issues can be addressed together. Changes to work models may affect the User Environment Design, and changes to the User Environment may affect the user interface, so the first issues to deal with are those related to the work models—move forward from there. No one wants to spend hours on some aspect of the user interface, only to discover later that a change to the User Environment Design obviates that whole part of the interface.

For the work models, collect the issues from all users for each type of model. Organize them to see what they imply for the model. Extend

it with any new aspects of work practice that came from this interview: new roles or flows between roles, new strategies, new influences, or new structures in the physical environment. If this new data affects the focus of the design, you'll deal with it as part of

Address work issues first, then UED, and then UI

addressing the User Environment Design; otherwise, it becomes part of your permanent representation of your customer population.

Then turn to the User Environment Design. First consider whether any of the work model changes affect the design, and if so identify which parts they affect. Then look across the data from all the users and ask what the primary structural issues are. Look for ways to redesign the overall system to address these issues. Then start working on sets of issues part by part, starting with the parts that are involved in the most important and far-reaching issues. Collect the issues across all users for each of those parts, and consider how to redesign them to address the issues and the new information from the models. Use the storyboards to help you think through particular tasks in the changed system. Go on from section to section of the User Environment Design until you've addressed all the issues you need to. You may decide that some issues are at too low a level of detail to bother with yet or affect some part of the system that is too peripheral. There's no point in spending a lot of time to get a part of the design right if it's only going to be cut later. Work to get the overall system stable, then prioritize what to ship, and then do the details.

Restructuring the system tends to pull it apart as a system, so finish with a validation pass to reorganize it and pull it back together again. Clean up the loose ends, and make sure the design is reasonably clean.

Finally, roll the User Environment changes forward into a redesign of the user interface. First look for broad issues that affect the whole interface: Did the base metaphor work? Were your interaction mechanisms usable? Were there consistency issues to address? Decide what to do about these issues. If you'll change the base metaphor, do it first. before addressing any of the particular issues. Then move from focus area to focus area, collect the user interface parts that represent a focus area and the issues associated with them, and redesign the interface to deal with the issues and User Environment changes together.

## COMPLETING A DESIGN

This is the iterative, customer-centered process of Contextual Design. As you expand your design to address more and more of your vision,

the process will change and flex to accommodate new issues. The core design may be quite stable, but when you move to address a new area of work, you'll collect much more basic work practice data. You may need to switch to capture a set of work models in the middle of the interview. You may capture sequences

for a task that you were never able to observe until this point. Then the interview will move back to the prototype, and your interpretation session will go back to primarily capturing issues.

But you're always using the prototype to drive customer visits and keep the team grounded in real customer data. Returning to the customer every 10 days to two weeks keeps the team focused and moving forward; in our experience, lack of regular contact with customers is a primary reason teams lose focus and break into arguments with each other. A prototyping approach to design keeps you going.

This iterative design process continues until the team is sure it has a workable design. Usually after two to three iterations of a part of the

User Environment Design with customers, that part begins to stabilize. The number of structural issues, which are recorded on the User Environment Design, fall off, and the UI issues start to predominate. This is your signal that the structure is pretty

much right. Move to testing primarily the UI while simultaneously extending the prototype to test the structure of another part of the system. The part that has stabilized can be moved simultaneously to implementation design and code. Prioritize what parts of the system to deliver, as we described in Chapter 16, and build a shipping User Environment Design for the next release. This becomes your working specification.

When you move through a design in this way, you can be confident that you've understood the requirements and the appropriate system structure. Development of the system can proceed through the implementation and testing of running code in much the same way that we've tested prototypes. This maintains the customer contact while implementation progresses. The iterative prototyping process merges with an iterative implementation process that coordinates all the parts of the team to deliver on the vision.

CONCLUSION