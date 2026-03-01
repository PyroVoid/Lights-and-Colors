from TreeSimulation import Tree
import Controller
from LightDiffAlgo import algorithm, take_photo
import cv2
import platform
import pygame

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
        frame = take_photo(self.cap)
        self.cap.release()
        return coords, frame

if __name__ == "__main__":
    mapper = Automapper(1)
    coords, frame = mapper.map()
    height, width = frame.shape[:-2]
    print(coords)
    print(len(coords))
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i in range(len(coords)):
            pygame.draw.circle(screen, (255,255,255), coords[i], 5)