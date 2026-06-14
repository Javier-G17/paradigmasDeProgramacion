# Importa la clase Mascota desde el archivo mascota.py
from mascota import Mascota

# Creacion de dos objetos de la clase Mascota
mascota1 = Mascota("Tom", "Perro", 3)
mascota2 = Mascota("Pepe", "Gato", 2)

#Mostrar información y sonido de la primera mascota 
mascota1.mostrar_informacion()
mascota1.hacer_sonido()

# Mostrar información y sonido de la segunda mascota
mascota2.mostrar_informacion()
mascota2.hacer_sonido()