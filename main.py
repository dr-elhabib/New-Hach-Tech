import sys
import time
from statistics import pstdev

import numpy as np
import cv2


def sdvt_im_org2(data):
    image = []
    for x in data:
        image_col = []
        image_col.append(np.sqrt((x[0]) ** 2 + (x[1]) ** 2 + (
            x[2]) ** 2))  # distance entre pixel et sommet de coordonnee (0,0,0)
        image_col.append(np.sqrt((255 - x[0]) ** 2 + (x[1]) ** 2 + (
            x[2]) ** 2))  # distance entre pixel et sommet de coordonnee (255,0,0)
        image_col.append(np.sqrt((x[0]) ** 2 + (255 - x[1]) ** 2 + (
            x[2]) ** 2))  # distance entre pixel et sommet de coordonnee (0,255,0)
        image_col.append(np.sqrt((x[0]) ** 2 + (x[1]) ** 2 + (
                255 - x[2]) ** 2))  # distance entre pixel et sommet de coordonnee (0,0,255)
        image_col.append(np.sqrt((255 - x[0]) ** 2 + (255 - x[1]) ** 2 + (
            x[2]) ** 2))  # distance entre pixel et sommet de coordonnee (255,255,0)
        image_col.append(np.sqrt((255 - x[0]) ** 2 + (x[1]) ** 2 + (
                255 - x[2]) ** 2))  # distance entre pixel et sommet de coordonnee (255,0,255)
        image_col.append(np.sqrt((x[0]) ** 2 + (255 - x[1]) ** 2 + (
                255 - x[2]) ** 2))  # distance entre pixel et sommet de coordonnee (0,255,255)
        image_col.append(np.sqrt((255 - x[0]) ** 2 + (255 - x[1]) ** 2 + (
                255 - x[2]) ** 2))  # distance entre pixel et sommet de coordonnee (255,255,255)
        image_col.append(np.std([image_col[k] for k in range(8)]))  # ecart type des distances
        image_col.append(x)
        image.append(image_col)
    return image


# To merge level
def steps(data, min_size):
    while len(data) > min_size:
        data = step(data)
    return data


# To merge pixels have min-different SDV
def step(data):
    new_data = []
    min_diff = sys.maxsize
    index_min = -1

    while len(data) > 0:
        if len(data) == 1:
            new_data.append(
                [data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6], data[0][7],
                 data[0][8],data[0][9]])
            break
        else:
            for other_key in range(1, len(data)):
                if not all(item in data[0][:8] for item in data[other_key][:8]):
                    diff = abs(data[0][8] - data[other_key][8])
                    if diff < min_diff:
                        min_diff = diff
                        index_min = other_key

            if index_min != -1:
                new_data.append([(data[0][0] + data[index_min][0]) / 2, (data[0][1] + data[index_min][1]) / 2,
                                 (data[0][2] + data[index_min][2]) / 2, (data[0][3] + data[index_min][3]) / 2,
                                 (data[0][4] + data[index_min][4]) / 2, (data[0][5] + data[index_min][5]) / 2,
                                 (data[0][6] + data[index_min][6]) / 2, (data[0][7] + data[index_min][7]) / 2,
                                 (data[0][8] + data[index_min][8]) / 2,(data[0][9] + data[index_min][9]) / 2])
            else:
                print("/////////////////")
            del data[index_min]
            del data[0]
            index_min = -1
            min_diff = sys.maxsize

    return new_data


# To remove all duplicate pixel value file
def no_deps(img):
    no_dupes = []
    w, h = img.shape[:2]
    elements = [list(img[i][j]) for i in range(w) for j in range(h)]
    for x in elements:
        exist = False
        for e in no_dupes:
            if e[0] == x[0] and e[1] == x[1] and e[2] == x[2]:
                exist = True
        if not exist:
            no_dupes.append(x)
    return no_dupes


start_time = time.time()
# img = cv2.imread('image.png')
# img = cv2.imread('image_edit_2.png')
# img = cv2.imread('image_edit_2.png')
# array_data = no_deps(img)

# array_data = sdvt_im_org2(array_data)
# print(steps(array_data, 8))
img = cv2.imread('image_edit_1.png')
# img = cv2.imread('image_edit_2.png')
# img = cv2.imread('image_edit_2.png')
array_data = no_deps(img)

array_data = sdvt_im_org2(array_data)
print(steps(array_data, 8))
img = cv2.imread('image_edit_2.png')
# img = cv2.imread('image_edit_2.png')
# img = cv2.imread('image_edit_2.png')
array_data = no_deps(img)

array_data = sdvt_im_org2(array_data)
print(steps(array_data, 8))
print("--- %s seconds ---" % (time.time() - start_time))
