import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books= soup.find_all("article", class_="product_pod")

titles = []
prices = []

for books in books:
    title = books.h3.a["title"]
    price = books.find("p"  , class_="price color").text
    titles.append(titles)
    price.append(price)



df=pd.Dataframe({"title":titles,  "price":prices})

print(df)

df.to_csv("bookss.csv", index= False )
print("saved to bookss.csv")