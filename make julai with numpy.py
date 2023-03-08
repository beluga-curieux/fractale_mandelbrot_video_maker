from pprint import pprint

import numpy as np
import PIL.Image as pil

AXEX = -2, 2
AXEY = -2, 2
COEF = 1
SIZE = 1_920 * COEF, 1_080 * COEF
MAX_ITERATION = 4
TOLERENCE = 4
BRIHGT = 255


IMG_ARRAY = np.zeros(SIZE).astype(complex)


def creat_array(size) -> np.array:
    r = np.zeros(size, complex)
    r.real = np.ones((size[0], 1)).dot(np.linspace(*AXEX, size[1]).reshape((1, size[1])))
    r.imag = np.linspace(*AXEY, size[0]).reshape(size[0], 1).dot(np.ones((1, size[1])))
    return r


def diverge(ar: np.array, c, m, t):
    res = np.zeros(ar.shape, int)
    for loop in range(1, m+1):
        ar = ar * ar + c

        res[np.logical_and(np.abs(ar) > t, np.logical_not(res))] = loop
    return res


def creat_image(ar: np.array, m):
    result = 255 * ar.T / m
    result = result.reshape((ar.shape[1], ar.shape[0], 1)).copy()
    result = np.repeat(result, 3, 2).astype(np.uint8)
    print(result.shape)
    print()
    pil.fromarray(result).save('save/test.png')





if __name__ == '__main__':
    r = creat_array(SIZE)

    a = diverge(r, 0, MAX_ITERATION, TOLERENCE)
    creat_image(a, MAX_ITERATION)

