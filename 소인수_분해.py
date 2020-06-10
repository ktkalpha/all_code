d=2
a=int(input('소인수 분해:'))
while True:
    if a%d==0:
        a=a//d
        print(d)
    else:
        d=d+1
