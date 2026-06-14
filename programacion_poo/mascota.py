# Definiciónn de la clase Mascota
class Mascota:

    # Constructor de la clase 
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    # Método para mostrar la información de la mascota
    def mostrar_informacion(self):
        print("\n--- Información de la mascota ---")
        print("Nombre:", self.nombre)
        print("Especie:", self.especie)
        print("Edad:", self.edad, "años")

    # Metodo para simular un sonido de la mascota
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido característico.")
        
            