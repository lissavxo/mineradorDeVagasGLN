'''
AUTORES:  Lissa Ximenes, Guilherme Ferreira
DATA: 05/11/2019

'''

from bs4 import BeautifulSoup
import requests
import funcoes


def getVagas():

  soup = funcoes.get_soup('https://empregos.profissionaisti.com.br/vagas/distrito-federal/') 

  titles = funcoes.get_titles(funcoes.box_soup(soup))
  links = funcoes.get_links(soup)
  codes = funcoes.get_codes(funcoes.box_soup(soup))
  company = funcoes.empresa(funcoes.empresa_local_area(soup))

  vagas = [titles,links,codes,company]

  return vagas

   

  
