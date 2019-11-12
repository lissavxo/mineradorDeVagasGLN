# -*- coding: utf-8 -*-
'''
AUTORES:  Lissa Ximenes, Guilherme Ferreira
DATA: 05/11/2019

'''
from bs4 import BeautifulSoup
import requests
import funcoes
import json


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

    vagas = []
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
    for i in range(len(titles) - 1):
        vagas_dict = {
            codes[i]: {
                "Titulo": titles[i],
                "Link": links[i],
                "Company": companies[i],
                "Local": locais[i],
                "Tag": tags[i]
            }
        }
        vagas.append(vagas_dict)

    return vagas


def vagas_to_dict(vagas_dict):
  with open('person.txt', 'w') as json_file:
    json.dump(vagas_dict, json_file,ensure_ascii=False)

  
    
