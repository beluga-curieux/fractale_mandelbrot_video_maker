import os

import PIL.Image


size = 5_000, 5_000
axe_x = -4, 4
axe_y = -4, 4

c_global = -1.755
max_iteration = 100

x_len = axe_x[1] - axe_x[0]
y_len = axe_y[1] - axe_y[0]

img = PIL.Image.new('RGB', size)


def julia(c: complex | complex):
    for x in range(size[0]):
        for y in range(size[1]):

            z = pixel_to_complex(x, y)

            if test_diverge(z, c):
                img.putpixel((x, y), (255, 255, 255))

            else:
                img.putpixel((x, y), (0, 0, 0))


def test_diverge(z: complex, c: complex | int) -> bool:
    i = 0
    while z.real < 4 and i < max_iteration:
        z = (z*z)+c
        i += 1

    return max_iteration == i


def pixel_to_complex(x: int, y: int) -> complex:
    return complex(((x / size[0]) * x_len) + axe_x[0], ((y/size[1]) * y_len) + axe_y[0])


def main():
    global max_iteration

    repertoire = f"julia_c={c_global}_evolution"

    if not os.path.exists(repertoire):
        os.makedirs(repertoire)

    for loop in range(0, 30):
        max_iteration = loop
        julia(c_global)
        img.save(repertoire + f"/julia_c={c_global}_size={size}_pres={max_iteration}_axex={axe_x}_axe_y={axe_y}.png")


if __name__ == '__main__':
    main()
