<!DOCTYPE html>
<html lang="en">
<head>
	<title>Máy tính tổng </title>
	<meta charset="utf-8"/>
	<meta name="viewport" content="width=device-width, initial-scale=1"/>
	<title></title>
</head>
<body>
	<form method="post" action="sum_blog.php">
		<h1>Tính Tổng</h1>
		<label>Nhập số nguyên: </label>
		<input type="text" name="number">
		<input type="submit" value="Calculate Sum">
	</form>

<?php 
	$num = $_GET['num'];
	$sum = $_GET['sum'];
	$date = $_GET['date'];
	echo "Previous result: <br> <strong>", $date, "</strong> You enter: ", $num , " result is: ", $sum;
?>

</body>
</html>