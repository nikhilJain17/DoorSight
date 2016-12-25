# GUI master program
from Tkinter import *
import os
import bum


def switch_to_mode1():
	print "no block diagram available"

def switch_to_mode2():
	print "no block diagram required"
	results = bum.__main__()

	for result in results:
		result_label = Label(root, text='\n' + result)
		result_label.pack()
		


root = Tk()
root.title('No Patent Intended')
root.minsize(666,666)


w = Label(root, text="\n\nDoor Sight\n\n")
w.pack()

mode1_button = Button(root, text="Store Faces", command = switch_to_mode1)
mode1_button.pack()

mode2_button = Button(root, text="Recognize Faces", command = switch_to_mode2)
mode2_button.pack()


root.mainloop() 
