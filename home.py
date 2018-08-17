from tkinter import *
import sys
import os
import signal
import time
from subprocess import *
from tkinter import messagebox



def file_previous_close():
    try:
        with open('home_id.txt', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            os.kill(int(last_line),signal.SIGKILL)
    except:
        print('first instance no need to close previous file')
#file_previous_close()

def writing_id():
    file_home_id=open("home_id.txt","w+")
    home_id=os.getpid()
    file_home_id.writelines('home\n')
    file_home_id.writelines(str(home_id))
    file_home_id.close()
    print(home_id)

writing_id()

class Home():



    def __init__(self,master):




        menu = Menu(master)
        master.config(menu=menu)

        home=Menu(menu)
        menu.add_cascade(label='Home',menu=home)
        home.add_command(label='Take a Tour!!',command=self.take_a_tour)
        home.add_command(label='Terms of Use',command=self.terms_of_use)
        home.add_separator()

        login_option=Menu(menu)
        menu.add_cascade(label='Register and Login',menu=login_option)
        login_option.add_command(label='Login',command=self.login)
        login_option.add_command(label='Register',command=self.register)
        login_option.add_command(label='Admin Login',command=self.admin_login)
        login_option.add_separator()

        submenu = Menu(menu)
        menu.add_cascade(label='Help!!!', menu=submenu)
        submenu.add_command(label='Contact Us!',command=self.contact_us)
        submenu.add_command(label='FAQs', command=self.faq)
        submenu.add_command(label='Report Infringement', command=self.report_infringement)
        submenu.add_separator()

        about_us=Menu(menu)
        menu.add_cascade(label='About Us',menu=about_us)
        about_us.add_command(label='About us',command=self.about_us)
        about_us.add_separator()


        exit_button=Menu(menu)
        menu.add_cascade(label='Exit',menu=exit_button)
        exit_button.add_command(label='Exit',command=menu.quit)

        #can do a prompt to do yes or  no


        exit_button.add_command(label='Minimize',command=self.minimize)



    def admin_login(self):
        #import  admin_login
        call('python3 admin_login.py', shell=True)

    def about_us(self):
        top = Toplevel()
        top.geometry("200x200")
        top.title("About Us")

        msg = Message(top, text='I am Aryan Sharma.I am presently in my 3rd year of study.I love to '
                                'build cool stuff.I felt the need of this software so that Employee Management can be made easy.')
        msg.grid(row=0, column=15)
        button = Button(top, text="Dismiss", command=top.destroy)
        button.grid(row=4, column=15)

        ##declare a message box

    def faq(self):
        ##message box indicating faqs
        print('he')

    def login(self):
        print('login ')
        #import login
        call('python3 login.py', shell=True)



    def register(self):
        ##create a register Frame
        print('register')
        #import registration
        call('python3 registration.py', shell=True)

    def report_infringement(self):
        ##essage box
        messagebox.showerror("Report Infringement","If found any infringement please mail us at aryansharma23124@gmail.com or call us at 9087005180")



    def take_a_tour(self):
        ##take a tour of the app
        tour_take=Toplevel()
        tour_take.geometry("180x180")
        tour_take.title("Take a Tour")
        message=Message(tour_take,text="Press Register to Register an employee and fill the required details.Then Press Login to Login The Employee.")
        message.grid(row=0,column=1)
        button = Button(tour_take, text="Close", command=tour_take.destroy)
        button.grid(row=4, column=1)

        print('take a tour')

    def terms_of_use(self):
        string_terms="Privacy Statement Welcome to timex.com (timex.com or Company or we). By accessing or using this Software, you (User or you) agree to comply with the terms and conditions governing your use of any areas of the timex.com web Software (the Software) as set forth below. USE OF Software Please read the Terms of Use (Terms) carefully before you start using the Software. By using the Software you accept and agree to be bound and abide by these Terms of Use and our Privacy Policy, found at incorporated herein by reference. If you do not agree to these Terms of Use or the Privacy Policy, you must not access or use the Software. This Software or any portion of this Software may not be reproduced, duplicated, copied, sold, resold, or otherwise exploited for any commercial purpose except as expressly permitted by timex.com, Inc. timex.com, Inc. and its affiliates reserve the right to refuse service, terminate accounts, and/or cancel orders in its discretion, including, without limitation, if timex.com, Inc. believes that User conduct violates applicable law or is harmful to the interests of timex.com, Inc. or its affiliates."
        dialog=Toplevel()
        dialog.geometry("400x400")
        dialog.title("Terms of Use")
        message=Message(dialog,text=string_terms)
        message.grid(row=0,column=0)
        button = Button(dialog, text="Close", command=dialog.destroy)
        button.grid(row=4, column=0)

    def contact_us(self):
        messagebox.showerror("Contact us ","In case of any dicrepancy or misbehaving of software Please contact us immediately.You can mail us at aryansharma23124@gmail.com or call us at 9087005180 ")

    def minimize(self):
        print('minimize the window')



root=Tk()

photo = PhotoImage(file='timex.png')
Lower_frame=Frame(root)
label = Label(Lower_frame, image=photo)
label.pack()
Lower_frame.pack()
login_home=Home(root)
root.wm_geometry("1360x1200")
root.title("Home")
root.mainloop()
