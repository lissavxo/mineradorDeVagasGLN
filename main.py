from bs4 import BeautifulSoup
import requests
import funcoes

soup = funcoes.get_soup(
    'https://empregos.profissionaisti.com.br/vagas/distrito-federal/')

titles = funcoes.get_titles(funcoes.box_soup(soup))
links = funcoes.get_links(soup)
codes = funcoes.get_codes(funcoes.box_soup(soup))
company = funcoes.empresa(funcoes.empresa_local_area(soup))
place = funcoes.local(funcoes.empresa_local_area(soup))
tag = funcoes.tag(funcoes.empresa_local_area(soup))

for i in range(len(titles) - 1):

    print(" ")
    print("---------------------------------------------------")
    print("Titulo: {}".format(titles[i]))
    print("link: {}".format(links[i]))
    print("code: {}".format(codes[i]))
    print("company: {}".format(company[i]))
    print("place: {}".format(place[i]))
    print("tag: {}".format(tag[i]))
    print("---------------------------------------------------")
    print(" ")
