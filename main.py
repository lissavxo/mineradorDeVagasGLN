import scraping
import file_handler_functions as files 


vagas = scraping.get_vagas()
#print(vagas)
files.vagas_to_json(vagas)

