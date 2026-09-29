import pytest
from solucion.super_plomero import SuperPlomero
from solucion.nivel import Nivel
from solucion.objetos import Moneda, HongoMagico, FlorDeFuego, CajaMisterio
from solucion.ataques import Salto, BolaDeFuego
from solucion.enemigos import Caminante, Tortuga, Fantasma
from solucion.estado import Pequenio, Grande, Fuego

def test_plomero_comienza_pequeno():
    plomero = SuperPlomero()
    assert isinstance(plomero.estado, Pequenio)

def test_pequeno_obtiene_hongo_pasa_a_grande():
    plomero = SuperPlomero()
    plomero.obtener_objeto(HongoMagico())
    assert isinstance(plomero.estado, Grande)

def test_grande_obtiene_hongo_gana_puntos_y_no_cambia_estado():
    plomero = SuperPlomero()
    plomero.estado = Grande()
    plomero.obtener_objeto(HongoMagico())
    assert isinstance(plomero.estado, Grande)
    assert plomero.puntaje == 100

def test_grande_recibe_danio_vuelve_a_pequeno():
    plomero = SuperPlomero()
    plomero.estado = Grande()
    plomero.recibir_danio()
    assert isinstance(plomero.estado, Pequenio)

def test_fuego_recibe_danio_pasa_a_grande():
    plomero = SuperPlomero()
    plomero.estado = Fuego()
    plomero.recibir_danio()
    assert isinstance(plomero.estado, Grande)

def test_caja_misterio_entrega_objeto_una_vez():
    caja = CajaMisterio(HongoMagico())
    objeto = caja.sacar_contenido()
    assert objeto == "Hongo Mágico"
    with pytest.raises(ValueError):
        caja.sacar_contenido()

def test_caminante_derrotado_por_salto():
    plomero = SuperPlomero()
    caminante = Caminante()
    plomero.atacar_enemigo(Salto(), caminante)
    assert caminante.derrotado is True
    assert plomero.puntos == 100

def test_tortuga_primer_salto_se_esconde():
    plomero = SuperPlomero()
    tortuga = Tortuga()
    plomero.atacar_enemigo(Salto(), tortuga)
    assert tortuga.derrotado is False
    assert tortuga.saltos_restantes == 1

## No llegué a implementar el resto
