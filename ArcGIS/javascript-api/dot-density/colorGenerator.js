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

function splitNumToRGB(num){
    var redMask   = 0b111111110000000000000000;
    var greenMask = 0b000000001111111100000000;
    var blueMask  = 0b000000000000000011111111;

    var red = (redMask & num) >> 16;
    var blue = blueMask & num;
    var green = (greenMask & num) >> 8;

    return [red, green, blue];
}


function getColorString(num){
    rgb = splitNumToRGB(num);

    red = rgb[0];
    green = rgb[1];
    blue = rgb[2];

    return "rgb(" + red.toString() + ", " + green.toString() + ", " + blue.toString() + ")";
}

function getColorNum(redNum, greenNum, blueNum){
    return (redNum << 16) + (greenNum << 8) + blueNum;
}

function generateColors(numColors){
    const MAX_SIZE = 1 << 24;
    var result = [];
    var num = 0;

    for (i=0; i<numColors; i++){
        result.push(num);
        num += parseInt(MAX_SIZE/numColors);
    }

    return result;
}

function generateColorStrings(numColors){
    const MAX_SIZE = 1 << 24;
    var result = [];
    var num = 0;

    for (i=0; i<numColors; i++){
        result.push(getColorString(num));
        num += parseInt(MAX_SIZE/numColors);
    }

    return result;
}

function generateSortedColorStrings(numColors){
    const MAX_SIZE = 1 << 24;
    var temp = [];
    var num = 0;

    for (i=0; i<numColors; i++){
        rgb = splitNumToRGB(num);

        red = rgb[0];
        green = rgb[1];
        blue = rgb[2];

        var avg = (red + green + blue) / 3;
        temp.push([avg, [red, green, blue]]);

        num += parseInt(MAX_SIZE/numColors);
    }

    // sort temp by avg color
    temp.sort(function(a, b){
        return a[0] - b[0];
    });

    result = [];

    for (i=0; i<temp.length; i++){
        item = temp[i];
        colorNum = getColorNum(item[1][0], item[1][1], item[1][2]);
        result.push(getColorString(colorNum));
    }

    return result;
}