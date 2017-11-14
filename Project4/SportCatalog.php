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

echo '<pre>'; print_r($json); echo '</pre>';

?>

<!-- drop-down list with all titles from .json file -->
<select>
	<option>--Select Sport--</option>
	<?php foreach($json['sport'] as $titlelist){ ?>
		<option><?php echo $titlelist['title'];?></option>
	<?php } ?>
</select>

<!-- drop-down list with all the results from .json file -->
<select>
	<option>--Select File--</option>
	<?php foreach($json['sport'] as $resultlist){ ?>
		<?php foreach($resultlist['results'] as $key=>$value){ ?>
			<option><?php echo $key?></option>
		<?php } ?>
	<?php } ?>
</select>


<!-- drop-down list with all the searchterms from .json file -->
<select>
	<option>--Select Search Terms--</option>
	<?php foreach($json['sport'] as $searchlist){ ?>
		<?php foreach($searchlist['searchterms'] as $terms) { ?>
			<option><?php echo $terms;?></option>
		<?php } ?>
	<?php } ?>
</select>

</body>
</html>
