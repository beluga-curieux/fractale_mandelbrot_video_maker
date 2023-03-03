from pprint import pprint

import numpy as np

AXEX = -2, 2
AXEY = -2, 2
COEF = 2
SIZE = 1_920 * COEF, 1_080 * COEF
MAX_ITERATION = 40
TOLERENCE = 4


IMG_ARRAY = np.zeros(SIZE).astype(complex)


def creat_array(size) -> np.array:
    r = np.zeros(size, complex)
    r.real = np.ones((size[0], 1)).dot(np.linspace(*AXEX, size[1]).reshape((1, size[1])))
    r.imag = np.linspace(*AXEY, size[0]).reshape(size[0], 1).dot(np.ones((1, size[1])))
    return r


def diverge(ar: np.array ,c, m, t):
    res = np.zeros(ar.shape, int)
    for loop in range(m):
        ar = ar * ar + c
        res[np.logical_and(ar.__abs__() < t , np.logical_not(res))] = loop

    return res


if __name__ == '__main__':
    r = creat_array((20, 20))

    a = diverge(r, 0 , MAX_ITERATION , TOLERENCE)

    print(a)

    print(r.shape)

    print(r[0])
    print(r[:, 0])
