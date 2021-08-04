---
title: Contributing
subtitle: Steps to contribute to uoftbiophysics repos (including this site).
description: Joining our uoftbiophysics GitHub organization, forking repositories, and contributing code.
layout: blog
last-updated: 2021-8-1 # do NOT add 0 (such as 06 for June). Will break everything lol
---

### Submitting and reviewing articles

**Join the uoftbiophysics GitHub organization**
1. Make a [GitHub](https://github.com/) account and sign in.
2. Send your GitHub username to Matt or Jeremy to be added to [our GitHub organization](https://github.com/uoftbiophysics).

**Fork the website repo**
1. Go to the [website repository](https://github.com/uoftbiophysics/uoftbiophysics.github.io).
2. In the top right, click "Fork". It should now exist at `https://github.com/YOUR_USERNAME/uoftbiophysics.github.io`.

**Clone the forked copy, make your changes, commit and push them**
1. Install Git locally. You can do everything from terminal or command line, or you can install a git GUI (e.g. SourceTree, GitKraken).
2. Clone the forked repo to your computer.

**Update the code**

2. Make changes to the site files.
4. Commit then push those changes.

**Create a Pull Request**
1. Go to the [original website repo](https://github.com/uoftbiophysics/uoftbiophysics.github.io).
2. Click "Pull requests" (third tab at the top).
3. Click "New Pull Request".
4. Selection: pull your forked copy and its changes into the original copy.
5. Details: fill out the topic/description, add any reviewers or assignees, and submit.

**Syncing a forked repository**

If you've already forked the repo and cloned it a while ago, the upstream repository code may have changed.
It should be synced before you add more code.
There are [two approaches to do this](https://docs.github.com/en/github/collaborating-with-pull-requests/working-with-forks/syncing-a-fork):

*Web UI*
- Navigate to your forked repo at `https://github.com/YOUR_USERNAME/uoftbiophysics.github.io`.
- Click "Fetch upstream" (below green Code button). Select "Fetch and merge".
- Locally, use `git pull` to update your copy of the fork.

*Command line*
- Configure upstream remote (if you haven't yet): <br/>`git remote add upstream https://github.com/uoftbiophysics/uoftbiophysics.github.git`
- Verify it was added: `git remote -v`
- To sync changes, do:
	- `git fetch upstream`
	- `git checkout main`
	- `git merge upstream/main`
- This syncs your local changes. To update your fork on Github you need to `push` any changes.

### Locally viewing the website (and your changes to it) ###

#### Windows ####

- [GitHub documentation](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
- [Extra documentation](https://idratherbewriting.com/documentation-theme-jekyll/mydoc_install_jekyll_on_windows.html)

*Prerequisites (details in the links above)*
1. [Install Ruby](https://rubyinstaller.org/downloads/) (under WITH DEVKIT, select option to add to PATH).
2. In command line: `gem install bundler`
3. In command line: `gem install jekyll`

*Viewing the site*
1. Open terminal or command line and change directory to the root of the cloned website repository.
2. `bundle install`
3. `bundle exec jekyll serve`
4. Navigate to http://localhost:4000/ and see if it worked.

*Troubleshooting:*
1. A gem file is needed, but should already be on git. In case it isn't, run `> bundle init` to make one.
2. On windows three lines should be added to the end of the file:
- gem 'wdm'
- gem 'jekyll'
- gem "webrick", "~> 1.7"
3. See if `bundle exec jekyll serve` works now.

#### Linux ####

*Prerequisites (details in the links above)*

You only need to do this once. Either
1. Install all dependencies by running the script `linux-setup.sh`; or
2. [Follow this guide](https://jekyllrb.com/docs/installation/ubuntu/).

*Viewing the site*

Run the command

```bash
$ jekyll serve
```
and either navigate to [http://localhost:4000/](http://localhost:4000/) or Ctrl+click the link in terminal for it to open automatically in browser.

*Troubleshooting*
1. If the following code appears

```bash
FATAL: Listen error: unable to monitor directories for changes.
        Visit https://github.com/guard/listen/blob/master/README.md#increasing-the-amount-of-inotify-watchers for info on how to fix this.
```
then it is likely your server didn't close properly in an earlier session. You can always increase the number of inotify-watchers by running

```bash
$ echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
```
