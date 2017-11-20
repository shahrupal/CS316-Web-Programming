<!--
Author: Rupal Shah
Grading Rubric:
a) implemented
b) implemented
c) implemented
d) implemented
e) implemented
f) implemented
BONUS:
g) implemented
-->


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

// check if json file is valid
if(json_last_error() == 0){
	inputValidation($json);
}
else{
	echo "<p>ERROR: json file is improper.</p>";
}

?>


<!--   INPUT VALIDATION FUNCTION  -->
<?php
function inputValidation($json){
	
	// if the user enters required fields
	if(isset($_GET['titlechoice']) && !empty($_GET['titlechoice']) && isset($_GET['resultchoice']) && !empty($_GET['resultchoice']) && isset($_GET['termchoice'])){
		// create boolean to store whether the inputted combination is valid
		$combination = false;

		// search for user input for result and pass key (.json file) associated with it to showResults function
		foreach($json['sport'] as $asport){
			if($asport['title'] == $_GET['titlechoice']){
				foreach($asport['results'] as $key=>$value){ 
		                	if($key == $_GET['resultchoice']){

						// check if json file is valid
						if(file_exists($value)){	
	
							// pass in new json file and search term selected by user
							showResults($value,$_GET['termchoice']);
						}
						else{
							echo "<p>ERROR: file does not exist.</p>";
						}

						// set valid combination to be true
						$combination = true;
					}
       		         	}

				// output if combination is nonexistent					
				if(!isset($value) || empty($value) || ($combination == false)){
					echo "<p>ERROR: this combination does not exist.</p>";
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

}
?>


<!--   SHOW RESULTS FUNCTION   -->
<?php
function showResults($file,$search){

	// store json information in string
	$subdata = file_get_contents($file);

	// store data in an array
	$subjson = json_decode($subdata, true);

	// create variables to store wins/losses data
	$win = 0;
	$loss = 0;
	$total = 0;
?>

<?php	// check if json file is valid
	if(json_last_error() != 0){
		echo "<p>ERROR: json file is improper.</p>";
	}
	else{
?>		
		<!-- SHOW COMMENTS AS HEADER -->
		<h2>
		<?php foreach($subjson['comments'] as $comments){
			echo $comments;
			echo " ";
		} ?>
		</h2>
	
		<!-- SHOW ALL GAME DATA -->
		<table width=100%>
	
		<?php foreach($subjson['games'] as $games){ ?>
	
			<tr>	
			<?php foreach($games as $key=>$val){ ?>		
				
				<?php if(empty($search) || ($key != $search)){ ?>
					<td><?php echo $key ?>:   <?php echo $val ?></td>    		
				<?php }
				// <!-- BOLD SEARCH TERMS --> //
				else{ ?>
					<td><b><?php echo $key ?>:  <?php echo $val ?></b></td>
				<?php } ?>
	
				<!-- COUNT NUMBER OF WINS/LOSSES -->
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
	
		<!-- OUTPUT SUMMARY OF WINS/LOSSES -->
		<h2>Games Won: <?php echo $win ?></h2>
		<h2>Games Lost: <?php echo $loss ?></h2>
		<h2>Total Number of Games Played: <?php echo $total ?></h2>
		<h2>% of Games Won: <?php echo round((100*$win/$total),2) ?></h2>
		<h2>% of Games Lost: <?php echo round((100*$loss/$total),2) ?></h2>

		<?php break;?>

	<?php } ?>
<?php } ?>


<!-- CREATE HTML FORM -->
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
