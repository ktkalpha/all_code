import time
from tkinter import *

kst = time.localtime()

ko_num = ["한", "두", "세", "네", "다섯", "여섯", "칠곱", "여덟", "아홉", "열", "열한", "열두"]
ko_num2 = ["일", "이", "삼", "사", "오", "육", "칠", "팔", "구", "십", "십일", "십이", "십삼", "십사", "십오", "십육", "십칠", "십팔", "십구", "이십", "이십일", "이십이", "이십삼", "이십사", "이십오", "이십육", "이십칠", "이십팔", "이십구", "삼십", "삼십일", "삼십이", "삼십삼", "삼십사", "삼십오", "삼십육", "삼십칠", "삼십팔", "삼십구", "사십", "사십일", "사십이", "사십삼", "사십사", "사십오", "사십육", "사십칠", "사십팔", "사십구", "오십", "오십일", "오십이", "오십삼", "오십사", "오십오", "오십육", "오십칠", "오십팔", "오십구", "육십"]

root = Tk()
def update():
    kst = time.localtime()
    timer.configure(text=ko_num[kst.tm_hour-13] + "시\n" + ko_num2[kst.tm_min-1] + "분\n" + ko_num2[kst.tm_sec-1] + "초")
    root.after(100, update)
timer = Label(text = "jjjjjjjjjjjjjjj", font = ("맑은 고딕", 50))
timer.pack()
update()
root.mainloop()