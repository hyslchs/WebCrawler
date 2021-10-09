import requests
from bs4 import BeautifulSoup

# Get HTML and parse it
response = requests.get('http://pythonscraping.com/pages/page3.html')

soup = BeautifulSoup(response.text, 'html.parser')


# Print the gifts
tr_list = soup.find_all('tr', class_ = 'gift')

for tr in tr_list:#找出tr裡面的img再取出src #strip去掉首尾空白  #replace(A,B)即把字串裡的A換成B
    print(tr.find('img').get('src').strip().replace('..', 'https://www.pythonscraping.com') + '\n')

    td_list = tr.find_all('td')

    for td in td_list:
        print(td.text.strip() + '\n')