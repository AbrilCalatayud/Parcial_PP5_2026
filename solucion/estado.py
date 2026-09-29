from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def siguiente_estado(self):
        pass

    @abstractmethod
    def estado_anterior(self):
        pass

    @abstractmethod
    def puede_perder_vidas(self):
        pass

class Pequenio(Estado):
    def estado_anterior(self):
        return self

    def siguiente_estado(self):
        return Grande()

    def puede_perder_vidas(self):
        return True

class Grande(Estado):
    def estado_anterior(self):
        return Pequenio()

    def siguiente_estado(self):
        return Fuego()

    def puede_perder_vidas(self):
        return False

class Fuego(Estado):
    def estado_anterior(self):
        return Grande()

    def siguiente_estado(self):
        return self

    def puede_perder_vidas(self):
        return False
