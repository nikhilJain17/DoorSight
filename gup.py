# GUI master program
from Tkinter import *
import os
import bum


def switch_to_mode1():
	print "no block diagram"

def switch_to_mode2():
	# os.system('bum.py 1')
	bum.__main__()


root = Tk()
root.minsize(666,666)


w = Label(root, text="Hello")
w.pack()

mode1_button = Button(root, text="QUIT", command = switch_to_mode1)
mode1_button.pack()

mode2_button = Button(root, text="QUIT", command = switch_to_mode2)
mode2_button.pack()


root.mainloop() 
