import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as message
app = tk.Tk()
def onlogin():
    def onok():
        global _id
        _id = txt1.get()
        app1.destroy()
    app1 = tk.Tk()
    lbl = tk.Label(app1, text="ID", font=fontStyle)
    lbl.grid(row=0, column=0)
    txt1 = tk.Entry(app1, font=fontStyle)
    txt1.grid(row=0, column=1)
    btn = tk.Button(app1, text="OK", font=fontStyle, command=onok)
    btn.grid(row=2, column=1)
    app1.title("Sign up")
    app1.mainloop()
def onsign():
    def onok2():
        if _id == txt1.get():
            message.showinfo("login!", "login!")
            app1.destroy()
        else:
            message.showerror("login fail", "login fail")
    app1 = tk.Tk()
    lbl = tk.Label(app1, text="ID", font=fontStyle)
    lbl.grid(row=0, column=0)
    txt1 = tk.Entry(app1, font=fontStyle)
    txt1.grid(row=0, column=1)
    btn = tk.Button(app1, text="OK", font=fontStyle, command=onok2)
    btn.grid(row=2, column=1)
    app1.title("Login")
    app1.mainloop()

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
buttonExample1 = tk.Button(app, text="Sign up", font=fontStyle, command=onlogin)
buttonExample2 = tk.Button(app, text="Login", font=fontStyle, command=onsign)

buttonExample1.pack(side=tk.LEFT)
buttonExample2.pack(side=tk.LEFT)
app.mainloop()
