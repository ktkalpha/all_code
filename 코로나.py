from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyautogui
import time
n=[]

with urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%95%9C%EA%B5%AD%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90&oquery=%ED%95%9C%EA%B5%AD%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90+%EC%82%AC%EC%9D%B4%ED%8A%B8&tqi=UpzFgdprvmZsskp2GKdssssstRs-515551') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('strong', {'class' : 'num'}):
        n.append(anchor.get_text())   
while True:
    de=pyautogui.confirm(text="확진자 수="+n[0]+" 사망자 수="+n[3],buttons=['새로 고침','종료'])
    if de=='새로 고침':
        n=[]

        with urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%95%9C%EA%B5%AD%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90&oquery=%ED%95%9C%EA%B5%AD%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90+%EC%82%AC%EC%9D%B4%ED%8A%B8&tqi=UpzFgdprvmZsskp2GKdssssstRs-515551') as response:
            soup = BeautifulSoup(response, 'html.parser')
            for anchor in soup.find_all('strong', {'class' : 'num'}):
                n.append(anchor.get_text())
    if de=='종료':
        break
