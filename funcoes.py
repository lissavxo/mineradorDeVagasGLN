from bs4 import BeautifulSoup
import requests

def get_soup(url):
  
  site = requests.get(url)
  soup = BeautifulSoup(site.content, 'html.parser')
  return soup

#funçao para retornar lista de soups box da vaga
def box_soup(soup):
  box_list = []
  for box in soup.find('ul', class_="job-list"):
    box_list.append(box)
  return box_list
#funcao retorna lista de titulos
def get_titles(box_soup):
  titles = []
  for box in box_soup:
    text = box.h4.get_text()
    titles.append(text) 
  return titles 

#funcao retorna lista de links de vaga
def get_links(soup):
  links = []
  links_soup = BeautifulSoup(str( soup.find_all('h4')), 'html.parser' )
  for link in links_soup.select('a'):
    links.append(link.get('href'))
  return links

#funcao retorna lista de codigos da vaga
def get_codes(box_soup):
  codes = []
  for box in box_soup:
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
def data_vagas(soup):
    data_vagas = []
    for item in soup.find_all('a', class_="nolink"):
        data = item.get_text().strip()
        data_vagas.append(data)
    return data_vagas



#Lista contendo empresa, local e area da vaga
def empresa_local_area(soup): #
    lista = []
    for item in soup.find_all('div', class_="job-icons clearfix"):
        for atributo in item.find_all('a'):
            x = atributo.get('title')
            if x != None:
                lista.append(x)
    return lista


#Retorna empresa da vaga
def empresa(empresa_local_area):
    empresa_vaga = []
    controle_tamanho = len(empresa_local_area)
    for indice in range(0, controle_tamanho, 3):
        empresa_vaga.append(empresa_local_area[indice])
    return empresa_vaga


#Retorna local da vaga
def local(empresa_local_area):
    local_vaga = []
    controle_tamanho = len(empresa_local_area)
    for indice in range(1, controle_tamanho, 3):
        local_vaga.append(empresa_local_area[indice])
    return local_vaga


#Retorna área da vaga
def area(empresa_local_area):
    area_vaga = []
    controle_tamanho = len(empresa_local_area)
    for indice in range(2, controle_tamanho, 3):
        area_vaga.append(empresa_local_area[indice])
    return area_vaga
