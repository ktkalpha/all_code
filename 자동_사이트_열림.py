import time
import webbrowser
import sys
a=time.localtime()
while True:
    if a.tm_hour==#켜지는_시 and a.tm_min==#켜지는_분:
        webbrowser.open('#사이트_주소')
        break
sys.exit()
