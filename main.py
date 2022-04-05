from circle import Circle
from rectangle import Rectangle
from triangule import Triangle

my_circle=Circle(3)
print(my_circle.area())
my_circle.greet() #puedo usar asi pq python va buscanado por clase de herencia, si no esta en una busca en la anterior

my_rectangle=Rectangle(5,4)
my_rectangle.greet()

my_triangle=Triangle(2,3)
my_triangle.greet()
print("hola")
print("hola")