import turtle as t
def d():
    t.setx(t.xcor()+30)
def a():
    t.setx(t.xcor()-30)
def w():
    t.sety(t.ycor()+30)
def s():
    t.sety(t.ycor()-30)
t.onkeypress(d,'d')
t.onkeypress(a,'a')
t.onkeypress(w,'w')
t.onkeypress(s,'s')
t.onkeypress(t.up,'Up')
t.onkeypress(t.down,'Down')
t.onkeypress(t.clear,'space')
t.listen()
t.mainloop()
