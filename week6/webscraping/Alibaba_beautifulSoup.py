import requests
from bs4 import BeautifulSoup
import csv
url='https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.132.2ce267afSeLPmg&SearchText=Auto+Accessories&indexArea=product_en&search_cource_scene=pc_home_product_category&has4Tab=true&tab=all'

r=requests.get(url)
soup= BeautifulSoup(r.content,'html5lib')
productlist=[]
products=soup.find_all('div',attrs={'class':"fy26-product-card-wrapper"})
for item in products:
    product={}
    title=item.find('h2',class_='fy26-card-title-line-clamp').text
    price=item.find('div',class_='searchx-product-price price--two-line').text

    product['title']=title
    product['price']=price
    productlist.append(product)

filename="week6/Alibaba_beautifulsoup.csv"
with open (filename,'w',newline="")as f:
    w=csv.DictWriter(f,['title','price'])
    w.writeheader()
    for product in productlist:
        w.writerow(product)