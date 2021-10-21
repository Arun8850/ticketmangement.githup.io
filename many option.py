from tkinter import *
from PIL import ImageTk
import Train




class abcd:

    def __init__(self, root):
        self.root = root
        self.root.geometry("450x400")
        self.root.config(bg="red")
        # self.root.title("login form")

        label2 = Label(text="Choose your choice", font=("Goody old style", 20, "bold"), fg='light green',
                       bg='white')
        label2.place(x=0, y=0)
        b = Button(self.root, text="Bus", cursor="hand2",
                   font=("times new roman", 15), fg="white", bg="light green", bd=0, width=15, height=1)
        b.place(x=10, y=40, height=100, width=100)
        a = Button(self.root, text="Train",command=self.add_train, cursor="hand2",
                   font=("times new roman", 15), fg="white", bg="light green", bd=0, width=15, height=1)
        a.place(x=300, y=40, height=100, width=100)
        c = Button(self.root, text="Flight", cursor="hand2",
                   font=("times new roman", 15), fg="white", bg="light green", bd=0, width=15, height=1)
        c.place(x=10, y=200, height=100, width=100)
        d = Button(self.root, text="Emergency", cursor="hand2",
                   font=("times new roman", 15), fg="white", bg="light green", bd=0, width=15, height=1)
        d.place(x=300, y=200, height=100, width=100)
    def add_train(self):
        Train.busreservation()
        #self.new_win=Toplevel(self.root)
        #self.new_obj=abc(self.new_obj)
        #pass



root = Tk()
ob = abcd(root)
root.mainloop()