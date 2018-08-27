from tkinter import *
from tkinter import  messagebox
import sys
import os
import signal
import time
from subprocess import  call
import  xlrd
import xlwt
import sqlite3
import datetime

class Home():
    def __init__(self,master):

        self.date = datetime.date.today()
        attendance=Label(master,text='Attendance',font=("Courier", 44))
        attendance.grid(row=0,columnspan=2)

        edit_attendance = Button(master, text='Edit Attendance', command=self.edit_attendance)
        edit_attendance.grid(row=1, column=1)

        update_attendance=Button(master,text='Upload Attendance',command=self.update_attendance)
        update_attendance.grid(row=1,column=0)
        display_attendance=Button(master,text="Today's Attendance",command=self.display_attendance)
        display_attendance.grid(row=2,column=0)
        username = []
        status_list = []
        button_list = []
        conn = sqlite3.connect('timex_portal_final.db')
        attendance = conn.cursor()
        attendance.execute('SELECT * from attendance_whole where date="%s"' % (self.date))
        store = attendance.fetchall()
        print(store)
        for j in range(0, len(store)):
            username.append('var' + str(j))
            status_list.append('entry' + str(j))
            button_list.append(store[j][0])
        print(button_list)
        username_head = Label(master, text='Name:', font=("Courier", 36))
        username_head.grid(row=9, column=0)
        status_head = Label(master, text='Status:', font=("Courier", 36))
        status_head.grid(row=9, column=1)
        for i in range(0, len(store)):
            username[i] = Label(master, text=store[i][0], font=("Courier", 22))
            username[i].grid(row=10 + i, column=0)
            status_list[i] = Label(master, text=store[i][1],font=("Courier", 22))
            status_list[i].grid(row=10+i,column=1)

        #message box code


        message_label=Label(master,text="   Message to Employees",font=("Courier", 44))
        message_label.grid(row=0,column=10)
        self.message_variable=StringVar()
        large_font = ('Verdana', 30)
        message_entry = Entry(master, textvariable=self.message_variable, bd=10, font=large_font)
        message_entry.grid(row=4,column=10)
        message_submit=Button(master,text='Send to all the Employees',command=self.send_message)
        message_submit.grid(row=5,column=10)

    def update_attendance(self):
        print('update_at')
        location=("attendance.xls")
        wb = xlrd.open_workbook(location)
        sheet = wb.sheet_by_index(0)
        number_columns=sheet.ncols
        number_rows=sheet.nrows
        print(number_columns,number_rows)
        conn = sqlite3.connect('timex_portal_final.db')
        attendance_db_today_ = conn.cursor()
        attendance_db_today_.execute('SELECT * from attendance_whole where date="%s"' % (self.date))
        atte_store=attendance_db_today_.fetchall()
        print(len(atte_store))
        if len(atte_store)==0:
            for i in range(0,number_rows):
                name=sheet.cell_value(i,0)
                status=sheet.cell_value(i,1)
                conn = sqlite3.connect('timex_portal_final.db')
                attendance_db_today = conn.cursor()
                attendance_db_today.execute("INSERT into attendance_whole(username,status,date) values(?,?,?) ",(name,status,self.date))
                conn.commit()
                conn.close()
            messagebox.showerror("Success","Data Successfully Updated")
        else:
            messagebox.showerror("Failure","Alreday Updated")
        # For row 0 and column 0
        print(sheet.cell_value(0, 0))




        ###leave requests code
    def edit_attendance(self):
        from xlrd import open_workbook  # http://pypi.python.org/pypi/xlrd
        from xlwt import easyxf  # http://pypi.python.org/pypi/xlwt
        from xlutils.copy import copy
        import os

        conn = sqlite3.connect('timex_portal_final.db')
        register_fetch = conn.cursor()
        register_fetch.execute('SELECT * from register')
        store = register_fetch.fetchall()
        location = ("attendance.xls")

        rb = open_workbook(location, formatting_info=True)
        r_sheet = rb.sheet_by_index(0)  # read only copy to introspect the file
        wb = copy(rb)  # a writable copy (I can't read values out of this, only write to it)
        w_sheet = wb.get_sheet(0)  # the sheet to write to within the writable copy

        for row_index in range(0, len(store)):
            w_sheet.write(row_index, 0, store[row_index][0])
        wb.save(location)
        call('libreoffice attendance.xls',shell=True)

    def display_attendance(self):
        messagebox.showerror("Failed","Update Today's Attendance First")

    def send_message(self):
        messagebox.showinfo("Message Sent","Your Message has been Sent")
        message_value=self.message_variable.get()
        date=self.date
        try:
            conn = sqlite3.connect('timex_portal_final.db')
            message_insert=conn.cursor()
            message_insert.execute("INSERT into message_alerts(message,date) values(?,?) ",(message_value,date))
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error","Internal Servor Error Occured")




root=Tk()
admin_login_home=Home(root)
root.wm_geometry("1360x1200")
root.title("Admin Login")
root.mainloop()
