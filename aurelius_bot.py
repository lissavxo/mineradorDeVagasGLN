# Documentação: https://python-telegram-bot.readthedocs.io/en/stable/index.html
# Instalação: https://pypi.org/project/python-telegram-bot/
# Exemplos: https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples
# README: https://github.com/python-telegram-bot/python-telegram-bot
# Primeiro BOT: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
# Introdução a API: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API

import logging
import json

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters, ConversationHandler, MessageHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# Função chamada no /start
def start(update, context):
    keyboard = [[InlineKeyboardButton("Obter vaga recente", callback_data='obter_vaga'),
                 InlineKeyboardButton("Filtrar por área", callback_data='filtrar_area')]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Escolha uma opção:', reply_markup=reply_markup)

# Função para retornar ao /start
def start_over(update, context):
    query = update.callback_query

    bot = context.bot

    keyboard = [[InlineKeyboardButton("Obter vaga recente", callback_data='obter_vaga'),
                 InlineKeyboardButton("Filtrar por área", callback_data='filtrar_area')]
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
        text="Certo, qual área?"
    )

# filtra vagas pela tag (IMPLEMENTAR AS TAGS AQUI)
def filtrar_area(update, context):
    text = update.message.text
    print(text)
    if text == 'python':
        update.message.reply_text('Funcionou!')

# Retorna uma vaga (IMPLEMENTAR JSON DAS VAGAS)
def retornar_vaga(update, context):
    query = update.callback_query

    bot = context.bot

    keyboard = [
        [InlineKeyboardButton("Carregar mais", callback_data='load_more'),
         InlineKeyboardButton("Retornar ao ínicio", callback_data='start_over')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text='vaga 1',
        reply_markup=reply_markup
    )

# Atualiza a mensagem com outra vaga (IMPLEMENTAR JSON DAS VAGAS)
def load_more(update, context):
    query = update.callback_query

    bot = context.bot

    keyboard = [
        [InlineKeyboardButton("Carregar mais", callback_data='obter_vaga'),
         InlineKeyboardButton("Retornar ao ínicio", callback_data='start_over')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text='vaga 2',
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
