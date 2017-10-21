##############################################################
##############################################################

FFFF     A      CCC   EEEE    RRR  EEEE  CCC   OOO  N   N  
F       A A    C   C  E       R  R E    C   C O   O NN  N
FFF    A   A   C      EEE     RRR  EEE  C     O   O N N N
F     AAAAAAA  C   C  E       R R  E    C   C O   O N  NN
F    A       A  CCC   EEEE    R  R EEEE  CCC   OOO  N   N  

##############################################################
##############################################################




This project is about using Face Recognition to authenticate to Ubuntu, Windows or Mac SO's during login windows at system start as an alternative.

I will first try to test it on Ubuntu SO (the first version will work on it), but then this application will grow and expand to other ones.

For this, I'm going to use python language and PAM module to generate this login alternative.
For preparing the environment to work, it's very simple. You must execute:
- bash install.sh
and it will install all dependencies automatically.

An example could be found in ExampleApp folder. The MyFirstRecognition.sh will show how can the script recognize people from "WhoIs" folder, and match with name of one person of "FaceDatabase" folder which contains an image of the people loaded to that database.  

The tool will consist of:
- Face Loader: a tool that can take a photo and save it to a directory (default is "FaceDatabase" on root project folder)
- Face Tester: a tool that you must use for testing if the person using the computer at this time is found in the database. It may help to test if you have recently load a new face.
- PAM: Module for adding it to system login.


===========================================================================
Tested on:

$ lsb_release -a
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.3 LTS
Release:	16.04
Codename:	xenial

$ uname -a 
Linux personal-ubuntu 4.10.0-37-generic #41~16.04.1-Ubuntu SMP Fri Oct 6 22:42:22 UTC 2017 i686 i686 i686 GNU/Linux
===========================================================================


Documentation:
--------------_


Python Face Recognition can be found here: https://github.com/ageitgey/face_recognition

