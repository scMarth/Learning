/*

Generates colors that are an HSL gradient from #FF000 to #00FF00

Red     #FF0000     hsl(0, 100%, 50%)
Green   #00FF00     hsl(120, 100%, 50%)

*/
function splitNumToRGB(num){
    var redMask   = 0b111111110000000000000000;
    var greenMask = 0b000000001111111100000000;
    var blueMask  = 0b000000000000000011111111;

    var red = (redMask & num) >> 16;
    var blue = blueMask & num;
    var green = (greenMask & num) >> 8;

    return [red, green, blue];
}

function getColorNum(redNum, greenNum, blueNum){
    return (redNum << 16) + (greenNum << 8) + blueNum;
}

function hslToRgb(h, s, l){
    var r, g, b;

    if(s == 0){
        r = g = b = l; // achromatic
    }else{
        var hue2rgb = function hue2rgb(p, q, t){
            if(t < 0) t += 1;
            if(t > 1) t -= 1;
            if(t < 1/6) return p + (q - p) * 6 * t;
            if(t < 1/2) return q;
            if(t < 2/3) return p + (q - p) * (2/3 - t) * 6;
            return p;
        }

        var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
        var p = 2 * l - q;
        r = hue2rgb(p, q, h + 1/3);
        g = hue2rgb(p, q, h);
        b = hue2rgb(p, q, h - 1/3);
    }

    return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
}

function getColorString(num){
    rgb = splitNumToRGB(num);

    red = rgb[0];
    green = rgb[1];
    blue = rgb[2];

    return "rgb(" + red.toString() + ", " + green.toString() + ", " + blue.toString() + ")";
}

function generateHeatmapColorStrings(numColors){
    const MAX_SIZE = 120/360;
    var result = [];
    var num = 0;

    for (i=0; i<numColors; i++){
        var color = hslToRgb(num, 1, 0.5);
        colorNum = getColorNum(color[0], color[1], color[2]);
        result.push(getColorString(colorNum));
        console.log(num);
        num += MAX_SIZE/numColors;
    }

    return result;
}