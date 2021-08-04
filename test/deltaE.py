import struct
from colormath.color_conversions import convert_color
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_diff import delta_e_cie1976

rgb1 = (1, 242, 50)
rgb2 = (200, 121, 51)

rgb11 = sRGBColor(rgb1[0], rgb1[1], rgb1[2])
rgb22 = sRGBColor(rgb2[0], rgb2[1], rgb2[2])
a = convert_color(rgb11, LabColor)
b = convert_color(rgb22, LabColor)
print('kk')
print(delta_e_cie1976(a, b))
print('mm')