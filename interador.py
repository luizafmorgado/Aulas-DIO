class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros 
        self.contador = 0

    def __iter__(self):
        return (self)
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError: #quando o python aparecer essa mensagem o código vai entender que deve parar
            raise StopIteration #interrompe a interação, impedindo de ficar em loop infinito


for i in MeuIterador(numeros=[1, 2, 3]):
    print(i)