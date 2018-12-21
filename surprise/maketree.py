import turtle
from tkinter import *
import os
import random
import time
import datetime
import json


# implement multithreading and fix that issue

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

def draw_recepient(artist, name = "Santa"):
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
	artist.write(name, font = ('Courier', 40, 'bold'))

def draw_signature(artist, name = "1ntEgr8"):
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
	greeting = "from " + name
	artist.write(greeting, font = ('Courier', 30, 'bold'))

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

# MATRIX FUNCTIONS

def modify_treecolormatrix(ls):
	"""this function takes in the treecolormatrix and appends zeros at the end of each list so as
	 to get a 20x20 matrix. It then returns this matrix"""

	return_ls = []

	for i in range(len(ls)):
		return_ls.append(ls[i])
		if len(ls[i]) != 20:
			index = len(ls[i])
			while index < 20:
				return_ls[i].append(0)
				index += 1
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
		return """ Matrix Vector Multiplication cannot be carried out because the number of rows of the matrix 'a' is 
					not equal to the number of columns of the vector 'x' """

def vector_multiply(x1, x2):
	"""takes in two vectors and returns the product as an integer"""

	if len(x1) == len(x2):
		product = 0

		for i in range(len(x1)):
			product += x1[i] * x2[i]

		return product
	else:
		return """ Vector Multiplication could not be carried out because the length of the vector 'x1' is 
					not equal to the length of the vector 'x2' """

def matrix_multiply(m1, m2, m1_dict = False):
	"""takes in two matrices and returns the product of the two matrices
		CURRENTLY WORKS ONLY IF M2 IS A DICTIONARY SPARSE MATRIX
		ASSUMES THAT M2 is a compatible matrix"""

	if not m1_dict:
		if len(m1[0]) == len(m2):
			product = []
			column_vectors = []

			for i in range(len(m2[0])):
				new_column = []
				for row in m2:
					new_column.append(row[i])
				column_vectors.append(new_column)

			for row in m1:
				product_row = []

				for column in column_vectors:
					product_row.append(vector_multiply(row, column))

				product.append(product_row)

			return product

		else:
			return """ Matrix Multiplication cannot be carried out because the number of rows of the matrix 'm1' is 
						not equal to the number of columns of the vector 'm2 """
	else:
		product = []
		column_vectors = []

		for i in range(len(m2[0])):
			new_column = []
			for row in m2:
				new_column.append(row[i])
			column_vectors.append(new_column)

		for i in range(len(m2[0])):
			row_vector = []

			product_row = []
			for j in range(len(m2[0])):
				row_vector.append(m1.get((i,j),0))

			for column in column_vectors:
				product_row.append(vector_multiply(row_vector,column))

			product.append(product_row)

		return product

def modify_matrixproduct(ls):
	"""takes in a product matrix and rounds all the answers to the nearest int.
	Also changes extraneous values to something closer"""

	for i in range(len(ls)):
		for j in range(len(ls[i])):
			ls[i][j] = int(round(ls[i][j],1))
			if ls[i][j] >= 10 and ls[i][j] <= 12:
				ls[i][j] = 0
			elif ls[i][j] >= 13:
				ls[i][j] = 1
	return ls


# HASH FUNCTIONS

def create_hash(ls):
	"""this function takes in the treecolor matrix and returns a tuple of the hash code and the hash vector that 
	uniquely identifies a particular combination of colors"""

	index_vector = [x for x in range(20)] # creates a vector of the indexes

	hash_vector = matrixvector_multiply(modify_treecolormatrix(ls), index_vector)

	hash_code = ''

	for code in hash_vector:
		hash_code += str(code)

	return (hash_code[:10], hash_vector)

def next_pattern(ls):
	"""this function returns a new list of green colors for the treecolor matrix. This must be passed into the add_bobtails()
	function to add bobtails"""

	return modify_matrixproduct(matrix_multiply(thematrix, modify_treecolormatrix(ls)))


# SAVE IMAGE

def save_img(artist, id1, id2):
	"""saves the turtle graphic to jpg image generated with unique name"""

	filename = str(id1) + "_" + str(id2)

	ps =  artist.getscreen().getcanvas().postscript(file = filename + ".ps", colormode = 'color')
	os.system('convert ' + filename + '.ps' + ' ' + filename + '.jpg')
	os.system('rm ' + filename + '.ps')
	os.system('mv ' + filename + '.jpg' + ' surprise/static/gift_generated')


# INIT AND DATA STORAGE FUNCTIONS

def alpha():
	pass

def init_session(creator_name, recepients, id1=1, id2=1, time_of_request = 0):
	"""this function is to be called whenever a new user makes a request to send greetings to no_of_requests recepients"""
	
	wn = turtle.Screen()
	santa = turtle.Turtle() # creates a turtle names santa

	recepient_number_list = []
	flag = True

	# get creator number
	#creator_number = get_creator_number()

	for recepient in recepients:

		# t1
		t1 = time.time()

		# positioning santa
		santa.penup()
		santa.hideturtle() # hides santa
		santa.setpos(0,-80)
		santa.speed(0)
		santa.pensize(0)
		santa.pendown()

		# position trunk
		position_trunk(santa)
		# draw trunk
		draw_trunk(santa, list(main_colors.keys())[-4:], length = 3)
		# position tree
		position_tree(santa)
		# get treecolormatrix
		if flag:
			treecolormatrix = add_bobtails(add_greenrows())
			flag = False
		else:
			treecolormatrix = add_bobtails(next_pattern(treecolormatrix))
		# draw the tree
		draw_tree(santa,treecolormatrix)
		# draw the circle on top of the tree
		draw_circle(santa)
		# write merry christmas
		draw_greeting(santa)
		# write recepient name
		draw_recepient(santa, recepient)
		# write creator name
		draw_signature(santa, creator_name)

		# get recepient number
		# recepient_number = get_recepient_number()

		# store image
		save_img(santa, id1, id2)

		#t2
		t2 = time.time()

		# store hash for treecolor matrix
		hash_code, hash_vector = create_hash(treecolormatrix)
		store_hash(hash_code, hash_vector, treecolormatrix, id1, id2, t2-t1)	

		# update request data to be stored
		#recepient_number_list.append(recepient_number)

		santa.clear()

	# # store request data
	# store_request_data(creator_name, creator_number, recepients, recepient_number_list)


def store_hash(hash_code, hash_vector, treecolormatrix, creator_number, recepient_number, time_taken):
	"""This function stores the hash generated by create_hash() in a file named patterns.json
	The hash is passed into the function"""

	# FORMAT OF DATA AS STORED ON THE FILE

	# The file will be one dictionary with the hash codes as keys
	# The value of the hash code will be a dictionary with the following keys:
	#	* creator_number 
	#   * recepient_number  
	#   * date_created
	#   * time_taken
	#   * treecolormatrix

	data_entry_dict = {}
	data_entry_dict['hash_vector'] = hash_vector
	data_entry_dict['treecolormatrix'] = treecolormatrix
	data_entry_dict['creator_number'] = creator_number
	data_entry_dict['recepient_number'] = recepient_number
	data_entry_dict['date'] = str(datetime.datetime.now())
	data_entry_dict['time_taken'] = time_taken

	try:
		with open("patterns.json",'r') as input:
			data = json.load(input)
			data[hash_code] = data_entry_dict
	except:
		data = {}
		data[hash_code] = data_entry_dict

	with open("patterns.json",'w') as output:
		json.dump(data, output, indent = 4)   # indent stores the data in a better way 

def store_request_data(creator_name, creator_number, recepients, recepient_number_list):
	pass


#def get_creator_number():
	""" Updates creator_number and returns a zero padded string"""

	# global creator_number
	# creator_number += 1
	# return str(creator_number).zfill(6)

#def get_recepient_number():
	""" Updates recepient_number and returns a zero padded string"""

	# global recepient_number
	# recepient_number += 1
	# return str(recepient_number).zfill(6)

# RESET

# def reset_requst_data():
# 	""" Resets the value of creator_number and recepient_number to zero"""

# 	global creator_number
# 	global recepient_number

# 	creator_number = 0
# 	recepient_number = 0

# 	# empty request_data.json
# 	with open("request_data.json", 'w') as file:
# 		pass

# WARNING: CALL THIS IF YOU WANT TO DELETE ALL DATA AND START AFRESH
def end():
	quit()

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

thematrix = [[0.0, 0.03333333333333333, 0.05, 0.06666666666666667, 0.06666666666666667, 0.05, 0.06666666666666667, 0.0, 0.05, 0.05, 0.05, 0.06666666666666667, 0.05, 0.0, 0.03333333333333333, 0.016666666666666666, 0.08333333333333333, 0.06666666666666667, 0.03333333333333333, 0.08333333333333333],
             [0.0, 0.0, 0.05, 0.05, 0.016666666666666666, 0.06666666666666667, 0.06666666666666667, 0.08333333333333333, 0.05, 0.03333333333333333, 0.016666666666666666, 0.03333333333333333, 0.06666666666666667, 0.08333333333333333, 0.016666666666666666, 0.05, 0.016666666666666666, 0.0, 0.016666666666666666, 0.08333333333333333], 
             [0.06666666666666667, 0.016666666666666666, 0.0, 0.016666666666666666, 0.11666666666666667, 0.0, 0.0, 0.03333333333333333, 0.016666666666666666, 0.08333333333333333, 0.016666666666666666, 0.06666666666666667, 0.13333333333333333, 0.0, 0.05, 0.08333333333333333, 0.05, 0.016666666666666666, 0.08333333333333333, 0.08333333333333333], 
             [0.0, 0.08333333333333333, 0.1, 0.03333333333333333, 0.016666666666666666, 0.08333333333333333, 0.08333333333333333, 0.06666666666666667, 0.03333333333333333, 0.1, 0.03333333333333333, 0.05, 0.016666666666666666, 0.03333333333333333, 0.13333333333333333, 0.016666666666666666, 0.06666666666666667, 0.08333333333333333, 0.08333333333333333, 0.0], 
             [0.0, 0.016666666666666666, 0.05, 0.05, 0.0, 0.0, 0.03333333333333333, 0.08333333333333333, 0.0, 0.0, 0.0, 0.016666666666666666, 0.05, 0.05, 0.08333333333333333, 0.06666666666666667, 0.06666666666666667, 0.0, 0.0, 0.08333333333333333], 
             [0.0, 0.13333333333333333, 0.03333333333333333, 0.06666666666666667, 0.05, 0.08333333333333333, 0.016666666666666666, 0.016666666666666666, 0.05, 0.06666666666666667, 0.15, 0.03333333333333333, 0.05, 0.016666666666666666, 0.06666666666666667, 0.0, 0.06666666666666667, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333],
             [0.06666666666666667, 0.05, 0.016666666666666666, 0.03333333333333333, 0.05, 0.05, 0.0, 0.016666666666666666, 0.03333333333333333, 0.08333333333333333, 0.03333333333333333, 0.016666666666666666, 0.06666666666666667, 0.03333333333333333, 0.06666666666666667, 0.06666666666666667, 0.03333333333333333, 0.08333333333333333, 0.08333333333333333, 0.0], 
             [0.0, 0.1, 0.06666666666666667, 0.016666666666666666, 0.05, 0.15, 0.0, 0.03333333333333333, 0.03333333333333333, 0.13333333333333333, 0.08333333333333333, 0.05, 0.08333333333333333, 0.08333333333333333, 0.06666666666666667, 0.06666666666666667, 0.0, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333], 
             [0.11666666666666667, 0.08333333333333333, 0.08333333333333333, 0.03333333333333333, 0.03333333333333333, 0.05, 0.05, 0.016666666666666666, 0.03333333333333333, 0.0, 0.11666666666666667, 0.016666666666666666, 0.08333333333333333, 0.08333333333333333, 0.03333333333333333, 0.03333333333333333, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333], 
             [0.05, 0.05, 0.016666666666666666, 0.05, 0.016666666666666666, 0.0, 0.016666666666666666, 0.0, 0.03333333333333333, 0.016666666666666666, 0.0, 0.08333333333333333, 0.08333333333333333, 0.0, 0.0, 0.0, 0.08333333333333333, 0.08333333333333333, 0.06666666666666667, 0.0], 
             [0.0, 0.03333333333333333, 0.0, 0.0, 0.016666666666666666, 0.06666666666666667, 0.08333333333333333, 0.08333333333333333, 0.06666666666666667, 0.016666666666666666, 0.08333333333333333, 0.08333333333333333, 0.0, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.0, 0.0, 0.06666666666666667, 0.06666666666666667], 
             [0.15, 0.08333333333333333, 0.08333333333333333, 0.06666666666666667, 0.08333333333333333, 0.11666666666666667, 0.0, 0.08333333333333333, 0.05, 0.06666666666666667, 0.08333333333333333, 0.0, 0.08333333333333333, 0.0, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.03333333333333333, 0.06666666666666667], 
             [0.016666666666666666, 0.08333333333333333, 0.05, 0.03333333333333333, 0.08333333333333333, 0.06666666666666667, 0.06666666666666667, 0.016666666666666666, 0.08333333333333333, 0.06666666666666667, 0.0, 0.08333333333333333, 0.08333333333333333, 0.016666666666666666, 0.0, 0.0, 0.08333333333333333, 0.0, 0.06666666666666667, 0.03333333333333333], 
             [0.05, 0.016666666666666666, 0.016666666666666666, 0.06666666666666667, 0.0, 0.0, 0.05, 0.05, 0.0, 0.03333333333333333, 0.016666666666666666, 0.08333333333333333, 0.0, 0.08333333333333333, 0.0, 0.08333333333333333, 0.0, 0.0, 0.06666666666666667, 0.0], 
             [0.13333333333333333, 0.03333333333333333, 0.03333333333333333, 0.05, 0.15, 0.0, 0.08333333333333333, 0.0, 0.06666666666666667, 0.0, 0.08333333333333333, 0.08333333333333333, 0.0, 0.08333333333333333, 0.0, 0.08333333333333333, 0.08333333333333333, 0.06666666666666667, 0.03333333333333333, 0.08333333333333333],
             [0.06666666666666667, 0.1, 0.016666666666666666, 0.13333333333333333, 0.016666666666666666, 0.0, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.0, 0.08333333333333333, 0.06666666666666667, 0.05, 0.0, 0.06666666666666667, 0.0, 0.0], 
             [0.0, 0.0, 0.0, 0.08333333333333333, 0.06666666666666667, 0.0, 0.08333333333333333, 0.08333333333333333, 0.06666666666666667, 0.0, 0.05, 0.0, 0.03333333333333333, 0.08333333333333333, 0.06666666666666667, 0.016666666666666666, 0.06666666666666667, 0.03333333333333333, 0.0, 0.0], 
             [0.11666666666666667, 0.03333333333333333, 0.03333333333333333, 0.05, 0.06666666666666667, 0.05, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.05, 0.05, 0.0, 0.08333333333333333, 0.03333333333333333, 0.08333333333333333, 0.05, 0.06666666666666667, 0.0, 0.06666666666666667], 
             [0.1, 0.05, 0.15, 0.05, 0.03333333333333333, 0.08333333333333333, 0.06666666666666667, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.05, 0.05, 0.06666666666666667, 0.08333333333333333, 0.06666666666666667, 0.06666666666666667, 0.016666666666666666, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667], 
             [0.06666666666666667, 0.0, 0.15, 0.05, 0.06666666666666667, 0.08333333333333333, 0.06666666666666667, 0.08333333333333333, 0.08333333333333333, 0.0, 0.0, 0.05, 0.05, 0.016666666666666666, 0.05, 0.05, 0.06666666666666667, 0.03333333333333333, 0.05, 0.03333333333333333]]









