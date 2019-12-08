# Documentação: https://python-telegram-bot.readthedocs.io/en/stable/index.html
# Instalação: https://pypi.org/project/python-telegram-bot/
# Exemplos: https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples
# README: https://github.com/python-telegram-bot/python-telegram-bot
# Primeiro BOT: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
# Introdução a API: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API

import logging
import json
import file_handler_functions as files
import bot_functions as bf

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters, ConversationHandler, MessageHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# Função chamada no /start
def start(update, context):
    keyboard = [[InlineKeyboardButton(
        "Filtrar por tag", callback_data='filtrar_area')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Escolha uma opção:', reply_markup=reply_markup)

# Função para retornar ao /start


def start_over(update, context):
    query = update.callback_query

    bot = context.bot

    keyboard = [
        [InlineKeyboardButton("Filtrar por área",
                              callback_data='filtrar_area')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Escolha uma opção",
        reply_markup=reply_markup
    )

# Inicia a conversa para filtrar vagas


def iniciar_filtrar_area(update, context):
    query = update.callback_query

    bot = context.bot

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Ok, entendido! \nDigite a tecnologia que deseja filtrar\nVou te mandar uma lista das vagas que eu encotrar aqui: \nSelecione a vaga clickando na tag"
    )

# filtra vagas pela tag (IMPLEMENTAR AS TAGS AQUI)


def dict_treatment(dict_vagas):
    new_dict_vagas = []
    for item in dict_vagas:
        lista = []
        lista.append(item)
        lista.append(dict_vagas[item])
        new_dict_vagas.append(' '.join(lista))
    dict_vagas = new_dict_vagas

    return dict_vagas


def filtrar_area(update, context):
    text = update.message.text
    files.create_txt(text)
    print(text)

    keyboard = [[InlineKeyboardButton("Carregar mais", callback_data='load_more')],
                [InlineKeyboardButton(
                    "Retornar ao ínicio", callback_data='start_over')]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    dict_vagas = bf.filter_vagas(text.lower())
    if dict_vagas == {}:
        _message = 'Nao encontrei nada aqui. Tente pesquisar por outra palavra relacionada'
    else:
        dict_vagas = dict_treatment(dict_vagas)
        _message = '\n'.join('/{}'.format(k) for k in dict_vagas)
    if len(dict_vagas) < 10:

        keyboard = [[InlineKeyboardButton(
            "Retornar ao ínicio", callback_data='start_over')]]

        reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(_message, reply_markup=reply_markup)

# Retorna uma vaga (IMPLEMENTAR JSON DAS VAGAS)


def retornar_vaga(update, context):
    code = update.message.text
    code = list(code)
    code = code[1:]
    code = ''.join(code)
    print(code)
    message = bf.formated_vaga(code)
    print(message)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=message, callback_data='lissa')

# Atualiza a mensagem com outra vaga (IMPLEMENTAR JSON DAS VAGAS)


def load_more(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Retornar ao ínicio",
                              callback_data='start_over')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = files.read_temporary_txt()
    dict_vagas = bf.filter_vagas(text.lower(), True)
    dict_vagas = dict_treatment(dict_vagas)
    _message = '\n'.join('/{}'.format(k) for k in dict_vagas)
    files.read_temporary_txt()
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=_message,
        reply_markup=reply_markup
    )


#Função /help
def help(update, context):
    update.message.reply_text("Use /start para iniciar o bot")

# Exibe uns log loco que eu não sei usar


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(
        "835018973:AAGk01FZbqkBQdR5JJ6s3V5U4s8BmjuEsbw", use_context=True)

    # Inicia as funções
    updater.dispatcher.add_handler(CommandHandler('start', start))

    keys = files.read_all_keys()

    for i in keys:
        updater.dispatcher.add_handler(
            CommandHandler('{}'.format(i), retornar_vaga))

    updater.dispatcher.add_handler(CallbackQueryHandler(
        retornar_vaga, pattern='^' + 'obter_vaga' + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(
        load_more, pattern='^' + 'load_more' + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(
        iniciar_filtrar_area, pattern='^' + 'filtrar_area' + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(
        start_over, pattern='^' + 'start_over' + '$'))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, filtrar_area))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Inicia o bot
    updater.start_polling()

    # Executa o bot até o usuário apertar Ctrl-C ou o processo receber SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
