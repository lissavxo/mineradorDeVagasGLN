from bs4 import BeautifulSoup
import requests



# funçao para retornar uma soup de toda a pagina a partir da url
def get_soup(url):

    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')
    return soup


# funçao para retornar lista de soups box da vaga
def soup_box(soup):
    box_list = []
    for box in soup.find('ul', class_="job-list"):
        box_list.append(box)
    return box_list


# Lista contendo empresa, local e tag da vaga
def soup_details(soup):  #
    lista = []
    for item in soup.find_all('div', class_="job-icons clearfix"):
        for atributo in item.find_all('a'):
            x = atributo.get('title')
            if x != None:
                lista.append(x)
    return lista


# Retorna o regime de trabalho e o período
def soup_label(soup):
    conjunto_de_atribuicoes_vaga = []
    for item in soup.find_all('span', class_="label"):
        texto = item.get_text().strip()
        conjunto_de_atribuicoes_vaga.append(texto)
    return conjunto_de_atribuicoes_vaga


# funcao retorna lista de titulos
def get_titles(soup_box):
    titles = []
    for box in soup_box:
        text = box.h4.get_text()
        titles.append(text)
    return titles


# funcao retorna lista de links de vaga
def get_links(soup):
    links = []
    links_soup = BeautifulSoup(str(soup.find_all('h4')), 'html.parser')
    for link in links_soup.select('a'):
        links.append(link.get('href'))
    return links


# funcao retorna lista de codigos da vaga
def get_codes(soup_box):
    codes = []
    for box in soup_box:
        code = list(box.get('id'))
        del code[0:5]
        code = ''.join(code)
        codes.append(int(code))

    return codes


# Retorna o regime de trabalho
def get_regime(soup_label):
    regimes = []
    controle_tamanho = len(soup_label)
    for indice in range(0, controle_tamanho, 2):
        regime = soup_label[indice]
        regimes.append(regime)
    return regimes


# Retorna o período de trabalho
def get_periodo(soup_label):
    periodos = []
    controle_tamanho = len(soup_label)
    for indice in range(1, controle_tamanho, 2):
        periodo = soup_label[indice]
        periodos.append(periodo)
    return periodos


# Retorna a data da publicação
def get_dates(soup):
    dates = []
    for item in soup.find_all('a', class_="nolink"):
        data = item.get_text().strip()
        dates.append(data)
    return dates


# Retorna empresa da vaga
def get_companies(soup_details):
    companies = []
    controle_tamanho = len(soup_details)
    for indice in range(0, controle_tamanho, 3):
        item = list(soup_details[indice])
        del item[0:9]
        item = ''.join(item)
        companies.append(item)
    return companies


# Retorna local da vaga
def get_locals(soup_details):
    locais = []
    controle_tamanho = len(soup_details)
    for indice in range(1, controle_tamanho, 3):
        local = list(soup_details[indice])
        del local[0:9]
        local = ''.join(local)
        locais.append(local)
    return locais


# Retorna tag da vaga
def get_tags(soup_details):
    tags = []
    controle_tamanho = len(soup_details)
    for indice in range(2, controle_tamanho, 3):
        tag = list(soup_details[indice])
        del tag[0:11]
        tag = ''.join(tag)
        tags.append(tag)
    return tags


# Retorna com uma lista dos salários
def get_salario(soup, links):
    lista_salarios = []
    for url in links:
        
        soup_internal_dialog = get_soup(url)
        lista_de_p = []
        for item in soup_internal_dialog.find_all('p'):
            conteudo = item.get_text().strip()
            lista_de_p.append(conteudo)
            salarios = [s for s in lista_de_p if "Salário:" in s]
            if len(salarios) == 0:
                salarios = ['Não informado!']
        lista_salarios.append(salarios[0])
    return lista_salarios


# Retorna com uma lista com a descrição das vagas
# a descricao esta organizada em topicos, cada topico e um intem de uma lista por vaga
def get_descricao(soup, links):
    lista_descricoes = []
    for url in links:
        lista_de_p = []
        
        soup_internal_dialog = get_soup(url)
        for item in soup_internal_dialog.find_all('div', class_="job-content"):
            for item2 in item.find_all('p', class_=""):
                p = item2.get_text()
                p = p.replace(u'\xa0', u'')
                lista_de_p.append(p)
            lista_descricoes.append(str(lista_de_p))
    return lista_descricoes
