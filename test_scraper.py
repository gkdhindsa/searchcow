import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


keyword=input("Enter keyword: ")
query=keyword+" amazon"
l1=query.split(" ")
query="+".join(l1)

urlamazon="https://www.google.com/search?q="+query+"&rlz=1C1CHBD_enIN864IN864&biw=1536&bih=403&tbm=shop&sxsrf=ALeKk03PXXwoGAWTZMkJ1lXHLxkY8DXzqg%3A1617977463008&ei=d2BwYOkHiLmtAcKugtgN&oq=iphone+11&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgQIIxAnMgQIIxAnMggIABCxAxCDATIICAAQsQMQgwEyCAgAELEDEIMBMgIIADIICAAQsQMQgwEyAggAMggIABCxAxCDATICCAA6BAgAEA06CAgAEAgQDRAeOgoIABANEAUQHhAYOgoIABAIEA0QHhAYUJgzWJgzYKI1aABwAHgAgAHOAogB7wOSAQcwLjEuMC4xmAEAoAEBwAEB&sclient=products-cc&ved=0ahUKEwipn7_fq_HvAhWIXCsKHUKXANsQ4dUDCAs&uact=5"
print(urlamazon)
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('C:\src\chromedriver_win32\chromedriver.exe',options=option) 
driver.get(urlamazon) 

time.sleep(5) 
  
html = driver.page_source
soup=BeautifulSoup(html,'html.parser')
AdElements=soup.findAll('div',{"class":"KZmu8e"})
i=0
for element in AdElements:
    a=element.contents[0]
    nav=a.contents[2].contents[0]
    seller=nav.contents[2].text
    if(seller=="Amazon.in"):
        prodname=nav.contents[0].text
        price=nav.contents[1].contents[0].text
        i+=1
        if(i<=10):
            print(prodname+'\n'+price+'\n')        
driver.quit()


