<?php

# show errors
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

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
    echo "{$key} => {$value} ";
    print_r($arr);
    echo '<br>';
}

echo '<br><br>';

$arr1 = array(
    'adsf' => 1,
    'avfasdf' => 3,
    'bsgfhnyjt' => 3,
    '456ghw45' => 3,
    'dfghj' => 3,
    'qwreavsd' => 3,
    'oiuuio' => 3,
    'mn' => 3,
    'jhhj' => 3
);

$arr2 = array(
    'adsf' => 1,
    'tbre' => 3,
    '7ij' => 3,
    '5h' => 3,
    'dv' => 3,
    'fads' => 3
);

$arr3 = array(
    'adsf' => 1,
    'ghj' => 3,
    'klj' => 3,
    'sfgd' => 3,
    'oiu' => 3,
    'yui' => 3,
    'fyt' => 3,
    'yt' => 3,
    'yt' => 3
);

foreach (array($arr1, $arr2, $arr3) as $curr_array){
    ksort($curr_array);
    foreach ($curr_array as $key=>&$val){
        echo $key . ' => ' . $val . '<br>';
    }
    echo '<br><br>';
}

# the arrays are not sorted, because a temporary variable was sorted

foreach ($arr1 as $key=>&$val){
     echo $key . ' => ' . $val . '<br>';
}
echo '<br><br>';

foreach ($arr2 as $key=>&$val){
     echo $key . ' => ' . $val . '<br>';
}
echo '<br><br>';

foreach ($arr3 as $key=>&$val){
     echo $key . ' => ' . $val . '<br>';
}
echo '<br><br>';

echo '-----------------------------------------------------------------';

echo '<br><br>';

foreach (array(&$arr1, &$arr2, &$arr3) as &$curr_array){ # ampersands are needed in both
    ksort($curr_array);
    foreach ($curr_array as $key=>&$val){
        echo $key . ' => ' . $val . '<br>';
    }
    echo '<br><br>';
}

foreach ($arr1 as $key=>&$val){
     echo $key . ' => ' . $val . '<br>';
}
echo '<br><br>';

foreach ($arr2 as $key=>&$val){
     echo $key . ' => ' . $val . '<br>';
}
echo '<br><br>';

foreach ($arr3 as $key=>&$val){
     echo $key . ' => ' . $val . '<br>';
}
echo '<br><br>';

?>