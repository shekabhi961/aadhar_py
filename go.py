import mysql.connector
from tkinter import *
from PIL import Image, ImageTk



root=Tk()
root.title("Window")
root.minsize(width=900,height=450)

photo = ImageTk.PhotoImage(Image.open("D:/logo.png"))
panel = Label(root, image=photo)
panel.pack(side=TOP, fill=BOTH, expand=YES)


id = StringVar()
nm = StringVar()
add = StringVar()
e_date = StringVar()


def data():
    head = Label(root, text="Database Entry", font=("arial", 20, "bold")).pack()

    label_3 = Label(root, text="Id", font=("arial", 10, "bold")).pack()
    entry_3 = Entry(root,textvariable=id).pack()


    label = Label(root, text="Name", font=("arial",10,"bold")).pack()
    entry = Entry(root,textvariable=nm).pack()

    label_1 = Label(root, text="Address", font=("arial", 10, "bold")).pack()
    entry_1 = Entry(root,textvariable=add).pack()

    label_2 = Label(root, text="Exp_date", font=("arial", 10, "bold")).pack()
    entry_2 = Entry(root,textvariable=e_date).pack()

    var = IntVar()
    Gender= Label(root,text='Status',font=("arial",10,"bold")).pack()
    radio = Radiobutton(root, text="Purchased", variable=var, value=0).pack()
    radio_1 = Radiobutton(root, text="Rented", variable=var, value=1).pack()

    submit = Button(root, text="submit", font=("arial", 10, "bold"), command=comp).pack()
    btn1 = Button(root, text="quit",font=("arial", 10, "bold"), command=quit).pack()


def comp():
    uid=id.get()
    name=nm.get()
    Add=add.get()
    exp_date=e_date.get()


    connect = mysql.connector.connect(user='root', password='',
                                      host='localhost',
                                      database='test')


    cursor = connect.cursor()
    cursor.execute("CREATE TABLE Student(id VARCHAR(20),name VARCHAR(20),address VARCHAR(20),E_date DATE )")
    cursor.execute("INSERT INTO Student (id,name,address,E_date) VALUES (%s,%s,%s,%s )",
                   (uid,name,Add,exp_date))


    connect.commit()
    connect.close()


def full():
    Lpdf = Label(root, text="Database",font=("arial",10,"bold"), height=6, width=20).pack()

    btn= Button(root, text='Input Data', height=3, width=10,command=data).pack()
    btn2 = Button(root, text='Exit', height=3, width=10, command=quit).pack()


a=full()
root.mainloop()