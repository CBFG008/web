import requests
from bs4 import BeautifulSoup
import os

url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parsel")

os.makedirs("books_images" , exist_ok=True)
books = soup.find_all("article", class_ = "product_pod")

for index , books in enumerate(books,starts=1) :
   img_tag = books.find("ing")
   img_src =img_tag["src"]

   img_url = url + img_src.replace('../../', '')
   img= requests.get(img_url).content

   with open(f'book_images/book c_(index+1).jpg', "wb") as f:
     f.write(img)

   print(f"download book c_[index +1].jpg") 