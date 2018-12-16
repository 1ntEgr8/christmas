import turtle
from tkinter import *
from PIL import Image
import os

alex = turtle.Turtle()

alex.forward(100)
alex.left(100)

ts = turtle.getscreen()

ps = ts.getcanvas().postscript(file = "duck.eps", colormode = 'color')

os.system('convert ' + 'duck.eps' + ' ' + "duck.jpg")
