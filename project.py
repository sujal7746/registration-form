from dataclasses import field
#import kinter file
from tkinter import *

#tkinter for graphical interface // pip install

root = Tk() #import kinter file in root
root.geometry("500x300") #registration frame
#define function for submit btn
def getvals():
    print("Accepted")
#for heading
Label(root, text= "Registration Form", font= "arial 15 bold").grid(row=0, column = 3 )

#field Name

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")

#packing fields
name.grid(row = 1, column= 2)
phone.grid(row = 2, column= 2)
gender.grid(row = 3, column= 2)

#Creating Variable for storing value
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
checkvalue = IntVar

#creating entry field
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)

#packing entry field
nameentry.grid(row = 1, column=3 )
phoneentry.grid(row = 2, column= 3)
genderentry.grid(row = 3, column=3 )

#Creating Checkbox
checkbtn = Checkbutton(text="remember me? ", variable=checkvalue)
checkbtn.grid(row= 4, column= 3)

#Submit Button
Button(text="Submit", command=getvals).grid(row=5, column= 3)
#main
root.mainloop()