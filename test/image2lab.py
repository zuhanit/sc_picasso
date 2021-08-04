from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
import cv2

src = cv2.imread('./test/test2.jpg', cv2.IMREAD_COLOR)
resizedImage = cv2.resize(src, dsize=(64, 64), interpolation=cv2.INTER_AREA)
resizedImage = resizedImage.tolist()

print('k')