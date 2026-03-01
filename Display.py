import cv2
import numpy as np

def Display(original_picture, mapp, pic_to_show):
    pTS = pic_to_show
    og_pic = original_picture
    image = cv2.imread(pic_to_show)
    if image is None:
        raise Exception("No picture found")
    op_width, op_height = og_pic.shape[:2]
    resized_PTS = cv2.resize(pTS, (op_width, op_height), interpolation = cv2.INTER_AREA)
