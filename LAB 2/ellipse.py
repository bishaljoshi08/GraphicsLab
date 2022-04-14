import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Ellipse():
    def __init__(self, rx, ry, x_center, y_center):
        self.rx = rx
        self.ry = ry
        self.x_center = x_center
        self.y_center = y_center

    def draw(self):
        x = 0
        y = self.ry
        self.symmetry(x, y)
        p1o = self.ry**2 - self.rx**2*self.ry + self.rx**2/4
        while 2*self.ry**2*x < 2*self.rx**2*y:
            if p1o < 0:
                x = x+1
                self.symmetry(x, y)
                p1o = p1o + 2*self.ry**2*x + self.ry**2
            else:
                x = x + 1
                y = y - 1
                self.symmetry(x, y)
                p1o = p1o + 2*self.ry**2*x - 2*self.rx**2*y + self.ry**2
        p2o = (self.ry*(x+0.5))**2 + (self.rx*(y-1))**2 - (self.rx*self.ry)**2
        while y != 0:
            if p2o > 0:
                y -= 1
                self.symmetry(x, y)
                p2o = p2o - 2*self.rx**2*y + self.rx**2
            else:
                x += 1
                y -= 1
                self.symmetry(x, y)
                p2o = p2o + 2*self.ry**2*x - 2*self.rx**2*y + self.rx**2
            

    def symmetry(self, x, y):
        self.add_center(x, y)
        self.add_center(-x, y)
        self.add_center(x, -y)
        self.add_center(-x, -y)

    def add_center(self, x, y):
        glVertex2i(x+self.x_center, y+self.y_center)

def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-150.0, 150.0,-150.0,150.0)

def draw_axis():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    glPointSize(2.0)
    glBegin(GL_LINES)
    glVertex2f(150,0)
    glVertex2f(-150,0)
    glVertex2f(0,150)
    glVertex2f(0,-150)
    glEnd()
    glFlush()
    draw_ellipse()

def draw_ellipse():
    glColor3f(0.8,0.8,0.8)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    Ellipse(70,50,10,10).draw()
    glEnd()
    glFlush()


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Drawing")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(draw_axis)
    clearScreen()
    glutMainLoop()