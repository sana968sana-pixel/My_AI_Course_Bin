import requests
from bs4 import BeautifulSoup
import csv

URL='https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094'
headers = {"User-Agent": "Mozilla/5.0"}
response=requests.get(URL,headers=headers)
soup=BeautifulSoup(response.content,'html5lib')


products = []   

table = soup.find_all('li', attrs={'class': 'brwrvr__item-card'})

for row in table:
    product = {}

    title = row.find('h3', class_='bsig__title__text')
    price = row.find('span', class_='bsig__price--displayprice')
    link = row.find('a')

    if title and price:
        product['title'] = title.text.strip()
        product['price'] = price.text.strip()
        product['link'] = link.get('href') if link else ""

        products.append(product)


filename = 'Week6/ebay_products.csv'

with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, ['title', 'price', 'link'])
    w.writeheader()

    for product in products:
        w.writerow(product)

print(" Data saved successfully")