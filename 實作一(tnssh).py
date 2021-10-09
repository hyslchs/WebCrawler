import requests
from bs4 import BeautifulSoup

# Get HTML and parse it
response = requests.get('http://www.tnssh.tn.edu.tw/default.asp')
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')


# Print the gifts
table_list = soup.find('table', summary = '最新消息列表' ).find_all('a')


for table in table_list:

    print(table.text.strip() + '\n', )
    print('http://www.tnssh.tn.edu.tw/' + table.get('href') + '\n')
    print('------------------------------------------------')