<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test</title>
    <?php

        ini_set('display_errors', 1);
        ini_set('display_startup_errors', 1);
        ini_set('memory_limit', '-1');
        date_default_timezone_set('America/Los_Angeles');

        $testVar = null;

        if ($testVar){
            echo 'var exists';
        }else{
            echo 'var doesn\'t exist';
        }

        $department = $district = $typename= $record = $tsClosed = $tsAdded = $hoursBetween = null;

        echo '<br><br>';
        $dt = new DateTime();
        $test = $dt->getTimeStamp();        
        echo $test;
        echo '<br><br>';

        var_dump($test);

        var_dump(localtime($test, true));

        /*
            Converts a Unix timestamp to a human readable string in the local timezone.
            Don't forget to set the timezone: date_default_timezone_set('America/Los_Angeles');

            struct tm {
               int tm_sec;         // seconds,  range 0 to 59
               int tm_min;         // minutes, range 0 to 59
               int tm_hour;        // hours, range 0 to 23
               int tm_mday;        // day of the month, range 1 to 31
               int tm_mon;         // month, range 0 to 11
               int tm_year;        // The number of years since 1900
               int tm_wday;        // day of the week, range 0 to 6
               int tm_yday;        // day in the year, range 0 to 365
               int tm_isdst;       // daylight saving time   
            };

        */
        function timestampToString($timestamp){
            $lt = localtime($timestamp, true);
            $string = ($lt['tm_mon']+1) . '/' . $lt['tm_mday'] . '/' . ($lt['tm_year']+1900) . ' ' . $lt['tm_hour']
                . ':' . $lt['tm_min'] . ':' . $lt['tm_sec'];
            return $string;
        }

        echo '<br><br>';
        echo timestampToString($test);


    ?>
</head>
<body>

</body>
</html>