import struct
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color

dict = {}
dict2 = {}

with open('./data/ashworld.picasso', 'rb') as file:
    format = '1H3B'
    format_len = struct.calcsize(format)
    x = 0
    while True:
        binary = file.read(format_len)
        if not binary: break
        data = struct.unpack(format, binary)
        rgb = sRGBColor(data[1], data[2], data[3])
        lab = convert_color(rgb, LabColor)
        dict[data[0]] = lab
        dict2[x] = data[0]
        x+=1