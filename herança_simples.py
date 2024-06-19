class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando o motor')


class Motocicleta(veiculo):
    pass

class Carro (veiculo):
    pass

class Caminhao (veiculo):
    def __init__(self, carregado, cor, placa, numero_rodas):
        self.carregado = carregado
        super().__init__(cor, placa, numero_rodas)

    def esta_carregado(self):
            print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("roxa", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("azul", "xyz-0987", 4)
carro.ligar_motor()

caminhao = Caminhao("preta", "jkl-8520", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()