class Foo:
    def __init__(self, x = None):
        self._x = x  # Inicializa o atributo protegido _x com o valor de x passado, ou None se não for especificado

    @property
    def x(self):
        return self._x or 0  # Getter da propriedade x, retorna o valor de _x se não for None, senão retorna 0

    @x.setter
    def x(self, value):
        self._x += value  # Setter da propriedade x, incrementa o valor de _x pelo valor passado

    @x.deleter
    def x(self):
        self._x = -1  # Deleter da propriedade x, redefine o valor de _x para -1 ao deletar a propriedade

# Criando uma instância da classe Foo com _x inicializado como 10
foo = Foo(10)
print(foo.x)   # Saída: 10
foo.x = 10
print(foo.x)   # Saída: 20 (pois 10 + 10)
del foo.x
print(foo.x)   # Saída: -1
