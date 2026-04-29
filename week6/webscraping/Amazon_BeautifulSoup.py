import requests
from bs4 import BeautifulSoup
import csv

url='https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2'

r= requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')
productlist=[]
products=soup.find_all('li',attrs={'class':"a-carousel-card "})

for item in products:
    product={}
    title=soup.find('div',class_='ucw-widget-product-card-title').text
    rating=soup.find('div',class_='ucw-widget-product-card-review').text
    price=soup.find('div',class_='ucw-widget-product-card-price').text
    shiping=soup.find('div',class_='a-color-secondary a-size-base').text


    product['title']=title
    product['rating']=rating
    product['price']=price
    product['shiping']=shiping

    productlist.append(product)

filename="week6/Amazon_beautifulSoup.csv"
with open(filename,'w',newline="",)as f:
    w=csv.DictWriter(f,['title','rating','price','shiping'])
    w.writeheader()
    for product in productlist:
        w.writerow(product)
