
확률=100
import random as r

while True:
    input('확률 서바이벌:')
    if r.randint(1,100)>=확률:
        print(str(확률)+'% 사망')
        break
    else:
        print(str(확률) + '% 생존')
        확률=확률-1
