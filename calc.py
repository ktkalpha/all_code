from tkinter import *
import tkinter.font as tkFont
root = Tk()
root.title("calc")
root.geometry("202x275")
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
def setTextInput(text):
    txt.insert('end', text)
def setaTextInput(text):
    if not txt.get() == "":
        txt.insert('end', text)
def non():
    get_text = txt.get()
    txt.delete(0, "end")
    txt.insert(0, eval(get_text))
txt = Entry(font=fontStyle, width=12)
txt.place(x=0, y=0)
btn1 = Button(text=7, font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setTextInput(7))
btn1.place(x=0, y=29)
btn1 = Button(text=8, font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setTextInput(8))
btn1.place(x=50, y=29)
btn1 = Button(text=9, font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setTextInput(9))
btn1.place(x=100, y=29)
btn1 = Button(text="X", font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setaTextInput("*"))
btn1.place(x=150, y=29)
#1
btn1 = Button(text=4, font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setTextInput(4))
btn1.place(x=0, y=90)
btn1 = Button(text=5, font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setTextInput(5))
btn1.place(x=50, y=90)
btn1 = Button(text=6, font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setTextInput(6))
btn1.place(x=100, y=90)
btn1 = Button(text="-", font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setaTextInput("-"))
btn1.place(x=150, y=90)
#2
btn1 = Button(text=1, font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setTextInput(1))
btn1.place(x=0, y=150)
btn1 = Button(text=2, font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setTextInput(2))
btn1.place(x=50, y=150)
btn1 = Button(text=3, font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setTextInput(3))
btn1.place(x=100, y=150)
btn1 = Button(text='+', font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setTextInput("+"))
btn1.place(x=150, y=150)

btn1 = Button(text=0, font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setaTextInput(0))
btn1.place(x=50, y=210)
btn1 = Button(text="/", font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setaTextInput("/"))
btn1.place(x=100, y=210)
btn1 = Button(text="=", font=tkFont.Font(family="Lucida Grande", size=25), command=non)
btn1.place(x=150, y=210)
btn1 = Button(text=" .", font=tkFont.Font(family="Lucida Grande", size=25), command=lambda:setaTextInput("."))
btn1.place(x=0, y=210)
root.mainloop()