# program to make the pdf
from fpdf import FPDF
from  tkinter import *
class baba:

    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.frame()


    def resume(self):
        try:


            my_pdf = FPDF()
            name = self.username_txt.get()
            marks = self.Marks_txt.get()
            my_pdf.add_page()
            my_pdf.set_font("Arial",size=16)
            my_pdf.cell(200,10,txt="My Resume",ln=1,align="C")
    #name=input("Enter your name")
    #marks=input("Enter your marks")
            text=("i am "+self.username_txt.get()+"i have secured"+self.Marks_txt.get()+"in my acedemics")
            my_pdf.cell(200,10,txt=text,ln=2,align="C")

            my_pdf.output("myPDF.pdf")

        except Exception as es:
            print("error")





    def frame(self):
        self.root.geometry("350x400+450+100")
        self.root.resizable(False, False)

        Frame_login = Frame(self.root, bg="orange")
        Frame_login.place(x=0, y=0, height=700, width=1366)
        label1 = Label(text="Username", font=('Goody old style', 20, 'bold'), fg="orange", bg="white")
        label1.place(x=30, y=45)
        self.username_txt = Entry(font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.username_txt.place(x=30, y=95, width=270, height=35)
        label2 = Label(text="Marks", font=('Goody old style', 20, 'bold'), fg="orange", bg="white")
        label2.place(x=30, y=150)
        self.Marks_txt = Entry(font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.Marks_txt.place(x=30, y=200, width=270, height=35)

        btn1 = Button(text="Login", command=self.resume, cursor="hand2", font=('times new roman', 15), bg='orange', fg='white',
              bd=0, width=15, height=1)
        btn1.place(x=90, y=290)


root = Tk()


ob = baba(root)
root.mainloop()






