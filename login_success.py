from tkinter import *
from tkinter import  messagebox
import sys
import os
import signal
import time
from subprocess import  *
from tkinter.scrolledtext import ScrolledText
import sqlite3



class home_login():
    def __init__(self,master):
        try:
            with open('login_details.txt', 'r') as f:
                lines = f.read().splitlines()
                   # last_line = lines[-1]
                self.username = lines[-2]
        except:
            messagebox.showerror("Failed","Unable to unlock root directory")

        logout_button=Button(master,text='Logout',command=master.quit)
        logout_button.grid(row=0,column=1)
        username_label=Label(master,text="Welcome!!!"+self.username,font=("Courier", 36))
        username_label.grid(row=0,column=0)
        conn = sqlite3.connect('timex_portal_final.db')
        attendance_db= conn.cursor()
        attendance_db.execute('SELECT * from attendance_whole where username="%s"' % (self.username))
        atte_store = attendance_db.fetchall()
        date_label=Label(master,text="Date",font=("Courier", 22))
        date_label.grid(row=1,column=0)
        status_attendance_label=Label(master,text="Attendance",font=("Courier", 22))
        status_attendance_label.grid(row=1,column=1)
        for i in range(0,len(atte_store)):
            date_label_db=Label(master,text=atte_store[i][2],font=("Courier", 18))
            date_label_db.grid(row=2+i,column=0)
            status_attendance_db=Label(master,text=atte_store[i][1],font=("Courier", 18))
            status_attendance_db.grid(row=2+i,column=1)

        messages_label=Label(master,text="Admin Messages",font=("Courier", 44))
        messages_label.grid(row=40,column=1)
        try:
            conn = sqlite3.connect('timex_portal_final.db')
            message_db = conn.cursor()
            message_db.execute('SELECT * from message_alerts')
            message_db_store = message_db.fetchall()
        except:
            messagebox.showerror("Failed","Failed to Load  Messages")


        date_label_messages=Label(master,text="Date",font=("Courier", 36))
        date_label_messages.grid(row=41,column=0)
        message_content=Label(master,text='Message',font=("Courier", 36))
        message_content.grid(row=41,column=1)
        length_row=len(message_db_store)
        for i in range(0,len(message_db_store)):
            details_messages=Label(master,text=message_db_store[i][0],font=("Courier", 22))
            details_messages.grid(row=42+i,column=1)
            date_message=Label(master,text=message_db_store[i][1],font=("Courier", 22))
            date_message.grid(row=42+i,column=0)

        leave_request_leabel=Label(master,text='Leave Request',font=("Courier", 36))
        leave_request_leabel.grid(row=32,column=1)
        from_date_label=Label(master,text='From Date',font=("Courier", 22))
        from_date_label.grid(row=33,column=0)
        to_date_label=Label(master,text='To Date',font=("Courier", 22))
        to_date_label.grid(row=33,column=1)
        reason_label=Label(master,text='Reason',font=("Courier", 22))
        reason_label.grid(row=33,column=2)
        self.from_date=StringVar()
        self.to_date=StringVar()
        self.reasons=StringVar()
        from_date_entry=Entry(master,bd=5,textvariable=self.from_date)
        from_date_entry.grid(row=34,column=0)
        to_date_entry=Entry(master,bd=5,textvariable=self.to_date)
        to_date_entry.grid(row=34,column=1)
        reason_entry=Entry(master,bd=5,textvariable=self.reasons)
        reason_entry.grid(row=34,column=2)
        submit_button=Button(master,text='Submit',command=self.submit_leave)
        submit_button.grid(row=34,column=3)

    def submit_leave(self):
       try:
            from_date=self.from_date.get()
            to_date=self.to_date.get()
            reason=self.reasons.get()
            print(from_date,to_date,reason)
            conn = sqlite3.connect('timex_portal_final.db')
            leave_db = conn.cursor()
            leave_db.execute("INSERT into leave_requests(username,from_date,to_date,reason) values(?,?,?,?) ",(self.username,from_date,to_date,reason))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Leave request sent to admin")
       except:

            messagebox.showerror("Failed","Internal Server Error Occured")
    def logout(self):
        import login
        print('logout called')




root=Tk()
login_home_success=home_login(root)
root.wm_geometry("1360x1200")
root.title("Login")
root.mainloop()
