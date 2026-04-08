import requests

from bs4 import BeatifulSoup

pagina = requests.get('https://quotes.toscrape.com/')
dados_pagina = BeatifulSoup( pagina.text, 'html.parser' )