from bs4 import BeautifulSoup
import requests
import file_handler_functions as files
# ------------------------------------------------------------------------------------------------------------
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
# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------

# Retorna o regime de trabalho e o período
def soup_label(soup,lim_vagas= 0):
    internal_value = lim_vagas
    internal_count = 0
    internal_bol = False
    if internal_value != 0:
        internal_bol = True
    conjunto_de_atribuicoes_vaga = []
    for item in soup.find_all('span', class_="label"):
        if internal_bol:
            if internal_count <= lim_vagas:
                texto = item.get_text().strip()
                conjunto_de_atribuicoes_vaga.append(texto)
            else:
                return conjunto_de_atribuicoes_vaga
                
            internal_count+=1
        else:
            texto = item.get_text().strip()
            conjunto_de_atribuicoes_vaga.append(texto)
        
        

    return conjunto_de_atribuicoes_vaga


# funcao retorna lista de titulos
def get_titles(soup_box,lim_vagas= 0):
    internal_value = lim_vagas
    internal_count = 0
    internal_bol = False
    if internal_value != 0:
        internal_bol = True
    
    titles = []
    for box in soup_box:
        if internal_bol:
            if internal_count < lim_vagas:
                text = box.h4.get_text()
                titles.append(text)
            else:
                return titles
            internal_count+=1
        else:
            text = box.h4.get_text()
            titles.append(text)

            
    return titles


# funcao retorna lista de links de vaga
def get_links(soup,lim_vagas= 0):
    internal_value = lim_vagas
    internal_count = 0
    internal_bol = False
    if internal_value != 0:
        internal_bol = True
    links = []
    links_soup = BeautifulSoup(str(soup.find_all('h4')), 'html.parser')
    for link in links_soup.select('a'):
        if internal_bol:
            if internal_count < lim_vagas:
                links.append(link.get('href'))
            else:
                return links
            internal_count+=1
        else:
            links.append(link.get('href'))


        
    return links


# funcao retorna lista de codigos da vaga
def get_codes(soup_box,lim_vagas= 0):



    codes = []
    for box in soup_box:
        code = list(box.get('id'))
        del code[0:5]
        code = ''.join(code)
        if files.last_sendend_verification(code) == False:
            return codes , True # keep atention HEERE  
        codes.append(int(code))
    return codes , False



# Retorna o regime de trabalho
def get_regime(soup_label,lim_vagas= 0):
    regimes = []
    controle_tamanho = len(soup_label)
    internal_value = lim_vagas
    internal_count = 0
    internal_bol = False
    if internal_value != 0:
        internal_bol = True


    for indice in range(0, controle_tamanho, 2):

        if internal_bol:
            if internal_count < lim_vagas:
                regime = soup_label[indice]
                regimes.append(regime)
                
            else:
                return regimes
            internal_count+=1
        else:
            regime = soup_label[indice]
            regimes.append(regime)


    return regimes


# Retorna o período de trabalho
def get_periodo(soup_label,lim_vagas= 0):


    periodos = []
    controle_tamanho = len(soup_label)
    internal_value = lim_vagas
    internal_count = 0
    internal_bol = False
    if internal_value != 0:
        internal_bol = True
    
   
    for indice in range(1, controle_tamanho, 2):
        if internal_bol:
            if internal_count < lim_vagas:
                periodo = soup_label[indice]
                periodos.append(periodo)
            else:
                return periodos
            internal_count+=1
        else:
            periodo = soup_label[indice]
            periodos.append(periodo)

        
    return periodos


# Retorna a data da publicação
def get_dates(soup,lim_vagas= 0):
    dates = []

    internal_value = lim_vagas
    internal_count = 0
    internal_bol = False
    if internal_value != 0:
        internal_bol = True
    
   
    for item in soup.find_all('a', class_="nolink"):
   #---------------------------------------
        if internal_bol:
            if internal_count < lim_vagas:
                data = item.get_text().strip()
                dates.append(data)
            else:
                return dates
            internal_count+=1
        else:
            data = item.get_text().strip()
            dates.append(data)

        
    return dates


# Retorna empresa da vaga
def get_companies(soup_details,lim_vagas= 0):
    companies = []
    controle_tamanho = len(soup_details)
    internal_value = lim_vagas
    internal_count = 0
    internal_bol = False
    if internal_value != 0:
        internal_bol = True
    
   
    for indice in range(0, controle_tamanho, 3):
   #---------------------------------------
        if internal_bol:
            if internal_count < lim_vagas:
                item = list(soup_details[indice])
                del item[0:9]
                item = ''.join(item)
                companies.append(item)
            else:
                return companies
            internal_count+=1
        else:
            item = list(soup_details[indice])
            del item[0:9]
            item = ''.join(item)
            companies.append(item)

        
    return companies


# Retorna local da vaga
def get_locals(soup_details,lim_vagas= 0):
    locais = []
    controle_tamanho = len(soup_details)
    internal_value = lim_vagas
    internal_count = 0
    internal_bol = False
    if internal_value != 0:
        internal_bol = True
    
   
    for indice in range(1, controle_tamanho, 3):
   #---------------------------------------
        def my_work():
            local = list(soup_details[indice])
            del local[0:9]
            local = ''.join(local)
            locais.append(local)
            # --------
        if internal_bol:
            if internal_count < lim_vagas:
                my_work()
            else:
                return locais
            internal_count+=1
        else:
            my_work()      

    return locais


# Retorna tag da vaga
def get_tags(soup_details, descricoes):
    tags = []
    # Lista de tags das vagas
    lista_tags = []
    controle_tamanho = len(soup_details)
    
    for indice in range(2, controle_tamanho, 3):
        tag = list(soup_details[indice])
        del tag[0:11]
        tag = ''.join(tag)
        lista_tags.append(tag)

    # Lista de palavras dentro das descriçoẽs
    listona = []
    lista_palavras = []
    for d in descricoes:
        lista_frases_quebradas = d.lower().split()
        lista_palavras.append(lista_frases_quebradas)
    listona.append(lista_palavras)

    # Lista de palavras dentro do tags_banco
    lista_linhas = []
    with open("./files/lista_de_tags.txt", "r") as fd:
        for line in fd:
            line = line.strip()
            lista_linhas.append(line)

    # Compara a lista de palavras da descrição da vaga com a lista do tags_banco
    lista_tags_2 = []
    for lista in listona:
        for frase in lista:
            for palavra in frase:
                if palavra in lista_linhas:
                    lista_tags_2.append(palavra)
            tags.append(lista_tags_2)

    return tags



# Retorna com uma lista dos salários
def get_salario( links):
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
def get_descricao(links, lim_vagas):
    lista_descricoes = []
    for url in links:
        lista_descricao = []
        soup_internal_dialog = get_soup(url)
        for item in soup_internal_dialog.find_all('div', class_="job-content"):
            for item2 in item.find_all('p', class_=""):
                frase = str(item2)
                frase = frase.replace(u'\xa0', u'')
                frase = frase.replace("<br>", " ")
                frase = frase.replace("<br/>", " ")
                frase = frase.replace("</br>", " ")
                frase = BeautifulSoup(frase, "html.parser")
                frase = frase.get_text().strip()
                lista_descricao.append(frase)
            lista_descricoes.append(''.join(lista_descricao))
    return lista_descricoes



