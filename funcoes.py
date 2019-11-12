# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


def get_soup(url):

    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')
    return soup


#funçao para retornar lista de soups box da vaga
def soup_box(soup):
    box_list = []
    for box in soup.find('ul', class_="job-list"):
        box_list.append(box)
    return box_list


#Lista contendo empresa, local e tag da vaga
def soup_details(soup):  #
    lista = []
    for item in soup.find_all('div', class_="job-icons clearfix"):
        for atributo in item.find_all('a'):
            x = atributo.get('title')
            if x != None:
                lista.append(x)
    return lista


#funcao retorna lista de titulos
def get_titles(soup_box):
    titles = []
    for box in soup_box:
        text = box.h4.get_text()
        titles.append(text)
    return titles


#funcao retorna lista de links de vaga
def get_links(soup):
    links = []
    links_soup = BeautifulSoup(str(soup.find_all('h4')), 'html.parser')
    for link in links_soup.select('a'):
        links.append(link.get('href'))
    return links


#funcao retorna lista de codigos da vaga
def get_codes(soup_box):
    codes = []
    for box in soup_box:
        code = list(box.get('id'))
        del code[0:5]
        code = ''.join(code)
        codes.append(int(code))

    return codes


#Retorna o regime de trabalho e o período
def get_regime_periodo(soup):
    conjunto_de_atribuicoes_vaga = []
    for item in soup.find_all('span', class_="label"):
        texto = item.get_text().strip()
        conjunto_de_atribuicoes_vaga.append(texto)
    return conjunto_de_atribuicoes_vaga


#Retorna a data da publicação
def get_dates(soup):
    dates = []
    for item in soup.find_all('a', class_="nolink"):
        data = item.get_text().strip()
        dates.append(data)
    return dates


#Retorna empresa da vaga
def get_companies(soup_details):
    companies = []
    controle_tamanho = len(soup_details)
    for indice in range(0, controle_tamanho, 3):
        item = list(soup_details[indice])
        del item[0:9]
        item = ''.join(item)
        companies.append(item)
    return companies


#Retorna local da vaga
def get_locals(soup_details):
    locais = []
    controle_tamanho = len(soup_details)
    for indice in range(1, controle_tamanho, 3):
        local = list(soup_details[indice])
        del local[0:9]
        local = ''.join(local)
        locais.append(local)
    return locais


#Retorna tag da vaga
def get_tags(soup_details):
    tags = []
    controle_tamanho = len(soup_details)
    for indice in range(2, controle_tamanho, 3):
        tag = list(soup_details[indice])
        del tag[0:11]
        tag = ''.join(tag)
        tags.append(tag)
    return tags
