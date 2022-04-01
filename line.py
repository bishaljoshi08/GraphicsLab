from mimetypes import init
import sys


class Line:
    
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def slope(self):
        self.dx = self.x2 - self.x1
        self.dy = self.y2 - self.y1
        self.m = abs(self.dy/self.dx) if self.dx != 0 else 100 #consider 100 as infinity you can also use sys.maxsize

    def dda(self):
        self.slope()
        roundx1 = self.x1
        roundy1 = self.y1
        while roundx1 != self.x2 or roundy1 != self.y2:
            print(roundx1,roundy1)
            if self.m < 1:
                if self.dx < 0:
                    self.x1 -= 1
                elif self.dx > 0:
                    self.x1 += 1
                if self.dy <= 0:
                    self.y1 -= self.m 
                elif self.dy>0:
                    self.y2 += self.m
            else:
                if self.dy < 0:
                    self.y1 -= 1
                elif self.dy > 0:
                    self.y1 += 1
                if self.dx <= 0:
                    self.x1 -= 1/self.m
                elif self.dx > 0:
                    self.x1 += 1/self.m
            roundx1 = round(self.x1)
            roundy1 = round(self.y1)
        print(roundx1,roundy1)

    def beshenham(self):
        self.slope()
        if self.m < 1:
            p0 = 2 * self.dy - self.dx
            while self.x1 != self.x2 or self.y1 != self.y2:
                print(self.x1,self.y1)
                if p0 < 0:
                    p0 =p0 + abs(2*self.dy)
                else:
                    p0 = p0 + abs(2*self.dy) - abs(2*self.dx)
                    if self.dy<0:
                        self.y1 -= 1
                    elif self.dy>0:
                        self.y1 += 1
                if self.dx > 0:
                    self.x1 += 1
                elif self.dx < 0:
                    self.x1 -= 1

        else:
            p0 = 2*self.dx -self.dy
            while self.x1 != self.x2 or self.y1 != self.y2:
                if p0 < 0:
                    p0 =p0 + abs(2*self.dx)
                else:
                    p0 = p0 + abs(2*self.dx) - abs(2*self.dy)
                    if self.dx<0:
                        self.x1 -= 1
                    elif self.dx>0:
                        self.x1 += 1
                if self.dy > 0:
                    self.y1 += 1
                elif self.dy < 0:
                    self.y1 -= 1
        print(self.x1,self.y1)


a = Line(30,20,0,20)
a.beshenham()

