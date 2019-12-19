import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs
import json
import matplotlib.pyplot as plt

url = rq.get('https://www2.2019seagames.com/countries/')
soup = bs(url.content, 'html.parser')

# Maaf pak saya belum bisa scraping, nanti saya akan belajar lagi

a= soup.find_all('em')
scrape = [i.get_text() for i in a]
scrape = (scrape)
scrape = scrape.split
print (scrape)

negara = []
for e in len(scrape):
    if e%7== 0 or e==0 :
        negara.append (e)
print (negara)
