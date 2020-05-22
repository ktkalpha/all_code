import time
import webbrowser
import sys
시=0 #<-켜지는 시
분=0 #<-켜지는 분
a=time.localtime()
while True:
    if a.tm_hour==시 and a.tm_min==분:
        webbrowser.open('#사이트_주소')
        break
sys.exit()
