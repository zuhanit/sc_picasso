"""
Data extractor of SC:R Tileset. Maybe support to Remaster?
It extract data and match rgb to Megatile, and pack(.piccaso)
"""

import struct

class Tile:
    def getCV5Data(self, tileset: str):
        format = '20B16H'
        format_len = struct.calcsize(format)
        filePath = './data/lib/' + tileset + '.cv5'
        megatileIndex = []
        with open(filePath, 'rb') as files:
            while True:
                binary = files.read(format_len)
                if not binary: break
                data = struct.unpack(format, binary)
                group = data[20:36]
                for index in group:
                    megatileIndex.append(index)

        return megatileIndex

    def getVX4Data(self, tileset: str):
        format = '16L'
        format_len = struct.calcsize(format)
        filePath = './data/lib/' + tileset + '.vx4ex'
        vx4Index = []
        
        with open(filePath, 'rb') as files:
            while True:
                binary = files.read(format_len)
                if not binary: break
                data = struct.unpack(format, binary)
                k = []
                for minitile in data:
                    m = []
                    m.append(int(bin(minitile >> 1), 2)) # 상위 31비트
                    m.append(int(bin(minitile & 0b1), 2)) # 하위 1비트, flipped
                    k.append(m)
                vx4Index.append(k)

        return vx4Index


    def getVR4Data(self, tileset: str):
        format = '64B'
        format_len = struct.calcsize(format)
        filePath = './data/lib/' + tileset + '.vr4'
        vr4Index = []

        with open(filePath, 'rb') as files:
            while True:
                binary = files.read(format_len)
                if not binary: break
                data = struct.unpack(format, binary)
                m = []
                for vr4 in data:
                    m.append(vr4)
                vr4Index.append(m)

        return vr4Index

    def getWPEData(self, tileset: str):
        format = '4B'
        format_len = struct.calcsize(format)
        filePath = './data/lib/' + tileset + '.wpe'
        rgbData = []

        with open(filePath, 'rb') as files:
            while True:
                binary = files.read(format_len)
                if not binary: break
                data = struct.unpack(format, binary)
                m = [data[0], data[1], data[2]]
                rgbData.append(m)

        return rgbData

    def getTileData(self):
        """
        Get tile data from library.
        """

        tilesets = {
            'ashworld' : {
            },
            'badlands' : {
            },
            'Desert' : {
            },
            'ice' : {
            },
            'install' : {
            },
            'jungle' : {
            },
            'platform' : {
            },
            'twilight' : {
            }
        }

        for tileset in tilesets:
            k = tilesets[tileset]
            k['megatiles'] = self.getCV5Data(tileset)
            k['minitiles'] = self.getVX4Data(tileset)
            k['rgbs'] = self.getVR4Data(tileset)
            k['rgbDatas'] = self.getWPEData(tileset)

        return tilesets

k = Tile()
j = k.getTileData()

matchedTileData = {
    'ashworld' : {
    },
    'badlands' : {
    },
    'Desert' : {
    },
    'ice' : {
    },
    'install' : {
    },
    'jungle' : {
    },
    'platform' : {
    },
    'twilight' : {
    }
}

# Match RGB Data to Index 1 of Minitile

for tileset in j:
    z = j[tileset]
    for mega in z['megatiles']:
        minitiles = z['minitiles']
        rgbs = z['rgbs']
        rgbDatas = z['rgbDatas']
        m = []
        for i in range(0, 16):
            minitile = minitiles[mega][i][0]
            rgbIndex = rgbs[minitile][47]
            rgb = rgbDatas[rgbIndex]
            m.append(rgb)

        matchedTileData[tileset][mega] = m

"""
Package Data
WORD[0] Megatile Index
CHAR[3] RGB Data
"""

for tileset in matchedTileData:
    filename = './data/' + tileset + '.picasso'
    with open(filename, 'wb') as file:
        for mega in matchedTileData[tileset]:
            format = '1H3B'
            rgb = matchedTileData[tileset][mega]
            data = struct.pack(format, mega, rgb[0], rgb[1], rgb[2])
            file.write(data)
        file.close()

print('k')
print('asd')