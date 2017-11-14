<!DOCTYPE html>
<html>
<head>
<title>Sports Information</title>
</head>
<body>

<h1>SPORTS!</h1>

<?php

// store information from .json file into string
$data = file_get_contents("Sports.json");

// store data as an array
$json = json_decode($data, true);

// prints out each title in .json file
foreach($json['sport'] as $mydata){
	echo $mydata['title'];
}

//echo '<pre>'; print_r($json); echo '</pre>';
//echo "My first PHP script!";

?>

<!-- drop-down list with all titles from .json file -->
<select name="title">
	<?php foreach($json['sport'] as $mydata){ ?>
		<option><?php echo $mydata['title']; ?></option>
	<?php } ?>
</select>

</body>
</html>
