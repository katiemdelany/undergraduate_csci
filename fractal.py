 # Kathleen Delany delan270
 #
 # I understand that this is a graded, individual examination that may not be
 # discussed with anyone. I also understand that obtaining solutions or
 # partial solutions from outside sources, or discussing any aspect of the exam
 # with anyone is academic misconduct and will result in failing the course.
 # I further certify that this program represents my own work and that none of
 # it was obtained from any source other than the material presented as part of the
 # course.

from complex import Complex
from mandelbrot import Mandelbrot
import turtle

class Display:
    def __init__(self):

        self.imagesizeX = 300
        self.imagesizeY = 300
        self.canvwidth = 300
        self.canvlength = 300
        self.curcanvwidthpos = 150
        self.curcanvlengthpos = 150
        self.curcanvwidthneg = -150
        self.curcanvlengthneg = -150
        self.xzoom = 1
        self.yzoom = 1
        self.conx = 0
        self.cony = 0
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.speed(0)
        self.t.pensize(1)
        self.screen = self.t.getscreen()
        self.screen.setup(self.imagesizeX,self.imagesizeY)
        self.screen.screensize(self.canvwidth,self.canvlength)
        self.screen.tracer(2000,0)
        self.screen.onclick(self.click)
        self.screen.listen()
        self.isdrawing = False
        self.__draw__()


    def click(self,x,y):
        if (x < self.canvwidth/2 and x > -self.canvwidth/2 and y < self.canvlength/2 and y > -self.canvlength/2):
            if self.isdrawing == False:
                self.conx = x/100
                self.cony = y/100
                #unused code for attempts at centering screen on mouse click
                # self.curcanvwidthpos+=x
                # self.curcanvlengthpos+=y
                # self.curcanvwidthneg+=x
                # self.curcanvlengthneg+=y
                self.__zoom__()
                self.__draw__()


    def __zoom__(self):
        if self.xzoom == 1 and self.yzoom == 1:
            self.xzoom +=1
            self.yzoom +=1
        else:
            self.xzoom +=2
            self.yzoom +=2

        self.conx = self.conx/2
        self.cony = self.cony/2


    def __draw__(self):
        self.t.clear()
        self.t.penup()
        for i in range(int(self.curcanvwidthneg), int(self.curcanvwidthpos)):
            for j in range(int(self.curcanvlengthneg), int(self.curcanvlengthpos)):
                self.isdrawing = True
                coni = i/100/self.xzoom
                conj = j/100/self.yzoom
                complexnum = Complex(coni,conj)
                mandelseq = Mandelbrot(complexnum,50)
                ColorPoint = str(mandelseq.__get_color__())
                self.t.goto(i,j)
                self.t.pendown()
                self.t.color(ColorPoint)
                self.t.forward(1)
                self.t.penup()
        self.isdrawing = False

def main():
    Display()

if __name__ == '__main__':
    main()
