from math import sin, cos, radians
from circle import Circle
from line import Line

class Piechart:
    def __init__(self):
        self.end_x = 100
        self.end_y = 0

    def circle(self,degrees):
        c = Circle(0,0,100)
        c.mid_point()
        sum = 0
        for degree in degrees:
            sum += degree
        if sum > 360:
            print('Total degree can\'t be greater than 360 ')
        else:
            if len(degrees) == 1 and (degrees[0] == 0 or degrees[0] == 360):
                return
            else:
                for degree in degrees:
                    self.rotate(degree)
                l = Line(0,0,self.end_x,self.end_y)
                l.dda()

    def rotate(self,angle):
        if angle == 0 or angle == 360:
            return
        else:
            l = Line(0,0,self.end_x,self.end_y)
            l.dda()
            tempx = self.end_x
            tempy = self.end_y
            self.end_x = round(cos(radians(angle))* tempx- sin(radians(angle))*tempy)
            self.end_y = round(sin(radians(angle)) * tempx + cos(radians(angle))*tempy)