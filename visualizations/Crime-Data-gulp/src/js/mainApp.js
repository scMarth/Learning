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

$.getJSON("./json/visualization_data_cached.json", function(data){
    generateCharts(data);
    setTotals(data);
    stopLoadingScreen();
}).fail(function(){
    stopLoadingScreen();
    showErrorScreen();
});

function showErrorScreen(){
    $('#page-content-container > div:gt(0)').remove();
    $('#page-content-container').append('<div class="text-panel-error">The site is being updated or down for maintenance, please check again later.</div>');
}

function setTotals(data){
    outHTML = "Total Records: " + data.numRecords;
    $('#totals').html(outHTML);
}

function generateCharts(data){
    generateLineChartFromPhpData(
        data.allCrimeDatasets,
        'Timeline for all crimes',
        'all-crime-timeline',
        'start date',
        '# records',
        true,
        [
            "rgb(0,0,0)"
        ]
    );

    generateLineChartFromPhpData(
        data.crimesPerMonth,
        'Crimes per month over time',
        'crimes-per-month-timeline',
        'month started',
        '# records',
        true,
        [
            "rgb(0,0,0)"
        ]
    );

    generateLineChartFromPhpData(
        data.gangRptDatasets,
        'Gang-related and non-gang-related crimes over time',
        'gang-rpt-timeline',
        'start date',
        '# records',
        true,
        [
            "rgb(0,0,0)",
            "rgb(255,0,0)"
        ]
    );

    generatePieChartFromPhpArray(
        data.gangRptFreq,
        'Breakdown of gang-related and non-gang-related crimes',
        'gang-rpt-pie-chart',
        true,
        [
            "rgb(0,0,0)",
            "rgb(255,0,0)"
        ]
    );

    generateLineChartFromPhpData(
        data.categoryDatasets,
        'Crimes over time by category',
        'category-timeline',
        'start date',
        '# records',
        true,
        null
    );

    generateHorizontalBarChartFromPhpArray(
        data.categoryFreq,
        'Total number of crimes per category',
        'category-chart',
        '# records',
        true,
        null
    );

    let districtColors = getFirstNColors(12);
    districtColors.push('#000000');
    generatePieChartFromPhpArray(
        data.beatFreq,
        'Breakdown of crimes by police beat districts',
        'police-beat-pie-chart',
        true,
        districtColors
    );            

    generateLineChartFromPhpData(
        data.beatDatasets,
        'Crimes over time by police beat district',
        'police-beat-timeline',
        'start date',
        '# records',
        true,
        districtColors
    );            

    generateHorizontalBarChartFromPhpArray(
        data.crimeDescFreq,
        'Total number of crimes per crime description',
        'crime-desc-chart',
        '# records',
        false,
        null
    );

    generateLineChartFromPhpData(
        data.crimeDescDatasets,
        'Crimes over time by crime description',
        'crime-desc-timeline',
        'start date',
        '# records',
        false,
        null
    );

    generateHorizontalBarChartFromPhpArray(
        data.classDescFreq,
        'Total number of crimes per class description',
        'class-desc-chart',
        '# records',
        true,
        null
    );

    generateLineChartFromPhpData(
        data.classDescDatasets,
        'Crimes over time by class description',
        'class-desc-timeline',
        'start date',
        '# records',
        false,
        null
    );

    generateDoughnutChartFromPhpArray(
        data.arrestMadeFreq,
        'Arrests made',
        'arrest-made-chart',
        true,
        [
            "rgb(0,0,0)",
            "rgb(255,0,0)"
        ]
    );

    generateLineChartFromPhpData(
        data.arrestMadeDatasets,
        'Arrests made over time',
        'arrest-made-timeline',
        'start date',
        '# records',
        true,
        [
            "rgb(0,0,0)",
            "rgb(255,0,0)"
        ]
    );

    generateVerticalBarChartFromPhpArray(
        data.victimAgesFreq,
        'Distribution of victim ages',
        'victim-ages-distribution',
        'age',
        '# victims',
        true,
        null
    );

    generateVerticalBarChartFromPhpArray(
        data.suspectAgesFreq,
        'Distribution of suspect ages',
        'suspect-ages-distribution',
        'age',
        '# suspects',
        true,
        null
    );
}