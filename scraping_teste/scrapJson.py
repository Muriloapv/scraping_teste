import requests
from bs4 import BeautifulSoup
import json

pagina = requests.get('https://quotes.toscrape.com/')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

todas_frases = dados_pagina.find_all('div', class_="quote")

lista_frases = []

for div in todas_frases:
    texto  = div.find('span', class_='text').text
    autor = div.find('small', class_='author' ).text

    lista_frases.append({
        "texto":texto,
        "autor":autor
    })
    print(texto)

with open('frases.json', 'w', encoding='utf-8') as arquivo:
        json.dump(lista_frases, arquivo, indent=4, ensure_ascii=False)

print( 'Aquivo frases.json criado com sucesso')