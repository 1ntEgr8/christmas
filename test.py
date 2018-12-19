# import turtle
# from tkinter import *
# from PIL import Image
# import os
import json
# alex = turtle.Turtle()

# alex.forward(100)
# alex.left(100)

# ts = turtle.getscreen()

# ps = ts.getcanvas().postscript(file = "duck.eps", colormode = 'color')

# os.system('convert ' + 'duck.eps' + ' ' + "duck.jpg")

# data_entry_dict = {}
# hash_code = '123'
# data_entry_dict['treecolormatrix'] = [1,2,3]
# data_entry_dict['creator_number'] = 123
# data_entry_dict['recepient_number'] = 123
# data_entry_dict['date'] = '12312'
# data_entry_dict['time_taken'] = 12312

# try:
# 	with open("patterns.json",'r') as input:
# 		data = json.load(input)
# 		print(data)
# 		data[hash_code] = data_entry_dict
# except:
# 	raise
# 	print("yea")
# 	data = {}
# 	data[hash_code] = data_entry_dict

# with open("patterns.json",'w') as output:
# 	json.dump(data, output, indent = 4)   

m2 = [[0, 2, 3, 4, 4, 3, 4, 0, 3, 3, 3, 4, 3, 0, 2, 1, 5, 4, 2, 5],
[0, 0, 3, 3, 1, 4, 4, 5, 3, 2, 1, 2, 4, 5, 1, 3, 1, 0, 1, 5],
[4, 1, 0, 1, 7, 0, 0, 2, 1, 5, 1, 4, 8, 0, 3, 5, 3, 1, 5, 5],
[0, 5, 6, 2, 1, 5, 5, 4, 2, 6, 2, 3, 1, 2, 8, 1, 4, 5, 5, 0],
[0, 1, 3, 3, 0, 0, 2, 5, 0, 0, 0, 1, 3, 3, 5, 4, 4, 0, 0, 5],
[0, 8, 2, 4, 3, 5, 1, 1, 3, 4, 9, 2, 3, 1, 4, 0, 4, 5, 5, 5],
[4, 3, 1, 2, 3, 3, 0, 1, 2, 5, 2, 1, 4, 2, 4, 4, 2, 5, 5, 0],
[0, 6, 4, 1, 3, 9, 0, 2, 2, 8, 5, 3, 5, 5, 4, 4, 0, 5, 5, 5],
[7, 5, 5, 2, 2, 3, 3, 1, 2, 0, 7, 1, 5, 5, 2, 2, 5, 5, 5, 5],
[3, 3, 1, 3, 1, 0, 1, 0, 2, 1, 0, 5, 5, 0, 0, 0, 5, 5, 4, 0],
[0, 2, 0, 0, 1, 4, 5, 5, 4, 1, 5, 5, 0, 5, 5, 5, 0, 0, 4, 4],
[9, 5, 5, 4, 5, 7, 0, 5, 3, 4, 5, 0, 5, 0, 5, 5, 5, 5, 2, 4],
[1, 5, 3, 2, 5, 4, 4, 1, 5, 4, 0, 5, 5, 1, 0, 0, 5, 0, 4, 2],
[3, 1, 1, 4, 0, 0, 3, 3, 0, 2, 1, 5, 0, 5, 0, 5, 0, 0, 4, 0],
[8, 2, 2, 3, 9, 0, 5, 0, 4, 0, 5, 5, 0, 5, 0, 5, 5, 4, 2, 5],
[4, 6, 1, 8, 1, 0, 5, 5, 5, 5, 5, 5, 0, 5, 4, 3, 0, 4, 0, 0],
[0, 0, 0, 5, 4, 0, 5, 5, 4, 0, 3, 0, 2, 5, 4, 1, 4, 2, 0, 0],
[7, 2, 2, 3, 4, 3, 5, 5, 5, 5, 3, 3, 0, 5, 2, 5, 3, 4, 0, 4],
[6, 3, 9, 3, 2, 5, 4, 5, 5, 5, 3, 3, 4, 5, 4, 4, 1, 4, 4, 4],
[4, 0, 9, 3, 4, 5, 4, 5, 5, 0, 0, 3, 3, 1, 3, 3, 4, 2, 3, 2]]


for i in range(len(m2)):
	for j in range(len(m2[i])):
		m2[i][j]/=60

print(m2)
