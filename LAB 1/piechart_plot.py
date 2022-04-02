import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from piechart import Piechart

def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-150.0, 150.0,-150.0,150.0)

def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(3.0)
    glBegin(GL_POINTS)
    Piechart().circle(degreelist)
    glEnd()
    glFlush()

inp = input("Give the frequency number")
inplist = [int(i) for i in inp.split()]
global degreelist
degreelist = []
total = 0
for input in inplist:
    total += input
for input in inplist:
    (degreelist.append(input*360/total)) if total!= 0 else degreelist.append(0)
glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("Drawing")
glutInitWindowSize(500, 500)
glutInitWindowPosition(50, 50)
glutDisplayFunc(plot_points)
clearScreen()
glutMainLoop()