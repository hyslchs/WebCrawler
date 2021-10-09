import requests
from bs4 import BeautifulSoup

response = requests.get('http://pythonscraping.com/pages/page1.html')

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.h1)#抓取第一個遇到的<h1>節點
print(soup.h1.text)#只表示<h1>裡面的文字(text)
print(soup.find('h1').text)#用soup尋找第一個<h1> 並表示裡面的文字(text)