from bs4 import BeautifulSoup
import requests


def get_soup():
    url = 'https://empregos.profissionaisti.com.br/vagas/distrito-federal/'
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')
    return soup


soup = get_soup()


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
def emaranhado(soup): #
    lista = []
    for item in soup.find_all('div', class_="job-icons clearfix"):
        for atributo in item.find_all('a'):
            x = atributo.get('title')
            if x != None:
                lista.append(x)
    return lista


x = []
x = emaranhado(soup)
y = len(x)


#Retorna empresa da vaga
def empresa():
    empresa_vaga = []
    for k in range(0, y, 3):
        empresa_vaga.append(x[k])
    return empresa_vaga


#Retorna local da vaga
def local():
    local_vaga = []
    for item in range(1, y, 3):
        local_vaga.append(x[item])
    return local_vaga


#Retorna área da vaga
def area():
    area_vaga = []
    for item in range(2, y, 3):
        area_vaga.append(x[item])
    return area_vaga
