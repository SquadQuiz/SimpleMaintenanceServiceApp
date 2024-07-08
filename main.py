from tkinter import *
from tkinter import messagebox
from datetime import datetime
# Import Database
from db_maintenance import *

GUI = Tk()
GUI.title("Maintenance Application")
GUI.geometry("500x500+800+400")

#### FONT ####
FONT1 = ("Angsana New", 20, 'bold')
FONT2 = ("Angsana New", 16)

#### Label & Entry ####
L = Label(GUI, text="Maintenance Tickets!", font=FONT1)
L.pack()

# ---------------
L = Label(GUI, text="Name:", font=FONT2)
L.place(x=30, y=50)
v_name = StringVar()  # special variable for GUI
E1 = Entry(GUI, textvariable=v_name, font=FONT2)
E1.place(x=150, y=50)

# ---------------
L = Label(GUI, text="Department:", font=FONT2)
L.place(x=30, y=100)
v_department = StringVar()
E2 = Entry(GUI, textvariable=v_department, font=FONT2)
E2.place(x=150, y=100)

# ---------------
L = Label(GUI, text="Equipment/Tools:", font=FONT2)
L.place(x=30, y=150)
v_tools = StringVar()
E3 = Entry(GUI, textvariable=v_tools, font=FONT2)
E3.place(x=150, y=150)

# ---------------
L = Label(GUI, text="Details:", font=FONT2)
L.place(x=30, y=200)
v_details = StringVar()
E4 = Entry(GUI, textvariable=v_details, font=FONT2)
E4.place(x=150, y=200)

# ---------------
L = Label(GUI, text="Part number:", font=FONT2)
L.place(x=30, y=250)
v_part_number = StringVar()
E5 = Entry(GUI, textvariable=v_part_number, font=FONT2)
E5.place(x=150, y=250)

# ---------------
L = Label(GUI, text="Phone number:", font=FONT2)
L.place(x=30, y=300)
v_phone_number = StringVar()
E6 = Entry(GUI, textvariable=v_phone_number, font=FONT2)
E6.place(x=150, y=300)

# ---------------

def write_csv(record_list):
    with open('log.csv', 'a', newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(record_list)

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
    # messagebox.showinfo("Saving information...", text)
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tsid = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Generate transaction id
    encrypt_num = 123543999010
    tsid = str(int(datetime.now().strftime('%y%m%d%H%M%S')) + encrypt_num)
    insert_mtworkorder(tsid, name, department, tools, details, part_number, phone_number)
    messagebox.showinfo('Save', 'Saving information...')
    # Clear string
    clear_stringvar_value()

def clear_stringvar_value():
    v_name.set('')
    v_department.set('')
    v_tools.set('')
    v_details.set('')
    v_part_number.set('')
    v_phone_number.set('')

#### Button ####
B = Button(GUI, text="   Save   ", font=FONT2, command=save_button)
B.place(x=200, y=350)

#### Main loop ####
GUI.mainloop()
