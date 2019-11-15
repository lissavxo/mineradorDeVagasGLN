from bs4 import BeautifulSoup
import requests
import scraping

vagas = scraping.get_vagas()

scraping.vagas_to_dict(vagas)
