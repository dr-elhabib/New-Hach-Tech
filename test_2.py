from statistics import pstdev

import numpy as np
import cv2


def exist(array, element):
    for i in range(0, len(array)):
        if (array[i] == element).all(1).any():
            return True

    return False


def sdvt_im_org(img):
    w, h = img.shape[:2]
    imge = np.zeros((w, h, 9), dtype='f')
    for i in range(w):
        for j in range(h):
            x = img[i][j]
            imge[i][j][0] = np.sqrt((1 + x[0]) ** 2 + (1 + x[1]) ** 2 + (
                    1 + x[2]) ** 2)  # distance entre pixel et sommet de coordonnee (0,0,0)
            imge[i][j][1] = np.sqrt((1 - x[0]) ** 2 + (1 + x[1]) ** 2 + (
                    1 + x[2]) ** 2)  # distance entre pixel et sommet de coordonnee (255,0,0)
            imge[i][j][2] = np.sqrt((1 + x[0]) ** 2 + (1 - x[1]) ** 2 + (
                    1 + x[2]) ** 2)  # distance entre pixel et sommet de coordonnee (0,255,0)
            imge[i][j][3] = np.sqrt((1 + x[0]) ** 2 + (1 + x[1]) ** 2 + (
                    1 - x[2]) ** 2)  # distance entre pixel et sommet de coordonnee (0,0,255)
            imge[i][j][4] = np.sqrt((1 - x[0]) ** 2 + (1 - x[1]) ** 2 + (
                    1 + x[2]) ** 2)  # distance entre pixel et sommet de coordonnee (255,255,0)
            imge[i][j][5] = np.sqrt((1 - x[0]) ** 2 + (1 + x[1]) ** 2 + (
                    1 - x[2]) ** 2)  # distance entre pixel et sommet de coordonnee (255,0,255)
            imge[i][j][6] = np.sqrt((1 + x[0]) ** 2 + (1 - x[1]) ** 2 + (
                    1 - x[2]) ** 2)  # distance entre pixel et sommet de coordonnee (0,255,255)
            imge[i][j][7] = np.sqrt((1 - x[0]) ** 2 + (1 - x[1]) ** 2 + (
                    1 - x[2]) ** 2)  # distance entre pixel et sommet de coordonnee (255,255,255)
            imge[i][j][8] = np.std([imge[i][j][k] for k in range(8)])  # ecart type des distances
    return imge


img = cv2.imread('image.png')
array_data = sdvt_im_org(img)
