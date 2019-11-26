import telepot
import json 

def bot_run():
    bot = telepot.Bot('967072767:AAGwRX7xXYjDL005j8eu8rHAsXXwA-mq77U')

    with open('vagas.json') as file_data:
        vagas = json.load(file_data)

        for vaga in vagas:
            vaga = vagas[vaga]

            message = '{}\n{}\n{} - {} - {}\n{}\n{}\n{} - {}\n\n{}\n'.format(vaga['Titulo'],vaga["Link"],vaga["Data"],vaga["Empresa"],vaga[ "Local"],vaga[ "Tag"],vaga["Salary"],vaga[ "Regime"],vaga["Período"],vaga["Descrição"])


            bot.sendMessage(-1001494820086,message)
        
        

