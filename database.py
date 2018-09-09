import sqlite3
conn = sqlite3.connect('timex_portal_final.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS login_details
             (username varchar PRIMARY KEY , password varchar)''')
# Save (commit) the changes
conn.commit()

#c.execute("INSERT into Login_details values('aryan','aryan')")
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

c_register = conn.cursor()

# Create table
c_register.execute('''CREATE TABLE IF NOT EXISTS register
             (username varchar PRIMARY KEY , password varchar,salary varchar, aadhar_number varchar,email varchar,name varchar,post varchar,phone varchar,address varchar)''')
# Save (commit) the changes
conn.commit()

attendance=conn.cursor()
attendance.execute('''CREATE TABLE IF NOT EXISTS attendance(username varchar PRIMARY KEY ,status varchar,date varchar)''')
#c.execute("INSERT into Login_details values('aryan','aryan')")
conn.commit()



attendance_whole=conn.cursor()
attendance_whole.execute('''CREATE TABLE IF NOT EXISTS attendance_whole(username varchar,status varchar,date varchar)''')
#c.execute("INSERT into Login_details values('aryan','aryan')")
conn.commit()

message=conn.cursor()
message.execute('''CREATE table if not exists message_alerts(message varchar,date varchar)''')
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
leave=conn.cursor()
leave.execute('''CREATE TABLE IF NOT EXISTS leave_requests(username varchar,from_date varchar,to_date varchar,reason varchar)''')
conn.close()
