#!/usr/bin/perl

#Authors: Rupal Shah, Petia Nikolova
#Sources: Professor Paul Linton's Notes (to retrieve data from html form)
        # perldoc.perl.org/Scalar/Util.html (for looks_like_number function)

use Scalar::Util qw(looks_like_number);

my @values = split(/&/, $ENV{QUERY_STRING});

#splits strings further so only input is left
foreach my $i (@values) {
        my($fieldname, $data) = split(/=/, $i);
        $FORM{$fieldname} = $data;
}


print "Content-type: text/html\n\n";

#splits multiple inputs into different strings
my @values = split(/&/, $ENV{QUERY_STRING});

#splits strings further so only input is left
foreach my $i (@values) {
	my($fieldname, $data) = split(/=/, $i);
	$FORM{$fieldname} = $data;
}

#units in curly brackets are same as those in html file
#creates variables and stores user's input from form
$origunits = $FORM{origunits};
$convunits = $FORM{convunits};
$numunits = $FORM{numunits};
$convfactor = $FORM{convfactor};


#create variables
$original = $numunits; #stores original value of numunits - mutation var can cause unexpected values
$error = 0; #checks if error and uses it to set font color of parameters
$overallError = 0; #checks if there is an error and uses it to set error messages
$indirectConv = 0; #checks to see if conversions are invalid


#----------- DIRECT CONVERSIONS ----------#

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

#no conversion - assume indirect
else{
	$indirectConv = 1;
}


#------------ OUTPUT USER'S INPUT -----------#

#output user's input for ORINIGAL UNIT TYPE
#check if there is an error - use this to set color of output text
if(looks_like_number($origunits) || ($origunits eq "") || (choiceError($origunits) == 1)){
	$error = 1;
	$overallError = 1;
}
else{
	$error = 0;
}
printInput($origunits, "Original Unit Type", $error);

#output user's input for NEW UNIT TYPE
#check if there is an error - use this to set color of output text
if(looks_like_number($convunits) || ($convunits eq "") || (choiceError($convunits) == 1)){
	$error = 1;
	$overallError = 1;
}
else{
	$error = 0;
}
printInput($convunits, "New Unit Type", $error);

#output user's input for VALUE TO CONVERT
#check if there is an error - use this to set color of output text
#use "original" variable, since "numunits" has been manipulated
if(!looks_like_number($original) || ($original eq "")){
	$error = 1;
	$overallError = 1;
}
else{
	$error = 0;
}
printInput($original, "Value to Convert", $error);

#output user's input for CONVERSING FACTOR
#check if there is an error - use this to set color of output text
if(!looks_like_number($convfactor) || ($convfactor eq "")){
	$error = 1;
	$overallError = 1;
}
else{
	$error = 0;
}
printInput($convfactor, "Conversing Factor", $error);



#----------- OUTPUT ERRORS ----------#

if($overallError == 0){
	#if there are no errors EXCEPT indirect conversion, output error
	#checks if no other errors bc the two choices could be strings but not any of the listed choices
	#this prevents output of error when it is not solely due to indirect conversion of valid choices
	if($indirectConv == 1){
		print "<html><p style=\"color:red\"><b>error: this tool does not account for indirect conversions</b></p></html>";
	}	
	else{
		#if there are absolutely no errors, multiply result by conversion factor and print out answer in green
		$numunits = $numunits*$convfactor;
		print "<html><p style=\"color:green\">$original $origunits = $numunits $convunits</p></html>";
	}
}
#if there are errors, call subroutines to determine and output specific error
else{
	dataTypeError($origunits, $convunits, $original, $convfactor);
	if((choiceError($origunits) == 1) || (choiceError($convunits) == 1)){ 
		print "<html><p style=\"color:red\"><b>error: one or more of the types of units to be converted are invalid</b></p></html>";
	}
	if(($origunits eq "") || ($convunits eq "") || ($original eq "") || ($convfactor eq "")){
		print "<html><p style=\"color:red\"><b>error: one or more of the required fields were left blank</b></p></html>";
	}
	if(indirectError($indirectConv,$origunits,$convunits) == 0){
		print "<html><p style=\"color:red\"><b>error: this tool does not account for indirect conversions</b></p></html>";
	}
}



#------------ SUBROUTINES --------------#

#checks to see if user entered invalid string (string not included in below options)
sub choiceError{
	my $option = shift;
	if(($option ne "parsec") && ($option ne "lightyear") && ($option ne "kilometer") && ($option ne "xlarn") && ($option ne "galacticyear") && ($option ne "terrestrialyear") && ($option ne "xarnyear") && ($option ne "terrestrialminute") && ($option ne "")){
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
	if(((looks_like_number($original)) && ($original ne "")) || ((looks_like_number($new)) && ($new ne "")) || ((!looks_like_number($value)) && ($value ne "")) || ((!looks_like_number($factor)) && ($factor ne ""))){
		print "<html><p style=\"color:red\"><b>error: incorrect data type submitted for one or more of the fields</b></p></html>";
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

#print out if there's an indirect conversion error
#returns 1 if "conversion error" is due to something else such as blank inputs or invalid options
#returns 0 if ACTUAL indirect conversion error
sub indirectError{
	$indConversion = shift;
	$original = shift;
	$new = shift;
	if(($original eq "") || ($new eq "")){
		return 1;
	}
	if(looks_like_number($original) || looks_like_number($new)){
		return 1;
	}
	if((choiceError($original) == 1) || (choiceError($new) == 1)){
		return 1;
	}
	if($indConversion == 1){
		return 0;
	}
	else{
		return 1;	
	}
}
