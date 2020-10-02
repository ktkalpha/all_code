from bs4 import BeautifulSoup
from urllib.request import urlopen
url = input("url : ")
index = input("index : ")
with urlopen(url) as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all(index):
        print(anchor.get_text())
input("pause")
