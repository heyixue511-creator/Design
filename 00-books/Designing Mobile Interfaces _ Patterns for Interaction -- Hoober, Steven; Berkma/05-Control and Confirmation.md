# Control and Confirmation

## Quiet, Please

The lights in the theater dim. Voices die down. All eyes stare at the giant illuminated screen and silence overtakes the room. Projecting now, the movie begins. Starting from high above a city, the audience’s view mimics the flight of a bird. Slowly, as the view trickles down below the clouds, a row of houses appears. Dropping lower, the view focuses to one house in particular. We enter the house; it’s dark, old, and abandoned. Slower now, the camera leads us down the stairs to the basement.

The audience is coaxed into believing something isn’t quite right. Attention is focused on the closed closet door, now bringing an increase in fear and tension. Something terrible is about to happen; the audience waits. The camera leads the audience closer to the door. Closer. Closer. Closer. Not a sound to be heard now. Then it happens! The sound of Lady Gaga’s “Bad Romance” chimes loudly, breaking everyone’s concentration. Heads turn and eyes seek to identify the location of the sound and culprit. The patron embarrassingly finds her mobile phone and switches it off.

Yes, it’s annoying when someone forgets to turn off her phone. But hey, people make mistakes. Mistakes happen every day in our lives. Some mistakes go unnoticed, while others can be quite catastrophic. Some mistakes are caused by us, others by objects in our environment. But many mistakes can be prevented!

## That Was Easy

How could the mistake of the lady not turning off her phone have been prevented? If only she had an “Easy” button to push that would have allowed her to start over and turn off her phone prior to the movie beginning. Maybe through a distributed cognitive network, her friends could have reminded her. Or maybe the situation could have been resolved if her mobile device detected that she was in a movie theater, and incorporated constraint controls, such as automatically defaulting her device to vibrate.

Unfortunately, life doesn’t provide us with a personal “Easy” button to turn a complex situation filled with chaos and mistakes into one of error-free simplicity. Relying on friends can be, well, unreliable. Having our device provide controls and constraints to limit our careless mistakes seems plausible and doable. Therefore, as designers we need to equip ourselves with a general understanding of why we make mistakes to begin with.

## Understanding Our Users

![](images/6f88193b4e673e63b8b92a9590d334b9427d0bfb1badc0f6fa49fa7447e5c5c3.jpg)  
Figure 3-1. Pop ups and similar controls are key to Confirmation, Sign On, and many other types of interactions due to their modality. The user is required to make a choice, and this both focuses the user’s attention and prevents her from accidentally performing errors.

We must accept that we are human and we make mistakes because our body has unique limits. We are limited in our cognitive processing abilities, which are constrained by capacity and duration. We have physical limits in our endurance and strength. We have ergonomic limits in our reach and rotation. We have perceptive limits in what certain electromagnetic and mechanical wavelengths we can detect and filter.

Mixed together with our limitations, we expend a lot of cognitive energy to process and interact with the enormous amounts of stimuli in our environment. Our attention on the task at hand will affect which environmental stimulus needs to be filtered, focused on, and stored. Think of the human mind as a leaky bucket that is constantly being filled. As more and more stimuli are collected through sensory memory, most will be lost due to filtering. Important stimuli will be processed and stored using our working and long-term memories.

Humans have also developed ways to reduce the mental load required to process information. According to Payette, this is possible because cognition is embodied, situated in an environment and distributed among agents, artifacts, and external structures (Payette 2008). We do not solely rely on our individual human limits to process information all the time. We can embed our knowledge of the world in objects that serve as episodic reminders to help us recall. We can distribute our cognitive load to multiple agents or devices. Consider a grocery list. We could try to store all that information in our heads and hope to recall it by the time we get to the store. But it is more effective to situate our cognition in a notebook where we can write down the entire list.

We then no longer need to recall each item. We just need to recall that the notebook contains the list. Further, we can distribute our cognitive load among others. Let’s say we are in a baking class that teaches only how to make cakes. Rather than have everyone remember to buy all the ingredients, we can assign each person a specific ingredient to purchase. Can we reduce cognitive load and error even more? Yes. Let’s distribute all cognitive load onto technology. What if your refrigerator monitors your shopping habits and cooking behaviors, and can automatically sense which ingredients you need? Then it sends a grocery list order via SMS to your local supermarket. You mobile device can confirm your order was placed, the amount can be charged to your bank account, and you can be notified when your order is ready to be picked up!

## Control and Confirmation

Because not all devices are designed today to absorb all our cognitive load, as in the preceding example, this chapter will provide methods that help distribute that load to create enriching situations while preventing user error. Throughout this chapter, cognitive frameworks are presented to help us understand how people process information. These frameworks apply when interactions require control and confirmation:

## Control

This refers to respecting user data and input while protecting against human error, data loss, and unnecessary decision points. This is a key principle of mobile design.

## Confirmation

When a necessary decision point is needed, an actionable choice is modally presented to the user to prevent human error. Before adding modal confirmations, consider the following:

– Is a decision point required here that needs confirmation from the user?

– Will having this confirmation eliminate risk of human error and loss of input data?

Do not use confirmations arbitrarily or excessively. They will increase user frustration by:

• Stopping the user’s goal from automatically happening by presenting a confirmation

• Forcing the user to read, understand, decide, and then act on the confirmation

• Increasing unnecessary mental load through the entire process

For example, let’s say a user’s goal is to enlarge an image on his mobile device by touching it. Would this particular situation require control and confirmation to prevent human error from occurring? And if so, can human error lead to a drastic consequence? In this example, the user’s risk for error is low. Security is not compromised, and loss of data is not imminent and likely to follow. Therefore, having a control or pop up modally appear with a confirmation message asking, “Would you like to enlarge this image for viewing?” is not necessary. This will create user frustration.

Let’s examine another example. This time a user is at an ATM with a goal to withdraw money. The user’s risk for error is moderately high. Security can be compromised and money loss can occur. In this case, having a modal message appear to confirm the amount of money withdrawn may be viable and necessary.

## Patterns for Control and Confirmation

The patterns detailed in this chapter are concerned with specialized methods of preventing and protecting loss of input data. In some cases, patterns listed in other chapters will offer alternative methods, and these will usually be cross-referenced within the pattern. For example, Pop-Up may be referenced when creating patterns found in this chapter. See Figure 3-1 for some real-world examples.

## Confirmation

When a decision point is reached within a process where the user must confirm an action, or choose between a small number of disparate (and usually exclusive) choices.

## Sign On

This pattern is used to confirm that only authorized individuals have access to a device, site, service, or application on the device. Theory and principles of privacy and security will only be alluded to, and are not discussed. Please find appropriate references for these.

## Exit Guard

This pattern is used when exiting a screen, process, or application could cause a catastrophic loss of data, or a break in the session.

## Cancel Protection

This pattern is used when entered data or subsidiary processes would be timeconsuming, difficult, or frustrating to reproduce if lost due to accidental user-selected destruction.

## Timeout

High-security systems or those which are publicly accessed and are likely to be heavily shared (such as kiosks) must have a timer to exit the session and/or lock the system after a period of inactivity.

## Confirmation

## Problem

You have created a process that includes points where the user must confirm an action, or pick from among a small number of disparate (and usually exclusive) choices.

Confirmation steps are simple, logical parts of many processes, and can be easily implemented in any number of ways. This pattern describes the best ways to do so on mobile devices.

## Solution

![](images/248106fa3ceea51f923a40f7c87336a75c876a572f70211f1620ce139e1500a6.jpg)  
Figure 3-2. For Confirmation dialogs, the process is interrupted to present a series of choices. For touch and pen devices, arrangements like this, with stacked buttons, are common and easy to understand.

Whenever possible, you should use information from current and previous user behavior, sensors, and any other sources to try to present the correct option to the user. When that is not possible or likely, you should present the likeliest choice, and give options to switch to others.

For example, when opening a Messaging compose screen, instead of presenting a Confirmation dialog asking whether the user intends to compose an MMS or SMS message, just open a Compose screen with attachment options. If the user chooses an attachment, the message becomes an MMS message; otherwise, it’s an SMS message. The user is still the one making the choice, but he is making it implicitly by actions and choices (selection of the attachments) he needed to make anyway.

Except for error or guard conditions such as Exit Guard, systems can often be designed to avoid explicit choices.

When the step cannot be avoided and user input cannot be divined contextually, you must present the choices contextually, as choices related to the task or screen that preceded the Confirmation screen. Always communicate the consequences of the choices simply and clearly.

![](images/fcf153790db73b7f5329650ac4f1dc44bc661cbeb5b65a9d769a1b7641fddd51.jpg)  
Figure 3-3. Single-choice Confirmation dialogs are important variations. When the user must be notified of something he cannot alter, but that will affect him, such as a dropped call or frozen system, informing the user even when he has no choice is better than not telling him at all. Processes that require a Wait Indicator widget will also often be in Confirmation dialogs, either with a Cancel button, as shown here, or without one.

Though many display methods are possible, all will be modal dialogs of some sort, as shown in Figure 3-2. For more details on these, see variations under Pop-Up.

Three key variations exist. A single choice (Figure 3-3) is only used to inform the user. For example, let’s say a fatal error has occurred and the handset must be restarted. Instead of just restarting the handset for the user without warning, it may be helpful to tell the user that the condition has been reached, in which case you should present a Confirmation dialog with a single Restart button. In cases where the condition is not catastrophic (such as a dropped call), you may choose to have the dialog disappear after a brief time. Including a button then simply allows the user to dismiss the dialog that much faster.

When you automatically dismiss messages, it is usually best to have some other method display the same message. Load the call log, with the item visible, or add an item to the Notifications area. You can determine the best method by examining the OS or application standards.

The cancel variant of the single choice includes a Wait Indicator to denote that a process— usually a user-initiated one—has begun and the user must wait to perform other tasks. When possible, include a Cancel button. If you do not, this may become a sort of “no choice” confirmation box, with nothing but messaging and the Wait Indicator widget in a Pop-Up.

By far the most common is the two or three choices variant. This is the maximum number of choices that a user can readily comprehend at a glance, while also presenting enough options for most required decisions. Here are some examples of three choices when exiting with unsaved documents:

• Keep working on the document.

• Save the document and exit.

• Exit without saving the document.

Note that these are not ideal labels. See the Exit Guard pattern for more discussion of these sorts of conditions.

In some cases, a larger number of choices must be presented. These will generally be offered as a single Select List in the dialog. You should avoid scrolling, but note that scrolling may be unavoidable.

Interaction details  
![](images/1dc0bbdf24d835bc29e4da03ab435a90aeb41ee77612e10d59873249643d4df9.jpg)

![](images/8170a2526535373c6b2e82220a04636c3e8477941ed7b717ec2ba715290e1cc1.jpg)  
Figure 3-4. For devices with soft keys or with soft-key-like buttons, there are two methods of presenting the Pop-Up. It may be floating, and the lack of graying out of the buttons and Pop-Up relate them, or it may be anchored to the same edge as the buttons, to tie them together more strongly.

The Confirmation pattern involves an error or choice that stops the process. Such choices should not be avoidable, but should be contextual to make it clear what application or process they will affect. These should therefore almost always be modal Pop-Up dialogs. See that pattern for additional details.

Whether two or three choices is convenient or a nonstandard UI is required depends on the OS paradigms. If the device OS you are designing for uses soft keys or soft-key-like on-screen buttons, two choices with the dialog docked to the edge with the buttons is the simplest way to present a small number of options, as shown in Figure 3-4. However, this (usually) limits the options to two.

If additional selections are required, they may be loaded in any way needed, such as buttons in the Pop-Up, as pick lists, and so on. Use any soft keys or on-screen buttons for primary supporting actions, such as Cancel. In the earlier example of exiting with unsaved documents, the choices to exit without saving and to save the documents would be in the dialog; the option to return to the application would be labeled “Cancel” and would be the soft key conventionally used for this. See Figure 3-4 for two examples of this.

When working with such devices, avoid disregarding soft keys entirely, for consistency of the interface.

When designing for other interfaces, especially for touch and pen input, selections should usually be in the form of buttons.

Presentation details  
![](images/24b60ebddebdebf7a396e5e3c3af780412f962f1a627cc00c85883b14ac64acc.jpg)  
Figure 3-5. The title, description, and button labels must work independently and in concert to make the Confirmation dialog clear and immediately obvious to the user.

When the Pop-Up appears, use other methods to notify the user of the stop in the process, such as audio and/or vibration. Follow current system volume settings for the notification. Mobiles are used in quick glances, so the user may not notice such a stop in process for minutes or hours unless he is informed via a nonvisual channel.

If the Confirmation action occurs while an application is running in the background, use any available notification method installed with the OS to bring this to the front. If the only method is a Pop-Up dialog interrupting the in-focus process, use this carefully. Trivial processes, such as your game crashing, do not need to interrupt phone calls.

The Title of the dialog must clearly denote the choice to be made. Do not label it as “Error,” with codes or jargon, or with the name of the parent application. For the example used earlier of exiting with unsaved work, “Unsaved work” would be a suitable title.

![](images/c9be38cd9901dcbffee1ed1f6a31e148992180970f08526a808b1ae103a780d1.jpg)  
Figure 3-6. In rare cases, more options than can fit on the screen must be presented. In this case, a scrolling selection box may be offered instead. This is not something a user can understand at a glance, so it should be avoided.

A description should usually be provided. If the choices are clear or simple enough, you can sometimes leave this out. For the earlier example, a suitable description would be, “You have chosen to exit but have made changes to files without saving.” The description and title may or may not be in the form of questions, as the choices will often serve this role.

Button labels must not depend on the description or title. Never present selections such as “Yes” and “No.” Do not try to fix these by adding a question such as, “Save these changes?” Users will not read the whole thing, but just glance at the options, and will become confused by your vague buttons.

At the same time, do not let options be too long, or they may not be readable or may not look like selections. Options such as “Delete” and “Save” are much more suitable. For the relatively complex example used previously, options might be:

• “Save changes”

• “Exit without save”

• “Cancel”

“Cancel” may not seem to be the clearest label. It is instead a placeholder for the common term or symbol used in the OS to denote canceling or going back from the current action. In this case, the action is the presence of the Confirmation dialog, so the application will be returned to. See Figure 3-6 for an example of all these messages in one design.

When a choice is clearly the preferred one, or is the safest (e.g., it preserves user data), it should be indicated as such. The OS standards should include a method of indicating button preference such as color, icon use, or border treatment.

## Antipatterns

Reduce clicks whenever possible. When a selection is made, it should immediately commit the change and proceed to the next step. Never force the user to make the choice, then press some sort of “Submit” button.

Do not overuse the single-choice variation. For example, if an application must quit and a Confirmation dialog is useful, a dual choice would usually be better. Offer options to just quit or to quit and restart the same application immediately.

Carefully consider whether a Confirmation dialog is the right pattern whenever more than three choices are offered. It may be a natural part of the process. The use of the modal dialog implies exceptional conditions or errors and so should only be used when needed.

Unless it is the standard and exclusive way of canceling a process, do not provide a Close button for the Pop-Up dialog. Even if the behavior can be mapped to both the Close and Cancel functions, the Confirmation dialog presents options as a set of required choices. Closing the dialog implies it is optional and can be avoided.

Do not develop new terminology, or use new or nonstandard icons for simple behaviors such as Cancel or Back. Use the OS standard labels or iconic representations.

## Sign On

## Problem

You must provide a method to allow only authorized individuals access to a device, or a site, service, or application on the device.

Authentication is built into the security model of most devices, but you may want or need to provide additional security for any application, service, or site accessed from the device.

![](images/fc6b308ad3fbcdc716e8f1cd076d05125e6c4e9e4ac265e4d75d68aaf9eb63c9.jpg)  
Figure 3-7. Username and password fields do not change, but Submit and Cancel can change depending on the interaction methods available, and the OS standards. Touch and pen devices are very different from scroll-and-select.

Security is very often overused. Do not automatically implement it, and consider whether your specific situation requires explicit authentication. Mobiles are personal, and so should only require authentication for first-time entry, or for very high-security situations. Mobile-like multiuser devices such as kiosks will also require authentication.

Personal mobile devices also have built-in security methods, so users can lock them if they are security-conscious. During setup, you may remind users of these features instead of adding additional security to your application or website.

User identity, whenever known, should be used and as much information in the system displayed as possible before authentication gateways are passed. Authentication may then only require the password, as in Figure 3-8.

Authentication must be presented in context, so it is clear what system the user is gaining access to and why the level of security is needed. Entry methods must be designed to encourage ease of access and to prevent miskeying. Users justifiably do not trust vague, general, or inappropriate requests for authentication.

This is an excellent example where common practices are often not just difficult to use, but actually insecure. Use confirmed best practices, and follow the intent and letter of all security laws and regulations that apply to you. Also be aware that some regulations, such as current US CPNI requirements, are not fixed in time, and presume you will improve security as threats change over time.

![](images/7a8cd26b9f8d27065cd3fabe8817618ff6837e086acaddfef82c8401204e1854.jpg)  
Figure 3-8. Anonymous users, such as users signing into an account for the first time, must provide a username and password. When just checking credentials on a second visit, display the user’s information and only ask for the password.

The most common method is to extend desktop paradigms and accept input via form fields, as text or numeric entry using the conventional input methods provided with the device and/or OS: hardware or virtual keyboards and keypads. This works on all devices and platforms, but is not ideal. The difficulty of entering text is exacerbated with the nonword nature of passwords.

For on-screen, virtual Keyboards & Keypads, you may find it helpful to develop a custom keypad, which the user may tap or drag across in a pattern, for increased security or additional ease of entry.

Additional entry methods, such as biometrics, are not yet established enough to have best practices in the general mobile space, and therefore no design patterns exist. Fingerprint readers are the likeliest to become common, and generally work as a single factor (identity), providing most access but requiring that a short password be entered for highersecurity actions.

Remember that entry of credentials is not enough to count as a full security methodology. Recovery, reset, and out-of-channel notifications are also required, but are systematic approaches are outside the scope of this book. For very high-security applications, multifactor authentication, biometrics, and token-based security systems (such as RSA SecurID) must also be considered.

![](images/263fe219d2e4adc5d213cbceaf33733797392fe2bb13258e2ed0caeeace25f7a.jpg)  
Figure 3-9. Creating credentials is very similar to entering them for Sign On. When the field is in focus, make it entirely visible. If it will be on the screen for a while, it can be obscured when out of focus.

When you present a Sign On dialog, it is usually best to make it the only accessible item to avoid confusing entry with other behaviors. This makes it either a complete page or state, or a modal Pop-Up.

When using a form field to enter passwords, you must restrict entry methods to those allowed. If the password is only numeric, disregard alpha or symbol entry on hardware keyboards, and only display the virtual numeric keypad. See the example entry methods in Figure 3-7.

For small, personal-size devices such as phones, MIDs, and tablets, you should generally not obscure or “mask” passwords. This is the common practice of replacing the characters with dots or asterisks. “Shoulder surfing” on mobiles is extremely difficult due to the scale and viewing angles. In addition, the user may be relied on to move to a more private area or simply turn around, behaviors that desktop users cannot exercise. Displaying the entire field will greatly speed entry and reduce errors on entry, all of which not only reduce user frustration, but also increase security by reducing time on entry and reducing use of recovery methods.

When the password field may be on the page for a while—such as during account creation—the password may be obscured when the entire field is not in focus, or after a brief time, as in Figure 3-9. You can also give the user a selection, such as a checkbox, to hide the password. You may appreciate this during demonstrations, so you may hide it while projecting your cool new product at a conference.

An excellent method to enter a passcode for touch and pen devices is to provide a custom keypad, as shown in Figure 3-10. This may use conventional characters, such as numbers, or special symbols to add a layer of obscurity. These are mostly used as an increased security method; the order of the items changes each time, preventing observers from determining the passcode string by looking at finger patterns or examining the screen for marks.

![](images/aa463a980205c305db3624a4a087b463b29d6ccd73807e697223a29f4837ef5f.jpg)  
Figure 3-10. Patterns can be a good way to add security for touch and pen devices, and if the grid changes each time, they provide an extra measure of security when entry can be observed or the device itself is available for others to access.

Another method that is especially useful for securing device lock screens is to provide a pattern entry, as in Figure 3-11. A grid of numbers or symbols is provided, and a series of adjacent items must be selected as a single gesture, such as an L or U. Although fewer combinations are possible, this can be done with minimal visual input, and may also be configured to learn specifics of the approved user’s gesture speed and accuracy. Gestures outside established bounds, though good enough for typing, may require entry of conventional passwords as a backup confirmation method.

You should always consider the entire method of access, and provide links to seek help on entry and to get more information on system security as well as recovery and/or reset methods. For many applications and tools, unusual conditions such as these can simply load your website to complete these processes. However, be sure to weigh the extra complexity, delay, risk of the site not loading, and other factors. This might be best as a stopgap for the first release, but you will need an integrated solution for later on.

When creating usernames and passwords for account creation systems, use tools to check that the username is available and the password is sufficiently secure as soon as the user moves to the next field. Avoid displaying errors after submission.

You should always provide a Cancel function in case the user cannot recall her credentials, or must perform some other task instead. Even for device authentication, there must be a way to revert to the sleep state without inducing an error.

![](images/4200a804329280bf5d94c7098f8583cbf90674a79d35250c55bacb84694845fe.jpg)  
Figure 3-11. Gestures are lower-security because they reduce the number of patterns and cannot randomize, but are so easy to enter they may encourage locking the device more often.

You must always label password entry screens and Pop-Up dialogs in the context of the process or portion of the process. Explain the reason for the authentication specifically. Do not say “Sign on to our store,” but rather “Sign on to complete purchase.” If the title is insufficient, add a description, but keep it brief; users are unlikely to read much, and will gravitate to the entry fields.

Label each field, and be sure to use the same terms each time they are presented, throughout the entire experience. Use parallel labels. “Sign on” and “Sign off ” go together. “Sign on” and “Log out” do not, and will be confusing.

Indicate the allowable input methods and the current input method for each field. You may have to add hint text in or under the field, or you may be able to simply lock the keypad into the allowable mode. Be sure to indicate locked entry with an Input Method Indicator. Do not needlessly duplicate information. If entry is locked to numeric values, do not also say “Enter numbers only.”

If the user has been identified by device ID, cookies, or something similar, provide the known and nonsecret user information, such as the user’s avatar photo and name on any Sign On screens. Although all you know is the password, do not just ask for it with no supporting information. Of course, avoid demanding that the user enter her username when this is already known, or has actually been printed on previous screens (or in the header of the Sign On screen).

Buttons to submit Sign On forms must, whenever possible, be contextually labeled. Use labels such as “Continue” to remind the user she is in a process, and avoid “Sign On” and the even more generic and technical “Submit” whenever possible. If completing the Sign On process will submit another action, make that clear. Use “Sign on and submit order,” for example.

When two buttons of equivalent visual weight are presented, the “Submit” choice should be designated as the preferred selection; the OS standards should include a method of indicating button preference such as color, icon use, or border treatment.

The label for the “Cancel” function should always use the common term or symbol designated by the OS to denote canceling or going back from the current action. For devices with soft keys, or OSes with soft-key-like buttons, the “Cancel” function at least should be displayed as a soft-key button. When the Submit button is presented as a more prominent on-screen button, this can entirely alleviate any concerns over prominence of the preferred method.

## Antipatterns

If your use case demands hidden fields, use caution when coding or specifying. Do not assume that the default password method built into the OS is secure. Most still reveal the character being typed, and this is basically required in triple-tap text entry modes. If an obscured entry is required due to use as a kiosk, while attached to a projected device or in other shared situations, be sure to specify how obscured it must be. This may require custom fields to be coded.

Avoid using any desktop paradigms without considering the consequences. For example, do not use dual fields to attempt to solve the entry problems associated with obscured entry. The difficulty of entry on a mobile device will make a large percentage of users simply incapable of creating a password with this method.

Be careful to use terminology absolutely consistently throughout the process. If all your documentation refers to a “passcode” (because it is a number), do not suddenly use the term password on the Sign On screen. Also try to use correct terms when possible. Enough users are used to authentication systems, and many of them understand the difference between recovery and reset. Do not conflate or confuse the terms.

## Exit Guard

## Problem

Exiting a screen, process, or application could cause a catastrophic (unrecoverable) loss of data, or a break in the session.

Exit guards can be built into almost any process, though in some cases, preservation of information can be difficult. Plan carefully to ensure that the goal of keeping user data is well designed.

## Solution

![](images/931342b99f171c761fcb538b71fcdcbdb99b9d968b7ede29cd02379cbe738eb1.jpg)  
Figure 3-12. The Exit Guard is a modal dialog that interrupts the process of exiting an application or process. The Cancel soft key will close the dialog and return to the last state without exiting.

You should simply present a modal dialog that delays the user from exiting immediately. The use of the Pop-Up, as shown in Figure 3-12, keeps the app or function open in the background, and so should preserve any information. The dialog informs the user of the consequences of exiting (loss of data) and requires the user to make choices, at least to confirm exit or return to the session.

Be sure to build systems to prevent data loss even if exiting occurs. For example, auto-save all user entry, save draft messages, and so on. In many cases, even critical entry systems may forgo an Exit Guard as long as recovery is simple and the process may be easily reinitiated. These concepts are discussed further in the Cancel Protection pattern.

For high-security or time-sensitive entry, such as banking, you may find it implausible to auto-save information with sufficient security, or a break in the session may cause too much delay. In these cases, an explicit Exit Guard is useful.

## Variations

![](images/ad58e8bbf630e3fd712be63909bae2292b7d77c0d16a84e590eee6a308357a6f.jpg)  
Figure 3-13. Devices without soft keys will place both buttons within the modal dialog. The top is generally the “Exit” button, and the bottom will “Cancel” the request.

The most typical variant is a simple modal dialog, informing the user of the risk of exiting and presenting a choice to exit or return to the previous state (Figure 3-13).

Sometimes you may also want to present additional options. These are usually special exit conditions, such as choosing to exit with or without saving, as discussed under the Confirmation pattern.

A variant, shown in Figure 3-15, uses the Wait Indicator and a delay timer to provide oneclick exiting, as long as the user is willing to wait a short time. For immediate exit, provide an “Exit now” button for the user to select.

A subvariant of the timer, used for high-criticality applications, reverses the process. The user must select to exit in a short time (or continue pressing the exit button for a designated period), or the process will not terminate and will return to the last state.

Interaction details  
![](images/f869ce1f32f6b85434977308e48f73cce0dab95d46bda78f66b11bc0c4aab34e.jpg)

![](images/d828093237b9fbafc7c98a8b859579e439d6acb14d6bb0da65bab650a4c7b735.jpg)  
Figure 3-14. Titles, descriptions, and labels must be clear and easy to understand. If additional options are available, such as the example on the right, display those within the same dialog.

If additional selections are required, you may load them in any way needed, such as buttons in the Pop-Up, as a Select List, and so on. Use any soft keys or soft-key-like buttons for primary supporting actions, such as Cancel. In the example of exiting with unsaved documents, the choices to exit without saving and to save the documents would be in the dialog, and the option to return to the application would be labeled “Cancel” and would be the soft key conventionally used for this.

For devices with soft keys, even if the Pop-Up can be designed to hold all the required buttons, use soft keys for at least some expected actions. If “Back” is always on one of the soft keys, use that function as the “Cancel” function for this screen.

Keyboard and touch input buffers must be cleared the moment the exit selection is made. This will prevent accidental press-and-hold or multiple click-buffered input from skipping past the Exit Guard dialog. If problems continue to occur with this, add a brief delay (one-tenth of a second or less is usually enough) before accepting new input.

You may also wish to have no function selected by default on scroll-and-select devices (requiring a deliberate scroll and then a select to make either choice). Touch and pen devices may wish to consider the location of the dialog buttons relative to the original exit selection mechanism, to prevent accidental or too-easy input; requiring moving to a different part of the screen may provide a sufficiently deliberate action to avoid accidental activation.

Presentation details  
![](images/38814adbec7b42e44c3b9abb90f8a09941603af1946a8fb2facb13e12f2f9ae2.jpg)

![](images/d0e69269d6c67a4b2f9358e576203512e3c396f9b77121ead4792150c234772b.jpg)  
Figure 3-15. Delays may be used for convenience (left), or to add an additional level of assurance to the guard process (right). When describing press-and-hold or other special key behavior, the key can be iconically represented, and pointed at.

Timed Exit Guard dialogs must notify the user using tones and/or vibration, to ensure that they are seen. This may also be useful for conventional Exit Guard dialogs, to ensure that the user does not assume the application or process exited, and then does not check back for some time. Use the system-set volume or vibration settings in general, but always at least vibrate, even if set to no output at all. Remember, this only happens on user action, so it is not a notification and should not be detectable to others.

Make sure the Title of your dialog denotes the condition requested, usually something like “Confirm Exit,” “Exit?,” or another clear and actionable statement. See Figure 3-14 for labeling examples.

If this title is insufficient to explain the situation, because there are special conditions such as unsaved documents, a description should immediately follow the title. To explain a timed exit function, for example, a description might read “Hold the Power button for 5 seconds to turn off the device.” Be sure to add functions to this as required to make it reflect the condition accurately. For example, countdown timers should usually change the number in the description as an active countdown so that the user has a sense of how much time remains. If the button is released before the time required to exit, the dialog should remain on the screen for several seconds so that the first-time user, more familiar with short presses and taps, has a chance to learn the process.

If a press-and-hold function can be initiated modelessly (such as powering off the device by holding the Power key, which works from any screen), you should make a dialog appear as soon as the function is selected, to inform the user how to exit, or warn the user of the action.

Button labels must not depend on the description or title. Never present selections such as “Yes” and “No.” The best are along the lines of:

• “Exit”

• “Cancel”

where “Cancel” is the OS default label or icon for canceling or going back from the current process, and so should not be ambiguous. In this case, the process is the subset of the previous process, or the exit condition Pop-Up itself. The logic can get confusing if you think about it too much, so don’t. If there is no clear default label for cancel, use something unambiguous such as “Continue editing.”

When a choice is clearly the preferred one, it should be indicated as such. The OS standards should include a method of indicating button preference such as color, icon use, or border treatment. This may or may not be the safest choice; you will have to determine this during design based on the criticality of the process being canceled and the expected, most common use cases.

This dialog may carry additional cues such as being associated with the location of the button being used, and having a graphic of the button associated with it, perhaps in the title bar. This can even extend to pointing at the location of hardware buttons.

For touch devices, the pop up should spring from the virtual key being pressed, which should not itself move during this action.

## Antipatterns

Do not use Exit Guard for all applications and processes. Limit its use to only those that must be explicitly protected. If the OS you are designing for does not really exit, but keeps applications running in the background, Exit Guard will almost never be needed. Think about protecting user data, and only add explicit Exit Guard functions to the process after it has otherwise been designed and you cannot solve the problem in other ways. See more about the concept under Cancel Protection.

Use only a single dialog, with a single set of selections. Do not make exiting a process, where step 1 confirms exit, step 2 is deciding what to do with unsaved documents, and so forth.

## Cancel Protection

## Problem

Your app, site, or service is gathering user-entered data that would be time-consuming, difficult, or frustrating to reproduce if lost due to accidental user-selected destruction.

Many of these methods require relatively low-level software control or preservation of information, and so cannot be used on every platform. However, several variations are offered, so select whatever can be implemented for your product and users.

## Solution

![](images/7c80e93558c33579bea7f3c0cb2abcb583f20b212e1cf811d16b18718b014637.jpg)  
Figure 3-16. When a Clear Field widget is provided, an “Undo” button can be used to retrieve accidentally erased information.

Very simply, all the processes you design must protect or preserve user input. You have to provide methods to recover previous and historical entry.

This is a broad class of methods, and many of them have no explicit user interface, but instead simply offer the data at the right time. You cannot tack these on to existing systems well, and must plan for them at the early information architecture phases.

Don’t confuse this pattern with the explicit dialog solution for exiting (or canceling a process) under Exit Guard.

## Variations

One of the key principles of mobile design is to respect user-entered data. Design all your processes and interactions to avoid the loss of user-entered data. Design technical systems such as storage methods to automatically save entries and present them for retrieval. Three specific types of interactive design cases must be considered:

## Implicit protection

Design interactive methods to avoid exit or deletion. Take the example of deleting characters in a form field. If the convention in the OS would make an additional delete key press exit the field, and grant focus to the previous field, do not do this on automatic key repeat. This will avoid accidentally deleting the entry in multiple fields. Add a pause, or a hard stop, so that the user must release and repress the Delete key. This prevents deleting other fields, or with excessive acceleration, all fields in a form. We have seen this happen.

## Repopulation

When reentering a previously used but abandoned form, prepopulate the last-entered information. A Clear Entry method should be provided for the user to start a fresh form if the user intentionally abandoned it.

## Explicit protection

When a single function is provided to clear user entry, provide a method within the screen to allow recovery of the user-entered data, such as that shown in Figure 3-16.

## Interaction details

![](images/176aa7b2e711db9cc8837e33d990e68c3bfe245085aa137a4a8a13f2f9c2ca96.jpg)  
Figure 3-17. Be sure to differentiate historical, user-entered auto-complete entries from other sorts of results, by separating and labeling them.

Implicit protection methods may use any interactive or systematic methods, or any patterns outlined in this book. To find them, consider how any interactive system can be misused. Often, very small changes, such as clearing the scroll buffer as described earlier, can alleviate them. Larger changes must be considered carefully so that primary use cases guide the design, not rare or edge cases.

When the Clear Field widget is provided, and that method has been used, as long as the session is active, another function will be present that will recover the cleared information and display it in the field. If this is used when there is new content in the field, the user should be asked if she wants to add it to the newly entered information, or replace it with the recovered entry.

Autocomplete & Prediction processes should save user entries as they are being typed, so they are available for auto-complete even when accidentally deleted or an accidental loss of session (such as loss of signal) occurs. When entry into fields may be tedious or repetitive, or recovered user entry is available, display the auto-complete list of options as soon as a match is found with the current entry. To avoid overusing auto-complete, do not attempt to match until a few characters have been typed. The exact number will vary by type of entry and by the processing capacity of the device.

You can leverage the history, such as that used by web browsers, to let users revisit specific locations without recalling and reentering the same address, search, or other information. This should be displayed as a Hierarchical List grouped by session. See Figure 3-17 for a way to combine this concept with auto-complete.

Presentation details  
![](images/85ee424a51c87f78308f3160a26cf2b9f6a2c6a9aed4c948a1a61449ef558bcf.jpg)  
Figure 3-18. History works best when built as a Hierarchical List. For recovery of accidentally deleted user input, consider contextual use, such as loading the list into a Pop-Up.

Implicit protection methods are basically invisible to the user, and if you repopulate a form with previously entered data, it usually does not need an explanation.

For details on general Autocomplete & Prediction presentation, see that pattern. For the purposes of recovering user information, an indicator should also differentiate userentered information from community or spellcheck results, if several types are offered.

Displaying history with a Hierarchical List, as in Figure 3-18, is essentially as described in that pattern. Parent folders or groups should be labeled by the date and time the session occurred, using natural language to account for ranges; “Yesterday afternoon” is clearer than “1:20–3:45 p.m., 7 November.”

When you provide an undo process from a clear field, or a history link, make sure there is a clear label or use a well-understood iconic representation. If the OS uses a standard “Back” or “Cancel” icon, this is often a good choice and will fit the existing interactive language even if it is not used in the normal location. Text labels should label either the direct activity, such as “History,” or the recovery task, such as “Recent entry.”

## Antipatterns

Do not preserve secure information such as passwords and financial transaction information without informing the user.

Do not store any information as plain text that can be searched remotely or when stored as backup files, and do not keep all information forever. It is difficult to tell what information is secure to the user, and one person’s public knowledge may be another’s secrets. Assume everything is worth at least minimal protection.

## Timeout

## Problem

When designing high-security systems or those that are publicly accessed and are likely to be heavily shared (such as kiosks), you must include a timer to exit the session, or lock the entire system after a period of inactivity.

Timers and sensors are not available for some programming platforms and many web browsers, and so may limit the ability to offer a good experience for some users.

![](images/fec12b707c80f7721e4d2e7e03040c1a6d2d8559e5f8e1f118236e998103809e.jpg)  
Figure 3-19. When a period of inactivity is detected, either by a simple timer on-screen interaction, or due to sensors not detecting use of or proximity to the device, a Timeout notification is presented and the session may be terminated.

Many websites or web services use session timeout as a cost-saving measure to reduce load. Affinity-based load balancing is the default due to simplicity of sharing user data, but it requires that session-startup processes or overhead be left for all predicted users for a particular server.

Mobile interaction, even with websites, may be interrupted more than on desktops, and so should avoid such behaviors. There are other methods as well, so if system and data design is within the scope of your project, consider these as part of the overall design.

If your sessions must expire due to the method by which they have been built, consider making this transparent. Keep a log of the last-used location in the system, and when the user initiates new activity, resume at that state.

Mobiles are personal, so there is generally less worry about security of individual applications than on the desktop web, or for kiosks. Do not use old-school security practices by default, and only use them when necessary.

If session expiry is required for security purposes, try to work around it using sensors to detect when a user leaves or puts the device down for some time. Strict timeout dialogs, as in Figure 3-19, are based on desktop paradigms, where the computers do not have sensors.

When a strict timeout is needed, a modal dialog appears describing the impending loss of the session and presenting methods to preserve the session, as in Figure 3-20. When expired, additional information will be presented, and the user will be required to sign on again.

## Variations

When you must present an explicit timeout warning or notice to the user, there are several states and variations for doing so.

When the session expires, a Pop-Up will appear that states the session has expired. Depending on the needs of the system (load or security), the session may be restarted from the dialog, or dismissal may send the user to a Sign On screen to reauthenticate.

You may want an alert to appear before the session timeout. This may be very strident, such as a Pop-Up, or may simply be a countdown in the title bar or corner of the screen.

There may be multiple levels of timeout for security. For example, a banking application may require entering the passcode again when the first timeout is passed, but when a second, longer period of time has passed, the complete credentials must be reentered. These are mostly used on shared systems, such as kiosks, to prevent access by others when the original user has abandoned the session.

If secure information is on the screen when a timeout occurs, it may be necessary to obscure the information behind the notification dialog to ensure that no unauthorized users can see the information.

## Interaction details

![](images/d81d38a8100b5ba38cc200843f2780ea20e1f23747f9c4c488cd427554355fd1.jpg)  
Figure 3-20. Session and security details should not be routinely shared, mostly to avoid confusing the user. Describe the condition in clear, understandable language, and provide unambiguous, freestanding choices.

Determining the appropriate timeout requires careful consideration of the user’s tasks, their context, and the complexity of their interaction and entry of information for a screen, state, or process. Some guidelines for cognitive load are available, but often the best case is to simply run a test, even with your friends or with other employees, to get a sense of the time required to comprehend and enter information.

Mobile devices should use sensors to replace or supplement the timeout. If you have access to a camera, you can use it to determine whether a user leaves even a fixed device such as a kiosk. Face recognition is now available, and can already just barely be used to determine whether a particular user has likely left the field of view, or more than one person is in view of the screen. Shoulder surfing can be prevented by displaying alerts when more than one user can see the screen. For portable devices such as handsets, timeout can be based on the time the device is left unattended, by accessing the accelerometer information. This timing can be very short, since any application requiring this level of security can generally be assumed to take the user’s full attention; if the user sets the device aside, he may understand the need to reauthenticate to continue using the device securely.

When a Pop-Up is presented for timeout, this is a sort of reverse Exit Guard. The user will be presented with options to exit, but the primary condition will be to resume work. This will reset the timer, or load a Sign On screen or dialog as required by security needs.

If the timeout dialog is not used within a certain period of time, it may have a second timer, after which the system returns to its idle state. This is mostly used in shared systems, but may be useful for personal mobile applications where the primary function is consumption. The lost data will be saved as a draft message, as described in Cancel Protection. A notice should appear on this screen somewhere, informing the user of the loss of session and auto-saving of data.

When complete session expiry must occur, be sure the subsequent pages presented are useful and lead the user back into the system. Do not load full-screen errors, or the site home page. When requiring Sign On, use the identified user information when permitted by your security policy.

Continue presenting useful information throughout the expired session process. Once reauthenticated, return to the last location in the system, not to generic start pages or error pages due to loss of session identifiers.

It may be useful to present the Sign On information within the Timeout dialog, as shown in Figure 3-22. Even if this is technically possible, make sure it is not confusing, and does not exceed the space available. This is a case where tasks may need to be broken up to avoid complexity, even though it will slow down experienced users.

Presentation details

![](images/59860f8a51ff51183c3277eab9e60cf786d79ca75d96e1716abef782c9a0c408.jpg)  
Figure 3-21. It may be useful to include a countdown timer as the timeout approaches. If the user is otherwise aware of the consequences, or there is room to tell the user what will happen, this may help prevent inactivity before the Timeout Pop-Up is presented.

Timeout is a very critical condition, so it must be very clear. Anything less intrusive than a modal dialog often will not be seen.

The Pop-Up dialog must be titled and labeled clearly, but with as little technical jargon as possible. Describe the situation not as a “timeout,” but by stating the specific reason, such as “Locked due to inactivity” or “Since you walked away…” Emphasize security, and never admit other issues such as load, or discuss a session.

Button labels must not depend on the description or title. Never present selections such as “Yes” and “No.” At the same time, do not let options be too long, or they may not be readable or may not look like selections. Typical options are along the lines of:

• “Continue working”

• “Exit application”

However, these need to be contextually relevant—”Continue drawing” and “Stop banking,” for example. Cancel and close conditions, as they apply to the Pop-Up dialog, do not really apply here. Though the “Continue” label could be replaced with an action to dismiss the dialog, since it was system-initiated, the explicit label is clearer and more understandable.

If the user must sign on to continue, do not use generic labels such as “Continue working,” and state in the description that they must reauthenticate.

If on-screen data is determined to be secret enough that it must be obscured during timeout, you may do this by either making the dialog big enough to obscure all key information, or using a pattern to darken the screen. A simple 1-pixel checkerboard of clear and black (also an old trick before alpha transparency was common) will reduce type legibility as it is laid across. If it is still readable, change the scale of the pattern.

Use nonvisual methods to notify the user of the stop in process, such as audio and/or vibration. Follow current system volume settings for the notification. Mobiles are often used in quick glances, so the user may not notice such a stop in process for minutes or hours unless informed via a nonvisual channel.

If the timeout is very short, or when it begins to become very short (less than 30 seconds), it may be desirable to add a countdown somewhere on the screen, as shown in Figure 3-21. This must be labeled clearly, the timer should count individual seconds, and it should be slightly obtrusive. Make sure it appears from a blank area, instead of replacing another component; this, coupled with the movement of the clock, should make it reasonably visible.

![](images/2f2b4e3e98b577c4db11e1c90c92846ac0b42067bfc7b3944e4e4068a505ed81.jpg)  
Figure 3-22. The Timeout notice may also carry other useful information or processes, such as directly allowing reauthentication. Be careful to not provide too much information or too many choices, thereby confusing the primary message.

## Antipatterns

Do not let system or load calculations determine an acceptable timeout. Often, this will be the driving requirement after all, but fight for a user-based method of determining the correct timing.

Do not use desktop security models, or follow the practices of other products, to determine timeout for mobile or kiosk-based systems.

Never permanently expire the session without warning the user at the time the session expires. Otherwise, the user will attempt to continue entering information, and will receive an error message and probably lose the entered information. This can be difficult for web applications on many current mobile browsers due to JavaScript limitations, which is a key reason to consider other methods such as automatic resumption of the session.

Do not overprotect information. You should consider giving different portions of an application different timeout policies based on varying levels of security. Very rarely does information on the screen need to be obscured; transactional protection is much more common.