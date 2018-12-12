<html>
<head>
    <link rel="stylesheet" href="https://js.arcgis.com/4.9/esri/css/main.css">
    <script src="https://js.arcgis.com/4.9/"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>

<body>
    <div id="outDiv"></div>

    <script>
        var outDiv = $('#outDiv')[0];

        require(["esri/tasks/Locator"], function(Locator){

        locator = new Locator("https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer");

        singleLineAddr = <?php echo '"' . $_GET['Address'] . '"'; ?> + " salinas CA";

        address = {
            SingleLine: singleLineAddr
        };
        var options = {
            address: address,
            outFields: ["*"]
        };

        locator.addressToLocations(options).then(function(evt){
            outHTML = "";

            if (evt.length != 1){
                outHTML = "Ambiguous Address, please try again.";
            }else{
                foundAddr = evt[0].address;
                loc = evt[0].location;

                lat = loc.latitude;
                long = loc.longitude;

                outHTML += "Address: " + foundAddr + "<br>";
                outHTML += "Latitude: " + lat + "<br>";
                outHTML += "Longitude: " + long + "<br>";
            }

            outDiv.insertAdjacentHTML('beforeend', outHTML);

            console.log(evt);
            console.log(evt[0]);
        });

        });
    </script>
</body>
</html>