import math

class Coord:
    THRESHOLD = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, coord):
        return math.sqrt((self.x - coord.x)**2 + (self.y - coord.y)**2)

    def __eq__(self, other):
        return self.distance(other) < Coord.THRESHOLD