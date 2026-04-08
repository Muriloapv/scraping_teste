import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://quotes.toscrape.com/')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

todas_frases = dados_pagina.find_all('div', class_="quote")

for div in todas_frases:
    text = div.find('span', class_='text')
    print(text.text)