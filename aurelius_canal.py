# Documentação: https://python-telegram-bot.readthedocs.io/en/stable/index.html
# Instalação: https://pypi.org/project/python-telegram-bot/
# Exemplos: https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples
# README: https://github.com/python-telegram-bot/python-telegram-bot
# Primeiro BOT: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
# Introdução a API: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API

import telegram
import json
import bot_functions as bf
def main():
    bot = telegram.Bot('835018973:AAGk01FZbqkBQdR5JJ6s3V5U4s8BmjuEsbw')

    with open('./files/vagas.json') as file_data:
        vagas = json.load(file_data)
        keys = bf.vagas_to_send()
        for key in keys:
            vaga = vagas[key]
            print('sending -:' ,key)
            message = '{}\n{} - {} - {}\n{}\n{}\n{} - {}\n\n'.format(vaga['Titulo'],vaga["Data"],vaga["Empresa"],vaga["Local"],vaga["Salary"],vaga[ "Regime"],vaga["Período"],vaga["Link"])


            bot.sendMessage(-1001494820086,message)

# if __name__ == '__main__':
#     main()