from TreeSimulation import Tree
import Controller
from LightDiffAlgoTmp import get_diffs, take_pic

def map():
    coords = []
    controller = Controller.Controller()
    for i in range(Tree.LIGHTS):
        controller.set_color(i, (0, 0, 0))
    for i in range(Tree.LIGHTS):
        take_pic()
        controller.set_color(i, (255, 255, 255))
        take_pic()
        coords.append(get_diffs())
        controller.set_color(i, (0, 0, 0))
    return coords

if __name__ == "__main__":
    coords = map()
    print(coords)