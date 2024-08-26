import pandas as pd
import os

# Chama a pasta "Arquivos" e mostra todos os arquivos dentro dela
varFiles = os.listdir("Arquivos") # Checa todos os arquivos dentro da pasta selecionada
for x in varFiles:
    splitValue = x.split(".")
    if splitValue[len(splitValue)-1] != "xlsx": # Mais extensões devem ser incluídas 
        # Deve impedir que arquivos que não representem certas extensões de spreadsheet sejam mostrados ao usuário
        varFiles.remove(x) # Remove o arquivo da listagem
    else:
        print(str(varFiles.index(x)) + ":" + x) # Mostra o arquivo que é da extensão correta

pathFinal = "Arquivos/" + varFiles[int(input("Selecione o arquivo: "))] # Concatena o caminho do arquivo
df = pd.read_excel(pathFinal, engine="openpyxl") # Coloca os valores da tabela na variável "df"
    