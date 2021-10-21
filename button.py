from tkinter import *
import os
root=Tk()
root.geometry("500x600")
def see():
    #npath ="C://Users//ARUN PANDEY//PycharmProjects//pythonProject1"
    #os.startfile(npath)
    npath = "C://Users//ARUN PANDEY//PycharmProjects//pythonProject1/resume.txt"
    os.startfile(npath)




btn1 = Button(text="See vacancy",command=see, cursor='hand2', font=('calibre', 10), bg='white',
                      fg='black', bd=0)
btn1.place(x=125, y=255)
root.mainloop()