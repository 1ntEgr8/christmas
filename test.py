# import turtle
# from tkinter import *
# from PIL import Image
# import os

# alex = turtle.Turtle()

# alex.forward(100)
# alex.left(100)

# ts = turtle.getscreen()

# ps = ts.getcanvas().postscript(file = "duck.eps", colormode = 'color')

# os.system('convert ' + 'duck.eps' + ' ' + "duck.jpg")

# data_entry_dict = {}
# data_entry_dict['hash'] = '123'
# data_entry_dict['treecolormatrix'] = [1,2,3]
# data_entry_dict['creator_number'] = 123
# data_entry_dict['recepient_number'] = 123
# data_entry_dict['date'] = '12312'
# data_entry_dict['time_taken'] = 12312

# with open("patterns.json", 'a+') as file:
# 	file.seek(0,0)
# 	text = file.read()

# 	if len(text) != 0:
# 		file.seek(len(text), 0)
# 		print('yea')
# 		file.write(',')
# 		file.write(str(data_entry_dict))
# 	else:
# 		file.seek(len(text), 0)
# 		file.write(str(data_entry_dict))

import json

data = json.loads('patterns.json')

print(data)