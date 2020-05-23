import time
import webbrowser
import sys
chrome_path = ''#<-브라우저_path ex)=C:/Program Files (x86)/Naver/Naver Whale/Application/whale.exe
시=12 #<-켜지는 시
분=26 #<-켜지는 분
사이트_주소='naver.com' #<-사이트 주소
while True:
    a = time.gmtime()
    if a.tm_hour+9==시 and a.tm_min==분:
        webbrowser.get(chrome_path+' %s').open(사이트_주소)
        break
sys.exit()
