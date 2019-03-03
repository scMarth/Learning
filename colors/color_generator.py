# generate 'num_colors_to_generate' amount of colors that are
# equidistant from the color spectrum

import itertools, sys, math

def get_color_string(num):
    red_mask   = 0b111111110000000000000000
    green_mask = 0b000000001111111100000000
    blue_mask  = 0b000000000000000011111111

    red = (red_mask & num) >> 16
    blue = blue_mask & num
    green = (green_mask & num) >> 8

    return "rgb(%d, %d, %d)"%(red, green, blue)

def get_color_string_formatted(num):
    red_mask   = 0b111111110000000000000000
    green_mask = 0b000000001111111100000000
    blue_mask  = 0b000000000000000011111111

    red = (red_mask & num) >> 16
    blue = blue_mask & num
    green = (green_mask & num) >> 8

    return "rgb(%3d, %3d, %3d)"%(red, green, blue)

def get_color_num(red_num, green_num, blue_num):
    return (red_num << 16) + (green_num << 8) + blue_num

def generate_colors(num_colors_to_generate):
    MAX_SIZE = 1 << 24
    result = []
    num = 0

    for i in range(0, num_colors_to_generate):
        result.append(num)
        num += MAX_SIZE/num_colors_to_generate

    return result

def print_num_colors(num_colors_to_generate):
    ind = 0
    for i in generate_colors(num_colors_to_generate):
        print("%2d: %8d"%(ind, i))
        ind += 1

def print_num_formatted_colors(num_colors_to_generate):
    ind = 0
    for i in generate_colors(num_colors_to_generate):
        print("%2d: %s"%(ind, get_color_string_formatted(i)))
        ind += 1

def gen_css(num_colors_to_generate):
    colors = generate_colors(num_colors_to_generate)

    filename = str(num_colors_to_generate) + ".css"
    with open(filename, 'w') as file:
        for color in colors:
            file.write(".color" + str(color) + "{\n")
            file.write("   background-color: " + get_color_string(color) + ";\n")
            file.write("}\n\n")

def gen_html(num_colors_to_generate):
    colors = generate_colors(num_colors_to_generate)
    filename = str(num_colors_to_generate) + ".html"

    outHTML = "<!DOCTYPE html>\n"
    outHTML += '<html lang="en">\n<head>'
    outHTML += '  <meta charset="UTF-8">'
    outHTML += '  <meta name="viewport" content="width=device-width, initial-scale=1.0">'
    outHTML += '  <meta http-equiv="X-UA-Compatible" content="ie=edge">'
    outHTML += '  <title>Document</title>'
    outHTML += '</head>\n<body>'

    for color in colors:
        outHTML += '  <div class=color' + str(color) + ' style="background-color:' + get_color_string(color) \
            + '; height: 100px; width: 100%;"></div>\n'

    outHTML += '</body>\n</html>'

    with open(filename, 'w') as file:
        file.write(outHTML)


gen_html(50)

print_num_colors(10)
print("")
print_num_colors(5)
print("")
print_num_colors(20)
print("")

print_num_formatted_colors(5)
print("")
print_num_formatted_colors(10)
print("")
print_num_formatted_colors(20)
print("")


print("")
print(get_color_num(255,0,0))
print(get_color_num(0,255,0))
print(get_color_num(0,0,255))
print("")
print(get_color_string(get_color_num(255,0,0)))
print(get_color_string(get_color_num(0,255,0)))
print(get_color_string(get_color_num(0,0,255)))

