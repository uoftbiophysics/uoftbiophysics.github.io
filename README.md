# HLML

Welcome to our website!
It is hosted on Github Pages and uses Liquid and Jekyll to display the webpage.
It was made by slightly modifying a fork of "Mozilla Study Group" (see below) and many elements were inspired by the Uoft Coders fork of the same repository.

Normally contributing requires 'Watching' the repository, forking and push request.
Since we maintain our own internal schedule, I (Jeremy) thought it would be best if we stuck to a simple push/pull technique for updating any elements of the website.
Accordingly, below are the contribution mechanisms for different types of elements to the website.

## Contributing

If you're unfamiliar with Github for any of the following steps, please feel to contact anyone in the group for help.
First of all, you need to clone the repository to your local device.
To contribute properly, you'll need permission to push any changes you make to the remote repository.
To get the necessary permission, join the [hlml-toronto GitHub group](https://github.com/hlml-toronto).
You can contact any one of the owners of the group to join.
Once you have push access to the repository, you can start changing the code for the website and modifying whatever you please!
Remember to always pull first, in case someone else has made considerable changes to the repository before you manage to push any new code.
Any changes you make will take some time to appear on the website.

Although not necessary, you can locally view any changes you've made to the website before pushing it to the remote Github repository and having it go live for the world to see.
To do this, you'll need to have the correct packages on your local machine (talk to Jeremy for help).
For Linux users, here is a link that will help you get the correct packages: [jekyll install link](https://jekyllrb.com/docs/installation/ubuntu/).

Once this is done, you can easily start up a local server by navigating to the main folder of the repository and typing the following command in terminal:

```shell
jekyll serve
```

A bunch of text should appear in the terminal and the server should be up and running.
Find the server address displayed on the terminal and either ctrl-click it or type the address into a web browser to view the website.
To close the server, either close your terminal running the program or ctrl-c.

Again, this is not necessary to having the website work but it helps in understanding what your changes do to the website.

### Scheduled Events

To update the schedule you need to be able to run python scripts on your device and have push permissions to the repository.
We currently keep a schedule of our events on [this Google Sheet](https://docs.google.com/spreadsheets/d/1g5YJG3eM5Nce51zA7Vuy-tRkN3CzBXFOp02jR28Tjas/edit?usp=sharing).
To update the schedule on the website, first download the correct year from the Google Sheet as a .csv file and move it the the /\_data/ folder in this repo.
Then, move to the /scripts/ folder open the file /scripts/update_schedule.py in whichever IDE or text editor you prefer working in.
In line 5, you'll find a line you may need to change every year.

```python
year = '2021'
```

Note that if the name of our Google Sheets has changed in any way, you'll need to change the line 11 where the name of the file is (otherwise, no need to change it)

```python
file = "Machine Learning Club Schedule - "
```

Now, running the python script should populate the /\_posts/ folder, which is where all the event files are listed.
Commit all changes to your local repository (leave a comment if you'd like) and push to the remote repository.

### Projects

Adding a project is as simple as creating a markdown file in the folder /\_projects and filling it with the correct information.
An example may be found in /\_projects/\_project-template.md, feel free to copy it and change it.
The header is a YAML frontmatter, it gets parsed by the website in different areas to generate the project cards; filling in the information should be sufficient for having it appear on the website.
Below the YAML frontmatter is the content that will appear on the website.
It can be the copy/paste from the README.md of the corresponding Github repository, but I suggest putting a bit of effort into the content as it creates a nice webpage of it.

### Lessons

This still needs to be figured out, stay tuned.

### Adding/editing members

Member information can be found in /\_data/members.yml.
The data is in YAML format, which is pretty straightforward.
If you want to add any new keys for functionalities, be my guest!

### Any other changes to the website

Once you've made any changes and are happy with how it turned out, use git to commit your changes and push the code back to the remote repository.
The changes should take a couple of minutes to appear live.

This is meant to be a collaborative group and, as such, the building of the website is similarly a cooperative process.
If there are elements you want to add, play around with and change... be my guest!
Feel free to contact me (Jeremy) for any help you need or if you have ideas on what can be changed.

## Mozilla Study Groups

Welcome to [Mozilla Science Lab](https://www.mozillascience.org/)'s Study Group project! From here, we'll set you up with everything you need to start your own study group.

### Wait, What's a 'Mozilla Study Group'?

Mozilla Study Groups are fun, informal meetups of your friends and colleagues from around your local institution or town to share skills, stories and ideas on using code for research, and explore open research practices. The goal is to create a friendly, no-pressure environment where people can share their work, ask for help on a coding problem, and learn and work together with their peers. **Anyone can start a Study Group-- you don't have to be an expert coder to do so!**

What do Study Groups look like in Real Life? Check out the [Boston University Study Group's website](http://study.bu.edu/), and the [University of Toronto Coders website](https://uoftcoders.github.io/studyGroup/). You can also watch a few short [videos from Study Group Leads in our Orientation Guide](https://mozillascience.github.io/study-group-orientation/1-about-study-groups.html).


### For New Organizers
* **Join our Gitter Chat:** There are Study Groups all around the world. We use an online [Gitter Chat](https://gitter.im/mozillascience/studyGroup) to connect and share resources and ideas (you can sign in with GitHub, or using a Twitter ID if you're not set up on GitHub just yet). If you'd like to say hello, please introduce yourself in the chat, tell us where you are, and what you're thinking about or planning for your new Study Group. We're looking forward to meeting you.
* **Check out the Study Group Orientation Guide:**  If you think you might want to start your own group, [The Study Group Orientation Guide](https://mozillascience.github.io/study-group-orientation/index.html) covers running Group meetings, the super easy setup of your Study Group website, collaborating online using GitHub, an introduction to open research practice, and more. Take a look at the [About section here](https://mozillascience.github.io/study-group-orientation/1-about-study-groups.html) and the section on the [Study Group Lead role](https://mozillascience.github.io/study-group-orientation/1.1-lead-role.html)-- these should help you figure out if you'd like to start a Group.  
* **Come to an Online Orientation Meeting:** We’ll be running an online Orientation-- a series of 4 meetings, -- for new Group Leads starting next month (November 2016!) and also in January of 2017. It’s a great opportunity to meet, network, and share ideas with other Groups.  If you’re interested in joining us, [let us know by filling out this form.](https://docs.google.com/a/mozillafoundation.org/forms/d/e/1FAIpQLSdtKqAMQnKri-0xLx4hD_fpb000n9czsQd4oo9B2JUgtuIVlg/viewform?c=0&w=1)
* **Read the code of conduct:** this Study Group Program is for everyone - we abide by a [set of rules](https://www.mozillascience.org/code-of-conduct/) that require everyone be treated with respect. Help us make a space where everyone feels welcome, and we'll all have a better time!
* **Watch this repo:** up in the top right, there's a button that says 'Watch'; click it, and set yourself to 'Watching'. This will send you email notifications of new discussions; if you don't want email, but would like an alert just on GitHub, change the setting in Settings -> Notification Center (Settings is the little cog in the top right).

### How to Set Up Your Own Mozilla Study Group Website

Everything you need to set up your own beautiful Mozilla Study Group website (it looks like this!) for organizing events is [right here in the Orientation Guide.](https://mozillascience.github.io/study-group-orientation/3.3-get-online.html) If you are new to GitHub, don't worry, [there's an introduction to it here](https://mozillascience.github.io/study-group-orientation/3.1-collab-vers-github.html). Take a look, and if you need any help, you can ask a question in the [Gitter chat](https://gitter.im/mozillascience/studyGroup) or email sciencelab@mozillafoundation.org.

### How to Set Up Mozilla Study Group Website locally

* Fork the Repository [Mozilla Study Group.](https://github.com/mozillascience/studyGroup)
* Open Terminal (on a Mac) or the equivalent on your machine and type:
	1. git clone [SSH OR HTTPS CODE FOR studyGroup]
	2. cd studyGroup/
	3. jekyll build
	4. jekyll serve
* It shows "Server address". Open it in browser. Yes, Mozilla Study Group is set locally!!

#### It's Broken, I Need Help!!!

If anything in these instructions doesn't work or doesn't make sense, ask a question in the [Gitter chat](https://gitter.im/mozillascience/studyGroup), open an issue [here](https://github.com/mozillascience/studyGroup/issues) or email sciencelab@mozillafoundation.org.

### UPDATE November 2019

The Mozilla Science Lab was sunsetted in September of 2018.  While we had hoped to find a partnership with another organization to take the Study Group work forward, it did not take place.  Please feel free to use the materials hosted here to build your own Study Groups, though keep in mind that Mozilla is no longer actively supporting this program.

Our heartfelt :sparkling_heart: and appreciation to all the Study Group Leads and participants who made this program the success that it was.

Much of the work done by the Science Lab has moved on in some way under the Open Leadership & Events Team.  If you're interested in that work, you can see how that work is being continued on [their website](https://foundation.mozilla.org/en/initiatives/open-leadership-events/).
