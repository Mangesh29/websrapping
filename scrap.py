import requests
from bs4 import BeautifulSoup as bs 
from urllib.request import urlopen
import logging

flipcart_url = "https://www.flipkart.com/search?q=" + "iphone12pro"

urlclint = urlopen(flipcart_url)

flipcart_url = urlclint.read()

flipcart_html= bs(flipcart_url,'html.parser')

bigbox = flipcart_html.findAll("div",{"class":"_1AtVbE col-12-12"})
print(len(bigbox))
del bigbox[0:2]
del bigbox[-3:]

for i in range(len(bigbox)):
    print(bigbox[i].div.div.div.a['href'])


print(len(bigbox))

product_link="https://www.flipkart.com"+bigbox[3].div.div.div.a['href'] 

product_req=requests.get(product_link)
print(product_req)

print(bs(product_req.text,'html.parser'))