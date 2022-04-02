from math import sin, cos, radians
from line import Line


class Pentagram:
    def __init__(self,radius):
        self.radius = radius

    def pentagram(self):
        self.points = []
        self.point = (0,self.radius)
        self.points.append(self.point)

        for i in range(4):
            self.rotate()
        self.draw_lines()

    def rotate(self):
        tempx = self.point[0]
        tempy = self.point[1]
        listpoint = list(self.point)
        listpoint[0] = round(cos(radians(72))* tempx- sin(radians(72))*tempy)
        listpoint[1] = round(sin(radians(72)) * tempx + cos(radians(72))*tempy)
        self.point = tuple(listpoint)
        self.points.append(self.point)

    def draw_lines(self):
        for index,point in enumerate(self.points):
            Line(point,self.points[(index+2)%5]).dda()
            Line(point,self.points[(index+3)%5]).dda()

