n=[]
import pyautogui
from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query=%EB%82%A0%EC%94%A8') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('div', {'class' : 'main_info' }):
        n.append(anchor.get_text())
pyautogui.alert(n[0][0:len('   16도씨℃    흐림, 어제보다 0˚ 높아요')])