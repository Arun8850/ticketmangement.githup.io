import random
import smtplib
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from twilio.rest import Client

from PIL import ImageTk
class abc:
    def __init__(self, root):
        #root=Tk()

        self.root = root
        self.root.overrideredirect(True)
        self.root.geometry("1200x1200+0+0")
        self.root.resizable(True, True)
        self.busreservation()


    def getvals(self):
        if self.a.get() == "" or self.b.get() == "" or self.spin1.get() == "" or self.spin2.get() == "" or self.spin3.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Root", database="login")
                cur = con.cursor()
                cur.execute("INSERT INTO Reservation ( FromCity,ToCity,Month,Date,Year) values (%s,%s,%s,%s,%s)",
                            (self.a.get(), self.b.get(), self.spin1.get(), self.spin2.get(), self.spin3.get()))
                con.commit()
                con.close()
                messagebox.showerror("Success", f"Reservation successful", parent=self.root)




            except Exception as es:

                messagebox.showerror("Error", f"Error due to:(str(es))", parent=self.root)

            # c = Frame(root, bg="white")
            # c.place(x=10, y=10, height=2000, width=2000)


    # root.geometry("1200x800")
    def busreservation(self):
       # self.root.geometry("1000x1000+0+0")
        #self.root.resizable(True, True)
        self.j = ImageTk.PhotoImage(file="pythonProject1.jpg")
        b = Label(self.root, image=self.j).pack()
        user = Label(root, text="Book the ticket", font="Helvetica 16 bold", fg="red", pady=0)
        user.place(x=0, y=0)
        user = Label(root, text="From", font="Helvetica 16 bold", fg="black", pady=0)
        user.place(x=200, y=100)
        user1 = Label(root, text="To", font="Helvetica 16 bold", fg="black", pady=0)
        user1.place(x=730, y=100)

        self.a = ttk.Combobox(root, values=(
        "Mahim", "Bandra", "dadar", "Andheri", "Borivali", "Kandivali", "kalyan", "Dombivali"),
                              font=("times new roman", 20, "bold"), justify=CENTER, state='readonly')
        self.a.place(x=300, y=100, width=400, height=40)
        self.a.set("select your choice")
        self.b = ttk.Combobox(root, values=(
        "Mahim", "Bandra", "dadar", "Andheri", "Borivali", "Kandivali", "kalyan", "Dombivali"),
                              font=("times new roman", 20, "bold"), justify=CENTER, state='readonly')
        self.b.place(x=800, y=100, width=400, height=40)
        self.b.set("select your choice")

        c = Button(root, text="SERACH BUS", command=self.getvals, bg="red", relief=SUNKEN)
        c.place(x=400, y=300)
        # date....................................
        #self.root.config(bg="sky blue")

        lb1 = Label(root, text="Month", font=('arial', 9, 'bold')).place(x=200, y=200)
        lb2 = Label(root, text="Year", font=('arial', 9, 'bold')).place(x=300, y=200)
        lb3 = Label(root, text="Date", font=('arial', 9, 'bold')).place(x=400, y=200)
        self.spin1 = Spinbox(root, values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), width=4)
        self.spin1.place(x=245, y=200)
        self.spin2 = Spinbox(root, from_=1999, to=2100, width=4)
        self.spin2.place(x=340, y=200)
        self.spin3 = Spinbox(root, values=(
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31),
                             width=4)
        self.spin3.place(x=440, y=200)
        self.spin3.place(x=440, y=200)
root=Tk()

#root = tk.ThemedTk()
#root.get_themes()
#root.set_theme("black")


ob = abc(root)
root.mainloop()