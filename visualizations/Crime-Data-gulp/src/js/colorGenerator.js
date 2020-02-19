function splitNumToRGB(num){
    let redMask   = 0b111111110000000000000000;
    let greenMask = 0b000000001111111100000000;
    let blueMask  = 0b000000000000000011111111;

    let red = (redMask & num) >> 16;
    let blue = blueMask & num;
    let green = (greenMask & num) >> 8;

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
    let result = [];
    let num = 0;

    for (i=0; i<numColors; i++){
        result.push(num);
        num += parseInt(MAX_SIZE/numColors);
    }

    return result;
}

function generateColorStrings(numColors){
    const MAX_SIZE = 1 << 24;
    let result = [];
    let num = 0;

    for (i=0; i<numColors; i++){
        result.push(getColorString(num));
        num += parseInt(MAX_SIZE/numColors);
    }

    return result;
}

function generateSortedColorStrings(numColors){
    const MAX_SIZE = 1 << 24;
    let temp = [];
    let num = 0;

    for (i=0; i<numColors; i++){
        rgb = splitNumToRGB(num);

        red = rgb[0];
        green = rgb[1];
        blue = rgb[2];

        let avg = (red + green + blue) / 3;
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