import cv2
import numpy

def getBGRData(path, height, width):
    src = cv2.imread(path, cv2.IMREAD_COLOR)
    resizedImage = cv2.resize(src, dsize=(height, width), interpolation=cv2.INTER_AREA)
    return resizedImage