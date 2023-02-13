import os
from time import strftime
from datetime import datetime
from PIL import Image, ImageDraw


b = 200

coef = 5
size = 1_920 * coef, 1_080 * coef

axe_x = -2, 2
axe_y = -2, 2

# c_global = -1.755
c_global = complex(1.452)

max_iteration = 20
tollerense = 4

x_len = axe_x[1] - axe_x[0]
y_len = axe_y[1] - axe_y[0]

img = Image.new('RGB', size)
draw = ImageDraw.Draw(img)


def center_ortonorme(x_axe=4):
    global axe_x, axe_y, x_len, y_len

    y_axe = size[1] / size[0] * x_axe

    axe_x = 0 - x_axe / 2, x_axe/2
    axe_y = 0 - y_axe / 2, y_axe/2

    x_len = axe_x[1] - axe_x[0]
    y_len = axe_y[1] - axe_y[0]


def get_color():
    pass


def julia(c: complex | complex):
    for x in range(size[0]):
        for y in range(size[1]):

            z = pixel_to_complex(x, y)

            res = test_diverge(z, c)
            co = int(b - (255 * res))

            if res:
                img.putpixel((x, y), (co, co, co))
            else:
                img.putpixel((x, y), (b, b, b))


def test_diverge(z: complex, c: complex | int) -> float:
    i = 0
    # (0-tollerense < z.imag < tollerense and 0-tollerense < z.real < tollerense)
    while abs(z) < tollerense and i < max_iteration:
        z = (z*z)+c
        i += 1

    return i / max_iteration


def pixel_to_complex(x: int, y: int) -> complex:
    return complex(((x / size[0]) * x_len) + axe_x[0], ((y/size[1]) * y_len) + axe_y[0])


def gen_plusieur():
    global max_iteration

    repertoire = f"julia_c={c_global} size={size} xax={axe_x} yax={axe_y} {strftime('%Y-%m-%d_%H-%M-%S', datetime.now().timetuple())}"

    if not os.path.exists(repertoire):
        os.makedirs(repertoire)

    for loop in range(1, 60):
        print(loop)
        max_iteration = loop
        julia(c_global)
        img.save(repertoire + f"/{loop}.png")


def main():
    center_ortonorme(8)

    julia(c_global)

    img.save(f"save/julia_c={c_global}_size={size}_pres={max_iteration}_axex={axe_x}_axe_y={axe_y}.png")

    # gen_plusieur()
    # img.save(f"julia_c={c_global}_size={size}_pres={max_iteration}_axex={axe_x}_axe_y={axe_y}.png")


    img.show()


if __name__ == '__main__':
    main()
