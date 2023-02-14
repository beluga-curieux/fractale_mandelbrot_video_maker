import os
from time import strftime, time, sleep
from datetime import datetime
from multiprocessing import Process, cpu_count
import numpy as np
from PIL import Image, ImageDraw

p_count = 0

bright = 150

coef = 2
size = 1_920 * coef, 1_080 * coef

axe_x = -2, 2
axe_y = -2, 2

max_iteration = 40
tollerense = 4

x_len = axe_x[1] - axe_x[0]
y_len = axe_y[1] - axe_y[0]


def center_ortonorme(x_axe=4):
    global axe_x, axe_y, x_len, y_len

    y_axe = size[1] / size[0] * x_axe

    axe_x = 0 - x_axe / 2, x_axe/2
    axe_y = 0 - y_axe / 2, y_axe/2

    x_len = axe_x[1] - axe_x[0]
    y_len = axe_y[1] - axe_y[0]


def pixel_to_complex(x: int, y: int) -> complex:
    return complex(((x / size[0]) * x_len) + axe_x[0], ((y/size[1]) * y_len) + axe_y[0])


def test_diverge(z: complex, c: complex | int) -> float:
    i = 0
    # (0-tollerense < z.imag < tollerense and 0-tollerense < z.real < tollerense)
    while abs(z) < tollerense and i < max_iteration:
        z = (z*z)+c
        i += 1

    return i / max_iteration


def julia(c: complex | complex, img: Image.Image):
    for x in range(size[0]):
        for y in range(size[1]):

            z = pixel_to_complex(x, y)

            res = test_diverge(z, c)
            co = int(bright - (255 * res))

            if res:
                img.putpixel((x, y), (co, co, co))
            else:
                img.putpixel((x, y), (bright, bright, bright))


def creat_and_save_julia(rep, name, c):
    global p_count


    img = Image.new('RGB', size)
    julia(c, img)
    img.save(rep + f"/{name}.png")



def threding_gen_plusieur(n):
    global p_count
    lan = np.linspace(-2, 0, n)

    att_lst = []
    run_lst = []

    repertoire = f"th pres={max_iteration} size={size} xax={axe_x} yax={axe_y} {strftime('%Y-%m-%d_%H-%M-%S', datetime.now().timetuple())}"

    if not os.path.exists(repertoire):
        os.makedirs(repertoire)

    for f in range(len(lan)):
        print(f)
        att_lst.append(Process(target=creat_and_save_julia, args=(repertoire, f, lan[f])))

    for th in att_lst:
        if len(run_lst) > 10:
            run_lst[0].join()
            del run_lst[0]

        run_lst.append(th)
        th.start()

    for th in run_lst:
        th.join()


def main():
    julia(0, Image.new('RGB', size))

    threding_gen_plusieur(1000)


if __name__ == '__main__':
    main()
