import turtle
from tkinter import *
import os
import random
import time
import datetime

# need a function to delete the eps file


# add functions that determine the color scheme for a row
# add functions that store necessary data onto a file


# DRAWING FUNCTIONS
def draw_pixel(artist, size = 10, pencolor = 'black', fillcolor = 'white'):
	"""draws a pixel of given size with pencolor and fillcolor"""

	artist.color(pencolor,fillcolor) # sets fill colors
	artist.begin_fill() 

	# begins drawing the pixel
	for i in range(4):
		artist.forward(size)
		artist.left(90)

	artist.end_fill()

def draw_row(artist, length, colors, size = 10):
	"""draws a row of pixel with length number of pixels. the color of each pixel is passed in as a list"""

	for i in range(length):
		color = main_colors[colors[i]]
		draw_pixel(artist, size, color, color)
		artist.forward(size)

def move_up_row(artist, prevrowlength, size = 10):
	"""moves artist up to a new row to draw the tree"""
	artist.left(90)
	artist.forward(size)
	artist.left(90)
	artist.forward(size * (prevrowlength))
	artist.left(180)
	artist.forward(size//2)

def draw_tree(artist, colors, start_size = 20):
	"""this function draws the christmas tree"""

	while start_size != 0:
		draw_row(artist, start_size, colors[20-start_size])
		move_up_row(artist, start_size)
		start_size -= 1

def draw_trunk(artist, colors  = ['brown', 'brown', 'brown'], size = 10, length = 2):
	"""this function draws a trunk for the tree"""

	for i in range(4):
		random.shuffle(colors)
		draw_row(artist, 3, colors)
		artist.left(90)
		artist.forward(size)
		artist.left(90)
		artist.forward(size * length)
		artist.left(180)

def draw_circle(artist):
	"""this function draws a yellow circle on top of the tree"""

	artist.color('orange','yellow')
	artist.begin_fill()
	artist.circle(7)
	artist.end_fill()

def draw_greeting(artist):
	"""this function writes the greeting on top"""

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
	"""this function writes the name of the recepient"""

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
	"""this function writes a signtaure at the bottom"""

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
	"""positions the artist so that the trunk can be drawn in the correct position"""

	artist.penup()
	artist.right(90)
	artist.forward(size * 7)
	artist.left(90)
	artist.pendown()

def position_tree(artist, size = 10):
	"""positions the artist so that the tree can be drawn in the correct position"""

	artist.penup()
	artist.left(180)
	artist.forward(size*9)
	artist.left(180)
	artist.pendown()

# COLOR DETERMINATION FUNCTIONS

def add_greenrows():
	"""creates a list of lists with color combinations for shades of green"""

	green_rows = []

	for i in range(20):
		green_rows.append([random.randrange(0,6) for x in range(20-i)])

	return green_rows


def add_bobtails(ls):
	"""creates a list of lists that adds bobtail colors to the list returned by add_greenrows()"""

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

def modify_treecolormatrix(ls):
	"""this function takes in the treecolormatrix and appends zeros at the end of each list so as
	 to get a 20x20 matrix. It then returns this matrix"""

	return_ls = []

	for i in range(len(ls)):
		return_ls.append(ls[i])
		if len(ls[i]) != 20:
			while len(return_ls) != 20:
				return_ls[i].append(0)
	return return_ls	

def matrixvector_multiply(a, x):
	"""takes a matrix and a vector represented as a list of list and multiplies them"""

	if len(a[0]) == len(x):
		product = []

		for i in range(len(a)):
			product.append(0)
			for j in range(len(x)):
				product[i] += a[i][j]*x[j]
		return product 
	else:
		return """ Multiplication cannot be carried out because the number of rows of the matrix 'a' is 
					not equal to the number of columns of the vector 'x' """

def create_hash(ls):
	"""this function takes in the treecolor matrix and creates a hash vector that 
	identifies a particular combination of colors"""

	index_vector = [x for x in range(20)] # creates a vector of the indexes

	return matrixvector_multiply(modify_treecolormatrix(ls), index_vector)

def store_hash(hash_code, treecolormatrix, creator_number, recepient_number, time_taken):
	"""This function stores the hash generated by create_hash() in a file named patterns.json
	The hash is passed into the function"""


	##### >>>>>> PLEASE ALTER THIS >>>>>>> #######

	# FORMAT OF DATA AS STORED ON THE FILE

	# each hash will be stored in the form of a dictionary
	# the dictionary will have the following keys:
	# 	* hash
	#   * date_created
	#   * time_taken
	#   * recepient_number
	#   * creator_number
	#   * treecolormatrix


	data_entry_dict = {}
	data_entry_dict['hash'] = hash_code
	data_entry_dict['treecolormatrix'] = treecolormatrix
	data_entry_dict['creator_number'] = creator_number
	data_entry_dict['recepient_number'] = recepient_number
	data_entry_dict['date'] = datetime.datetime.now()
	data_entry_dict['time_taken'] = time_taken

	with open("patterns.json", 'a+') as file:

		if file.readline() != '[':
			file.seek(0,0)
			file.write('[')
		if file.read()[-1] != ']':
			file.seek(0,2)
			file.write(']')

		file.seek(1,2)
		file.readline()
		file.write(data_entry_dict)
		file.write(',')


def next_pattern():
	pass

# SAVE IMAGE

def save_img(artist):
	"""saves the turtle graphic to jpg image generated with unique name"""

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

# THEMATRIX
thematrix = {
			(0,0): 1,
			(6,0): 1,
			(10,0): 1,
			(14,0): 6,
			(1,1): 2,
			(9,1): 4,
			(16,1): 3,
			(2,2): 3,
			(7,2): 3,
			(14,2): 3,
			(3,3): 4,
			(8,3): 2,
			(12,3): 3,
			(4,4): 2,
			(13,4): 4,
			(17,4): 3,
			(5,5): 3,
			(9,5): 3,
			(15,5): 3,
			(6,6): 1,
			(12,6): 1,
			(15,6): 1,
			(18,6): 6,
			(7,7): 2,
			(9,7): 1,
			(11,7): 1,
			(13,7): 1,
			(16,7): 1,
			(19,7): 3,
			(8,8): 2,
			(13,8): 3,
			(17,8): 4,
			(9,9): 6,
			(14,9): 3,
			(10,10): 3,
			(13,10): 3,
			(17,10): 3,
			(11,11): 6,
			(13,11): 1,
			(15,11): 1,
			(18,11): 1,
			(12,12): 2,
			(15,12): 1,
			(16,12): 1,
			(17,12): 1,
			(18,12): 1,
			(19,12): 3,
			(13,13): 9,
			(14,14): 3,
			(16,14): 3,
			(19,14): 3,
			(15,15): 6,
			(16,15): 1,
			(18,15): 1,
			(19,15): 1,
			(16,16): 9,
			(17,17): 6,
			(18,17): 2,
			(19,17): 1,
			(18,18): 6,
			(19,18): 3,
			(19,19): 9
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