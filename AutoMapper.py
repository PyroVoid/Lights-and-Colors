from TreeSimulation import Tree
import Controller
from LightDiffAlgo import algorithm, take_photo
import cv2
import platform

class Automapper:
    def __init__(self, cap):
        if platform.system() == "Windows":
            self.cap = cv2.VideoCapture(cap, cv2.CAP_DSHOW)
        else:
            self.cap = cv2.VideoCapture(cap)
        self.controller = Controller.Controller()

    def find_led(self, i):
        leds = set()
        while len(leds) != 1:
            self.controller.set_all((0, 0, 0))
            first = take_photo(self.cap)
            self.controller.set_color(i, (255, 255, 255))
            second = take_photo(self.cap)
            leds = algorithm(first, second)
        return leds[0]

    def map(self):
        coords = []
        for i in range(Tree.LIGHTS):
            coords.append(self.find_led(i))
        self.cap.release()
        return coords

if __name__ == "__main__":
    mapper = Automapper(1)
    coords = mapper.map()
    print(coords)
    print(len(coords))