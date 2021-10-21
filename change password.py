from tkinter import *
import  pymysql
from tkinter import messagebox
root=Tk()
#root.gemotry("400x500")
class abc:


    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.bus()



    def bus(self):
        self.root.geometry("350x400+450+100")
        self.root.resizable(False, False)

        Frame_loging= Frame(self.root, bg="orange")
        Frame_loging.place(x=0, y=0, height=700, width=1366)

        frame_input = Frame(self.root, bg="white")
        frame_input.place(x=10, y=10, height=380, width=330)

        btn1 = Button(frame_input, text="Get help",command=self.change, cursor='hand2', font=('calibre', 10), bg='white',
                      fg='black', bd=0)
        btn1.place(x=125, y=255)

        btn2 = Button(frame_input, text="Book Ticket", command=self.login, cursor="hand2", font=('times new roman', 15),
                      bg='orange', fg='white', bd=0, width=15, height=1)
        btn2.place(x=90, y=290)

        btn3 = Button(frame_input, text="setting", command=self.Register, cursor='hand2',
                      font=('calibre', 10), bg='white', fg='black', bd=0)
        btn3.place(x=110, y=340)

        btn4 = Button(self.root, text="Back", command=root.destroy, cursor='hand2', font=('calibre', 12),
                      bg='orange', fg='white', bd=0)
        btn4.place(x=300, y=0, height='30', width='50')



        btn2 = Button(frame_input, text="confirm", command=self.confirm, cursor="hand2", font=('times new roman', 15),
                  bg='orange', fg='white', bd=0, width=15, height=1)
        btn2.place(x=90, y=290)
'''
    def confirm(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="Root", database="login")
            cur = con.cursor()
            cur.execute("update register set password=%s,confirmpassword=%s where password=%s",(self.c_p.get(), self.c_p.get(), self.o_p.get()))
            messagebox.showinfo("new password created")
            con.commit()
            con.close()
                # messagebox.showinfo("success", "Register Successful for:/n Username: %s/n Password: %s"
                # + self.entry.get() + self.entry2.get(), parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error due to:(str(es))", parent=self.root)
'''

ob = abc(root)
root.mainloop()