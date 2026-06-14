def registrar_mascota():
    nombre = input("Ingrese nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota: "))

    return nombre, especie, edad
def mostrar_mascota(nombre, especie, edad): 
    print("\n--- Información de la mascota ---")
    print("Nombre:", nombre)
    print("Especie:", especie)
    print("Edad:", edad)

nombre, especie, edad = registrar_mascota()
mostrar_mascota(nombre, especie, edad)