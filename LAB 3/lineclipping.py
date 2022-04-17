import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

xmin = 10
xmax = 150
ymin = 10
ymax = 100
vertices = [[150,0],[100,50]]


class Boundary:

    def __init__(self,xmin,xmax,ymin,ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def cohensutherland(self, start:list, end:list):
        startTBRL = self.getTBRL(start)
        # print(startTBRL)
        endTBRL = self.getTBRL(end)
        # print(endTBRL)
        m = (end[1]- start[1]) / (end[0] - start[0]) if end[0] - start[0] != 0  else 100 #consider 100 as max slope
        if startTBRL == endTBRL == '0000':
            # print('trivially accepted')
            # glVertex2f(start[0], start[1])
            # glVertex2f(end[0], end[1])
            return [start,end]
        else:
            andTBRL = ''
            for i in range(4):
                k = int(startTBRL[i]) and int(endTBRL[i])
                andTBRL = andTBRL + (str(k))
            # print(andTBRL)
            if andTBRL != '0000':
                # print('not accepted')
                # glVertex2f(start[0], start[1])
                # glVertex2f(end[0], end[1])
                # print(start,end)
                return [[0,0],[0,0]]
            else:
                if startTBRL != '0000':
                    if startTBRL[3] == '1':
                        self.leftclip(start,end,m)
                        
                    elif startTBRL[2] == '1':
                        self.rightclip(start,end,m)
                        
                    elif startTBRL[1] == '1':
                        self.bottomclip(start,end,m)
                        
                    elif startTBRL[0] == '1':
                        self.topclip(start,end,m)
                        
                elif endTBRL != '0000':
                    if endTBRL[3] == '1':
                        self.leftclip(end,start,m)
                    elif endTBRL[2] == '1':
                        self.rightclip(end,start,m)
                    elif endTBRL[1] == '1':
                        self.bottomclip(end,start,m)
                    elif endTBRL[0] == '1':
                        self.topclip(end,start,m)

    def lianbarsky(self, start, end):
        pass
                        
    def leftclip(self, start, end, m):
        start[1] = round(start[1] + m*(self.xmin- start[0]))
        start[0] = self.xmin
        self.cohensutherland(start,end)

    def rightclip(self, start, end, m):
        start[1] = round(start[1] + m*(self.xmax - start[0]))
        start[0] = self.xmax
        self.cohensutherland(start,end)

    def bottomclip(self, start, end, m):
        start[0] = round(start[0] + (self.ymin - start[1])/m)
        start[1] = self.ymin
        self.cohensutherland(start,end)

    def topclip(self, start, end, m):
        start[0] = round(start[0] + (self.ymax - start[1])/m)
        start[1] = self.ymax
        self.cohensutherland(start,end)
    
    def getTBRL(self, vertex):
        l = '1' if self.xmin > vertex[0] else '0'
        r = '1' if self.xmax < vertex[0] else '0'
        b = '1' if self.ymin > vertex[1] else '0'
        t = '1' if self.ymax < vertex[1] else '0'
        return t+b+r+l


def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-150.0, 150.0,-150.0,150.0)

def mouse(button,state,x,y):
    global vertices
    if (button == GLUT_LEFT_BUTTON):       
        vertices = list(Boundary(xmin,xmax,ymin,ymax).cohensutherland(vertices[0],vertices[1]))
        glutPostRedisplay()

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
    glVertex2f(vertices[0][0], vertices[0][1])
    glVertex2f(vertices[1][0], vertices[1][1])
    glutMouseFunc(mouse)
    # Boundary(xmin,xmax,ymin,ymax).cohensutherland(vertices[0],vertices[1])
    glEnd()

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
    glutCreateWindow("Windmill")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(draw_axis)
    clearScreen()
    glutMainLoop()



    

    

        