from tkinter import filedialog
from AutoMapper import Automapper

import cv2
import numpy as np

import Controller


def Display(original_picture, mapp, pic_to_show):
    controller = Controller.Controller()
    pTS = pic_to_show

    og_pic = original_picture
    image = cv2.imread(pTS)
    if image is None:
        raise Exception("No picture found")
    op_height, op_width = og_pic.shape[:2]
    resized_PTS = cv2.resize(image, (op_width, op_height), interpolation = cv2.INTER_AREA)
    print(mapp)
    for i in range(len(mapp)):
        coords = mapp[i]
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        b, g, r = resized_PTS[coords[0], coords[1]]
        rgb = (int(r), int(g), int(b))
        controller.set_color(i, rgb)

if __name__ == "__main__":
    file = filedialog.askopenfilename()
    mapper = Automapper(1)
    coords, frame =  mapper.map()
    print(coords)
    Display(frame, coords, file)