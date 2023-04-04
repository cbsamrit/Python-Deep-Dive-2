import math

class circle :

    def __init__ (self,r):
        self.radius=r
    
    @property
    def radius(self) :

        return self.radius
    
    @radius.setter
    def radius(self,r):
     self.radius=r
     self.area=math.pi* r**2