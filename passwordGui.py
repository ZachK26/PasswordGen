from tkinter import *
import os
from passwordGenAlg import *

og = ""


#the function to copy a string to the clipboard
def addToClipBoard(str):
 import tempfile
 with tempfile.NamedTemporaryFile("w") as fp:
  fp.write(str)
  fp.flush()
  command = "pbcopy < {}".format(fp.name)
  os.system(command)

#to change the label in order to display the password
def changenow():
   temp = wtf()
   lbl['text'] = temp
   addToClipBoard(temp)

def changenowforten():
   temp = tenLetter()
   lbl['text'] = temp
   addToClipBoard(temp)

def changenowfortwenty():
   temp = twentyLetter()
   lbl['text'] = temp
   addToClipBoard(temp)

def oofer():
   wtf()
   changenow()

def tenlet():
   tenLetter()
   changenowforten()

def twentylet():
    twentyLetter()
    changenowfortwenty()

def ghostMode():
    if var1.get() == 1:
        lbl.config(fg='white')
    if var1.get() == 0:
        lbl.config(fg='red')

#creating the window
window=Tk()
btn=Button(window, text="Generate 8 Character Password", fg='blue', command = changenow)
btn.place(x=0, y=150)
btn2=Button(window, text="Generate 10 Character Password", fg='blue', command = tenlet)
btn2.place(x=0, y=180)
btn3=Button(window, text="Generate 20 Character Password", fg='blue', command = twentylet)
btn3.place(x=0, y=210)
copy1=Button(window, text="Copy", fg='blue', command = addToClipBoard)
copy1.place(x=350, y=228)
lbl1=Label(window, text="Password Generator", fg='red', font=("Comic_Sans", 16))
lbl1.place(x=100, y=10)
var1 = IntVar()
c1 = Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=ghostMode)
c1.pack()
c1.place(x=50, y=50)
lbl=Label(window, text  = og , anchor = "e", justify = RIGHT, fg='red', width = 20, font=("Comic_Sans", 16))
lbl.place(x=190, y=260)
window.title('Mysts Password Gen')
window.geometry("400x300")
window.mainloop()


#use the lbl bit to make a display for what the generated password is

