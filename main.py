import scraping
import bot
vagas = scraping.get_vagas()

scraping.vagas_to_dict(vagas)

bot.bot_run()