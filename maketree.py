import turtle
from tkinter import *
import os
import random

# need a function to delete the eps file


# add functions that determine the color scheme for a row
# add functions that store necessary data onto a file


# DRAWING FUNCTIONS
def draw_pixel(artist, size = 10, pencolor = 'black', fillcolor = 'white'):
	"draws a pixel of given size with pencolor and fillcolor"

	artist.color(pencolor,fillcolor) # sets fill colors
	artist.begin_fill() 

	# begins drawing the pixel
	for i in range(4):
		artist.forward(size)
		artist.left(90)

	artist.end_fill()

def draw_row(artist, length, colors, size = 10):
	"draws a row of pixel with length number of pixels. the color of each pixel is passed in as a list"

	for i in range(length):
		color = main_colors[colors[i]]
		draw_pixel(artist, size, color, color)
		artist.forward(size)

def move_up_row(artist, prevrowlength, size = 10):
	"moves artist up to a new row to draw the tree"
	artist.left(90)
	artist.forward(size)
	artist.left(90)
	artist.forward(size * (prevrowlength))
	artist.left(180)
	artist.forward(size//2)

def draw_tree(artist, colors, start_size = 20):
	"this function draws the christmas tree"

	while start_size != 0:
		draw_row(artist, start_size, colors[20-start_size])
		move_up_row(artist, start_size)
		start_size -= 1

def draw_trunk(artist, colors  = ['brown', 'brown', 'brown'], size = 10, length = 2):
	"this function draws a trunk for the tree"

	for i in range(4):
		random.shuffle(colors)
		draw_row(artist, 3, colors)
		artist.left(90)
		artist.forward(size)
		artist.left(90)
		artist.forward(size * length)
		artist.left(180)

def draw_circle(artist):
	"this function draws a yellow circle on top of the tree"

	artist.color('orange','yellow')
	artist.begin_fill()
	artist.circle(7)
	artist.end_fill()

def draw_greeting(artist):
	"this function writes the greeting on top"

	artist.penup()
	artist.left(90)
	artist.forward(100)
	artist.left(90)
	artist.forward(170)
	artist.left(180)
	artist.pendown()
	artist.color('red')
	artist.write("Merry Christmas", font = ('Times', 50, 'bold'))

def draw_recepient(artist):
	"this function writes the name of the recepient"

	artist.penup()
	artist.setpos(0,-80)
	artist.left(90)
	artist.forward(210)
	artist.left(90)
	artist.forward(5*7)
	artist.left(180)
	artist.pendown()
	artist.color("red")
	artist.write("Elton", font = ('Courier', 40, 'bold'))


def draw_signature(artist):
	"this function writes a signtaure at the bottom"

	artist.penup()
	artist.color('blue')
	artist.setpos(0,-80)
	artist.right(90)
	artist.forward(140)
	artist.right(90)
	artist.forward(11*7)
	artist.right(180)
	artist.pendown()
	artist.write("from Evonne", font = ('Courier', 30, 'bold'))



# POSITIONING FUNCTIONS

def position_trunk(artist, size = 10):
	"positions the artist so that the trunk can be drawn in the correct position"

	artist.penup()
	artist.right(90)
	artist.forward(size * 7)
	artist.left(90)
	artist.pendown()

def position_tree(artist, size = 10):
	"positions the artist so that the tree can be drawn in the correct position"

	artist.penup()
	artist.left(180)
	artist.forward(size*9)
	artist.left(180)
	artist.pendown()

# COLOR DETERMINATION FUNCTIONS

def add_greenrows():
	"creates a list of lists with color combinations for shades of green"

	green_rows = []

	for i in range(20):
		green_rows.append([random.randrange(0,6) for x in range(20-i)])

	return green_rows


def add_bobtails(ls):
	"creates a list of lists that adds bobtail colors to the list returned by add_greenrows()"

	bobtail_rows = []
	count = 0

	rows = [[19,17,16,14,12,9,7,5,3,2],
			[18,16,15,13,11,8,6,4,2,1],
			[19,18,15,13,11,8,6,4,2,1],
			[18,17,15,14,11,8,7,5,3,2]
			]
	bobtail_rows = rows[random.randrange(0,4)]

	for row in bobtail_rows:
		no_of_bobtails = 0
		count2 = 0

		if row <= 7:
			no_of_bobtails = 3
		elif row <=15:
			no_of_bobtails = 2
		else:
			no_of_bobtails = 1

		distance_factor = int((20-row)/(no_of_bobtails))

		indexes = [x for x in range(20-row-1)]
		random.shuffle(indexes)
		
		count2 = 0
		bobtail_loc = []

		for index in indexes:
			if count2 >= no_of_bobtails:
				break
			flag = True
			for loc in bobtail_loc:
				if abs(index-loc) < distance_factor:
					flag = False
					break
			if flag:
				bobtail_loc.append(index)
				count2 += 1

		for loc in bobtail_loc:
			ls[row][loc] = random.randrange(6,10)

	return ls

# HASH FUNCTIONS

def create_hash():
	pass

def next_pattern():
	pass

# SAVE IMAGE

def save_img(artist):
	"saves the turtle graphic to jpg image generated with unique name"

	ps =  artist.getscreen().getcanvas().postscript(file = "test.ps", colormode = 'color')
	os.system('convert ' + 'test.ps' + ' ' + 'test.png')


main_colors = {
		  0:'#228B22', # forestgreen
		  1:'#008000', # green
		  2:'#006400', # darkgreen
		  3:'#2E8B57', # seagreen
		  4:'#6B8E23', # darkolivegreen
		  5:'#556B2F', # olivedrab
		  6:'#00ccff', # deepskyblue
		  7:'#FF0000', # neon red
		  8:'#ff99ff', # pink
		  9:'#FFFF33', # neon yellow
		  10:'#A0522D', # sienna
		  11:'#8B4513', # saddlebrown
		  12:'#A52A2A', # brown
	      13:'#D2691E'  # chocolate
		 }

#---- INIT ---- #

wn = turtle.Screen()
santa = turtle.Turtle() # creates a turtle names santa

santa.penup()
santa.hideturtle() # hides santa
santa.setpos(0,-80)
santa.speed(0)
santa.pensize(0)
santa.pendown()

position_trunk(santa)
draw_trunk(santa, list(main_colors.keys())[-4:], length = 3, )
position_tree(santa)
draw_tree(santa,add_bobtails(add_greenrows()))
draw_circle(santa)
draw_greeting(santa)
draw_recepient(santa)
draw_signature(santa)

save_img(santa)
os.system('open ' + 'test.png')