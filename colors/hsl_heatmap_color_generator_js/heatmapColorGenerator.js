/*

Generates colors that are an HSL gradient from hsl(120, 100%, 50%) to hsl(0, 100%, 50%)

*/
function getHSLColorString(h, s, l){
    return "hsl(" + h.toString() + ", " + s.toString() + "%, " + l.toString() + "%)";
}

function generateHeatmapColorStrings(numColors){
    const MAX_SIZE = 120;
    var result = [];
    var num = 0;

    for (i=0; i<numColors; i++){
        result.push(getHSLColorString(num, 100, 50));
        console.log(num);
        num += MAX_SIZE/numColors;
    }

    return result.reverse();
}