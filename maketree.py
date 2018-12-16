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

santa = turtle.Turtle() # creates a turtle names santa
wn = turtle.Screen() 
santa.hideturtle() # hides santa
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
		  '#006400']
draw_row(santa, len(colors), colors)
wn.mainloop()