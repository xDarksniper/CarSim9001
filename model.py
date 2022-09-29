from random import randint

class Car(object):
    pass

class Wheel(object):
    def __int__(self):
        self.orientaion = randint(0,360)

    def rotate(self, revolutions):
        degreesOfRotation = 360 * revolutions
        self.orientaion = (self.orientaion + degreesOfRotation) %360



    pass

class Engine(object):
    pass

class Gearbox(object):
    pass

class Tank(object):

    def __int__(self):
        self.capacity = 100
        self.contents = 100

    def refuel(self):
        self.contents = self.capacity

    def remove(self, amount):
        self.contents = self.contents - amount
        if self.contents < 0:
            self.contents = 0

        pass
