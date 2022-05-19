
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from line import Line
from polygram import Polygram

def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-150.0, 150.0,-150.0,150.0)

def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    Polygram(100,n,k).polygram()
    glEnd()
    glFlush()


print("Give the polygram you want to draw in the form of n/k")
global n,k
while(True):
    n = int(input("n: "))
    k = int(input("k: "))
    if k>=1 and n>=3 and 2*k +1 <= n:
        break
    else:
        print('Invalid Format')

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow(f"Polygram {n}/{k}")
glutInitWindowSize(500, 500)
glutInitWindowPosition(50, 50)
glutDisplayFunc(plot_points)
clearScreen()
glutMainLoop()
