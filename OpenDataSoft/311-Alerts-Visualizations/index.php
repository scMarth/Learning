<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>311 Alerts (QScend)</title>
    <link rel='icon' href='images/SalinasLogoTagline.png'>

    <link rel="stylesheet" href="https://js.arcgis.com/4.13/esri/themes/light/main.css"/>
    <link rel='stylesheet' href='./css/styles.css'>

    <?php include_once("./php/main.php") ?>

    <script src='./lib/Chart.bundle.min.js'></script>
    <script src='./js/colorGenerator.js'></script>
    <script src='./js/utils.js'></script>
</head>
<body>
    <div id='site-header'>
        <div class='salinas-logo'>
            <a href='https://www.cityofsalinas.org/' target='_blank'>
                <img class='image-logo' src='images/SalinasLogoTagline.png'>
            </a>
        </div>
    </div>

    <div class="text-panel">
        Total Requests: <?php echo $numRecords ?>
        <br>
        Total # of Open Requests: <?php echo $openRequests ?>
        <br>
        Total # of Closed Requests: <?php echo $closedRequests ?>
        <br>
        Total # of In-Progress Requests: <?php echo $inProgressRequests ?>
        <br>
        Total # of On-Hold Requests: <?php echo $onHoldRequests ?>
    </div>

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

<?php include_once("./php/generateCharts.php") ?>
<script src="https://js.arcgis.com/4.13/"></script>
<!-- Include Esri Map Visualizations -->
<script src='./js/districtMap.js'></script>
<script src='./js/departmentDotDensityMap.js'></script>
<script src='./js/originDotDensityMap.js'></script>
</body>
</html>