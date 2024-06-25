arquivo = open('C:\Apps\Python\Aulas DIO Python\Aulas-DIO-1\lendo_arquivo\lorem.txt', "r")

print(arquivo.read()) #le todo o arquivo

print(arquivo.readline()) #mostra uma linha por vez

print(arquivo.readlines()) #mostra todas as linhas como lista

while len(linha := arquivo.readline()): 
    print(linha)
    
arquivo.close()