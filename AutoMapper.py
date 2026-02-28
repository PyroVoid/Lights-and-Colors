from TreeSimulation import Tree
import Controller
from LightDiffAlgo import algorithm, take_photo
import cv2
import platform

if platform.system() == "Windows":
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
else:
    cap = cv2.VideoCapture(1)
controller = Controller.Controller()

def find_leds():
    leds = set()
    first = take_photo(cap)
    controller.set_all((0, 0, 0))
    second = take_photo(cap)


def map():
    coords = []
    controller.set_all((0, 0, 0))
    frame1 = take_photo(cap)
    for i in range(Tree.LIGHTS):
        controller.set_color(i, (255, 255, 255))
        frame2 = take_photo(cap)
        coords += algorithm(frame1, frame2)
        controller.set_color(i, (0, 0, 0))
    cap.release()
    return coords

if __name__ == "__main__":
    coords = map()
    print(coords)
    print(len(coords))