from microbit import *
class Lantern:
    def __init__(self):
        self.intensity = 1
        self.exit = False
        self.hasChange = True
        self.numero = 0
        self.update()


    def update(self):
        while self.exit is False:
            self.checkButtons()

            if self.hasChange:
                display.show(self.makeImage(str(self.intensity)))
                #display.show(str(self.intensity))
                self.toggleHasChange()

    def makeImage(self,intensity):
        temp = ''
        for i in range(0,5):
            temp += intensity

        return Image(temp + ":" +temp + ":" +temp + ":" +temp + ":" +temp)


    def checkButtons(self):

        if button_b.was_pressed():
            self.moreIntensity()
        elif button_a.was_pressed():
            self.lessIntensity()



    def moreIntensity(self):
        if self.intensity < 9:
            self.intensity += 1
            self.toggleHasChange()

    def lessIntensity(self):
        if self.intensity > 0:
            self.intensity -= 1
            self.toggleHasChange()

    def toggleHasChange(self):
        if self.hasChange:
            self.hasChange = False
        else:
            self.hasChange = True


    def close(self):
        self.exit = True
