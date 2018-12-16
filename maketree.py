import turtle

# need a function that makes the rows
# need a function that decides the colors
# need a function that decides the position 
# need a save function to store the png file
# need a function to delete the eps file

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

	if len(colors) < length:
		return "Insufficient number of rows"

	for i in range(length):
		draw_pixel(artist, size, colors[i], colors[i])
		artist.forward(size)

def move_up_row(artist, prevrowlength, size = 10):
	"moves artist up to a new row to draw the tree"
	artist.left(90)
	artist.forward(size)
	artist.left(90)
	artist.forward(size * (prevrowlength))
	artist.left(180)
	artist.forward(size//2)

def draw_tree(artist, start_size = 20):
	while start_size != 0:
		draw_row(artist, start_size, colors[:start_size])
		move_up_row(artist, start_size)
		start_size -= 1

santa = turtle.Turtle() # creates a turtle names santa
wn = turtle.Screen() 
santa.hideturtle() # hides santa
santa.speed(0)
colors = ['#228B22',
		  '#008000',
		  '#7CFC00',
		  '#008000',
		  '#7CFC00',
		  '#32CD32',
		  '#008000',
		  '#228B22',
		  '#32CD32',
		  '#006400',
		  '#006400',
		  '#006400',
		  '#228B22',
		  '#228B22',
		  '#008000',
		  '#32CD32',
		  '#006400',
		  '#006400',
		  '#7CFC00',
		  '#006400']
draw_tree(santa)

wn.mainloop()