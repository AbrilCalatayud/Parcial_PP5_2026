from abc import ABC, abstractmethod

class ObjetoEspecial(ABC):
    @abstractmethod
    def otorgar_beneficio(self, estado):
        pass

class Moneda(ObjetoEspecial):
    def otorgar_beneficio(self, estado):
        return estado, 50

class HongoMagico(ObjetoEspecial):
    def otorgar_beneficio(self, estado):
        return estado.recibir_hongo_magico(), 100

class FlorDeFuego(ObjetoEspecial):
    def otorgar_beneficio(self, estado):
        return estado.recibir_flor_de_fuego(), 0