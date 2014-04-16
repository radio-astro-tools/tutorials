.. tutorial by Drew Brisbin with help from Adam Ginsburg and Thomas Robitaille

I have some code. I just want to add it! How do I do that?
==========================================================

`radioscripts_contrib
<https://github.com/radio-tools/radioscripts_contrib>`_ is a collection
of user-created radio astronomy python scripts. This code is offered
with minimal vetting process and without any guarantee of reliability
or accuracy. We encourage interested visitors to contribute by adding
their own useful python routines. The radioscripts_contrib collection
operates out of a Git Hub repository. Below is a very quick and very
dirty tutorial on how to contribute your own code to the
repository. This will not make you a Git master, but it will let you
get the job done. If you're interested in a more in depth look at
coordinating public contributed code in a nice controlled manner you
may want to check out the Astropy tutorial on contributing code:
http://docs.astropy.org/en/latest/development/workflow/development_workflow.html

Briefly, here are the steps we'll be going through (if these don't
make sense right now, don't worry we've got you covered below!):
install and configure Git; create a personal fork of the
radioscripts_contrib repository; clone your fork onto your machine;
add your code as a new file in the appropriate directory; add, commit,
and push your changes back onto your online repository; and finally do
a pull request to ask moderators to merge the changes in your fork
into the main version.


1. Get Git

   If you already know your way around Git you can skip down to step 2.

   a. If you don't already have an account, the first step is to go to
   https://github.com and set one up.

   b. Next you need to make sure Git is installed on your computer. If
   you're working on a linux machine there's a good chance you already
   have it. To check, open a terminal and type::

      git --version
   

   If git is installed you should see a message telling you what
   version you have. Something along these lines::

      git version 1.7.1

   If it's not installed head over to http://git-scm.com/downloads and
   download the version appropriate for your OS.

   c. You need to configure Git on your machine to let it know who you
   are. You can read through the Git guide on doing this here:
   https://help.github.com/articles/set-up-git#set-up-git But in the end
   this only requires two simple lines of typing in terminal::

   
      git config --global user.name "Your Name Here"
      git config --global user.email "your_email@example.com"
   

   The Git guide also describes how to set up password caching (and
   there's the alternative of using SSH keys instead.) These steps are
   *generally* only useful to save yourself time later from typing in
   a password when intereacting with your online Git repository. Don't
   worry about that unless you want to. *However,* if you have git
   version 1.7.1 (as we do in this example,) you need to set up SSH
   keys.

Extra special steps for those using git version 1.7.1
-----------------------------------------------------

   If you have a later version skip down to step 2.  For those of you
   working with git version 1.7.1, head over to
   https://help.github.com/articles/generating-sshkeys and follow
   along with their walkthrough and explanation of setting up an SSH key.


2. Set up your personal version of radioscripts_contrib

   a. You need to create a "fork" of the radioscripts_contrib
   repository to have a personal version you can muck around
   with. From the online Git repository
   (https://github.com/radio-tools/radioscripts_contrib) click the
   button labelled "Fork" located near the upper right hand corner.

   .. image:: forkbutton.png

   b. You now need to create a "clone" (copy) of the
   radioscripts_contrib repository. Navigate to a path in terminal
   where you want to work and type::

   
      git clone https://github.com/your-user-name/radioscripts_contrib.git
   

   c. This will create a subdirectory named radioscripts_contrib which
   contains the full repository. Within
   radioscripts_contrib/radioscripts_contrib/ scripts are organized
   into subfolders by topic. If there is a subfolder that describes
   the topic your script fits into, copy your code into that path (for
   instance, if you wrote a routine to fit spectral lines, this might
   belong under the spectralline path.) If no folder adequately
   describes the topic of your script, just copy it into the
   radioscripts_contrib/radioscripts_contrib/ path. We request that
   contributed code be prefaced with a two line license statement at
   the top::

   
      # Licensed under a 3-clause BSD style license - see LICENSE.rst
      # Copyright [authorname]
   

   We also request that you add a one or two line description of your
   code in the README file in the subdirectory where you place your
   code.

   Note that if you're just trying this tutorial out to get the hang
   of it, there's a file named helloworld.py which you should feel
   free to edit.


3. Tell the online GitHub about your edited version of the repository

Extra special steps for those using git version 1.7.1
-----------------------------------------------------

   There's one more step of configuration at this point if using Git
   version 1.7.1. If you have a more recent version skip down to step a. Open
   the file .git/config in your favorite text editor. It will look
   something like this::

   
      [core]
           repositoryformatversion = 0
           filemode = true
           bare = false
           logallrefupdates = true
      [remote "origin"]
           fetch = +refs/heads/*:refs/remotes/origin/*
           url = https://github.com/brisbind/radioscripts_contrib.git
      [branch "master"]
           remote = origin
           merge = refs/heads/master
   
   

   Change the url in the [remote "origin"] section::

   
      [core]
           repositoryformatversion = 0
           filemode = true
           bare = false
           logallrefupdates = true
      [remote "origin"]
           fetch = +refs/heads/*:refs/remotes/origin/*
           url = git@github.com:brisbind/radioscripts_contrib.git
      [branch "master"]
           remote = origin
           merge = refs/heads/master

   save and close the file.

   a. At this point on your machine you should have a version of the
   radioscripts_contrib repository that is nearly identical to the one
   you started with, except with one or two new or edited files (the
   README file and your new script.)

   If you ask Git about your files by typing::

   
      git status
   

   Git will point out these new and edited files to you. You should
   get some lines of informational text along with the notice that you
   have "Untracked" files. These are the files which are newly updated
   since the last time you told Git about the important files you want
   to add. Along with the one or two files you actually care about
   there might be some junk files you don't care about (autosaved
   files ending in a ~ for instance.) It will look something like
   this::

      # On branch master
      # Your branch is ahead of 'origin/master' by 1 commit.
      #
      # Untracked files:
      #   (use "git add <file>..." to include in what will be committed)
      #
      #	helloworld.py
      #       README.md
      #	helloworld.py~
      nothing added to commit but untracked files present (use "git add" to track)

   Stage the important files for uploading by typing::

   
      git add your-first-file.name
      git add your-second-file.name
   

   Ask git about the status again::

   
      git status
   

   And you should now see your important files listed under "# Changes
   to be committed"

   b. You are now ready to commit these changes. As you do this
   include a brief message saying what changes you've made in your Git
   repository::

      git commit -m "Added my python script to fit spectral lines and
      updated README"

   c. Now you need to push this version of the repository back online::

   
         git push
   

   d. Almost done, now you just need to request to get your
   contributions merged into the main radioscripts_contrib repository
   by performing a "pull request". To do this, go back to your online
   forked version of the radioscripts_contrib repository. If you want
   to check, you can browse to the appropriate path and you should now
   see your newly added file(s). On the left side of the page, just
   above the list of files there is a green button with two
   arrows. 

   .. image:: pullbutton1.png

   Click it to go to a page that will summarize your changes
   and ask for a title. If all looks good then click the green button
   on that page and your pull request will be processed

   .. image:: pullbutton2.png

You're done!


