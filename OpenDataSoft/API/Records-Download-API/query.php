<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <?php
        ini_set('display_errors', 1);
        ini_set('display_startup_errors', 1);
        error_reporting(E_ALL);

        //set POST variables
        $url = 'https://leicester.opendatasoft.com/api/records/1.0/download/';
        // $url = 'http://leicester.opendatasoft.com/api/records/1.0/download/';
        $data = array('dataset' => urlencode('planning-permissions'), 'format' => urlencode('json'));

        // use key 'http' even if you send the request to https://...
        $options = array(
            'http' => array(
                'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
                'method'  => 'POST',
                'content' => http_build_query($data)
            )
        );
        $context  = stream_context_create($options);
        $result = file_get_contents($url, false, $context);
        if ($result === FALSE) { /* Handle error */ }

        var_dump($result);

    ?>
</head>
<body>
</body>
</html>