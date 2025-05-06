ListaAnimales = []
ListaAnimales == {}

def IngresarCaracteristicas():
        Nombre = input("Ingrese el nombre del animal: ")
        Edad = input("Ingrese la edad del animal: ")
        Especie = input("Ingrese la especie del animal: ").lower()
        Sexo = input("Ingrese el sexo del animal: ").lower()  
        Enfermo = input("¿Está enfermo? (Si/No): ").lower()
        
        Animal = {
            "Nombre": Nombre,
            "Edad": Edad,
            "Especie": Especie,
            "Sexo": Sexo,
            "Enfermo": Enfermo
        }
        ListaAnimales.append(Animal)
        
def ListaAnimales():
        if len(ListaAnimales) == 0:
            print("No hay animales en la lista.")
        else:
            for i, animal in enumerate(ListaAnimales):
                print(f"Animal {i + 1}:")
                for key, value in animal.items():
                    print(f"{key}: {value}")
                print()
                
def EliminarAnimales(): #por nombre
        if len(ListaAnimales) == 0:
            print("No hay animales en la lista.")
        else:
            Nombre = input("Ingrese el nombre del animal a eliminar: ")
            for i, animal in enumerate(ListaAnimales):
                if animal["Nombre"] == Nombre:
                    del ListaAnimales[i]
                    print(f"Animal {Nombre} eliminado.")
                    break
            else:
                print(f"No se encontró el animal {Nombre}.")


def menu_principa():
    while True:
        print("1. Agregar animal")
        print("2. Mostrar lista de animales")
        print("3. Eliminar animales")
        print("4. Salir del programa")
        input("Seleccione una opción: ")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            IngresarCaracteristicas()
        elif opcion == "2":
            ListaAnimales()
        elif opcion == "3":
            EliminarAnimales()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
menu_principa()