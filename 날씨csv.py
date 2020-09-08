import csv
import time
#{'id' : 'wob_dc'}
def update():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen

    with urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8') as response:
        soup = BeautifulSoup(response, 'html.parser')
        for anchor in soup.find_all('p', {'class' : 'cast_txt'}):
            return anchor.get_text()

now = (str(time.gmtime().tm_year) + "-" +str(time.gmtime().tm_mon) + "-" +str(time.gmtime().tm_mday) + "-" +str(time.gmtime().tm_hour + 9) + "-" +str(time.gmtime().tm_min) + "-" +str(time.gmtime().tm_sec))
f = open('output.csv', 'w', encoding='utf-8', newline='')
while True:
    consol_input = str(input("consol:"))
    if consol_input == "quit":
        break
    elif consol_input == "update":
        now = (str(time.gmtime().tm_year) + "-" + str(time.gmtime().tm_mon) + "-" + str(time.gmtime().tm_mday) + "-" + str(time.gmtime().tm_hour + 9) + "-" + str(time.gmtime().tm_min) + "-" + str(time.gmtime().tm_sec))
        wr = csv.writer(f)
        wr.writerow([now, "", update()])
f.close()
