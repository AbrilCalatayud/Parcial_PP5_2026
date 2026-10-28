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
    assert plomero.puntos == 100

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
    assert isinstance(objeto, HongoMagico)
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

def test_tortuga_escondida_es_derrotada_segundo_salto():
    plomero = SuperPlomero()
    tortuga = Tortuga()
    plomero.atacar_enemigo(Salto(), tortuga)
    plomero.atacar_enemigo(Salto(), tortuga)
    assert tortuga.derrotado is True

def test_fantasma_no_es_derrotado_por_salto():
    plomero = SuperPlomero()
    fantasma = Fantasma()
    plomero.atacar_enemigo(Salto(), fantasma)
    assert fantasma.derrotado is False

def test_fantasma_es_derrotado_por_bola_de_fuego():
    plomero = SuperPlomero()
    plomero.estado = Fuego()
    fantasma = Fantasma()
    plomero.atacar_enemigo(BolaDeFuego(), fantasma)
    assert fantasma.derrotado is True

def test_plomero_no_puede_lanzar_bola_de_fuego_si_no_esta_en_fuego():
    plomero = SuperPlomero()
    caminante = Caminante()
    with pytest.raises(TypeError):
        plomero.atacar_enemigo(BolaDeFuego(), caminante)
    assert caminante.derrotado is False
    assert plomero.puntos == 0

def test_derrotar_caminante_otorga_100_puntos():
    plomero = SuperPlomero()
    caminante = Caminante()
    plomero.atacar_enemigo(Salto(), caminante)
    assert caminante.derrotado is True
    assert plomero.puntos == 100

def test_nivel_completado_cuando_todos_los_enemigos_estan_derrotados():
    caminante = Caminante()
    nivel = Nivel(1, [caminante], [], [])
    plomero = SuperPlomero()
    plomero.atacar_enemigo(Salto(), caminante)
    assert caminante.derrotado is True
    assert nivel.esta_completado()

def test_obtiene_caja_con_hongo_luego_sufre_danio():
    plomero = SuperPlomero()
    assert isinstance(plomero.estado, Pequenio)
    
    caja = CajaMisterio(HongoMagico())
    plomero.recibir_caja_misterio(caja)
    assert isinstance(plomero.estado, Grande)
    
    plomero.recibir_danio()
    assert isinstance(plomero.estado, Pequenio)

def test_plomero_de_fuego_vs_fantasma():
    plomero = SuperPlomero()
    plomero.estado = Fuego()
    fantasma = Fantasma()
    
    plomero.atacar_enemigo(BolaDeFuego(), fantasma)
    
    assert fantasma.derrotado is True
    assert plomero.puntos == 300

## el test automático (req. 16) de la caja que entrega el objeto una sola vez, ya lo hice

def test_18_perder_ultima_vida_interrumpe_juego():
    plomero = SuperPlomero()
    plomero.perder_vidas()
    plomero.perder_vidas()
    
    with pytest.raises(ValueError):
        plomero.perder_vidas()