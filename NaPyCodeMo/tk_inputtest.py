from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root,text="Hello, "+e.get()+"!")
    myLabel.pack()

startlabel = Label(root,text="Enter Your Name:")
startlabel.pack()

e=Entry(root,width=20,borderwidth=5)
e.pack()

myButton = Button(root,text="Go!",command=myClick,fg="blue",bg="orange")

myButton.pack()

myButton2 = Button(root,text="Quit",command=quit,fg="white",bg="red")
myButton2.pack()

root.mainloop()