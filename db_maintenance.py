import sqlite3

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
    # Create a new work order in the database
    with conn:
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?)'
        c.execute(command, (None, tsid, name, department, tools, details, part_number, phone_number))
    conn.commit()  # saving database

# Read workorder list from database
def view_mtworkorder():
    with conn:
        command = 'SELECT * FROM mt_workorder'
        c.execute(command)
        result = c.fetchall()
    return result

# Update information on database mt_workorder
def update_mtworkorder(tsid, field, newvalue):
    with conn:
        command = 'UPDATE mt_workorder SET {} = (?) WHERE tsid=(?)'.format(field)
        c.execute(command, (newvalue, tsid))
    conn.commit() 

# Delete information on database mt_workorder
def delete_mtworkorder(tsid):
    with conn:
        command = 'DELETE from mt_workorder WHERE tsid=(?)'
        c.execute(command, ([tsid]))
    conn.commit()
