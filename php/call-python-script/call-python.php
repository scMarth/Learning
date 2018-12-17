<?php 

$output=shell_exec('C:\path\python.exe C:\path\test.py one two 2>&1'); // 2>&1 will also print the error
echo "<pre>$output</pre>";

?>