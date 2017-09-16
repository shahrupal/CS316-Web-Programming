#!/usr/bin/perl
use Scalar::Util qw(looks_like_number);

print "Content-type: text/html\n\n";

#splits multiple inputs into different strings
my @values = split(/&/, $ENV{QUERY_STRING});

#splits strings further so only input is left
foreach my $i (@values) {
	my($fieldname, $data) = split(/=/, $i);
	$FORM{$fieldname} = $data;
#######	print "$fieldname = $data<br>\n"; ########

}

#units in curly brackets are same as those in html file
#creates variables and stores user's input from form
$origunits = $FORM{origunits};
$convunits = $FORM{convunits};
$numunits = $FORM{numunits};
$convfactor = $FORM{convfactor};

my $original = $numunits;
$error = 0;



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



#output user's input
#blue = valid
#red = invalid
if(looks_like_number($origunits) || ($origunits eq "") || (choiceError($origunits) == 1)){
	$error = 1;
}
else{
	$error = 0;
}
printInput($origunits, "Original Unit Type", $error);

if(looks_like_number($convunits) || ($convunits eq "") || (choiceError($convunits) == 1)){
	$error = 1;
}
else{
	$error = 0;
}
printInput($convunits, "New Unit Type", $error);








#if there are no errors, print conversion in green
if($error == 0){
	print "<html><p style=\"color:green\">$original $origunits = $numunits $convunits</p></html>";
}
#if there are errors, call subroutines to determine and output specific error
else{
	dataTypeError($origunits, $convunits, $numunits, $convfactor);
	if((choiceError($origunits) == 1) || (choiceError($convunits) == 1)){ 
		print "<html><p style=\"color:red\">error: invalid units to be converted in red above</p></html>";
	}
}



#default conversing factor = 1
#at end of calculations, muiltiple $numunits by conversing factor




###SUBROUTINES###
#checks to see if user entered invalid string
sub choiceError{
	my $option = shift;
	if(($option ne "parsec") && ($option ne "lightyear") && ($option ne "kilometer") && ($option ne "xlarn") && ($option ne "galacticyear") && ($option ne "terrestrialyear") && ($option ne "xarnyear") && ($option ne "terrestrialminute")){
		return 1;
	}
	else{
		return 0;
	}		
}

#checks to see if user enters wrong data type for parameters
sub dataTypeError{
	my $original = shift;
	my $new = shift;
	my $value = shift;
	my $factor = shift;
	if(looks_like_number($original) || looks_like_number($new) || !looks_like_number($value) || !looks_like_number($factor)){
		print "<html><p style=\"color:red\">error: incorrect data type submitted for parameters in red above</p></html>";
	}
	else{
		print "";
	}
}

#print's user's input in red if invalid or blue if valid
sub printInput{
	$input = shift;
	$variable = shift;
	$color = shift;
	if($color == 0){
		print "<html><p style=\"color:blue\">$variable = $input</p></html>";
	}
	else{
		print "<html><p style=\"color:red\">$variable = $input</p></html>";
	}
}

