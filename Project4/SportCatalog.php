<!DOCTYPE html>
<html>
<body>

<?php

// store information from .json file into string
$data = file_get_contents("Sports.json");

// store data as an array
$json = json_decode($data, true);

//echo '<pre>'; print_r($json); echo '</pre>';
echo "My first PHP script!";

?>

</body>
</html>
