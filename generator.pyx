from colormath.color_diff import delta_e_cie1976
import time
from tqdm import tqdm

def findSimilarTile2(tilesetLab, imageLab):
    startt = time.time()
    times = 0
    tiles = []
    for j in tqdm(imageLab):
        distances = []
        for k in tilesetLab:
            distance = delta_e_cie1976(imageLab[j], tilesetLab[k])
            distances.append(distance)
        minDistance = min(distances) # 가장 작은 거리를 계산. len of distances: len of tilesetLab == megatiles.
        tiles.append(distances.index(minDistance))
        times += 1
    print("--- %s seconds elapsed to find similar tile ---" % (time.time() - startt))
    return tiles