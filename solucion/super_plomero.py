from solucion.estado import Pequenio
class SuperPlomero:
    def __init__(self):
        self.estado = Pequenio()
        self.puntos = 0
        self.vidas = 3 #no especificaba cuántas vidas debia tener, elegí 3
        self.objetos = []

    def recibir_danio(self):
        self.estado = self.estado.estado_anterior()
        if self.estado.puede_perder_vidas():
            self.perder_vidas()

    def obtener_objeto(self, objeto_especial):
        pass

    def atacar_enemigo(self):
        pass

    def sumar_puntos(self, cantidad):
        pass

    def perder_vidas(self):
        if self.vidas == 1:
            raise ValueError("La cantidad de vidas no puede ser cero. Juego terminado.")
        self.vidas = self.vidas - 1

    def ganar_vida(self):
        self.vidas = self.vidas + 1
        

