from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('1000x500')

class WorkorderList(ttk.Treeview):
    def __init__(self, GUI):
        header_list = ['TSID', 'Name', 'Department', 'Equipment', 'Details', 'Part number', 'Phone number', 'Status']
        header_width = [100, 100, 100, 150, 150, 100, 100, 100]
        ttk.Treeview.__init__(self, GUI, columns=header_list, show='headings', height=20)
        for h_list, h_width in zip(header_list, header_width):
            self.heading(h_list, text=h_list)
            self.column(h_list, width=h_width, anchor='center')

    def insertdata(self, values):
        self.insert('', 'end', values=values)

t = WorkorderList(GUI)
t.pack()
# t.place(x=50, y=50)

t.insertdata(['Test', 'A', 'B'])

GUI.mainloop()