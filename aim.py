import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as message
import random
point = 0
app = tk.Tk()
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
def on1():
    if l.cget('text') == "red":
        randomset()
    else:
        global point
        point = point - 1
        l1['text'] = point
def on2():
    if l.cget('text') == "yellow":
        randomset()
    else:
        global point
        point = point - 1
        l1['text'] = point
def on3():
    if l.cget('text') == "green":
        randomset()
    else:
        global point
        point = point - 1
        l1['text'] = point

def on4():
    if l.cget('text') == "blue":
        randomset()
    else:
        global point
        point = point - 1
        l1['text'] = point
def randomset():
    n = random.randint(1,4)
    if n == 1:
        l['text'] = "red"
    if n == 2:
        l['text'] = "yellow"
    if n == 3:
        l['text'] = "green"
    if n == 4:
        l['text'] = "blue"
    global point
    point = point + 1
    l1['text'] = point

l=tk.Label(text="red", font=fontStyle)
l.grid(row=1, column=0)
l1=tk.Label(text="0", font=fontStyle)
l1.grid(row=1, column=1)
btn1 = tk.Button(app, text="red", font=fontStyle, bg="red", width=5, command=on1, highlightcolor="red")
btn1.grid(row=2, column=0)
btn2 = tk.Button(app, text="yellow", font=fontStyle, width=5, bg="yellow", command=on2, highlightcolor="yellow")
btn2.grid(row=2, column=1)
btn3 = tk.Button(app, text="green", font=fontStyle, width=5, bg="green", command=on3, highlightcolor="green")
btn3.grid(row=3, column=0)
btn4 = tk.Button(app, text="blue", font=fontStyle, width=5, bg="blue", command=on4, highlightcolor="blue")
btn4.grid(row=3, column=1)
app.mainloop()
