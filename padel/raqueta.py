# clase raqueta
class Raqueta:
    def __init__(self, numSerie, marca, modelo, peso, material):
        self.numSerie = numSerie
        self.marca = marca
        self.modelo = modelo
        self.peso = peso
        self.material = material

    def __str__(self):
        return f"Raqueta: {self.numSerie}, Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Estado: {self.estado}, Peso: {self.peso}"
    
    # metodos get y set
    def get_numSerie(self):
        return self.numSerie
    def get_marca(self):
        return self.marca
    def get_modelo(self):
        return self.modelo
    def get_peso(self):
        return self.peso
    def get_material(self):
        return self.material
    
    def set_numSerie(self, numSerie):
        self.numSerie = numSerie
    def set_marca(self, marca):
        self.marca = marca
    def set_modelo(self, modelo):
        self.modelo = modelo
    def set_peso(self, peso):
        self.peso = peso
    def set_material(self, material):
        self.material = material

    def cambiarGrip(self):
        if self.material == "Dañado"
            return "Cambiar grip"
        else:
            return "No cambiar grip"
    
    def cambiarMalla(self):
        if self.modelo == "wilson"
            return "Se sugiere cambiar la malla cada 3 años"
        else:
            return "Cambiar la malla cada año"
    

