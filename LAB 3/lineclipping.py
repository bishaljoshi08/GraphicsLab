
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

xmin = 10
xmax = 150
ymin = 10
ymax = 100
vertices = [[0,0],[-100,-110]]


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
            print(start,end)
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
                return []
            else:
                if startTBRL != '0000':
                    if startTBRL[3] == '1':
                        return self.leftclip(start,end,m)     
                    elif startTBRL[2] == '1':
                        return self.rightclip(start,end,m)
                        
                    elif startTBRL[1] == '1':
                        return self.bottomclip(start,end,m)
                        
                    elif startTBRL[0] == '1':
                        return self.topclip(start,end,m)
                        
                elif endTBRL != '0000':
                    if endTBRL[3] == '1':
                        return self.leftclip(end,start,m)
                    elif endTBRL[2] == '1':
                        return self.rightclip(end,start,m)
                    elif endTBRL[1] == '1':
                        return self.bottomclip(end,start,m)
                    elif endTBRL[0] == '1':
                        return self.topclip(end,start,m)

    def lianbarsky(self, start, end):
        p=[None,None,None,None]
        q=[None,None,None,None]
        r = [None,None,None,None]
        p_less_than_zero = [0,0,0,0]
        p_greater_than_zero = [1,1,1,1]
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        p[0] = -dx
        p[1] = dx
        p[2] = -dy
        p[3] = dy
        q[0] = start[0] - self.xmin
        q[1] = self.xmax - start[0]
        q[2] = start[1] - self.ymin
        q[3] = self.ymax - start[1]
        for i in range(4):
            if p[i] == 0 and q[i] < 0 :
                print('reject')
                return []
            elif p[i] == 0 and q[i] >= 0:
                pass
            else:
                r[i]=q[i]/p[i]
        for i in range(4):
            if p[i] < 0 :
                p_less_than_zero[i] = r[i]
            elif p[i] > 0:
                p_greater_than_zero[i] = r[i]
        u1 = max(p_less_than_zero)
        u2 = min(p_greater_than_zero)
        clipped_start = [None,None]
        clipped_end = [None,None]
        if u1 > u2:
            print('rejected')
            return []
        else:
            clipped_start[0] = start[0]+u1*dx
            clipped_start[1] = start[1]+u1*dy
            clipped_end[0] = start[0]+u2*dx
            clipped_end[1] = start[1]+u2*dy
            print(clipped_start,clipped_end)
            return [clipped_start,clipped_end]

                        
    def leftclip(self, start, end, m):
        start[1] = round(start[1] + m*(self.xmin- start[0]))
        start[0] = self.xmin
        return self.cohensutherland(start,end)

    def rightclip(self, start, end, m):
        start[1] = round(start[1] + m*(self.xmax - start[0]))
        start[0] = self.xmax
        return self.cohensutherland(start,end)

    def bottomclip(self, start, end, m):
        start[0] = round(start[0] + (self.ymin - start[1])/m)
        start[1] = self.ymin
        return self.cohensutherland(start,end)

    def topclip(self, start, end, m):
        start[0] = round(start[0] + (self.ymax - start[1])/m)
        start[1] = self.ymax
        return self.cohensutherland(start,end)

    
    
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
    b = Boundary(xmin,xmax,ymin,ymax)
    if (button == GLUT_LEFT_BUTTON):       
        vertices = b.cohensutherland(vertices[0],vertices[1])
        glutPostRedisplay()
    elif (button == GLUT_RIGHT_BUTTON):
        vertices = b.lianbarsky(vertices[0],vertices[1])
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
    if vertices:
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
    glutCreateWindow("Line Clipping")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(draw_axis)
    clearScreen()
    glutMainLoop()



    

    

        