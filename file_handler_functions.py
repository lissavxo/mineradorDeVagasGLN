import json
import os 
def read_code_from_json():

    with open('./files/vagas.json') as file_data:
        vagas = json.load(file_data)
        for code_vaga in vagas:
            return code_vaga



def last_sendend_verification(code=None):
    arquivo = './files/last_sended.txt'
    while True:
            
        try:
            file = open(arquivo, 'r')  
            last_code = file.readlines()[0]
            
            break
        except :
            file = open(arquivo, 'w')
            print('Creating a file with the last code')
            file.write(read_code_from_json())


    file.close()
    if code == last_code :
        return False   
    else:
        return True


def vagas_to_json(vagas_dict):
    file_name = './files/vagas.json'
    data = vagas_dict
    if os.path.exists(file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)
            data.update(vagas_dict)

    with open(file_name, 'w') as f:
        json.dump(data, f, ensure_ascii=False)

        
def read_last_code():
    arquivo = './files/last_sended.txt'
    file = open(arquivo, 'r')  
    last_code = file.readlines()[0]
    return last_code
    
def deletar_txt():
    arquivo = './files/last_sended.txt'
    os.remove(arquivo)