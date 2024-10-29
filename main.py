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
GUI.geometry("1200x600+50+50")

#### FONT ####
FONT1 = ("Angsana New", 20, 'bold')
FONT2 = ("Angsana New", 16)

#### TAB ####
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
T4 = Frame(Tab)
Tab.add(T1, text='Create Ticket') 
Tab.add(T2, text='Tickets Information') 
Tab.add(T3, text='Approve Repairs') 
Tab.add(T4, text='Closed Tickets') 
Tab.pack(fill=BOTH, expand=1) 

#### Tab Font & Padding ####
tabStyle = ttk.Style()
tabStyle.configure('TNotebook.Tab', font = (None, 13), padding = [40, 10])

####------------------ TAB1-Maintenance Tickets ------------------###

#### Label & Entry ####
L = Label(T1, text="Maintenance Tickets!", font=FONT1)
L.place(x=100,y=5)

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
    update_table()

#### Button ####
# Create a style and configure the font for the TButton
style = ttk.Style()
style.configure("TButton", font=FONT2)

B = ttk.Button(T1, text="   Save   ", style="TButton", command=save_button)
B.place(x=200, y=350)

####------------------ TAB2-Tickets Information ------------------###
#TODO: Tree-view table 
header_list = ['TSID', 'Name', 'Department', 'Equipment', 'Details', 'Part number', 'Phone number', 'Status']
header_width = [100, 100, 100, 150, 150, 100, 100, 100]

mtworkorderlist = ttk.Treeview(T2, columns=header_list, show='headings', height=20)
mtworkorderlist.pack()

# Creating table header: zip -> pair two lists
for h_list, h_width in zip(header_list, header_width):
    mtworkorderlist.heading(h_list, text=h_list)
    mtworkorderlist.column(h_list, width=h_width, anchor='center')
# anchor some headings to left side
mtworkorderlist.column('TSID', anchor='w')
mtworkorderlist.column('Details', anchor='w')

def update_table():
    # clear old data before inserting
    mtworkorderlist.delete(*mtworkorderlist.get_children())
    # Inserting table value
    mtworkorder_db = view_mtworkorder()
    for d in mtworkorder_db:
        d = list(d) # convert tuble to list
        del(d[0]) # delete index number on list
        mtworkorderlist.insert('','end', values=d)

# Database Edit dialog
def editpage_mtworkorder(event=NONE):
    # loading data from list
    select = mtworkorderlist.selection()
    output = mtworkorderlist.item(select) # dictionary data structure (key-based)
    op = output['values']
    
    tsid = op[0]
    t_name = op[1]
    t_department = op[2]
    t_tools = op[3]
    t_details = op[4]
    t_part_number = op[5]
    t_phone_number = '0{}'.format(op[6])
    
    # Creating new dialog
    edit_dialog = Toplevel()
    edit_dialog.title('Editing database')
    edit_dialog.geometry('500x500')
    
    #### Label & Entry ####
    L = Label(edit_dialog, text="Maintenance Tickets!", font=FONT1)
    L.place(x=100,y=5)

    # ---------------
    L = Label(edit_dialog, text="Name:", font=FONT2)
    L.place(x=30, y=50)
    v_name2 = StringVar()  # special variable for T1
    v_name2.set(t_name)
    E1 = ttk.Entry(edit_dialog, textvariable=v_name2, font=FONT2)
    E1.place(x=150, y=50)

    # ---------------
    L = Label(edit_dialog, text="Department:", font=FONT2)
    L.place(x=30, y=100)
    v_department2 = StringVar()
    v_department2.set(t_department)
    E2 = ttk.Entry(edit_dialog, textvariable=v_department2, font=FONT2)
    E2.place(x=150, y=100)

    # ---------------
    L = Label(edit_dialog, text="Equipment/Tools:", font=FONT2)
    L.place(x=30, y=150)
    v_tools2 = StringVar()
    v_tools2.set(t_tools)
    E3 = ttk.Entry(edit_dialog, textvariable=v_tools2, font=FONT2)
    E3.place(x=150, y=150)

    # ---------------
    L = Label(edit_dialog, text="Details:", font=FONT2)
    L.place(x=30, y=200)
    v_details2 = StringVar()
    v_details2.set(t_details)
    E4 = ttk.Entry(edit_dialog, textvariable=v_details2, font=FONT2)
    E4.place(x=150, y=200)

    # ---------------
    L = Label(edit_dialog, text="Part number:", font=FONT2)
    L.place(x=30, y=250)
    v_part_number2 = StringVar()
    v_part_number2.set(t_part_number)
    E5 = ttk.Entry(edit_dialog, textvariable=v_part_number2, font=FONT2)
    E5.place(x=150, y=250)

    # ---------------
    L = Label(edit_dialog, text="Phone number:", font=FONT2)
    L.place(x=30, y=300)
    v_phone_number2 = StringVar()
    v_phone_number2.set(t_phone_number)
    E6 = ttk.Entry(edit_dialog, textvariable=v_phone_number2, font=FONT2)
    E6.place(x=150, y=300)

    # ---------------
    
    def edit_save_button():
        name = v_name2.get()
        department = v_department2.get()
        tools = v_tools2.get()
        details = v_details2.get()
        part_number = v_part_number2.get()
        phone_number = v_phone_number2.get()
        
        update_mtworkorder(tsid, 'name', name)
        update_mtworkorder(tsid, 'department', department)
        update_mtworkorder(tsid, 'tools', tools)
        update_mtworkorder(tsid, 'details', details)
        update_mtworkorder(tsid, 'part_number', part_number)
        update_mtworkorder(tsid, 'phone_number', phone_number)
        update_table()
        messagebox.showinfo('Save', 'Saving information...')
        edit_dialog.destroy() # Destroy dialog after save

    #### Button ####
    # Create a style and configure the font for the TButton
    style = ttk.Style()
    style.configure("TButton", font=FONT2)

    B = ttk.Button(edit_dialog, text="   Save   ", style="TButton", command=edit_save_button)
    B.place(x=200, y=350)
    
    edit_dialog.mainloop()

mtworkorderlist.bind('<Double-1>', editpage_mtworkorder)

def delete_list_mtworkorder(event=None):
    # loading data from list
    select = mtworkorderlist.selection()
    output = mtworkorderlist.item(select) # dictionary data structure (key-based)
    tsid = output['values'][0] # get only tsid
    
    confirm_check = messagebox.askyesno('Delete', 'Are you trying to delete information?')
    if (confirm_check):    
        delete_mtworkorder(tsid)
        update_table()

mtworkorderlist.bind('<Delete>', delete_list_mtworkorder)

#### Context Menu (Right-click Menu) ####

def approve_ticket():
    selection = mtworkorderlist.selection()
    item = mtworkorderlist.item(selection) # dictionary data structure (key-based)
    ticket_id = item['values'][0] # get ticket ID
    
    confirm = messagebox.askyesno('Approve Ticket', 'Are you sure you want to approve this ticket?')
    if confirm:    
        update_mtworkorder(ticket_id, 'status', 'approved')
        update_table()

def mark_as_pending():
    selection = mtworkorderlist.selection()
    item = mtworkorderlist.item(selection) # dictionary data structure (key-based)
    ticket_id = item['values'][0] # get ticket ID
    
    confirm = messagebox.askyesno('Change Status', 'Are you sure you want to mark this ticket as pending?')
    if confirm:    
        update_mtworkorder(ticket_id, 'status', 'pending')
        update_table()

context_menu = Menu(GUI, tearoff=0)
context_menu.add_command(label='Approve Ticket', command=approve_ticket)
context_menu.add_command(label='Mark as Pending', command=mark_as_pending)
context_menu.add_command(label='Delete Ticket', command=delete_list_mtworkorder)

## Context Menu Event Handler
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

mtworkorderlist.bind('<Button-3>', show_context_menu) # Right-click binding

### START-UP ###
update_table()

####------------------ TAB3-Summary ------------------###
#TODO: Summary table

####------------------ END-TAB3 ------------------###

#----------------------- Main loop -----------------------#
GUI.mainloop()
