from microbit import *
class Paint:
    def __init__(self):
        # save the canvas by position. [x][y]
        self.canvas = [[0 for x in range(0,5)] for y in range(0,5)]
        self.hasChange = False
        self.canPrint = False
        # save the current position. [x,y]
        self.position = [0,0]
        self.lastPosition = [0,0]
        self.exit = False
        self.update()

    def update(self):
        self.changePosition()
        while self.exit is False:

            self.checkAccelerometer()

            self.checkButtons()

            if self.hasChange:
                self.changePosition()
                self.toggleHasChange()


    def checkButtons(self):
        # move to bottom
        self.lastPosition[1] = self.position[1]
        self.lastPosition[0] = self.position[0]
        if button_a.was_pressed():
            if  self.position[1] < 4:
                self.position[1] += 1
            else:
                self.position[1] = 0
            self.toggleHasChange()

        if button_b.was_pressed():
            if self.position[0] < 4:
                self.position[0] += 1
            else:
                self.position[0] = 0
            self.toggleHasChange()

    def checkAccelerometer(self):
        if accelerometer.get_y() < -40 and self.canPrint:
            if self.canvas[self.position[0]][self.position[1]]:
                self.canvas[self.position[0]][self.position[1]] = False
            else:
                self.canvas[self.position[0]][self.position[1]] = True
            self.canPrint = False
        if accelerometer.get_y() > 0:
            self.canPrint = True


    def changePosition(self):
        if self.canvas[self.lastPosition[0]][self.lastPosition[1]]:
            display.set_pixel(self.lastPosition[0],self.lastPosition[1],5)
        else:
            display.set_pixel(self.lastPosition[0],self.lastPosition[1],0)
        #display.set_pixel(self.lastPosition[0],self.lastPosition[1],0)
        display.set_pixel(self.position[0],self.position[1],9)

    def toggleHasChange(self):
        if self.hasChange:
            self.hasChange = False
        else:
            self.hasChange = True
