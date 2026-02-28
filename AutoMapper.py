from TreeSimulation import Tree
import Controller
from LightDiffAlgoTmp import get_diffs

def map():
    coords = []
    controller = Controller.Controller()
    for i in range(Tree.LIGHTS):
        controller.set_color(i, (0, 0, 0))
    for i in range(Tree.LIGHTS):
        controller.set_color(i, (255, 255, 255))
        coords.append(get_diffs())
        controller.set_color(i, (0, 0, 0))