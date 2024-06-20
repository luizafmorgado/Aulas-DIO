class Animal:
    def __init__(self,numero_patas):
        self.numero_patas = numero_patas


class Mamifero(Animal):
    def __init__(self,numero_patas):
        self.numero_patas = numero_patas
        super().__init__(numero_patas)

class Ave(Animal):
    def __init__(self,numero_patas):
        self.numero_patas = numero_patas
        super().__init__(numero_patas)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass