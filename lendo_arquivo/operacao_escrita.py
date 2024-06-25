arquivo = open ("C:\Apps\Python\Aulas DIO Python\Aulas-DIO-1\lendo_arquivo/teste.txt","w")
arquivo.write("Escrevendo dados novos em um arquivo! ")
arquivo.writelines(["\n",'escrevendo ',"\n", 'um ',"\n", 'novo ',"\n", 'texto']) #uma lista ou tuplas que deve ser interavél
arquivo.close()