import os

import PIL.Image


size = 10_000, 10_000
axe_x = -2, 2
axe_y = -2, 2

c_global = -1.755
max_iteration = 100

x_len = axe_x[1] - axe_x[0]
y_len = axe_y[1] - axe_y[0]

img = PIL.Image.new('RGB', size)


def julia(c: complex | complex):
    for x in range(size[0]):
        for y in range(size[1]):

            z = pixel_to_complex(x, y)

            res = test_diverge(z, c)
            co = int(255*res)

            if res:
                img.putpixel((x, y), (co, co, co))
            else:
                img.putpixel((x, y), (0, 0, 0))


def test_diverge(z: complex, c: complex | int) -> float:
    i = 0
    while z.real < 4 and i < max_iteration:
        z = (z*z)+c
        i += 1

    return i / max_iteration


def pixel_to_complex(x: int, y: int) -> complex:
    return complex(((x / size[0]) * x_len) + axe_x[0], ((y/size[1]) * y_len) + axe_y[0])


def gen_plusieur():
    global max_iteration

    repertoire = f"julia_c={c_global}_evolution"

    if not os.path.exists(repertoire):
        os.makedirs(repertoire)

    for loop in range(0, 30):
        max_iteration = loop
        julia(c_global)
        img.save(repertoire + f"/julia_c={c_global}_size={size}_pres={max_iteration}_axex={axe_x}_axe_y={axe_y}.png")


def main():
    julia(c_global)
    img.save(f"julia_c={c_global}_size={size}_pres={max_iteration}_axex={axe_x}_axe_y={axe_y}.png")

    img.show()


if __name__ == '__main__':
    main()
