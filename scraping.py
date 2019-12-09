'''
AUTORES:  Lissa Ximenes, Guilherme Ferreira
DATA: 05/11/2019

'''
import funcoes
import json
from datetime import date
import file_handler_functions as files

def get_vagas(lim=2):

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

    page = 1
    while (True):

        # variaveis de controle 
        b = 1 
        _b = 1
      

        # variaveis com objetos soup 
        soup = funcoes.get_soup(
            'https://empregos.profissionaisti.com.br/vagas/distrito-federal/' +
            '?p=' + str(page))
        details = funcoes.soup_details(soup)
        box = funcoes.soup_box(soup)
        
        
        print("Page: %s" % page)

        
        _codes = funcoes.get_codes(box)
        codes_bool = _codes[1]
        _codes = _codes[0]
        lim_vagas = 0
        if codes_bool == False:
            lim_vagas = len(_codes)
            _b = 0


        # for c in _codes: 
        #     if str(c) in files.read_all_keys():
        #         if _codes.index(c) == 0:
        #             b = 0
        #         print( 'entrou')
        #         cont +=1
        
        # if cont > 1:
        #     print('again')
        #     lim_vagas = cont
        #     _codes = _codes[:cont]

        titles.extend(funcoes.get_titles( box ,lim_vagas))
        new_link = funcoes.get_links(soup,lim_vagas)
        links.extend(new_link)
        codes.extend(_codes)
        dates.extend(funcoes.get_dates(soup,lim_vagas))
        companies.extend(funcoes.get_companies(details,lim_vagas))
        locais.extend(funcoes.get_locals(details,lim_vagas))
        new_descricoes = funcoes.get_descricao(new_link,lim_vagas)
        descricoes.extend(new_descricoes)
        tags.extend(funcoes.get_tags(details,new_descricoes))
        salaries.extend(funcoes.get_salario(links))
        regimes.extend(funcoes.get_regime(funcoes.soup_label(soup),lim_vagas))
        periodos.extend(funcoes.get_periodo(funcoes.soup_label(soup),lim_vagas))
    
        print(b)
        #verifica data e controla o loop para a alteracao de paginas buscadas
        if (date_verification(dates[-1], lim) == False or _b==0):
            print("Breaking in page: %s" % str(page + 1))
            print(dates[-1])
            break

        page += 1

    vagas = {}

    for i in range(len(titles) - 1):
        if date_verification(dates[i], lim):
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
            # vagas.append(vagas_dict)

            vagas = {**vagas, **vagas_dict}

    return vagas





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
