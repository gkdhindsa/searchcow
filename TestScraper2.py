import requests
import bs4
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json


keyword=input("Enter keyword: ")


def amazonScrape(keyword):
    query=keyword.split(" ")
    query="+".join(query)
    urlamazon="https://www.amazon.in/s?k="+query+"&ref=nb_sb_noss"
    print(urlamazon)
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome('C:\src\chromedriver_win32\chromedriver.exe',options=option) 
    driver.get(urlamazon) 

    time.sleep(5) 
    
    html = driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    Elements=soup.findAll('div',{"class":"s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16"})
    eDict={}
    i=0
    for Element in Elements:
        try:
            elemcontainer=Element.find('div',{'class':'sg-row'}).findNext('div',{'class':'sg-row'})
            title=elemcontainer.find('h2').text.replace('\n','')
            imgurl=elemcontainer.find('img')['src']
            pricetxt=elemcontainer.find('span',{'class':'a-offscreen'}).text
            price=pricetxt[1:]
            price=int(price.replace(',',''))
            tmp={'title':title,
            'price':price,
            'imageURL':imgurl}
            eDict[str(i)]=tmp
            i+=1
        except:
            continue
    driver.quit()
    return json.dumps(eDict)

def flipkartScrape(keyword):
    query=keyword.split(" ")
    query='%20'.join(query)
    urlflipkart="https://www.flipkart.com/search?q="+query+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    print(urlflipkart)
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome('C:\src\chromedriver_win32\chromedriver.exe',options=option) 
    driver.get(urlflipkart) 

    time.sleep(5) 
    
    html = driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    Elements=soup.findAll('div',{"class":"_1AtVbE col-12-12"})
    eDict={}
    i=0
    for Element in Elements:
        try:
            elemcontainer=Element.find('a',{'class':'_1fQZEK'})
            title=elemcontainer.find('div',{'class':'_4rR01T'}).text
            imgurl=elemcontainer.find('img')['src']
            pricetxt=elemcontainer.find('div',{'class':'_30jeq3 _1_WHN1'}).text
            price=pricetxt[1:]
            price=int(price.replace(',',''))
            tmp={'title':title,
            'price':price,
            'imageURL':imgurl}
            eDict[str(i)]=tmp
            i+=1
        except:
            continue
    driver.quit()
    return json.dumps(eDict)

def tataCliqScrape(keyword):
    query=keyword.split(" ")
    query='%20'.join(query)
    urlCliq="https://www.tatacliq.com/search/?searchCategory=all&text="+query
    print(urlCliq)
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome('C:\src\chromedriver_win32\chromedriver.exe',options=option) 
    driver.get(urlCliq) 

    time.sleep(5) 
    
    html = driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    Elements=soup.findAll('div',{"class":"Grid__element"})
    eDict={}
    i=0
    for Element in Elements:
        try:
            elemcontainer=Element.find('div',{'class':'ProductModule__base'})
            title=elemcontainer.find('div',{'class':'ProductDescription__content'}).find('h2').text
            imgurl=elemcontainer.find('img')['src']
            pricetxt=elemcontainer.find('div',{'class':'ProductDescription__content'}).find('h3').text
            price=pricetxt[1:]
            price=int(price.replace(',',''))
            tmp={'title':title,
            'price':price,
            'imageURL':imgurl}
            eDict[str(i)]=tmp
            i+=1
        except:
            continue
    driver.quit()
    return json.dumps(eDict)

    