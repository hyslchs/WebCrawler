from bs4 import BeautifulSoup
import requests
import os

input_tag = input("輸入tag：")

response = response = requests.get(f"https://unsplash.com/s/photos/{input_tag}")
soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all('img', class_='oCCRx', limit=1)

image_links = [result.get("src") for result in results]

for index, link in enumerate(image_links):
    if not os.path.exists('images'):
        os.mkdir("images") #建立資料夾
    
    img = requests.get(link) #下載圖片

    with open("images\\" + input_tag + str(index+1) + ".jpg", "wb") as file:
        file.write(img.content) 
        
print(image_links)
        