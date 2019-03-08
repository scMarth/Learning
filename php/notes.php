<?php

# hashmaps
$array = array();

$array[0] = 'Hello';
$array[2] = 'Hello2';
print_r($array);

$test = array('test'=>array());
echo '<br>';

// works as expected
// foreach($test as $key=>$val){
//     array_push($test[$key], 'the quick brown fox'); // works as expected
// }

// modify the array by reference
// https://stackoverflow.com/questions/10810225/modify-an-array-by-reference
foreach($test as $key=>&$val){
    array_push($val, 'val by reference');
}
print_r($test);
echo '<br>';


$arr = array('the', 'quick', 'brown', 'fox', 'jumps');
print_r($arr);
if (in_array('the', $arr)){
    echo 'Found';
}else{
    echo 'Not found';
}
echo '<br>';
echo '<br>';

// http://php.net/manual/en/control-structures.foreach.php
// see the warning
$arr = array(1, 2, 3, 4);
foreach ($arr as &$value) {
    $value = $value * 2;
}
print_r($arr);
echo '<br><br>';

// $arr is now array(2, 4, 6, 8)

// without an unset($value), $value is still a reference to the last item: $arr[3]

foreach ($arr as $key => $value) {
    // $arr[3] will be updated with each value from $arr...
    echo "{$key} => {$value} ";
    print_r($arr);
    echo '<br>';
}
// ...until ultimately the second-to-last value is copied onto the last value


// fixed:
echo '<br><br>';
$arr = array(1, 2, 3, 4);
foreach ($arr as &$value) {
    $value = $value * 2;
}
print_r($arr);
echo '<br><br>';
unset($value);
foreach ($arr as $key => $value) {
    // $arr[3] will be updated with each value from $arr...
    echo "{$key} => {$value} ";
    print_r($arr);
    echo '<br>';
}
// ...until ultimately the second-to-last value is copied onto the last value

?>