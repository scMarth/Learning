function getFirstNColors(num){
    colors = [
        "#ff6384",
        "#ff9f40",
        "#ffcd56",
        "#4bc0c0",
        "#36a2eb",
        "#9966ff",
        "#c9cbcf",
        "#ffb0c0",
        "#ffc58d",
        "#ffe4a3",
        "#84d4d4",
        "#7cc2f2",
        "#ccb3ff",
        "#a1a4ab",
        "#ff1748",
        "#f37900",
        "#ffb60a",
        "#318d8d",
        "#137bc1",
        "#661aff",
        "#787d87",
        "#c9002b",
        "#a65300",
        "#bc8400",
        "#1e5454",
        "#0c4f7c",
        "#4400cc",
        "#54585f",
        "#7d001a",
        "#5a2d00",
        "#704f00",
        "#0a1c1c",
        "#052236",
        "#2b0080",
        "#404042"
    ];

    if (num > colors.length)
        // return generateSortedColorStrings(num);
        return generateColorStrings(num).reverse();
    return colors.splice(0, num).reverse();
}

// convert hex to Rgb
// https://stackoverflow.com/questions/5623838/rgb-to-hex-and-hex-to-rgb
function hexToRgb(hex){
    let result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}

// function getFirstNColors(num){
//     return generateColorStrings(num).reverse();
// }

function splitIntoDataAndLabels(phpArray){
    let data = [];
    let labels = [];
    for (let key in phpArray){
        data.push(phpArray[key]);
        labels.push(key);
    }
    return [data, labels];
}

function generatePieChartFromPhpArray(phpArray, titleStr, canvasId, maintainAspectRatio, specifiedColors){
    let dataAndLabels = splitIntoDataAndLabels(phpArray);
    let colors = null;

    if (!specifiedColors){
        colors = getFirstNColors(dataAndLabels[0].length);
    }else{
        colors = specifiedColors;
    }

    let config = {
        type: 'pie',
        data: {
            datasets: [{
                data: dataAndLabels[0],
                backgroundColor: colors,
            }],
            labels: dataAndLabels[1]
        },
        options: {
            maintainAspectRatio: maintainAspectRatio,
            responsive: true,
            title: {
                display: true,
                text: titleStr
            }
        }
    };

    pieChart = new Chart(document.getElementById(canvasId).getContext('2d'), config);
}

function generateDoughnutChartFromPhpArray(phpArray, titleStr, canvasId, maintainAspectRatio, specifiedColors){
    let dataAndLabels = splitIntoDataAndLabels(phpArray);
    let colors = null;

    if (!specifiedColors){
        colors = getFirstNColors(dataAndLabels[0].length);
    }else{
        colors = specifiedColors;
    }

    let config = {
        type: 'doughnut',
        data: {
            datasets: [{
                data: dataAndLabels[0],
                backgroundColor: colors,
            }],
            labels: dataAndLabels[1]
        },
        options: {
            maintainAspectRatio: maintainAspectRatio,
            responsive: true,
            title: {
                display: true,
                text: titleStr
            }
        }
    };

    doughnutChart = new Chart(document.getElementById(canvasId).getContext('2d'), config);
}

function generateVerticalBarChartFromPhpArray(phpArray, titleStr, canvasId, xAxisLabel, yAxisLabel, maintainAspectRatio, specifiedColors){
    let dataAndLabels = splitIntoDataAndLabels(phpArray);
    let colors = null;

    if (!specifiedColors){
        colors = getFirstNColors(dataAndLabels[0].length);
    }else{
        colors = specifiedColors;
    }

    let config = {
        type: 'bar',
        data: {
            datasets: [{
                data: dataAndLabels[0],
                backgroundColor: colors,
            }],
            labels: dataAndLabels[1]
        },
        options: {
            maintainAspectRatio: maintainAspectRatio,
            legend: {
                display: false
            },
            responsive: true,
            title: {
                display: true,
                text: titleStr
            },
            scales: {
                xAxes: [{
                    ticks: {
                        autoSkip: false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: xAxisLabel
                    }
                }],
                yAxes: [{
                    ticks: {
                        min: 0
                    },
                    scaleLabel: {
                        display: true,
                        labelString: yAxisLabel
                    }
                }]
            }
        }
    };

    verticalBarChart = new Chart(document.getElementById(canvasId).getContext('2d'), config);
}

function generateHorizontalBarChartFromPhpArray(phpArray, titleStr, canvasId, xAxisLabel, maintainAspectRatio, specifiedColors){
    let dataAndLabels = splitIntoDataAndLabels(phpArray);
    let colors = null;

    if (!specifiedColors){
        colors = getFirstNColors(dataAndLabels[0].length);
    }else{
        colors = specifiedColors;
    }

    
    let config = {
        type: 'horizontalBar',
        data: {
            datasets: [{
                data: dataAndLabels[0],
                backgroundColor: colors,
            }],
            labels: dataAndLabels[1]
        },
        options: {
            maintainAspectRatio: maintainAspectRatio,
            legend: {
                display: false
            },
            responsive: true,
            title: {
                display: true,
                text: titleStr
            },
            scales: {
                xAxes: [{
                    ticks: {
                        min: 0
                    },
                    scaleLabel: {
                        display: true,
                        labelString: xAxisLabel
                    }
                }]
            }
        }
    };

    horizontalBarChart = new Chart(document.getElementById(canvasId).getContext('2d'), config);
}

function generateLineChartFromPhpData(phpArray, titleStr, canvasId, xAxisLabel, yAxisLabel, maintainAspectRatio, specifiedColors){
    let colors = null;

    if (!specifiedColors){
        let datasetCount = 0;
        for (let key in phpArray){
            if (key != 'dates'){
                datasetCount++;
            }
        }
        colors = getFirstNColors(datasetCount);
    }else{
        colors = specifiedColors;
    }

    let datasets = [];
    let colorInd = 0;
    for (let key in phpArray){
        if (key != 'dates'){
            let dataset = {
                label: key,
                data: phpArray[key],
                backgroundColor: colors[colorInd],
                borderColor: colors[colorInd++],
                // steppedLine: true,
                pointRadius: 2,
                fill: false
            };
            datasets.push(dataset);
        }
    }

    let config = {
        type: 'line',
        data: {
            labels: phpArray.dates,
            datasets: datasets,                    
        },
        options: {
            hover: {
                animationDuration: 0
            },
            tooltips: {
                intersect: false
            },
            elements: {
                line: {
                    tension: 0 // disable bezier curves
                },
                point: {
                    pointStyle: 'line' // don't show dots for points
                }
            },
            maintainAspectRatio: maintainAspectRatio,
            title: {
                display: true,
                text: titleStr
            },
            responsive: true,
            scales: {
                yAxes: [{
                    ticks: {
                        min: 0
                    },
                    scaleLabel: {
                        display: true,
                        labelString: yAxisLabel
                    }
                }],
                xAxes: [{
                    ticks: {
                        min: 0
                    },
                    scaleLabel: {
                        display: true,
                        labelString: xAxisLabel
                    }
                }]
            }
        }
    };

    let lineChart = new Chart(document.getElementById(canvasId).getContext('2d'), config);
}