<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <?php

        $filename = 'test.csv';

        $csv = [];

        if (($h = fopen("{$filename}", "r")) !== FALSE){
            while (($data = fgetcsv($h, 1000, ",")) !== FALSE){
                $csv[] = $data;
            }
            fclose($h);
        }

        echo "<pre>";
        var_dump($csv);
        echo "</pre>";

    ?>
</body>
</html>