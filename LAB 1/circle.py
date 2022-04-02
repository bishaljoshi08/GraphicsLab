from OpenGL.GL import *

class Circle:
    def __init__(self,center_x,center_y,radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def mid_point(self):
        self.x = 0
        self.y = round(self.radius)
        self.eight_point_symmetry()
        if isinstance(self.radius, int):
            p0 = 1 - self.radius
        elif isinstance(self.radius, float):
            p0 = 5/4 - self.radius
        while not self.x >= self.y:
            if p0 < 0:
                self.x += 1
                p0 = p0 + 2*self.x +1
            else:
                self.x += 1
                self.y -= 1
                p0 = p0 + 2*self.x +1 -2*self.y
            self.eight_point_symmetry()
            
    def add_center(self,xadd,yadd):
        glVertex2f(xadd+self.center_x,yadd+self.center_y)

    def eight_point_symmetry(self):
        self.add_center(self.x,self.y)
        self.add_center(-1*self.x,self.y)
        self.add_center(self.x,-1*self.y)
        self.add_center(-1*self.x,-1*self.y)
        self.add_center(self.y,self.x)
        self.add_center(-1*self.y, self.x)
        self.add_center(self.y, -1*self.x)
        self.add_center(-1*self.y,-1*self.x)