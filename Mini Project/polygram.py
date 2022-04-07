from math import sin, cos, radians
from line import Line

class Polygram:
    def __init__(self,radius,n,k):
        self.radius = radius
        self.n = n
        self.k = k
    
    def polygram(self):
        self.points = []
        self.point = (0,self.radius)
        self.points.append(self.point)

        for i in range(self.n-1):
            self.rotate()
        self.draw_lines()

    def rotate(self):
        tempx = self.point[0]
        tempy = self.point[1]
        listpoint = list(self.point)
        listpoint[0] = round(cos(radians(360/self.n))* tempx- sin(radians(360/self.n))*tempy)
        listpoint[1] = round(sin(radians(360/self.n)) * tempx + cos(radians(360/self.n))*tempy)
        self.point = tuple(listpoint)
        self.points.append(self.point)

    def draw_lines(self):
        currentpoint = 0
        count = 0
        copylist = self.points[:]
        
        
            
        while (count != self.n):
            if self.points[currentpoint] not in copylist:
                currentpoint+=1
            nextpoint =(currentpoint+self.k)%self.n
            Line(self.points[currentpoint],self.points[nextpoint]).dda()
            copylist.remove(self.points[currentpoint])
            currentpoint = nextpoint
            count += 1
        

        
                
            


