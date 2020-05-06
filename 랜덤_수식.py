import random as r
import pyautogui
n=""
k=r.randint(0,9)
for x in range(6):
    k = r.randint(0,4)
    if k==1:
        n=n+str(r.randint(0,9))+'+'
    if k == 2:
        n = n + str(r.randint(0, 9)) + '-'
    if k==3:
        n=n+str(r.randint(0,9))+'/'
    if k == 4:
        n = n + str(r.randint(0, 9)) + '*'
n=n[0:len(n)-1]
pyautogui.alert(n+'='+str(eval(n)))
