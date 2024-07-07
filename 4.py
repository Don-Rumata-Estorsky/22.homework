"""
реализация машины, её дверей, колёс  и движка
"""

class Wheel:
   
    def __init__(self, size: int, material: str):
        self.size = size
        self.material = material

    def rotate(self):
        print(f"Колесо размером {self.size} дюйма из {self.material} вращается...")

class Engine:
    def __init__(self, power: int, fuel_type: str):
        self.power = power
        self.fuel_type = fuel_type

    def start(self):
        print(f"Двигатель мощностью {self.power} л.с. на {self.fuel_type} запускается...")

    def accelerate(self):
        print(f"Двигатель набирает обороты...")

class Door:
    def __init__(self, side: str, is_open: bool = False):
        self.side = side
        self.is_open = is_open

    def open(self):
        if self.is_open:
            print(f"{self.side} дверь уже открыта.")
        else:
            print(f"{self.side} дверь открывается...")
            self.is_open = True

    def close(self):
        if not self.is_open:
            print(f"{self.side} дверь уже закрыта.")
        else:
            print(f"{self.side} дверь закрывается...")
            self.is_open = False


class Car(Wheel, Engine, Door):
    def __init__(self, name: str, wheels: list, engine: Engine, doors: list):
        self.name = name
        self.wheels = wheels
        self.engine = engine
        self.doors = doors

    def start(self):
        self.engine.start()
        for door in self.doors:
            door.close()  

    def drive(self):
        print(f"Автомобиль {self.name} едет...")
        for wheel in self.wheels:
            wheel.rotate()

    def open_door(self, side: str):
        for door in self.doors:
            if door.side == side:
                door.open()
                break
        else:
            print(f"В автомобиле {self.name} нет двери с такой стороны: {side}")

car = Car(
    name="Lada",
    wheels=[Wheel(15, "резина")],
    engine=Engine(98, "бензин"),
    doors=[Door("левая"), Door("правая"), Door("задняя левая"), Door("задняя правая")],)

car.start()
car.drive()
car.open_door("левая")