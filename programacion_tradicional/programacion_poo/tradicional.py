# Función para registrar los datos de la mascota
def registrar_mascota():
    nombre = input("Ingrese nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota: "))

# Retorna los datos ingresados
    return nombre, especie, edad

# Función para mostrar la información de la mascota
def mostrar_mascota(nombre, especie, edad): 
    print("\n--- Información de la mascota ---")
    print("Nombre:", nombre)
    print("Especie:", especie)
    print("Edad:", edad)

# Programa principal 
# Registra los datos de la mascota
nombre, especie, edad = registrar_mascota()

# Muestra la información registrada
mostrar_mascota(nombre, especie, edad)