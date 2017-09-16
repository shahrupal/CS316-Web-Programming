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

#if any of the required fields are blank, output error message
if(($origunits eq "") || ($convunits eq "") || ($numunits eq "") || ($convfactor eq "")){
	$error = 1;
	print "<html>error: one or more fields are blank</html>";
}

#if any of the fields are given a wrong parameter type, output error message
elsif(looks_like_number($origunits)){
	$error = 1;
	print "<html>error: original unit type field needs to be a string - instead, a numerical value was submitted</html>";
}
elsif(looks_like_number($convunits)){
	$error = 1;
	print "<html>error: new unit type field needs to be a string - instead, a numerical value was submitted</html>";
}
elsif(!looks_like_number($numunits)){
	$error = 1;
	print "<html>error: value to convert field needs to be a numerical value - instead, a string was submitted</html>";
}
elsif(!looks_like_number($convfactor)){
	$error = 1;
	print "<html>error: conversing factor field needs to be a numerical value - instead, a string was submitted</html>";
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

if($error == 0){
	print "<html><h2>New = $numunits</h2></html>";
}

#default conversing factor = 1
#at end of calculations, multiple $numunits by conversing factor
