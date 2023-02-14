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
video_title = f"video {strftime('%Y-%m-%d_%H-%M-%S', datetime.now().timetuple())}.avi"
video = cv2.VideoWriter('video7.avi', cv2.VideoWriter_fourcc(*'mp4v'), 60, video_resolution)


def video_init(resolution, fps=60):
    global video_resolution, video
    video_resolution = resolution
    video = cv2.VideoWriter(video_title, cv2.VideoWriter_fourcc(*'MP4v'), fps, video_resolution)


def video_from_dir(dir_path: str):
    i = 1
    path = dir_path+"/"+str(i)+".png"
    img = PIL.Image.open(path)
    video_init(img.size, 30)

    while os.path.exists(path):
        print(i)
        video.write(np.array(img))

        i += 1

        img = PIL.Image.open(path)
        path = dir_path+"/"+str(i)+".png"


def main():

    video_from_dir("th pres=40 size=(1920, 1080) xax=(-2.0, 2.0) yax=(-1.125, 1.125) 2023-02-14   13-52-24")


if __name__ == '__main__':
    main()
