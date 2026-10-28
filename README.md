# Parcial de Paradigmas de Prograamción 5
## Correcciones
* En la bola de fuego chequeas si el estado es fuego. El que hace el ataque es el super plomero, el si no es de fuego deberia no poder hacer el ataque de fuego. [Listo]

* Ataque.aplicar te quedo sin self, lo cual afecta atacar_enemigo. [Listo]

* Hay un error en el fantasma al recibir la bola de fuego, el atributo se llama derrortado en lugar de derrotado, con lo cual no muere nunca. [Listoo]

* Evitar las validaciones innecesarias como por ejemplo la de la caja misterio. No deberia ser problema de la caja que guarda. [Listo]

* No hay respuesta a la pregunta teorica.

* El hongo magico aporta 100 puntos estando pequeño, cuando no deberia. [Listo]

* El test pide plomero.puntaje y el atributo se llama puntos. [Listo]

* tocar_enemigo lee el atributo enemigo.derrotado en vez de preguntar al enemigo si esta vivo" [Listo]

## Respuesta a la pregunta teórica
### Nombra qué patrones hay en tu solución y por qué
Los patrones de diseño que hay en mi solución son State y Strategy.

El patrón State lo usé en los estados en los que puede estar el Super Plomero, ya que hay un flujo definido de Pequeño->Grande->Fuego, el estado interno del Plomero puede ir cambiando y cada uno conoce las reglas de transición. También los ataques que puede hacer el personaje dependen de su estado actual. En lugar de usar condicionales para chequear en qué estado está a la hora de realizar ataques y reaccionar al recibir objetos, delego esto a su estado actual.

El patrón Strategy lo utilicé en los ataques (Salto y BolaDeFuego), ya que cada uno de estos reacciona de forma polimórfica al mismo mensaje "ataque.aplicar()", pero con su propio comportamiento, son algo que el jugador puede seleccionar, son intercambiables y podrían sumarse otros que cumplan con la clase los métodos de la clase abstracta. Algo similar sucede con los objetos (Moneda, HongoMagico y FlorDeFuego) que todos reaccionan a su manera al mensaje "objeto.otorgar_beneficio", pueden intercambiarse y pueden sumarse más objetos al juego.
