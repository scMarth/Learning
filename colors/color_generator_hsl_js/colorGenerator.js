/*

Notes: so far, doesn't turn out well

*/
function getColorString(num){
    lightness = 10 + (num/360)
    saturation = 100
    hue = num % 360

    var result = "hsl(" + hue.toString() + ", " + saturation.toString() + "%, " + lightness.toString() + "%)";
    console.log(result);
    return result;
}

function generateColorStrings(numColors){
    const MAX_SIZE = 28800;
    var result = [];
    var num = 0;

    for (i=0; i<numColors; i++){
        result.push(getColorString(num));
        num += parseInt(MAX_SIZE/numColors);
    }

    return result;
}