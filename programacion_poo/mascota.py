class Mascota:

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print("\n--- Información de la mascota ---")
        print("Nombre:", self.nombre)
        print("Especie:", self.especie)
        print("Edad:", self.edad, "años")

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido característico.")
        
            