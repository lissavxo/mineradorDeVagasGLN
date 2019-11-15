'''
AUTORES:  Lissa Ximenes, Guilherme Ferreira
DATA: 05/11/2019

'''
from bs4 import BeautifulSoup
import requests
import funcoes
import json
from datetime import date


def get_vagas():

    soup = funcoes.get_soup(
        'https://empregos.profissionaisti.com.br/vagas/distrito-federal/')

    # atribuindo valores as variaveis atributos
    titles = funcoes.get_titles(funcoes.soup_box(soup))
    links = funcoes.get_links(soup)
    codes = funcoes.get_codes(funcoes.soup_box(soup))
    dates = funcoes.get_dates(soup)
    companies = funcoes.get_companies(funcoes.soup_details(soup))
    locais = funcoes.get_locals(funcoes.soup_details(soup))
    tags = funcoes.get_tags(funcoes.soup_details(soup))
    salaries = funcoes.get_salario(soup, links)
    regimes = funcoes.get_regime(funcoes.soup_label(soup))
    periodos = funcoes.get_periodo(funcoes.soup_label(soup))

    # faz uma lista de dicionarios de vagas
    vagas = []

    for i in range(len(titles) - 1):
        if date_verification(dates[i]):
            vagas_dict = {
                codes[i]: {
                    "Titulo": titles[i],
                    "Link": links[i],
                    "Data": dates[i],
                    "Empresa": companies[i],
                    "Local": locais[i],
                    "Tag": tags[i],
                    "Salary": salaries[i],
                    "Regime": regimes[i],
                    "Periodo": periodos[i]
                }
            }
            vagas.append(vagas_dict)
    return vagas


def vagas_to_dict(vagas_dict):
    with open('vagas.json', 'w') as json_file:
        json.dump(vagas_dict, json_file, ensure_ascii=False)


def date_verification(data_vaga, lim=2):
    # limite pode ser 2
    # formatando  o dado
    data_vaga = data_vaga.split('/')
    # data_vaga = '-'.join(data_vaga)

    data_limite = str(date.today()).split('-')

    if int(data_vaga[2]) >= int(data_limite[1]) - lim:
        return True
    else:
        return True
