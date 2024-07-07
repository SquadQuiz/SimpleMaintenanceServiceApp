# basicsql.py

import sqlite3

'''
	Data information will store in Database
    name = v_name.get()
    department = v_department.get()
    tools = v_tools.get()
    details = v_details.get()
    part_number = v_part_number.get()
    phone_number = v_phone_number.get()
'''

# Create a connection to the SQLite3 database named 'maintenance.sqlite3'.
# If the database does not exist, it will be created.
conn = sqlite3.connect('maintenance.sqlite3')

# Create a cursor object using the connection to perform SQL operations.
c = conn.cursor()

# Sql Execute Command, Create a database table
c.execute(""" CREATE TABLE IF NOT EXISTS mt_workorder (
					ID INTEGER PRIMARY KEY AUTOINCREMENT,
					tsid TEXT,
					name TEXT,
					department TEXT,
					tools TEXT,
                    details  TEXT,
					part_number TEXT,
					phone_number TEXT) """)

def insert_mtworkorder(tsid, name, department, tools, details, part_number, phone_number):
    """
    Inserts a new work order into the mt_workorder table.

    Parameters:
    tsid (int): The transaction ID of the work order.
    name (str): The name associated with the work order.
    department (str): The department handling the work order.
    tools (str): The tools required for the work order.
    details (str): The details of the work order.
    part_number (str): The part number associated with the work order.
    phone_number (str): The phone number associated with the work order.

    Returns:
    None
    """
    # Create a new work order in the database
    with conn:
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?)'
        c.execute(command, (None, tsid, name, department, tools, details, part_number, phone_number))
    conn.commit()  # saving database
    print('Database has been saved')

# Insert data into table
# insert_mtworkorder('TS0001', 'Somsak', 'HR', 'Printer', 'Paper stuck', 'PT001', '159')
# insert_mtworkorder('TS0002', 'Somrak', 'IT', 'Laptop', 'Can\'t turn on', 'LT001', '120')

# Read workorder list from database
def view_mtworkorder():
    with conn:
        command = 'SELECT * FROM mt_workorder'
        c.execute(command)
        result = c.fetchall()
    return result

# Print workorder list 
workorder_list = view_mtworkorder()
for list in workorder_list:
    print(list)