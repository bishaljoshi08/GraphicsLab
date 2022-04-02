class Circle:
    def __init__(self,center_x,center_y,radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        

    def mid_point(self):
        self.x = 0
        self.y = round(self.radius)
        self.add_center()
        if isinstance(self.radius, int):
            p0 = 1 - self.radius
            print(p0)
        elif isinstance(self.radius, float):
            p0 = 5/4 - self.radius
        while not self.x >= self.y:
            if p0 < 0:
                print('a')
                self.x += 1
                p0 = p0 + 2*self.x +1
            else:
                self.x += 1
                self.y -= 1
                p0 = p0 + 2*self.x +1 -2*self.y
            self.add_center()
            
    def add_center(self):
        self.xadd = self.center_x + self.x
        self.yadd = self.center_y + self.y
        self.eight_point_symmetry()

    def eight_point_symmetry(self):
        print(self.xadd,self.yadd)
        print(-1*self.xadd,self.yadd)
        print(self.xadd,-1*self.yadd)
        print(-1*self.xadd,-1*self.yadd)
        print(self.yadd,self.xadd)
        print(-1*self.yadd, self.xadd)
        print(self.yadd, -1*self.xadd)
        print(-1*self.yadd,-1*self.xadd)

c = Circle(100,100,8)
c.mid_point()