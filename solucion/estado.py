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

    @abstractmethod
    def recibir_hongo_magico(self):
        pass

    @abstractmethod
    def recibir_flor_de_fuego(self):
        pass

class Pequenio(Estado):
    def estado_anterior(self):
        return self

    def siguiente_estado(self):
        return Grande()

    def puede_perder_vidas(self):
        return True

    def recibir_hongo_magico(self):
        return Grande()

    def recibir_flor_de_fuego(self):
        return Fuego()

class Grande(Estado):
    def estado_anterior(self):
        return Pequenio()

    def siguiente_estado(self):
        return Fuego()

    def puede_perder_vidas(self):
        return False

    def recibir_hongo_magico(self):
        return self

    def recibir_flor_de_fuego(self):
        return Fuego()

class Fuego(Estado):
    def estado_anterior(self):
        return Grande()

    def siguiente_estado(self):
        return self

    def puede_perder_vidas(self):
        return False

    def recibir_hongo_magico(self):
        return self
    
    def recibir_flor_de_fuego(self):
        return self
