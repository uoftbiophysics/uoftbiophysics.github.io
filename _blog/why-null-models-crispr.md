---
title: What's the point of a simple theory?
subtitle: A story about the power of ``null models'' to shape how we interpret data
#status: inactive #active if you want it on the frontpage

category: paper

description: |
  A story about the power of ''null models'' to shape how we interpret data

people: # add peope that are involved in this project
  - maddy

layout: blog # do not change this
image: '/img/posts/why-null-modles-crispr/banfield_data_theory.svg'
#link:
no-link: false # if you don't want it's own webpage
last-updated: 2022-01-08
# do NOT add 0 (such as 06 for June). Will break everything lol
# take out the underscore in the name.
---

## Why do we need theory?

Experimentalists wade through the murky waters of biology, hoping to tease out knowledge by controlling the things they can control and carefully observing what they cannot. In a well-designed experiment, the observed data reveals some truth, and this truth is reached by painstakingly ruling out other explanations. This might sound logical and sytematic, but it's an art form: how do you know when you're done considering reasonable alternatives? And in biology, where some [truly unreasonable](https://www.theatlantic.com/science/archive/2017/06/jumping-spiders-can-see-the-moon/529329/) things can happen, how do you know what's 'reasonable' anyway?

This is where theory can help, and in particular, theory so simple that it predicts what would happen if *nothing* weird or cool was happening. Theories like this are often called ''null models'' because they model the ''null'' (''zero'' or ''nothing'') expectation. And if your null model ends up doing something weird or cool after all? Well, you're in business! 

To demonstrate the power of simple theory to understand biology, here's a story about a null model we created to better understand how bacteria overcome infection by viruses. 

## A brief introduction to the CRISPR immune system

Bacteria, single-celled organisms that inhabit [nearly every environment on earth](https://en.wikipedia.org/wiki/Extremophile), can get the flu too. Well, not the flu exactly, but there are viruses called *phages* that infect bacteria specifically. If you're a bacterium and your entire body (a single cell) gets infected by a phage, this is a big problem, so bacteria have evolved [many cool ways to deal with phages](https://kids.frontiersin.org/articles/10.3389/frym.2019.00102). 

For 60 years since the [1940s](https://en.wikipedia.org/wiki/Luria%E2%80%93Delbr%C3%BCck_experiment), all known bacterial immune processes could be boiled down to *innate* immunity: either you were born lucky with the right mutation, or you die. But in the mid-2000s, [several](https://pubmed.ncbi.nlm.nih.gov/15791728/) [groups](https://pubmed.ncbi.nlm.nih.gov/16079334/) [near](https://pubmed.ncbi.nlm.nih.gov/16545108/)-[simultaneously](https://pubmed.ncbi.nlm.nih.gov/15758212/) discovered something entirely new: an *adaptive* immune system that allows bacteria to gain new immunity to phages over the course of their short lifetimes. The section of bacterial DNA that contains this immune system had already been named CRISPR[^1] over a decade before, but now finally people knew what it did. 

Bacteria with a CRISPR immune system can store a memory of past phage infections by cutting out small pieces of phage DNA and inserting these pieces in their own genome. The phage DNA mugshots are (unhelpfully) called *spacers*, and bacteria use them to recognize and bind to the DNA of phages that they've seen before, then neatly snip the phage DNA at that spot[^2], making the phage DNA useless and preventing the infection from proceeding. The important concepts to remember as we go on are that CRISPR immunity works through bacteria acquiring *spacers*, and that because spacers are stored in the genome, bacteria pass on their immunity to all their descendants as well.

[^1]: CRISPR stands for Clustered Regularly Interspaced Short Palindromic Repeats, and it was given this name back in the 1990s by [Francisco Mojica](https://en.wikipedia.org/wiki/Francisco_Mojica) who first observed and characterized the genomic region that contains the CRISPR immune system in bacteria. It's a name that purely describes what the DNA looks like and says nothing at all about what it does!

[^2]: This part of CRISPR immunity, the ability of CRISPR to cut DNA in a particular spot determined by what matches a spacer, has fueled a massive revolution in genome editing. The hard part of DNA editing is making an accurate cut, and up until the 2010s this was done by painstakingly engineering a particular protein for each edit. But when researchers Jennifer Doudna and Emmanuelle Charpentier were studying the CRISPR immune system, they realized that they could give the CRISPR-associated (Cas) proteins any DNA sequence they wanted instead of phage-derived spacers and that it would then make a precise DNA cut at the exact place they wanted. The pair received the [2020 Nobel Prize in Chemistry](https://www.nature.com/articles/d41586-020-02765-9) for their discovery.

<p align="center">
<img src="/img/posts/why-null-models-crispr/CRISPR_diagram_v3.svg" alt="crispr_diagram" width="600px" style="padding:5px;">
</p>

## Where do skewed spacer abundance distributions come from?

Many different research groups have observed the same phenomenon: when bacteria use their CRISPR immune system, some spacers end up being a lot more common in the population than others. A *lot* more common: in the data we analyzed for this project, the most common spacer sequence was *ten thousand* times more common than the least common sequence. Distributions like this are often called ''long-tailed'' because in a histogram the data is smeared out for a long way on one or both sides: a long tail.

This figure shows the abundance of each spacer sequence in the experiment, and each colour is a different day in the 14-day experiment. Each sequence is sorted from most common to least common (left to right), and the y-axis shows the frequency of each sequence. For most days, the most common sequence at rank 1 has a frequency of 10<sup>-1</sup> = 10%, and the least common sequences have frequencies around 10<sup>-5</sup>.

<p align="center">
<img src="/img/posts/why-null-models-crispr/banfield_data.svg" alt="banfield_data" width="400px" style="padding:5px;">
</p>

This study also found that certain regions of the phage genome were more likely to be a source for spacers, and combined with this skewed abundance distribution, they concluded that the high-abundance spacers were special: their sequence makes them more likely to be high abundance. This sounds like a perfectly reasonable explanation, and it's supported by other experiments. Here’s a figure from a another paper that looked specifically at the process of spacer acquisition - they sequenced new spacers 24 hours after bacteria were infected by phages without leaving the bacteria lots of time to grow and die. They performed the same experiment twice (two 'replicates'), and this plot shows the frequency of spacer sequences in the first replicate versus the frequency of the same spacer sequences in the second replicate. The data points are strongly correlated: they fall on or near a straight diagonal line with slope 1. This means that if a spacer sequence was highly abundant in the first experiment, it is also generally highly abundant in the second experiment, suggesting that there is indeed something about the spacer itself that destines it for high or low abundance[^3]. 

[^3]: This [theory paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005486) included variable spacer effectiveness as an ingredient to get broad abundance distributions.

<p align="center">
<img src="/img/posts/why-null-models-crispr/Heler2019.svg" alt="Heler2019" width="450px" style="padding:5px;">
</p>

So we're done, right? We know why some spacers are highly abundant and others are not, and if we see a broad abundance distribution we know the cause. Or do we? Remember where we started: to figure out what's going on when we observe something, we have to rule out other explanations. Could there be other explanations for a spacer abundance distribution that looks like this? 

Enter our null model. We modelled bacteria and phage interacting with CRISPR, and we included absolutely no distinguishing features for individual spacers: all spacers were equally likely to be acquired and all spacers were equally effective at preventing infection. This is the most boring model possible that still includes the bare bones of CRISPR immunity. We simulated this population over time, watching bacteria grow, die, and acquire spacer sequences randomly. If a bacterium had a spacer when it was infected, it got a CRISPR immune boost and was more likely to survive.

<p align="center">
<img src="/img/posts/why-null-models-crispr/model_diagram_simplified.png" alt="model" width="800px" style="padding:5px;">
</p>

Amazingly, we found a strikingly broad spacer abundance distribution. The figure below compares experimental data on the left and our simulation data on the right. Our null model shows that you don't need special spacer sequences to find that some are very common and some are rare: you can get large differences in abundance purely because of randomness[^4].

[^4]: How exactly does the randomness produce this broad distribution? In a nutshell, it happens because there are multiple random events all happening together. A random subset of bacteria acquire spacers at random times, and then the processes of bacterial growth and death (also random) magnify the initial randomness. Imagine two different spacer acquisition events: if one happens a little earlier than the other, the first bacterium has more time to produce offspring that also contain the spacer, and since they're growing exponentially, that initial head start can mean a large difference in abundance later. Mathematically, we found that these distributions were most broad if the spacer acquisition probability was low (but still the same for every spacer). If spacer acquisition rates are high across the board, the randomness of bacterial growth and death gets 'washed out' by many acquisitions of the same sequence, and the abundance distribution becomes more sharply peaked. The gory details are in the supplementary material of [our paper](https://www.pnas.org/content/115/32/E7462) ([direct PDF link](http://madeleinebonsma.com/wp-content/uploads/2018/07/Bonsma-Fisher_PNAS_2018.pdf)).

<p align="center">
<img src="/img/posts/why-null-models-crispr/banfield_data_theory.svg" alt="banfield_data_theory" width="600px" style="padding:5px;">
</p>

Does this mean that the study that found high correlation between replicates was wrong to conclude that acquisition was biased? Not at all, in fact their study demonstrates that beyond a doubt! But here's the very important catch: our work shows that if you observe a broad distribution by itself, you *cannot* conclude that biased acquisition is the cause, because we know you don't need that ingredient to get a similar result. These things are all true at once: spacer acquisition IS biased, biased acquisition CAN lead to broad abundance distributions, BUT observing a broad abundance distribution does not guarantee that acquisition is biased. 

Why does this matter? In lab experiments like those described here, you can do multiple copies of the same experiment under the same conditions to prove a result. But the world is full of important and fascinating research areas where that isn't possible. Any study of bacteria in a natural environment is inherently unreproducible: you can never turn back the clock and do things the same way twice. So you trek to the glacial meltwater lake, sequence millions of bacteria, find all their CRISPR spacers, and plot the abundance distribution. How can you figure out what's going on? In biology *everything* is going on, and the key to understanding is to figure out *which* of the things going on are important for what you observe and which are not. And our null model taught us that if you want to learn about spacer acquisition, you'll need to look beyond a broad spacer abundance distribution to find it. 
