from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Title of App")
root.iconbitmap("face_angel.ico")

button_quit = Button(root,text="Exit Program",command=root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open("conway.jpg"))
my_label = Label(image = my_img)
my_label.pack()

my_text = Label(text="RIP John Horton Conway, A Pioneer in Mathematics and Computer Science. (1937-2020)")
my_text.pack()


root.mainloop()