import time
while True:
    if time.gmtime().tm_hour+9>12:
        print(str(time.gmtime().tm_hour + 9-12) + ':' + str(time.gmtime().tm_min) + ':' + str(time.gmtime().tm_sec))
    else:
        print(str(time.gmtime().tm_hour + 9) + ':' + str(time.gmtime().tm_min) + ':' +str(time.gmtime().tm_sec))
    time.sleep(1)
