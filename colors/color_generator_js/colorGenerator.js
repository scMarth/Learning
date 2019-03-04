// Looks bad if the amount of colors to generate is low (~below 50)

function getColorString(num){
    var redMask   = 0b111111110000000000000000;
    var greenMask = 0b000000001111111100000000;
    var blueMask  = 0b000000000000000011111111;

    var red = (redMask & num) >> 16
    var blue = blueMask & num
    var green = (greenMask & num) >> 8

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

// tests
// console.log(16000000);
// console.log(getColorString(16000000));
// console.log(getColorNum(244, 36, 0));
// console.log(generateColors(12));
// console.log(generateColorStrings(12));
