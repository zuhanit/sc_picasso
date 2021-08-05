import struct
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
import cv2
import numpy

def convertTileset(tileset):
    tilesetLabDict = {}
    path = "./data/" + tileset + ".picasso"
    with open(path, 'rb') as file:
        format = '1H3B'
        format_len = struct.calcsize(format)
        while True:
            binary = file.read(format_len)
            if not binary: break
            data = struct.unpack(format, binary)
            rgb = sRGBColor(data[1], data[2], data[3])
            lab = convert_color(rgb, LabColor)
            tilesetLabDict[data[0]] = lab
    return tilesetLabDict

def convertImage(src):
    srcLabDict = {}
    x = 0
    for height in src:
        for width in height:
            rgb = sRGBColor(width[0], width[1], width[2])
            lab = convert_color(rgb, LabColor)
            srcLabDict[x] = lab
            x += 1
    print("Complete")
    return srcLabDict


def asd(tileset):
    tilsetHistogramDict = {}
    path = "./data/" + tileset + ".picasso"
    with open(path, 'rb') as file:
        format = '1H48B'
        format_len = struct.calcsize(format)
        while True:
            binary = file.read(format_len)
            if not binary: break
            data = struct.unpack(format, binary)
            rgb = data[1:50]
            tileColorArr = [[[rgb[12*j + 3*k + x] for x in range(0, 3)] for k in range(0, 4)] for j in range(0, 4)]
            npArr = numpy.array(tileColorArr, dtype='uint8')
            cv2.calcHist([npArr], cv2.)