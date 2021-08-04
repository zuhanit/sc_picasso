import struct
from generator import findSimilarTile2
from keyboard import press
import image
from convert import convertImage, convertTileset
from math import sqrt

def pressanykey():
    import os
    os.system('pause')
    exit()

print("Picasso: Starcraft Minimap Drawer\nhttps://cafe.naver.com/edac\n------------------------------\n[1/4] Input Map Height")
height = input()
print("[1/4] Input Map Width")
width = input()

if height.isnumeric() == False or width.isnumeric() == False or int(height) > 256 or int(width) > 256:
    print("ERROR: Please input correct value. map size must be smaller than 256.")
    pressanykey()

height = int(height)
width = int(width)

print("[2/4] Select Tileset.\n[ashworld, badlands, desert, ice, installation, jungle, platform, twilight]")
tileset = input()
tilesets = {
    'ashworld': 0,
    'badlands': 1,
    'desert': 2,
    'ice': 3,
    'installation': 4,
    'jungle': 5,
    'platform': 6,
    'twilight': 7,
}
tileset = tileset.lower()

if tileset not in tilesets:
    print("ERROR: Entered Tileset '" + tileset + "' is not valid tileset.")
    pressanykey()

print("[3/4] Type image absolute path:")
path = input()
try:
    image.getBGRData(path, height, width)
except:
    print("ERROR: Failed to open file. Check file path is valid.")
    pressanykey()

srcRGB = image.getBGRData(path, height, width)
srcRGB = srcRGB.tolist()

print("[4/4] Converting tileset RGB Color to Lab Color Space...")
tilesetLabDict = convertTileset(tileset)

print("[5/4] Converting image RGB Color to Lab Color Space...")
imageLabDict = convertImage(srcRGB)

print("[6/4] Finding similar tile. this takes a while...")
similarTiles = findSimilarTile2(tilesetLabDict, imageLabDict)

print("[7/5] Generating MXTM...")
with open('.picassoMXTM', 'wb') as file:
    format = 'H'
    format_len = struct.calcsize(format)
    for tile in similarTiles:
        binary = struct.pack(format, int(tile))
        file.write(binary)
    file.close()

print('k')
