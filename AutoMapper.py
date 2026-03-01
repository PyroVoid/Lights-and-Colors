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


def find_led(i):
    leds = set()
    while len(leds) != 1:
        controller.set_all((0, 0, 0))
        first = take_photo(cap)
        controller.set_color(i, (255, 255, 255))
        second = take_photo(cap)
        leds = algorithm(first, second)
    return leds[0]

def map():
    coords = []
    for i in range(Tree.LIGHTS):
        coords.append(find_led(i))
    cap.release()
    return coords

if __name__ == "__main__":
    coords = map()
    print(coords)
    print(len(coords))