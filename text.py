from tkinter import *
# from PIL import ImageTK
from tkinter import messagebox
import pymysql
import sys
import fileinput
import  os


# Login class code
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("1366x700+0+0")
        self.root.resizable(False, False)
        self.loginform()

    def loginform(self):
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=0, y=0, height=700, width=1366)

        # =================CODE FOR ImageTK========================

        frame_input = Frame(self.root, bg="white")
        frame_input.place(x=320, y=130, height=450, width=350)

        label1 = Label(frame_input, text="Update Here", font=('impact', 32, 'bold'), fg="black", bg="white")
        label1.place(x=75, y=20)

        label2 = Label(frame_input, text="Name", font=('Goudy old style', 20, 'bold'), fg="orange", bg="white")
        label2.place(x=30, y=95)
        self.name = Entry(frame_input, font=("times new roman", 15, "bold"), bg='lightgray')
        self.name.place(x=30, y=145, width=270, height=35)
        f = open("resume.txt", "w")
        name = input(self.name.get())
        f.write("i am " + name)
        f.close

        label3 = Label(frame_input, text="marks", font=('Goudy old style', 20, 'bold'), fg="orange", bg="white")
        label3.place(x=30, y=195)
        self.marks = Entry(frame_input, font=("times new roman", 15, "bold"), bg='lightgray')
        self.marks.place(x=30, y=245, width=270, height=35)

        btn1 = Button(frame_input, text="make resume", command=self.update, cursor='hand2', font=('calibri', 10),
                      bg='white',
                      fg='black', bd=0)
        btn1.place(x=125, y=305)

    def update(self):
        if self.name.get() == "" or self.marks.get() == "":
            messagebox.showerror("Error", "All Field Are Required", parent=self.root)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Root", database="login")
                cur = con.cursor()

                cur.execute("insert into test values(%s,%s)", (self.name.get(), self.marks.get()))

                con.commit()
                con.close()
                messagebox.showinfo("success", "Register Succesfull"
                                    , parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:(str(es))"
                                     , parent=self.root)


root = Tk()
ob = Login(root)
root.mainloop()