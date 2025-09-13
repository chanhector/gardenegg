#!/usr/local/bin/perl
print "Content-type: text/html\n\n";
print "<HTML><HEAD><TITLE>Email Test</TITLE></HEAD><BODY TEXT=$colortext BGCOLOR=$colorbg LINK=$colorlink VLINK=$colorvlink ALINK=$coloralink>\n";

##############################################
# SUB: Send E-mail
#
# Takes:
# (To, Subject, Reply-To, IP ADDRESS of SMTP host, Message)
##############################################
# SUB: Send E-mail

$TO="support\@helix.com.hk"; 
$SUBJECT="Testing";
$REPLYTO="peter\@helix.com.hk"; # put your e-mail here.
$BLATPATH = "blat.exe ";

$commandline = $BLATPATH;
$commandline .= "d:/home/chanhector/public_html/dir/readme.txt "; # the temp file
$commandline .= "-s $SUBJECT ";
$commandline .= "-t $TO " if $TO;
$commandline .= "-f $REPLYTO " if $REPLYTO;
print "\$commandline \= $commandline";
system($commandline);
print "<P>\n";
print "<P>\n";
print "Blat has been executed.  <P>\n";

#system ($commandline);
