from bs4 import BeautifulSoup
import requests
import random
import os


#https://yande.re/post?tags=
input_tag = input("輸入tag：")
input_tag = (input_tag + '+')

response = response = requests.get(f"https://yande.re/post?tags={input_tag}")
soup = BeautifulSoup(response.text, "html.parser")


results = soup.find('ul', id ='post-list-posts').find_all('li', limit=1)
results = soup.find('a', class_ ='thumb').get('href')
link = ('https://yande.re/' + results)
#source = random.choice[results]

response = response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")
results = soup.find("div",class_='content').find('img').get("src")
print(results)
    