#!/usr/local/bin/perl
#set the line above this to your perl path. Usually fine as is
# or /usr/local/bin/perl  /sbin/perl
# make certain that the first line stays the first line!

use Socket;

$|=1;

@okaydomains=("http://gardenegg.com", "http://www.gardenegg.com");
$DAYS=10;

# USE EITHER SMTP OR SEND_MAIL DEPENDING ON YOUR SYSTEM-
# BUT NOT BOTH!

$SMTP_SERVER="smtp.gardenegg.com";
#$SEND_MAIL="/usr/lib/sendmail -t";

$BASEDIR="/cards";
$BASEURL="http://gardenegg.com/cards";
$SITEURL="http://gardenegg.com/";
$SITENAME="GardenEgg.Com";
$EXT=".htm";
$PROGNAME="/usr/public_html/cgi-bin/card.cgi";
$MAILLOG="maillog";
$SUBJECT ="You have a virtual card waiting for you!";

###############################################################

  &main_driver;

###############################################################
#
# Now go thru the program looking for the string "BNB SAYS!"
# to locate other changes you should make, such as wording of
# the notification e-mail and "plug" for the site.
#
# to keep things simple, the field names are hard coded in.
# you can of course modify what you wish.
###############################################################

sub thank_you
{
 if ($MAILLOG ne "")
  {
   open (ML,">>$BASEDIR/$MAILLOG");      
   print ML "$fields{'recip_email'}\n";  
   print ML "$fields{'sender_email'}\n"; 
   close(ML);
  }

print "Content-type: text/html\n\n";
print <<__STOP_OF_THANKS__;

<CENTER>
<H1><B>THANKS!</B></H1>
Your card notification has been sent to $fields{'recip_name'}<BR>
The URL of this card is<P>
<A HREF="$URL_NAME">$URL_NAME</A>
<P>
<B><A HREF=$fields{'parent'}>RETURN TO CARD CREATOR</A></B>
<P>

__STOP_OF_THANKS__
}

# BNB SAYS! 
# THIS IS WHERE YOU CAN CUSTOMIZE YOUR NOTIFICATION LETTER
# DO NOT TOUCH THE TWO LINES WITH __STOP_OF_MESSAGE__ ON
# THEM!!!!

sub setup_letter
{
$msgtext =<<__STOP_OF_MESSAGE__;
Hi,

$fields{'sender_name'} stopped by my site, $SITENAME
and created a Virtual Card just for you! To pick up your
card, simply point your browser at the page listed below.

   $URL_NAME

The card will remain on the server for about one week, so
please print it out or save it as soon as you can.

__STOP_OF_MESSAGE__
}

# BNB SAYS! 
# This is what makes up the body of your card. DO NOT REMOVE OR
# MODIFY THE LINES ABOVE THE WORD $param or the $param line
# itself. Doing so will cause the script to fail.
sub make_body
{
$cardbody =<<__END_OF_CARD_BODY__;
<SCRIPT LANGUAGE="JavaScript">
<!--
if(navigator.userAgent.indexOf("MSIE") != -1)
document.writeln ('');
else
document.writeln ('<EMBED SRC="$BASEURL/$fields{'midifile'}" AUTOSTART="true" HIDDEN="true" VOLUME="80%">');
//-->
</SCRIPT>
<BGSOUND SRC="$BASEURL/$fields{'midifile'}">
$BODYTAG
$params
<CENTER>
<P>
<TABLE WIDTH=580 BGCOLOR=$fields{'back_color'} BORDER=5>
 <TR>
 <TD>
<TABLE WIDTH=580 BGCOLOR=$fields{'back_color'}>
 <TR>
 <TD>
  <TABLE WIDTH=200 BORDER=4>
    <TR>
      <TD ALIGN=CENTER VALIGN=CENTER>
       <IMG SRC=$BASEURL/$fields{'pic_select'} HEIGHT=250 WIDTH=175 BORDER=0><P>
      </TD>
    </TR>
  </TABLE>
 </TD>
 <TD WIDTH=380 VALIGN=TOP >
   <CENTER>
   <FONT SIZE=+2 COLOR=$fields{'text_color'}
     FACE=ARIAL><B>$fields{'the_title'}</B></FONT>
   <HR WIDTH=200>
   <TABLE WIDTH=355>
    <TR>
     <TD><FONT FACE=ARIAL COLOR=$fields{'text_color'}>
         $fields{'the_message'}

      <P ALIGN=CENTER>
      <I>$fields{'sig_line'}
      </I>
      </P>
      </FONT>
      </TD>
    </TR>
   </TABLE>
   </CENTER>
 </TD>
 </TR>
</TABLE>
</TD>
</TR>
</TABLE>
<P>
<TABLE WIDTH=500>
  <TR>
  <TD>
  <FONT FACE="ARIAL">
  This card was created by
  $fields{'sender_name'} 
  (<I><A HREF=mailto:$fields{'sender_email'}>
     $fields{'sender_email'}</A></I>)
  expressly for $fields{'recip_name'}. If you would like to
  send a card to a person you really care for, just go to
  <A HREF=$SITEURL>$SITEURL</A>
  and create your own free virtual cards.
  </FONT>
 <P>
 </FONT>
  <BLOCKQUOTE>
  <I>
  <A HREF=$SITEURL>$SITENAME</A> 
    BNB SAYS! DESCRIBE YOUR SITE HERE!
  <I>
  </BLOCKQUOTE>
<PRE>


</PRE>
<CENTER>
<FONT FACE="ARIAL" SIZE="-1"><B>
Card Creator Script by<A HREF="http://bignosebird.com"/>BigNoseBird.com</A>
</B><BR>
<I>Everything for the webmaster, for free!
</CENTER>
  </TD>
  </TR>
</TABLE>
</CENTER>
</BODY>
</HTML>
__END_OF_CARD_BODY__
}

sub pass_params
{
$params=<<__END_OF_PARAMS__;
<CENTER>
<TABLE WIDTH=500>
 <TR>
 <TD>
 <FONT FACE="ARIAL">
 <B>To send your creation, click on the SEND-CARD button. To return
    the card creation screen without sending, please press your
    browser's BACK button.
 </B>
 <P>
<CENTER>
<FORM METHOD="POST" ACTION="$PROGNAME">
<INPUT TYPE="HIDDEN" NAME="action_code" VALUE="SENDCARD">
<INPUT TYPE="HIDDEN" VALUE="$fields{'pic_select'}" NAME="pic_select">
<INPUT TYPE="HIDDEN" VALUE="$fields{'sender_name'}" NAME="sender_name">
<INPUT TYPE="HIDDEN" VALUE="$fields{'sender_email'}" NAME="sender_email">
<INPUT TYPE="HIDDEN" VALUE="$fields{'recip_name'}" NAME="recip_name">
<INPUT TYPE="HIDDEN" VALUE="$fields{'recip_email'}" NAME="recip_email">
<INPUT TYPE="HIDDEN" VALUE="$fields{'text_color'}" NAME="text_color">
<INPUT TYPE="HIDDEN" VALUE="$fields{'back_color'}" NAME="back_color">
<INPUT TYPE="HIDDEN" VALUE="$fields{'the_title'}" NAME="the_title">
<INPUT TYPE="HIDDEN" VALUE="$fields{'the_message'}" NAME="the_message">
<INPUT TYPE="HIDDEN" VALUE="$fields{'sig_line'}" NAME="sig_line">
<INPUT TYPE="HIDDEN" VALUE="$fields{'midifile'}" NAME="midifile">
<INPUT TYPE="HIDDEN" VALUE="$fields{'background'}" NAME="background">
<INPUT TYPE="HIDDEN" VALUE="$ENV{'HTTP_REFERER'}" NAME="parent">
<INPUT TYPE="submit" VALUE="SEND-CARD">   
</FORM>
</CENTER>
 </TD>
 </TR>
</TABLE>
__END_OF_PARAMS__
}


###################################################################
#Sendmail.pm routine below by Milivoj Ivkovic 
###################################################################
sub sendmail  {

# error codes below for those who bother to check result codes <gr>

# 1 success
# -1 $smtphost unknown
# -2 socket() failed
# -3 connect() failed
# -4 service not available
# -5 unspecified communication error
# -6 local user $to unknown on host $smtp
# -7 transmission of message failed
# -8 argument $to empty
#
#  Sample call:
#
# &sendmail($from, $reply, $to, $smtp, $subject, $message );
#
#  Note that there are several commands for cleaning up possible bad inputs - if you
#  are hard coding things from a library file, so of those are unnecesssary
#

    my ($fromaddr, $replyaddr, $to, $smtp, $subject, $message) = @_;

    $to =~ s/[ \t]+/, /g; # pack spaces and add comma
    $fromaddr =~ s/.*<([^\s]*?)>/$1/; # get from email address
    $replyaddr =~ s/.*<([^\s]*?)>/$1/; # get reply email address
    $replyaddr =~ s/^([^\s]+).*/$1/; # use first address
    $message =~ s/^\./\.\./gm; # handle . as first character
    $message =~ s/\r\n/\n/g; # handle line ending
    $message =~ s/\n/\r\n/g;
    $smtp =~ s/^\s+//g; # remove spaces around $smtp
    $smtp =~ s/\s+$//g;

    if (!$to)
    {
	return(-8);
    }

 if ($SMTP_SERVER ne "")
  {
    my($proto) = (getprotobyname('tcp'))[2];
    my($port) = (getservbyname('smtp', 'tcp'))[2];

    my($smtpaddr) = ($smtp =~
		     /^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/)
	? pack('C4',$1,$2,$3,$4)
	    : (gethostbyname($smtp))[4];

    if (!defined($smtpaddr))
    {
	return(-1);
    }

    if (!socket(MAIL, AF_INET, SOCK_STREAM, $proto))
    {
	return(-2);
    }

    if (!connect(MAIL, pack('Sna4x8', AF_INET, $port, $smtpaddr)))
    {
	return(-3);
    }

    my($oldfh) = select(MAIL);
    $| = 1;
    select($oldfh);

    $_ = <MAIL>;
    if (/^[45]/)
    {
	close(MAIL);
	return(-4);
    }

    print MAIL "helo $SMTP_SERVER\r\n";
    $_ = <MAIL>;
    if (/^[45]/)
    {
	close(MAIL);
	return(-5);
    }

    print MAIL "mail from: <$fromaddr>\r\n";
    $_ = <MAIL>;
    if (/^[45]/)
    {
	close(MA
    {
	close(MAIL);
	return(-5);
    }

    foreach (split(/, /, $to))
    {
	print MAIL "rcpt to: <$_>\r\n";
	$_ = <MAIL>;
	if (/^[45]/)
	{
	    close(MAIL);
	    return(-6);
	}
    }

    print MAIL "data\r\n";
    $_ = <MAIL>;
    if (/^[45]/)
    {
	close MAIL;
	return(-5);
    }

   }

  if ($SEND_MAIL ne "")
   {
     open (MAIL,"| $SEND_MAIL");
   }

    print MAIL "To: $to\n";
    print MAIL "From: $fromaddr\n";
    print MAIL "Reply-to: $replyaddr\n" if $replyaddr;
    print MAIL "X-Mailer: Perl Powered Socket Mailer\n";
    print MAIL "Subject: $subject\n\n";
    print MAIL "$message";
    print MAIL "\n.\n";

 if ($SMTP_SERVER ne "")
  {
    $_ = <MAIL>;
    if (/^[45]/)
    {
	close(MAIL);
	return(-7);
    }

    print MAIL "quit\r\n";
    $_ = <MAIL>;
  }

    close(MAIL);
    return(1);
}


sub no_email
{
print <<__STOP_OF_NOMAIL__;
Content-type: text/html

<FONT SIZE="+1">
<B>
SORRY! Your request could not be processed because of missing
e-mail address(es). Please use your browser's back button to
return to the card entry page.
</B>
</FONT>
__STOP_OF_NOMAIL__
}

sub send_mail
{

&setup_letter;
$mailresult=&sendmail($fields{sender_email}, $fields{sender_email}, $fields{recip_email}, $SMTP_SERVER, $SUBJECT, $msgtext); 

}

sub card_expire
 {
  local(@items, $item);
  opendir(CARDDIR, "$BASEDIR");
  @items = grep(/[0-9]$EXT/,readdir(CARDDIR));
  closedir(CARDDIR);
  foreach $item (@items)
   {
    if (-M "$BASEDIR/$item" > $DAYS)
     {
      unlink("$BASEDIR/$item");
     }
   }
 }



##################################################################
sub valid_address 
 {
  $testmail = $fields{'recip_email'};
  if ($testmail =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/ ||
  $testmail !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$/)
   {
     return 0;
   }
   else 
    {
      return 1;
    }
}


sub bad_email
{
print <<__STOP_OF_BADMAIL__;
Content-type: text/html

<FONT SIZE="+1">
<B>
SORRY! Your request could not be processed because of an improper
recipient's e-mail address. Please use your back button to return
to the card screen and try again!
</B>
</FONT>
__STOP_OF_BADMAIL__
}

sub test_basedir
{
  if (not -w $BASEDIR)
   {
print <<__STOP_OF_BADBASE__;
Content-type: text/html

<FONT SIZE="+1">
<B>
The script cannot either find or write to the<BR>
$BASEDIR directory. Please check this setting if
the BASEDIR variable, and the permissions of the
directory. If you have them set to 755, please 
change them to 777.
</B>
</FONT>
__STOP_OF_BADBASE__
exit;
   }
}

##################################################################
sub valid_page
 {
 if (@okaydomains == 0) {return;}
  $DOMAIN_OK=0;                                         
  $RF=$ENV{'HTTP_REFERER'};                             
  $RF=~tr/A-Z/a-z/;                                     
  foreach $ts (@okaydomains)                            
   {                                                    
     if ($RF =~ /$ts/)                                  
      { $DOMAIN_OK=1; }
   }                                                    
   if ( $DOMAIN_OK == 0)                                
     { print "Content-type: text/html\n\n Sorry, cant run it from here....";    
      exit;
     }                                                  
}

sub decode_vars
{
#This part of the program splits up our data and gets it
#ready for formatting.
  $i=0;
  read(STDIN,$temp,$ENV{'CONTENT_LENGTH'});
  @pairs=split(/&/,$temp);
  foreach $item(@pairs)
   {
    ($key,$content)=split(/=/,$item,2);
    $content=~tr/+/ /;
    $content=~s/%(..)/pack("c",hex($1))/ge;
    $content =~ s/<!--(.|\n)*-->//g;
    $fields{$key}=$content;
    $i++;
    $item{$i}=$key;
    $response{$i}=$content;
   }
}

sub get_file_name
{
   $proc=$$;
   $newnum=time;
   $newnum=substr($newnum,4,5);
   $date=localtime(time);  
   ($day, $month, $num, $time, $year) = split(/\s+/,$date); 
   $month=~tr/A-Z/a-z/;
   $PREF = "$month$num-";
   $FILE_NAME="$BASEDIR/$PREF$newnum$proc$EXT";
   $URL_NAME="$BASEURL/$PREF$newnum$proc$EXT";
}


#Write out our HTML FILE
sub create_file
{
  open(OUTFILE,">$FILE_NAME") ;
  print OUTFILE "$cardbody\n";
  close (OUTFILE);
}

#Set up our HTML Preview Form
sub do_preview
{
$fields{'the_message'} =~s/\"/\'/g;
  &pass_params;
  &make_body;
print "Content-type: text/html\n\n";
print "$cardbody\n";
}

sub main_driver
{
   &valid_page;
   &test_basedir;
   &decode_vars;

   if ($fields{'recip_email'} eq "")
     { &no_email; exit; } 
   if (&valid_address == 0)
    { &bad_email; exit; }
   if ($fields{'sender_email'} eq "")
     { &no_email; exit; }

   if ($fields{'background'} ne "")
    { $BODYTAG="<BODY BACKGROUND=\"$BASEURL/$fields{'background'}\">";}
     else { $BODYTAG="<BODY BGCOLOR=\"#FFFFFF\">"; }

   if ($fields{'action_code'} eq "NEW") 
     { &do_preview; }

   if ($fields{'action_code'} eq "SENDCARD") 
     {                             
      &make_body;
      &get_file_name;
      &create_file;
      &setup_letter;
      $mailresult=&sendmail($fields{sender_email}, $fields{sender_email}, $fields{recip_email}, $SMTP_SERVER, $SUBJECT, $msgtext); 
      &thank_you;
      if ($DAYS > 0)
       {&card_expire;}
     }

}
