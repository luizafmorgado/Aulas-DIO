import os
import shutil
from pathlib import Path 

ROOT_PATH = Path(__file__).parent #mostra qual pasta você está tem a mesma função que o pwd
print(ROOT_PATH.parent) #parent tem a mesma função que o cd ...
print(ROOT_PATH.parent)

os.mkdir(ROOT_PATH / 'novo-diretorio') #cria um novo diretorio
# arquivo = open("novo-arquivo.txt") #também cria um novo arquivo

arquivo = open(ROOT_PATH / "novo.txt", "w") #forma correta de abrir um novo arquivo na pasta de deseja

arquivo = close()

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt") #troca o nome do arquivo

os.remove(ROOT_PATH / "alterado.txt") #apaga arquivos

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt") #move arquivos de pasta