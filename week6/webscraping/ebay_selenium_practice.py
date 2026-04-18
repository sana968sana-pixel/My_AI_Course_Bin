from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import csv

url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"

cService = webdriver.ChromeService(executable_path='C:\\Users\\TTS LAPTOPS\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe') 
driver = webdriver.Chrome(service=cService)

driver.get(url)


productlist=[]
products=driver.find_elements(By.XPATH,"//li[contains(@class,'brwrvr__item-card')]")
for item in products:
    product={}
    title=item.find_element(By.XPATH,".//h3[contains(@class,'bsig__title__text')]").text
    price=item.find_element(By.XPATH,".//span[contains(@class,'bsig__price--displayprice')]").text
    link=item.find_element(By.XPATH,".//a").get_attribute("href")

    product["title"] = title
    product["price"] = price
    product["link"] = link

    productlist.append(product)
filename='week6/ebay_selenium_scrapping.csv'
with open(filename,'w',newline="", encoding='utf-8')as f:
    w=csv.DictWriter(f,['title','price','link'])
    w.writeheader()
    for product in productlist:
        w.writerow(product)
driver.close()