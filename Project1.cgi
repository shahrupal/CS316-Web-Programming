#!/usr/bin/perl
use Scalar::Util qw(looks_like_number);

print "Content-type: text/html\n\n";

#splits multiple inputs into different strings
my @values = split(/&/, $ENV{QUERY_STRING});

#splits strings further so only input is left
foreach my $i (@values) {
	my($fieldname, $data) = split(/=/, $i);
	$FORM{$fieldname} = $data;
	print "$fieldname = $data<br>\n";
}

#units in curly brackets are same as those in html file
#creates variables and stores user's input from form
$origunits = $FORM{origunits};
$convunits = $FORM{convunits};
$numunits = $FORM{numunits};
$convfactor = $FORM{convfactor};

$error = 0;

if(($origunits eq "") || ($convunits eq "") || ($numunits eq "") || ($convfactor eq "")){
	$error = 1;
	print "<html>error: one or more fields are blank</html>";
}

#parsec <--> lightyear
if(($origunits eq "parsec") && ($convunits eq "lightyear")){
	$numunits = $numunits*3.26;
}
elsif(($origunits eq "lightyear") && ($convunits eq "parsec")){
	$numunits = $numunits/3.26;
}

#lightyear <--> kilometer
elsif(($origunits eq "lightyear") && ($convunits eq "kilometer")){
	$numunits = $numunits*(3.086*(10**13));
}
elsif(($origunits eq "kilometer") && ($convunits eq "lightyear")){
	$numunits = $numunits/(3.086*(10**13));
}

#xlarn <--> parsec
elsif(($origunits eq "xlarn") && ($convunits eq "parsec")){
	$numunits = $numunits*7.3672;
}
elsif(($origunits eq "parsec") && ($convunits eq "xlarn")){
	$numunits = $numunits/7.3672;
}

#galacticyear <--> terrestrialyear
elsif(($origunits eq "galacticyear") && ($convunits eq "terrestrialyear")){
	$numunits = $numints*250000000;
}
elsif(($origunits eq "terrestrialyear") && ($convunits eq "galacticyear")){
	$numunits = $numunits/250000000;
}

#xarnyear <--> terrestrialyear
elsif(($origunits eq "xarnyear") && ($convunits eq "terrestrialyear")){
	$numunits = $numunits*1.2579;
}
elsif(($origunits eq "terrestrialyear") && ($convunits eq "xarnyear")){
	$numunits = $numunits/1.2579;
}

#terrestrialyear <--> terrestrialminute
elsif(($origunits eq "terrestrialyear") && ($convunits eq "terrestrialminute")){
	$numunits = $numunits*525600;
}
elsif(($origunits eq "terrestrialminute") && ($convunits eq "terrestrialyear")){
	$numunits = $numunits/525600; 
}

#check to see if the required fields are empty
#if(($origunits == "") || ($convunits == "") || ($numunits == "") || ($convfactor == "")){
#	$error = 1;
#	print "<html><font color="red">error: one or more fields are blank</font></html>"
#}

if($error == 0){
	print "<html><h2>New = $numunits</h2></html>";
}

#default conversing factor = 1
#at end of calculations, multiple $numunits by conversing factor
