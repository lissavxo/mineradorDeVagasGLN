import json

def read_from_json():

    with open('./files/vagas.json') as file_data:
        vagas = json.load(file_data)
        for code_vaga in vagas:
            return code_vaga



def last_sendend_verification(code):
    arquivo = './files/last_sended.txt'
    try:
        file = open(arquivo, 'r')
        last_code = file.readlines()[0]
        print(last_code,code)
        file.close()
        if code == last_code :
            return False
        
    except :
        file = open(arquivo, 'w')
        file.write(read_from_json())

        return True

last_sendend_verification(code)