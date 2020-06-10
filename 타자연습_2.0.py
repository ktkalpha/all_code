from tkinter import filedialog
n=[]
file =  filedialog.askopenfilenames(initialdir ="C:/",title = "choose your file")
file=str(file).replace('(','')
file=str(file).replace(')','')
file=str(file).replace(',','')
file=str(file).replace("'",'')
f = open(file, 'r', encoding='UTF-8')
while True:
    line = f.readline().replace('\n','')
    if not line: break
    n.append(line)
f.close()
print(n)
import random
점수=0
nc=random.randint(0,len(n)-1)
import time
timer=time.time()
while True:
    a = input(n[nc] + ':')
    if a==n[nc]:
        print('오케이!')
        if len(n)==1:
            del n[nc]
            break
        else:
            del n[nc]
        점수=점수+1
        nc = random.randint(0, len(n)-1)
timer=timer-time.time()
print(str(abs(timer))+' 초가 걸렸습니다.')
