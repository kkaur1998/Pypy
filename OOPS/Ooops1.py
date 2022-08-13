class Vehicle:
    def __init__(self):
        self.mileage = 0
        self.speed = 0


class Fourwheeler(Vehicle):
    def __init__(self):
        self.engine = "Ford"
        

class Twowheeler:
    def __init__(self) -> None:
        pass

if(__name__ == '__main__'):
    obj1= Vehicle()
    obj2 = Fourwheeler()
    print(obj2.engine)
    print(obj1.mileage)
    print(obj1.speed)