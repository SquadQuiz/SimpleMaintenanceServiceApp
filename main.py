# Import tkinter GUI
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Import datetime
from datetime import datetime
# Import Database
from db_maintenance import *

GUI = Tk()
GUI.title("Maintenance Application")
GUI.geometry("800x600")

#### FONT ####
FONT1 = ("Angsana New", 20, 'bold')
FONT2 = ("Angsana New", 16)

#### TAB ####
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.add(T1, text='Maintenance Tickets') 
Tab.add(T2, text='Tickets Information') 
Tab.add(T3, text='Summary') 
Tab.pack(fill=BOTH, expand=1) 

####------------------ TAB1 ------------------###

#### Label & Entry ####
L = Label(T1, text="Maintenance Tickets!", font=FONT1)
L.pack()

# ---------------
L = Label(T1, text="Name:", font=FONT2)
L.place(x=30, y=50)
v_name = StringVar()  # special variable for T1
E1 = ttk.Entry(T1, textvariable=v_name, font=FONT2)
E1.place(x=150, y=50)

# ---------------
L = Label(T1, text="Department:", font=FONT2)
L.place(x=30, y=100)
v_department = StringVar()
E2 = ttk.Entry(T1, textvariable=v_department, font=FONT2)
E2.place(x=150, y=100)

# ---------------
L = Label(T1, text="Equipment/Tools:", font=FONT2)
L.place(x=30, y=150)
v_tools = StringVar()
E3 = ttk.Entry(T1, textvariable=v_tools, font=FONT2)
E3.place(x=150, y=150)

# ---------------
L = Label(T1, text="Details:", font=FONT2)
L.place(x=30, y=200)
v_details = StringVar()
E4 = ttk.Entry(T1, textvariable=v_details, font=FONT2)
E4.place(x=150, y=200)

# ---------------
L = Label(T1, text="Part number:", font=FONT2)
L.place(x=30, y=250)
v_part_number = StringVar()
E5 = ttk.Entry(T1, textvariable=v_part_number, font=FONT2)
E5.place(x=150, y=250)

# ---------------
L = Label(T1, text="Phone number:", font=FONT2)
L.place(x=30, y=300)
v_phone_number = StringVar()
E6 = ttk.Entry(T1, textvariable=v_phone_number, font=FONT2)
E6.place(x=150, y=300)

# ---------------
def clear_stringvar_value():
    v_name.set('')
    v_department.set('')
    v_tools.set('')
    v_details.set('')
    v_part_number.set('')
    v_phone_number.set('')

def save_button():
    name = v_name.get()
    department = v_department.get()
    tools = v_tools.get()
    details = v_details.get()
    part_number = v_part_number.get()
    phone_number = v_phone_number.get()
    
    text = "Name: " + name + "\n"
    text = text + "Department: " + department + "\n"
    text = text + "Tools: " + tools + "\n"
    text = text + "Details: " + details + "\n"
    text = text + "Part number: " + part_number + "\n"
    text = text + "Phone number: " + phone_number + "\n"
    # Generate transaction id
    encrypt_num = 123543999010
    tsid = str(int(datetime.now().strftime('%y%m%d%H%M%S')) + encrypt_num)
    insert_mtworkorder(tsid, name, department, tools, details, part_number, phone_number)
    messagebox.showinfo('Save', 'Saving information...')
    # Clear string
    clear_stringvar_value()

#### Button ####
# Create a style and configure the font for the TButton
style = ttk.Style()
style.configure("TButton", font=FONT2)

B = ttk.Button(T1, text="   Save   ", style="TButton", command=save_button)
B.place(x=200, y=350)

####------------------ END-TAB1 ------------------###

#----------------------- Main loop -----------------------#
GUI.mainloop()
