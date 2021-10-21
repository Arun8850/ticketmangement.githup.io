from  tkinter import  *
import webbrowser
root=Tk()
root.geometry("333x444")
def link():
    print("hello")
    webbrowser.open("https://docs.google.com/forms/d/1FWeAOoWUQRaE541ZxCWVFU6Lne4TJ_0vcWAD1RqMeCs/edit")
def group():
    webbrowser.open("https://meet.google.com/bor-yibs-cfk")
def exam():
    webbrowser.open("https://docs.google.com/document/d/15fLp2xJpiHxFp6Tx7E_-kH7KYoGc-3HPtnRU-Qj2YfA/edit")



btn2 = Button(command=link, text="start your exam", cursor="hand2",
              font=("times new roman", 15), fg="white", bg="light green", bd=0, width=15, height=1)
btn2.place(x=10, y=100)
btn4 = Button(command=group, text="group discussion", cursor="hand2",
                      font=("times new roman", 15), fg="white", bg="light green", bd=0, width=15, height=1)
btn4.place(x=10, y=200)
btn4 = Button(command=exam, text="make exam", cursor="hand2",
                      font=("times new roman", 15), fg="white", bg="light green", bd=0, width=15, height=1)
btn4.place(x=10, y=300)
root.mainloop()
