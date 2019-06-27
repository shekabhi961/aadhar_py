import mysql.connector
from tkinter import *
import tkinter as Tkinter
import tkinter.filedialog
from fitz import *
from PIL import Image, ImageTk,ImageOps
import tkinter as tk
import sqlite3


root=Tk()
root.title("Window")
root.minsize(width=900,height=450)


def pdf2img():
    pdf_file = ("C://aunico//input//aadhar.pdf")
    doc = fitz.open(pdf_file)
    n1 = doc.pageCount
    n2 = len(doc)
    assert n1 == n2
    doc.authenticate('######')
    page = doc.loadPage(0)
    pix = page.getPixmap()
    output = "C://aunico//outfile.png"
    pix.writePNG(output)

    img2img()
    png2jpg()
    jpg2pdf()
    Ay()


class Ay(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Ayush")

        self.canvas1 = tk.Canvas(root, width=500, height=350)  # create the canvas (tkinter module)
        self.canvas1.pack(side=RIGHT)

        self.imagepath1 = r"C:\aunico\crop.png"  # include the path for the image (use 'r' before the path string to address any special character such as '\'. Also, make sure to include the image type - here it is jpg)
        self.image1 = ImageTk.PhotoImage(file=self.imagepath1)  # PIL module
        self.canvas1.create_image(200, 150, image=self.image1)  # create a canvas image to place the background image

        self.canvas2 = tk.Canvas(root, width=500, height=350)  # create the canvas (tkinter module)
        self.canvas2.pack(side=LEFT)

        self.imagepath2 = r"C:\aunico\crop2.png"  # include the path for the image (use 'r' before the path string to address any special character such as '\'. Also, make sure to include the image type - here it is jpg)
        self.image2 = ImageTk.PhotoImage(file=self.imagepath2)  # PIL module
        self.canvas2.create_image(200, 150, image=self.image2)  # create a canvas image to place the background image


#---

#--- --crop image
def img2img():
    image = Image.open("C://aunico//outfile.png")
    area = (30,526,265,680)
    crop_image= image.crop(area)
    crop_image.save('C://aunico//crop2.png', 'PNG')

    #### img2img2
    image2 = Image.open("C://aunico//outfile.PNG")
    area2 = (280,526,518,682)
    crop_image2= image2.crop(area2)
    crop_image2.save('C://aunico//crop.png', 'PNG')


def png2jpg():
    imge = Image.open("C:/aunico/crop.png")
    imge2 = imge.convert('RGB')
    imge2.save('C:/aunico/logic.jpg')

    # PNG2 to JPG2-----------------

    pyt = Image.open("C:/aunico/crop2.png")
    pyt2 = pyt.convert('RGB')
    pyt2.save('C:/aunico/logic2.jpg')


def jpg2pdf():
    img= Image.open("C:/aunico/logic.jpg")

    pdf_path = "C:/aunico/imagepdf.pdf"

    img.save (pdf_path,"PDF",save= True,ndpi='200', imgwidthpx='200', imgheightpx='200')

    #------------------------------

    img2= Image.open("C:/aunico/logic2.jpg")

    pdf_path2 = "C:/aunico/imagepdf2.pdf"

    img2.save (pdf_path2,"PDF",save= True,ndpi='200', imgwidthpx='200', imgheightpx='200')

#-------------------------

id = StringVar()
nm = StringVar()
add = StringVar()
dob = StringVar()
mob = StringVar()


def data():

    head = Label(root, text="AADHAR CARD FORM", font=("arial", 20, "bold")).pack()

    label_3 = Label(root, text="Adhar_No", font=("arial", 10, "bold")).pack()
    entry_3 = Entry(root,textvariable=id).pack()


    label = Label(root, text="Name", font=("arial", 10, "bold")).pack()
    entry = Entry(root,textvariable=nm).pack()

    label_1 = Label(root, text="Address", font=("arial", 10, "bold")).pack()
    entry_1 = Entry(root,textvariable=add).pack()

    label_2 = Label(root, text="DOB", font=("arial", 10, "bold")).pack()
    entry_2 = Entry(root,textvariable=dob).pack()

    label_4 = Label(root, text="Mobile_No", font=("arial", 10, "bold")).pack()
    entry_4 = Entry(root,textvariable=mob).pack()

    var = IntVar()
    Gender= Label(root,text='Gender',font=("arial",10,"bold")).pack()
    radio = Radiobutton(root, text="male", variable=var, value=0).pack()
    radio_1 = Radiobutton(root, text="female", variable=var, value=1).pack()

    submit = Button(root, text="submit", font=("arial", 10, "bold"), command=comp).pack()
    btn1 = Button(root, text="quit",font=("arial", 10, "bold"), command=quit).pack()


def comp():
    uid=id.get()
    name=nm.get()
    addr=add.get()
    DoB=dob.get()
    MoB=mob.get()

    connect = mysql.connector.connect(user='root', password='',
                                      host='localhost',
                                      database='test')

    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXIST Student (id INTEGER,name TEXT,address INTEGER,dob TEXT,mob INTEGER)")
    cursor.execute("INSERT INTO persons VALUES (?,'?','?','?',?,)",(uid,name,addr,DoB,MoB))

    connect.commit()
    connect.close()


#open browse------
def ray():
    Tkinter.Tk().withdraw()  # Close the root window
    in_path = tkinter.filedialog.askopenfilename()
    print(in_path)



def full():
    Lpdf = Label(root, text="YOUR AADHAR CARD",font=("arial",10,"bold"), height=6, width=20).pack()
    entry= Entry((root)).pack()
    btn=Button(root, text='open', height=2, width=5, command=ray).pack()
    btn1=Button(root, text='Select', height=3, width=10,command=pdf2img).pack()
    btn3= Button(root, text='Info', height=3, width=10,command=data).pack()


a=full()
root.mainloop()