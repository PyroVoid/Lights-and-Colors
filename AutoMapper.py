from TreeSimulation import Tree
import Controller
from LightDiffAlgo import algorithm, take_photo
import cv2

def map():
    cap = cv2.VideoCapture(1)
    coords = []
    controller = Controller.Controller()
    for i in range(Tree.LIGHTS):
        controller.set_color(i, (0, 0, 0))
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