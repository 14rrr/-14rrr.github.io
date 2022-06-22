<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>PHP Variables, Condition, and loop</title>
</head>
<body>

<?php 
	include ("function_blog.php");
?>

<h1>Kết Quả</h1>

<?php
	if (isset($_POST["number"])) {
		$num = $_POST["number"];
		if (isPositiveInt($num)) {
			$sum = calculateSum($num);
			echo "Tổng các số tự nhiên từ 1 đến " , $num , " là: <strong>" , $sum , "</strong>";
		} else {
			echo "please input an interger";
		}
	} else {
		echo "check return file sun_calculate.html";
	} 
?>


<?php 
	// session_start();
	date_default_timezone_set('Asia/Ho_Chi_Minh');
	$date = date('m/d/Y h:i:s a', time());
	echo "<p><a href='sum_calculater_blog.php?num= $num & sum= $sum & date= $date'>Return</a></p>";
?>

</body>
</html> 