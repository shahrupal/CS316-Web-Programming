<!DOCTYPE html>
<html>
<head>
<title>Sports Information</title>
</head>
<body>

<h1>Sports Catalog!</h1>

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
					if(file_exists($value)){	
						showResults($value,$_GET['termchoice']);
					}
					else{
						echo "<p>ERROR: file does not exist.</p>";
					}
				}
                	}
		}	
	}
}

// if user does not enter required fields
else if(empty($_GET['titlechoice']) || empty($_GET['resultchoice'])){
	echo "<p>REQUIRED: choose a title and result.</p>";
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
	$win = 0;
	$loss = 0;
	$total = 0;
?>

	<h2><?phpecho $search ?></h2>
	<!-- SHOW COMMENTS -->
	<h2>
	<?php foreach($subjson['comments'] as $comments){
		echo $comments;
		echo " ";
	} ?>
	</h2>

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

			<!-- WIN/LOSS PERCENTAGES -->
			<?php if($key == "WinorLose"){
				if($val == "W"){
					$win = $win + 1;
				}
				else{
					$loss = $loss + 1;
				}
				$total = $total + 1;
			}?>

		<?php } ?>
		</tr>		
			
	<?php } ?>

	</table>
	
	<!-- SUMMARY OF WINS/LOSSES -->
	<h2>Games Won: <?php echo $win ?></h2>
	<h2>Games Lost: <?php echo $loss ?></h2>
	<h2>Total Number of Games Played: <?php echo $total ?></h2>
	<h2>% of Games Won: <?php echo round((100*$win/$total),2) ?></h2>
	<h2>% of Games Lost: <?php echo round((100*$loss/$total),2) ?></h2>

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
