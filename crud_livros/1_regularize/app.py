# import requests 
# from bs4 import BeautifulSoup

# #Body request
# url         = 'https://www.listadevedores.pgfn.gov.br/api/devedores/'
# nome        = "murilo varoto"
# id          = "11462916988"
# naturezas   = "00000000000"
# payload     =  { "id": id, "naturezas": naturezas, "nome" : nome }
# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json, text/plain, */*",
#     "Origin": "https://www.listadevedores.pgfn.gov.br",
#     "Referer": "https://www.listadevedores.pgfn.gov.br/",
#     "User-Agent": "Mozilla/5.0"
# }
# resposta = requests.post(url, json=payload, headers=headers)

# resposta.encoding = 'utf-8'
# print( resposta.status_code )
# print( resposta.json())


import requests
from bs4 import BeautifulSoup
import json

pagina = requests.get('https://www.flaviaguiarmelo.com.br/2023/06/basics-metodos-procedures-e-funcoes.html')
#pagina = requests.get('https://quotes.toscrape.com/')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

todas_frases = dados_pagina.find_all('div', class_="quote")
todas_frases = dados_pagina.find_all('div', id_='post-body-121169413875491')
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