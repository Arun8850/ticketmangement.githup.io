from tkinter import *
#from tkin
import pymysql
from tkinter import messagebox
#import calendar
root =Tk()
root.geometry("900x666")
#root.resizable(False, False)

a = Frame(root, bg="orange")
a.place(x=0, y=0, height=700, width=1366)
def show():
    c = Button(root, text="Next", bg="red", relief=SUNKEN)
    c.place(x=400, y=300,height=75,width=150)

    try:
        b=50
        con = pymysql.connect(host="localhost", user="root", password="Root", database="login")
        cur = con.cursor()
        cur.execute("Select * from Details ")
        myresult=cur.fetchall()
        for row in myresult:
            label1 = Label(a, text=row, font=("Goody old style", 20, "bold"), fg='light green',
                           bg='white')
            label1.place(x=20, y=b)
            b=b+50



        con.commit()
        con.close()
        #messagebox.showerror("Success", f"Reservation successful", parent=root)


    except Exception as es:
        messagebox.showerror("Error", f"Error due to:(str(es))", parent=root)
'''
    label1 = Label(a, text="aaa", font=("Goody old style", 20, "bold"), fg='light green',
                   bg='white')
    label1.place(x=30, y=50)


    label2 = Label(a, text="bbbb", font=("Goody old style", 20, "bold"), fg='light green',
                   bg='white')
    label2.place(x=40, y=50)
    '''

show()
root.mainloop()
