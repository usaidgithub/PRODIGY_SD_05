import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response = requests.get(url)

if response.status_code == 200:
    name = []
    price = []
    reviews = []
    ratings=[]
    soup = BeautifulSoup(response.content, 'lxml')
    
    product_name = soup.find_all('a', class_='title')
    for item in product_name:
        name.append(item.text)
    print(name)
    product_prices = soup.find_all('h4', class_='price float-end card-title pull-right')
    for i in product_prices:
        price.append(i.text)
    print(price)
    product_reviews=soup.find_all('p',class_='review-count float-end')
    for j in product_reviews:
        reviews.append(j.text)
    print(reviews)
    product_ratings=soup.find_all('p', {'data-rating': True})
    for k in product_ratings:
        stars=k.find_all('span',class_='ws-icon ws-icon-star')
        ratings.append(len(stars))
    print(ratings)
    df=pd.DataFrame({
    'Product name': name,
    'Product price':price,
    'Product reviews':reviews,
    'Product ratings':ratings
    })
    df.to_csv('product_csv',index=False)
    print("Data saved successfully")
else:
    print("An error occurred while saving the data")