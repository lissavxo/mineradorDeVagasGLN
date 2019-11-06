from bs4 import BeautifulSoup
import requests
def mainLissa():
  url = 'https://empregos.profissionaisti.com.br/vagas/distrito-federal/'
  site = requests.get(url)
  soup = BeautifulSoup(site.content, 'html.parser')
  nomeVagas = []
  linkVagas = []
  codigoVagas = []
  empresaVagas = []
  localVagas = []
  dataVagas = []
  print("---------")

  for box in soup.find_all('div', class_="job-list-content"):
    soupBox = BeautifulSoup(str(box), 'html.parser') #objeto soup para o box da vaga
    soupDetails = BeautifulSoup(str(soupBox.find('div',class_="job-icons clearfix")), 'html.parser') #objeto soup para a div dos detalhes da vaga
  
   # definido atributos da vaga

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
        
        
    
 
  # imprimindo vaga

    print("Titulo da vaga: {} ".format(titulo))
    nomeVagas.append(titulo)
    print("Link para vaga: {}".format(link))
    linkVagas.append(link)
    print("codigo: {}".format(codigo))
    codigoVagas.append(codigo)
    print("empresa: {}".format(empresa))
    empresaVagas.append(empresa)
    print("local: {}".format(local))
    localVagas.append(local)
    print("data: {}".format(data))
    dataVagas.append(data)
    print("   ")
    print("----------------")