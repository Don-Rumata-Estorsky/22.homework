"""
Используя понятие множественного наследования, 
разработайте класс «Окружность, вписанная в квадрат. 
"""

class krug_in_kvdrat:
    def __init__(self, perimeter, coordinates):
        self.Coordinates = coordinates
        self.krug = "circle"
        self.kvadrat = "square"
        self.perimeter = perimeter

    def infa(self):  
        print("")
        print(f"Coordinates of {self.figura}: {self.Coordinates} на карте каординат XY ")
        print(f"Perimeter of {self.figura}: {self.perimeter} см ")

class Krug(krug_in_kvdrat):
  def __init__(self):
        self.figura = "circle"
        self.Coordinates = "x=11 y=5"
        self.perimeter = 14
        self.radius = 22

  def radius(self):
    print(f"Радиус круга что врисан в квадрат  {self.radius} cм")
      
class Kvadrat(krug_in_kvdrat):
  def __init__(self):
        self.figura = "square"
        self.Coordinates = "x=12 y=4"
        self.perimeter = 23
        self.dlinna_stpron = "side_length"

  def lebght(self):
    print("длинна сторон квадрата равна: ", self.dlinna_stpron, "см2")

if __name__ == "__main__":
    circle = Krug()
    circle.infa()
    circle.radius()

    square = Kvadrat()
    square.infa()
    square.lebght()