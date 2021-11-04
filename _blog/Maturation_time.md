
---
title: Fluorescence maturation time: is it a bug or a tool?
subtitle: Using fluorescent maturation delays to infer gene expression dynamics from static snapshots of cell-to-cell variability
status: active 

description: |
  This blog post has a long title, with a subtitle.
  Setting the `no-link` property means that there's no link.

people: # add peope that are involved in this project
  - euan

layout: blog # do not change this
image: #'posts/forking/nice-fork.png'

last-updated: 2021-10-29
# do NOT add 0 (such as 06 for June). Will break everything lol
# take out the underscore in the name.
---

Few methods in the history of science have had a bigger impact than visualizing cellular processes with fluorescent proteins ([Exhibit A: Nobel Prizes 2008](https://www.nobelprize.org/prizes/chemistry/2008/illustrated-information/), [Exhibit B: Nobel Prize 2014](https:/www.nobelprize.org/prizes/chemistry/2014/prize-announcement/), [Exhibit C: This mind-blowing video of a brain](https://www.youtube.com/watch?v=c-NMfp13Uug)).
Invaluable as they are, an important caveat when using fluorescent proteins is that freshly produced proteins are dark and take time before they fluoresce, a process that can range from minutes to hours. Fluorescent proteins with short ``maturation times'' are thus used to avoid delays when probing dynamic systems.

Fluorescent maturation delays are analogous to the delayed response of COVID-19 case numbers. As infections take time to lead to symptoms, tests take time to be analyzed, and test results take time to be reported, the reported case numbers are not an instantaneous read-out of the actual number of infections. Similarly, fluorescence levels do not follow protein levels instantaneously because of their finite maturation time. Such delays are obviously bad for following (or controlling) dynamics in real-time, but there is an additional effect: because the maturation time of an individual protein is random and not a fixed number, even the average variability of a signal will be affected. For example, even if COVID-19 case numbers were delayed by a year, but the delay is always exactly the same, we could still recover the maximum number of cases that actually occurred from retrospective time-traces. However, if some of the cases get reported immediately, some take months, and some take a year, the whole dynamics are washed out, and we can no longer identify the size of the peak. The variability of the curve will be washed out due to the probabilistic delay of individual reports, and the very same is true for fluorescence levels in cells. This is why picking a fluorescent protein with fast maturation is a key experimental consideration.

The answer is yes we can!, because how much an exponentially distributed delay washes out a signal depends on the dynamics of the unseen original signal, and this can be exploited to infer unseen dynamics from observed variability. In particular, if we have two different fluorescent proteins X and Y reporting the same upstream signal, i.e., the transcription rate of a gene of interest, then the differences in variability will tell us something about the time-scale of the transcription rate variability. In fact, it's not just the time-scale of the invisible upstream dynamics of the signal that matters, but also its temporal structure! That's the entire (very simple) idea we are exploiting. The rest is just filling in the mathematical details which are all in the paper.

For example, oscillations are different from stochastic signals.  Time-averaged responses of the latter are constrained by
\begin{align}
    T_{m} \leq \frac{CV_{x}}{CV_{y}},
    \label{EQ: The bound}
\end{align}
where $T_{m} := \tau_{mat,y}/\tau_{mat,x}$ is the ratio of maturation times of the two fluorescent proteins, and $CV$ is the coefficient of variation obtainable from static snapshots of cell-to-cell variability. Any violation of this inequality implies that the transcription must be oscillating, even if cells are not followed over time and the transcription rate is never directly observed. This is crucial, because in recent years there has been an explosion of data produced from high-throughput methods like single-cell RNA sequencing and flow cytometry, and these methods lack temporal resolution and produce static snapshots of cell-to-cell variability. A key aim of systems biology is to translate such static datasets into gene expression dynamics.

Engineering co-regulated fluorescent reporters to readout a signal of interest is not new. In fact, such ``dual reporters'' have previously been used to quantify sources of non-genetic variability in gene expression. However, a fundamental issue remains when interpreting cell-to-cell variability: we generally do not know whether a component’s variability is due to stochastic upstream noise or whether a component is driven by deterministic variability. Eq. (1) can thus become and experimental tool to distinguish cell-to-cell variability that is caused by deterministic oscillations from variability due to stochastic fluctuations. 

There are quite a few more ideas in the paper \cite{joly2021inferring}  (such as detecting feedback), and if you're interested you can read about them [here](https://arxiv.org/abs/2109.00392~).
Currently we are working on an experimental collaboration to test these results in live cells using a synthetic biology approach. We hope to share with you the results of these experiments another time.


This is the text that will appear in the webpage, in Markdown.

To create a project, just create a markdown file in the `_projects` folder. Here are the things you can put in the YAML frontmatter:

- `title:` The project title.
- `notitle:` Set this to `true` if you don't want a title displayed on the project card. Optional.
- `description:` The text shown in the project card. It supports markdown.
- `people:` The people working on the project. This is a list of keys from the `_data/people.yml` file.
- `layout: project` This sets the layout of the actual project page. It should be set to `project`.
- `image:` The URL of an image for the project. This is shown on both the project page and the project card. Optional.
- `last-updated:` Date in the format of `YYYY-MM-DD`. The project cards are sorted by this, most recent first.
- `status: inactive` Set this to `inactive` if don't want the project to appear on the front page. Just ignore it otherwise.
- `link:` Set this to an external URL if this project has a page somewhere else on the web. If you don't have a `link:`, then the content of this markdown file (below the YAML frontmatter) will be this project's page.
- `no-link: true` Set this if you just don't want a project page for your project.

Links to github can be added like
[this](https://github.com/hlml-toronto/).

Adding images is as simple as using an html command for images, such as this:

<img src="/img/posts/Maturation_time/maturation_time.jpg" alt="idp" width="400px" align="center" style="padding:5px;">

Try to keep a nice hierarchy of images in our img folder.
