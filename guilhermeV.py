from bs4 import BeautifulSoup
import requests

def mainGui():
    url = 'https://empregos.profissionaisti.com.br/vagas/distrito-federal/'
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')
    lista_atribuicoes_periodos = []
    for item in soup.find_all('span', class_="label"): 
	    texto = item.get_text().strip()
	    lista_atribuicoes_periodos.append(texto)
    print(lista_atribuicoes_periodos)