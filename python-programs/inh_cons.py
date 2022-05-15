# inheriting constructor
class Phone :
    def __init__(self, name, price, camera) :
        print('inside phone constructor')
        self.name = name
        self.price = price
        self.camera = camera

class SmartPhone(Phone) :
    pass

ph1 = SmartPhone('Apple', 100000, 60)