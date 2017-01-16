# GUI master program
from Tkinter import *
import os
import bum
import facinator

def switch_to_mode1():
	print "no block diagram available"
	
	# create a popup to name the subject
	popup = Tk()
	popup.title('Enter subject name')
	popup.minsize(200, 50)

	textbox = Entry(popup)
	textbox.pack()

	# a lambda is an anonymous function, meant to be used as a one shot function 
	# and can only have one expression
	# in this case it is used to pass args to the button callback
	save_btn = Button(popup, text="Save", command = lambda: add_new_subject(popup, textbox))
	save_btn.pack()
	#@TODO Make sure they don't duplicate names! 

def add_new_subject(popup, textbox):

	name = textbox.get()

	# if name isn't already taken
	print "Adding new subject called " + name

	popup.destroy()

		# Take 12 pics boi
	facinator.main(name)
	

	# else don't accept the name!   


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
