from tkinter import *
import backend
import email_sender

def submit_command():
    state = backend.state_abb2(state_abb.get())
    online = backend.onlinecheck2(oneorTwo.get())
    zipcode = backend.zip_code2(zip_code.get())
    mile_rad = backend.mile_radius2(mile_radius.get())
    backend.main(state, online, zipcode, mile_rad)
def send_email():
    def submit():
        email_sender.send_email("chessTourney.csv", email_address.get())

    l5 = Label(window, text="Enter Your Email Address")
    l5.grid(row=30, column=0)

    email_address = StringVar()
    e5 = Entry(window, textvariable=email_address)
    e5.grid(row=30, column=1, rowspan=5)

    b2 = Button(window, text="Send My Data", width=10, height=1, command=submit)
    b2.grid(row=35, column=1)

window = Tk()
window.wm_title("Chess Tournament Finder")

l1=Label(window, text="Enter State Abbreviation ")
l1.grid(row=0, column=0)

state_abb = StringVar()
e1=Entry(window, textvariable=state_abb)
e1.grid(row=0, column=1, rowspan=5)

l2 = Label(window, text="Enter \" O \" for online and \" IN \" for in-person tournaments ")
l2.grid(row=5, column=0)

oneorTwo = StringVar()
e2 = Entry(window, textvariable=oneorTwo)
e2.grid(row=5, column=1, rowspan=5)

l3 = Label(window, text="Enter Your Zip Code ")
l3.grid(row=10, column=0)

zip_code = StringVar()
e3 = Entry(window, textvariable=zip_code)
e3.grid(row=10, column=1, rowspan=5)

l4 = Label(window, text="Enter Your Mile Radius From Your Zip Code")
l4.grid(row=15, column=0)

mile_radius = StringVar()
e4 = Entry(window, textvariable=mile_radius)
e4.grid(row=15, column=1, rowspan=5)

b1 = Button(window, text="Submit", width=10, height=1, command=submit_command)
b1.grid(row=20, column=1)

b1 = Button(window, text="Send Email", width=10, height=1, command=send_email)
b1.grid(row=25, column=1)


window.mainloop()