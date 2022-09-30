from random import randint

class Car(object):
    pass

class Wheel(object):
    def __int__(self):
        self.orientaion = randint(0,360)

    def rotate(self, revolutions):
        degreesOfRotation = 360 * revolutions
        self.orientaion = (self.orientaion + degreesOfRotation) %360




class Engine(object):
    pass

class Gearbox(object):
    def shiftUp(self):
        pass

    def ShiftDown(self):
        pass

    def __init__(self):
        self.wheels = {}
        for newWheel in ['frontLeft', 'frontRight','rearLeft', 'rearRight']:
            self.wheels[newWheel] = Wheel()
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]
        self.clutchEngaged = False
        self.currentGear = 0


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
