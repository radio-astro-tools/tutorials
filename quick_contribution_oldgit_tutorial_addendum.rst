Extra special steps for those using git version 1.7.1
-----------------------------------------------------

   There's one more step of configuration at this point if using Git
   version 1.7.1 (or, likely any version less than 1.7.10.) Open
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

   You may now resume the normal tutorial :doc:`quick_contribution_tutorial.rst`
