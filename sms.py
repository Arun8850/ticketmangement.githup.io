import os
from twilio.rest import Client
from tkinter import *


def send_sms(number, message):
    account_sid = 'ACf0227b3f25d89d9a7437e089f110696a'
    auth_token = '4b7dc9607172b066fc35066789bc5ec4'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=message,
        from_='+15158085366',
        to=number
    )

    print(message.sid)


def btn_click():
    num = textNumber.get()
    msg = textMessage.get()
    send_sms(num,msg)


root = Tk()
root.title("Message Sender")
root.geometry("400x500")
font = ("Helvetca", 22, "bold")

textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)

textMessage = Text(root)
textMessage.pack(fill=X)

sendBtn = Button(root, text="SEND SMS", command=btn_click)
sendBtn.pack()

root.mainloop()