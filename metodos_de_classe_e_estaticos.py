class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nasc(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome,idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# p0 = Pessoa("Luiza", 26)
# print(p0.nome, p0.idade)

p1 = Pessoa().criar_de_data_nasc(1998,5,27,"Luiza")
print(p1.nome, p1.idade)

#pessoa = classe e e_maior_idade = método exemplo de método estático
print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))