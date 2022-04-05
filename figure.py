from abc import ABC, abstractmethod
class Figure(ABC):# ABC decimos que es abstracto
    @abstractmethod #metodo abstracto
    def area(self):
        pass
    @abstractmethod #metodo abstracto
    def perimeter(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    def greet(self): #No abstracta puedo usar todas las figuras pq se hereda.
        print("Hola, soy un " + self.get_type())