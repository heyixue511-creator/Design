# Chapter 2 Atomic Design Methodology

Atoms, molecules, organisms, templates, and pages

My search for a methodology to craft interface design systems led me to look for inspiration in other felds and industries. Given this amazingly complex world we’ve created, it seemed only natural that other felds would have tackled similar problems we could learn from and appropriate. As it turns out, loads of other felds such as industrial design and architecture have developed smart modular systems for manufacturing immensely complex objects like airplanes, ships, and skyscrapers.

But my original explorations kept creeping back to the natural world, which triggered memories of sitting at a rickety desk in my high school’s chemistry lab.

## Taking cues from chemistry

My high school chemistry class was taught by a no-nonsense Vietnam vet with an extraordinarily impressive mustache. Mr. Rae’s class had a reputation for being one of the hardest classes in school, largely because of an assignment that required students to balance hundreds upon hundreds of chemical equations contained in a massive worksheet.

If you’re like me, you may need a bit of a refresher to recall what a chemical equation looks like, so here you go:

![](images/3fe7cbb30f8205b9f221faeb0e22c98f5948814b5e2525e5f0264f739cd7dbfb.jpg)

$$
2 H _ { 2 } + O _ { 2 }  2 H _ { 2 } O
$$

An example of a chemical equation showing hydrogen and oxygen atoms combining together to form a water molecule.

Chemical reactions are represented by chemical equations, which often show how atomic elements combine together to form molecules. In the example above, we see how hydrogen and oxygen combine together to form water molecules.

In the natural world, atomic elements combine together to form molecules. These molecules can combine further to form relatively complex organisms. To expound a bit further:

Atoms are the basic building blocks of all matter. Each chemical element has distinct properties, and they can’t be broken down further without losing their meaning. (Yes, it’s true atoms are composed of even smaller bits like protons, electrons, and neutrons, but atoms are the smallest functional unit.)

Molecules are groups of two or more atoms held together by chemical bonds. These combinations of atoms take on their own unique properties, and become more tangible and operational than atoms.

Organisms are assemblies of molecules functioning together as a unit. These relatively complex structures can range from single-celled organisms all the way up to incredibly sophisticated organisms like human beings.

Of course, I’m simplifying the incredibly rich composition of the universe, but the basic gist remains: atoms combine together to form molecules, which further combine to form organisms. This atomic theory means that all matter in the known universe can be broken down into a fnite set of atomic elements:

![](images/51bbee2f44567ca576ed298a3243d74f1f232b66309216f5425c8e1ae889ed00.jpg)  
The periodic table of chemical elements.

Apparently Mr. Rae’s strategy of having students mind-numbingly balance tons of chemical equations worked, because I’m coming back to it all these years later for inspiration on how to approach interface design.

## The atomic design methodology

By now you may be wondering why we’re talking about atomic theory, and maybe you’re even a bit angry at me for forcing you to relive memories of high school chemistry class. But this is going somewhere, I promise.

We discussed earlier how all matter in the universe can be broken down into a fnite set of atomic elements. As it happens, our interfaces can be broken down into a similar fnite set of elements. Josh Duck’s Periodic Table of HTML Elements beautifully articulates how all of our websites, apps, intranets, hoobadyboops, and whatevers are all composed of the same HTML elements.

![](images/676c69f84dd89b987cc363871977e9cffb450aedb171db3ae7a95b1682f00932.jpg)  
The periodic table of HTML elements by Josh Duck.

Because we’re starting with a similar fnite set of building blocks, we can apply that same process that happens in the natural world to design and develop our user interfaces.

Enter atomic design.

Atomic design is a methodology composed of fve distinct stages working together to create interface design systems in a more deliberate and hierarchical manner. The fve stages of atomic design are:

1. Atoms

2. Molecules

3. Organisms

4. Templates

5. Pages

![](images/9bc025bb438830a8a30dd3ce89936b4a715144d422cf1a6319a51d47ab3623b4.jpg)

Atomic design is atoms, molecules, organisms, templates, and pages concurrently working together to create efective interface design systems.

Atomic design is not a linear process, but rather a mental model to help us think of our user interfaces as both a cohesive whole and a collection of parts at the same time. Each of the fve stages plays a key role in the hierarchy of our interface design systems. Let’s dive into each stage in a bit more detail.

## Atoms

![](images/cf77e76a642ab541c9d2640ac7212376499e7391d980a8bc02791970b9af290b.jpg)

If atoms are the basic building blocks of matter, then the atoms of our interfaces serve as the foundational building blocks that comprise all our user interfaces. These atoms include basic HTML elements like form labels, inputs, buttons, and others that can’t be broken down any further without ceasing to be functional.

![](images/c7108cd7a4947dc45930a2d4efcd8658134db07c1db46a25a3bf70935ddbe7d4.jpg)  
Atoms include basic HTML tags like inputs, labels, and buttons.

Each atom in the natural world has its own unique properties. A hydrogen atom contains one electron, while a helium atom contains two. These intrinsic chemical properties have profound efects on their application (for example, the Hindenburg explosion was so catastrophic because the airship was flled with extremely fammable hydrogen gas versus inert helium gas). In the same

manner, each interface atom has its own unique properties, such as the dimensions of a hero image, or the font size of a primary heading. These innate properties infuence how each atom should be applied to the broader user interface system.

In the context of a pattern library, atoms demonstrate all your base styles at a glance, which can be a helpful reference to keep coming back to as you develop and maintain your design system. But like atoms in the natural world, interface atoms don’t exist in a vacuum and only really come to life with application.

## Molecules

![](images/224a5809ac4cde1d4c492ca8e565a6acc887002605b8c3eede67ba7d462d6554.jpg)

In chemistry, molecules are groups of atoms bonded together that take on distinct new properties. For instance, water molecules and hydrogen peroxide molecules have their own unique properties and behave quite diferently, even though they’re made up of the same atomic elements (hydrogen and oxygen).

In interfaces, molecules are relatively simple groups of UI elements functioning together as a unit. For example, a form label, search input, and button can join together to create a search form molecule.

![](images/9deb94c6c5772ac270c17bb8a9e520c5ede0aa23b37339bd340918b5f929d917.jpg)  
A search form molecule is composed of a label atom, input atom, and button atom.

When combined, these abstract atoms suddenly have purpose. The label atom now defnes the input atom. Clicking the button atom now submits the form. The result is a simple, portable, reusable component that can be dropped in anywhere search functionality is needed.

Now, assembling elements into simple functioning groups is something we’ve always done to construct user interfaces. But dedicating a stage in the atomic design methodology to these relatively simple components afords us a few key insights.

Creating simple components helps UI designers and developers adhere to the single responsibility principle, an age-old computer science precept that encourages a “do one thing and do it well” mentality. Burdening a single pattern with too much complexity makes software unwieldy. Therefore, creating simple UI molecules makes testing easier, encourages reusability, and promotes consistency throughout the interface.

Now we have simple, functional, reusable components that we can put into a broader context. Enter organisms!

![](images/c72eb4d033037027bc749437b8e41156081635ee36604b3de3b02102bf2ad22d.jpg)

Organisms are relatively complex UI components composed of groups of molecules and/or atoms and/or other organisms. These organisms form distinct sections of an interface.

Let’s revisit our search form molecule. A search form can often be found in the header of many web experiences, so let’s put that search form molecule into the context of a header organism.

![](images/ca85f0d34cef2a0f771ce858aec843075fa24bcbe4817cbef2e538d36333a36e.jpg)

Home About Blog Contact

![](images/252c5a9813a140d4cfa078d045a5fc5e42464b3b2de572a94bd08277937fa180.jpg)

This header organism is composed of a search form molecule, logo atom, and primary navigation molecule.

The header forms a standalone section of an interface, even though it contains several smaller pieces of interface with their own unique properties and functionality.

Organisms can consist of similar or diferent molecule types. A header organism might consist of dissimilar elements such as a logo image, primary navigation list, and search form. We see these types of organisms on almost every website we visit.

![](images/d353d35846d51c8d304ae62320f95b974f26f629674147f056cb23bc3a023f64.jpg)  
Organisms like website headers consist of smaller molecules like primary navigation, search forms, utility navigation, and logos.

While some organisms might consist of diferent types of molecules, other organisms might consist of the same molecule repeated over and over again. For instance, visit a category page of almost any e-commerce website and you’ll see a listing of products displayed in some form of grid.

Building up from molecules to more elaborate organisms provides designers and developers with an important sense of context. Organisms demonstrate those smaller, simpler components in action and serve as distinct patterns that can be used again and again. The product grid organism can be employed anywhere a group of products needs to be displayed, from category listings to search results to related products.

Now that we have organisms defned in our design system, we can break our chemistry analogy and apply all these components to something that resembles a web page!

![](images/e8dfa75c3560ec32fbfac4f588dc1cfc1af9191eb3f0965531fe6d213672cf59.jpg)  
A product grid organism on Gap’s e-commerce website consists of the same product item molecule repeated again and again.

## Templates

![](images/d87833ddec534ca147e3597e324fe3b6e3e803397b8d923478891664836724da.jpg)

Now, friends, it’s time to say goodbye to our chemistry analogy. The language of atoms, molecules, and organisms carries with it a helpful hierarchy for us to deliberately construct the components of our design systems. But ultimately we must step into language that is more appropriate for our fnal output and makes more sense to our clients, bosses, and colleagues. Trying to carry the chemistry analogy too far might confuse your stakeholders and cause them to think you’re a bit crazy. Trust me.

Templates are page-level objects that place components into a layout and articulate the design’s underlying content structure. To build on our previous example, we can take the header organism and apply it to a homepage template.

![](images/dc61bf1933d68dbb8e0cc37b88b12375036b6d2fdd1c88c4cf3b03fabb4559c7.jpg)  
The homepage template consists of organisms and molecules applied to a layout.

This homepage template displays all the necessary page components functioning together, which provides context for these relatively abstract molecules and organisms. When crafting an efective design system, it’s critical to demonstrate how components look and function together in the context of a layout to prove the parts add up to a well-functioning whole. We’ll discuss this more in a bit.

Another important characteristic of templates is that they focus on the page’s underlying content structure rather than the page’s fnal content. Design systems must account for the dynamic nature of content, so it’s very helpful to articulate important properties of components like image sizes and character lengths for headings and text passages.

Mark Boulton discusses the importance of defning the underlying content structure of a page:

You can create good experiences without knowing the content. What you can’t do is create good experiences without knowing your content structure. What is your content made from, not what your content is.

\- Mark Boulton

By defning a page’s skeleton we’re able to create a system that can account for a variety of dynamic content, all while providing needed guardrails for the types of content that populate certain design patterns. For example, the homepage template for Time Inc. shows a few key components in action while also demonstrating content structure regarding image sizes and character lengths:

![](images/521876376a41278561d41c06aaeecbe39111a5855188354de7d8e8f9cf67b7bf.jpg)

Time Inc.’s homepage template demonstrates the content’s underlying structure.

Now that we’ve established our pages’ skeletal system, let’s put some meat on them bones!

![](images/cb2699785f33a7da3c86d199427b012ad6ae1e23a661af15a82561cd117b630a.jpg)

Pages are specifc instances of templates that show what a UI looks like with real representative content in place. Building on our previous example, we can take the homepage template and pour representative text, images, and media into the template to show real content in action.

The page stage is the most concrete stage of atomic design, and it’s important for some rather obvious reasons. After all, this is what users will see and interact with when they visit your experience. This is what your stakeholders will sign of. And this is where you see all those components coming together to form a beautiful and functional user interface. Exciting!

![](images/8968569a2e3d97cbc0855123e574c6be4bb55fab6f73b8d3d13d975e1d2cb9ce.jpg)  
The page stage replaces placeholder content with real representative content to bring the design system to life.

In addition to demonstrating the fnal interface as your users will see it, pages are essential for testing the efectiveness of the underlying design system. It is at the page stage that we’re able to take a look at how all those patterns hold up when real content is applied to the design system. Does everything look great and function as it should? If the answer is no, then we can loop back and modify our molecules, organisms, and templates to better address our content’s needs.

When we pour real representative content into Time Inc.’s homepage template, we’re able to see how all those underlying design patterns hold up.

![](images/efad43f949b115694385814f1f2288d19c129f9a3b0b1336eee00d1fca7a3289.jpg)

![](images/62c609c21513e81931f91120079f6dafd9e0e926df538d4401d9d85466188e2a.jpg)  
MORE TIME INC. STORIES

## CHAMPION STORYTELLING AT THE OLYMPIC GAMES

Time Inc's brands cover every aspect of the Sochi XXII Winter Olympic Games. From the best athletes to the best viewing parties

![](images/0aa78390295c41302ab5431816a166b401d85bc1d7377d5294579da80ad76202.jpg)  
Story title # dolor set amit adipiscing volupsar a long title

![](images/1dd9a8f70b46857fddf373817b2ba449bca0fe40906a45e0d17d483f5df38eef.jpg)  
Story title W2 dolor set amit adipiscing volupsar a long title.

![](images/e6b15db5f6cd848df3b936b3547a8e38d03ca4087ac24f6bdf85d730d6f41a52.jpg)  
Story title #3 dolor set amit adipiscing volupsar a long title

![](images/ff2410379027ea46cc30b7682a3b84d13d45838e67df3d9d87ef8c586b8c8e83.jpg)  
Story title #4 dolor set amit adipiscing volupsar a long title.

At the page stage, we’re able to see what Time Inc.’s homepage looks like with real representative content in place. With actual content in place, we’re able to see if the UI components making up the page properly serve the content being poured into them.

We must create systems that establish reusable design patterns and also accurately refect the reality of the content we’re putting inside of those patterns.

Pages also provide a place to articulate variations in templates, which is crucial for establishing robust and reliant design systems. Here are just a few examples of template variations:

ɕ A user has one item in their shopping cart and another user has ten items in their cart.

ɕ A web app’s dashboard typically shows recent activity, but that section is suppressed for frst-time users.

ɕ One article headline might be 40 characters long, while another article headline might be 340 characters long.

ɕ Users with administrative privileges might see additional buttons and options on their dashboard compared to users who aren’t admins.

In all of these examples, the underlying templates are the same, but the user interfaces change to refect the dynamic nature of the content. These variations directly infuence how the underlying molecules, organisms, and templates are constructed. Therefore, creating pages that account for these variations helps us create more resilient design systems.

So that’s atomic design! These fve distinct stages concurrently work together to produce efective user interface design systems. To sum up atomic design in a nutshell:

ɕ Atoms are UI elements that can’t be broken down any further and serve as the elemental building blocks of an interface.

ɕ Molecules are collections of atoms that form relatively simple UI components.

ɕ Organisms are relatively complex components that form discrete sections of an interface.

Templates place components within a layout and demonstrate the design’s underlying content structure.

Pages apply real content to templates and articulate variations to demonstrate the fnal UI and test the resilience of the design system.