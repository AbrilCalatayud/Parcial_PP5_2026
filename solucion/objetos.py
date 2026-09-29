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

class CajaMisterio:
    def __init__(self, objeto_contenido):
        if isinstance(objeto_contenido, ObjetoEspecial):
            self.objeto_contenido = objeto_contenido

    def sacar_contenido(self):
        if self.objeto_contenido is None:
            raise ValueError("No se puede utilizar una caja misterio vacía.")

        objeto_contenido_temp = self.objeto_contenido
        self.objeto_contenido = None
        return objeto_contenido_temp