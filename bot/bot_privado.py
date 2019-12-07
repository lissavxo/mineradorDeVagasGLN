import telepot


def main():
    def on_chat_message(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print('Chat Message:', content_type, chat_type, chat_id)

        if content_type == 'text':
            if msg['text'] == '/procurar_vaga_por_area':
                bot.sendMessage(chat_id,
                                'Digite a área que você deseja procurar:')

            elif msg['text'] == 'Outra coisa':
                bot.sendMessage(
                    chat_id, 'Shimbalaiê, quando vejo o sol beijando o mar')

    bot = telepot.Bot('967072767:AAGwRX7xXYjDL005j8eu8rHAsXXwA-mq77U')
    
    print('Listening ...')
    bot.message_loop({'chat': on_chat_message}, run_forever=True)
