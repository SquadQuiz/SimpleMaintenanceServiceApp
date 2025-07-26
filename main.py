# Import tkinter GUI
from tkinter import Tk, Label, StringVar, Menu, Toplevel, Text, Frame
from tkinter import messagebox
from tkinter import ttk
from tkinter import BOTH, NONE

# Import datetime
from datetime import datetime
# Import Database
from db_maintenance import *
# Import Tkinter Calendar
from tkcalendar import DateEntry

GUI = Tk()
GUI.title("Maintenance Application")

# application window size
app_width_size = 1200
app_height_size = 600

winfo_width = GUI.winfo_screenwidth() # screen width
winfo_height = GUI.winfo_screenheight() # screen height

app_pos_x = (winfo_width / 2) - (app_width_size / 2)
app_pos_y = (winfo_height / 2) - (app_height_size / 2)

# centralize the window dialog by getting current screen width and height
GUI.geometry(f'{app_width_size}x{app_height_size}+{app_pos_x:.0f}+{app_pos_y:.0f}')

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

E1.bind('<Return>', lambda event: E2.focus())

# ---------------
L = Label(T1, text="Department:", font=FONT2)
L.place(x=30, y=100)
v_department = StringVar()
E2 = ttk.Entry(T1, textvariable=v_department, font=FONT2)
E2.place(x=150, y=100)

E2.bind('<Return>', lambda event: E3.focus())

# ---------------
L = Label(T1, text="Equipment/Tools:", font=FONT2)
L.place(x=30, y=150)
v_tools = StringVar()
E3 = ttk.Entry(T1, textvariable=v_tools, font=FONT2)
E3.place(x=150, y=150)

E3.bind('<Return>', lambda event: E4.focus())

# ---------------
L = Label(T1, text="Details:", font=FONT2)
L.place(x=30, y=200)
v_details = StringVar()
E4 = ttk.Entry(T1, textvariable=v_details, font=FONT2)
E4.place(x=150, y=200)

E4.bind('<Return>', lambda event: E5.focus())

# ---------------
L = Label(T1, text="Part number:", font=FONT2)
L.place(x=30, y=250)
v_part_number = StringVar()
E5 = ttk.Entry(T1, textvariable=v_part_number, font=FONT2)
E5.place(x=150, y=250)

E5.bind('<Return>', lambda event: E6.focus())

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

def save_button(event=None):
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
    
    # Focus on the first entry field
    E1.focus()

#### Button ####
# Create a style and configure the font for the TButton
style = ttk.Style()
style.configure("TButton", font=FONT2)

B = ttk.Button(T1, text="   Save   ", style="TButton", command=save_button)
B.place(x=200, y=350)

# Bind the Return key to the save_button function
E6.bind('<Return>', save_button)

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
    mtworkorder_db = view_mtworkorder() # status 'new' and 'pending'
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
        update_table_approved_repairs(g_approved_repairs_table)

def mark_as_pending():
    selection = mtworkorderlist.selection()
    item = mtworkorderlist.item(selection) # dictionary data structure (key-based)
    ticket_id = item['values'][0] # get ticket ID
    
    confirm = messagebox.askyesno('Change Status', 'Are you sure you want to mark this ticket as pending?')
    if confirm:    
        update_mtworkorder(ticket_id, 'status', 'pending')
        update_table()

context_menu = Menu(GUI, tearoff=0)
# context_menu.add_command(label='Create Ticket', command=create_ticket)
context_menu.add_command(label='Approve Ticket', command=approve_ticket)
context_menu.add_command(label='Mark as Pending', command=mark_as_pending)
context_menu.add_command(label='Delete Ticket', command=delete_list_mtworkorder)

## Context Menu Event Handler
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

mtworkorderlist.bind('<Button-3>', show_context_menu) # Right-click binding

### START-UP ###
update_table()

####------------------ TAB3 - Approved Repairs ------------------###
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

class MenuText(ttk.Label):
    def __init__(self, GUI, text='Example', size=20):
        ttk.Label.__init__(self, GUI, text=text, font=('Angsana New', size, 'bold'), foreground='navy')

# Table of Approve repair list
tab3_table_title = MenuText(T3, text='Request Details', size=30)
tab3_table_title.pack()

g_approved_repairs_table = WorkorderList(T3)
g_approved_repairs_table.pack()

def update_table_approved_repairs(workorder_table):
    """
    Updates the approved repairs table with current data from database
    Args:
        workorder_table: WorkorderList widget to be updated
    """
    # Clear existing table data
    workorder_table.delete(*workorder_table.get_children())
    # Fetch approved workorders from database
    approved_workorders = view_mtworkorder_status('approved')
    for workorder in approved_workorders:
        workorder_data = list(workorder) # Convert tuple to list
        workorder_data.pop(0)  # Remove index number
        workorder_table.insert('', 'end', values=workorder_data)

# Initial table population
update_table_approved_repairs(g_approved_repairs_table)

####------------------ END-TAB3 ------------------###

def new_note(event):
    GUI3 = Toplevel()
    GUI3.geometry('500x600')
    GUI3.title('Repair details')
    
    select = g_approved_repairs_table.selection()
    output = g_approved_repairs_table.item(select) # dictionary data structure (key-based)
    tsid = output['values'][0] # get only tsid
    
    FONT4 = (12)
    L = ttk.Label(GUI3, text='Repair details (tsid: {})'.format(tsid), font=FONT4)
    L.pack(pady=10)
    
    L1 = ttk.Label(GUI3, text='Date Start', font=FONT4)
    L1.pack(pady=10)
    cal = DateEntry(GUI3, width=20, background='darkblue', foreground='white', borderwidth=2, year=2025, date_pattern='dd/mm/yyyy')
    cal.pack(padx=10, pady=10)
    
    L2 = ttk.Label(GUI3, text='Details', font=FONT4)
    L2.pack(pady=10)
    E2 = Text(GUI3, font=FONT4, width=40, height=5) # 5 lines 40 characters textbox
    E2.pack()
    
    L3 = ttk.Label(GUI3, text='Notes', font=FONT4)
    L3.pack(pady=10)
    E3 = Text(GUI3, font=FONT4, width=40, height=5)
    E3.pack()
    
    # Get data from database
    get_data_db = view_mtnote_tsid(tsid)
    print(get_data_db)
    
    GUI3.bind('<F1>', lambda event: GUI3.focus())  # Bind F1 key to focus on the dialog
    
    # Insert data to textbox
    if (get_data_db != None):
        cal.set_date(get_data_db[2]) # get date from database
        E2.insert('1.0', get_data_db[3]) # insert details to textbox
        E3.insert('1.0', get_data_db[4]) # insert notes to textbox
    else:
        messagebox.showwarning('Warning', 'No data found!')
    
    def save_note():
        # check state if data is new or update
        date = cal.get()
        details = E2.get('1.0', 'end').strip() # strip '\n' from textbox
        other = E3.get('1.0', 'end').strip()
        if (get_data_db == None):
            insert_mtnote(tsid, date, details, other)
        else:
            update_mtnote(tsid, 'date_start', date) 
            update_mtnote(tsid, 'details', details)
            update_mtnote(tsid, 'other', other)
        messagebox.showinfo('Save', 'Saving information...')
        GUI3.destroy()
        update_table_approved_repairs(g_approved_repairs_table)
    
    B = ttk.Button(GUI3, text='Save', command=save_note)
    B.pack(pady=45, ipadx=20, ipady=10)
    
    GUI3.mainloop()

g_approved_repairs_table.bind('<Double-1>', new_note)       

#----------------------- Main loop -----------------------#
GUI.mainloop()
