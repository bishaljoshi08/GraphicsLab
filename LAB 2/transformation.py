from math import sin, cos, radians

import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = [[110,100],[-120,130],[90,70]]

class Transformation:
    def __init__(self, vertex_matrix):
        for row in vertex_matrix:
            row.append(1)
        zipped_rows = zip(*vertex_matrix)
        self.vertex_matrix = [list(row) for row in zipped_rows]
        

    def translation(self, tx, ty):
        self.transformation_matrix = [[1, 0, tx], [0, 1, ty], [0, 0, 1]]
        return self.getvertex()

    def rotation(self, angle):
        self.transformation_matrix = [[cos(radians(angle)), -sin(radians(angle)), 0], [sin(radians(angle)), cos(radians(angle)), 0], [0, 0, 1]]
        return self.getvertex()

    def scaling(self, sx, sy):
        self.transformation_matrix = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
        return self.getvertex()

    def reflection_xaxis(self):
        self.transformation_matrix = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
        return self.getvertex()

    def reflection_yaxis(self):
        self.transformation_matrix = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]
        return self.getvertex()

    def shearing_xaxis(self, sh):
        self.transformation_matrix = [[1, sh, 0], [0, 1, 0], [0, 0, 1]]
        return self.getvertex()

    def shearing_yaxis(self, sh):
        self.transformation_matrix = [[1, 0, 0], [sh, 1, 0], [0, 0, 1]]
        return self.getvertex()

    def getvertex(self):       
        result = [[sum(a*b for a,b in zip(X_row, Y_col)) for Y_col in zip(*self.vertex_matrix)] for X_row in self.transformation_matrix]   
        zipped_rows = zip(*result[:-1])
        result = [list(row) for row in zipped_rows]
        return result
        
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
    draw_polygon()
        
def draw_polygon():
    glColor3f(0.8,0.8,0.8)
    glPointSize(2.0)
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2i(vertex[0],vertex[1])
    glEnd()
    glFlush()
    transform()

def transform():
    glColor3f(0.8,0.3,0.5)
    glPointSize(2.0)
    result = Transformation(vertices).rotation(90)
    glBegin(GL_POLYGON)
    for vertex in result:
        glVertex2f(vertex[0],vertex[1])
    glEnd()
    result = Transformation(vertices).translation(5,5)
    glBegin(GL_POLYGON)
    for vertex in result:
        glVertex2f(vertex[0],vertex[1])
    glEnd()
    result = Transformation(vertices).scaling(1,-1)
    glBegin(GL_POLYGON)
    for vertex in result:
        glVertex2f(vertex[0],vertex[1])
    glEnd()
    # result = Transformation(vertices).shearing_yaxis(1.2)
    # glBegin(GL_POLYGON)
    # for vertex in result:
    #     glVertex2f(vertex[0],vertex[1])
    # glEnd()
    
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
    # print(Transformation(vertices).rotation(90))


