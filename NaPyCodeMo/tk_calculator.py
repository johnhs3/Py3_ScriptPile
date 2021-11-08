from tkinter import *
from tkinter.font import Font
root = Tk()
root.title("4-Func. Calc.")
root.resizable(width=False, height=False)

#Functions to be called by buttons:
txt = ""
res = False
ans = 0
equation = StringVar()
mem = ""


# Define Output Window / Display and Place Onscreen
e = Entry(root, width = 22, borderwidth = 5,textvariable=equation,font=("Aerial",20))
e.grid(row=0, column=0, columnspan=4, padx=10,pady=10)

#functions
def press(num):
   global txt, ans, res
   if (res==True):
      txt = ans
      res = False
   txt = txt + str(num)
   equation.set(txt)

def equal():
   try:
      global txt, ans, res
      ans = str(eval(txt))
      equation.set(ans)
      res = True
   except:
      equation.set("ERROR : Invalid Equation")
      txt=""

def clear():
   global txt, ans, res
   txt = ""
   equation.set("")
   res = False


# Define buttons
button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: press(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: press(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: press(3))

button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: press(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: press(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: press(6))

button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: press(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: press(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: press(9))

button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: press(0))
button_dec = Button(root,text=".",padx=42,pady=20,command=lambda: press("."))
button_exp = Button(root,text="^",padx=39,pady=20,command=lambda: press("**"))


button_add = Button(root,text="+",padx=38,pady=20,command=lambda: press("+"))
button_subtract = Button(root,text="-",padx=39,pady=20,command=lambda: press("-"))
button_multiply = Button(root,text="*",padx=39,pady=20,command=lambda: press("*"))
button_divide = Button(root,text="/",padx=39,pady=20,command=lambda: press("/"))

button_equal = Button(root,text="=",padx=85,pady=20,command=equal)
button_clear = Button(root,text="Clear",padx=77,pady=20,command=clear)


# Put the buttons on the screen
button_clear.grid(row= 1, column=0, columnspan=2)
button_equal.grid(row= 1, column=2, columnspan=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_divide.grid(row=2,column=3)


button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multiply.grid(row=3,column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_subtract.grid(row=4,column=3)

button_exp.grid(row=5, column=2)
button_0.grid(row=5, column=1)
button_dec.grid(row=5, column=0)
button_add.grid(row=5, column=3)



root.mainloop()