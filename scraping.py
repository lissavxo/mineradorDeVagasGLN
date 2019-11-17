'''
AUTORES:  Lissa Ximenes, Guilherme Ferreira
DATA: 05/11/2019

'''
from bs4 import BeautifulSoup
import requests
import funcoes
import json
from datetime import date


def get_vagas(lim = 2):


    
    titles = []
    links = []
    codes = []
    dates = []
    companies = []
    locais = []
    tags = []
    salaries = []
    regimes = []
    periodos = []
    descricoes = []


    
    page=1
    while(True):
        
        print("Page: %s" %page)
        # atribuindo valores as variaveis atributos
        soup = funcoes.get_soup('https://empregos.profissionaisti.com.br/vagas/distrito-federal/'+'?p='+str(page))
        titles.extend(funcoes.get_titles(funcoes.soup_box(soup)))
        links.extend(funcoes.get_links(soup))
        codes.extend(funcoes.get_codes(funcoes.soup_box(soup)))
        dates.extend(funcoes.get_dates(soup))
        companies.extend(funcoes.get_companies(funcoes.soup_details(soup)))
        locais.extend(funcoes.get_locals(funcoes.soup_details(soup)))
        tags.extend(funcoes.get_tags(funcoes.soup_details(soup)))
        salaries.extend(funcoes.get_salario(soup, links))
        regimes.extend(funcoes.get_regime(funcoes.soup_label(soup)))
        periodos.extend(funcoes.get_periodo(funcoes.soup_label(soup)))
        descricoes.extend(funcoes.get_descricao(soup, links))
        # verifica data e controla o loop para a alteracao de paginas buscadas
        if(date_verification(dates[-1],lim)==False):
            print("Breaking in page: %s" %str(page+1))
            print(dates[-1]) 
            break
        page+=1


    # faz uma lista de dicionarios de vagas
    vagas = []
    

    for i in range(len(titles) - 1):
        if date_verification(dates[i],lim):
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
                    "Período": periodos[i],
                    "Descrição": descricoes[i]
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
    mes_vaga = data_vaga[1]
    mes_atual = date.today().month
   
    
    if int(mes_vaga) >= mes_atual - lim:
        return True
    else:
        return False
