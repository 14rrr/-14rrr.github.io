<?php
function calculateSum($num) {
	$i = 1;
	$sum = 0;
	while ($i <= $num) {
		$sum += $i;
		$i += 1;
	}
	return $sum;
}

function isPositiveInt($num) {
	$result = false;
	if (is_numeric($num)) {
		if (floor($num) == $num) {
			$result = true;
		} else {
			echo "please enter an interger";
		}
	}
	return $result;
}
?>