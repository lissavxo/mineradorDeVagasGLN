'''
AUTORES:  Lissa Ximenes, Guilherme Ferreira
DATA: 05/11/2019

'''

from bs4 import BeautifulSoup
import requests

def getVagas():
  url = 'https://empregos.profissionaisti.com.br/vagas/distrito-federal/'
  site = requests.get(url)
  soup = BeautifulSoup(site.content, 'html.parser')
  nome_vagas = []
  link_vagas = []
  codigo_vagas = []
  empresa_vagas = []
  local_vagas = []
  data_vagas = []
  atribuicoes_vagas = []
  

    
  print("---------")

  for box in soup.find_all('div', class_="job-list-content"):
    
    soupBox = BeautifulSoup(str(box), 'html.parser') #objeto soup para o box da vaga
    soupDetails = BeautifulSoup(str(soupBox.find('div',class_="job-icons clearfix")), 'html.parser') #objeto soup para a div dos detalhes da vaga
  
   # atribuindo atributos da vaga para as variaveis

    titulo = soupBox.h4.string
    link = soupBox.a['href']
    codigo = soupBox.a['href'].split('/')[-2]

    cont = 0
    for atributo in soupDetails.find_all('a'):
      if atributo.get('title') != None:
        if cont == 0:
           empresa = atributo.get('title')
        elif cont == 1:
          local = atributo.get('title')
        cont+=1 
    data = soupDetails.find('a',class_="nolink").get_text() 

    conjunto_de_atribuicoes_vaga = []
    for item in soupBox.find_all('span', class_="label"): 
      texto = item.get_text().strip()
      conjunto_de_atribuicoes_vaga.append(texto)
      
      
        
  # Adicionando variaveis nas listas de cada atributo
    nome_vagas.append(titulo)
    link_vagas.append(link)
    codigo_vagas.append(codigo)
    empresa_vagas.append(empresa)
    local_vagas.append(local)
    data_vagas.append(data)
    atribuicoes_vagas.append(conjunto_de_atribuicoes_vaga)


 
  #imprimindo vaga

    print("Titulo da vaga: {} ".format(titulo))
    print("Link para vaga: {}".format(link))
    print("codigo: {}".format(codigo))
    print("empresa: {}".format(empresa))
    print("local: {}".format(local))
    print("data: {}".format(data))

    print("Atribuicoes da Vaga: ")
    print("----> {}".format(conjunto_de_atribuicoes_vaga[0]))
    print("----> {}".format(conjunto_de_atribuicoes_vaga[1]))


   

  
