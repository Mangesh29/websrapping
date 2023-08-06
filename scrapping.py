from flask import Flask, render_template, request,jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging
logging.basicConfig(filename="scrapper.log" , level=logging.INFO)
import math

app = Flask(name)

@app.route("/", methods = ['GET'])
def homepage():
    return render_template("index.html")

@app.route("/review", methods = ['POST'])
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","")
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = uReq(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            del bigboxes[0:3]
            del bigboxes[-3]
            print(len(bigboxes))

            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodRes = requests.get(productLink)
            prodRes.encoding='utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})
            page_num =findNumberOfPages(prod_html)
            child= prod_html.find('div', {'class': "_3UAT2v _16PBlm"})
            a_tag = child.find_parent('a')
            href_value = a_tag.get('href')
            pages_link = "https://www.flipkart.com" +href_value +"&page="
            print(href_value)
            rev_text=[]
            # page_num=input("Enter the pages")
            for i in range(1,int(page_num)+1):
            # for i in range(1,11):
                flipcart_url_i = pages_link+f"{i}"
                print(flipcart_url_i)
                req=requests.get(flipcart_url_i)
                content=bs(req.content,'html.parser')
                review=content.find_all('p',{"class":'_2sc7ZR _2V5EHH'})
                for rt in review:
                    rev_text.append(rt.text)

            for i in rev_text:
                print(i)
            reviews = [{"Product": "searchString", "Name": "name", "Rating": "rating", "CommentHead": "commentHead",
                          "Comment": "custComment"}]
            


            return render_template('results.html', reviews=reviews)
            # return render_template('result.html', reviews=reviews[0:(len(reviews)-1)])
        except Exception as e:
            logging.info(e)
            print(e)
            return 'something is wrong'
    else:
        return render_template("index.html")


def findNumberOfPages(html):
    total_review_text = (html.find('div', {'class': "_3UAT2v _16PBlm"})).text
    print(total_review_text)
    total_review=int(total_review_text.split(" ")[1])
    print(total_review)
    reveiw_per_page = 10
    total_pages= math.ceil(total_review/reveiw_per_page)
    print(total_pages)
    return total_pages


if name=="main":
    # app.run(debug=True)
    app.run(host="0.0.0.0")
# flipcart_url = "https://www.flipkart.com/search?q=" + "iphone12pro"
# urlclient = urlopen(flipcart_url)
# flipcart_page = urlclient.read()
# flipcart_html = bs(flipcart_page, 'html.parser')
# bigboxes = flipcart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
# print(len(bigboxes))
# del bigboxes[0:2]
# del bigboxes[-3:]
# print(len(bigboxes))
# box = bigboxes[len(bigboxes)-1]
# product_link = "https://flipkart.com" + bigboxes[1].div.div.div.a['href']
# print(product_link)
# product_req = requests.get(product_link)
# product_html = bs(product_req.text, 'html.parser')
# product_boxes = product_html.findAll("div", {"class": "_16PBlm"})
# print(len(product_boxes))