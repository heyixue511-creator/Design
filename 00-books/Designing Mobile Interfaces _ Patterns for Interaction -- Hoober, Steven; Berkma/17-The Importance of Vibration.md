# The Importance of Vibration

![](images/bb106c792359bb67ce0cd4bf08fee17cc7f402e3e1b0e43f332487bffa6fb015.jpg)

![](images/f5754a0dd90dba7968c4b220be21d21ef415aa60931a8eeb839213c4cf4911c8.jpg)  
Figure 12-3. Vibrate on most devices is coarse, and is provided by a simple motor with an off-center weight. Here, it is the silver cylinder between the camera and the external screen; the motor is mostly covered by a ribbon cable. It is mounted into a rubber casing, to avoid vibrating the phone to pieces, but this also reduces the fidelity of specific vibrate patterns, if you were to try to use it for that purpose. The figure on the right shows the motor assembly on its own.

Depending on our users’ needs, their sensory limitations, and the environment in which mobile is used, vibration feedback can provide another powerful sensation to communicate meaning.

Since the largest organ in our body is our skin, which responds to pressure, we can sense vibrations anywhere on our body. Whether we are holding our device in our hands or carrying it in our pocket, we can feel the haptic output our devices produce.

When designing mobile devices that incorporate haptics, be familiar with the following information:

• Haptic sense can provide support when the visual and auditory channels are overloaded.

• The touch sense can respond to stimuli just as quickly as the auditory sense, and can respond even faster than the visual sense (Bailey 1996).

• In high-noise-level areas or where visual and auditory detection is limited, haptics can provide an advantage.

## Common Haptic Outputs on Mobile Devices

Many mobile devices today use haptics to communicate a direct response to an action:

• A localized vibration on key entry or button push

• A ring tone set to vibrate

• A device vibration to indicate an in-application response, such as playing an interactive game (i.e., the phone might vibrate when a fish is caught, or when the car you’re steering accidentally crashes)

## Haptic Concerns

Using haptics appropriately is a great way to provide users with additional sensory feedback. However, you still need to be aware that:

• Using haptics can quicken the process of draining battery life. Provide the option to turn haptic feedback on and off.

• Use haptics when appropriate. Too much might reduce the user’s attention to the stimuli and ignore the response.

## Patterns for Audio and Vibration

Using audio and vibration control appropriately provides users with methods to engage with the device other than relying on their visual sense. These controls can be very effective when users may be at a distance from their device, or are unable to directly look at the display but require alerts, feedback, or notifications. In other situations, a visually impaired user may require these controls because they provide accessibility. We will discuss the following patterns in this chapter:

## Tones

Nonverbal auditory tones must be used to provide feedback or alert users to conditions or events, but must not become confusing, lost in the background, or so frequent that critical alerts are disregarded. See Figure 12-1.

## Voice Input

A method must be provided to control some or all of the functions of the mobile device, or provide text input, without handling the device. See Figure 12-2.

## Voice Readback

Mobile devices must be able to read text displayed on the screen, so it can be accessed and understood by users who cannot use or read the screen.

## Voice Notifications

Mobile devices must provide users with conditions, alarms, alerts, and other contextually relevant or time-bound content without reading the device screen.

## Haptic Output

Vibrating alerts and tactile feedback should be provided to help ensure perception and emphasize the nature of UI mechanisms. See Figure 12-3.

## Tones

## Problem

You must use nonverbal auditory tones to provide feedback or alert users to conditions or events, without them becoming confusing, lost in the background, or so frequent that critical alerts are disregarded.

Practically all mobile devices have audio output of some sort, and it can be accessed by almost every application or website. There can be strict limits, such as devices that only output over headsets, or those which only send phone call audio over Bluetooth, which can limit the use of some tones.

## Solution

![](images/dd8facf7286f40d7652ed41bf84a0266cc8e7d003be55e8b93344f4d4c9ae3f6.jpg)  
Figure 12-4. Feedback tones provide confirmation that the target was contacted correctly and that the device accepted the input. This is especially helpful for touch and pen devices, which have little or no tactile feedback, unlike hardware keys that move and (generally) click as part of the key action. Feedback has developed over time as a result of keys being obscured by the user’s finger or hand, so visual feedback is of limited value.

Interaction design, like much design work, focuses heavily on visual components. However, users of all devices have a multitude of senses, all of which can and should be engaged to provide a more complete experience.

Mobiles are carried all the time, often out of sight, and must use audio alerting and Haptic Output to get the user’s attention, or to communicate information more rapidly and clearly. Tones should be used not just for alerting or for problems, but as a secondary channel to emphasize successful input, such as on-screen and hardware button presses, scrolls, and other interactions.

Alerts are used to regain user focus on the device. Additional communication can then be made to the user, usually visually, with on-screen display of Notifications or other features. However, this may also involve Voice Readback or initiating voice reminders.

Whenever you are implementing this pattern, be aware of the danger of the “better safe than sorry” approach to auditory Tones. Too much sound can be as bad as too little in that it can add confusion or induce alarm fatigue. At its worst, this can be akin to the well-known phenomenon of banner blindness with some or all device tones simply edited out by the user’s brain.

## Variations

Feedback tones are used to provide direct response to a user action. You can serve up a tone as alternate and immediate feedback to indicate that the system has accepted the user action. This is usually a direct action such as a button press or gesture. This style of feedback developed in the machine era, as a result of the user’s fingers and hands obscuring the input devices; even when a button moved or was illuminated, more efficient input was ensured by the inclusion of auditory and Haptic Output. See Figure 12-4.

Alerts serve to notify the user of a condition which occurs independent of an action, such as a calendar appointment or new SMS. These also date back far before electronic systems. Due to the multitude of alarms, control systems such as those used for aircraft and power plants are more useful antecedents to study than simple items such as alarm clocks. See Figure 12-5.

Delayed response alerts exist in a difficult space between these two—for example, when an action is submitted and a remote system responds with an error several seconds later. The response is in context, so it is similar to a feedback tone, but it needs to inform the user to look at the screen again, much as an alert.

## Interaction details

Phenomena such as the McGurk effect—in which speech comprehension is related to the visual component—appear to exist for other types of perception. Tones should support interaction that is directly related to the visual portions of the interface.

Tones must always correspond to at least one visual or tactile component. If an alert sounds, you should always make sure there is a clear, actionable on-screen element. These should always appear in the expected manner for the type of event. Feedback tones correspond to key presses or other actions the user takes, and alert tones should display in the conventional method the device uses for Notifications.

Displayed notifications must not disappear without deliberate user input. Users may not be able to see the screen or act on a particular alert for some time; the visual display to explain the alert must remain in place.

Use caution with reminder alerts, or repeatedly announcing the same alert again. You should generally only use these for conditions that are time-sensitive and require the user to perform a real-world action, such as an alarm clock. There is generally no need to repeatedly sound an audible alert for normal-priority items such as email or SMS messages.

Alert silencing—removing the auditory portion or the audible and LED blinking portion of an alert—should be unrelated to any other notifications. It should be possible to silence an alert without dismissing the entire condition. Often, this can be done by simply opening or unlocking the device; if the device was previously in a locked mode, the user can be assumed to have seen and acknowledged all conditions. You can stop sending tones, but until the user has explicitly dismissed the message, the alert condition is marked as unread.

![](images/bf23fe60378c8661421ec40cf4e17ce4b48e41b0f1b7f8e2ab05d7ce3c508c67.jpg)  
Figure 12-5. A sample process by which alerts are displayed, with audio as a component. While the device is idle and locked, the alert condition occurs. The device LED illuminates and the alert tone plays. The user retrieves the device and taps the power button to illuminate the lock screen; this user action silences the audio alarm immediately, but does not cancel the alert otherwise, so the LED and notifications remain in place. Once the user unlocks the device, the notification will appear in the conventional location on the Idle screen, and can be interacted with as usual.

## Presentation details

Any Tones you send must correspond to the class and type of action, and should imply something about the action by the type of tone. Clicks denote key presses, whereas buzzers denote errors, for example.

Sound design is an entire field of study. If sounds must be created from scratch, a sound designer should be hired to develop the tones based on existing principles. Be sure to denote the meaning—and emotional characteristics—for each sound.

Vibration and audio are closely coupled, so you should consider them hand in hand. If Tones are used in concert with Haptic Output, ensure that they do not conflict with each other. For devices without haptic or vibration hardware, audio can serve this need in a limited manner. Short, sharp tones and especially those at very low frequencies provided through the device speaker can provide a tactile response greater than their audio response. Test on the actual hardware to be used, to make sure the device has appropriate responsiveness and that low-frequency tones do not induce unwanted buzzing.

The “illusory continuity” of tones can be exploited in a manner similar to how “persistence of vision” is for video playback. Simple tones can be output with gaps or in a rapid stairstep and be perceived to be a continuous tone. You can use this to simulate higherfidelity audio than can be achieved on devices with constrained processing hardware, or when the rest of your application is using so much of the processor power that you need to make components such as the audio output more efficient.

Do not allow alerts or other Tones to override voice communications. Many other types of audio output, such as video or music playback, may also demand some tones be greatly reduced or entirely eliminated.

Generally, alerts can be grouped. If three calendar appointments occur at the same time, only one alert tone needs to be played, not three in sequence. Never play more than one tone at a time. You only need to get the user’s attention once for her to glance at the screen and see the details.

Use caution with the display of multiple alerts that closely follow each other. If the user has not acknowledged an incoming SMS and a new voicemail arrives moments later, there may be no need to play the second alert tone. The delay time required to play a second alert tone depends on the user, the type of alert, and the context of use.

Carefully consider audibility, or how any sound can be perceived as separate from the background. You can use automatic adjustments by opening the microphone and analyzing ambient noise. However, do not simply make sounds louder to compensate for this. Adjust the pitch or select prebuilt variations more appropriate to the environment.

Be aware of the relationship between pitch and sound pressure, and adjust based on output volume. Consider using auditory patterns (or tricks) such as Sheppard-Risset tones to simulate rising or falling tones, which can be more easily picked out of the background or located in space.

## Antipatterns

Alarm fatigue is the greatest risk when designing notification or response Tones. If your audio output is too generic, too common, or too similar to other tones in the environment (whether similar to natural sounds or electronic tones from other devices), it can be discounted by the user. Use as few different sounds as possible. This may be deliberate, where the user consciously discards “yet another alert” for a time, or unconscious as the user’s auditory center eventually filters out repeated tones as noise. This can even result in users sleeping through quite loud alarms because their brains consider the tone to be noise.

Do not go too far in the other direction and have no auditory feedback, especially for errors. Delayed response conditions are especially prone to having no audible component. This induces a great risk in users who may believe they have sent a message or set a condition to be alerted later, and may not look at the device for some time.

It is even possible for accidental entry, or deliberate eyes-off entry, to clear a visible error so that users are not informed of alerts or delayed responses at all. Be sure to use notification Tones whenever the condition calls for it.

Keep in mind that users may be wearing headsets. Using tones to emulate Haptic Output will not work in this case, and can be very annoying. Consider changing the output when headsets are in use. In addition, some headsets will not accept all output, so if your application relies on tones, make sure there is a way for the device to still make these sounds.

## Voice Input

## Problem

You must provide a method to control some or all of the functions of the mobile device, or provide text input, without handling the device.

Most mobiles are centered on audio communications, so they can accept Voice Input in at least some ways. Some application frameworks and most web interfaces cannot receive inbound audio, but there are sometimes workarounds, using the voice network. Devices not built around voice communications may not have the appropriate hardware and cannot use this pattern at all.

## Solution

Voice Input has for many decades promised to relieve users of all sorts of systems from executing complex commands in unnatural or distracting ways. Some specialized, expensive products have met these goals in fields such as aviation, while desktop computing continues to not meet promises, and not gain wide acceptance.

Mobile is, however, uniquely positioned to exploit voice as an input and control mechanism, and has uniquely higher demand for such a feature. The ubiquity of the device means many users with low vision or poor motor function (and thus poor entry) demand alternative methods of input. Near universal use and contextual requirements such as safety—for example, to use navigation devices while operating a vehicle—demand eyesoff and hands-off control methods.

And lastly, many mobile devices are (or are based on) mobile handsets, so they already have speakers, microphones designed for voice-quality communications, and voice processing embedded into the device chipset.

Since most mobile devices are now connected, or only are useful when connected to the network, an increasingly useful option is for a remote server to perform all the speech recognition functions. This can even be used for fairly core functions, such as dialing the handset, as long as a network connection is required for the function to be performed anyway. For mobile handsets, the use of the voice channel is especially advantageous, as no special effort must be made to gather or encode the input audio.

![](images/cf868a5ed3f230b156579abd8c7ef078fdae612f5becbbaa4dc941ec2df76e92.jpg)  
Figure 12-6. Voice input must be considered as an entire replacement UI, with Voice Readback as the output channel. Use the same principles of organizing information and communicating clearly but concisely when designing voice overlays to a conventional UI. State changes must be clearly communicated, as the user cannot necessarily glance at the interface to see what is happening. Here, the initiation of the voice interface and the acceptance of the command are stated. Note how the user input was read back not as stated, but as interpreted by the system.

## Variations

Voice command uses voice to input a limited number of preset commands. The commands must be spoken exactly as the device expects, as the device cannot interpret arbitrary commands. These can be considered akin to Accesskeys, as they are sort of shortcuts to control the device. The command set is generally very large, offering the entire control domain. Often, this is enabled at the OS level and the entire handset can be used without any button presses. Any other domain can also be used; dialing a mobile handset is also a common use, in which case the entire address book becomes part of the limited command set as well. See Figure 12-6.

Speech-to-text or speech recognition enables the user to type arbitrary text by talking to the mobile device. Though methods vary widely, and there are limits, generally the user can speak any word, phrase, or character and expect it to be recognized with reasonable accuracy.

Note that voice recognition implies user-dependent input, meaning the user must set up his voice profile before working. User-independent systems are strongly preferred for general use, as users can use them without having to set them up. Only build user voice profiles when this would be acceptable to the user, such as when a setup process already exists and is expected.

A detailed discussion of the methods used for recognizing speech is beyond the scope of this book, and is covered in detail in a number of other sources.

## Interaction details

Constantly listening for Voice Input can be a drain on power and can lead to accidental activations. Generally, you will need to provide an activation key press which either enables the mode (Press-and-Hold to input commands or text) momentarily, or switches to the Voice Input mode. A common activation sequence is a long press of the speakerphone key.

You will need to find other keys or methods when there are no suitable hardware keys. Devices whose primary entry method is the screen (touch or pen) may have trouble activating Voice Input without undue effort by those who cannot see the screen.

Consider any active Voice Input session to be entirely centered on eyes-off use, and to require hands-off use whenever possible. Couple the input method with Tones and Voice Readback as the output methods, for a complete audio UI.

When input has been completed, a Voice Readback of the command as interpreted should be stated before it is committed. Offer a brief delay after the readback, so the user may correct or cancel the command. Without further input, the command will be executed.

For speech-to-text, this readback phase should happen once the entire field is completed, or when the user requests readback in order to confirm or correct the entry.

You must carefully design the switch between voice command and speech-to-text. Special phrases can be issued to switch to voice command during a speech-to-text session. Key presses or gestures may also be used, but may violate key use cases behind the need for a Voice Input system.

Correction generally requires complete reentry, though it is possible to use IVR-style lists, as examples or to allow choosing from list items.

You should consider the use of voice command in the same way as the use of a five-way pad for a touchscreen device. Include as much interactivity as possible, to offer a complete voice UI. When controlling the device OS, you must enable all the basic functions to be performed by offering controls such as Directional Entry and the ability to activate menus. This also may mean a complete scroll-and-select-style focus assignment system is required, even for devices that otherwise rely purely on touch or pen input.

Provide an easy method to abandon the Voice Input function and return to keyboard or touchscreen entry, without abandoning the entire current process. The best method for this will reverse the command used to enter the mode, such as the Press-and-Hold speakerphone key.

## Presentation details

![](images/5e93ae7b7b787215e3e333c1d018d56cc4b88ac2e76a38566ba9d50470a927fa.jpg)  
Figure 12-7. Whenever there is space, such as in this dedicated search box, selecting voice control or entry should communicate the mode switch with icons and labels, and describe the actions to be taken, or the action the system is taking, very clearly. Additional hints, and links to get even more information, can also be provided.

Whenever the Voice Input mode becomes active, you should make it announce this in the audio channel with a brief tone. When this is rarely used, for first-time users or whenever it may be confusing, a Voice Readback of the condition (e.g., “Say a command”) may be used instead. After this announcement is completed, the system accepts input.

All Voice Input should have a visual component, as in Figure 12-7, to support glancing at the device, or completing the task by switching to a hands-on/eyes-on mode. When in the Voice Input mode, this should be clearly denoted at all times. The indicator may be very similar to an Input Method Indicator, or may actually reside in the same location, especially when in speech-to-text modes.

Hints should be provided on-screen to activate voice command or speech-to-text modes. Use common shorthand icons, such as a microphone, when possible. For speech-to-text especially, this may be provided as a mode switch or adjacent to the input mode switch.

When space provides—such as a search, which provides text input into a single field—you should display on-screen instructions so that first-time users may become accustomed to the functionality of the speech-to-text system. Additional help documentation, including lists of command phrases for voice command, should also be made available, either in text on-screen or as a Voice Readback.

## Antipatterns

You cannot rely on audio systems and processing to be full duplex, or to be heard at full fidelity while speaking. Give decent pauses, so tones and readback output don’t get in the way of user inputs. Consider extra cognitive loads of users in environments where

Voice Input is most needed; they may require much more time to make decisions than in focused environments, so pauses must be longer than for visual interfaces. These timings may not emerge from typical lab studies even, and will require additional insights.

## Voice Readback

## Problem

You must allow certain classes of users or any user in certain contexts to consume content without reading the screen.

Practically all mobile devices have audio output of some sort, and it can be accessed by almost every application or website. There can be strict limits, such as devices which only output over headsets, or those which only send phone call audio over Bluetooth, which can limit the use of some tones.

## Solution

Mobile devices must be able to read text displayed on the screen for the user, so it can be accessed and understood by those who cannot use the screen.

Due to mobiles being contextually employed, there are numerous instances in which the user may not be able to, not be allowed to, or choose not to read the screen.

The user may well choose to use Voice Readback so that she can use her hands and eyes for other purposes. While working, or performing hobbies which do not require excessive cognitive load themselves, such as most driving, radio and other audio output is used to gather information or provide entertainment. Video is generally more entertaining, but is totally unsuitable for these situations.

![](images/b1e945655e122bc1e53a43aa77c5256a199fca7a72fbc740099b5e4ee93f6bc0.jpg)  
Figure 12-8. Voice Readback can form an integral part of a complete voice UI for mobile devices. Readback is used to prompt for commands, and then confirms the user input or declares how the system has interpreted the command. It will also read on-screen displays and options, to allow the user to select appropriate items without looking at the screen.

## Variations

Voice Readback always works in broadly the same way, but what is being read varies:

## Universal

The entire interface is read, to allow the device to be used without any view of the display. This is usually combined with the Voice Input pattern to create a complete voice UI, as an alternative to the conventional button (or touch) and screen UI native to the device. Even if used for only one section, action, or phrase, this same method is used for any readback of voice commands. See Figure 12-8.

## Elemental

An entire document, such as a PDF, email, or web page, is read until the user cancels the action or the entire document is read. See Figure 12-10.

## Selected

A selection the user has specified within any context—for example, by highlighting text in a web page—is read in its entirety. See Figure 12-9.

Voice output that is presented based on conditions, such as position or time, is discussed under the Voice Notifications pattern.

Interaction details  
![](images/ea2514a0e7e27fd85a69921ac9436dcf3a5ea771e3a1c2db1eaa32337f2b93ea.jpg)  
Figure 12-9. Selections made by the user can be read. The play control is usually contextual and is related to the selection such as the Pop-Up menu shown here.

Voice Readback can be turned on as a setting for the entire OS, or on an application basis.   
It will then be used automatically, whenever a change in the application is initiated.

Other input methods, such as keypads and directional controls, will still function. Buttons will generally be needed to unlock or refresh a screen so that the current condition is read aloud.

Readback can also be initiated, for the elemental and selection variations, within the application or as a contextual control such as a Pop-Up, menu, Annotation, or other control.

Readback for single-use cases of UI control is the result of Voice Input. Initiation is discussed under that pattern.

![](images/9a7e6f5b5a20a7e08412d772e687ec187ab59472f08b422fa68fb499073b748d.jpg)  
Figure 12-10. When entire documents, long passages, or even just marquee text is being read, the document will scroll to always have the current reading selection visible in the viewport. A cursor or highlight, as shown here, should be displayed to correspond to the word currently being read. An indicator of audio playback should be on the screen at all times, and a control should be provided to immediately mute or pause the audio.

Audio should be played by default through the external speaker or speakerphone. The last-set in-call volume (or equivalent playback volume for nonphones) should be used. Whenever possible, detect the ambient noise level and adjust the volume accordingly, in order to make it audible.

When a headset is attached (either physically or by a link such as Bluetooth), the playback should default to this device, and use the last-set in-call volume for this device.

Content read must be identical to that printed on the screen. The condition that resulted in the user employing Voice Readback may be temporary and transient. Allow the user to switch between the screen and audio channels. The user may even wish to read along with the voice output. Even for users with a vision deficit, others may be accompanying them, who may also wish to use the device.

Also be sure that content scrolls as the audio gets to that part so that the item being read back is in the viewport.

There may be delays between phrases, or before the start of the audio readback. To inform the user that audio is about to commence and to prepare the user for the volume level, play a subtle tone immediately beforehand.

Use a similar tone when Voice Readback has stopped for a significant time, or to communicate a selected volume setting, to confirm this condition to the user.

## Antipatterns

Avoid mixing readback of commands and text. When the two must be used together, use delays, tones, changes in voice, and clear syntax (such as “You said...”) to indicate the difference.

The voice you select must be as understandable as possible. Text-to-voice translation of names especially can be difficult to understand or improperly pronounced. If quality is too low with the available hardware and software, do not implement the solution.

Keep in mind that users may be wearing headsets. Some headsets will not accept all output, so if your application relies on Voice Readback, make sure the targeted devices support your application or service sending audio to all attached headsets or other audio devices.

## Voice Notifications

## Problem

You must inform certain classes of users—or any user in certain contexts—of conditions, alarms, alerts, and other contextually relevant or time-bound content without requiring them to read the device screen.

Practically all mobile devices have audio output of some sort, and it can be accessed by almost every application or website. There can be strict limits, such as devices that only output over headsets, or those that only send phone call audio over Bluetooth, which can limit the use of some tones.

## Solution

Much as Notifications appear on the device screen (and sound alarms and blink the LED) when messages arrive or other such alerts activate, Voice Notifications read the content of a notification so that the information can be used when the device is not in the hand or cannot be viewed.

These can be especially useful for users or contexts in which reading would be difficult. A common case is turn-by-turn directions. The reminders are based on telemetry information instead of time (like alarms) or remote information (like messages), but the principle is identical: a message is read, without specific user input, at the relevant time.

Voice Notifications also allow the screen to remain available for the display of other content. It may be able to be glanced at to retrieve certain types of data (such as a map, in the navigation example), but not to the level or type of detail of the read-aloud text.

![](images/23a06162bc7ced828470f184158c50b390919e13f631587c3fc15c47342762ba.jpg)

![](images/a0531bc823691b46585a513f2adcced5dbfedc8a1efe34d98ea9e4f70e3d83bd.jpg)

![](images/aeabead3df26434a31d9be547273ebebb9bb14562ce531ecef427cf916d2da3a.jpg)  
“Time to take your 3:45 pill... Take one blue and yellow, 500 milligram Abelcet, with water.”  
Figure 12-11. The best way to notify is to use technologies such as push messaging, supported by a surprising number of devices, on most networks. Remote messages can launch the application, then not only read the alert but also present a correspondingly well-formatted page to look at. Note that the audio only plays when the entire message has loaded, so the user may glance at the device to get other information and follow along. The audio must always be able to be paused or stopped, in case it is disrupting an event or the user has privacy concerns.

## Variations

There are only two basic variations:

## In context

The device is operating in the mode or application from which the alert is launched. Often, the alert is integral to the application, and on-screen display accompanies the alert in a critical manner. Turn-by-turn directions are the key example of this variation. See Figure 12-12.

## Change of context

The device is in an arbitrary mode, on the Idle screen, or locked when the alert is read from an application that is not in focus. A simple example is any typical notification, such as an appointment or incoming SMS. See Figure 12-11.

If the user requests voice output, or voice output is used as a part of generally navigating the device UI, this is a Voice Readback pattern instead.

## Interaction details

Voice Notifications occur based on time, position, remote messaging, or other actions outside the user’s direct control.

Treat reminders currently being read the same way as other alarms. Make sure they appear in the Notifications area, or as Pop-Up dialogs, as the rest of the OS standards dictate. You must also enable the same actions; they may be muted, snoozed, or canceled. Do not snooze alarms that are irrelevant at a later time, such as position-related messages.

If the voice component is muted, this is the same as silencing an alarm of Tones. The notification itself will remain in the Notifications area, and may be manually selected and viewed (or listened to), or be cleared.

A privacy mode may only read a generic version of the message. When the user interacts with the device, a more detailed message can be seen, or read aloud. This will rapidly become the Voice Readback pattern. See that for specifics of the design and interaction.

Consider informing users of the risks of reading private data aloud when setting up Voice Notifications, and provide methods to change or cancel them easily.

Presentation details

![](images/e85bc85274f9a82171207e1e0e7ba7422c4621bbc45d49f2fe86b352becf0748.jpg)  
“Turn coming up... Turn right onto Missouri Highway Y - Y in 500 yards... 6 miles to next turn.”  
Figure 12-12. In-context Voice Notifications are most often used for features such as turn-by-turn navigation. The display is mostly reserved for pictorial displays of information, which are more glanceable and allow multiple types of information to be presented at once. A summary of the audio message should be presented on-screen, even if you expect it to be unreadable; the user may change contexts (e.g., stop the car), another individual may be able to assist the user, and the mere presence of the information box reinforces that the message is originating from this device and relates to this task.

Make sure all alerts are presented visually, as well as via audio. See the patterns under Notifications for display of notifications. Even when in context, the alert should be noted in some manner, though this may be more specific, such as an Annotation over a map. Only use Pop-Up dialogs or other intrusive measures when absolutely required.

To inform the user that audio is about to commence and to prepare the user for the volume level, play a subtle tone or unimportant audio message immediately beforehand. This may also be the normal alert tone to emphasize that the device is communicating an alert. Make sure the volume of this tone is similar to (or lower than) the audio to be read aloud, as the intention is not just to consciously alert the user, but to prime the user’s auditory system for receiving messages.

Use syntax that makes it clear what is being communicated and attempt to give users a moment to acclimate to the voice and the instruction format, even after any notification Tones. For example, state the type of message or action the user must take, then the details:

• “Turn coming up . . . turn right in 500 yards.”

• “Time to take your medications . . . take one Ritalin now.”

Repetition generally is not perceived in a negative way in spoken phrases as it is in print, due to the immediacy and the way audio versus visual perception works.

Use caution when choosing what sort of content will be read—and to what level of detail. Alerts will generally be sent through the speaker, so they have minimal privacy. Since anyone nearby can hear, messages must be formatted to be general or have no explicitly secret information. For example, instead of stating the medicine and dosage as noted earlier, the message could just be, “Time to take your medication. . . . Be sure to take it with a meal.”

Use a consistent voice and tone of voice for all notifications. This way, the user can become accustomed to the reminder, and be able to comprehend the intent without listening as closely to opening phrases.

## Antipatterns

Avoid “blurting out” alerts or instructions, especially with important information in the beginning of the phrase. Directions such as “Turn right in 500 yards” are often not useful, as the user is still acclimating to the voice speaking through the direction statement; the user may only hear “...in 500 yards.”

Voices provide strong emotional responses, and when the user is not accustomed to them or expecting them, they may be startling. Avoid using Voice Notifications when users are asleep, and be sure to precede all notifications with Tones to make it clearer that this is a machine, not a scary intruder sneaking up from behind.

The voice you use must be as understandable as possible. Even within a single language, be sure to use the most generic accents possible, and be aware of regional idioms.

Text-to-voice translation of names especially can be difficult to understand or improperly pronounced. If quality is too low with the available hardware and software, do not implement the solution.

## Haptic Output

## Problem

You should use vibrating alerts and tactile feedback to help ensure perception and emphasize the nature of UI mechanisms.

Haptic vibration is available on many devices, and can be activated by most any application. The use of sound to simulate vibration is a viable alternative. Future technology will improve many aspects, and may broaden the base of devices with this feature.

## Solution

Haptics refers to receiving information by touch. Practically, with current, generally available technology, this refers to the use of vibration to communicate with the user. In much the same way that mobiles have evolved to contain a variety of sensors, they also have a broad range of output devices; most mobiles have some sort of vibration, or an external speaker, which can be used for at least basic Haptic Output.

These vibrations are generally propagated through the entire device, but they can be localized, or placed only in specific components, such as the pen in a Pen Input device.

Most vibration is very coarse and is accomplished by a simple off-center weighted motor. Control is only by intensity and switching the motor on and off. Transducer-based vibration is rarer but also available, using tools typically employed for audio output to make more nuanced vibrations. This may simply involve the bone conduction transducer (BCT) included for use of hearing-impaired users being repurposed for general Haptic Output. Use of the BCT for general audio output is not part of this pattern, and is otherwise beyond the scope of this book.

Additional methods of haptic output are being developed in the laboratory, and may appear in production soon. These include the ability to sense objects that are not physically present, enabling tactile virtual keyboards, for example.

Variations

![](images/913ded8b9ed012c68fa9fea53e415809948deaad6869b38eec5f5ef582f7d8b7.jpg)  
Figure 12-13. When the user performs a function on the device, haptic response can make this more obvious, can confirm that it happened, and confirms that the device perceived and is reacting to the action. For touch devices, the haptic response takes the place of physical response, and allows more natural and assured use of the interface.

For mobile devices, Haptic Output is currently used in two ways, both of which are dynamic output methods:

## Response

When the user makes an action, the device confirms that it has received and understood the action, and makes it seem more real by adding a response. Most typical is a “click” when virtual buttons are used, but any action may use this, including scrolling, gestures (the system indicates when a complete gesture is accepted), and even the use of physical buttons. See Figure 12-13.

## Notification

Alert lights and tones, used to notify the user of events when out of context, may be emphasized or replaced with haptics. Vibrate has been heavily used for this for so long that it has become a well-understood pattern by the general population. Vibration also helps users detect alerts when the sound is off or muffled, and can help to local ize the device when in a pocket or purse. For additional details, especially on display in other channels, refer to the Notifications and Tones patterns. See Figure 12-14.

As discussed earlier, haptics may soon also be used for other types of tactile output. Especially useful will be the ability to detect shape and texture—to allow users to feel virtual on-screen elements. This will form a third variation of output perceived by the user to be passive and representing static, physical spaces and objects. It may even enable new interactions, where users may turn dials around a resisting axis, or be able to pinch and grab UI elements as though they are physical objects.

## Interaction details

Use Haptic Output to emphasize that an action happened or to communicate in another channel, when users may not notice audio or visual cues. You should never use haptics alone, and must only use vibration to reinforce actions by the user, reactions on-screen, or displays on-screen, by LED or by audio.

Phenomena such as the McGurk effect—where speech comprehension is related to the visual component—appear to exist for other types of perception. Vibration should support interaction with the visual portions of the interface, by being related to the physical area interacted with whenever possible and by having a corresponding visual or physical component.

If an alert is expressed as Haptic Output, you should always have a clear, actionable onscreen element. These should always appear in the expected manner for the type of event, as described in the Notifications pattern.

Haptics resulting from key presses or other actions the user takes should be the only response aside from the intended action (e.g., typing the character). You can also use them to support a Wait Indicator, or replace them for very short time frames (less than one-quarter of a second), when indicating that the device has received and understands the input.

Consider Haptic Output for Notifications, including ring tones, to be contiguous with the volume control system. Vibrate is the setting between off and the lowest level, or it can be enabled as a switch so that it is on (or off) at all volume levels. While being used, vibration will be silenced in the same manner and at the same moment as Tones or Voice Notifications are. The same mute, cancel, or silence function will be presented when only vibration is enabled, and there is no audio output.

Presentation details

![](images/d613ae5f4b13c0c4e35b35c07f476ebb8a95df3b1acc04ec7a15aad6f09e8737.jpg)  
Figure 12-14. Notifications can use vibrating output to help users locate the device, or to provide a (generally) more silent “ring tone” than audio output. Typically, vibrate is activated alongside tones. Be sure to alternate audio and vibrate, to avoid the two conflicting with each other.

When using Haptic Output as response items, you should not use haptic vibration generically but have the signal carry meaning in much the same way audio does. Clicks should feel like clicks, errors should be harsh as though being rejected, and so on.

When emulating real objects, the tactile characteristics of those objects can be measured, and codified for the simulation. Tricks of audio playback sometimes work for vibration; this is in fact why vibration can be used to simulate tactile perception. However, touch is different from audio, so different guidelines must be used and specialists in the design of vibration should be employed.

For devices without haptic or vibration hardware, audio can serve this need in a limited manner. Short, sharp tones, or very low-frequency tones, output through the device speaker can provide a tactile response greater than their audio response.

Very low bass tones can provide some of the best response, and most speakers can actually generate tones below the threshold of human hearing. However, devices are generally not designed in this manner, so the amplifier hardware may not go this low, the software to access the hardware may not accept output this low, or the tones can generate distractingly improper resonance in the case, ruining the effect. Test on targeted devices before use.

Also use care when generating tones at the edge of human hearing with the intent of using them purely as haptics. Younger populations, and certain individuals, have wider ranges of hearing and may be able to detect it audibly. This may be an acceptable side effect, but ensure that it is not distracting or interferes with the use of audio in other frequencies for those users.

Vibration and sound are closely coupled behaviors and can influence each other in undesirable ways. When both are needed, they generally must be alternating to avoid conflicting with or modifying each other. Vibration devices can cause unintended buzzing or other distorting resonance in audio devices. Alerts, for example, generally vibrate briefly, then sound a brief tone, and repeat this until the notification alert time expires or the user cancels or mutes the output.

## Antipatterns

Do not overuse Haptic Output without a good understanding of all effects of the device hardware. Besides the audio conflicts described earlier, if traditional motor-driven vibration is used it may consume the battery excessively quickly.

Do not play multiple vibrations at one time. Even if the device supports this, they cannot generally be perceived accurately by the user, and may end up as noise, even if in multiple localized areas.

Make sure haptic alerts send vibrations repeatedly. Phantom ringer behaviors are known to exist for vibration as well as audio; single vibrations may be written off as an accident of perception by the user, and the alert will be missed.

When employing an audio output device for haptic vibration (either the device speaker or the BCT), audio has priority, especially when used for playback of media or for ongoing communications. Never interrupt the voice channel of a call to play a haptic alert.

Haptic output can easily induce alarm fatigue in the same manner as for alert Tones. If the alert method is too generic, too common, or too similar to other tones in the environment (whether similar to natural sounds or electronic tones from other devices) the user can discount the alert. Use as few different sounds as possible, but avoid using simple “vibrate” for every alert. Note that disregarding alerts is not always a deliberately conscious action; the tone or vibration is eventually considered noise by the user’s brain, such that it will not longer be noticed.