import requests
from bs4 import  BeautifulSoup
import csv

url='https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel'

r= requests.get(url)

soup=BeautifulSoup(r.content,'html5lib')
productlist =[]

products=soup.find_all('div',class_="Bm3ON")
for item in products:
    product={}
    title=item.find('div',class_="RfADt")
    price=item.find('span', class_="ooOxS")
    link=item.find('a')
    discount=item.find('span',class_="IcOsH").text
    if title and price:
        product["title"]=title.text.strip()if title else""
        product['price']=price.text.strip()if price else ""
        product['link']=link ["href"]if link and link.get("href") else ""

        product['discount']=discount.text.strip()if discount else""

    productlist.append(product)
filename="week6/webscraping/daraz_beautifulsoup.csv"
with open(filename,'w',newline="",encoding="utf_8") as f:
    w=csv.DictWriter(f,["title","price","link",'discount'])
    w.writeheader()
    for product in productlist:
         w.writerow(product)

    
