r=0
g=0
b=0
import turtle as t
t.colormode(255)
while True:
    for x in range(255):
        t.bgcolor(r,g,b)
        r=r+1
        if not g==0 and not b==0:
            g=g-1
            b=b-1
    for x in range(255):
        t.bgcolor(r,g,b)
        g=g+1
        if not r==0 and not b==0:
            r=r-1
            b=b-1
    for x in range(255):
        t.bgcolor(r,g,b)
        b=b+1
        if not r==0 and not g==0:
            r=r-1
            g=g-1
