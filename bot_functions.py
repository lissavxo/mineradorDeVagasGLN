import json 
import file_handler_functions as files

def vagas_to_send():
    keys = []
    code = files.read_last_code()
    _file = './files/vagas.json'
    keys_to_send = []
    with open(_file) as f:
        vagas = json.load(f)
        keys = list(vagas.keys())
        keys.reverse()
        for key in keys:
            if key <= code:
                return keys_to_send
            
            keys_to_send.append(key)
    return keys_to_send
            

def filter_vagas(tag):
    arquivo = './files/vagas.json'
    tags_to_send = []
    with open(arquivo) as json_file:
        vagas = json.load(json_file)

        for code_vaga in vagas:
            Tags = vagas[code_vaga]['Tag']
            

            for vaga_tag in Tags:
                if vaga_tag == tag:
                    tags_to_send.append(code_vaga)  
                    break
    return tags_to_send


