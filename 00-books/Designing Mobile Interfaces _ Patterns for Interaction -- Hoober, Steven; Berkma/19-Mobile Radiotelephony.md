# Mobile Radiotelephony

## An Introduction to Mobile Radiotelephony

Aside from simply understanding your place in history, the underpinnings of mobile communications can be crucial to ensuring that your particular application, site, or service works correctly. Decisions made long ago, whether technical or regulatory, influence how mobile telephony evolved, and are still felt today.

An example might help. My favorite is that SMS (text messaging) isn’t data. It looks like data, because it’s typed; email and IM are data, right? But SMS is in the paging channel, or the part that is used to ring the phone and send caller ID data. What does that mean for pricing, availability, and traffic management? Well, too much to go into here, but importantly different things than managing data services.

I have gone out of my way to take actual RF engineering classes. It’s pretty arduous, and I no longer remember how to calculate Walsh codes by hand, for example. But as it turns out, almost no one does. I was in class with guys who had EE degrees and had been working as radio techs for mobile operators for years, and they still didn’t know the history or how parts of the system outside their domain work.

Hence, I feel pretty good about boiling several thousand pages of lecture slides and books into this short appendix. Just understanding the basics can matter a lot to your everyday work.

## The Electromagnetic Spectrum

We’ll start with junior high physics, to make sure everyone is on the same page. Everything from light to radio to x-rays (and much more) is part of the electromagnetic spectrum. These various parts of it are named, and discussed as separate elements based on the way the radiation interacts with physical matter. Visible light excites electrons at a frequency convenient to biochemical processes, so there are rods and cones in our eyes that detect it. Radio collectively oscillates materials, like all the electrons in an antenna at the same time.

Think of the entire electromagnetic spectrum in the same way as the spectrum of visible light; there is a clear area that is “red” and a clear area that is “orange,” but also a space in between, parts of which could be considered “red-orange,” or red, or orange. Though the individual components are discussed as though they are separate components, they are also part of a continuum and certain interactions overlap quite strongly.

Everything on the electromagnetic spectrum has a frequency, wavelength, and power. Radio especially is very commonly discussed in these terms, as it influences range and the speed and capacity of the information carried.

Radio is generally considered to be the frequencies between 3 kHz and 300 GHz. That “collective oscillation” mentioned earlier means you can feed an RF frequency electrical signal into an antenna (of the right materials, size, and shape) and it will send waves through the air, radiating much like ripples in a pond. When another antenna (again, of the right configuration) gets struck by these waves, they vibrate the electrons in the antenna in such a way that it generates electrical signals, and the receiving electronics do their job. See Figure A-1.

![](images/36bbc7eb3d5001f0e6a0ea9cc278e22b347d7d2429fb9971148162ecd55a69b1.jpg)  
Figure A-1. The electromagnetic spectrum, with a detail of the radiofrequency spectrum, including the allocations of various services, within the United States as of 2003. As you can see, a lot of different services are vying for a limited amount of space. Key mobile frequencies and a few others are labeled. All others have been removed for clarity.

Frequencies are measured in Hertz, where 1 Hz is one “cycle” per second. Electrical power in the United States is delivered at 60 Hz. Mobile phones are much higher frequency, measured in megahertz (MHz) or gigahertz (GHz).

In general, longer wavelengths travel farther, and may go through and around objects. Very low frequencies have global ranges. High frequencies carry much more information, but cannot penetrate objects.

Certain frequencies are unavailable due to physical phenomena, such as cosmic rays and the sun. Frequencies are managed by national governments (in the United States, by the FCC), generally through international agreements. The spectrum is quite full of traffic now, such that adding any service requires disabling another one. The switch to digital television, for example, freed up quite a bit of useful bandwidth, just now coming into service for some next-generation mobile networks.

## History

I always start presentations about mobile telephony by getting a baseline of the audience. I ask when mobile telephony was first instituted, and where. Occasionally someone will refer to the DynaTac, and correctly insist it all started in the United States. Much to the derision of their youthful cohorts, who are sure it came about no earlier than 1985, in Japan or, for the very clever, Finland.

No one guesses that it emerged directly from experience with miniaturization of radios in World War II, and was first placed into service by the Bell system right after the war, in 1946. See Figure A-2.

![](images/9cc26be0d23b143db981c1207362519719272760a86a666ba014fabbbbf6e0da.jpg)  
Figure A-2. A contemporary illustration of the 1946 Bell MTS system in St. Louis. This was a quite complex installation for MTS. Due to the size of the surrounding areas, multiple receive antennas were installed, something not common with the first systems.

These first systems were based in relatively small areas, covering a single city, for example. A single radio antenna on a tall building downtown sent signals to a large radio in your car, and received signals from it. To dial a call, you had to get an operator to physically connect the call by dialing it on a switchboard, then plugging a patch cable between the mobile network and the wireline phone network.

These Mobile Telephone Systems were replaced starting in 1963 with an improved version, which added antennas for larger areas such as the St. Louis region shown in Figure A-2, and had some capacity for handoff between them, allowing larger range and lower power. Devices became smaller (though still installed, they were the size of a briefcase, not a trunk). The customer could even direct-dial calls straight from his car.

These were mostly replaced by 1995, but at least one IMTS network was operating in Canada until 2002. The long range of the individual towers (up to 25 miles) was an advantage in the specific locale.

But these were still not cellular devices.

## Legal and regulatory

Much of the behavior of these systems, and even how they work today, is tied up in regulatory requirements. The FCC allocates frequencies in the United States; other countries have their own bodies, but radio waves do not respect international borders, so they generally coordinate through an organization called the ITU.

The delay moving to IMTS, for example, was due entirely to the allocation of bandwidth to the mobile operators. The FCC denied anyone wanted or needed mobile phones, so it sat on the requests for more than 10 years.

Despite the name, mobile phones are not really phones. The wireline phone network is more precisely called the PSTN, or Public Switched Telephone Network. It is a single system that connects to (more or less) the entire globe. It also must generally provide a certain level of service, offering subsidies to the poor or disabled, for example. As usual, specifics vary by country.

Related to this is Quality of Service. This is not quality in the sense of resolution or clarity, but degree of service. For example, if the PSTN is totally jammed up—perhaps due to some disaster—when the fire department picks up their phone, someone else (you or I) is forcibly dropped to provide room. Gradations between this public safety override and general access, where you may pay for better access for your business, also exist.

Traditionally, there is no such equivalent practice in any private network, such as satellite or mobile telephony. In some countries, the devices must dial emergency services, and there is a small trend, starting in Scandinavia, to make mobile service and complete coverage a right of every citizen.

Additional regulations are as or more crucial to understanding how and why services work in a particular manner, or what you must do to comply with them. In the United States, location must be made available to emergency operators by offering GPS telemetry (this under the e911 mandates), but cannot be used for any other purpose for individuals under the age of 13 without quite specific consent rules. How do you enforce this, without overly burdensome rules?

Likewise, there are restrictions on how your personal data can be used to market to you, and how it can be sold. In the United States these are all consolidated under a concept of Customer Proprietary Network Information, which has more recently been used to ensure the security of your data as well. If you get phone service in the United States, you get a mailing at least once a year outlining your rights under CPNI, much like the privacy brochure you are given at the doctor’s office.

This all means that, aside from technical and moral limits, there are significant and generally well-enforced restrictions to what can be done with personal information, and is much the reason that it is difficult to get customer information from mobile operators. Understand local technology, markets, laws, and regulations.

## Early cellular

Although it seems no one could have foreseen the growth in mobile we are continuing to experience, there was a great deal of pent-up demand for more, more portable, and more flexible mobile telephony. After numerous delays, mostly due to regulatory approval, a new service was launched starting in 1983. The day this service launched, there were some 10,000 people on waiting lists for an IMTS device in New York City alone.

The Advanced Mobile Phone System, what we all call the “old analog system” today— once again, first launched in the United States—was a massive success, and was used in one guise or another throughout the world.

This was the first true cellular mobile network because it shared two key characteristics, both designed for efficiency at multiple levels:

• Handoff between base stations

• Frequency reuse

These allow much more traffic in the network, by a very simple frequency division multiplexing scheme. Although signals are still fixed to a channel, that channel uses a dedicated frequency range, and your call uses the whole channel, it is much narrower than in MTS, and is not fixed for the duration of the call. When you switch to another tower, the handoff may change the channel to suit the available space.

Aside from some cleverness with handoffs, and being over radio instead of wires, this was still very similar to the classic, wired PSTN. At any one moment there is a dedicated voice circuit. Replacing the analog voice carrier with a digital signal allows even more capacity, as well as reductions in power. This is what D-AMPS (D for digital) sought to do in an effort to extend their network life in the face of the next-generation networks.

D-AMPS encoded the voice (by adding a vocoder, which turns it into data), then chunks the data stream into “frames,” which are then sent in intervals, with a specific time slot for each user on the network in that cell.

This time-based system is called Time Division Multiple Access, or TDMA. Digital signals allow compression of the voice signal. Combined with very rapid time slice switching, the same frequency can be used for several users at once.

## Cells and backhaul

There are two fundamental components of a cellular network. The first is the most common, the handset (or aircard, or tablet, or eReader, or home modem, etc.). Operators also call this a terminal, or customer terminal, or use the old CPE terminology, for Customer Premises Equipment.

The other side of the equation is the cell site, which is actually a small complex of items. Although we all use the term as a shorthand, the tower is actually just the mast to which antennas are mounted. Wires run down this to a shed which houses transmitters, and often backup power such as generators. GPS antenna and other equipment are also included on the tower or in the shelter. The whole arrangement is more technically called a BTS, or Base Transceiver Station.

The antennas themselves are arranged around the top of the tower, in a flat ring of three (or sometimes four), grouped with two or three antennas pointing in each direction. The multiple antennas work together for power management and position finding, using math not worth getting into.

Whenever you see more than one stack of antennas on a tower, this is just because they lease to their competitors. This is a very profitable business alone, so competing operators rarely restrict one another from mounting antennas to their tower, at least for the right money.

![](images/205f3644c481f160d4612459f1cb7bea0422bfbc46736f997d8efb839834c1a4.jpg)  
Figure A-3. The arrangement of the antennas on a tower is very specific, and not just to cover more space, but integral to the way cellular mobile telephony works.

Each group of antennas pointing in a specific direction constitutes a sector (see Figure A-3). When you are on a call or using data services and you’re moving through the network, your handset stays connected by negotiating with the BTS to “hand off ” between cells and between sectors. When you run out of available coverage in your home network, you can even be handed off to a roaming network.

There are differences in the various types of handoff, but they are fairly unimportant for our purposes. Networks are generally voice-optimized still, so they spend a lot of time making sure calls are not interrupted during handoff. Data services often are interrupted, and this can have implications in terms of network-based services. Websites in particular can become confused and suddenly reset when they find you coming from a new IP range.

Handoff does require continuous coverage, so cells and sectors overlap. Your handset is, as you now might expect, communicating not just with the tower it’s getting voice and data from, but with all adjacent towers. They all work together to decide when to hand off to ensure maximum efficiency and prevent drops in coverage.

As discussed earlier, the mobile network must attach to the PSTN at some point. The first step is to connect the BTS to all other nearby BTSes in that operator’s network. Then they connect to a central office, and at various points interchange with the PSTN. The whole scheme of connecting the towers to one another and to the central office is called backhaul. This can severely limit the speed or capacity of the network, especially when not considered in the design of new radio technologies.

Last year I was on vacation in Door County, Iowa. It is a relatively remote peninsula, but we were able to get mostly decent mobile coverage (high signal strength, low noise). However, the data speeds were awful and it even sometimes took forever to connect a call. It turned out that the backhaul was all done by a microwave link, one tower to the next in a line down the peninsula. It was not able to handle the traffic load of tourist season, even though the individual towers easily could.

Backhaul is generally microwave, via yet another antenna on the tower, or cables in the ground. Some other radio technologies are used, and some have backups and so provide both. Central offices (which may be collocated with a BTS) sometimes have satellite links as a last-resort backup even, to offer service in the event the local PSTN fails.

## The 2G networks

Quite soon after AMPS took over the world, it became clear that mobile telephony was a big deal, and eventually the current networks simply wouldn’t be able to handle the load. Several schemes were put forward, and these all-new digital networks took over the mobile landscape by the late 1990s.

Since these were considered an upgrade to AMPS (et al.), or the second generation, they came to be called 2G networks. In the United States, the FCC codified the system under the moniker of Personal Communications Service, or PCS, which you could see appended to the name of several operators.

It also became clear that mobile telephony was a huge industry, and would only grow. This ended up changing the industry landscape, as it suddenly became very expensive to be a mobile operator. The reason is not strictly one of scale or technology, but of competition. As discussed already, national governments control the bandwidth in their borders. When a new type of network launches, it generally appears on an all-new band, so it can coexist with the older network and we can all take most of a decade to switch over.

To decide how to allocate this bandwidth to the various operators, there are auctions. Other portions are involved (you have to prove there’s a valid business plan and a market for the service, and agree to actually offer service), but basically the one with the most money wins. Many of the small or local operators simply could not compete in the face of big telecoms and consortia of smaller ones. In some countries, of course, the nationalized telecom simply assigned the rights to itself.

The 2G networks led to much more reliable, wide-reaching, and eventually data-driven mobile use. However, despite being able to be grouped as a class, they are not a single service like AMPS became. Instead, two competing network technologies emerged, and are still dominant in their follow-on versions.

## GSM

Although pretty much the entire United States and many other regions implemented AMPS with fairly good consistency, Europe suffered severe fragmentation, both by carrier and across international borders. This just extended the muddled, expensive system already in place, with toll calls (on a complex scale) being the norm even for much local service. For both technical and market pressures, by the mid 1980s it became clear that a common standard would be needed, and it should be built into a next-generation system.

GSM, or its follow-on variations, did meet much of the promise and is a global standard that a majority of handsets use. Many implementations are even seamlessly interoperable, so you can enjoy relatively global coverage with a single handset. Relatively, of course, is not “complete,” and Japan, for example, has no GSM coverage at all.

![](images/a9ab4297ec8174048de7041b00564287eb0a1f052fbf1fea1fb9bc8788caa515.jpg)  
Figure A-4. A summary of the network operations between a GSM handset and the BTS

A key feature of GSM is the Subscriber Identity Module, or SIM card (shown on the right in Figure A-4). The SIM is a smart card that carries the user’s subscription information and a phone book. Theoretically, the user can then just swap the SIM freely between handsets. Practically, there are a few different sizes, so some phones aren’t compatible with the card you own, the SIM is always older technology, so address book data is more limited than you want, and many operators just don’t let you swap cards. A practice called SIM locking means you cannot get the SIM to work in another device. This is for business reasons, when the operator underwrites the price of the handset, and makes you sign a contract. The freedom of the SIM violates this principle, so the operator might not get its money back. In some countries, consumer freedom laws prevent SIM locking.

GSM is an entirely digital standard, encoding the voice as a stream of data. This is then assigned to frames, which are sent out over specific timeslots, mixed in with all the other traffic on the network. At the other end, it is extracted from the frame, bolted to the rest of the stream, and then turned back into continuous voice. The time slices make this a TDMA or Time Division Multiple Access system. On each of the 124 frequency channels, 26 different conversations can be had. This is possible partly due to the efficiency of digital encoding; the coded traffic takes less time to encode, send, and decode than it does to say or hear, so it can be broken up into bits without you noticing the lag.

Additional parts of the network are dedicated to various traffic control functions, and to power management. Among the traffic control functions is a message section, originally just for network technicians to send short text phrases between the BTSes, then repurposed to let the handsets replace pagers. As you might have guessed, this is where SMS text messaging came from.

Despite all the voice traffic being digital, this does not mean early GSM supported data. The concept was still of delivering circuit-switched voice to the PSTN, so data essentially operated like a dial-up modem, and was inefficient.

## CDMA

The first thing most people notice about CDMA, when comparing it to GSM, is that it has no SIM. There is actually a similar part of the device that has the subscriber information, but it is not removable. When comparing to SIM-locked devices, though, this is an unimportant distinction.

Another key difference is that CDMA is less of a standard. There are several implementations of it, and even the standard ones detailed here (Figure A-5) can be made so that they are not interoperable with others. You generally cannot use your CDMA phone in any other country, and often it will not even work on a competing CDMA operator’s network in the same country.

![](images/7542a17d5728c97b72a1907707ddf16c1ee0ca5b011a1bf402bc243652aa4669.jpg)  
Figure A-5. A summary of the network operations between a CDMA (IS-95) handset and the BTS.

Another interesting feature is that the underlying technology is covered by a handful of very specific patents, and the result has been that a company called QUALCOMM effectively owns the technology. Instead of (for the most part) literally licensing, it simply retains the right to provide essentially all the chipsets that run these devices. It has parlayed this into being among the largest mobile chipset suppliers for all types of networks, worldwide. A surprising amount of what mobile telephony can do, and will do in the future, is at the whim of a single company.

CDMA uses the name of the underlying technology, Code Division Multiple Access. Voice is again encoded digitally, but this time the encoding itself is part of the message scheme. The voice signal is encoded in such a way that when sent over the air it is mixed willy-nilly with the bits from every other conversation or bit of data on the same frequency. At the other end, a code is used to extract each conversation individually from the pool of random-looking data.

This scheme is much more secure, and ends up being faster and more efficient. Although the original implementation did not directly support data, the underpinnings were better able to support it, so CDMA-based networks have gained some dominance with the move to data networks in 2.5 and 3G.

As with GSM, other portions of the signal are used for traffic control measures, power control, and signaling. Although not originally implemented in the same way, a paging-like one-way text sending system evolved to be 100% compatible with SMS text messaging.

## Other Networks and Concepts

These are the two largest basic network technologies, but others do exist. PDC is a network used almost exclusively in Japan, and nowhere else. Many others who create taxonomies of mobile history consider D-AMPS to be a 2G network, due to it being a digital service (I don’t, because it seemed like a half-measure at the time and in retrospect more so, as it was a dead end).

Both of the ubiquitous mobile technologies have benefits and risks or limitations. Many of the downsides are not inherent, and get fixed in later implementations.

The key features that mobile networks are evaluated on tend to be:

## Cost

This includes the density of the networks, and the ability to reuse existing towers, antennas, switchgear, and backhaul.

## Efficiency

This is mostly about compression and reuse of assets. You never want unused frames or channels.

## Capacity

As many handsets as possible must be able to be connected to a particular tower. Capacity regularly doubles, or more, when a new generation is released. There seems to be no end to network tricks.

## Reliability

If the network gets to its rated capacity, it had better be able to continue functioning, and have some overhead where it can function at degraded call quality. Drops and blocks must be kept to a minimum, and the tower must never, ever simply crash so that it is off the network entirely.

## Interference

This has largely been cracked, but it is still waiting in the sidelines. Interference from other radios and from obstacles must be tolerated or worked around, and the mobile signal must not interfere with other radios.

## Power

This includes both total radiated power and power management. Modern mobiles use single-digit milliwatts of power when connected correctly, and this continues to go down all the time. The less power, the less the tower needs, and the more that any battery on the handset needs to use for radios (and more for big screens and other features). Poor power management means the handset sends out higher-power signals trying to get a good signal.

Much of this is about the costs associated with the network. It costs billions just to own the rights to the network (those auctions), and billions more to build a network. A nationalscale operator can spend a billion US dollars every year on network maintenance and improvements.

## 2.5 and 3G

Without getting into too much detail, third-generation networks (or 3G) are directly descended from 2G. They retain the basic underpinnings of the technology (TDMA versus CDMA) and much of the general layout of control and network configuration, but can also naturally handle data, by turning some traffic channels into packet data channels.

Naturally, a change to the network architecture also means other parts were changed, and the networks use even less power, manage power and interference better, and offer markedly increased capacity.

The 3G networks had to meet certain requirements by international certifying bodies, especially those of data transmission speeds and capacity. The “2.5G” networks are simply steppingstones, which were so different from 2G that they were worth mentioning, but not yet good enough to be “3G.” This is, however, an insider’s term. Consumers didn’t mostly get told all this, and thus began the marketing of network specs, and a set of lies. Many 2.5G networks were marketed at the time as 3G. The same is happening with 4G today; although good WiMax and LTE networks are active, none are really 4G-certified yet.

## Future networks

To a certain degree, the future is already here. It is just, to borrow a phrase, unevenly distributed. And for that largest of mass markets, mobile telephony, that means everything can still change. LTE and WiMax networks certainly point the way, but it is still hard to tell which will be most dominant, if either of them, and what features will actually make it to devices when they are more broadly adopted.

As far as networks in general, one clear trend is to data-only operation. This is far past simply encoding voice traffic for efficiency. The expectation of more and more pure data services, the possibility of using any traffic channel for any type of traffic, and other efficiencies mean that VoIP will replace dedicated voice channels, and data networks will rule in the future. This requires all-new networks, not just updates, partly so that things such as data handoff happen seamlessly. Without this, voice service (still by orders of magnitude the largest communications method on mobile networks) will suffer a severe degradation, and operators will not be able to sell their customers on the changeover.

This theoretically means any data connection could be used as well, such as ad hoc WiFi networks. People who use services such as Skype can tell you there is no overwhelming technical impediment to this today. However, they also can tell you it isn’t really business class, or grandmother-proof. Aside from this reliability, the whole model of operating a mobile network makes this unlikely in the foreseeable future; operators want to retain more complete control, for revenue, perceptions of trust, and customer support purposes.

However, if there is anything I have learned from my time in the industry, it is not to predict anything. No specific network technology is clearly going to win out. Whatever does emerge will probably be used in a way that is somewhat different from how it was conceived, and by the time it is in widespread service, the replacement will be well on its way to market.

## An Introduction to Location Technologies

Appropriate use of sensors is one of the key methods to make mobile devices behave in a useful, intelligent manner. Most of these are fairly easy to comprehend. A camera is a camera, and even accelerometers are understandable in a general sense with only minimal exposure.

Location services, however, are very complex due to their scale, the opacity of the operation, and poor choices in marketing communications. The most important thing for understanding location technology on mobile devices is to never, ever, ever conflate “GPS” with “location.” We discussed the numerous technologies briefly in the Location pattern. Longer descriptions of the same are provided in this appendix.

The following are key guidelines to keep in mind when designing location services on mobile devices:

• Every phone is location-enabled. GPS or not, working or not, there’s some location available as long as it is attached to the network. If your service offers up a weather report or local news, a few thousand yards is practically pinpoint precision.

• All the available location technologies must be addressed when designing your application or service. Don’t disable the whole service, even if it’s about something that seems to require precision such as mapping, just because the GPS is off.

• Precision and accuracy must be understood by designers, and correctly exploited by the product. When the GPS is off, or doing badly, show the CEP circle so that it’s clear that we don’t know “exactly’’ where you are. Admit the same lack of precision in text; say “Turn right in ‘about’ one-quarter of a mile,” and so on.

• If you work for a carrier, exploiting the network like this should be a snap. If not, your devices or software may or may not be able to talk to the phone enough, and you might need to negotiate with the carrier or find a third-party provider. There are providers of location services that have already set up agreements with the operators.

• Consider what to store locally. Does the handset really need to be on the network, or should you give some functionality when the connection is bad or unavailable?

• Look useful without acting creepy. And don’t just follow the letter of the law. Be careful with your user’s data, share only what is needed, and store only what you really have to. Often, these last two are answered as “nothing.” If that is the decision, make sure it’s implemented as such, and no one gets lazy with the development or doesn’t get the memo. Don’t keep location information that is not relevant anymore, and be sure to encode information that has to be stored. Presence is considered personal information, so it will be perceived as a breach of confidence, even if not a breach of law.

## Location Technologies

As we have already mentioned, GPS is not the only location technology available. A whole series of them are employed, and work together to give a sense of location to any device. Whenever possible, these technologies are listed from least to most precise.

## Cell

Mobile telephony is based on communications and handoff between cells, each of which is (generally) controlled by a single base station, generally on a tower with multiple antennas. The entire assemblage of tower, antennas, transmitters, shed to house it in, and so on is called a Base Transceiver Station or BTS.

The tower location is well known, and its ID is attached to the call data record (used for billing and network control purposes), so it can be used by certain systems.

This is excellent as a fallback, when other things are not available. Better technologies are generally not available when roaming, and the data is not or cannot (due to technology or politics) be shared at more precision with your home network or because you are from another operator.

Precision will vary widely by the size of the cell, and there is no (good, universally accepted) method to determine and communicate precision and accuracy to the handset or any systems that use it. A good rule of thumb—and something similar is generally used by devices—is to assume the device falls within a circle 3,000 yards (m) across, though this varies by the technology used.

## Sector

Recall that each tower has multiple antennas. Those three antennas (or four, depending on the technology and carrier implementation) point in different directions to cover an entire circle. Each of those is an independent mobile radio sector. Just like signals are handed off between cells, they are handed off between sectors, and the data is generally known to the handset and can sometimes be shared with services or providers. However, since the direction the sector faces is really only known to the company that installed it, and the network operator, they are the only ones that can use the data well.

Precision will vary widely by the size of the cell, the antennas used, the number on the cell, the down-angle, and so on. There are some semi-useful ways to determine precision and accuracy for a single read, but they are not universally implemented and there is no way to send the data to the information providers (e.g., the map program). A good rule of thumb—and something similar is generally used by devices—is a circle 1,200 yards (m) across, collocated with the radio centroid of the sector (which can be determined from maps and some educated guesswork; others have already done this). Yes, sectors are not circles, but it’s also hard to communicate shape and orientation, so this works.

## Triangulation

Generally, triangulation is the practice of determining the location of a point by measuring the angle and/or distance from several known locations. More points give more precision. It can get more complex when you try to find points in 3D space, but all mobile triangulation systems mostly assume the Earth is locally perfectly flat, and simply find the location on the geoid. Methods of triangulating get really complex and vary by network type and equipment available; multilateration and signal interpolation are some of those. The math can get pretty harrowing.

Precision varies mostly by the number of sectors being used, the distance between them, and other variables of the network. There may be a method of communicating to services employing it an approximation of the precision available. In any remotely built-up area, where it most often has enough sectors to work, a circle 50 yards (m) across is typical; 12 yard precision is possible, with good accuracy.

## GPS telemetry

The Global Positioning System is a GNSS (Global Navigation Satellite System) consisting of a ground-based control system, a series of satellites, and any number of anonymous receivers. So, reading that alone dismisses many misconceptions; it’s one-way, it’s a system, and the signal is from satellites and has nothing to do with mobile networks.

Telemetry means data sent from a remote (usually mobile) site such as a rocket, back to base. Here it means the device figures out where it is by listening to the satellites, then tells the network or website or whatever where it is.

GPS can yield precision to fractions of an inch at least. But those are large, complex devices used for special surveying and scientific tasks, and require the antenna to be fixed to the ground for a period of time, and then rotated for reasons not worth getting into here. Portable, handheld receivers like those in mobile handsets can generally be assumed to give precision of 20 to 50 feet, though antenna and signal processing improves constantly and precision can be in single-digit feet.

Selective availability is the capability of the US government to partly or entirely disable the commercial GPS network so that enemy forces cannot use the system. Military receivers are functionally identical, but use a special, coded signal instead. In practice, this is unlikely to ever take place outside of a global catastrophe in which you won’t much care about GPS anyway.

However, it exemplifies the theoretical risk of a major system being held by a single country. Therefore, there are other national and regional GNSSes, including Galileo, GLONASS, and COMPASS as well. None of these are really fully active, and there are few or no receivers in mobiles as yet. In theory, eventually, using multiple unrelated systems will give better accuracy yet, and give better coverage when in touchy situations like in dense cities.

## WAAS

GPS uses radios, and the atmosphere and Earth are imperfect and can displace or distort the signals. WAAS is a satellite-based augmentation system based in North America (others exist in the rest of the world, but are less well established) that sends additional signals via another set of satellites to allow GPS receivers to adjust for those inaccuracies. I know of no mobile phones that have a built-in WAAS receiver, but it’s a location technology that does exist, is almost universally used on every dedicated GPS device, and is employed on BTSes using AGPS.

## AGPS

Assisted GPS requires the use of mobile networks, so it only works when in data communication range. The BTS has its own GPS receiver (which many already have in order to get precise time signals), and usually a WAAS receiver. AGPS provides a bit more precision, assures it of more accuracy, but mostly helps speed up cold or warm starts.

Briefly, for a GPS to work, the receiver has to download data about all the satellites before it can calculate the position. AGPS caches this info for the phone, and sends over just the relevant bits, cutting minutes to a second or two.

This is a reason you may not see WAAS, and might see some benefits from another GNSS (say, GLONASS) before the receivers are added to the handsets. AGPS generally gives precision, even in dense areas and on the move, of 10 feet or better. Two-foot indicated precision has been observed.

AGPS is not generally selectable as a separate service; when the user chooses to turn on or off “GPS” and has a network connection (and an AGPS-compliant phone, etc.), he gets the advantages of AGPS if it is available on the network and BTS. You can often see this at work, as your location will be almost perfect when in a home network, but suddenly be worse when traveling. Check, and you will probably be roaming, and therefore incapable of communicating with the AGPS features of the roaming network BTS.

## WLANs and PANs

Local networks such as WiFi and Bluetooth are not exactly more precise, but are at the bottom of this list because they are local, and can add another layer of location, so they could increase precision. They can also be used instead of other technologies when there is no GPS signal or a bad mobile signal in which triangulation cannot be used.

Both of these currently use the “cell” (or network identifier) and triangulation methods described earlier, but with their transmitters. There are no sectors, and no universally adopted AGPS to work with device telemetry. Naturally, a handset getting good GPS data can send that telemetry to anyone over any network, including WiFi, but that’s not the same thing.

They are both relatively rarer, and often are supported by third-party software or individual services (which may have specific capabilities), and are not universally implemented on the handset. There are no reliable, independently verified numbers on the real-world precision, but tests of WiFi triangulation alone have gone down to inches. On the other hand, poor network identification has led to placing users on the wrong continent. There’s room to improve here.

## Ask

People often know where they are. If you cannot get any location, or there’s a reason your users might want to override it (even as simple as the data is bad), let them enter a location. Never override user-entered data—at least not without providing a warning.

If you do this, allow lots of methods and think about what the user knows, and is comfortable with. Do not require a street address unless it is really needed. Do not use simple entries such as a zip (or postal) code, if the user is unlikely to know it, such as when traveling.

## Key Topics in Implementing Location Services

## Location is not just GPS

All of the above is pretty well known by network engineers, chip makers, and various low-level handset software designers. But it is often missed a bit by various software implementations (and certainly by marketing). All too often GPS “is’’ navigation, such that turning it off kills all location services. Certain systems are becoming aware of this, and (for example) just give poorer precision when you turn the GPS off, but they do allow location services to work.

## Vertical accuracy

Vertical location is not known with many systems, and is much worse than the horizontal accuracy even with GPS/AGPS. Consider this in your design if users in buildings or even just multilevel roadways are likely to be encountered. Technology may not reveal the vertical position with sufficient fidelity for the system to respond usefully. But if you can derive vertical location, start thinking about using it. A person 120 feet off the ground does not want a coupon for the Starbucks across the street; he’s probably in a meeting or at his desk in a building. Eventually, map data should account for this, and even simple, obvious things like multilevel roadway navigation will also become easier.

## Precision versus accuracy

Precision and accuracy are often confused. A quick primer: precision is the number of decimal places you measure something to; accuracy is how correct it is. The less accurate a measurement is, the less precisely it should be reported. Practically every location system gives location to the same degree of precision (e.g., 1 meter, using full UTM precision) at all times, and presumes the accuracy measure will be considered as well.

Visual representations are similar. The moving arrow (or car, or person icon) is the centroid of the current location precision circle. Even when that accuracy circle is displayed, the centroid marker implies much higher precision than is actually being achieved. Consider better ways to represent location to avoid user confusion.

## Appropriateness of information

Display of information services should be related to the current accuracy. For example, turn-by-turn directions always assume perfect location precision (using the centroid of the current location accuracy circle), and say “You have arrived” instead of “It’s the big, white building on the north side of the street.” What if the location is vague and the target or turn is 30 yards behind you, or 50 yards in front of you? The user is confused. Close roads (in dense cities), multitier highways, and other situations can exacerbate the effect of this behavior.

Design to accommodate imperfect location instead.

## Data integrity and reliability

If your map might be wrong, or imprecise or inaccurate (and they all might be), you should think about this when planning the interaction. Don’t assume your data is perfect, and give contextually helpful information. Let users note problems, and do something with the problem reports.

## Local versus network storage

Handheld dedicated GPS units and most in-car units store map data locally, so when a GPS fix is found, a map can be displayed immediately. Mobiles generally assume functionality only when on the network, even when a GPS is included. If your service is usable when out of network range (e.g., it’s just for navigation, not for social media or communications), consider storing or caching enough information locally for the device to work when out of network coverage.