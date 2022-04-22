import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from lineclipping import Boundary as bound

xmin = -50
xmax = 50
ymin = -50
ymax = 50
vs = [[0,50],[-100,-100],[100,-50]]
vs_copy = []


class Boundary:

    def __init__(self,xmin,xmax,ymin,ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    # def polygonclipping(self):
        
    # def topboundary(self,point):

    # def rightboundary(self,point):
    # def bottomboundary(self,point):
    # def leftboundary(self,point):
def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-150.0, 150.0,-150.0,150.0)

def drawboundary():
    # glClear(GL_COLOR_BUFFER_BIT)
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
    glBegin(GL_POLYGON)
    for vertex in vs:
        glVertex2f(vertex[0],vertex[1])
    glEnd()
    

    glutMouseFunc(mouse)
    # Boundary(xmin,xmax,ymin,ymax).cohensutherland(vs[0],vs[1])
    # glEnd()

def mouse(button,state,x,y):
    global vs
    global vs_copy
    print(f'first {vs}')
    b = bound(xmin,xmax,ymin,ymax)
    # print(vs)
    if (button == GLUT_LEFT_BUTTON):
        # v = []
        for index,vertex in enumerate(vs):
            v = list(b.lianbarsky(vs[index],vs[(index+1)%len(vs)]))
            print(vs)
            # print('a')
            # print(v)
            if v:
                vertex0 = v[0]
                vertex1 = v[1]
                if vertex0 not in vs_copy:
                    vs_copy.append(vertex0)
                if vertex1 not in vs_copy:
                    vs_copy.append(vertex1)
        # print(vs_copy)
        vs = vs_copy
        glutPostRedisplay()

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
    drawboundary()
    glFlush()
    
    
if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Line Clipping")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(draw_axis)
    clearScreen()
    glutMainLoop()
