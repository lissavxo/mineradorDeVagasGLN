import scraping
import file_handler_functions as files 
import aurelius_canal as canal

vagas = scraping.get_vagas()
#print(vagas)
files.vagas_to_json(vagas)

canal.main()

