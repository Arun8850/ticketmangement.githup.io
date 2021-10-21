import random
import smtplib
from fpdf import FPDF
from tkinter import *
from tkinter import messagebox
import pymysql
from twilio.rest import Client
from ttkthemes import themed_tk as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders




class Nalla:

    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.UserDetails()

    def userdetail(self):
        try:
            my_pdf = FPDF()

            name = self.entry.get()
            email = self.entry2.get()
            skill = self.entry3.get()
            branch = self.entry4.get()
            project = self.entry5.get()
            my_pdf.add_page()
            my_pdf.set_font("Arial", size=16)
            my_pdf.cell(200, 10, txt="My Resume", ln=1, align="C")

            text = (
                        "Respected Sir/Madam,\n I am " + name )
            my_pdf.cell(200, 10, txt=text, ln=2, align="C")
            text=(" \nI have learned the following " + skill )
            my_pdf.cell(200, 10, txt=text, ln=3, align="C")
            text=(" thourly \ni have done my graduation in " + branch )
            my_pdf.cell(200, 10, txt=text, ln=4, align="C")
            text=(" i have made following projects " + project )
            my_pdf.cell(200, 10, txt=text, ln=5, align="C")
            text=("\n  Yours Faithfully\n " + name)
            my_pdf.cell(200, 10, txt=text, ln=6, align="C")

            my_pdf.output("myPDF.pdf")
            email_user = 'babakijaiho866@gmail.com'
            email_password = 'Pass@1234'
            email_send= email

            subject = 'Your Resume'

            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            body = 'Hi here, is your resume'
            msg.attach(MIMEText(body, 'plain'))

            filename = 'myPDF.pdf'
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

    def UserDetails(self):
        self.root.geometry("650x550+300+100")
        self.root.resizable(True, True)

        Frame_login1 = Frame(self.root, bg="light green")
        Frame_login1.place(x=0, y=0, height=550, width=650)

        frame_input2 = Frame(self.root, bg='white')
        frame_input2.place(x=10, y=10, height=530, width=630)

        label2 = Label(frame_input2, text="Full Name", font=("Goody old style", 20, "bold"), fg='light green',
                       bg='white')
        label2.place(x=30, y=25)
        self.entry = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry.place(x=30, y=85, width=270, height=35)

        label3 = Label(frame_input2, text="Email Id", font=("Goody old style", 20, "bold"), fg='light green',
                       bg="white")
        label3.place(x=30, y=145)
        self.entry2 = Entry(frame_input2, font=("times roman", 15, "bold"), bg='white', bd=2)
        self.entry2.place(x=30, y=195, width=270, height=35)

        label4 = Label(frame_input2, text="Skills", font=("Goody old style", 20, "bold"), fg='light green',
                       bg='white')
        label4.place(x=330, y=25)
        self.entry3 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry3.place(x=330, y=85, width=270, height=35)

        label5 = Label(frame_input2, text="Branch", font=("Goody old style", 20, "bold"), fg='light green',
                       bg='white')
        label5.place(x=330, y=145)
        self.entry4 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry4.place(x=330, y=195, width=270, height=35)

        label5 = Label(frame_input2, text="Project link", font=("Goody old style", 20, "bold"), fg='light green',
                       bg='white')
        label5.place(x=30, y=245)
        self.entry5 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry5.place(x=30, y=295, width=270, height=35)

        btn2 = Button(frame_input2, command=self.userdetail, text="Register", cursor="hand2",
                      font=("times new roman", 15), fg="white", bg="light green", bd=0, width=15, height=1)
        btn2.place(x=330, y=440)


root = Tk()

ob = Nalla(root)
root.mainloop()