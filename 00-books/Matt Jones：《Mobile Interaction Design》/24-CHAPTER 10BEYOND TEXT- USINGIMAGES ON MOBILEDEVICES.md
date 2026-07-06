# CHAPTER 10 BEYOND TEXT – USING IMAGES ON MOBILE DEVICES

## OVERVIEW

10.1. Introduction

10.2. Ethnography

10.3. Finding photos

10.4. Browsing photos

10.5. Downscaling case study

10.6. Advanced technology

10.7. What are photos for?

10.8. Looking to the future

## KEY POINTS

Rarely does anyone take the time to organize and annotate photographs; it is likely that this trend will continue for digital photographs.

Searching photographic collections is hard, more so on smaller screens where less detail is apparent.

Mobile devices can contain many thousands of images, which requires highly scalable search solutions.

■ Besides recording an event or person, a key use of photographs is to maintain social contacts.

The introduction of communication devices with imaging has created new types of application (e.g. storytelling) that would not have occurred with camera-and-PC-style digital imaging.

■ Simultaneous audio and image recording can be used to give new purpose to images or simply to augment the experience of seeing an image.

## 10.1 INTRODUCTION

2004 was an important year for mobile computing and photography – it was the year in which camera-phone sales overtook the sales of digital cameras. According to iSuppli (www.isuppli. com), 100 million camera-phones were bought in 2004 as opposed to just 20 million digital cameras. As the technology improves, we will, no doubt, have handsets capable of taking multi-megapixel images which are stored on gigabyte-sized long-term storage. It is possible to take images of any aspect of your life and carry these images with you anywhere you take your cellular handset.

The great benefit of camera-phones is that they have communication capabilities at their core, so sharing photographs should be straightforward. Cellular service providers are hoping that Multimedia Messaging Service (MMS) – the standard way to send a picture from a cellular handset – will prove as popular as SMS.

Of course, photographs are only the beginning of rich media content. As 3G becomes widespread, we are starting to see video transmissions, music files and even virtual environments turning up on handsets.

In this chapter, however, we will focus exclusively on static images. There are several reasons for this; most importantly, as camera-phones have been around for a few years now, there is more research relating to their use than any other media type. The approach presented below is equally applicable to other types of rich media, however.

## 10.2 ETHNOGRAPHY

Rather than rush headlong into the excitement of counting megapixels, it is worth standing back and taking a look at what people do with paper-based photographs. Sure, these new devices will allow people to do things with photographs that were not previously possible: for instance, should we be recording audio along with the photograph? What about text annotations? Cataloging for albums or sharing images with others? However, before we look at any of these advanced features, we need to make sure that the systems we produce now are able to support how users work with photographs currently.

If you have read the earlier chapters of this book, you will know that the way to answer these questions is to conduct some form of ethnography. Fortunately, a lot of work has already gone into analyzing what people do with paper-based photographs and, to a lesser extent, what happens to digital photographs.

## 10.2.1 WHERE HAVE ALL THE PHOTOGRAPHS GONE?

It would be nice to believe that we are all highly organized beings, who work efficiently and are in control of our lives. How many of us fall into that category, however? When it comes to collections of photographs, how organized would you say you were? Are all your photos neatly annotated and stored in albums, resting on a shelf in chronological order? If photos are not stored in this way, then how do people organize them?

A study undertaken by Frohlich et al. (2002) produced some alarming results. They undertook an ethnographic study funded by HP to answer these questions. Essentially, most people do nothing to organize their photographs – the time required to organize them into albums is simply too great. One of the families studied had 20 years’ worth of photographs in a drawer under a sofa-bed!

Some people did manage to organize photographs for particular events, such as birthdays or weddings. Unlike the organization of regular photographs, participants were keen to work on these ‘special’ projects. (One can speculate that, in this instance, the task is creative and the photos are a single part of the wider task; organizing photographs for the sake of having organized photographs is obviously a less attractive task.) So most photographs stay in the packets in which they were returned from the processing laboratory and these packets end up distributed around the house. Besides the problems of organization, users also confessed a tendency to forget the locations and identities of people from older photographs.

Rodden (2002) also conducted an extensive survey of what people do with their photographs. The findings were similar to those in Frohlich’s study, with people tending to keep photographs in their original packets and only occasionally making an album of a special event.

So, from our ethnography, we can conclude that any system which relies on users explicitly labeling photographs (or making any other sort of meta-data annotation) is unlikely to succeed. However, it would be great to provide some way of remembering who is in a given photograph.

One aspect unique to Rodden’s study was her interest in how people used (or searched) their collections. She discovered that people often searched for an individual photograph. To aid their search, they would remember something about the packet the photograph was in, or would remember a vague point in time when the image was taken. Of course, if images had been moved from packets, or the packets were out of chronological order, these search recollections were useless.

Another class of search activity was finding a group of photographs all containing the same element, usually a particular person. This was often an impossible task and required a full search of the entire collection.

Clearly, from Rodden’s research, any application to support digital photography will have to support:

Searching for an individual image

Searching for a special event

Searching for a group of photos containing a common element.

To follow up on these ideas, she asked users what features they would want from photograph software to support these activities.

The first requirement was for folders which are used to group photographs of a particular event. It is also necessary for the folders to be arranged chronologically.

A slide show facility was also highly rated as a way to share the images.

Text annotations were also considered useful, but there was no consensus on how they might be implemented.

To support searching, users wanted to be able to see all the contents of a folder simultaneously. This should be supported by a rapid-scan facility ‘like video fast-forward’ to rapidly search the archive.

Chronological ordering was also considered important, more so than being able to search for a given date (the human sense of time being more relative than absolute).

More importantly were the features users did not value. None of the users (except an art student and an architecture student) wanted to search on image attributes like color and composition. Also, searching for similarity in images was not valued, as users reckoned that similar images would be taken at the same time, so chronological ordering would be sufficient to support this type of search.

## 10.2.2 DIGITAL ETHNOGRAPHY

If we know what people do with paper-based photographs, what do they do once they are in the digital domain?

Frohlich et al. (2002) continued their study on paper-based photography into how people used digital photographs on a PC. Interestingly, they did not see evidence of any organizational scheme on the PCs. They attributed this primarily to the fact that digital photography had not yet replaced paper-based photography; families were simply not prepared to store their most precious memories in something as ephemeral as hard disk data. Instead, the hard disk was used as a dumping ground for images, which were then sifted for forwarding to other friends or family members.

Like Frohlich, Rodden continued her research into the usage of digital images. She discovered that, although users of digital images put no more effort into organizing their photographs than they did with paper-based images – when the camera’s memory filled up, the photos were dumped into a folder which may or may not be labeled – they felt that their digital image collections were better organized. Rodden attributes this to having all the images in one place (no more individual packets around the house), in folders (which roughly correspond to events) and in chronological order (generated for-free by the PC file system).

So, bearing in mind that we know people want to search for events, groups and single images, how can we build software to support these activities?

## 10.3 FINDING PHOTOS

Finding text is easy – Google can search 8 billion web pages for a given phrase in less than a second. This is possible because written language was developed as a concise abstract way of sharing knowledge. Searching photographs this way is impossible, as there is no simple automatic way to extract meaning from the image – you may be able to find an image of your Aunt Lucy rapidly, but your computer doesn’t know what Aunt Lucy looks like, or even what an ‘aunt’ is. The information is implicit, which is of no use to the computer.

To compensate for this lack of explicit information, we can ask the user to annotate each photograph with typed text. Once the annotations are complete, we can then search the text relating to the image. Of course, this scheme will work only if users go to the effort of labeling photographs. While this may happen for professional photographic agencies, we know from Frohlich and Rodden that amateur photographers are unlikely to put in the effort to annotate their photographs.

(This is further exacerbated on mobile devices where text entry is complicated by limited input functionality.) As expected, users did not annotate their digital photographs any more than printed photographs. While a user might label a folder the image is stored in, individual image names remained largely unaltered.

The PhotoFinder system from Kang and Shneiderman (2000) goes some way to alleviating this problem by allowing users to drag ‘canned’ annotations onto a photograph (see Figure 10.1). These annotations may be taken from the user’s address book, so that they can easily label photographic subjects. This solution seems like an ideal way to address the problem of forgetting the names of people in photographs (reported by users in Rodden’s study). However, it’s not clear how easily this solution will transfer to camera-phones that don’t support this type of ‘dragging’ interaction.

![](images/d83e206c475eba1564bde885112a75bd5e4d3e30441480174adb19c1a2ac63a4.jpg)  
FIGURE 10.1  
Dragging an annotation from the box on the left allows members of an image to be tagged with meta-data without any typing

The good news is that meta-data need not be entered explicitly. Mobile devices, and cellular handsets in particular, have meta-data available to them from other sources. We shall investigate the application of these below. Before we do that, it’s worth noting that using the image data directly (i.e. the pixel values of the image) is of little benefit in finding images. Rodden et al. (2001) found that searching for objects grouped by similar attributes (e.g. a lot of green in the image) was less useful than searching for images arranged around some meta-data category.

## 10.3.1 META-DATA

The term ‘meta-data’ refers to data about data, in this case data about photographs. Meta-data is essential in searching for images, as it gives context to an image that is otherwise meaningless to a computer. Below we discuss some of the forms of meta-data that could be used.

## Time

As part of the Exif format (Exif, 1998) for storing digital images, digital cameras automatically record the time a photograph is taken. Intuitively, we would expect that ordering photographs according to time would help users locate them. Research from Graham et al. (2002) confirms that time does, indeed, help users locate photographs. In fact, it’s impossible to find a photo browser that doesn’t allow users to order their photograph collection according to time. More sophisticated systems, however, try to automatically extract ‘events’ from the collection by spotting periods of time when more photographs were taken than usual; for example, Loui and Savakis (2003) report a system that automatically generates digital ‘albums’ by spotting clusters of photographs taken over a given timeline.

## Location Data

One obvious way to search for photographs is according to location. Using a GPS system in conjunction with a digital camera allows us to accurately record where a particular photograph was taken. Toyama et al. (2003), for example, report a photo management system which they created to use with GPS-enabled cameras. The accompanying photograph management software allows users to browse their collections on a map showing where each photograph was taken.

## Diary Data

Besides being a camera and a phone, camera-phones are also diaries. In other words, they can know where we are at a given time and with whom we’ll be meeting. While it’s a pain to fill in this type of meta-data for photo-organizing software, many of us are motivated to fill it into a diary as an aid in organizing our lives. So, if we take a photograph when our diary says we are ‘Meeting with Aunt Lucy in Darkest Peru’, then the handset could automatically attach ‘Aunt Lucy’ and ‘Darkest Peru’ as meta-data to the image. To date, we haven’t found a system that exploits this type of information.

## 10.3.2 META-DATA MANAGEMENT

A project from the Helsinki Institute for Information Technology and the University of California at Berkeley has been looking at tying together all these different threads of meta-data and allowing users to review the inferences the system is making (Sarvas et al., 2004). The system automatically records location, time and user data as one might expect, but then compares these readings with values in a central server to see whether any further meta-data is available. The idea is that a lazy user can exploit the efforts of a user willing to enter the meta-data. However, before any inferred data is attached to the image, the photographer is first asked for verification. The process is neatly summarized in Figure 10.2.

## 10.4 BROWSING PHOTOS

Given the meta-data available, how do we facilitate someone rapidly browsing or searching through thousands of photographs on a screen smaller than the size of a single standard print? Well, from the ethnographies on photographers, time is seen as a key way in which people think about and organize their photographs. Ordering chronologically would therefore seem like a good place to start. (This is fortuitous, as all current digital cameras support time-stamping.) Spatial and other forms of meta-data will all help in locating an image, but should not serve as the primary interface for a general photograph browser.

![](images/93557ed8fddbf8358221969170794a7d56fea2ed031807620fd3792d81e3c489.jpg)  
FIGURE 10.2  
The process of inferring data from images taken by other people

So having decided that we wish to display images chronologically, how can they be effectively displayed on a small screen?

## EXERCISE 10.1

## PHOTOGRAPHIC TIMELINES

We know that people think about their collections in terms of time: either absolute time, where day, hours and minutes are provided, or time in terms of a series of events. Given this information, how would you go about designing an interface to a photographic collection on a small screen? Is a simple timeline enough? How would you cluster images? What information do you need to give on screen besides the photographs? ■

## 10.4.1 TIMELINE

As Harada et al. (2004) report, when getting feedback on their timeline system, it is essential to provide the users with a wide context of photographs; showing a few on the screen is insufficient. A naive start would therefore be to shrink all the photos to a smaller size and display as many of them as possible in a grid on the screen. This is, in fact, the approach taken by most contemporary software for mobile devices. The details may vary – the iPod photo has a 5 5 grid on a two-inch screen, while ACDSee for PocketPC uses a 3 3 grid on a 3.7-inch screen – but the interaction is the same. We shall shortly investigate the effectiveness of this solution.

## 10.4.2 TREEMAPS

Khella and Bederson (2004) have developed a PocketPC version of the excellent PhotoMesa desktop image browser. The system works by showing a small thumbnail of every image stored on the device, but laid out as a treemap and not in a simple grid. Images are grouped in the treemap depending on the folder in which they are stored. Clicking a group expands the individual images to fill the screen, and selecting a thumbnail expands the thumbnail to a full image. These expansions are smoothly animated to preserve the users’ context within the application: in other words each screen is not suddenly replaced with the next, which has been shown to lead to user confusion (Combs and Bederson, 1999). The interface is shown in Figure 10.3.

## BOX 10.1 TREEMAPS

Treemaps were developed by Ben Shneiderman as an efficient way of visualizing hierarchical data. This technique has been applied to photographs, stock markets, Usenet groups, hard disks, etc. – in fact, any form of hierarchical data you can think of. There are variations on the technique to optimize it for different application areas, but essentially the visualization attempts to display every data item on screen simultaneously. The size of each item varies depending on the user’s criteria – for example, in the stock market visualization, the area used to display information about each individual company is directly proportional to the company’s value. A well-designed treemap is an astoundingly effective tool. The potential problem with using them for photographs is that there is no intrinsic ‘value’ in the photograph to determine the relative size at which the photographs should be displayed.

To find out more about treemaps, check out the following site:

http://www.cs.umd.edu/hcil/treemap-history/ ■

Sadly, in user tests, the browser did not perform quantitatively better than a standard thumbnail browser (ACDSee in this case). However, users’ subjective experience was much more positive, enjoying the zooming aspect of the interface and the treemap layout.

One area for concern with Pocket PhotoMesa is its scalability. The first image in Figure 10.3 shows the interface working with 110 images. The authors concede that the interface will not scale much beyond that, but justify their decision by stating that mobile devices do not have a storage capacity much greater. This may have been true at the time the system was developed, but since that time devices such as the iPod photo have come to market: the iPod can hold 25 000 images!

## 10.4.3 RSVP

The approach taken by the iPod to managing so many photographs is an interesting blend of solutions. One area where the iPod has always shone is the tight integration between the mobile device, the desktop computer and the online iTunes music store. For the iPod photo, iTunes synchronizes the photos from the user’s iPhoto collection (iPhoto is the standard photograph management software for Macintosh OS-X). So, any albums or rolls created in iPhoto appear on the iPod in much the same way as song playlists appear. Selecting a group of photos fills the screen with a $5 \times 5$ grid of thumbnails. Using the jog wheel, the user can scroll to the desired images as they would on any standard thumbnail browser – rather disappointingly, there is no smooth transition between thumbnail screens to maintain context as one finds in, say, PhotoMesa. Selecting an individual image, however, allows users to view images according to an RSVP paradigm – turning the scroll wheel scrolls users through full-size images (see Box 10.2).

![](images/a9964445103bacc754d4d71f96d19b426a62c55a082e5c0eebcea9bbd1ab6a01.jpg)  
FIGURE 10.3  
The PocketPC version of PhotoMesa showing all images simultaneously

In an effort to determine how effective an RSVP approach would be in browsing image collections on a variety of devices, Spence et al. (2004) conducted a major multi-factor evaluation. They set users the task of identifying a single target image from a collection of 64. Users were presented with images at different rates, on different screen sizes (to simulate a PC screen, a PDA screen and a cellular handset screen) and in different layouts. Their were several significant findings from their experiment:

Users had great trouble in identifying images properly if they were shown for less than 100 ms.

Screen size did not affect the task error rate.

Users preferred mixed-mode presentation.

The first finding was universal across all modes of display – the human visual system cannot parse images properly if they are replaced more often than every tenth of a second. In these experiments, the visualization rate was under the control of the system. With the iPod photo, the user can dynamically alter the presentation rate using the scroll wheel, allowing them to find the presentation rate which best suits their current conditions.

Interesting, for designers of mobile devices, was the finding that the screen size did not effect task performance. It is not clear whether this result was due to the nature of the task chosen by the researchers, but this finding could be seen to support the perceived suitability of RSVP to devices with small screens.

Taking the last point, the researchers in this experiment created a hybrid mode between ‘pure’ RSVP (one image per screen) and thumbnail presentations (multiple images per screen). They found that a mixed-mode approach of rapidly presenting screens containing four thumbnail images proved most successful with the users. Interestingly, this is not the approach taken with the iPod photo, where the thumbnail mode remains distinct from the RSVP mode.

## BOX 10.2 RSVP

RSVP is an acronym for Rapid Serial Visual Presentation, a visualization technique developed by de Bruijn and Spence (2000). The idea behind this approach to visualization is to throw snippets of information at the user to give them an overview of the entire contents of whatever it is they are looking at – think of flicking through the pages of a book in a bookstore or fast-forwarding a video DVD. More formally, the idea is to compress information in time rather than space. In terms of image browsing, this would mean that, rather than display four thumbnails on screen for a second, RSVP would show four full-size images each for a quarter-second. As the RSVP technique does not rely on screen size for efficacy, it would seem like an ideal visualization technique for use on small-screen devices.

RSVP works due to the staggering visual processing capability of our brains. Current estimates by cognitive psychologists, e.g. Zeki (1993), speculate that about half the celebral cortex of all primates is used to process visual information. In computing terms, this is of the order of several gigabits per second. ■

Although the results from RSVP look promising, the results reported were derived from a single task of looking for a target image among 64 possibilities. This is obviously not representative in terms of collection size or task domain (we have already seen that people wish to find events and collections of images containing the same person). We look forward to future studies which investigate the applicability of RSVP to searching large collections of photographs.

## 10.4.4 SPEED DEPENDENT AUTOMATIC ZOOMING

Another approach to visualization on the small screen is that of SDAZ (Speed Dependent Automatic Zooming) (Igarashi and Hinckley, 2000). Again, this technique was developed for desktop machines but, we believe, it has great potential for mobile devices. It was originally developed by Igarashi and Hinckley to overcome the problems of losing context when working with large documents on PC monitors. Context losses fall into two categories:

Forcing users to shift focus from the area of interest in the document and the scrollbars at the edge of the screen.

Having disproportionately large movements in the document for relatively small movements of the scrollbar, which leads to visual blurring.

Of course, these problems are greatly multiplied on small-screen devices, where the amount of screen real-estate not only forces more scrolling, but the size of the scrollbars is greatly reduced. (Having small scroll-bars was a huge usability problem on small screens, as reported in Chapter 8.)

The approach Igarashi and Hinckley took to eliminate these problems was to automatically link the zoom level to the rate at which the document was being scrolled. For example, consider Figure 10.4(a), which shows part of a document at maximum zoom. As the user starts to scroll down the document, the zoom level reduces, as in Figure 10.4(b), so that more of the document is visible on the screen. The subjective effect is like ‘flying’ over the document, where the faster you scroll the more your altitude increases. (If you’re familiar with Grand Theft Auto, a similar mechanism is used to link the map scale to driving speed.) Despite being visually appealing, the results from user evaluations were disappointing. For the tasks set, SDAZ was no better, and occasionally worse, than existing techniques.

![](images/ae28ec210873abdb7dd96b67fdd5a39e4cbcbceb22aaedae72bedd7387d854de.jpg)  
FIGURE 10.4  
(a) The document at full zoom; (b) as the user starts to scroll, the zoom level is automatically reduced

Undaunted by this result, Cockburn and Savage (2003) improved on the original SDAZ algorithms, producing a highly responsive system with improved scrolling. They conducted evaluations for two application domains; namely document viewing and map viewing (the first testing vertical scrolling, the second testing vertical and horizontal scrolling). For document scrolling, users were, on average, 22% faster when finding a target text than they were with a commercially available document viewer. For the map application, users were 43% faster. Added to these quantitative measures, qualitative feedback from the users heavily favored the SDAZ techniques.

Given this successful set of results, we were inspired to adapt SDAZ techniques to scrolling through photos on the small screen. At least, that is what we thought we would do. It turns out that we had to think of a lot more than just the screen size. The physical diversity of camera-phones and camera-PDAs is truly staggering. This applies not just to the dimensions of the screen, but also to the physical input mechanisms available: some have touchscreens, others have jog-wheels and some even have tilt-based interfaces. Therefore our final, modified SDAZ algorithm would need to cope with diverse input devices modifying images on a screen that is as little as 5% of the size the algorithm was originally developed for!

We do not claim to have a sure-fire way of converting interaction techniques from desktop to mobile systems – due to the inherent diversity, it is unlikely that a prescriptive technique is possible. However, we will take you through the steps we followed as an example of how one might approach this type of problem.

## 10.5 DOWNSCALING CASE STUDY

## 10.5.1 ARRANGING PHOTOS

The first decision we needed to make was the order in which photographs would appear on the screen. We could have a two-dimensional browsing scheme, with photographs laid out in a grid. Alternatively, we could present photographs linearly and stick with one-dimensional scrolling. As the two-dimensional system had proved so dramatically effective in Cockburn and Savage’s work, we tried hard to think of a meaningful organizational scheme that would result in a regular grid of photographs. From the ethnographic studies reviewed already, particularly Rodden et al. (2001) and Frohlich et al. (2002), we knew that most users favored a chronological layout. We therefore produced a one-dimensional SDAZ system, allowing users to scroll vertically through a chronologically ordered list of photographs.

## 10.5.2 SCREEN SIZE

As we discussed in the prototyping chapter, we always start development of any technique on a desktop machine to see whether our approach is viable. In this instance, we developed in Java to make the most of the Piccolo toolkit developed by Bederson et al. (2004) – if you develop interfaces that scroll and zoom, this is an excellent resource. In effect, we replicated Cockburn and Savage’s system, but this time limiting ourselves to a standard 240 320 PDA-sized display area. Once we had the algorithm working, the next problem we faced was in setting the thresholds for the zooming.

SDAZ has two thresholds, which we will call ‘take-off’ and ‘cruising altitude’. To explain further, when the user is making small scrolling movements of an image, it is not necessary to decrease the zoom level – the desired portion of the document is, obviously, already visible. When the user makes large scrolling movements, then the zoom level should decrease so that the user can have a wider view of the document. The point at which the zoom level starts to decrease is the take-off point. Once ‘in the air’, the user can continue to increase the scroll rate, which will continue to decrease zoom level. However, the zoom reduction cannot continue unabated, otherwise the document will eventually zoom to a single pixel and disappear. That is why we need to set a cruising altitude, beyond which the user can continue to increase scroll rate but the zoom will remain unaffected.

When setting these for our application we obviously could not naively adopt the values from previous research in desktop systems – the ‘take-off’ point could be a value greater than the number of pixels on the small screen! In the end, we modified our prototype to allow these thresholds to be set dynamically. This can be seen in Figure 10.5, along with sliders to set initial zoom levels, etc.

With this version of the prototype, we conducted informal evaluations to find default values for the algorithm. The good news is that the settings for a given device seem to be constant across all users – the algorithm does not need to be customized for each individual user.

Once we had default thresholds in place, informal feedback from users was very positive, but most expressed skepticism that the highly graphical approach of SDAZ could be supported on a device as computationally limited as a PDA. This seemed like a valid criticism so, rather than continue with full user evaluations, we decided to see whether it was possible to implement an acceptable version of SDAZ on a PDA.

![](images/c5058026f7e7a4feeea14f4d12181fd906197ce9133642a1e779ee3fd9ea4af2.jpg)  
FIGURE 10.5  
You can see the sliders which allowed us to tune the thresholds to the smaller screen size

## 10.5.3 WRITE ONCE, RUN ANYWHERE

One of the advantages of developing in Java should be that you can deploy the same code on multiple hardware platforms. This is largely true, but we had a problem in that we were using Piccolo Java, which needs J2SE (designed for desktop computers), not J2ME which is more common on mobile devices. Fortunately, we found a version of J2SE for mobile Linux, so set up a PDA running J2SE on top of Linux. However, it turned out that this version of J2SE didn’t implement the graphics routines we needed.

We won’t bore you with the details, but we could have saved ourselves months if we had planned our prototype strategy more effectively from the outset. In the end, we scrubbed the original code and reimplemented the prototype using .net, making sure the routines we used were also available in the compact framework version. Of course, we could have done this with Java, limiting ourselves to J2ME routines, but Waikato University had just given us the fastest PDA available commercially. This PDA was running PocketPC, so we felt this would give us the best shot at producing a workable implementation. In the end, it took several months’ work and some consultation with Microsoft, but the SDAZ photo browser runs smoothly on a standard 5550 iPAQ.

## 10.5.4 MEANWHILE, BACK WITH THE USERS

Even if it turned out that it was not possible to implement SDAZ on current camera-phones and PDAs, Moore’s law means that these devices would eventually provide appropriate levels of computing power. (Moore’s law states that the power of processors will double every year. As this law has held true since 1965, we can be fairly confident that cellular handsets will eventually be powerful enough to run our software.) We therefore continued with the development of the interface.

From informal user experimentation, we were able to determine the default thresholds for the screen size. So far, so good. Our next issue was that of input device. Even the most basic handset available supports some way to specify ‘up’ and ‘down’, so the modified SDAZ should be able to work using no more than that. At the other end of the scale, camera-PDAs had touchscreens allowing continuous input in two-dimensional coordinates. One might, therefore, be able to directly translate the mouse movements from the desktop SDAZ directly into PDA stylus movements.

Due to the highly graphical nature of the SDAZ algorithm, it was impossible to prototype any of our proposed solutions on paper. Each had to be prototyped and tested using a desktop simulation of the PDA. After many iterations we derived two SDAZ variants, which we called AutoZoom and GestureZoom.

## AutoZoom

AutoZoom was the variant developed for minimal specification devices – the interaction is limited to scrolling up and down. The up and down scrolling can be achieved by key, joystick, stylus or even wheel-based interaction. In AutoZoom, scrolling down starts the images scrolling down the screen, as in Figure 10.6(a). The line that extends from the circle that can be seen in the center of the screen in Figure 10.6(a) represents the current scroll rate. (The cross represents the current position of the stylus on the screen, as these images were taken using a stylus-based version of AutoZoom.) Using key or stylus or wheel, the user can ‘grow’ this line, as in Figure 10.6(b). Here, we have passed the take-off threshold and the zoom level has decreased. Similarly the line can be shrunk, so the zoom level increases once more.

![](images/a60f02d4c3c60ee64250e70a371e9c3bd19e6d215df8f3cea23cc818dbcad9a6.jpg)

![](images/c5c51519d725bd6805b391a4ae5669926c08a7c4ca19322244cffa448d8dce46.jpg)  
FIGURE 10.6  
(a) The user is scrolling and the images are at full zoom; (b) the user is scrolling faster and the image size is diminished

## GestureZoom

GestureZoom was developed for devices which allow two-dimensional input. Similar to AutoZoom, dragging the cursor vertically from the center point of the screen increases scrolling rate in that direction. For GestureZoom, however, zoom level is independent of scroll rate. Instead, zoom level is dictated by the horizontal distance of the cursor from the center of the screen. This is shown in Figure 10.7, where the stylus (represented by the cross) has been placed below and to the right of the central circle. The effect of this is to give a slight reduction in zoom level (proportional to the length of the horizontal line to the right of the circle) and to scroll the images down the screen (at a speed proportional to the length of the vertical line below the circle).

![](images/7721ce92f8802c9b383997ed88e7753b48587a6bc447bca056a0c6bc078fff97.jpg)

![](images/6f03da877dab7a7d8270f98934f062a1687500823ae6a288832e5e7e69fe0857.jpg)  
FIGURE 10.7  
(a) The user is scrolling and the images are at full zoom; (b) the user is scrolling faster and the image size is diminished

Sadly, a paper description and static images do not do justice to this highly interactive technique. Experientially, it allows users to fly rapidly over their photographs, swooping down for more detail when they spot something of interest. At this point they can descend so the image fills the screen, or soar back up over the photograph landscape. When scrolling at maximum speed and smallest zoom, it is not possible to pick out individual images well, but events are rapidly identifiable due to the similarity in images – as we know from the ethnography, identifying events is an essential user requirement.

At the risk of over-emphasizing a point, you should always conduct user tests as early and as often as possible, no matter how informal. Even if the testers are your friends, exposure to your system, especially over long periods of time, is invaluable. By doing exactly this (installing our system on people’s computers and watching them ‘play’ with it), we discovered two things about GestureZoom and AutoZoom that we would never have picked up, even in formal user testing.

Firstly, we discovered that we needed to add a third threshold to the algorithm! This came about as the size of the photo collections we examined increased. On the small screen, once the cruising altitude has been achieved, it was taking users too long to scroll down their collections. We therefore added a new threshold, beyond which scrolling rate would accelerate. Descriptively, this notion of three thresholds may sound overly complex, but is surprisingly natural in usage.

Our second discovery was the usefulness of the scrollbars (visible in Figures 10.6 and 10.7). The widget set used to develop the application included a scrollbar by default on this type of window. As people played with the application, we realized it provided good feedback on where, roughly, the currently displayed photo fell in the current collection. Also, it provided a very coarse way for users to scroll to a particular part of their photo collections. As Igarashi and Hinckley observed, the scrollbar was too coarse-grained to be used as the only way of scrolling through a photo collection, but worked will in combination with AutoZoom and GestureZoom.

So having conducted informal tests and ironing out the unforeseen issues with this new technique, we proceeded on to full user testing.

## 10.5.5 USER TESTING

## Tasks

Just as Khella and Bederson (2004) had done when testing Pocket PhotoMesa, we wanted to test how the SDAZ variants compared with thumbnail browsers for typical photo-finding tasks. Our experiment therefore had to evaluate three separate systems (Thumbnail, AutoZoom and GestureZoom).

When deciding on the tasks for users to perform, we tested for the tasks identified in the ethnographic studies of Rodden et al. (2001) and Frohlich et al. (2002), namely:

Finding events – locating a group of consecutive images related to a well-defined event

Finding an individual image – locating a single photograph from the entire collection

Finding a group of images containing a common element – locating a group of non-consecutive images which all share something in common (e.g. identify all photos in which you appear).

One final influence for our evaluation was taken from Cockburn and Savage’s original evaluation of the improved SDAZ. In their paper, they tested whether there was any difference in scrolling techniques when scrolling for a distant target or a close target. Therefore, when designing the tasks for locating events and individual images, we ensured that some targets were close to, and others far from, the point of origin – for our purposes, ‘far from’ is defined as requiring the user to scroll through more than half the total photographs in the collection. Obviously, this distinction of close and distant does not apply to the search for a group of images, as users are expected to scan the entire collection. When searching for individual images, we did make the distinction of asking users to search for images containing large features and small features (in this instance, we defined large as occupying more than an eighth of the image area). Also, we wanted to test whether the size of an event had any bearing on how easy it was to find. We therefore had far and close events which were both large (more than three photographs) and small (three or fewer photographs).

## Conditions

By taking into account the three influences described above, our experiment ended up with three independent variables as follows:

1. System type: AutoZoom, GestureZoom and Thumbnail

2. Task target: event, individual image and image group

3. Target distance: close and far (or big and small).

Taking into account the different values for each of the independent variables, we end up with 27 conditions. At 10 users per condition, this would imply 270 users! However, even with some statistical jiggery-pokery, we ended up having to test with 72 users to provide statistically meaningful results. (System type was between-subject, while the other variables were within-subject.) As this is not a chapter on experimental method, we shall spare you the drudgery of the procedural details. You can always read the paper on the experiment (Patel et al., 2004) if you’re interested.

## Results

The results from our evaluation were very encouraging. To summarize:

Events

1. AutoZoom and GestureZoom were better than Thumbnail browsing for finding small events. For events in general, there was no significant benefit from the SDAZ systems.

2. Far events were found more quickly than close events.

3. For far events, long events were found more quickly than short events.

Individual image

4. AutoZoom was better than Thumbnail browsing for far images.

5. SDAZ techniques were better for finding images with small features.

6. Close images were found more quickly than far images.

7. Images with large features were found more quickly than images with small features.

## <sub>•</sub> Image groups

8. No interface was proved faster in identifying image groups, though SDAZ-based interfaces provided much more accurate results.

## Discussion

Overall, the new systems were just as fast as, and sometimes better than, existing thumbnail browsers. Given that none of the users had seen an SDAZ-based system before taking part in this experiment, the results are particularly encouraging. Taking each result in turn:

1. We speculate that this result is due to the fact that the user has greater control of the scroll rate than with a thumbnail browser. The discrete lurching from screen to screen of thumbnails may result in small events going undetected.

2. This seemingly paradoxical result came about as users assumed that the image would be far away and were keen to start scrolling as quickly as possible.

3. As users scroll further from their origin, their scroll speed increases, which can hide small events.

4. It is not clear why AutoZoom (and not GestureZoom) should be better here, as in every other task they performed identically. We would speculate that this is an anomaly and that SDAZ techniques provide much faster scrolling rates than are possible with thumbnail browsers.

5. SDAZ will allow users to select an appropriate size of image, allowing them to see small features which are hidden in the predetermined image size of the thumbnail browser.

6. This result would have seemed self-evident had we not observed result number 2. Further investigation is need to see why close images are found more easily than close events.

7. This result seems self-evident.

8. When completing these tasks, users scrolled at a uniform rate. Again, it seems that the ability to select a dynamic zoom level allowed users to select a level appropriate to the task.

## 10.5.6 PLATFORM

Having conducted these experiments, and found such promising results, we were motivated to continue development onto the target hardware platforms and explore other variations. One direct implication from our experiment was that the AutoZoom system (with more simple input needs) was just as good as (and possibly better than) the GestureZoom system. Therefore, we are currently concentrating on AutoZoom.

Currently, AutoZoom is running smoothly on a variety of iPAQs and a Nokia 6600 handset. We are also looking at ways of enhancing AutoZoom, perhaps using semantic zooming techniques involving timelines, as in Harada et al. (2004).

The system we developed here is only the first step into photo organization; there are many variants on this system which one might pursue. However, we are convinced it represents a sound, scalable solution to the problems of image searching as identified in the earlier ethnographic studies. Like the developers of RSVP, our solution hinges on human capabilities: specifically, the capacity for rapid image processing and a good understanding of relative time. Other researchers, however, are pursuing solutions based on machine intelligence in order to aid users in finding photographs. These two approaches are not necessarily exclusive and we shall look at some promising avenues currently being explored.

## 10.6 ADVANCED TECHNOLOGY

One alternative to simply shrinking the image to a thumbnail is to automatically crop the image to an area of interest within the photograph. Of course, it is tricky for the computer to figure out what a human might find interesting. However, there are algorithms which make a reasonable attempt by exploiting knowledge about how the human visual system works. One such algorithm developed specifically for PDAs is reported by Liu et al. (2003) (see Color Plate 7). While the approach looks promising, the evaluation in the paper is rather disappointing. Instead of measuring how the cropped photos affected searching and browsing performance, the authors conducted an experiment in which users rated the algorithm’s performance in identifying interesting parts of the image. So while the algorithm could find interesting things, we don’t know whether it aids humans in image recognition and retrieval – for instance, it may turn out that users remember the overall composition of an image much better than the component key elements. Until such an evaluation is conducted, it would be unwise to adopt this technique – especially as it is currently too computationally expensive to run on a PDA or digital camera.

Another alternative is not to show all the images stored, but rather a single key image to represent a group of similar images. The problem then becomes one of figuring out what distinguishes a key image from other candidates. Research such as that by Savakis et al. (2000) and Luo et al. (2003) has shown the following factors to be important:

Colorfulness

<sub>•</sub> Sharpness

Format uniqueness (e.g. the only panoramic image in a group)

Skin area

<sub>•</sub> People present

Close-up subject

Good composition

Analyzing these factors from a sample data set, researchers built a Bayesian network to identify key images (Luo et al., 2003). As an evaluation of the network, they compared the images it selected as ‘key’ to those selected by humans: 77% of the images selected by the network were in the top three chosen by the user group. This is a fairly impressive result on one level but, again, does not constitute any kind of meaningful result. In their work, these researchers are assuming that a single representative frame is the best way to identify a given event. A better evaluation would have been to simulate some user task, such as finding a particular event, and seeing whether the key image selected could be used to identify an event more quickly than an image chosen at random (or the first one for a given event). Given that the computation required to identify a key image is fairly expensive (too much for current camera-phones or PDAs), it may be that a randomly selected image is good enough to represent a group of images.

## 10.7 WHAT ARE PHOTOS FOR?

Assuming for the moment that we have solved the problems of organizing photos, what do people actually do with them?

The KAN-G framework from Liechti and Ichikawa (2000) suggests that it is primarily to maintain social contacts. Their work is based on ethnographic studies which show that photographs are used within families and social groups to create and build emotional links between members. These links are further strengthened by the ability of the group to give feedback on the images and share reactions to them. One of the inspirations behind their ideas comes from email and SMS ethnographies which show that people often exchange messages with fairly meaningless context just as a way of keeping in touch and maintaining emotional links: sending photos for this purpose allows much more information to be sent for relatively less effort. The ultimate goal of these links is to create a sense of ‘affective awareness’ – the sense of feeling ‘close’ to someone.

They suggest that social links can be created in two ways. When we receive a photograph from someone, we feel connected to them; knowing that someone has seen a photograph I sent to them connects me with that person. One consequence of desiring feedback on an image is that users tend to email them to recipients, rather than place them on a website. Emails are a symmetric communication medium which encourages commentary, whereas the web tends to be asymmetric. The mix between using the web and email is analogous to the situation from paper-based photography where we have albums for special events, but the rest of the images float around the house where they can be viewed by anyone who is sufficiently well known to be let into our house.

## EXERCISE 10.2

## SOCIAL AWARENESS

Given that photographs are used to maintain social contact, design an information appliance for social contact preservation via images. Think particularly about the issues of calm technology, context (social and technical, especially) and which user groups in particular may want a device that does these things. Having thought about all that, how well does a camera-phone fulfill that role? ■

So, returning to the camera-phone, what happens if we think of it as a social link tool, rather than a miniature version of a camera-cum-digital-gallery? Firstly, the device should be able to display images in a ‘calm’ fashion (see Box 10.3 for a discussion on calm technology) – so the screen saver on my phone should be able to cycle through my MMSs. (This does not really represent a huge change in technology.) More interesting is the ability to show people that you have seen their photograph. At present, this functionality is provided in email and SMS by including the original message as part of the reply. There does not seem to be any handset which supports replying to an MMS by, say, overlaying text on the original image.

## BOX 10.3

## CALM TECHNOLOGY

The notion of calm technology was first suggested by Weiser and Brown (1997). They were keen to ensure that, as the number of computers around us increases, they do not overly intrude into our lives. At present devices like cellular handsets, PDAs, pagers and computers all attract our attention in fairly invasive and irritating ways. Instead, ➤

Weiser would like to see devices that inform without irritating. One of his key ideas is to have all devices lie in the background of awareness and come into ‘center stage’ only when they have something urgent to tell us. As an example, think about the helpful balloon and accompanying beep that appear every time you insert your USB drive into a Windows computer. Is it really necessary to announce this and attract your attention every time you insert the drive? Calm technology is an attempt to force designers to consider what information the user should deal with immediately and what information should be left available for the user’s convenience. ■

Of course, being mobile, camera-phones can be used to show images to other people when meeting together. Rodden discovered that laptops are an ideal way to show and share photographs, unlike the desktop systems examined by Frohlich. Similarly, the television-out feature on many digital cameras was seen as an ideal way to share images. Using add-on Bluetooth devices, camera-phones already have the ability to display images on a television screen for shared viewing.

The research and ethnographic studies on mobile photography emphasize the value of sharing photographs to improve and maintain relationships. Counts and Fellheimer (2004) built a system for camera-phones which supports what they term ‘lightweight’ sharing. Identifying that a barrier to sharing is the effort required to make the sharing happen on a mobile device, their system is set up to automatically share photos with a group of friends. To improve social cohesion, the application constantly displays images of group members, and clicking on an individual image reveals the photographs taken by that person. Surprisingly, in the field studies, users were happy to have their images shared indiscriminately – only one user changed their photo-taking habits. Also, recipients were not swamped, as the metaphor for retrieving images was a ‘pull’ rather than a ‘push’ based approach like email (calm technology again). In fact, users reported enjoyment at looking through the latest images taken by people in the group. The biggest design flaw reported was the fact that the application supported only one group of people; participants would have liked several groups of friends, at the expense of an extra click in the sharing process. Finally, one excellent extra addition to this system was a client application for PCs. This allowed users to offload and archive data from their device. This notion of online and offline integration is discussed further in Section 9.5.

So, provided the cost of image sharing is not prohibitively high, sharing images from a mobile device does indeed seem to fulfill the aims of maintaining and improving relationships.

One final interesting discussion from Liechti and Ichikawa’s work is around video conferencing, a technology which many network providers hope will drive revenue streams. They postulate that annotated photographs may prove to be a more effective (and affective) means of communication than can be achieved with video conferencing. In part, this idea is driven by their observation that static images are still cherished in an age when it is so easy to record video. Again, we do not need more technology, we just need to understand what people want to do with communication media and how to support their social needs.

## 10.7.1 WHAT ARE WE SHARING?

Given that photo sharing is clearly a popular activity, what is it we are sharing? There is a branch of anthropology called ‘visual anthropology’ dedicated to answering that question. Obviously there are artistic, scientific and journalistic applications, where the photographs have a well-understood purpose. Less obvious in application is the home photograph. One visual anthropologist, Richard Chalfen, has produced numerous works studying how North Americans and Japanese use home photographs (see more at www.richardchalfen.com). Reporting on their work, Liechti and Ichikawa (2000) show that photographs are taken for five main purposes:

Shared photographs – photographs taken to give to friends

Household photographs – for framing and display

Work photography – photos to display at work

Wallet photography – personal photos to be carried in a wallet or purse

Tourist photography – photos taken on holiday

These results come from the study of paper-based photography. A study of children using prototype camera-phones in Finland shows that the potential uses of mobile photography are much more diverse (Makel¨ a¨ et al., 2000). In this paper, five separate activities are identified:

Creating stories

Expressing spirituality – art from photographs

Expressing affection

Increasing or maintaining group cohesion

Conversation support – augmentation with images

Overall, the images were used for expressing emotion or humor. The images were of primary use where sender and receiver were sufficiently aware of each other’s lives to make the image meaningful. Within the family context, the exchange of images was seen by older family members as a great way of communicating with their children or grandchildren.

In a later study by Kurvinen (2003), the author analyzes the use of MMS and discovers that message senders will often send ‘teasing’ images in order to elicit a response from the recipient. The example given is of a message showing a ring on the finger of the sender’s hand – he has just become engaged. The recipients then respond with appropriate messages.

The work reported in Bitton et al. (2004) represents an interesting approach to studying digital photography. This project sets out to discover how people use a new type of digital camera which records a minute’s worth of audio before, and after, an image is taken. The authors go to great lengths not to influence their subjects, so do not show them other users’ recordings or give them any ideas of what the camera should be used for. To their credit, the authors evaluate the device in a developing world context to see how people who have low media exposure use the device. Initial observations from their work suggest that image collection falls into one of four main categories:

Social glancing. Essentially the recording is used as a ‘conversation piece’ around which to build up some social interaction.

Caught in activities. Recordings are used to document activities in a given day. There is no intended audience for these recordings but they simply act as a documentation of the activity.

Active documentation. Here, the user produces a mini-documentary about some aspect of their lives.

Intentional disclosures. In this category, the audio and images are used in a complementary fashion to communicate a specific idea or message.

## EXERCISE 10.3

## MOBILE BLOGGING

All of the above uses for the audio imaging devices sound plausible, but it is by no means an exhaustive list. The device that was created for the research seems like an ideal mobile blogging device (except that the results are not placed on the web). To start with, consider how design enhancements to the system would allow the device to become a blogging tool. Then, take a look at an existing mobile blog and see how well the posts on that blog fit the four categories given above. It’s likely that there are other types of activity not covered here. Is it possible to modify the design of the device so that it supports the new activities as well? ■

## 10.7.2 USING AUDIO WITH PHOTOGRAPHS

As mentioned at the end of the previous section, one other digital enhancement of photographs is the use of audio recording. Either the audio can be recorded at the time the photograph is taken, or a subsequent recording can be attached to the photograph. The purpose of most audio/photo systems is not to aid in searching (although, with speech recognition, this is a possibility) but to provide more information about a photograph once it is found.

Work by Frohlich and Tallyn (1999) shows that ambient noise recordings taken at capture time can enhance the enjoyment of a photograph. Not only that, but the inclusion of the audio can ‘save’ a bad photograph – the authors give the example of a poorly lit photograph of a marching band, which was highly valued by the photographer, as the ambient noise and photo together perfectly captured the moment. Interestingly, the ambient noise seemed to act as a memory aid, with subjects talking more about the context of photographs when accompanying audio is recorded.

Here again, we see the benefits of adopting a calm technology by automatically recording audio, whether the photographer ultimately wants it or not. The software Rodden used in her study supported explicit audio annotation, but this was largely unused, even though users requested this feature from the software. One reason for this may be that, as the camera automatically time-stamps images, users considered this to be sufficient annotation.

## 10.7.3 VIDEO

Video is coming to a mobile computer near you. Either it will appear in the form of a dedicated ‘Personal Media Device’ where the hard disk contains movies and other video clips, or the movies could be streamed directly to your handset via a wireless network. There are many cellular service providers globally who are hoping you will elect the second option as they struggle to recoup the costs they paid for 3G licenses a few years ago. This is all very well, and technically viable, but will anyone want to watch movies on a small screen? Is video really a mobile technology?

Video on mobile phones has been available in Finland since the second half of 2002. A team from the National Consumer Research Center in Finland investigated how people used this service and integrated it into their lives (Repo et al., 2004). The somewhat unremarkable result of their research was that when on their own, users would watch videos to avoid being bored; when in a group, they would use the video to share an experience together. This second category of sharing a video refers not just to personal video clips, but karaoke videos which a group could sing together. It is not surprising that people wish to use videos as part of a group, but the nature of karaoke is that it relies more on its audio, rather than visual, content. Is it likely that a group of people will sit together and watch, say, a soccer match on a small screen? At the time of writing, this remains an open question.

Again, all the issues we discussed in finding and using photographs apply equally well to video. Like photographs, videos have no content that is meaningful to a computer. Beyond time and possibly location, video has no useful meta-data to aid in a search. In fact, the problem is much worse with video as users would typically have to watch several seconds of video before they could identify what the clip contains. At the moment this problem is not too great as mobile devices have limited memory and cannot contain too many clips. As storage space expands, searching for video clips will become a huge research area.

## 10.8 LOOKING TO THE FUTURE

With the advent of terabyte disks and miniscule image recorders, the idea of recording one’s entire life becomes a possibility. Although we are not big fans of ‘context-aware’ computing, recording heart rate and galvanic skin response (GSR) could provide ways to rapidly identify those sections of one’s life that are ‘interesting’, be it for positive or negative reasons. Already, systems such as the StartleCam (Healey and Picard, 1998) are designed to record images in response to a change in GSR.

However, this opens up many philosophical questions about what one should record and when you are going to get the time to watch what you have recorded. Some of these issues have already been humorously discussed in Umberto Eco’s essay on how to create a 1:1 map (Eco, 1995). With cameras, there is the added recursive problem of recording oneself while watching oneself watching a recording (etc.). Potentially more interesting are the ethical questions raised by recording so much information. How would you feel if your health insurance company could demand a full recording of your life to see how well you ate and how much you exercised?

Even with existing camera-phone technology, a number of interesting ethical problems are created. Obviously there are the invasion-of-privacy issues which have resulted in camera-phones being banned from some public buildings. Before we become carried away with the negative aspects of camera-phones, it should be realized that there are many positive aspects. For instance, it becomes a lot harder to fake a photograph of an event if several hundred witnesses of the same event have their own photographic evidence. Regardless, camera-phones are unlikely to go away due to any ethical constraint. As designers of technology, however, it is our responsibility to help make sure these devices augment society and human activity rather than restrict it.

## SUMMARY

Incorporating imaging capabilities on communication devices opens up all sorts of exciting new application possibilities. The crucial thing to remember is that, despite the ➤ marketing, the result is not a camera, but a social awareness and cohesion device. When you start to look at it in those terms, new design ideas become apparent. A lot of ethnography has already been conducted and offers some great insights into how to design new applications and devices.

Having said all that, there are still the major issues of image searching and browsing to be solved. Many approaches have been tried but few have made the successful transition from large to small screen. Until users can effectively search image collections of several thousand photographs to find a target image, there is limited application in allowing them to share images.

## WORKSHOP QUESTIONS

How do you organize your digital photographs? First write down what you think you do, and then go and check your collection to see whether that is what you actually do.

The evaluation we conducted for the zooming browsers in Section 10.5.5 tested very specific aspects of the interface. What other types of evaluation do you think might have been appropriate and what information might we have missed by conducting so focused a study?

If you have a camera-phone, go through the images you have taken that are still stored on the device. Can you classify them according to the lists given in Section 10.7.1? Are there any that fall outside this classification?

## DESIGNER TIPS

Building a photobrowser which requires users to manually input meta-data is unlikely to succeed.

Users tend to think about their collections in terms of time, be that absolute, data-stamped time or relative time, where users recall events and the order in which they occurred.

Mobile devices already have gigabytes of hard disk space. Make sure any photo visualization software you devise can cope with at least 4000 images.

<sub>•</sub> Supporting sharing of images in a rapid way is absolutely critical to the success of a imaging application or device.

Remember that camera + phone camera. Camera + phone = social awareness and relationship building device.