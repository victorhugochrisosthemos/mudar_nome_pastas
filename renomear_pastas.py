import os
folder = r'C:/Users/Victor/projetos_git/mudar_nome_pastas/Arquivos//'
for file_name in os.listdir(folder):
    old_name = folder + file_name
    nome = ""
    for i in range(len(file_name)):
        if(file_name[i] != ' ' and file_name[i] != '_'):
            if(i == 0 or file_name[i - 1] == ' ' or file_name[i - 1] == '_'):
                nome += file_name[i].upper()
            else:
                nome += file_name[i].lower()
    new_name = folder + nome
    os.rename(old_name, new_name)    
print(os.listdir(folder))





