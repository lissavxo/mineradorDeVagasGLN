'''
AUTORES:  Lissa Ximenes, Guilherme Ferreira
DATA: 05/11/2019

'''

from bs4 import BeautifulSoup
import requests
import funcoes


def get_vagas():

  
  soup = funcoes.get_soup(
    'https://empregos.profissionaisti.com.br/vagas/distrito-federal/')


  #atribuindo valores as variaveis atributos

  titles = funcoes.get_titles(funcoes.soup_box(soup))
  links = funcoes.get_links(soup)
  codes = funcoes.get_codes(funcoes.soup_box(soup))
  companies = funcoes.get_companies(funcoes.soup_details(soup))
  locais = funcoes.get_locals(funcoes.soup_details(soup))
  tags = funcoes.get_tags(funcoes.soup_details(soup))


  vagas = [titles,links,codes,companies,locais,tags]
  #impressao da vaga

  # for i in range(len(titles) - 1):

  #     print(" ")
  #     print("---------------------------------------------------")
  #     print("Title: {}".format(titles[i]))
  #     print("link: {}".format(links[i]))
  #     print("code: {}".format(codes[i]))
  #     print("company: {}".format(companies[i]))
  #     print("local: {}".format(locais[i]))
  #     print("tag: {}".format(tags[i]))
  #     print("---------------------------------------------------")
  #     print(" ")
      
  return vagas

   

  
