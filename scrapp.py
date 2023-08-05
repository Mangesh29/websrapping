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
               
bigbox=flipkart_html.findAll("div",{"class":"_1AtVbE col-12-12"})

print(len(bigbox))

del bigbox[0:3]

del bigbox[-3:]

# for i in bigbox:
#     print("https://www.flipkart.com"+i.div.div.div.a['href'])

product_link="https://www.flipkart.com"+bigbox[0].div.div.div.a['href'] 

print(product_link)

product_req=requests.get(product_link)
print(product_req)

print(bs(product_req.text,'html.parser'))
product_html=bs(product_req.text,'html.parser')


product_boxs=product_html.findAll("div",{"class":"_16PBlm"})

print(len(product_boxs))
del product_boxs[-1]

print(product_boxs[2].div.div.find('p',{"class":"_2sc7ZR _2V5EHH"}).text)

allReviews=[]
for i in product_boxs:
    # print("Reviewer name :")
    # print(i.div.div.find('p',{"class":"_2sc7ZR"}).text)
    # print("Reviewer Rating :")
    # print(i.div.div.div.div.text)
    # print("Reviewer Comment :")
    # print(i.div.div.div.p.text)
    # print("Reviewer Description :")
    # print(i.div.div.find_all('div',{"class":""}))
    # print("================")

    review={

        "name":i.div.div.find('p',{"class":"_2sc7ZR _2V5EHH"}).text,
        "rating":i.div.div.find('div',{"class":"_3LWZlK _1BLPMq"}).text,
        "description":i.div.div.find('div',{"class":""}).text


        }
    allReviews.append(review)
print(allReviews)

 

 