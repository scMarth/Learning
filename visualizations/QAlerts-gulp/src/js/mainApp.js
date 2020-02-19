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

function showErrorScreen(){
    $('#page-content-container > div:gt(0)').remove();
    $('#page-content-container').append('<div class="text-panel-error">The site is being updated or down for maintenance, please check again later.</div>');
}

function setTotals(data){
    outHTML = "Total Requests: " + data.numRecords + "<br>" +
        "Total # of Open Requests: " + data.openRequests + "<br>" +
        "Total # of Closed Requests: " + data.closedRequests + "<br>" +
        "Total # of In-Progress Requests: " + data.inProgressRequests + "<br>" +
        "Total # of On-Hold Requests: " + data.onHoldRequests;
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
        'Total number of requests per typename (Parked More Than 3 Days (Public Property) requests excluded)',
        'typename-requests',
        '# requests',
        false
    );

    generateHorizontalBarChartFromPhpArray(
        data.typenameHours,
        'Total request hours per typename (Parked More Than 3 Days (Public Property), Tree Trimming, incomplete requests excluded)',
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
    var typenameRequestsOverTime = generateLineChartFromPhpData(
        data.typenameDatasets,
        'Typename requests over time',
        'typename-request-timeline',
        'start date',
        '# requests',
        false
    );

    // hide Parked More Than 3 Days (Public Property) initially so that it doesn't mess up the scale
    typenameRequestsOverTime.getDatasetMeta(117).hidden = true;
    typenameRequestsOverTime.update();

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

    generateHorizontalBarChartFromPhpArray(
        data.parkedOver3DaysPerDistrict,
        'Parked More Than 3 Days (Public Property) per district',
        'parked-over-3-days-per-district-chart',
        '# requests',
        true
    );
}

console.log('hello?');

function loadJSToHead(url){
    var script = window.document.createElement('script');
    script.src = url;
    script.async = false;
    document.getElementsByTagName("head")[0].appendChild(script);
}

function loadJSToBody(url){
    console.log('loadJS');
    console.log(url);
    var ref = window.document.getElementsByTagName('body')[0].getElementsByTagName('script')[0];


    console.log(ref);
    var script = window.document.createElement('script');
    script.src = url;
    script.async = false;
    ref.insertBefore(ref, script);
}

function loadCSS(url){
    var el = document.createElement("link");
    el.setAttribute("rel", "stylesheet");
    el.setAttribute("type", "text/css");
    el.setAttribute("href", url);
    document.getElementsByTagName("head")[0].appendChild(el);
}

// loadJSToBody('https://js.arcgis.com/4.13/');
// loadJSToBody('./lib/Chart.bundle.min.js');

// loadJSToHead('./lib/jquery-3.4.1.min.js');

loadCSS('https://js.arcgis.com/4.13/esri/themes/light/main.css');
loadCSS('./css/app.styles.min.css');

$.getJSON("./json/visualization_data_cached.json", function(data){
    generateCharts(data);
    setTotals(data);
    stopLoadingScreen();
}).fail(function(){
    stopLoadingScreen();
    showErrorScreen();
});
