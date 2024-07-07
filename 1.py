




"""

"""
class Devices:
    def __init__(self, device, power, price  ):
        self.device = device
        self.power = power
        self.price = price


class CoffeeMachine(Devices):
    def __init__(self, device, power, price, assortment):
        super().__init__(device, power, price, )
        self.assortment = assortment

    def device_name(self):
        return f"{self.device}"

    def device_power(self):
        return f"{self.power}"
    
    def device_price(self):
        return f"{self.price}"    
    
    def pet_type_show(self):
        return f"{self.assortment}"
    
    def info(self):
         return f"The {self.device} have {self.power} VAT of power, price={self.price}$. can giv you {self.assortment} ."

class Blender(Devices):
    def __init__(self, device, power, price, spin_speed ):
        super().__init__(device, power, price, )
        self.spin_speed = spin_speed
    
    def device_name(self):
        return f"{self.device}"

    def device_power(self):
        return f"{self.power}"
    
    def device_price(self):
        return f"{self.price}"
    
    def device_spin_speed(self):
        return f"{self.spin_speed}"
    
    def info(self):
         return f"The {self.device} have {self.power} VAT of power, price={self.price}$. have spin speed={self.spin_speed} per second ."
 

class MeatGrinder(Devices):
    def __init__(self, device, power, price, meat ):
        super().__init__(device, power, price, )
        self.meat = meat

    def device_name(self):
        return f"{self.device}"

    def device_power(self):
        return f"{self.power}"
    
    def device_price(self):
        return f"{self.price}"
    
    def type_of_meat(self):
        return f"{self.meat}"   
    
    def info(self):
        return f"The {self.device} have {self.power} VAT of power, price={self.price}$. can giv you {self.meat} ."

  
if __name__ == "__main__":

    cofe = CoffeeMachine("CoffeeMachine", 100, 200, "Late, Expresso, CapuchiNO", )
    print("")
    print(cofe.device_name())
    print(cofe.info())
    print("")
  

    blender = Blender("Blender3000", 300, 300, 12 )

    print(blender.device_name())
    print(blender.info())
    print("")

    meatrub = MeatGrinder("MeatGrinder", 400, 500, "farsh (baran)" )

    print(meatrub.device_name())
    print(meatrub.info())
    print("")
















