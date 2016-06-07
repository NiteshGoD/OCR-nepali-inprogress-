import os
#Importing all from Tkinter for GUI
from Tkinter import *
#Importing openFileDialog and saveFileDialog
from tkFileDialog import *
import tkMessageBox

#Main window creation
window = Tk()
window.title("Nepali-OCR")
w, h= window.winfo_screenwidth(),window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
#def resize(event):
#    print("New size is: {}x{}".format(event.width, event.height))
#window.bind("<configure>",resize)
window.geometry("600x400")
window.wm_iconbitmap('@icon1.xbm')

def noprintermsg():
    tkMessageBox.showwarning('Warning!','There is no printer found')
    
def closewindow():
    window.destroy()
    
frame = Frame(window)
frame.pack()
button=Button(frame,text="Quit",command=closewindow)
button.pack()
frame.place(x=475,y=350)

flag = 0
filepath = None
#Button click event for Open File Button
def openFile():
	global filepath
	filepath = askopenfilename()

#Button click event for OCR Button	
def recognize():
        
        
	print filepath
	cmd = "tesseract \"%s\" output_text" %filepath
	os.system(cmd)
	#os.system(exit)
	global flag
	flag = 1
	#Output text printing on GUI
        
	if flag == 1:
		file = open("output_text.txt")
		global print_text
		print_text = file.read()
		outputText.insert(INSERT, print_text)
		file.close()

#Button click event for Save File Button
def saveFile():
	save_file = asksaveasfile(mode = 'w', defaultextension = '.txt')
	save_file.write(print_text)
	save_file.close()

def aboutus():
    root=Tk()
    root.title("Product Info")
    label1=Label(root,text="Developers:")
    label2=Label(root,text="Mr. Nitesh Ranjitkar")
    label3=Label(root,text="Mr. Ganesh Raj Manandhar")
    label4=Label(root,text="Mr. Manoj Shrestha")
    label5=Label(root,text="Mr. Manraj Thapa Magar")
    label6=Label(root,text="All Rights Reserved, Version 1")
    label1.pack(padx=2,pady=2)
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()
    label6.pack(padx=7,pady=7)
    root.mainloop()

#creating menu
menu=Menu(window)
window.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Open File",command=openFile)
subMenu.add_command(label="Save File",command=saveFile)
subMenu.add_command(label="Show text in the image file",command=recognize)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=closewindow)

editmenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Browse text file")

viewmenu=Menu(menu)
menu.add_cascade(label="View",menu=viewmenu)
viewmenu.add_command(label="Toolbar")
viewmenu.add_command(label="Stausbar")
viewmenu.add_command(label="Fullscreen")

searchmenu=Menu(menu)
menu.add_cascade(label="Search",menu=searchmenu)
searchmenu.add_command(label="Find")

toolmenu=Menu(menu)
menu.add_cascade(label="Tools",menu=toolmenu)

documentmenu=Menu(menu)
menu.add_cascade(label="Documents",menu=documentmenu)

helpmenu=Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About the product",command=aboutus)

# creating toolbar
toolbar = Frame(window, bg="black")
insertbutt= Button(toolbar,text="Print File",command=noprintermsg)
insertbutt.pack(side=LEFT,padx=2,pady=2)


toolbar.pack(side=TOP, fill=X)

#creating status bar
if flag == 1:
   variabletext="processing..."
elif flag == 0:
   variabletext="Ready.."
status=Label(window,text=variabletext,bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)
	
#Open File Button widget
openImage = Button(window, text = "Open Image File", command = openFile)
openImage.pack()
openImage.place(x = 50, y = 35)

#Save File Button widget
saveFile = Button(window, text = "Save Text File", command = saveFile)
saveFile.pack()
saveFile.place(x = 475, y = 35)

#OCR Button widget
recognize = Button(window, text = "Start OCR", command = recognize)
recognize.pack()
recognize.place(x = 250, y = 350, width = 100)

#Text widget
outputText = Text(window, height = 15, width = 70, wrap = "word")
outputText.pack()
outputText.place(x = 50, y = 75)

window.mainloop()
