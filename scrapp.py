import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging


flipkart_url= "https://www.flipkart.com/search?q=" +"iphone12pro"

urlclient= urlopen(flipkart_url)
flipkart_page=urlclient.read()

# print(urlclient)

# print(bs(flipkart_page,'html.parser'))
flipkart_html=bs(flipkart_page,'html.parser')
               
bigbox=flipkart_html.find_all("div",{"class":"_1AtVbE col-12-12"})

print(len(bigbox))

del bigbox[0:3]

del bigbox[-3]

for i in bigbox:
    print("https://www.flipkart.com"+i.div.div.div.+a['href'])

 