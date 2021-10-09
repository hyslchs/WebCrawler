import requests
from bs4 import BeautifulSoup, StopParsing

response = requests.get('https://pso2.jp/players/news/')

soup = BeautifulSoup(response.text, 'html.parser')

target = soup.find_all("span")
for span in target:
    span.decompose()

target2 = soup.find_all("time")
for time in target2:
    time.decompose()

ul_list = soup.find('ul', class_ = 'topicList').find_all('a')

for ul in ul_list:
    print(ul.get('href').strip() + '\n')
    print(ul.text.strip())
    print('==========================')
    