class bicicleta:
    def __init__ (self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar (self):
        print("Bibiiii")
    
    def para (self):
        print("Parando bicicleta")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm")

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave} = {valor}' for chave, valor in self.__dict__.items()]}"

b1= bicicleta("cereja","caloi", 2024, 600)
b1.correr()
b1.buzinar()
b1.para()

print (b1)