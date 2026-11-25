# clase pelota  
class Pelota:
    def __init__(self, numSerie, tamanio, color, estado, peso):
        self.numSerie = numSerie
        self.tamanio = tamanio
        self.color = color
        self.estado = estado
        self.peso = peso

    def __str__(self):
        return f"Pelota: {self.numSerie}, Tamaño: {self.tamanio}, Color: {self.color}, Estado: {self.estado}, Peso: {self.peso}"

   # Métodos getter y setter
    def get_numSerie(self):
        return self.numSerie

    def get_tamanio(self):
        return self.tamanio

    def get_color(self):
        return self.color

    def get_estado(self):
        return self.estado
    def get_peso(self):
        return selt.peso
    
    def set_numSerie(self, numSerie):
        self.numSerie = numSerie

    def set_tamanio(self, tamanio):
        self.tamanio = tamanio

    def set_color(self, color):
        self.color = color

    def set_estado(self, estado):
        self.estado = estado
    def set_peso(self, peso):
        self.peso = peso
    # metodo rebotar de acuerdo al peso de la pelota
    def rebotar(self):
        if self.peso > 100:
            return "La pelota rebota alto"
        else:
            return "La pelota rebota bajo"
