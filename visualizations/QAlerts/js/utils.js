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
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
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
    var data = [];
    var labels = [];
    for (var key in phpArray){
        data.push(phpArray[key]);
        labels.push(key);
    }
    return [data, labels];
}

function generatePieChartFromPhpArray(phpArray, titleStr, canvasId, maintainAspectRatio){
    var dataAndLabels = splitIntoDataAndLabels(phpArray);
    var config = {
        type: 'pie',
        data: {
            datasets: [{
                data: dataAndLabels[0],
                backgroundColor: getFirstNColors(dataAndLabels[0].length),
            }],
            labels: dataAndLabels[1]
        },
        options: {
            maintainAspectRatio: maintainAspectRatio,
            responsive: true,
            title: {
                display: true,
                text: titleStr
            },
            tooltips: {
                callbacks: {
                    label: (tooltipItem, data) => {
                        var label = data.labels[tooltipItem.index] || '';
                        var value = data.datasets[0].data[tooltipItem.index] || '';

                        var sum = 0;
                        var dataArr = data.datasets[0].data;
                        dataArr.map(curr_val => {
                            sum += curr_val;
                        });
                        var percentage = (value*100 / sum).toFixed(3)+"%";
                        return label + ": " + value.toString() + " (" + percentage + ")";
                    }
                }
            }
        }
    }

    pieChart = new Chart(document.getElementById(canvasId).getContext('2d'), config);
    return pieChart;
}

function generateDoughnutChartFromPhpArray(phpArray, titleStr, canvasId, maintainAspectRatio){
    var dataAndLabels = splitIntoDataAndLabels(phpArray);
    var config = {
        type: 'doughnut',
        data: {
            datasets: [{
                data: dataAndLabels[0],
                backgroundColor: getFirstNColors(dataAndLabels[0].length),
            }],
            labels: dataAndLabels[1]
        },
        options: {
            maintainAspectRatio: maintainAspectRatio,
            responsive: true,
            title: {
                display: true,
                text: titleStr
            },
            tooltips: {
                callbacks: {
                    label: (tooltipItem, data) => {
                        var label = data.labels[tooltipItem.index] || '';
                        var value = data.datasets[0].data[tooltipItem.index] || '';

                        var sum = 0;
                        var dataArr = data.datasets[0].data;
                        dataArr.map(curr_val => {
                            sum += curr_val;
                        });
                        var percentage = (value*100 / sum).toFixed(3)+"%";
                        return label + ": " + value.toString() + " (" + percentage + ")";
                    }
                }
            }
        }
    }

    doughnutChart = new Chart(document.getElementById(canvasId).getContext('2d'), config);
    return doughnutChart;
}

function generateVerticalBarChartFromPhpArray(phpArray, titleStr, canvasId, yAxisLabel, maintainAspectRatio){
    var dataAndLabels = splitIntoDataAndLabels(phpArray);
    var config = {
        type: 'bar',
        data: {
            datasets: [{
                data: dataAndLabels[0],
                backgroundColor: getFirstNColors(dataAndLabels[0].length),
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
    }

    verticalBarChart = new Chart(document.getElementById(canvasId).getContext('2d'), config);
    return verticalBarChart;
}

function generateHorizontalBarChartFromPhpArray(phpArray, titleStr, canvasId, xAxisLabel, maintainAspectRatio){
    var dataAndLabels = splitIntoDataAndLabels(phpArray);
    var config = {
        type: 'horizontalBar',
        data: {
            datasets: [{
                data: dataAndLabels[0],
                backgroundColor: getFirstNColors(dataAndLabels[0].length),
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
    }

    horizontalBarChart = new Chart(document.getElementById(canvasId).getContext('2d'), config);
    return horizontalBarChart;
}

function generateLineChartFromPhpData(phpArray, titleStr, canvasId, xAxisLabel, yAxisLabel, maintainAspectRatio){
    var datasetCount = 0
    for (var key in phpArray){
        if (key != 'dates'){
            datasetCount++;
        }
    }
    colors = getFirstNColors(datasetCount);

    datasets = [];
    colorInd = 0;
    for (var key in phpArray){
        if (key != 'dates'){
            var dataset = {
                label: key,
                data: phpArray[key],
                backgroundColor: colors[colorInd],
                borderColor: colors[colorInd++],
                // steppedLine: true,
                pointRadius: 2,
                fill: false
            }
            datasets.push(dataset);
        }
    }

    var config = {
        type: 'line',
        data: {
            labels: phpArray['dates'],
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
    }

    lineChart = new Chart(document.getElementById(canvasId).getContext('2d'), config);
    return lineChart;
}