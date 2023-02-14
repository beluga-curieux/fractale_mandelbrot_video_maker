import os
from time import strftime, time, sleep
from datetime import datetime
from multiprocessing import Process, cpu_count
import numpy as np
from PIL import Image, ImageDraw

p_count = 0

bright = 150

coef = 1
size = 1_920 * coef, 1_080 * coef

max_iteration = 40
tollerense = 4


def center_ortonorme(x_axe=4):

    y_axe = size[1] / size[0] * x_axe

    axe_x = 0 - x_axe / 2, x_axe/2
    axe_y = 0 - y_axe / 2, y_axe/2

    return axe_x, axe_y


def pixel_to_complex(x: int, y: int, axe_x: tuple[int | float, int | float], axe_y: tuple[int | float, int | float]) -> complex:
    x_len = axe_x[1] - axe_x[0]
    y_len = axe_y[1] - axe_y[0]
    return complex(((x / size[0]) * x_len) + axe_x[0], ((y/size[1]) * y_len) + axe_y[0])


def test_diverge(z: complex, c: complex | int) -> float:
    i = 0
    # (0-tollerense < z.imag < tollerense and 0-tollerense < z.real < tollerense)
    while abs(z) < tollerense and i < max_iteration:
        z = (z*z)+c
        i += 1

    return i / max_iteration


def julia(c: complex | complex, axe_x: tuple[int | float, int | float], axe_y: tuple[int | float, int | float], img: Image.Image):
    for x in range(size[0]):
        for y in range(size[1]):

            z = pixel_to_complex(x, y, axe_x, axe_y)

            res = test_diverge(z, c)
            co = int(bright - (255 * res))

            if res:
                img.putpixel((x, y), (co, co, co))
            else:
                img.putpixel((x, y), (bright, bright, bright))


def creat_and_save_julia(c, axe_x, axe_y, rep="save", name=None):
    global p_count

    if name is None:
        name = f"julia_c={c}_size={size}_pres={max_iteration}_axex={axe_x}_axe_y={axe_y}"

    img = Image.new('RGB', size)

    julia(c, axe_x, axe_y, img)
    img.save(rep + f"/{name}.png")


def threding_gen_plusieur(n, axes):
    global p_count

    lan_r = np.linspace(-1, 1, n)
    lan_i = np.linspace(-1, 1, n)

    att_lst = []
    run_lst = []

    repertoire = f"th pres={max_iteration} size={size} xax={axes[0]} yax={axes[1]} {strftime('%Y-%m-%d   %H-%M-%S', datetime.now().timetuple())}"

    if not os.path.exists(repertoire):
        os.makedirs(repertoire)

    for f in range(len(lan_i)):
        att_lst.append(Process(target=creat_and_save_julia, args=(complex(lan_r[f], lan_i[f]), *axes, repertoire, f)))

    for i, th in enumerate(att_lst):
        if len(run_lst) > 15:
            run_lst[0].join()
            del run_lst[0]

        run_lst.append(th)
        th.start()
        print("lauch : ", i)

    for th in run_lst:
        th.join()


def main():
    global max_iteration

    threding_gen_plusieur(600, center_ortonorme())


if __name__ == '__main__':
    main()
