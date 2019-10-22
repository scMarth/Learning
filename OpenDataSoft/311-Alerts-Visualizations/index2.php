<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>311 Alerts (QScend)</title>
    <?php
        ini_set('display_errors', 1);
        ini_set('display_startup_errors', 1);
        error_reporting(E_ALL);
    
        //set POST variables
        $url = 'https://leicester.opendatasoft.com/api/records/1.0/download/';
        $fields = array('dataset' => urlencode('planning-permissions'), 'format' => urlencode('json'));

        // Method: POST, PUT, GET etc
        // Data: array("param" => "value") ==> index.php?param=value

        function CallAPI($method, $url, $data = false)
        {
            $curl = curl_init();

            switch ($method)
            {
                case "POST":
                    curl_setopt($curl, CURLOPT_POST, 1);

                    if ($data)
                        curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
                    break;
                case "PUT":
                    curl_setopt($curl, CURLOPT_PUT, 1);
                    break;
                default:
                    if ($data)
                        $url = sprintf("%s?%s", $url, http_build_query($data));
            }

            // Optional Authentication:
            curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
            curl_setopt($curl, CURLOPT_USERPWD, "username:password");

            curl_setopt($curl, CURLOPT_URL, $url);
            curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

            $result = curl_exec($curl);

            curl_close($curl);

            return $result;
        }

        var_dump(CallAPI('POST', $url, $fields));

    ?>
</head>
<body>
</body>
</html>