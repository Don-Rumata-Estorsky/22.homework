"""
реализация класса ship и его придатков Фригат, дестроир, крусадёр,
или же как я перестал бояться и полюбил ядерную бомбу
"""
class Ship:

    def __init__(self, name, country, dislocation, crew):

        self.name = name
        self.country = country
        self.dislocation = dislocation
        self.crew = crew

    def info(self):
        print("")
        print(f"Корабль: {self.name}")
        print(f"Страна: {self.country}")
        print(f"Дислокация: {self.dislocation} ")
        print(f"Экипаж: {self.crew} чел")
        

class Frigate(Ship):

    def __init__(self, name, country, dislocation, crew, armament):

        super().__init__(name, country, dislocation, crew)
        self.armament = armament

    def info(self):

        super().info()
        print("")
        print(f"Вооружение:")
        
        print( self.armament)
        print("")


class Destroyer(Ship):

    def __init__(self, name, country, dislocation, crew, missiles):

        super().__init__(name, country, dislocation, crew)
        self.missiles = missiles

    def fire_missiles(self):
        print("")
        print(f"Эсминец {self.name} выпускает ракеты!")
        print("")


class Cruiser(Ship):

    def __init__(self, name, country, dislocation, crew, air_group):

        super().__init__(name, country, dislocation, crew)
        self.air_group = air_group

    def launch_aircraft(self):
        print("")
        print(f"Крейсер {self.name} запускает самолеты!")


if __name__ == "__main__":


    fregat = Frigate("Большая лодка 39", "Russia", "Северо-запад", 500,  "торпедные аппараты")
    fregat.info()

    destroyer = Destroyer("Уничтожитель 121", "China", "Юго-восток", 950, 80)
    destroyer.info()
    destroyer.fire_missiles()

    cruiser = Cruiser("Авионосец 22", "USA", "Запад", 300, "ракеты: воздух -> вода")
    cruiser.info()
    cruiser.launch_aircraft()
    print("")
    print("We'll meet Again, dont no were, dont no when...")        
    print("")