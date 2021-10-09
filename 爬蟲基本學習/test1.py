import requests

params = {'firstname' : 'suzuhara', 'lastname' : 'ruru'}

response = requests.post('http://pythonscraping.com/pages/files/processing.php', data = params)

print(response.text)