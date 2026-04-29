from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url='https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel'

cService=webdriver.ChromeService(executable_path='C:\\Users\\TTS LAPTOPS\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(service=cService)

driver.get(url)
productlist=[]
products=driver.find_elements(By.XPATH,"//div[contains(@class,'Bm3ON')]")
for item in products:
    product={}
    title=item.find_element(By.XPATH,".//div[contains(@class,'RfADt')]").text
    price=item.find_element(By.XPATH,".//span[contains(@class,'ooOxS')]").text
    link=item.find_element(By.XPATH,'.//a').get_attribute("href")
    discout=item.find_element(By.XPATH,"//span[contains(@class,'IcOsH')]").text

    product["title"]=title
    product["price"]=price
    product['link']=link
    product['discount']=discout
    productlist.append(product)

filename="week6/daraz_selenium.csv"
with open(filename,'w',newline="",encoding="utf_8") as f:
    w=csv.DictWriter(f,['title','price','link','discount'])
    w.writeheader()
    for product in productlist:
        w.writerow(product)
driver.close()