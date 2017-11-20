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

?>


<?php
// if the user enters required fields
if(isset($_GET['titlechoice']) && !empty($_GET['titlechoice']) && isset($_GET['resultchoice']) && !empty($_GET['resultchoice']) && isset($_GET['termchoice'])){

	// search for user input for result and return key (.json file) associated with it
	foreach($json['sport'] as $asport){
		if($asport['title'] == $_GET['titlechoice']){
			foreach($asport['results'] as $key=>$value){ 
	                	if($key == $_GET['resultchoice']){
			
					showResults($value,$_GET['termchoice']);

				}
                	}
		}	
	}

}

// if user does not enter required fields
else if(empty($_GET['titlechoice']) || empty($_GET['resultchoice'])){
	echo "Must choose from Title and Result list.";
}
else{
        echo "NOT SUBMITTED";
}
?>

<!--   SHOW RESULTS FUNCTION   -->
<?php
function showResults($file,$search){
	$subdata = file_get_contents($file);
	$subjson = json_decode($subdata, true);
?>

	<h2><?phpecho $search ?></h2>
	<!-- SHOW COMMENTS -->
	<h1>
	<?php foreach($subjson['comments'] as $comments){
		echo $comments;
		echo " ";
	} ?>
	</h1>

	<!-- SHOW GAMES -->
	<table width=100%>

	<?php foreach($subjson['games'] as $games){ ?>

		<tr>	
		<?php foreach($games as $key=>$val){ ?>		
			
			<?php if(empty($search) || ($key != $search)){ ?>
				<td><?php echo $key ?>:   <?php echo $val ?></td>    		
			<?php }
			// BOLD SEARCH TERMS
			else{ ?>
				<td><b><?php echo $key ?>:  <?php echo $val ?></b></td>
			<?php } ?>

		<?php } ?>
		</tr>

	<?php } ?>

	</table>
	<?php break;?>

<?php } ?>

<form action="" method="GET">

	<!-- drop-down list with all titles from .json file -->
	<select name="titlechoice">
		<option></option>
		<?php foreach($json['sport'] as $titlelist){ ?>
			<option><?php echo $titlelist['title'];?></option>
		<?php } ?>
	</select>

	<!-- drop-down list with all the results from .json file -->
	<select name="resultchoice">
		<option></option>
		<?php foreach($json['sport'] as $resultlist){ ?>
			<?php foreach($resultlist['results'] as $key=>$value){ ?>
				<option><?php echo $key?></option>
			<?php } ?>
		<?php } ?>
	</select>


	<!-- drop-down list with all the searchterms from .json file -->
	<select name="termchoice">
		<option></option>
		<?php foreach($json['sport'] as $searchlist){ ?>
			<?php foreach($searchlist['searchterms'] as $terms) { ?>
				<option><?php echo $terms;?></option>
			<?php } ?>
		<?php } ?>
	</select>

	

	<!-- submit button -->
	<input type="submit" value="submit">	

</form>


</body>
</html>
