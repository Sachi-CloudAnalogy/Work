#inheritance
class Car:     #parent class
    color = "blue"

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class Maruti(Car):     #child class
    def __init__(self, name):
        self.name = name

car1 = Maruti("Swift")
print(car1.name)
car1.start()
car1.stop()
print(car1.color)

#types - single, multi level, multiple

class Toyota(Maruti):
    def __init__(self, type, name):
        super().__init__(name)
        self.type = type

car2 = Toyota("Electric", "Fortuner")
print(car2.type)
print(car2.name)
car2.start()
