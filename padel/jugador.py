# relaciona con la clase pelota y raqueta
from pelota import Pelota
from raqueta import Raqueta

# crear la clase jugador

class jugador:
    def __init__(self, cedula, nombre, posicion, lado):
        self.cedula = cedula
        self.nombre = nombre
        self.posicion = posicion
        self.lado = lado
        self.energia = 100
        self.raqueta = None

    def __str__(self):
        return f"El jugador: {self.cedula}, Nombre: {self.nombre}, Posición: {self.posicion}, Lado: {self.lado}, Nivel de energia: {self.energia}"

# Crear los metodos get y set
# Métodos getter y setter
    
    def set_cedula(self, cedula):
            self.cedula = cedula
    
    def get_cedula(self):
        return self.cedula

    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
    
    def set_posicion(posicion):
        self.posicion = posicion
            
    def get_posicion(self):
        return self.posicion

    def set_lado(lado):
        self.lado = lado
                
    def get_lado(self):
        return self.lado

    def get_energia(self):
        return self.energia
    

    def golpear_pelota(self, pelota):
        if self.energia > 30:
            self.energia = self.energia - 30
            return f"{self.nombre} golpea la pelota. {pelota.rebotar()}"
        else:
            return "El jugador no tiene energía suficiente para golpear"

    def cambiarRaqueta(self, raqueta):
        self.raqueta = raqueta
        return f"{self.nombre} cambió a la raqueta {raqueta.get_marca()} {raqueta.get_modelo()}. {raqueta.cambiarMalla()}"

    def mover(self, nueva_posicion):
        if self.energia > 10:
            self.posicion = nueva_posicion
            self.energia = self.energia - 10
            return f"El jugador se movió a {self.posicion}. Energía restante: {self.energia}"
        else:
            return "El jugador no tiene energía suficiente para moverse"
