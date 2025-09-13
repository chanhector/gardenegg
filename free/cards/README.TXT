        ** card.cgi Virtual Greeting Card Generator **
                 ** Installion Instructions **
             Another Free Script by BigNoseBird.Com
                      Updated 04-18-1999

   Security Note: place an "index.html" in the cards directory
   so it is snoop-proof!

04-28-99 

   Added ability to do either sendmail or SMTP

04-18-99

   Since so many people where having problems with sendmail,
   I replaced it with SOCKET based SMTP. You now need to specify
   an SMTP server if your computer is not capable of originating
   e-mail. By default it is set to localhost which should be fine
   for almost all systems- unix or windows.

   There is now a single card setup for both the preview and the
   final card. Don't kill the line that says $param. That is what
   contains all the hidden fields that must be sent from preview
   to create the final card.

   Moved all user configurable stuff such as thank you, card format,
   e-mail notification up near the top so you have an easier time
   finding it!

11-02-98

   Fixed the Sat Sep  8 21:46:39 2001 bug. Due to the way the
   files are named, come this date new file numbers would only
   be possible every 10 seconds! This fix also provides for
   a zero chance of collisions- even if cards are created at the
   same second.

   Replaced $VALID_DOMAIN with the array okaydomains. This way
   you can support the script from multiple sites. (unix only)

07-17-98 Let's call it Version 1.2.0 ;-)
 
  I went through ALL the e-mail over the past couple of months
  and the following items should eliminate most of my "help"
  e-mail on this script. (one can dream, right?)

  1.) Some servers are now parsing all pages whether they
      have the extention shtml or html. Added code to remove
      comment tags to prevent server side include nasties!

  2.) Routine and logic added to test recipient's e-mail 
      address for valid format.

  3.) Runtime diagnostics to let you know if your $MAIL_PROG
      or $BASEDIR are set wrong. Permissions on $BASEDIR are
      checked as well.

  4.) Optional $VALID_DOMAIN check for preventing others from
      attempting to call your script from their site.

05-18-98
  
  1.) Auto Expire feature has been added. You will find
      the $DAYS=11; which means to delete cards older than
      11 days. You can set this number to whatever you wish.
      If you delete the line $DAYS=11; you can disable this
      feature. 

  2.) You can now have users pick background images by
      setting the FORM field "background". Place the 
      background graphics files in the same directory as
      your cards. You can then set up a display of the graphic
      along with radio buttons such as:

      <INPUT TYPE=RADIO NAME="background" VALUE="" CHECKED>None
      <INPUT TYPE=RADIO NAME="background" VALUE="file.gif">Blue Sky
      <INPUT TYPE=RADIO NAME="background" VALUE="filx.gif">Red Sky

03-08-98

  1.) The system also records a list from/to e-mail addresses
      in cards/maillog  (PLEASE DO NOT ABUSE THIS FEATURE!)
  2.) Midi music is now supported.
  3.) All midi and graphic files MUST reside in the cards
      directory.
  4.) For people with multiple card pages, a feature for you!
      The script passes the original HTML page name to the
      "Thank You" screen so you do not have to have more than
      one script for all of your pages.

03-26-98

  1.) Downshift of month in URL name to help AOL recipients!

04-13-98
  1.) Eliminated ccount sequential numbering and replaced it
      with the following format.:  apr13-76091 where the 5
      digit number is the last part of the system integer 
       representing the date and time. This should help reduce
     installation problems, AND make it pretty hard for people to 
     snoop for cards!

Hopefully these modifications and additions will prevent some of
the problems a few people have had, as well as make the script more
flexible.

##################################################################
  (C)1998-9 Bignosebird.com
  This software is FREEWARE! Do with it as you wish. It is yours
  to share and enjoy. Modify it, improve it, and have fun with it!
  It is distributed strictly as a learning aid and bignosebird.com
  disclaims all warranties- including but not limited to:         
  fitness for a particular purpose, merchantability, loss of      
  business, harm to your system, etc... ALWAYS BACK UP YOUR
  SYSTEM BEFORE INSTALLING ANY SCRIPT OR PROGRAM FROM ANY
  SOURCE!                          
  Note: Although I obtained these midi files from what I believe
  to be public domain sources, I cannot warranty this to be true.
##################################################################

WHAT THIS PROGRAM DOES.
This script allows you to provide a Virtual Greeting Card 
service to your site's visitors. It is a rather simple concept.
The goal is to allow a user to create a small HTML file and
e-mail a recipient the URL with as little input as possible.
The created files are named along the lines of:
nov11-12345 where nov11 is November 11th, and 12345 is the
last 5 digits of the unix system time.
This makes for easy purging.  ie,# rm nov11*.html

HOW IT WORKS.
Once on the HTML page that contains the FORM that calls card.cgi
the user supplies:
   A Picture selection
   The Sender's name and e-mail address
   The Recipient's name and e-mail address
   Select the TEXT color
   Select the BACKGROUND color
   Provide a Title
   Provide a Message (body)
   Provide a Signature Line
   Pick a Song
   (optional background image)
These steps completed, the user may either preview or clear
the form. Assuming they preview, the script does the following.
   Reads the input from the submitted form
   Outputs back to the browser, HTML on the fly showing a 
     preview of the card. The user can then either SEND or
     edit the card.
When SEND is clicked, the script then
   Creates a new HTML file with a unique name
   Sends e-mail to the recipient explaining how to pick up the card
   Displays a confirmation screen to the user

WHAT IS CONTAINED IN THIS DISTRIBUTION?
This file, either in unix tar format or as a zip archive should
contain the following files:

README.TXT    Instructions
card.cgi      The Script 
card.html     An example page with the FORM
babybird.jpg  example 175W X 250H Graphic
birthday.jpg  ""
getwell.jpg   ""
longbird.jpg  ""
turkey.jpg    ""
irish.jpg     ""
tnailbb.jpg   example 75W X 107H Thumbnail Graphic
tnailbt.jpg   ""
tnailgw.jpg   ""
tnaillb.jpg   ""
tnailtk.jpg   ""
tnailir.jpg   ""
addicted.mid  example MIDI file
alloveru.mid ""
bestfriend.mid ""
birthday.mid ""
doyaloveme.mid ""
holdyrhand.mid ""
itsinyreyes.mid ""
itsmyparty.mid ""
thatthing.mid ""
walksunshine.mid ""


HOW DO I INSTALL THIS PROGRAM?
Assuming you have some type of UNIX server and CGI permission,
just do the following.

1.) Create a subdirectory in your main HTML documents directory
    called "cards". use whatever means necessary to set the 
    permissions to 777. This means that using telnet you would give
    the command: chmod 777 cards
       With FTP, use the command tool to set the unix permissions
       so that owner can read-write-execute, 
       group can read-write-execute,
       others can read-execute. 
2.) Upload all of the midi & graphic files to the cards directory.
3.) Upload the card.html file to your main HTML directory.
4.) Upload the card.cgi program to your cgi-bin directory-
    making absolute certain that you:
    a) upload the file from your PC to the server as ASCII-
       NOT binary.
    b) use whatever means necessary to set the permissions
       to 755. This means that using telnet you would give
       the command: chmod 755 card.cgi
       With FTP, use the command tool to set the unix permissions
       so that owner can read-write-execute, group can read-execute,
       others can read-execute.
5.) Edit the card.cgi file so that the proper path and file names
    are at the top. Additionally, search for the string 
         BNB SAYS! for tips on customization of messages and
    such. Keep in mind that there are two fairly identical
    HTML sections of the card.cgi program regarding the preview.
    The reason they are duplicated for the most part is that you
    might want messages on the preview and the real card to differ.
6.) Edit the card.html file to meet your needs. Note: Until you 
    really have the hang of things, please do not change any
    variable or field names in the program or form.
7.) Create graphics to suite your needs. Okay, mine are corny,
    but they are cute in their own way. The sizes I used were
    250H X 175W for the actual size, and 107H X 75W for the
    thumbnails.

User instructions are of course written into the form itself!

Have fun and enjoy card.cgi. If you have any problems, please
first check that you uploaded the file as ASCII and that you
set the permissions properly.

Please let me know when you have it up and running so I can
see what you are doing with the script. I will of course add
a link from my site to yours.

Good luck!
Bruce

PS- If you have any problems, PLEASE go to 
      http://bignosebird.com/trouble.shtml before writing me.

http://bignosebird.com/


