import os
from tkinter import filedialog
from tkinter import *


content = ''
file_path = ''


#~~~~ FUNCTIONS~~~~

def open_file():
	global content
	global file_path

	filename = filedialog.askopenfilename()
	infile = open(filename, 'r')
	content = infile.read()
	file_path = os.path.dirname(filename)
	return content

def process_file(content):
	print(content)

#~~~~~~~~~~~~~~~~~~~


#~~~~~~ GUI ~~~~~~~~

root = Tk()
root.title('Urdu Mehfil Ginti Converter')
root.geometry("598x120+250+100")

mf = Frame(root)
mf.pack()


f1 = Frame(mf, width=600, height=250)
f1.pack(fill=X)
f2 = Frame(mf, width=600, height=250)
f2.pack()

file_path = StringVar


Label(f1,text="Select Your File (Only txt files)").grid(row=0, column=0, sticky='e')
Entry(f1, width=50, textvariable=file_path).grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=25)
Button(f1, text="Browse", command=open_file).grid(row=0, column=27, sticky='ew', padx=8, pady=4)
Button(f2, text="Process Now", width=32, command=lambda: process_file(content)).grid(sticky='ew', padx=10, pady=10)


root.mainloop()


#~~~~~~~~~~~~~~~~~~~