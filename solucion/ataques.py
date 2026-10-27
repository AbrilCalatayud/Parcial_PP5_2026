from abc import ABC, abstractmethod
from solucion.estado import Fuego
class Ataque(ABC):
    @abstractmethod
    def aplicar(self, enemigo, estado):
        pass

class Salto(Ataque):
    def aplicar(self, enemigo, estado):
        return enemigo.recibir_salto()
    
class BolaDeFuego(Ataque):
    def aplicar(self, enemigo, estado):
        if not isinstance (estado, Fuego):
            raise TypeError("Solo puede lanzar una bola de fuego si tiene estado Fuego")
        return estado.lanzar_bola_de_fuego(enemigo)
