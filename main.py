import scraping
import bot

print("\nOpções:\n1 - Fazer o scraping das vagas\n2 - Enviar para o canal\n")
entrada = int(input("Selecione uma opção: "))
print("")

if entrada == 1:
    vagas = scraping.get_vagas()
    scraping.vagas_to_dict(vagas)
elif entrada == 2:
    bot.bot_run()
