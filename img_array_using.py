from datetime import datetime
import os
from time import strftime

import cv2

import PIL.Image
import numpy as np


# img = PIL.Image.open("julia_c=-1.755_size=(10000, 10000)_pres=100_axex=(-2, 2)_axe_y=(-2, 2).png")
# array_img = np.array(img)

# size_var = np.array(array_img.shape[:2])

border = 1
pas = 25
finit = (1_000, 1_000)

video_resolution = 2000, 2000
video_title = f"video {strftime('%Y-%m-%d_%H-%M-%S', datetime.now().timetuple())}"
video = cv2.VideoWriter('video7.avi', cv2.VideoWriter_fourcc(*'MP4v'), 60, video_resolution)


def video_init(resolution, fps=60):
    global video_resolution, video_title, video
    video_resolution = resolution
    video_title = f"video {strftime('%Y-%m-%d_%H-%M-%S', datetime.now().timetuple())}.avi"
    video = cv2.VideoWriter(video_title, cv2.VideoWriter_fourcc(*'MP4v'), fps, video_resolution)


def video_from_dir(dir_path: str):
    i = 1
    path = dir_path+"/"+str(i)+".png"
    img = PIL.Image.open(path)
    video_init(img.size, 5)

    while os.path.exists(path):
        print(i)
        video.write(np.array(img))

        i += 1

        img = PIL.Image.open(path)
        path = dir_path+"/"+str(i)+".png"


def main():
    video_from_dir("julia_c=-1.755 size=(3840, 2160) xax=(-0.5, 0.5) yax=(-0.28125, 0.28125) 2023-02-12_17-03-31")



# while tuple(size_var) != finit and size_var[0] > finit[0] and size_var[1] > finit[1]:
#     print("boucle", size_var, finit)
#
#     fram_array = array_img[border:-border, border:-border]
#     frame = PIL.Image.fromarray(fram_array).resize(video_resolution)
#     video.write(np.array(frame))
#
#     size_var = np.array(fram_array.shape[:2])
#     border += pas


if __name__ == '__main__':
    main()
