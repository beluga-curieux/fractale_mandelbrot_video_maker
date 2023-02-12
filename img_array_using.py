import pprint
import cv2

import PIL.Image
import numpy as np


img = PIL.Image.open("julia_c=-1.755_size=(10000, 10000)_pres=100_axex=(-2, 2)_axe_y=(-2, 2).png")
array_img = np.array(img)

size_var = np.array(array_img.shape[:2])

border = 1
pas = 25
finit = (1_000, 1_000)

video_resolution = 2000, 2000
video = cv2.VideoWriter('video7.avi', cv2.VideoWriter_fourcc(*'MP4v'), 60, video_resolution)


def video_im_dict(path: dict):
    pass


while tuple(size_var) != finit and size_var[0] > finit[0] and size_var[1] > finit[1]:
    print("boucle", size_var, finit)

    fram_array = array_img[border:-border, border:-border]
    frame = PIL.Image.fromarray(fram_array).resize(video_resolution)
    video.write(np.array(frame))

    size_var = np.array(fram_array.shape[:2])
    border += pas


if __name__ == '__main__':
    pass
