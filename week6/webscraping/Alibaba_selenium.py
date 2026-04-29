from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import csv
import time
url='https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.132.2ce267afSeLPmg&SearchText=Auto+Accessories&indexArea=product_en&search_cource_scene=pc_home_product_category&has4Tab=true&tab=all'
 
cservice=webdriver.ChromeService(executable_path="C:\\Users\\TTS LAPTOPS\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=cservice)
driver.get(url)

time.sleep(5)
productlist=[]
products=driver.find_elements(By.XPATH,'//div[contains(@class,"fy26-product-card-wrapper")]')
for item in products:
    product={}
    title=item.find_element(By.XPATH,'.//div[contains(@class , "searchx-title-area title-area-layout fix-height")]').text
    
    price=item.find_element(By.XPATH,'.//div[contains(@class,"searchx-product-price price--two-line")]').text
   

    product['title']=title
   
    product['price']=price
    

    productlist.append(product)

filename="week6/Alibaba_selenium.csv"
with open(filename,'w',newline="") as f:
    w=csv.DictWriter(f,['title','price'])
    w.writeheader()
    for product in productlist:
        w.writerow(product)
driver.close()