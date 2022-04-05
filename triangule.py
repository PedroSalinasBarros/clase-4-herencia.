from figure import Figure

class Triangle (Figure):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura / 2

    def perimeter(self):
        return 3*self.base

    def get_type(self):
        return "Triangulo Equilatero"