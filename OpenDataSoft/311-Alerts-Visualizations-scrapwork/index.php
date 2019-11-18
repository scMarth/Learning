<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>311 Alerts (QScend)</title>
    <link rel='icon' href='images/SalinasLogoTagline.png'>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

    <link rel="stylesheet" href="https://js.arcgis.com/4.13/esri/themes/light/main.css"/>
    <link rel='stylesheet' href='./css/styles.css'>
</head>
<body>
    <div id="loader-container">
        <div id="logo">
            City of Salinas GIS Services
        </div>
        <div id="loader-frame">
            <div id="loader-white"></div>
            <div id="loader-red"></div>
            <div id="loader-green"></div>
            <div id="loader-blue"></div>
            <div id="loader-purple"></div>
        </div>
    </div>

    <div style="display:none;" id="page-content-container">
        <div id='site-header'>
            <div class='salinas-logo'>
                <a href='https://www.cityofsalinas.org/' target='_blank'>
                    <img class='image-logo' src='images/SalinasLogoTagline.png'>
                </a>
            </div>
        </div>

        <div id="totals" class="text-panel"></div>

        <div class="panels">
            <div class="panel">
                <div class="canvas-container">
                    <canvas id="status-requests"></canvas>
                </div>
            </div>
            <div class="panel">
                <div class="esri-map-container">
                    <div class="esri-map-div esri-map-dot-density-legend" id="department-dot-density-map"></div>
                </div>
                <div class="canvas-container">
                    <canvas id="department-requests"></canvas>
                </div>
                <div class="canvas-container">
                    <canvas id="department-hours"></canvas>
                </div>
                <div class="canvas-container">
                    <canvas id="department-avg-hours"></canvas>
                </div>
                <div class="canvas-container">
                    <canvas id="department-request-timeline"></canvas>
                </div>
            </div>
            <div class="panel">
                <div class="esri-map-container">
                    <div class="esri-map-div" id="district-map"></div>
                </div>
                <div class="canvas-container">
                    <canvas id="district-requests"></canvas>
                </div>
                <div class="canvas-container">
                    <canvas id="district-hours"></canvas>
                </div>
                <div class="canvas-container">
                    <canvas id="district-avg-hours"></canvas>
                </div>
                <div class="canvas-container">
                    <canvas id="district-request-timeline"></canvas>
                </div>
            </div>
            <div class="panel">
                <div class="big-canvas-container">
                    <canvas id="typename-requests"></canvas>
                </div>
                <div class="big-canvas-container">
                    <canvas id="typename-hours"></canvas>
                </div>
                <div class="big-canvas-container">
                    <canvas id="typename-avg-hours"></canvas>
                </div>
                <div class="big-canvas-container">
                    <canvas id="typename-request-timeline"></canvas>
                </div>
            </div>
            <div class="panel">
                <div class="esri-map-container">
                    <div class="esri-map-div esri-map-dot-density-legend" id="origin-dot-density-map"></div>
                </div>
                <div class="canvas-container">
                    <canvas id="origin-requests"></canvas>
                </div>
                <div class="canvas-container">
                    <canvas id="origin-hours"></canvas>
                </div>
                <div class="canvas-container">
                    <canvas id="origin-avg-hours"></canvas>
                </div>
                <div class="canvas-container">
                    <canvas id="origin-request-timeline"></canvas>
                </div>
            </div>
        </div>
    </div>

    <script src='./lib/Chart.bundle.min.js'></script>
    <script src='./js/colorGenerator.js'></script>
    <script src='./js/utils.js'></script>
    <script>
        function stopLoadingScreen(){
            // make the loading screen fade out
            $('#loader-container').css("animation", "fadeout 1s");
            // wait 1 second before turning the display property of the loading screen to none
            setTimeout(function(){
                $('#loader-container').css("display", "none");
            }, 1000);
            // display page contents
            $('#page-content-container').css("display", "block");
        }

        // $.post("./php/main.php", function(data){
        //     generateCharts(JSON.parse(data));
        //     setTotals(JSON.parse(data));
        //     stopLoadingScreen();
        // });

        $.getJSON("./json/visualization_data_cached.json", function(data){
            generateCharts(data);
            setTotals(data);
            stopLoadingScreen();
        });

        function setTotals(data){
            outHTML = "Total Requests: " + data.numRecords + "<br>"
                + "Total # of Open Requests: " + data.openRequests + "<br>"
                + "Total # of Closed Requests: " + data.closedRequests + "<br>"
                + "Total # of In-Progress Requests: " + data.inProgressRequests + "<br>"
                + "Total # of On-Hold Requests: " + data.onHoldRequests;
            $('#totals').html(outHTML);
        }

        function generateCharts(data){
            generateDoughnutChartFromPhpArray(
                data.requestStatusFreq,
                'Request Status',
                'status-requests',
                true
            );

            generatePieChartFromPhpArray(
                data.departmentFreq,
                'Total number of requests per department',
                'department-requests',
                true
            );

            generatePieChartFromPhpArray(
                data.departmentHours,
                'Total request hours per department (incomplete requests excluded)',
                'department-hours',
                true
            );

            generateHorizontalBarChartFromPhpArray(
                data.avgDepartmentHours,
                'Average hours per request for each department (incomplete requests excluded)',
                'department-avg-hours',
                'hours',
                true
            );

            // department timeline
            generateLineChartFromPhpData(
                data.departmentDatasets,
                'Department requests over time',
                'department-request-timeline',
                'start date',
                '# requests',
                true
            );

            generatePieChartFromPhpArray(
                data.districtFreq,
                'Total number of requests per district',
                'district-requests',
                true
            );

            generatePieChartFromPhpArray(
                data.districtHours,
                'Total request hours per district (incomplete requests excluded)',
                'district-hours',
                true
            );

            generateHorizontalBarChartFromPhpArray(
                data.avgDistrictHours,
                'Average hours per request for each district (incomplete requests excluded)',
                'district-avg-hours',
                'hours',
                true
            );

            // district timeline
            generateLineChartFromPhpData(
                data.districtDatasets,
                'District requests over time',
                'district-request-timeline',
                'start date',
                '# requests',
                true
            );

            generateHorizontalBarChartFromPhpArray(
                data.typenameFreq,
                'Total number of requests per typename',
                'typename-requests',
                '# requests',
                false
            );

            generateHorizontalBarChartFromPhpArray(
                data.typenameHours,
                'Total request hours per typename (incomplete requests excluded)',
                'typename-hours',
                'hours',
                false
            );

            generateHorizontalBarChartFromPhpArray(
                data.avgTypenameHours,
                'Average hours per request for each typename (incomplete requests excluded)',
                'typename-avg-hours',
                'hours',
                false
            );

            // typename timeline
            generateLineChartFromPhpData(
                data.typenameDatasets,
                'Typename requests over time',
                'typename-request-timeline',
                'start date',
                '# requests',
                false
            );

            generatePieChartFromPhpArray(
                data.originFreq,
                'Total number of requests per origin',
                'origin-requests',
                true
            );

            generatePieChartFromPhpArray(
                data.originHours,
                'Total request hours per origin (incomplete requests excluded)',
                'origin-hours',
                true
            );

            generateHorizontalBarChartFromPhpArray(
                data.avgOriginHours,
                'Average hours per request for each origin (incomplete requests excluded)',
                'origin-avg-hours',
                'hours',
                true
            );

            // department timeline
            generateLineChartFromPhpData(
                data.originDatasets,
                'Origin requests over time',
                'origin-request-timeline',
                'start date',
                '# requests',
                true
            );
        }
    </script>
    <script src="https://js.arcgis.com/4.13/"></script>
    <!-- Include Esri Map Visualizations -->
    <script src='./js/districtMap.js'></script>
    <script src='./js/departmentDotDensityMap.js'></script>
    <script src='./js/originDotDensityMap.js'></script>
</body>
</html>