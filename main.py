from microbit import *
from lantern import Lantern
from paint import Paint

apps = [Lantern,Paint]
finalPosition = 0

class Main:
    def __init__(self):
        self.position = 0
        self.exit = False
        self.maxPosition = 2
        self.update()

    def update(self):
        while self.exit is False:

            self.checkButtons()

            if self.position == 0:
                display.show("L")

            elif self.position == 1:
                display.show("P")

            if self.checkAccelerometer():
                self.close()

    def close(self):
        global finalPosition
        self.exit = True
        finalPosition = self.position
        display.clear()

    def nextApp(self):
        if self.position < 2:
            self.position += 1

    def beforeApp(self):
        if self.position > 0:
            self.position -= 1

    def getPosition(self):
        return self.position

    def checkButtons(self):
        if button_a.was_pressed():
            self.beforeApp()

        elif button_b.was_pressed():
            self.nextApp()

    def checkAccelerometer(self):
        if accelerometer.get_y() < -40:
            return True

Main()
apps[finalPosition]()
