class Nivel:
    def __init__(self, numero, enemigos, objetos_especiales, cajas_misterio):
        self.numero = numero
        self.enemigos = enemigos
        self.objetos_especiales = objetos_especiales
        self.cajas_misterio = cajas_misterio

    def esta_completado(self):
        return all(not enemigo.sigue_vivo() for enemigo in self.enemigos)