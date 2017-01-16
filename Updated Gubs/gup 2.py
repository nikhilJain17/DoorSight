# GUI master program
from Tkinter import *
import os
import oldbum
import facinator # for mode 1
import mode2_facinator


# the root gui element
root = Tk()

def switch_to_mode1():
	print "no block diagram available"
	
	# create a popup to name the subject
	# YOU SHOULDN'T CREATE MULTIPLE ROOT WIDGETS 
	popup = Toplevel(root)
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


	# print some stuff
	some_label = Label(root,text='Do not read!')
	some_label.pack()
	

def add_new_subject(popup, textbox):

	name = textbox.get()

	# if name isn't already taken
	print "Adding new subject called " + name

	
	# Take some pics
	facinator.main(name)

        print "added successfully"
        # repoen the guiguiguigui
        # gui_creator()
        
        # while True:
          #       print "aryafetcher"
	# else don't accept the name!   


def switch_to_mode2():
	print "no block diagram required"

	# delete the old pics
	folder = os.getcwd() + '/test_faces'
	for file in os.listdir(folder):
		filepath = os.path.join(folder, file)
		try:
			os.remove(filepath)
		except Exception as e:
			print e	

	mode2_facinator.main()
	results = oldbum.main()

	for result in results:
		result_label = Label(root, text='\n' + result)
		result_label.pack()
		

def gui_creator():
        root.title('No Patent Intended')
        root.minsize(666,666)


        w = Label(root, text="\n\nDoor Sight\n\n")
        w.pack()

        mode1_button = Button(root, text="Store Faces", command = switch_to_mode1)
        mode1_button.pack()

        mode2_button = Button(root, text="Recognize Faces", command = switch_to_mode2)
        mode2_button.pack()


        root.mainloop() 

gui_creator()
