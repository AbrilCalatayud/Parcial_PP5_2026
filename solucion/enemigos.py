from abc import ABC, abstractmethod

class Enemigo(ABC):
    def __init__(self):
        super().__init__()
        self.derrotado = False

    @abstractmethod
    def recibir_salto(self):
        pass

    @abstractmethod
    def recibir_bola_de_fuego(self):
        pass
        

class Caminante(Enemigo):
    def __init__(self):
        super().__init__()

    def recibir_salto(self):
        self.derrotado = True
        return 100

    def recibir_bola_de_fuego(self):
        self.derrortado = True
        return 100

class Tortuga(Enemigo):
    def __init__(self):
        super().__init__()
        self.saltos_restantes = 2

    def recibir_salto(self):
        if self.saltos_restantes == 1:
            self.derrotado = True
            return 200
        self.saltos_restantes = 1
        return 0

    def recibir_bola_de_fuego(self):
        self.derrotado = True
        return 200

class Fantasma(Enemigo):
    def __init__(self):
        super().__init__()

    def recibir_salto(self):
        return 0

    def recibir_bola_de_fuego(self):
        self.derrortado = True
        return 300