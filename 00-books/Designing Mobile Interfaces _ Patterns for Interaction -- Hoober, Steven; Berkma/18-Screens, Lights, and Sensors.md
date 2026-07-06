# Screens, Lights, and Sensors

## The Relationship

Let’s travel down memory lane. Take a moment to think back to your first date. Stop! Just kidding; that’s outside the scope of this book. But do take a moment to remember when you bought your first cell phone. Even though I bought mine some time ago, I clearly remember the exact year, model, and reason I bought it in the first place.

The year: 1997, while in college.

The model: Motorola StarTAC, 2G GSM; 4 × 15 character, monochrome graphic display (see Figure 13-1).

The reason: Cool factor! A flip phone and the smallest cell phone available. I could send and receive calls, SMS, and store up to 100 contacts. And I could show it off ever so smoothly when I clamped it onto my belt. Back then, that was all the functionality I could ever want! It was love at first sight!

## The Breakup

Well, I’m sad to say that that phone is no longer with me. I’ve had to keep up with the times and the technology. Since that StarTAC, I’ve gone through an extensive number of mobile phones. I believe the count total now is eight. That number seems reasonable, considering the rate at which people upgrade their mobile phones today—once every 18 months, according to Gizmodo.com. Today, my mobile requirements consist of greater interactive control and highly visible functionality on a powerfully crisp and color display. That original 4 × 15 monochrome graphic display, if used today, would be quite limiting and unsatisfying.

![](images/d0e9b1ff034498982595c6821dd0907fb4abfaf88fe685455958aa63fcca0cab.jpg)  
Figure 13-1. Over time, display technology has improved dramatically. Now color depth and resolution are high enough that traditional pixel-based display concerns are beginning to change. However, there is still a trade-off in cost and power consumption. Devices will always have a variety of screen quality levels. By the way, on the left is a StarTAC, just like my first phone.

## I’m Not “Everyman”

Not everyone needs what I need in a mobile phone. Mobile design is never about you and me. It’s about all the other people who are using a range of multiple devices, with varying needs in limitless contexts.

Here are the things we must consider in terms of screens, lights, and sensors in order to create an enriching user experience while considering everyone:

• Context of use

• Display size

• Display resolution

• Display technology

## Context of Use

One of the mobile design principles centered on in this book is that mobile devices must work in all contexts. They must function properly and behave appropriately in a variety of environments. Let’s consider the following contexts that can affect the way we interact with a mobile display.

## Outdoors

The outdoors is the most complicated environment to design around. It’s highly unpredictable, constantly dynamic, and uncontrollable. External stimuli such as bright sunlight, cloudy days, moonlight, darkness, and street lights aren’t controlled by the user. We can’t just switch on and off the sun or blow the clouds away. All of these stimuli can make it more difficult to view the screen, thereby affecting the way our users interact with the device.

## Indoors

The indoor environment may be more predictable, less dynamic, and more controllable than the outdoors, but it is still highly complicated. External stimuli present may include natural light from windows, doors, or skylights, or generated light from bulbs, fluorescent light, incandescent light, LEDs, halogens, and high-pressure sodium lamps.

## Both

Mobile users are constantly transient, which changes their environment. They may use their device outside in daylight to read the news, and then walk inside a public building with dim lighting.

This change affects the amount of time it takes our rod receptors in the back of our retina to respond to light differences. The greater the difference between the two environments, the longer it will take our eyes to appropriately adjust. This affects our ability to quickly detect and identify details in that time—such as text, small images, and even controls.

Imagine this scenario: a user takes his mobile smartphone into a movie theater. The lights inside are very dim. He wakes his phone to check the time. The screen display is excessively bright, causing him to look away. This is not just a screen display technology issue; it’s a UI design problem.

## Here are two solutions:

1. Have the automatic brightness sensor pick up the ambient light around the user and the phone (not the user’s face, which is what typically occurs). The sensor recognizes the low level of light and automatically dims the screen to an appropriate level to minimize eye strain and maximize viewability.

But not all users like automatic brightness on, partly as it can rapidly drain the device’s battery.

2. Provide immediate access to brightness controls. Rather than have them buried in a system setting, consider using the physical keys (e.g., volume) that can open a menu to control the display settings. These physical controls have eyes-off functionality and the user can interact with them without even looking at the device.

## Displays

Mobile device displays can range in size, resolution, and pixel density (ppi). As a mobile designer and developer, it’s helpful to become familiar with these differences so that you can make appropriate decisions throughout the design process. Depending on the requirements of the project, you may be designing for one particular device or for multiple devices with varying displays.

## Screen Sizes

Display sizes vary with the type of mobile device. They are measured diagonally from the display’s corners. Typically, smartphones have larger screen sizes than feature phones. A common misconception with mobile devices is that the screen size limits the user’s ability to see the screen.

However, people automatically adjust the visual angle between the device and their eyes. Entirely aside from phones being handheld, they get moved to the right distance to see things correctly.

Broadly speaking, video display ends up occupying the same field of view regardless of the device size. If we watch a movie on a 46-inch HDTV, we will distance ourselves enough so that we are able to see the entire TV in our visual field. That visual angle can be similar when we view a movie on a phone. This is why people actually do watch video on phones, and will continue to do so.

Other factors that affect how we automatically adjust our visual angle to see the screen include:

• Vision impairments a person might have

• The size of the display content, such as images, text, buttons, and indicators

• The amount of light the device is giving off (illuminance)

• The amount of light reflected from the light’s surface (luminance)

## Screen Resolutions

The screen resolution is determined by the total number of physical pixels on a screen. Note that the actual size of a pixel varies across devices as well as the type of technology being used in the display. So it can be very misleading when people say to design an object with a minimum touch target size of 44 pixels. Across devices with different screen resolutions, this touch target size will not be consistent. Therefore, when designing for appropriate touch target sizes, use unit measures that aren’t variable. For more information on proper use of touch target size, refer to the section “General Touch Interaction Guidelines” in Appendix D.

Here are common screen resolutions (pixels) across mobile devices, including feature phones, smartphones, and tablets:

Small: 128, 176, 208, 220 Medium: 240, 320 Large: 320, 360, 480+ Tablet: 600, 800, 768, 1,024

## Pixel Density

Pixel density (ppi) is based on the screen resolution. It equals the number of pixels within an area, such as a square inch (units do vary, so refer to numbers you find very carefully).

A screen with a lower pixel density has fewer available pixels spread across the screen width and height. A screen with a higher density has more pixels spread across the same area.

When designing for mobile displays, it’s important to be aware of the targeted device’s pixel density. Images and components that are designed in a particular height and width in screen pixels appear larger on the lower-density screen and smaller on the higherdensity screen. Objects that become too small will affect legibility, readability, and detail detection.

## Mobile Display Technology

Mobile devices use a range of display technology. Some devices may use multiple types of hardware within a single device. Each technology can serve a unique purpose in functionality—backlight, primary display, and flashing indicators.

As a designer and developer, it’s important to understand that each of these technologies has limitations in terms of the device’s battery life, the device’s lifespan, creation of glare, or restriction of orientation modes (see Figure 13-2). Therefore, we need to create UIs that can maximize the user experience around these limitations. Here are descriptions of some common types of display technology:

## LED

Light-emitting diodes are a superconductor light source. When the diode is switched on, the electrons move within the device and recombine with electron holes. This causes a release of photons.

– Used in annunciator illumination.

– Benefits include low power consumption, small size, and efficient and fast operation.

– Limitations include the ability to communicate only one piece of information at a time; also, they are single-channel, single-bit devices.

## OLED

Organic light-emitting diodes contain an organic semiconductor film that emits light in response to an electrical current.

– Used in the primary display.

– Benefits include the ability to function without a backlight, thin width, the ability to achieve a high contrast ratio, and when inactive does not produce light or use power.

– Limitations include the fact that it uses a lot of power to display an image (such as black text) with a white background, and may develop screen burns over time.

## AMOLED

Active-matrix OLED is a technology that stacks cathode, organic, and anode layers on top of a thin-film transistor. This allows for line-scanning control of pixels.

– Used in the primary display.

– Benefits include the ability to function without a backlight and the ability to be used for large-screen displays.

– Limitations include known problems with viewability in glare and direct sunlight.

## ePaper

ePaper generally relies on reflected light, not emitted light, by suspending particles in a liquid; a charge causes the dark particles to rise and be visible, or bicolor particles to rotate from light to dark (technologies vary) and display dark areas on a lighter surface, much like ink on paper.

– Used in the primary display.

– Benefits include low power consumption, reduced glare, and high contrast ratio.

– Limitations include slow refresh rates, and the fact that color technologies are just emerging.

OLED and AMOLED displays are lit-pixel displays (without a backlight). White text on black will, unlike a backlit display, use much less power than black text on white. This may be a key design consideration for those devices.

## Retroreflectivity

Retroreflective displays include a reflective layer behind the backlight layer. Ambient light coming into the display is dispersed across the surface and reflected back to provide passive, power-free illumination of the display content. This can be used to save power, to provide some view of the display when the device is in sleep mode, or to boost the performance of the display in bright light; instead of fighting the sun with high-power backlight, it is simply reflected back.

In some displays, this is the primary or only method to illuminate the display, and there is no backlight. In this case, the layer is located immediately behind the backplane.

Transflective layers are similar in concept, but use a transmissive/reflective layer that can be placed in front of the backlight. The key problem with these two technologies is that high-density color screens with touch overlays limit the amount of light passing through. Placing the reflective layer as far forward as possible increases the efficiency.

This works only for pixel masking displays, such as LCDs. Lit-pixel displays, such as OLED, cannot use it as they have no backlight—all pixels are opaque and must provide their own illumination. Although ePaper uses this concept, some technologies also cannot use it directly, and the reflectivity is integral to the “white” component of the display.

Display illumination on devices with reflective layers must take this into account to provide the most suitable illumination, and to extend battery life when not needed. In sleep states, the lock screen must continue to display useful information since it can be read at any time.

![](images/381854a60ba143103f49d6e681d30c1f6557f7afb44ecd901b02f608ebab9772.jpg)  
Figure 13-2. Low-power screens, or low-power modes, must make trade-offs in other display characteristics. ePaper technologies may evolve, but currently they have grayish blacks and very unwhite whites, as well as slow refresh times. The variable power of OLED allows the primary display to stay illuminated while sleeping, but only a few items can be illuminated, and contrast masks the fact that the white pixels are actually not at full intensity either.

## Input Overlays

If the display includes a touch or other input function, this is generally attached as a separate layer on top of the display screen. This is a problem in two ways. First, every layer over the display plane adds depth, which increases the parallax.

Second, nothing is truly transparent. Stacking several layers, with different indexes of refraction as well, can significantly reduce the brightness the user is able to perceive. Any touchscreen will be dimmer than the same hardware without a touchscreen.

Touch and other input layers are frequently sold as an integrated package by component manufacturers. Therefore, solutions such as Super AMOLED are available that allow the sensing layer to be thinner and more optically integrated than separately developed components.

## Sensors

Another important concept that we will discuss later in this chapter is location-based services used by operators and GPS satellites. These services identify tracking sensors in your mobile device to determine your location with varying degrees of precision and accuracy. Location services can provide an enriching user experience for a multitude of reasons.

They can work tangentially with your device’s OS and existing applications to trigger notifications or create appropriate device state changes without compulsory user interaction.

For example, say you are driving to the airport to catch a flight. Your mobile “Itinerary travel application” has you scheduled for a 3:00 p.m. departure at ORD.

As you get within a particular range of the airport, location services identify your current location and proximity to the airport. After you send that information to your Itinerary application, a notification pops up mentioning the latest departure time, and any occurring gate changes.

![](images/5c777fbd1ce0c20536ff365c870b74c75ffd60068c367f6b030c0ba8a8df7865.jpg)

![](images/d5af5c7cc5cf557f2273ba6182c34e6772332af70a25a80f30a6a732da11613c.jpg)

![](images/c8b193b9f90c79cafb1a53f845b9319dc409ba3a77cdcc534e472d9076932240.jpg)

![](images/0f88ceade99fbe22c0e857efe35df653d5dc5d3234a8c52787e8f0eea922c437.jpg)  
Figure 13-3. Automatic brightness will probably remain imperfect for a long time, so brightness controls should be a function of other settings or a home-page widget so that the user can get to them easily.

## Patterns for Screens, Lights, and Sensors

The patterns in this chapter describe how you can use screens, lights, and sensors to increase visual and device performance, provide additional notifications, and incorporate location-based services with native applications. We will discuss the following patterns in this chapter:

## LED

Notice of status should have a visual component that does not require use of the primary display.

## Display Brightness Controls

Displays are the most critical output on smartphones. A method to control the display settings must be easy to access, be easy to use, and allow for manual adjustments. See Figure 13-3.

## Orientation

Devices must allow for orientation changes to display content in the manner most readable and comfortable to the user.

## Location

Availability of a location-based service, and the actual location of the handset, must be easily and accurately communicated.

## LED

## Problem

You should ensure that status notices have a visual component that does not require use of the primary display.

Every device has at least an annunciator LED, used for power and other key status messaging. This light can be used by many applications, but not usually by web pages.

## Solution

![](images/c0fe78fa342ee08938973595e204ecc8d43b1d4e3accc1377ecd661edf4246b5.jpg)  
Figure 13-4. LEDs are most often encountered above the screen, usually to the left, and generally facing the direction of the screen, though some are placed so that they can be seen at other angles. On-screen indicators must communicate what the LED is intending to signal. Here, the red LED is reflected in the red battery meter level in the annunciator. Critical alerts will often demand more strident notifications, such as Pop-Up dialogs.

Annunciator illumination has been used for status and alert purposes since before the invention of electric light. Mobile devices took on the legacy from larger electronics, and machine-era devices with only minor changes, to denote power, connectivity, and alerts, among other things.

In all electronics for the past decade at least, the small, efficient, light-emitting diode is used for annunciator lighting. The term LED has come to have this general meaning, even in the now-rare event that another type of lighting technology is used.

Mobiles use LEDs more than other devices due largely to power consumption. The display is the largest consumer of power, so it is only illuminated when needed. The LED uses very little power, especially when blinking, so it can be used to notify the user with essentially no effect on battery life. LEDs may even be used to inform the user that the battery is entirely dead, when no other systems have sufficient power to operate.

The LED has become so heavily used that it is always designed in, but it may not be needed in the future. OLED-based displays, for example, use power only for the lit pixels and so can perform many of these display actions without the concern for power. LEDs may be used less often, or differently, in the future.

## Variations

Even in the machine era, multiple types of annunciator lights were used for different purposes. Each of these has its own useful variation in mobile use:

## Fixed

A single light is placed in an obvious, expected location, usually on the front face of the device, above and to the left of the screen. One light is provided for each screen on flip phones and the like, or is positioned so that it is visible when either screen is in use. See Figure 13-4.

## Relational

This is a simple light, like a fixed variation, but is provided adjacent to a physical item or area of the screen for the notification it refers to. A secondary light adjacent to the charge port indicates that it is operating; a light along the top edge of the screen indicates a Notification that the user can see by activating the screen and looking at this area. See Figure 13-5.

## Ambient

Illumination of a major component provides not just visibility, but also signaling. The keypad backlight may change from white to red to indicate low battery, or the charge port may be illuminated internally. These may be relational (such as the charge port example) or abstract. The keypad has no direct relation to the battery, but is visible and obvious.

These are not exclusive choices, and may be combined in one device.

![](images/4c0914cbc1f0867788ae24a139c0dd1a9048dce165881807b2643c77e4d3fe34.jpg)  
Figure 13-5. Relational LEDs send a signal not just by abstracting to colored lights, but by their placement. Here, the light adjacent to the USB port is indicating that the device is charging. No light, when the cable is plugged in, means no power is being provided. No color or blink codes must be interpreted, or another part of the device consulted.

The LED is always a display item, with no inherent interaction. However, it must be considered as a part of the overall interaction of the device, so it is coupled with other functions and behaviors.

Never use the LED as the only notification of a status change. Even relational items should always display the status on the device screen as well, generally as a Notification or in the Annunciator Row. This does not have to be visible immediately; if the device is asleep, the user can be expected to wake or unlock it first.

You should usually make audio Tones and Haptic Output accompany any LED notifications. The light serves to confirm that the mobile device made the sound, and to help the user locate the device if it is not visible or if the environment is dark.

Relational lighting uses the same principles as Focus & Cursors, where position is most crucial. For example, when an LED is provided for camera flash (Xenon flash has more technical limits), you may also use the same light at very low power to indicate to the subject that the photo has been taken. There is no need to signal in any other way, as the meme of “camera flash” means the photo has been taken, regardless of the position or intensity.

LEDs are single-channel, single-bit devices. They can only communicate one piece of simple information at a time. Generally, multiple types of messages can be sent over the same LED, but not easily at the same time. One of three tactics must be used:

## Alternate

Each displays in turn. This can lead to confusion and some signals may be missed

## Priority

Only the highest-priority message is displayed. When cleared, the next-highestpriority message is displayed.

Alert

A general notifier is presented for all cases, and the user is expected to view the Notifications panel to see what alerts are present. When all alerts are cleared, the LED will no longer illuminate.

Presentation details

![](images/e0370df32e41dbc2375744ba7787d80dd24f29203a16e347b09afd1b77388dbf.jpg)  
Figure 13-6. Lenses obscure the operation of the LED, allowing users to see the final, combined color, and to see even illumination from multiple angles

Signaling by lights falls into three categories:

• Position

• Color

• Speed

Position is partly discussed earlier in this pattern, but it also has to do with simply being attached to the device. Always consider the contextual nature of the device, and as much as possible signal only useful messages to the user. When multiple lights are available on the device, use the one most relevant to the information being communicated.

Color has cultural meaning, though for electronics, the US standards have largely taken hold where red means “bad” and green means “good.” These are not universal, but should generally be, or users may be confused. Sometimes branding will supersede these colors; if the brand of the device involves much red, and the default backlight is red, a red LED may lose the “bad” meaning; another color will be needed to express urgency, such as yellow.

Speed refers to blinking (at speeds visible to the user). These should be used very rarely and carefully on mobile devices. As these devices are frequently glanced at, often for only a fraction of a second, blink rates that cycle slower than one-quarter of a second are unlikely to be seen reliably. High-speed blinking can be used to express urgency. If movement is needed, throbbing and pulsing, where the light is never entirely extinguished, are better choices.

LEDs are inherently directional and must have a lens or it would be blinding at one angle, and almost invisible from others. An “LED,” as perceived by the user and communicated in the device user guide, is actually the lens, often fed by multiple LEDs to provide different colors, as described in Figure 13-6. Generally, no more than three are used, as at this point (if red, green, and blue are used), combinations of all of them can be used to make essentially any color.

Brightness should be changed based on ambient light level. The LED should never disappear in bright sun, or blind the user (or light up the whole room) in the dark. See the Display Brightness Controls pattern for details.

## Antipatterns

LEDs like are not Tones or Haptic Output devices. You should only use them for alerts and hardware status changes, and not generally as feedback for key entry or otherwise as a regular feedback mechanism.

Avoid excessively technical signaling using the LED. If the message would not be popped up on the screen, do not display it as a light.

Be aware of how LEDs work before employing them in a specialized manner. For example, LEDs do not have useful low-power modes, and actually blink at very high rates to simulate reduced output. This blink rate can be detected if the device is moving relative to the user, or can cause interference with other blinking when used for multicolor output.

Avoid blinking to indicate any important state change. Users may glance repeatedly at the device, but it always seems to be during the off cycle, and they will then never see the signal.

Never use blink ratios, even for errors or diagnostic purposes, where the LED is off more than twice as much as it is on, and avoid using differences in timing to encode signaling. Users are poor at perceiving rates or time without a reference.

Codes that are more complex than a simple blink should be avoided whenever possible, and always for general use. There is no mnemonic to remember that three short blinks and then one long one means the battery is full. Users will have to refer to documentation, or will simply disregard the message.

## Display Brightness Controls

## Problem

Automatic light sensors and user-controlled display settings are difficult to find, are difficult to use, and often cannot be made to yield an appropriate light level without significant user input. You must make display controls easy to access, and devise schemes to ensure that automatic controls are effective and useful.

Display controls are built into the device OS, but some platforms allow adding to the standard control sets.

## Solution

![](images/dea6803e9384905e6546cb5c4537569b620c2ee79fdcc98a4aa50f9bc4bad2bf.jpg)  
Figure 13-7. Brightness controls are routinely located inside a settings panel with various other related controls. The level must be displayed numerically as well as graphically, and the automatic brightness switch should be immediately adjacent to the level control.

Displays are the most critical output on modern smartphones, as well as a highly touted feature. Even minor degradations in performance can render the display uncomfortable to use or unreadable, or can reduce the perception of the quality of the display

This pattern focuses on higher-quality color displays, with light sensors suitable for use in setting automatic brightness. Other display types may use many of the components of the patterns, but may not be able to meet all of them. This also presumes backlit screens; lit-pixel screens such as OLED (and AMOLED) screens may have to modify the technical information to achieve the intended result.

Users must be able to get to display settings easily, preferably without much on-screen interaction, in case the screen is hard to read and they need to adjust it. The primary display setting is brightness (white point). Contrast (black point) and other controls may also be provided, but will not be well understood by the typical user; good median values must be selected by default for all other display adjustments.

The user must be able to make manual adjustments even if an automatic setting is provided, and should be able to provide user input to the automatic settings, as well as provide user calibrations to the light sensor.

As a general rule, keyboard and keypad backlight should follow the same illumination guidelines as the display, though manual control may provide for separate settings. Key backlight color changes or blinking as a signaling method is discussed under the LED pattern.

## Variations

Manual is the most common mode, available on almost all devices with a screen. A simple one-axis user control is provided on a settings panel as in Figure 13-7.

Modern mobile devices with high-quality screens mostly come set to automatic mode by default. While in automatic, a light sensor detects the user’s face and surmises the ambient light level to determine optimal output. The user may switch to manual mode, which disables the automatic settings.

An automatic mode with manual input should also be provided, to allow user modifications to any failure of the automatic system to detect the optimal output level.

A learning mode would be a useful fourth variation, using the principles of learning user predictive text, voice, or gestural input. The device will monitor user overrides to automatic input and/or accept multiple user calibrations in order to adjust how automatic behaviors work, with the intent of an entirely satisfactory automatic behavior, eventually.

Interaction details  
![](images/db4b4a4dca411d8eb85b050a42f6991ef832014b2d4d7b7caf81c34b7c80b088.jpg)  
Figure 13-8. Easy access to brightness should be provided when it can be. The example Pop-Up appears when the volume control is used. Using the left and right directional controls changes focus to the brightness. Automatic brightness will be disabled when manual changes are made. Changes should always be immediately implemented, without explicit saving.

Whenever possible, make access to the brightness settings immediately accessible from any screen. A well-used option is to have an existing function (such as volume or power) make a general settings panel appear, with brightness, volume, synch, and power-off/ restart functions (see Figure 13-8). Once it appears, volume keys may change the volume, and (for example) the Left and Right Directional Entry keys may change brightness. Other solutions may be more suitable to your specific interface or operating system.

Eyes-off brightness control is necessary in case the brightness is set so low that the screen cannot be seen; the user may remember the interface, and be able to activate the panel and increase brightness, without viewing the screen.

The primary brightness adjustment control is a tape, as described in Mechanical Style Controls, or similar control with implied analog input. In fact, this will control input in steps based on the software controlling the display backlight. Allow direct numeric input of these values.

Make sure the brightness control allows the user to set true minimum and maximum output. Mobile devices can be used in complete darkness, where users’ eyes may be fully adjusted or bright screens may distract. Do not select an arbitrary minimum brightness above the adjustment range value of 1.

A simple setting on the brightness control panel must allow the user to enable and disable the automatic brightness control. This may be set from other places as well.

Provide a function to add user adjustment to auto-brightness. This will not disable automatic control; it will just add the user control as a new temporary zeroing point. Ideally, the device will remember this user setting and factor it in over time in a learning mode.

Sensors will continue to be most useful when placed on the front of the device (among other things, it is probably best for checking light where the user is). Calibrate sensors from the factory not to neutral gray, but to people’s faces at typical distances. Provide a function to allow users to recalibrate the sensor to their face and typical viewing angle and distance. This may also be implemented as an explicit learning mode, with the user performing this for several typical environments in which she uses the device.

## Presentation details

Whenever room is available in the Annunciator Row, in a Notifications area, or in similar areas where current settings are displayed, the current brightness settings should be displayed. This should indicate automatic or manual, and the level in the conventional scale of measure used on the adjustment panel itself.

Within the brightness panel, it must be very clear when automatic brightness is enabled. When enabled, display the actual brightness selected by the automatic controls in a manner similar to the manual setting.

When the user is adjusting brightness, make sure the screen reflects the adjustments in real time, so the user can tell how bright he wants it. This also may mean the brightness setting dialog may need to either have sufficient information or not gray out the parent window, so there is a chance for the user to see what typical screens look like.

It is highly suggested that adjustments be simulated when the brightness panel is displayed. This is so that the adjustment panel itself can be seen in all conditions. Set the screen backlight to 100% brightness, with the adjustment panel as a modal Pop-Up with the controls and instructions simulated (via the pixel color) to 50% brightness, with very high contrast, such as white letters and outlines on a black background. The parent window behind the Pop-Up will simulate (with color changes to the pixels themselves or opacity to a black overlay...) the adjusted-to value.

Within the display adjustment panel, present the brightness numerically as well as via any graphical control indicators. Some users will understand numerical values better, and most users will be able to recall numerical values that work in certain environments, so they may be able to adjust to those by memory if automatic systems do not work.

All hardware keys must be visible in darkness or marginal lighting conditions. Certain devices or keys may be able to use phosphorescent (“glow in the dark”) keys, but active backlight is generally required. All functions of the keys must be visible in all lighting conditions.

## Antipatterns

Avoid brightness-changing functions that are not discoverable or learnable.

Do not overly simplify the brightness control software (either automatic or manual) by limiting it to a small number of large steps. With even 16 steps, users can detect the difference between individual steps. They may not find a suitable brightness, or may find the display jumps settings (exhibits “seeking” behavior) when in automatic mode. Using the full complement of steps (e.g., 100 or 256) will provide sufficient levels and smoothness that even rapid adjustments will be perceived as smooth changes in brightness.

Do not illuminate only some portions or functions of a key. The key labels must be clearly visible in both reflected light as well as emitted light, when only visible under backlighting. For example, “function” modifiers may be yellow and correspond to a yellow-painted key on an otherwise white label set. When illuminated, and key labels are generally white, the function labels for each key must remain yellow, and the function key should be entirely yellow, to match the reflected color scheme and style.

On light-colored keys, keyboard backlight can conspire with ambient lighting to make the key labels entirely invisible to the user. White backlight, at low light levels, can easily have the same luminance as a white or silver key. Carefully test and adjust backlight settings or select contrasting keys or backlight colors.

## Orientation

## Problem

You must provide a way for any device orientation changes to display content in the manner most readable and comfortable to the user.

Many devices have accelerometers, dedicated rotation switches, or both. This hardware and any other OS-level orientation changes should be respected by all applications and other content. When not available at the OS level, orientation can often be changed anyway, if it would be more helpful to the user.

![](images/186e5ad54e931bc15a33a3f2033bd42a0a81b7282b853034c8a7e63bf16d72fb.jpg)  
Figure 13-9. An illustration of how device orientation should not take effect immediately, but requires significant commitment. Note how additional information is visible in some cases (wider title bar, more page width available allowing for larger text and images to be used) but less information is visible in others (two-thirds of the page does not fit in the viewport). This trade-off is why users must be allowed to control their viewing orientation.

Mobile devices are small and portable, and unlike desktop computers they can be manipulated and viewed in any manner. Naturally, users will rapidly face the screen in the correct direction, but after this they should be allowed to choose their preferred viewing Orientation. Content must be presented in a useful format in whichever orientation is chosen, modified to fit the screen, but without changing context or modifying existing user entry.

This change must be performed either automatically or with an obvious or deeply integrated physical mode switch.

A related function is for devices with screens on both sides, or other form factors; flipping, sliding, or otherwise switching screens can follow this pattern, but is not discussed explicitly due to the small number of such devices.

This pattern exclusively addresses screen orientation or activation, and does not discuss use of the orientation sensors as a gestural control. For generalized discussion of position and orientation, see the Kinesthetic Gestures pattern. For some methods of employing subtler orientation changes, see the pattern on Simulated 3D Effects.

## Variations

Variations in Orientation generally follow the device form factor and consider the effectiveness of the overall device, including input methods.

Fixed form factors, and especially “all touch” devices, generally should use automatic sensing to switch from portrait (vertical) to landscape (horizontal) mode (see Figure 13-9). Sensors have generally been accelerometers, to sense the device orientation relative to the ground. The device camera may also be used to sense the user’s head position and adjust relative to this plane. Level sensors can sometimes give poor results (when content is being shared or when the user is in an unusual position, such as lying down); the machine vision solution attempts to overcome this.

Devices with any sort of variable form factor generally also change the use of its display. This physical mode switch serves as a switch to the screen as well. This can be considered to include the activation of an external screen when a clamshell or flip phone is closed. Typical cases for rotation are the now-common messaging-oriented phones, with Directional Entry keys (or sometimes even a numeric pad) when closed, but a fold- or slide-out keyboard (see Figure 13-10). The switch in screen orientation corresponds to the orientation of the hardware entry method.

Interaction details  
![](images/d22b5982c2bcdb098dee1cc76876aa45d2f3fd9962741c280bd1851925de6205.jpg)

![](images/e0aeda681d36c966b9577e0e9fab96e1b94db4bf80dbf9d5ea5c74028b8e6388.jpg)  
Figure 13-10. Changing orientation does not just mean zooming content or reflowing text. Here, modules for a portal landing page switch from being simply stacked in the portrait view to being arranged in two columns in the landscape orientation. This device is typical of a large class that switches orientation on the physical mode change of opening the keyboard.

For automatic sensing devices, much leeway must be granted before a rotation is committed to. Users will not hold devices perfectly upright, and may use them in unusual orientations.

The angle of commitment must be a large value, such as 60 degrees from the vertical. Rotating to the opposite orientation (180 degrees, such as from one landscape orientation to the other) should likewise not take place as soon as the device passes level, but only after exceeding about 20 degrees of the opposite angle.

Once a switch has occurred, use a new baseline to measure from. The angle (e.g., 60 degrees) is measured from the current ideal vertical. The angle at which the orientation switches back must not be the same one for both, or it will flip back and forth repeatedly. This is a key reason 45 degrees cannot be used as the switching angle.

You can provide additional leeway based on context. Consider a device placed on a table. When picked up, it may be accidentally over-rotated, away from the user. The device should probably not immediately rotate 180 degrees on the expectation that someone else has picked it up from the opposite side of the table.

Here, the sensors can determine that the device has been set down and has not been used for some time, and can reset the baseline to be “from the tabletop.” Then something like the 60-degree guideline can be used. Only when rotated backward that far will the screen rotate 180 degrees to be usable at the opposite viewing angle.

The user’s selections or inputs on the screen must in no way be changed during an Orientation switch. Items in focus must remain so through the change, with selections to the character or pixel when applicable.

No uncommanded actions must take place. Do not clear entry, submit forms, scroll, or perform any actions that would not have been performed had the orientation change not taken place.

## Presentation details

Whenever possible, you should animate the rotation. Actually show the starting orientation rapidly rotating to the new position. The entire change does not have to animate, reflowing to the new shape; but the initial animation helps to explain the change and confirm to the user that the rotation action is occurring, and not some other, possibly uncommanded, behavior.

Avoid blanking the screen, as this can be perceived as an error or bug, and the discontinuity requires the user to reorient herself to the screen.

Make content reflow to fit to the screen. Never allow items to fall off the screen, or for gaps or margins to appear to the side as a way to cheat the rotation.

This will necessitate reflowing of text (changing where line breaks occur), or even switching to an entirely different display template, such as placing modules side by side, instead of stacked in a list. However, every effort must be made to have all content from the old orientation visible in the new one.

When this is not possible, the focus area from the initial orientation must always remain in the viewport in the new orientation. For example, if a list view is shown in portrait, and the bottom item on the screen is in focus, when rotated it may be off the screen. Instead, the page must scroll so that the item remains in the viewport in the horizontal screen, even though it means other items have been scrolled up off the screen.

At no point should the in-focus item be off the viewport, so use caution when designing an animation to depict this. For example, do not rotate and then scroll down to the infocus item. The time when the in-focus item is out of view may be disorienting.

Antipatterns  
![](images/6e9b95e73bdb7a6d496618a3fb09c02cbf1b14aab1f718f01b5b49a0810f1ae2.jpg)  
Figure 13-11. Never change orientation without redrawing the content to use the space more effectively. In this example, extra space is unused on the screen, but other cases exist where content flows off the screen. Don’t consider user controls that allow zooming as an excuse for this behavior—always deliver the best possible experience automatically, based on the current context.

Always redraw items on the screen to take advantage of the new orientation. Never leave blank space, as in Figure 13-11, allow content to fall off the screen, or otherwise take shortcuts that use the new orientation in a less-than-optimal manner.

A manual override is often provided for devices using automatic sensing. This may take the form of a manual selector or a lock (to prevent rotation from the current position). These are generally arbitrary buttons or on-screen actions, so they must be learned. In general, they should be considered a half-measure, and everything should be done to make automatic sensors and their algorithms as good as possible.

Use caution when including both physical mode switches and automatic sensing in a single device. Consider a perfectly usable “all touch” device, with automatic sensing for orientation changes. When the hidden hardware keyboard is slid out, it makes no sense to rotate, as the keyboard would face the wrong way, but the user may have become accustomed to having the ability to rotate orientation.

## Location

## Problem

You must clearly communicate the availability of location services, and use these location services to make services more personalized and relevant.

Aside from the many dedicated navigation devices, GPS is ubiquitous in many other devices, and other location technologies can extend this capability to almost any connected device. Access is sometimes restricted for websites and some application types, but there are workarounds.

## Solution

![](images/8e76e7c6a873918beebb2288aca805b98a2da21cebaa3bc49048a08c072cc1eb.jpg)  
Figure 13-12. Location can present more that just a pinpoint on a map. Direction can be indicated organically, with the pointer and by rotating the map to match the direction of travel, as well as with compasses. Speed and other attributes (e.g., height, relative position) can also be displayed.

Mobile devices have numerous methods of retrieving location information. These include:

• Cell

• Sector

• Triangulation

• GPS telemetry

• WAAS

## • AGPS

## • WLANs and PANs

Note that only one method is the use of GPS. You should try to understand at least the basics of each technology, and their capabilities and limitations. Each is detailed in Appendix A, “Mobile Radiotelephony.”

One more key method of retrieving information is, of course, to ask. Users often know where they are. If they cannot get any location, or there’s a reason they might want to override it (even one as simple as that the data is bad), let your users enter a location. If they do this, allow the device to accept lots of methods. Only accepting zip codes or postal codes is not useful for travelers, who do not generally know such details.

It is also important that you understand the difference between precision and accuracy. In brief, precision is the number of decimal places you measure something to; accuracy is how correct it is. The less accurate you think your measurement is, the less precisely you should report it.

Privacy and security concerns are beyond the scope of this book, but they must be considered when designing location-based services. In many countries, there are legislative or regulatory restrictions on enabling and using location, so notification of background tracking is a legal requirement, not just a best practice.

Location is not the same as Orientation or other types of position information. When these must be communicated—as for augmented reality—they are generally deeply integral to the visualization and interactive design of the application. No distinct patterns yet exist for these behaviors, but best practices from aviation may serve to guide designs.

## Variations

Location service is often used as a background service, as a way to enable smarter ambient computing. When directly referred to, it may only be momentarily switched to while other tasks occupy the remaining time. Therefore, both explicit and background indicator cases may be present, not just in the same system, but also at the same time:

## Explicit

Location services are currently mostly used for explicit location applications, such as mapping, directions, local information, and augmented reality. These explicit representations of location are discussed in detail shortly.

## Background

Location services can also be used as a trigger to initiate notifications or to change the behavior of the device. Geofencing, location-driven advertising, and location-based profile changes (e.g., silent when in a meeting room) have all been tested, but are not widely adopted.

Settings, including installation of applications using location services, must also take into account these principles, especially those of privacy and awareness.

Though this pattern discusses such behaviors and features on a mobile device, they may also be used for remote devices in much the same manner. “Child trackers” and similar functions may be used from another mobile device or from desktop computers to track a remote mobile device. In this case, both the viewing terminal and the mobile device must consider the display and behavior attributes of this pattern.

Interaction details

![](images/5904b61b8e95f3f88f2349d225198fc4fe2346849b69da81830d129855bc5646.jpg)  
Figure 13-13. When information is not available, such as speed and direction of travel, it should generally not be shown at all, instead of simply being zeroed out. Precision must always be shown with a true-to-scale error scale circle, and numerical precision whenever possible.

You should present indicators of state only in the Annunciator Row so that the user cannot interact with it. Make a system setting available to control the use of GPS, WiFi, and other controls, as well as to set privacy controls for sharing and how much automatic (versus manual) control is allowed over these systems.

Provide an easy method for the user to gain access to this control, without drilling into multiple submenus. Whenever possible, add this control shortcut to any application that uses location services. Another good method, when technically feasible, is to add the control as an interactive Icon on the Idle screen. In this way, the user can simply pop back to the home screen and change the setting before using any application.

Whenever possible, applications or services that work best with location should automatically enable the required hardware. OS-level restrictions or user settings may interfere with this behavior, and require user intervention each time. If so, an interstitial Pop-Up, despite the intrusive nature, will end up being the best way to request this access.

When the Pop-Up itself is restricted from offering a function to enable the GPS (or other hardware), use it sparingly, as a reminder to the user instead, and provide a link to the appropriate settings panel. When settings are changed, always return the user to the originally requested application.

Only use the precision required for the task at hand. Weather, for example, rarely requires more than city-level precision. The GPS is not required for basic conditions and forecast information, so if other location services are providing sufficient detail, do not enable the always power-hungry GPS.

On the other hand, always present the most relevant details for each view. If the user chooses to view a local radar map, the user should not be required to know her location but should be presented it systematically. This example weather application may have to turn on and off various location services as the application is used, and should not enable all services when it is opened, or get by with only the minimal set and present less-thanoptimal information.

Presentation details

![](images/b58710a3049ae7c27f2f960d8bacf10035ee9424847d2ee7a40a91faf53b5c05.jpg)

Figure 13-14. Icons to denote location services are not just optional variations, but can imply different meanings. The crosshair is a standard used to denote location-enabling as well as the fact that the mobile handset sends its location to the operator, for e911 and other purposes. The satellite dish and satellite denote GPS specifically, and may be used to denote other conditions. For example, the dish may imply the device requests service, and the satellite only appears when a link is established.

When location service is enabled, be sure to display an icon (see Figure 13-14) in the Annunciator Row. The location icon (crosshair) has come to mean GPS is enabled, so there may be challenges in communicating other types of location services. GPS specifically can use other types of icons, such as a satellite dish. GPS requires a short time to find position, can lose position due to interference, clutter, or other conditions, and must display the current status. Generally, animating the satellite dish (implying “scanning for service”) works well.

Avoid duplicating indicators. If the indicator is in the Annunciator Row, there is generally no need to also include such indicators within an application. This is another good reason to preserve the Annunciator Row bar, instead of loading applications full-screen.

For explicit graphical display of location, such as on a map, use a cursor to denote the current position. Note that this is actually the centroid of the “circular error of probability” (CEP). A probability threshold is programmatically established; based on the technology used to determine location, the device is almost certainly located within this circle. (Note that it is impossible to absolutely determine location [hence the “probability” phrasing], but this is not terribly important for general discussions.)

Display this CEP circle with the cursor at the center, as a visual method of communicating the precision of the location technology (see Figure 13-13). Unless additional precision is needed but is currently unavailable, the default view should hide the CEP circle from the user. For a weather map, for example, the default zoom level should be large enough that a 100 m CEP is smaller than the cursor, so it disappears under it. Good selection of map zoom levels can help to communicate the degree of precision available.

![](images/ef9902b822eeeba0f97c1540b64392dac583797bd6d16ed5f7f03172c28490ac.jpg)  
Figure 13-15. Coordinates and other location information, when relevant and useful, should be presented on-screen in an easy-to-read format. Multiple formats may be presented at once, as shown here. Many digits have been removed in this example, in the interest of using only the degree of precision available.

When the display is zoomed such that the CEP circle is at least 10 times the size of the cursor, or the edge is partly or entirely outside the viewport, print an explicit display of precision adjacent to the cursor.

An even greater pitfall in the display of precision information is with printed location, especially in coordinate systems (see Figure 13-15). Whenever possible, use standard, well-understood nomenclature. Avoid printing the location when it is not useful; lat/long is difficult to interpret and very few general users will understand it.

Account for precision in the display of coordinates and other printed locations. For this example, the MGRS coordinate system will be employed as it is based on simple measurements (meters from a regional baseline). This is unlikely to be employed in general consumer applications, but is convenient as an example. A complete location to 1 meter precision is listed as:

## 15S UD 12345 67890

(The 10 numbers at the end show the position in meters vertically from the equator, and horizontally from a point too complex to explain here.)

However, most location technologies, in most instances, cannot give such precision. To correct for this, remove digits until only the correct level of precision is shown. For example, if using cell sector, with precision in the 100 m range, only display:

## 15S UD 123 678

The last digit will always be of less precision than the others, and even when displayed digitally can be used like that on a dial or scale. Simply restrict the display to only the 5 or 0 digit.

Precision should be explicitly displayed when coordinates are printed. Use the existing settings for units of measure, but scale them appropriately. In the following examples, the user has set his navigation tool to use miles:

• “Accuracy 19 ft”—Correct. Appropriate scale (versus yards or miles) for the size, and in the same system.

• “Accuracy 6 m”—Incorrect. In the wrong system of measure.

• “Accuracy 0.004 mi”—Incorrect. Too large a measure with many decimal places and not easily understood.

Note that the term precision is not well understood, so it is often replaced with accuracy in general communications, as in the preceding examples, although it is not strictly true.

Addresses, likewise, should only be displayed when that level of precision is available. Otherwise, use existing best practices for general location:

• 5600 Russell Ave., Mission, Kansas 66202

– 56th St. & Russell Ave., Mission, Kansas 66202—Street or Intersection

– West Crossland, Mission, Kansas 66202—Neighborhood

– Mission, Kansas 66202—City

– 10 miles west of downtown Kansas City, MO—Relative Location

– Near Kansas City, MO—Area

Only display the larger-scale information such as state and country when needed. When moving between two areas only a few miles apart, the default location display should probably just be the street address portion. The same filtering logic should be used for coordinate systems, when applicable. Although Lat/Long is a global system, UTM and MGRS are divided into regions; the “15S UD” portion in the preceding example can be made much less prominent, as most precision navigation is not also global navigation, so it will not be used as much as the remainder of the displayed coordinates.

Only display the device’s direction of travel when available (see Figure 13-12), and just like the location, only display it to the degree known. Generally, the cursor can simply become a pointer. For free-standing displays, when users will get value from it display the current bearing in degrees and by named directions (northeast), but degrade to cardinal directions as the system’s understanding becomes poorer.

Cardinal directions (e.g., “north”) can imply precision if simply printed on the screen; use graphical displays (either dials or circular tapes) to communicate the degree of precision available, make small changes in bearing angle visible to the user, and make the display more glanceable.

When direction of travel cannot be determined (there is no compass and the device is not moving), display no direction of travel indicator, or an icon indicating it is unknown. The cursor may change to a circle, or otherwise become blunted to reduce or remove the implication that direction is known. Do not display the last direction, as this is likely to be spurious data arising from loss of signal, or coming to a stop.

When direction of travel is available, orient the map so that direction of travel is forward, or up. If there is a specific reason not to do this by default, provide a function so that the user can switch to this mode.

## Antipatterns

Never equate “location” with “GPS,” especially to the degree that a location-aware service or application may only launch when the GPS is enabled.

Never display or imply precision that is not available. Avoid the use of crosshairs and other implied attributes, even if a CEP circle is displayed as well.

## Summary

## Wrap-Up

People interact with their devices in unique ways that are most comfortable and natural to them. Some prefer using the keyboard, while others who are less familiar with text input may use the pen. Those who enjoy using natural gestures will use devices with touchscreens and accelerometers.

The environment and context also influence how users interact with these devices. Some people prefer to work outside no matter the weather condition. They might be bundled up in a coat and wearing gloves, and they still expect to input data. Those who use their device indoors while studying may require the use of lights and haptics as notifiers so that they aren’t interrupted. People who are constantly traveling may require an integration of location-based services with their current application use.

With all of these variables affecting how people interact within the mobile landscape, it’s important to carefully consider the mobile design principles when designing mobile interfaces:

• Respect user data.

• Mobiles are personal.

• Lives take precedence.

• Mobiles must work in all contexts.

• Use your sensors and your smarts.

• User tasks usually take precedence.

• Ensure consistency.

• Respect information.

## Pattern Reference Charts

The pattern reference charts in the following subsections list all the patterns found within each chapter described in this part of the book. Each pattern has a general description of how it can apply to a design problem while offering a broad solution.

Cross-referencing patterns are common throughout this book. Design patterns often have variations in which other patterns can be used due to the common principles and guidelines they share. These cross-referenced patterns are listed in the following charts.

## Chapter 9, “Text and Character Input”

Despite the existence of more efficient ways to input text, people still may choose to use what they are most comfortable with. Some people are comfortable with handwriting, others with keyboard input. Some may prefer to use a pencil, pen, or stylus. Always default to the most common method they can be expected to be familiar with, and provide options. Text and numeric entry methods must be simple, easy, visible, and so predictable in behavior that they may be performed by any likely user with little or no instruction.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td>Other patterns to reference</td></tr><tr><td>Keyboards &amp; Keypads</td><td>Text and numeric entry must be simple, easy, and so predictable in behavior it may be performed by any likely user with little or no instruction.</td><td>Three options exit: hardware/virtual, keyboard/keypad, and direct/multitap. Consider the constraints held by the device, as well as cultural norms, and adhere to basic keyboard principles.</td><td>Input Method Indicator Dialer Autocomplete &amp; Prediction Directional Entry Button</td></tr><tr><td>Pen Input</td><td>A method must be provided to input text that is simple, is natural, requires little training, and can be used in any environment.</td><td>Pen interfaces can be an alternative to keypads or touchscreens when touch is unavailable due to environmental conditions (gloves, rain), when the device is used while on the move, or just to provide additional precision and obscure less of the screen.</td><td>Exit Guard Keyboards &amp; Keypads Autocomplete &amp; Prediction Wait Indicator Cancel Protection</td></tr><tr><td>Mode Switches</td><td>Provide access to additional and alternative controls without taking up more hardware or screen space through the use of mode switching.</td><td>Mode switches provide extra capabili- ties of a keyboard or keypad by includ- ing access to variations of characters and symbols.</td><td>Tabs Keyboards &amp; Keypads Pen Input Dialer Input Method Indicator</td></tr><tr><td rowspan="3">Input Method Indicator</td><td rowspan="3">The user must be made aware of the current mode of the selected input method, and any limits on selecting modes for a particular entry field.</td><td>An indicator should be placed on the screen to explicitly indicate the current</td><td>Pen Input Mode Switches</td></tr><tr><td>input mode or method.</td><td>Annunciator Row</td></tr><tr><td></td><td>Notifications</td></tr><tr><td rowspan="3">Autocomplete &amp; Prediction</td><td rowspan="3">Whenever possible, use as- sistive technology to reduce</td><td rowspan="3">Autocomplete and predictive entry have proven especially valuable due</td><td>Accesskeys</td></tr><tr><td>Dialer</td></tr><tr><td>Infinite List Pen Input</td></tr><tr><td>text entry effort, and to reduce errors.</td><td></td><td>to the relative difficulty and reduced speed of text entry, and especially for</td><td>Tooltip</td></tr><tr><td colspan="2"></td><td>complex, technical character entry such as URLs.</td><td>Cancel Protection</td></tr></table>

## Chapter 10, “General Interactive Controls”

In addition to the keyboard and keypad, users expect to interact with the UI using many other methods of control. These controls may be hardware keys located on the device, touchscreens that allow for finger input, or sensors that allow for kinesthetic and remote gestural interaction. The type of control used depends on the context, the user’s preference and comfort level, and the technology available on the device. The control’s behavior must be well understood, provide immediate feedback, and use constraints to limit error.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td>Other patterns to reference</td></tr><tr><td>Directional Entry</td><td>To select and otherwise inter- act with items on the screen, a regular, predictable method of</td><td rowspan="4">Two separate solutions work hand in hand to meet these needs: hardware input devices (buttons</td><td>Focus &amp; Cursors</td></tr><tr><td></td><td>input must be made available.</td><td>Scroll</td></tr><tr><td rowspan="2"></td><td rowspan="2">and controls) and the behaviors (axis and planar) that govern</td><td>Wait Indicator Mode Switches</td></tr><tr><td></td></tr><tr><td>Press-and-Hold</td><td>In certain contexts, an alterna- tive cursor-initiated function should be made available. A simple, universal method of applying this mode switch should be provided.</td><td>A press-and-hold behavior may present a contextual menu of options, or other contextually relevant optional selections.</td><td>Keyboards &amp; Keypads Mode Switches Revealable Menu</td></tr><tr><td rowspan="3">Focus &amp; Cursors</td><td rowspan="3">The position of input behaviors must be clearly communicated to the user. Within the screen, inputs may often occur at any</td><td rowspan="3">Areas and items for which im- mediate interaction is possible are considered “in focus." When an exact point is in use within this area, this is indicated by a cursor.</td><td>Fixed Menu</td></tr><tr><td>Annotation</td></tr><tr><td>Directional Entry</td></tr><tr><td rowspan="4"></td><td rowspan="4">number of locations, and espe- cially for text entry, the current insertion point must be clearly communicated at all times.</td><td rowspan="4"></td><td>LED</td></tr><tr><td>Input Method Indicator</td></tr><tr><td>Mode Switches</td></tr><tr><td>Wait Indicator</td></tr><tr><td>Other Hardware Keys</td><td>Functions on the device, and in the interface, are controlled by a series of keys arrayed around the periphery of the device. Users must be able to understand, learn, and control their behavior.</td><td>All mobile devices have numerous additional keys. Regardless of their function, all must comply with some basic behavioral standards in order to be useful, usable, and valuable to the user.</td><td>Keyboards &amp; Keypads Directional Entry Annunciator Row Pop-Up Mode Switches</td></tr><tr><td>Accesskeys</td><td>Provide single-click access to an arbitrary set of key func- tions for each page or view.</td><td>Accesskeys provide one-click access to functions and features of the handset, application, or site for any device with a hardware</td><td>Exit Guard Mode Switches Dialer</td></tr><tr><td>Dialer</td><td>Most mobile devices are still centered on voice networks connected to the PSTN. Access to a phone dialer must be provided.</td><td>keyboard or keypad. Common numeric entry methods of operation that users are ac- customed to must be followed to provide easy and accurate access to the voice network.</td><td>Home &amp; Idle Screens Dialer Tooltip Autocomplete &amp; Prediction Keyboards &amp; Keypads</td></tr><tr><td>On-screen Gestures</td><td>Instead of physical buttons and other input devices mapped to interactions, allow the user to directly interact with on-screen objects and controls.</td><td>Items in the screen are assumed to be physical objects that can be “directly”manipulated in realistic (if sometimes practically impos- sible) ways.</td><td>Directional Entry Vertical List Film Strip Infinite Area Pop-Up</td></tr><tr><td>Kinesthetic Gestures</td><td>Mobile devices should react to user behaviors, movements, and the relationship of the device to the user in a natural and understandable manner.</td><td>The mobile device uses sensors to detect and react to proximity, action, and orientation.</td><td>Orientation Location Jump Remote Gestures Tones Voice Notifications Haptic Output</td></tr><tr><td>Remote Gestures</td><td>A handheld remote device— or the user alone—is the best, only, or most immediate method to communicate with another, nearby device with a display.</td><td>Ready availability of accelerom- eters, machine vision cameras, and other sensors now allows the use of gesture to control or provide ambient input.</td><td>LED Tooltip Annotation Kinesthetic Gestures Simulated 3D Effects Directional Entry On-screen Gestures Focus &amp; Cursors Tooltip</td></tr></table>

## Chapter 11, “Input and Selection”

In today’s mobile landscape, filling out fields and forms is a trite task in any mobile context. But such a common task continues to have a common problem: user input errors. Whether it’s from incorrect character input or accidental clearing, users can become quickly aggravated with input and selection. So it is essential to design these functions with the user in mind. This chapter discussed the input and selection methods that allow users to quickly and easily enter and remove text and other character-based information without restriction.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td>Other patterns to reference</td></tr><tr><td rowspan="3">Input Areas</td><td rowspan="3">A method must be provided for users to enter text and other character-based infor- mation without restriction.</td><td rowspan="3">Text and textarea input fields are heavily used to accept user- generated text input in all types of computing.</td><td>Dialer</td></tr><tr><td>Directional Entry Clear Entry</td></tr><tr><td>Focus &amp; Cursors</td></tr><tr><td rowspan="3">Form Selections</td><td rowspan="3">A method must be provided for users to easily make single or multiple selections from preloaded lists of options.</td><td rowspan="3">Mobile devices, even more than other computing devices, can use forms to good effect for selection from already-provided information.</td><td>Autocomplete &amp; Prediction Cancel Protection</td></tr><tr><td>Button</td></tr><tr><td>Select List Vertical List</td></tr><tr><td>Mechanical Style Controls</td><td>A simple, space-efficient method must be provided for</td><td>user input, improve accuracy, and greatly reduce frustration. Mechanical Style Controls are really</td><td>Focus &amp; Cursors</td></tr><tr><td rowspan="3">Clear Entry</td><td rowspan="3">users to easily make changes to a setting level or value.</td><td rowspan="3">just compact, graphically oriented variants of the single-select Form Selections.</td><td>Form Selections Vertical List</td></tr><tr><td>Zoom &amp; Scale</td></tr><tr><td>Search Within</td></tr><tr><td></td><td>Users must be able to remove contents from fields, or some- times whole forms, without undue effort and with a low risk of accidental activation.</td><td>Clear control can be used to clear or reset an entire text input field.</td><td>Input Areas Cancel Protection</td></tr></table>

## Chapter 12, “Audio and Vibration”

Using audio and vibration can be an effective way to communicate alerts and notifications. Tones, haptics, and voice notifications are used to get the user’s attention, communicate information more rapidly and clearly, or read the content of a notification when the device is not in the hand, cannot be viewed, or is chosen to not to be seen.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td>Other patterns to reference</td></tr><tr><td>Tones</td><td>Nonverbal auditory tones must be used to provide feedback or alert users to conditions or events, but must not become confusing,</td><td>Tones should be used for alerting, and as a channel to emphasize successful input, such as on-screen and hardware button presses, scrolls, and other interactions.</td><td>Haptic Output Notifications Voice Readback Voice Input</td></tr><tr><td>Voice Input</td><td>frequent that critical alerts are disregarded. A method must be provided to control some or all of the functions of the mobile device, or provide text input, without handling the device.</td><td>Voice Input allows voice to be used as a control and input mechanism to relieve users of eyes-on, hands-on control methods.</td><td>LED Accesskeys Voice Readback Directional Entry Input Method Indicator Tones</td></tr><tr><td>Voice Readback</td><td>Certain classes of users, or any user in certain contexts, must be able to consume content without reading the screen.</td><td>Voice Readback allows the device to read text displayed on the screen, so it can be accessed and understood by users who cannot use the screen.</td><td>Mode Switches Voice Notifications Directional Entry Annotation Pop-Up</td></tr><tr><td>Voice Notifications</td><td>Certain classes of users, or any user in certain contexts must be informed of condi- tions, alarms, alerts, and other contextually relevant or</td><td>Voice Notifications read the con- tent of a notification so that they can be used when the device is not in the hand, or cannot be viewed.</td><td>Voice Input Notifications LED Annotation</td></tr><tr><td>Haptic Output</td><td>time-bound content without reading the device screen. Vibrating alerts and tactile feedback should be provided to help ensure perception and emphasize the nature of UI mechanisms.</td><td>Most mobiles have some sort of vibration, or an external speaker, that can be used for at least basic haptic output.</td><td>Pen Input Tones Notifications LED Wait Indicator Voice Notifications</td></tr></table>

## Chapter 13, “Screens, Lights, and Sensors”

Mobile devices today are equipped with a range of technologies meant to improve our interactive experiences. These devices may be equipped with advanced display technology to improve viewability while offering better battery life, and incorporate location-based services integrated within other applications.

<table><tr><td>Pattern</td><td>Design problem</td><td>Solution</td><td>Other patterns to reference</td></tr><tr><td rowspan="3">LED</td><td>Notice of status should have a visual component that does display.</td><td>LED, a low-power-consuming diode, is used to indicate states and status of power,</td><td>Notifications Annunciator Row</td></tr><tr><td rowspan="2">not require use of the primary</td><td>connectivity, and alerts on mobile devices.</td><td>Tones</td></tr><tr><td>Focus &amp; Cursors</td><td>Haptic Output</td></tr><tr><td rowspan="3">Display Bright- ness Controls</td><td rowspan="3">Displays are the most critical output on modern smartphones. Even minor degradations in performance can render the display uncom-</td><td rowspan="3">Although most modern mobile devices come set to automatic mode by default, the user needs manual control to modify the current screen</td><td>Display Brightness Controls</td></tr><tr><td>LED</td></tr><tr><td>Pop-Up Mechanical Style Controls</td></tr><tr><td rowspan="3">Orientation</td><td>fortable to use or unreadable, or can reduce the perception of the quality of the display.</td><td>brightness settings.</td><td>Directional Entry Other Hardware Controls</td></tr><tr><td>Devices must allow for orientation changes to display content in the manner most</td><td>Mobile devices may use automatic sensing or respond to a physical mode switch to</td><td>Kinesthetic Gestures Simulated 3D Effects</td></tr><tr><td>readable and comfortable to the user. Availability of location-based service, and the actual location</td><td>change the orientation of the display. Mobile devices have numer- ous methods of retrieving</td><td>Directional Entry</td></tr><tr><td rowspan="2">Location</td><td rowspan="2">of the handset, must be easily and accurately communicated.</td><td rowspan="2">location information, which can be used for explicit location applications, and as a trigger to initiate notifications or change behaviors of the device.</td><td>Orientation</td></tr><tr><td>Annunciator Row Icon</td></tr></table>

## Additional Reading Material

If you would like to further explore the topics discussed in this part of the book, check out the following appendixes:

The section “Human Factors and Physiology” in Appendix D This appendix provides additional information on our human sensation, visual perception, and information processing abilities.

The section “Hearing” in Appendix D Here you can become familiar with how our auditory sense works and how sound is measured.

The section “Brightness, Luminance, and Contrast” in Appendix D This appendix discusses the differences between perceived brightness and emitted luminance as well as appropriate levels needed for visual acuity.

The section “General Touch Interaction Guidelines” in Appendix D This appendix provides valuable information on appropriate sizes for visual targets and touch sizes for interactive displays.

## Appendixes

To keep the patterns focused on design and implementation, we have pulled all kinds of supporting information out of them. However, a lot of it is still very interesting. And there’s no good way for a designer or developer to get a summary of this sort of information.

So we have included it here in the form of appendixes, ordered so that you can just pretty much read it from one end to the other.

You’ll find that a few of the appendixes are actually just lists of resources. And in this day and age, resources are links to websites—which, of course, will go out of date soon. Luckily, we keep this up to date on the 4ourth Mobile Design wiki (http://4ourth.com/wiki/).

Visit any time to get the latest updates, or just to avoid typing in long links from a piece of paper. And please add your own information, or update old or changed links.