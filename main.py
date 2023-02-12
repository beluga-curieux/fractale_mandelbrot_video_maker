import cmath

import PIL.Image

size = 10_000, 10_000
axe_x = -2, 2
axe_y = -2, 2

max_iteration = 20

x_len = axe_x[1] - axe_x[0]
y_len = axe_y[1] - axe_y[0]

img = PIL.Image.new('RGB', size)


def julia(c: complex):
    for x in range(size[0]):
        for y in range(size[1]):

            z = pixel_to_complex(x, y)

            if test_diverge(z, c):
                img.putpixel((x, y), (255, 255, 255))

            else:
                img.putpixel((x, y), (0, 0, 0))


def test_diverge(z: complex, c: complex) -> bool:
    i = 0
    while z.real < 4 and i < max_iteration:
        z = (z*z)+c
        i += 1

    return max_iteration == i


def pixel_to_complex(x: int, y: int) -> complex:
    return complex(((x / size[0]) * x_len) + axe_x[0], ((y/size[1]) * y_len) + axe_y[0])


def main():
    global max_iteration

    julia(c=complex(-1, 0))

    img.show()


if __name__ == '__main__':
    main()
    