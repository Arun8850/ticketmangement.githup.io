#== == == == == == == == == == == Code == == == == == == == == == == == == == =
from tkinter import *
# from PIL import ImageTK
from tkinter import messagebox
import pymysql
import random


class Userdetails:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("1366x700+0+0")
        self.root.resizable(False, False)
        self.userprofile()


    def userprofile(self):
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=0, y=0, height=700, width=1366)

    # =================CODE FOR ImageTK========================

        frame_input = Frame(self.root, bg="white")
        frame_input.place(x=360, y=430, height=450, width=350)

        label1 = Label(frame_input, text="Your Profile", font=('impact', 32, 'bold'), fg="black", bg="white")
        label1.place(x=75, y=20)

        label2 = Label(frame_input, text="Name", font=('Goudy old style', 20, 'bold'), fg="orange", bg="white")
        label2.place(x=35, y=23)
        self.name = Entry(frame_input, font=("times new roman", 15, "bold"), bg='lightgray')
        self.name.place(x=90, y=95, width=260, height=35)

        label3 = Label(frame_input, text="Marks", font=('Goudy old style', 20, 'bold'), fg="orange", bg="white")
        label3.place(x=30, y=195)
        self.age = Entry(frame_input, font=("times new roman", 15, "bold"), bg='lightgray')
        self.age.place(x=90, y=195, width=260, height=35)

        label4 = Label(frame_input, text="College or Organization Name", font=('Goudy old style', 20, 'bold'),
                   fg="orangered", bg="white")
        label4.place(x=30, y=295)
        self.school = Entry(frame_input, font=("times new roman", 15, "bold"), bg='lightgray')
        self.school.place(x=90, y=295, width=260, height=35)

        label5 = Label(frame_input, text="Your Project link ", font=('Goudy old style', 20, 'bold'), fg="orangered",
                   bg="white")
        label5.place(x=30, y=395)
        self.project = Entry(frame_input, font=("times new roman", 15, "bold"), bg='lightgray')
        self.project.place(x=90, y=395, width=260, height=35)

        btn1 = Button(frame_input, text="Login", cursor='hand2', font=('calibri', 10), bg='white',
                  fg='black', bd=0)
        btn1.place(x=30, y=420, width=270, height=35)

    # =============================User sql code=======================#


    def register(self):
        if self.name.get() == "" or self.age.get() == "" or self.school.get() == "" or self.project.get() == "":
            messagebox.showerror("Error", "All Field Are Required", parent=self.root)

        else:
            try:
                f = open("resume.txt", "w")
                nam = self.name.get()
                schoo = self.school.get()
                mark = self.marks.get()
                pro = self.project.get()
                c = f.write("Respected Sir / Madam, \n I  am"+nam +"I    am   an  I.T.enginner by a"
                "profession \n I have cleared my degree form"+schoo +"\n  I have  scored"+mark +"I"
                "had work  on  the various project during my college days \n the link of the project"
                " are as follows: \n"+pro)




                id = random.randint(1000,9999)


                con = pymysql.connect(host="localhost", user="root", password="Root", database="login")
                cur = con.cursor()

                cur.execute("insert into  userprofile values(%s,%s,%s,%s)", (self.name.get(), self.age.get(),
                                                                         self.school.get(),
                                                                         self.project.get()))
                con.commit()
                con.close()
                messagebox.showinfo("success", "Register Succesfull", parent=self.root)

                con = pymysql.connect(host="localhost", user="root", password="Root", database="login")
                cur = con.cursor()

                cur.execute("insert into resume values(%s,%s)", (id, c))
                con.commit()
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:(str(es))"
                     , parent=self.root)


    #def organizationprofile:

        #pass

        #Frame_login = Frame(self.root, bg="white")
        #Frame_login.place(x=0, y=0, height=700, width=1336)
        #label = Label(Frame_login, text="Hi  Bhailog", font=('times new     roman', 32, 'bold'),
                  #fg="black", bg='white')


root = Tk()
ob = Userdetails(root)
root.mainloop()
