from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, filedialog
import csv

class csvGUI:

    def __init__(self, master):
        self.master = master
        master.title("Title")

        # self.at = u''
        # self.ac = u''

        self.label = Label(master, text=" Enter Files (.csv):\t\t\t\t\t")

        self.attended_entry = Entry(master)
        self.attended = Button(master, text="Select Attended File", command=lambda: self.getFile("attended"))
        self.acted_entry = Entry(master)
        self.acted = Button(master, text="Select Acted File", command=lambda: self.getFile("acted"))
        self.action = Button(master, text="Save Output", command=lambda: self.start())

        # LAYOUT
        self.label.grid(row=0, column=2, columnspan=4, sticky=W)
        self.attended.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.attended_entry.grid(row=1, column=2, columnspan=5, sticky=W+E)

        self.acted.grid(row=2, column=0, columnspan=2, sticky=W+E)
        self.acted_entry.grid(row=2, column=2, columnspan=5, sticky=W+E)
        self.action.grid(row=3, column=2, sticky=W+E)


    def getFile(self, which):
        file_path = filedialog.askopenfilename()
        if which == "attended":
            self.attended_entry.delete(0, END)
            self.attended_entry.insert(0, file_path)
        elif which == "acted":
            self.acted_entry.delete(0, END)
            self.acted_entry.insert(0, file_path)

    def start(self):
        save_path = filedialog.askdirectory() + u'/output.csv'
        attended_file = self.attended_entry.get()
        acted_file = self.acted_entry.get()
        try:
            with open(attended_file, 'r+', encoding='utf-8') as attend, open(acted_file, 'r+', encoding='utf-8') as act, open(save_path, 'w', encoding='utf-8') as o:
                attendFileReader = csv.DictReader(attend)
                actFileReader = csv.DictReader(act)
                fields = attendFileReader.fieldnames
                output = csv.DictWriter(o, fieldnames = fields)
                output.writeheader()
                actEmails = []
                for row in actFileReader:
                    actEmails.append(row['Email'])
                for row in attendFileReader:
                    if row['Email'] in actEmails:
                        output.writerow(row)
                self.label['text']=" Done. "
        except Exception as e:
            print(e.strerror)
            #self.label['text']=sys.exc_info()[0]
            self.label['text']=" Error occured opening files, please check files and try again."


root = Tk()
my_gui = csvGUI(root)
root.mainloop()