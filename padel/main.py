# uso de las clases jugador, pelota y raqueta
from jugador import jugador
from pelota import Pelota
from raqueta import Raqueta

# crear una pelota
pelota = Pelota("P01", "estandar", "amarillo", "nueva", 120)

# crear una raqueta
raqueta = Raqueta("R01", "Wilson", "wilson", 360, "carbono")

# crear un jugador
jugador1 = jugador("1101", "Ana", "fondo", "derecho")

# mostrar los objetos
print(jugador1)
print(pelota)

# el jugador cambia de raqueta
print(jugador1.cambiarRaqueta(raqueta))
print(raqueta.cambiarGrip())

# el jugador se mueve y golpea la pelota
print(jugador1.mover("red"))
print(jugador1.golpear_pelota(pelota))
print(pelota.rebotar())
