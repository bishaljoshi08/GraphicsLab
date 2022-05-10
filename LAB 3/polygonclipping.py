import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

xmin = -50
xmax = 50
ymin = -50
ymax = 50
vs = [[0,50],[-100,-100],[100,-60]]
vs_copy = []


class Boundary:

    def __init__(self,xmin,xmax,ymin,ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.vs = vs[:]
        self.vs_copy = vs_copy[:]

    def reset(self):
        self.vs = self.vs_copy[:]
        self.vs_copy.clear()

    def polygonclipping(self):
        for i in range(len(self.vs)):
            pair = [self.vs[i-1],self.vs[i]]
            self.leftboundary(pair)
        self.reset()
        for i in range(len(self.vs)):
            pair = [self.vs[i-1],self.vs[i]]
            self.topboundary(pair)
        self.reset()
        for i in range(len(self.vs)):
            pair = [self.vs[i-1],self.vs[i]]
            self.rightboundary(pair)
        self.reset()
        for i in range(len(self.vs)):
            pair = [self.vs[i-1],self.vs[i]]
            self.bottomboundary(pair)
        self.reset()
        return self.vs
        
    def leftboundary(self,pair):
        v1,v2 = pair
        if v1[0] < self.xmin and v2[0] < self.xmin:
            pass
        elif v1[0] >= self.xmin and v2[0] >= self.xmin:
            self.vs_copy.append(v1)
            self.vs_copy.append(v2)
        elif v1[0] >= self.xmin and v2[0] < self.xmin:
            m = (v2[1] - v1[1]) / (v2[0] - v1[0]) if v2[0] - v1[0] != 0 else sys.maxsize
            y_clip = m*(self.xmin - v1[0]) + v1[1]
            self.vs_copy.append([self.xmin,y_clip])
        elif v1[0] < self.xmin and v2[0] >= self.xmin:
            m = (v2[1] - v1[1]) / (v2[0] - v1[0]) if v2[0] - v1[0] != 0 else sys.maxsize
            y_clip = m*(self.xmin - v1[0]) + v1[1]
            self.vs_copy.append([self.xmin,y_clip])
            self.vs_copy.append(v2)

    def topboundary(self,pair):
        v1,v2 = pair
        if v1[1] > self.ymax and v2[1] > self.ymax:
            pass
        elif v1[1] <= self.ymax and v2[1] <= self.ymax:
            self.vs_copy.append(v1)
            self.vs_copy.append(v2)
        elif v1[1] <= self.ymax and v2[1] > self.ymax:
            m = (v2[1] - v1[1]) / (v2[0] - v1[0]) if v2[0] - v1[0] != 0 else sys.maxsize
            x_clip = ((self.ymax - v1[1]) / m) + v1[0]
            self.vs_copy.append([x_clip, self.ymax])
        elif v1[1] > self.ymax and v2[1] <= self.ymax:
            m = (v2[1] - v1[1]) / (v2[0] - v1[0]) if v2[0] - v1[0] != 0 else sys.maxsize
            x_clip = ((self.ymax - v1[1]) / m) + v1[0]
            self.vs_copy.append([x_clip, self.ymax])
            self.vs_copy.append(v2)
        


    def rightboundary(self,pair):
        v1,v2 = pair
        if v1[0] <= self.xmax and v2[0] <= self.xmax:
            self.vs_copy.append(v1)
            self.vs_copy.append(v2)
        elif v1[0] > self.xmax and v2[0] > self.xmax:
            pass
        elif v1[0] > self.xmax and v2[0] <= self.xmax:
            m = (v2[1] - v1[1]) / (v2[0] - v1[0]) if v2[0] - v1[0] != 0 else sys.maxsize
            y_clip = m*(self.xmax - v1[0]) + v1[1]
            self.vs_copy.append([self.xmax,y_clip])
            self.vs_copy.append(v2)
        elif v1[0] <= self.xmax and v2[0] > self.xmax:
            m = (v2[1] - v1[1]) / (v2[0] - v1[0]) if v2[0] - v1[0] != 0 else sys.maxsize
            y_clip = m*(self.xmax - v1[0]) + v1[1]
            self.vs_copy.append([self.xmax,y_clip])

    def bottomboundary(self,pair):
        v1,v2 = pair
        if v1[1] >= self.ymin and v2[1] >= self.ymin:
            self.vs_copy.append(v1)
            self.vs_copy.append(v2)
        elif v1[1] < self.ymin and v2[1] < self.ymin:
            pass
        elif v1[1] < self.ymin and v2[1] >= self.ymin:
            m = (v2[1] - v1[1]) / (v2[0] - v1[0]) if v2[0] - v1[0] != 0 else sys.maxsize
            x_clip = ((self.ymin - v1[1]) / m) + v1[0]
            self.vs_copy.append([x_clip, self.ymin])
            self.vs_copy.append(v2)
        elif v1[1] >= self.ymin and v2[1] < self.ymin:
            m = (v2[1] - v1[1]) / (v2[0] - v1[0]) if v2[0] - v1[0] != 0 else sys.maxsize
            x_clip = ((self.ymin - v1[1]) / m) + v1[0]
            self.vs_copy.append([x_clip, self.ymin])
            

def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-150.0, 150.0,-150.0,150.0)

def drawboundary():
    # glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    for vertex in vs:
        glVertex2f(vertex[0],vertex[1])
    glEnd()
    glColor3f(0.8,0.8,0.8)
    # glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    glVertex2f(xmin, ymin)
    glVertex2f(xmin, ymax)
    glEnd()
    

    glutMouseFunc(mouse)
    # Boundary(xmin,xmax,ymin,ymax).cohensutherland(vs[0],vs[1])
    # glEnd()

def mouse(button,state,x,y):
    global vs
    global vs_copy
    # print(f'first {vs}')
    # print(vs)
    b = Boundary(xmin, xmax, ymin, ymax)
    if (button == GLUT_LEFT_BUTTON):
        vs = b.polygonclipping()
        glutPostRedisplay()

def draw_axis():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    glPointSize(2.0)
    drawboundary()
    glBegin(GL_LINES)
    glColor3f(0.5,0.9,1.0)
    glVertex2f(150,0)
    glVertex2f(-150,0)
    glVertex2f(0,150)
    glVertex2f(0,-150)
    glEnd()
    glFlush()
    
    
if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Polygon Clipping")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(draw_axis)
    clearScreen()
    glutMainLoop()
