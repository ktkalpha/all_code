while True:
    n=0
    n=input('1=이진수 -> 십진수, 2=십진수 -> 이진수:')
    if n=='1':
        ans=int(input('변환할 이진수를 입력하세요:'), base=2)
        print(n+'을 십진수로 변환하면 '+str(ans)+'입니다.')
    if n=='2':
        n=int(input('변환할 십진수를 입력하세요:'))
        ans = bin(n)[2:len(bin(n))]
        print(str(n)+'을 이진수로 변환하면 '+str(ans)+'입니다.')
