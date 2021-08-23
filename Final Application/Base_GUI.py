
from tkinter import messagebox
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import csv

#Plot the base plate
root = Tk()
root.resizable(0, 0)
root.title("Project Parachute Brigade")
root.geometry("600x400")
root.config(background="#00072D")
label_teamname  = Label(root, text="ATL F4, CTRL W", font=("bold", "18"), bg="#00072D", fg="Yellow").place(x = 200, y = 10)
label_present = Label(root, text="Presents", font = ("arial","12","italic"), bg="#00072D", fg="Yellow").place(x=265, y=45)
label_welcome = Label(root, text="Graphanator", font=("Times","15", "bold underline"), bg="#00072D",fg = "Yellow",width="25" ).place(x = 175, y = 80)



image = Image.open("images/download.jpeg")
size = (50,50)
resize_image = image.resize(size)
school_image = ImageTk.PhotoImage(resize_image)

pic = Label(root, image=school_image)
pic.place(y = 0.01)

#Plot the username and password fields
username = StringVar()
password = StringVar()
username_label = Label(root, text ="Username").place(x = 170, y =120, width=100, height=35)
username_enter = Entry(root, bg="white", textvariable = username).place(x=270, y= 120, height=35)
password_label = Label(root, text="Password").place(x=170, y = 170, width=100, height=35)
password_enter = Entry(root, show="*", textvariable = password).place(x = 270, y = 170, height=35)

#Getting the database
rows = []
doc = open('doc.csv', 'r')
csvReader = csv.reader(doc)
for row in csvReader:
    rows.append(row)



#Define the command of the button and place the button

def alpha():
    for i in range (0, len(rows)) :
        if username.get() == rows[i][0] and password.get() == rows[i][1]:
            root.destroy()
            import Window

            break
        elif username.get() != rows[i][0] or password.get() != rows[i][1]:
             i += 1






var1 = IntVar()

def beta():
    if var1.get() == 1:
        password_enter = Entry(root,textvariable = password).place(x = 270, y = 170, height=35)
    elif var1.get() == 0:
        password_enter = Entry(root, show="*", textvariable = password).place(x = 270, y = 170, height=35)




privacy = Checkbutton(root,text="Show Password", variable=var1, command=beta, onvalue=1, offvalue=0).place(x=273, y = 205.5)

login = Button(root, text="Login", command= alpha,bg="#59cd90", width="9").place(x = 169.5, y =206)


root.mainloop()
