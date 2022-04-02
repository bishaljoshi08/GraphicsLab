from OpenGL.GL import *

class Line:    
    def __init__(self,start,end):
        self.x1,self.y1 = start
        self.x2, self.y2 = end
        
    def slope(self):
        self.dx = self.x2 - self.x1
        self.dy = self.y2 - self.y1
        self.m = abs((self.dy)/(self.dx)) if self.dx != 0 else 100 #consider 100 as infinity you can also use sys.maxsize
    
    def dda(self):
        self.slope()
        roundx1 = self.x1
        roundy1 = self.y1
        while roundx1 != self.x2 or roundy1 != self.y2:
            glVertex2f(roundx1,roundy1)
            if self.m < 1:
                if self.dx < 0:
                    self.x1 -= 1
                elif self.dx > 0:
                    self.x1 += 1
                if self.dy <= 0:
                    self.y1 -= self.m 
                elif self.dy>0:
                    self.y1 += self.m
               
            else:
                if self.dy < 0:
                    self.y1 -= 1
                elif self.dy > 0:
                    self.y1 += 1
                if self.dx != 0:
                    if self.dx <= 0:
                        self.x1 -= 1/self.m
                    elif self.dx > 0:
                        self.x1 += 1/self.m
            x = self.x1
            y = self.y1
            roundx1 = round(x)
            roundy1 = round(y)
        glVertex2f(roundx1,roundy1)