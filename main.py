from bs4 import BeautifulSoup
import requests
import scraping

vagas = scraping.get_vagas()


for item in vagas:
  print(item)





