import io, subprocess, configparser

config = configparser.ConfigParser()
config.read('conf_db.ini')

with io.open("GTA_ALL.txt", encoding='utf-8') as file:

    print('Добро пожаловать в базу данных текстур GTA')   
    word = input('Введите название архива или текстуры\nВведите \"/exit\" для выхода\n\n')
    for i in file.readlines():
        
        if word in i:
            print(i)
            
        if word == "/exit":
            quit()

        if word == "":
            break
            
    a=input('Нажмите Enter, чтобы продолжить\n')
    if a == "/exit":
        quit()
            
p = subprocess.Popen([config.get('Settings', 'Python_dir'), 'dbCMD.py'], start_new_session = True)
