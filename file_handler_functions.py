import json
import os 
import bot_functions as bf
import file_handler_functions as files
def read_code_from_json():
    
    if os.path.exists('./files/vagas.json'):
        with open('./files/vagas.json') as file_data:
            vagas = json.load(file_data)
            keys = list(vagas.keys())
            keys.sort()
            return keys[-1]
    else:
        return '0'



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
    
    print ("my keys ->")
    for i in list(vagas_dict.keys()):
        print(i)
    data = None
    if os.path.exists(file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)
            data.update(vagas_dict)
    else:
        data = vagas_dict
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
def read_all_keys():
    arquivo = './files/vagas.json'
    with open(arquivo) as json_file:
        data = json.load(json_file)
        keys = list(data.keys())
    
    return keys

def get_vaga(code):
    vaga = None
    with open('./files/vagas.json') as file_data:
        vagas = json.load(file_data)
        keys = files.read_all_keys()
        for key in keys:
            print(type(key),type(code))
            if key == code:
                vaga = vagas[key]

    return vaga

def create_txt(content):
    file = open('./files/temporary.txt', 'w')
    file.write(content)
    file.close()


def read_temporary_txt():
    file = open('./files/temporary.txt', 'r')
    var  = file.readlines()[0]
    file.close()
    return var

def delete_temporary_txt():
    arquivo = '/home/guilherme/Documentos/Projetos/python/mineradorDeVagasGLN/files/temporary.txt'
    os.remove(arquivo)
    