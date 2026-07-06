# Make it public / Make it bigger / Make it context-agnostic / Make it contextual / Make it last / Go forth and be atomic

> Section: bibliography | Source: 05-Result-MD\03-Design-History-replenish-1\02-Books\Brad Frost：《Atomic Design》\Brad Frost：《Atomic Design》\Brad Frost：《Atomic Design》\auto\Brad Frost：《Atomic Design》.md

## Make it public

Communicating change, evangelizing, and setting up proper training and support are all great things to increase your system’s visibility. But there’s another big opportunity to take your communication strategy to another level: making your style guide publicly accessible.

Why? Isn’t a style guide merely an internal resource to help people in your organization work better together? What use is it to the outside world? And wouldn’t publishing your style guide give away all your trade secrets?

Publishing your style guide for the world to see increases its visibility, increases accountability, and serves as an amazing recruitment tool.

Putting your style guide behind a login or frewall reduces visibility and adds an unnecessary burden to your team and partners, which limits the resource’s efectiveness and potential. And the fears about giving away your trade secrets are completely unfounded. These are UI patterns, not nuclear codes.

![](images/1f90cb9ed872396a31c361e7ab80a271d5e3f4704abc8f596a21712881265d3e.jpg)  
Styleguides.io rounds up over 150 public-facing style guides from organizations across the world.

In addition to making important documentation easier to access, a public style guide helps create organizational accountability. Publishing your style guide demonstrates your organization’s commitment to the design system, which creates a helpful bit of pressure to keep it an up-to-date and useful resource.

Public-facing style guides are also hugely helpful for recruiting. Designers, developers, and people working in other disciplines want to work for organizations that embrace modern digital best practices, and (as we’ve discussed throughout this book) design systems are quickly becoming an industry-wide best practice. Publishing your style guide sends out a strong Bat-Signal that can attract passionate, pattern-minded people. For instance, style guide expert Jina Bolton went to work at Salesforce after seeing the company’s style guide for their Salesforce1 product.

When I saw [Salesforce’s style guide] I thought it was beautiful and it’s why I wanted to join this team.

\- Jina Bolton

Since joining Salesforce, she’s helped create the ultra-successful Lightning Design System and helps manage their growing design system team. Jina’s story is not an isolated one; almost every guest Anna Debenham and I interviewed on the Styleguides Podcast discussed how helpful their public-facing pattern library was for attracting talent. All that means your public style guide makes your organization more competitive, not less.

## Make it bigger

A visible, cross-disciplinary, approachable pattern library is one that your team will come back to again and again. Use that to your advantage. Since the team’s eyeballs are already fxated on that one resource, there’s a big opportunity to extend it to include other helpful documentation like the voice and tone, brand, code, design principles and writing guidelines we discussed in chapter 1.

![](images/00b450e27fde7b98388d75951be20d914894cc46e7f70cf269c4e2721ce61d4d.jpg)

Intuit’s Harmony design system includes a pattern library, design principles, voice and tone, marketing guidelines, and more. Housing this helpful documentation under one roof helps increase its visibility and efectiveness.

Now, your organization may not need to implement every favor of style guide out there, but the point is that creating a centralized style guide hub builds more awareness of best practices, increasing the documentation’s efectiveness.

Another way to extend the functionality of the pattern library is to include guidelines for native platform patterns alongside web-based patterns. We can look to Intuit’s Harmony design system once again for an example of how native mobile platform patterns for iOS and Android can live beside their web-based counterparts.

![](images/92c50f0e73af7c0295fffe64c46d9b16c1fe5880e765df93e1d549eeb6f9515b.jpg)  
Intuit’s Harmony pattern library includes buttons to switch between web, iOS, and Android for each pattern. This allows the team to maintain a mostly consistent design system across platforms but also document pattern divergences when they occur.

## Make it context-agnostic

The way your UI patterns are named will undoubtedly shape how they are used. The more agnostic pattern names are, the more versatile and reusable they become.

Because we tend to establish UI patterns in the context of a broader page, it can be tempting to name components based on where they live. But rather than naming your component “homepage carousel” (forgive my morbid obsession with carousels), you can simply call it “carousel,” which means you can now put carousels everywhere! (But for the love of all that is holy, please don’t.)

Another challenge for naming display patterns is that we tend to get distracted by the content patterns that live inside them. For instance, if working on an e-commerce site, you may be tempted to call a block containing a product image and title a “product card.”

But naming things in this manner immediately limits what type of content can live inside it. By naming the pattern simply “card,” you can put all sorts of content patterns inside it: products, promotions, store locations, and so on.

Fair warning: naming things is really freaking hard. But there are strategies to help you create robust names for your patterns. Conducting an interface inventory (as detailed in chapter 4) helps remove patterns from the context of the page where they normally reside, meaning your team can create names that aren’t distracted by their context. I’ve conducted naming exercises with teams where we’ve blurred out the content residing inside a pattern so everyone can focus on the pattern’s structure rather than the content that lives inside it.

![](images/ac3743f56280e4aafd471072fe03cc1e4a3f8b759142f4d8652284b87e6f9aa1.jpg)  
A good exercise when naming patterns is to blur out the content so your names refect the patterns structures rather than the content living inside them.

While naming things will always be a challenge, pattern names that are agnostic to context and content will be more portable, reusable, and versatile.

## Make it contextual

Showcasing UI patterns in a pattern library is all well and good, but you need to demonstrate context for design system users to understand how and where to properly use them. Most pattern libraries show a demo of each UI pattern, but as we’ve discussed, those patterns don’t live in a vacuum. Where exactly are these patterns used?

One way to demonstrate context might include showing screenshots or videos of a component in action. Material design’s documentation does a fantastic job at this; each component is rich with photos, videos, and usage details to give users a clear understanding of what these patterns look like in the context of an application, and demonstrate how each pattern should be used.

![](images/3577bb17640150909972592303563e36080ce0d57b55619127015c7c3c625dfb.jpg)  
Material design’s component library doesn’t just contain an example of each component; it thoroughly documents the component’s usage with plenty of images and videos to support it.

Another way to show context is to provide lineage information for each pattern. As we discussed in Chapter 3, a tool like Pattern Lab automatically generates this information, letting you see which patterns make up any given component in addition to showing where each component is employed. This provides a sort of pattern paper trail that helps immensely with QA eforts, as it highlights exactly which patterns and templates would need to be tested if changes were made to a particular pattern.

![](images/a6c37acdb260935d0df99fab39e1c58c6f6cd618605a3819cfae876faa73f4cd.jpg)  
Tools like Pattern Lab provide lineage information, allowing teams to see which smaller components are included in any given component, as well as where each pattern gets used.

## Make it last

Making a design system is an incredibly and important endeavor. But without proper maintenance, the value of your design system will depreciate much like a car that’s just been driven of the dealer’s lot. Instead, your design system should be like a bottle of fne wine that increases in value over time.

![](images/e4c112cf44025a3da8ec29c176de82323477b6367ec17adc39d1d7d8b0cc39fe.jpg)  
With proper maintenance, your design system should increase in value over time like a bottle of fne wine, rather than a used car that’s just been driven of the lot. Image credit: Sabin Paul Croce on Flickr and Ray Larabie on Flickr

As we’ve discussed throughout this chapter, making your design system stand the test of time requires a signifcant amount of time and efort. But isn’t that the case with all living things? Animals need to eat, and plants need water and sunlight in order to survive. Creating a living design system means giving it attention and care in order for it to continue to thrive.

All that efort not only creates a better present for your organization, but sets you up for long-term success. Establishing a clear governance plan, communicating change, and implementing the other advice found in this chapter helps the design system take root and become an integral part of your organization’s workfow. Creating the damn thing in the frst place is the hard part, but once established, you have a solid foundation with which to build on for years to come. Even if you were to burn everything down and rebuild a new system from the ground up, you’ll fnd your UIs will still need buttons, form felds, tabs, and other existing components. And you’ll need a happy home to display and document the system. Don’t throw the baby out with the bathwater!

So there you have it. To make a maintainable design system, you should:

ɕ Make it ofcial by allocating real time, money, and resources to your design system.

ɕ Make it adaptable by counting on change and establishing a clear governance plan.

Make it maintainable by seeking the holy grail and making it easy to deploy and communicate changes to the design system.

ɕ Make it cross-disciplinary by making your pattern library a watering hole the entire organization can gather around.

ɕ Make it approachable by making an attractive, easy-to-use style guide with helpful accompanying documentation.

ɕ Make it visible by communicating change, evangelizing the design system, and making it public.

ɕ Make it bigger by including brand, voice and tone, code, design principles, and writing guidelines.

ɕ Make it agnostic by naming patterns according to their structure rather than their context or content.

ɕ Make it contextual by demonstrating what patterns make up a particular pattern and showing where each pattern is used.

ɕ Make it last by laying a solid foundation with which to build on for years to come.

## Go forth and be atomic

We’re tasked with making a whole slew of products, sites, and applications work and look great across a dizzying array of diferent devices, screen sizes, form factors, and environments. I hope that the concepts covered in this book give you solid ground to stand on as you bravely tackle this increasingly diverse digital landscape. By creating design systems, being deliberate in how you construct user interfaces, establishing a collaborative and pattern-driven workfow, and setting up processes to successfully maintain your design system, I hope you and your team can create great things together. Go forth and be atomic!

