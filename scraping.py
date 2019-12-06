'''
AUTORES:  Lissa Ximenes, Guilherme Ferreira
DATA: 05/11/2019

'''
import funcoes
import json
from datetime import date


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

        print("Page: %s" % page)
        # atribuindo valores as variaveis atributos
        soup = funcoes.get_soup(
            'https://empregos.profissionaisti.com.br/vagas/distrito-federal/' +
            '?p=' + str(page))

        # testanto o tamanho da lista de codes 
        codes = funcoes.get_codes(funcoes.soup_box(soup))
        lim_vagas = 0
        if codes[1]:
            lim_vagas = len(codes[0])
        
        titles.extend(funcoes.get_titles(funcoes.soup_box(soup,lim_vagas)))
        links.extend(funcoes.get_links(soup,lim_vagas))
        codes.extend(codes[0])
        dates.extend(funcoes.get_dates(soup,lim_vagas))
        companies.extend(funcoes.get_companies(funcoes.soup_details(soup,lim_vagas)))
        locais.extend(funcoes.get_locals(funcoes.soup_details(soup,lim_vagas)))
        tags.extend(funcoes.get_tags(funcoes.soup_details(soup,lim_vagas)))
        salaries.extend(funcoes.get_salario(soup, links,lim_vagas))
        regimes.extend(funcoes.get_regime(funcoes.soup_label(soup,lim_vagas)))
        periodos.extend(funcoes.get_periodo(funcoes.soup_label(soup,lim_vagas)))
        descricoes.extend(funcoes.get_descricao(soup, links,lim_vagas))
        # verifica data e controla o loop para a alteracao de paginas buscadas
        if (date_verification(dates[-1], lim) == False):
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


def vagas_to_json(vagas_dict):
    with open('vagas.json', 'w') as json_file:
        json.dump(vagas_dict, json_file, ensure_ascii=False)
    

def last_sended():
  arquivo = './files/last_sended.txt'

  try:
    flag_permission = 'r'
    file = open(arquivo, flag_permission)
    print(file.readlines())
  except:
    flag_permission = 'w'
    file = open(arquivo, flag_permission)
    file.write('2233')
    
  finally:
    file.close()




  


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



last_sended()