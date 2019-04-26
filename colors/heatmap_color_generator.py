'''

From: https://stackoverflow.com/questions/2353211/hsl-to-rgb-color-conversion

Note: Use Python3 because of division

'''


'''
Converts an HSL color value to RGB. Conversion formula
adapted from http://en.wikipedia.org/wiki/HSL_color_space.
Assumes h, s, and l are contained in the set [0, 1] and
returns r, g, and b in the set [0, 255].

@param   {number}  h       The hue
@param   {number}  s       The saturation
@param   {number}  l       The lightness
@return  {Array}           The RGB representation
'''

def hue_to_rgb(p, q, t):
    if t < 0:
        t += 1
    if t > 1:
        t -= 1
    if t < 1/6:
        return p + (q - p) * 6 * t
    if t < 1/2:
        return q
    if t < 2/3:
        return p + (q - p) * (2/3 - t) * 6
    return p

def hsl_to_rgb(h, s, l):
    r = g = b = None

    if s == 0:
        r = g = b = 1 # achromatic
    else:
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)
    return [int(round(r*255)), int(round(g*255)), int(round(b*255))]

def get_color_num(r, g, b):
    return (r << 16) + (g << 8) + b

def get_color_string(num):
    red_mask   = 0b111111110000000000000000
    green_mask = 0b000000001111111100000000
    blue_mask  = 0b000000000000000011111111

    red = (red_mask & int(num)) >> 16
    blue = blue_mask & int(num)
    green = (green_mask & int(num)) >> 8

    return "rgb(%d, %d, %d)"%(red, green, blue)

def generate_heatmap_color_strings(num_colors):
    MAX_SIZE = 120/360
    result = []
    num = 0

    for i in range(0, num_colors):
        r, g, b = hsl_to_rgb(num, 1, 0.5)
        color_num = get_color_num(r, g, b)
        result.append(get_color_string(color_num))
        num += MAX_SIZE/num_colors
    return result

def generate_numeric_color_range(num_colors, MAXVAL):
    heatmap_colors = reversed(generate_heatmap_color_strings(num_colors))

    MAXVAL = float(MAXVAL)
    values = []

    for i in range(num_colors):
        num = MAXVAL * ((i+1)/num_colors)
        values.append(num)

    result = list(zip(values, heatmap_colors))
    return result

result = generate_numeric_color_range(200, 50)

for item in result:
    print("'{}':'{}',".format(item[0], item[1]), end=" ")

