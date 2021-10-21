import random
import smtplib
from tkinter import *
from fpdf import FPDF
from tkinter import messagebox
import pymysql
from twilio.rest import Client
from ttkthemes import themed_tk as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class Company:
    def __init__(self, root):



        self.root = root
        self.root.overrideredirect(True)
        self.Register()

    def register(self):
        try:
            print("fxhg df")
            #=self.entry1.get()
            #a=int(a)
            con = pymysql.connect(host="localhost", user="root", password="Root", database="login")
            cur = con.cursor()


            cur.execute("INSERT INTO  detials (Train_Id,Name,Age,Contact_Number,On_date) values (%s,%s,%s,%s,%s)",
                        (self.entry2.get(), self.entry.get(), self.entry3.get(), self.entry5.get(), self.entry4.get()))

            con.commit()
            con.close()
            #messagebox.showerror("Success", f"Booked Successfully", parent=self.root)
            con = pymysql.connect(host="localhost", user="root", password="Root", database="login")
            cur = con.cursor()
            cur.execute("Select * from Details where Id= %s", self.entry2.get())
            myresult = cur.fetchall()
            Train_Name = myresult[0][1]
            source = myresult[0][2]
            destination = myresult[0][3]

            con.commit()
            con.close()
            print("hello")

            my_pdf = FPDF()

            name = self.entry.get()
            Train_id = self.entry2.get()
            age = self.entry3.get()
            C_n = self.entry4.get()
            Date = self.entry5.get()
            email = self.entry6.get()
            my_pdf.add_page()
            my_pdf.set_font("Arial", size=16)
            my_pdf.cell(200, 10, txt="Ticket_Details ", ln=1, align="C")

            text = ("Passenger Details,\n " + name )
            my_pdf.cell(200, 10, txt=text, ln=2, align="C")
            text =( " \nAge"
                    + age )
            my_pdf.cell(200, 10, txt=text, ln=3, align="C")
            text=(" \n Contact_Number " + Date)
            my_pdf.cell(200, 10, txt=text, ln=4, align="C")
            text=(" \n Date  " + C_n )
            my_pdf.cell(200, 10, txt=text, ln=5, align="C")
            text=("\n Train_Id "+ Train_id)
            my_pdf.cell(200, 10, txt=text, ln=6, align="C")
            text = ("\n From " + source)
            my_pdf.cell(200, 10, txt=text, ln=8, align="C")
            text = ("\n To " + destination)
            my_pdf.cell(200, 10, txt=text, ln=9, align="C")
            text = ("\n Train_Name " + Train_Name)
            my_pdf.cell(200, 10, txt=text, ln=7, align="C")

            my_pdf.output("Ticket.pdf")


            email_user = 'babakijaiho866@gmail.com'
            email_password = 'Pass@1234'
            email_send = email

            subject = 'Your ticket'

            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            body = 'Hi here, is your ticket'
            msg.attach(MIMEText(body, 'plain'))

            filename = 'ticket.pdf'
            attachment = open(filename, 'rb')

            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= " + filename)

            msg.attach(part)
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_user, email_password)

            server.sendmail(email_user, email_send, text)
            server.quit()




        except Exception as es:
           messagebox.showerror("Error", f"Error due to:(str(es))", parent=self.root)



    def Register(self):
        self.root.geometry("650x550+300+100")
        self.root.resizable(True, True)

        Frame_login1 = Frame(self.root, bg="light green")
        Frame_login1.place(x=0, y=0, height=550, width=650)

        frame_input2 = Frame(self.root, bg='white')
        frame_input2.place(x=10, y=10, height=530, width=630)

        label2 = Label(frame_input2, text="Name", font=("Goody old style", 20, "bold"), fg='light green',
                   bg='white')
        label2.place(x=30, y=25)
        self.entry = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry.place(x=30, y=85, width=270, height=35)

        label3 = Label(frame_input2, text="Train_Id", font=("Goody old style", 20, "bold"), fg='light green',
                   bg="white")
        label3.place(x=30, y=145)
        self.entry2 = Entry(frame_input2, font=("times roman", 15, "bold"), bg='white', bd=2)
        self.entry2.place(x=30, y=195, width=270, height=35)

        label4 = Label(frame_input2, text="Age", font=("Goody old style", 20, "bold"), fg='light green',
                   bg='white')
        label4.place(x=330, y=25)
        self.entry3 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry3.place(x=330, y=85, width=270, height=35)

        label5 = Label(frame_input2, text="Date", font=("Goody old style", 20, "bold"), fg='light green',
                   bg='white')
        label5.place(x=330, y=145)
        self.entry4 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry4.place(x=330, y=195, width=270, height=35)

        label5 = Label(frame_input2, text="Contact_Number", font=("Goody old style", 20, "bold"), fg='light green',
                   bg='white')
        label5.place(x=30, y=245)
        self.entry5 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry5.place(x=30, y=295, width=270, height=35)

        label6 = Label(frame_input2, text="Email", font=("Goody old style", 20, "bold"), fg='light green',
                   bg='white')
        label6.place(x=330, y=245)
        self.entry6 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry6.place(x=330, y=295, width=270, height=35)

        btn2 = Button(frame_input2, command=self.register, text="Book ticket", cursor="hand2",
                  font=("times new roman", 15), fg="white", bg="light green", bd=0, width=15, height=1)
        btn2.place(x=330, y=440)


root = Tk()

ob = Company(root)
root.mainloop()