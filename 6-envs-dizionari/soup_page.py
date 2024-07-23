import requests 
from bs4 import BeautifulSoup as bs


r = requests.get("https://www.wikipedia.com")
soup = bs(r.content) 
print(soup.prettify())

