function generatePieChart(data, dataColors, labels, titleStr, canvasId){
    config = {
        type: 'pie',
        data: {
            datasets: [{
                data: data,
                backgroundColor: dataColors
            }],
            labels: labels
        },
        options: {
            maintainAspectRatio: true,
            // responsive: true,
            title: {
                display: true,
                text: titleStr
            },
            tooltips: {
                callbacks: {
                    label: function(tooltipItem, data){
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

    var ctx = document.getElementById(canvasId).getContext('2d');
    window.myPie = new Chart(ctx, config);
}

function createChartFromJSON(data, colors, titleField){
    console.log(data);
    console.log(colors);
    console.log(titleField);

    dataValues = [];
    labels = [];
    titleFieldValue = "";

    for (var key in data){
        if (key == titleField){
            titleFieldValue = data[key];
            continue;
        }
        labels.push(key);
        dataValues.push(data[key]);
    }

    generatePieChart(dataValues, colors, labels, titleFieldValue, "chart-area");
}