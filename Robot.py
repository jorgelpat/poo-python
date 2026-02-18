# Clase: es una plantilla que define caracteristicas y comportamientos de un objeto
class Robot:
    # Constructor: es un método especial que se ejecuta al crear una instancia y permite inicializar los atributos
    # Self: se refiere a la instancia específica
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

# Instancia: es un objeto específico crado a partir de la plantilla llamada clase
robotin = Robot("Robotín", "Humanoide")

print(robotin.nombre)
print(robotin.tipo)