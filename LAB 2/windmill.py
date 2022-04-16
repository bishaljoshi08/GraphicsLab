import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from transformation import Transformation


fin = [[0,0], [20,-50], [-20,-50]]
def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-150.0, 150.0,-150.0,150.0)

def draw_triangle(vertices):
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def draw_windmill():
    support = [[0,0], [30,-130], [-30,-130]]
    global fin
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.8,0.8,0.8)
    draw_triangle(support)
    glColor3f(0.8,0.3,0.5)
    draw_triangle(fin)
    fin = Transformation(fin).rotation(120)
    draw_triangle(fin)
    fin = Transformation(fin).rotation(120)
    draw_triangle(fin)
    fin = Transformation(fin).rotation(0.2)
    glutPostRedisplay()
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Windmill")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(draw_windmill)
    clearScreen()
    glutMainLoop()
