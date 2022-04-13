from figure import Figure
from math import pi

class Circle(Figure):
    def __init__(self,radius):
        self.radius=radius
    
    @property
    def radius(self):
        return self.__radius
    @ra
    

    def area(self):
        return pi * self.radius **2

    def perimeter(self):
        return 2*pi*self.radius

    def get_type(self):
        return "Circle"