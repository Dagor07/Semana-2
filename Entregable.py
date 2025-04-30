"""Mini-proyecto: "Agenda de Contactos"
Descripción:
Crea una pequeña agenda que permita:

Agregar un nuevo contacto (nombre y número de teléfono).

Buscar un contacto por su nombre.

Mostrar todos los contactos.

Eliminar un contacto.

Requisitos:
Usar un diccionario donde el nombre sea la clave y el número sea el valor.

Crear un pequeño menú en consola para elegir las acciones."""


agent = {
    "daniela" : "123456789",
    "aleja" : "987654321",
    "mariana" : "24681357"
    }
while True:
    print( "\n1. Agregar un nuevo contacto (nombre y número de teléfono)")
    print("2. Buscar un contacto por su nombre")
    print("3. Mostrar todos los contactos.")
    print("4. Eliminar un contacto.")
    print("5. Salir")
    option = input("Seleccione una opción: ")
    option1 = option.lower()
    match option1:
        case "1" | "uno" | "primero" | "primera":
            nombre = input("Ingrese el nombre: ")
            nombre1 = nombre.lower()
            numero = input("Ingrese el número: ")
            agent [nombre1] =numero
        case "2" | "dos" | "segundo" | "segunda":
            buscar = input("Ingrese nombre: ")
            buscar1 = buscar.lower() 
            if buscar1 in agent: 
                print(f"{buscar1} Si se encuentra en la agenda: ")
                
            else:
                print("No se encuentra en la agenda: ")
                
        case "3" | "tres" | "tercero" | "tercera":
            print(agent)
        case "4" | "cuatro" | "cuarto" | "cuarteto":
            elimina = input("Ingrese del contacto que quieres eliminar: ")
            del agent[elimina] 
            print(agent)
        case "5":
            print("El programa ha terminado")
            break
        case _:
            print("\n Opción invalida")

