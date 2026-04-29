from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv



url="https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2"

cservice= webdriver.ChromeService(executable_path='C:\\Users\\TTS LAPTOPS\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(service=cservice)

driver.get(url)

productlist=[]
products=driver.find_elements(By.XPATH,'//li[contains(@class,"a-carousel-card ucw-widget-carousel-element")]')
for item in products:
    product={}
    
    title=item.find_element(By.XPATH,'.//div[contains(@class,"ucw-widget-product-card-title")]').text
    rating=item.find_element(By.XPATH,'.//div[contains(@class,"ucw-widget-product-card-review")]').text
    price=item.find_element(By.XPATH,'.//div[contains(@class,"ucw-widget-product-card-price")]').text
    shiping=item.find_element(By.XPATH,'.//div[contains(@class,"ucw-widget-product-card-delivery")]').text

    product['title']=title
    product['rating']=rating
    product['price']=price
    product['shiping']=shiping

    productlist.append(product)

filename="week6/webscraping/amazon_selenium.csv"
with open(filename,'w',newline="") as f:
    w=csv.DictWriter(f,['title','rating','price','shiping'])
    w.writeheader()
    for product in productlist:
        w.writerow(product)
driver.close()