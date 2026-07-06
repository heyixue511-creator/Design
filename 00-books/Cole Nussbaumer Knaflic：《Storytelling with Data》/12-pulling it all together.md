# pulling it all together

Up to this point, we’ve focused on individual lessons that, together, set you up for success when it comes to effectively visualizing and communicating with data. To refresh your memory, we’ve covered the following lessons:

1. Understand the context (Chapter 1)

2. Choose an appropriate display (Chapter 2)

3. Eliminate clutter (Chapter 3)

4. Draw attention where you want it (Chapter 4)

5. Think like a designer (Chapter 5)

6. Tell a story (Chapter 7)

In this chapter, we will look at the comprehensive storytelling with data process from start to end—applying each of the preceding lessons—using a single example.

Let’s begin by considering Figure 8.1, which shows average retail price over time for five consumer products (A, B, C, D, and E). Spend a moment studying it.

![](images/77f3a2e819450fbdd12dd407c74cdc07544dd14efc324b0e895eb3c67d84fd34.jpg)  
Figure 8.1 Original visual

When presented with this graph, it’s easy to start picking it apart. But before we discuss the best way to visualize the data shown in Figure 8.1, let’s take a step back and consider the context.

## Lesson 1: understand the context

The first thing to do when faced with a visualization challenge is to make sure you have a robust understanding of the context and what you need to communicate. We must identify a specific audience and what they need to know or do, and determine the data we’ll use to illustrate our case. We should craft the Big Idea.

In this case, let’s assume we work for a startup that has created a consumer product. We are starting to think about how to price the product. One of the considerations in this decision‐making process— the one we will focus on here—is how competitors’ retail prices for products in this marketplace have changed over time. There is an observation made with the original visual that may be important: “Price has declined for all products on the market since the launch of Product C in 2010.”

If we pause to consider specifically the who, what, and how, let’s assume following:

Who: VP of Product, the primary decision maker in establishing our product’s price.

What: Understand how competitors’ pricing has changed over time and recommend a price range.

How: Show average retail price over time for Products A, B, C, D, and E.

The Big Idea, then, could be something like: Based on analysis of pricing in the market over time, to be competitive, we recommend introducing our product at a retail price in the range \$ABC–\$XYZ.

Next, let’s consider some different ways to visualize this data.

## Lesson 2: choose an appropriate display

Once we’ve identified the data we want to show, next comes the challenge of determining how to best visualize it. In this case, we are most interested in the trend in price over time for each product. If we look back to Figure 8.1, the variance in colors across the bars distract from this, making the exercise more difficult than necessary. Bear with me, as we’re going to go through more iterations of looking at this data than you might typically. The progression is interesting because it illustrates how different views of the data can influence what you pay attention to and the observations you can easily make.

First, let’s remove the visual obstacle of the variance in color and view the resulting graph, shown in Figure 8.2.

![](images/2fc20852186972cb2cf3a8b922e36441cd16f5403661dec4289953f5389370b1.jpg)  
Figure 8.2 Remove the variance in color

If you’re tempted to continue decluttering at this point, you are not alone. I had to resist the urge since that’s something I typically do as I go along. In this case, let’s refrain from doing so until the next section, where we can address it all at once.

Since the emphasis in the original headline was on what happened since Product C was launched in 2010, let’s highlight the relevant pieces of data to make it easier to focus our attention there for a moment. See Figure 8.3.

![](images/f7872e71f8998d3675f43e17ff6fb812aa978e3d068276fca5727458373d95a3.jpg)  
Figure 8.3 Emphasize 2010 forward

Upon studying this, we see clear declines in the average retail price for Products A and B in the time period of interest, but this doesn’t appear to hold true for the products that were launched later. We will definitely need to change the headline from the original visual to reflect this when we tell our comprehensive story.

If you’ve been thinking we should try a line graph here instead of a bar chart—since we are primarily interested in the trend over time—you are absolutely right. In doing so, we also eliminate the stairstep view that bars create somewhat artificially. Let’s see what lines would look like with the same layout as above. This is illustrated in Figure 8.4.

![](images/cb7a2ba4fa1df51d0622b2fc9c6926dae563aaefb863ab1854fcdbe8e3d86a30.jpg)  
Figure 8.4 Change to line graph

The view in Figure 8.4 allows us to see what’s happening over time more clearly for one product at a time. But it is hard to compare the products at a given point in time to one another. Graphing all of the lines against the same x‐axis will solve this. This will also reduce the clutter and redundancy of the multiple year labels. The resulting graph might look like Figure 8.5.

![](images/46c59d62032110ed94cf4f962e76b42cfe64cc28f499167b9ba84883872ec65f.jpg)  
Figure 8.5 Single line graph for all products

With the transition to the new graph setup, Excel added back the color that we removed in an earlier step (tying the data to the accompanying legend at the bottom). Let’s ignore that for a moment while we consider whether this view of the data will meet our needs. If we revisit our purpose, it is to understand how competitors’ prices have changed over time. The way the data is shown in Figure 8.5 allows for this with relative ease. We can make taking in this information even easier by eliminating clutter and drawing attention where we want it.

## Lesson 3: eliminate clutter

Figure 8.5 shows what our visual looks like when we rely on the default settings of our graphing application (Excel). We can improve this with the following changes:

•	 De‐emphasize the chart title. It needs to be present, but doesn’t need to attract as much attention as it does when written in bold black.

•	 Remove chart border and gridlines, which take up space without adding much value. Don’t let unnecessary elements distract from your data!

•	 Push the x‐ and y‐axis lines and labels to the background by making them grey. They shouldn’t compete visually with the data. Modify the x‐axis tick marks so they align with the data points.

•	 Remove the variance in colors between the various lines. We can use color more strategically, which we’ll discuss further momentarily.

•	 Label the lines directly, eliminating the work of going back and forth between the legend and the data to understand what is being shown.

Figure 8.6 shows what the graph looks like after making these changes.

Average Retail Product Price per Year  
![](images/5425aafbc4d82bde449a203e01abffd2196252eade6378e7df7f90ef14782c3f.jpg)  
Figure 8.6 Eliminate clutter  
Next, let’s explore how we can focus our audience’s attention.

## Lesson 4: draw attention where you want your audience to focus

With the view shown in Figure 8.6, we can much more easily see and comment on what’s happening over time. Let’s explore how we can focus on different aspects of the data through strategic use of preattentive attributes.

Consider the initial headline: “Price has declined for all products on the market since the launch of Product C in 2010.” Upon a closer look at the data, I might modify it to say something like, “After the launch of Product C in 2010, the average retail price of existing products declined.” Figure 8.7 demonstrates how we can tie the important points in the data to these words through the strategic use of color.

Average Retail Product Price per Year  
![](images/0e1418e00f727638ec237ff5c639a1f4a9740e9f9511e9d6bce7ad9c9dbd7f65.jpg)  
Figure 8.7 Focus the audience’s attention

In addition to the colored segments of the lines in Figure 8.7, attention is also drawn to the introduction of Product C in 2010 through the addition of a data marker at that point. This is tied visually to the subsequent decrease over time in Products A and B through the consistent use of color.

## Changing components of a graph in Excel

ypically, you format a series of data (a line or a series of bars) all at once. Sometimes, however, it can be useful to have certain points formatted differently—for example, to draw attention to specific parts, as illustrated in Figures 8.7, 8.8, and 8.9. To do this, click on the data series once to highlight it, then click again to highlight just the point of interest. Right‐click and select Format Data Point to open the menu that will allow you to reformat the specific point as desired (for example, to change the color or add a data marker). Repeat this process for each data point you want to modify. It takes time, but the resulting visual is easier to comprehend for your audience. It is time well spent!

We can use this same view and strategy to concentrate on another observation—one perhaps more interesting and noteworthy: “With the launch of a new product in this space, it is typical to see an initial average retail price increase, followed by a decline.” See Figure 8.8.

Average Retail Product Price per Year  
![](images/7e5db9c676a8599a336209478291e93afbd19762285e3d7cb005a0c97db94f4c.jpg)  
Figure 8.8 Refocus the audience’s attention

It might also be interesting to note, “As of 2014, retail prices have converged across products, with an average retail price of \$223, ranging from a low of \$180 (Product C) to a high of \$260 (Product A).” Figure 8.9 uses color and data markers to draw our attention to the specific points in the data that support this observation.

Average Retail Product Price per Year  
![](images/57c2825b2e9cde5e8145453ed00b10031a6ab497b7fb9b92169e9f5ad034b120.jpg)  
Figure 8.9 Refocus the audience’s attention again

With each different view of the data, the use of preattentive attributes allows you to more clearly see certain things. This strategy can be used to highlight and tell different pieces of a nuanced story.

But before we continue thinking through how to best tell the story, let’s put on our designer hats and perfect the visual.

## Lesson 5: think like a designer

Though you may not have recognized it explicitly as such, we’ve already been thinking like a designer through this process. Form follows function: we chose a visual display (form) that will allow our audience to do what we need them to do (function) with ease. When it comes to using visual affordances to make it clear how our audience should interact with our visual, we’ve already taken steps to cut clutter and de‐emphasize some elements of the graph, while emphasizing and drawing attention to others.

We can further improve this visual by leveraging the lessons we covered in Chapter 5 with respect to accessibility and aesthetics. Specifically, we can:

•	 Make the visual accessible with text. We can use simpler text in the graph title and capitalize only the first word to make it easier to comprehend and quicker to read. We also need to add axis titles to both the vertical and horizontal axes.

•	 Align elements to improve aesthetics: The center alignment of the graph title leaves it hanging in space and doesn’t align it with any other elements; we should upper‐left‐most align the graph title. Align the y‐axis title vertically with the uppermost label and the x‐axis title horizontally with the leftmost label. This creates cleaner lines and ensures that your audience sees how to interpret what they are looking at before they get to the actual data.

Figure 8.10 shows what the visual looks like after these changes have been made.  
Retail price over time  
![](images/944c2f4cbe53c5fd19636f3b3a3882188743b3149bfda27143ea843e62debeaa.jpg)  
Figure 8.10 Add text and align elements

## Lesson 6: tell a story

Finally, it is time to think about how we can use the visual we’ve created in Figure 8.10 as a foundation to walk our audience through the story in the way that we want them to experience it.

Imagine we have five minutes in a live presentation setting under the agenda topic: “Competitive Landscape—Pricing.” The following sequence (Figures 8.11–8.19) illustrates one path we could take for telling a story with this data.

In the next 5 minutes...

## OUR GOAL:

<sup>BUnderstand</sup> <sup>how</sup> <sup>prices</sup> <sup>have</sup> <sup>changed</sup>over time in the competitive landscape.

<sub>D</sub>Use this knowledge to inform the pricing<sub>of</sub> <sub>our</sub> <sub>product.</sub>

We will end with a specific recommendation. Figure 8.11

Products A and B were launched in 2008 at price points of \$360+

Retail price over time  
![](images/4a3ba4fdd8ceca271fc347ade78a4525798e1cda876c6c9c5623975ff0366c53.jpg)  
Figure 8.12  
They have been priced similarly over time, with B consistently slightly lower than A  
Retail price over time

![](images/ce925cb36e4091bc7447d11810661c0276e892850524a6e0b2831e0b25406906.jpg)  
Figure 8.13

In 2014, Products A and B were priced at \$260 and \$250, respectively  
Retail price over time  
![](images/4035f60b0e50a27b7a8fbebe7150ef31f325a5fee68d10b4bf27541b1f38fe05.jpg)  
Figure 8.14  
Products C, D, and E were each introduced later at much lower price points...  
Retail price over time

![](images/afcc7af15848d06e7fe11e2c376e0594f416abde612362b925ccce4499bad355.jpg)  
Figure 8.15

…but all have increased in price since their respective launches

Retail price over time  
![](images/8f1d0fec547195365e359868c3d065a65d8079a850b1bf62f7b59a5cf7134646.jpg)  
Figure 8.16

In fact, with the launch of a new product in this space, we tend to see an initial price increase, followed by a decrease over time

Retail price over time  
![](images/3b013e3eb67dba8c147c897d675432b224adb06d2f228b79b13882c95b409e32.jpg)  
Figure 8.17

As of 2014, retail prices have converged, with an average retail price of \$223, ranging from a low of \$180 (C) to a high of \$260 (A)

![](images/5befa708b0a25350fa86d0c7bef1e1112cfb76b1a11d05c0c6f592e4f00acaa4.jpg)  
Figure 8.18

To be competitive, we recommend introducing our product below the \$223 average price point in the \$150−\$200 range

Retail price over time  
![](images/67d886a9d5534a41534c4350b34bd835fa5510d95a5e85bbd79bbf901089f8b5.jpg)  
Figure 8.19

Let’s consider this progression. We started off by telling our audience the structure we would follow. I can imagine the voiceover in the live presentation could further set the plot before moving to the next slide: “As you all know, there are five products that will be our key competition in the marketplace,” then building the chronological price path that those products followed. We can introduce tension in the competitive landscape when Products C, D, and E significantly undercut existing price points at their respective launches. We can then restore a sense of balance as the prices converge. We end with a clear call to action: the recommendation for pricing our product.

By drawing our audience’s attention to the specific part of the story we want to focus on—either by only showing the relevant points or by pushing other things to the background and emphasizing only the relevant pieces and pairing this with a thoughtful narrative—we’ve led our audience through the story.

Here, we’ve looked at an example telling a story with a single visual. This same process and individual lessons can be followed when you have multiple visuals in a broader presentation or communication. In that case, think about the overarching story that ties it all together. Individual stories for a given visualization within that larger presentation, such as the one we’ve looked at here, can be considered subplots within the broader storyline.

## In closing

Through this example, we’ve seen the storytelling with data process from start to finish. We began by building a robust understanding of the context. We chose an appropriate visual display. We identified and eliminated clutter. We used preattentive attributes to draw our audience’s attention to where we want them to focus. We put on our designer hats, adding text to make our visual accessible and employing alignment to improve the aesthetics. We crafted a compelling narrative and told a story.

Consider the before‐and‐after shown in Figure 8.20.

Price has declined for all products on the market since the launch of Product C in 2010

![](images/8fd2931fccbb3338e2310f74887c8f158325596c08782fe48944b65e997f2779.jpg)  
Figure 8.20 Before‐and‐after  
To be competitive, we recommend introducing our product below the \$223 average price point in the \$150−\$200 range

![](images/21afddbd6de56ab34c61fd4b5b6eaf05f65cf4387a05800d7c4ca56653ae8096.jpg)

The lessons we’ve learned and employed help us move from simply showing data to storytelling with data.