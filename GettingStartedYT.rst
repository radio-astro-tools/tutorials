Once YT is installed:

(Installation was easy on my RH Linux workstation using instructions at https://github.com/jzuhone/yt_radio_cubes. There were lots of problems with compilers on my OSX 10.7.5 Mac however and we gave up).

> pip install -U ipython (to get version of ipython with ipython notebook)

at this point you are probably inside yt-3.x, go to where you would like to actually do your work (for example where the fits data for the examples are)

> yt notebook

    this gives a series of instructions for getting the port forwarding

    the password is just to connect to your session, need not be secure (its like a vnc password)

--------------

The notebook is now live at:

    http://127.0.0.1:8888/

Recall you can create a new SSH tunnel dynamically by pressing

~C and then typing -L8888:localhost:8888

where the first number is the port on your local machine.

If you are using 8888 on your machine already, try -L8889:localhost:8888

---------------

type ~C to get out of shell

> -L8888:localhost:8888

Then in your browser (chrome or I used firefox which seems ok)

put the address http://127.0.0.1:8888/ -- this starts the iPy notebook after putting in the password you created at the yt notebook step

To get started in the notebook

click on New notebook button

import yt (shift enter takes you to next line)

To run one of the examples:

    On https://github.com/jzuhone/yt_radio_cubes click on the example, this will show the python script. Click the “raw” button. This is the webaddress you need to set in wget below

    In the directory that you started yt notebook in wget --no-check-certificate webaddress

    Now in the yt notebook webpage you should see the script appear, click on it, and it will go to a new tab with the script loaded. IT DOES NOT RUN IT, it is just showing it. To run it, starting at the top, shift-return each block of code (these are called “cells”). The [*] symbol at the side of a “cell” indicates its running.
