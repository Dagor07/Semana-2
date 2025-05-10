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
    "daniela": "123456789",
    "aleja": "987654321",
    "mariana": "24681357"
}

while True:
    print("\n1. Agregar un nuevo contacto (nombre y número de teléfono)")
    print("2. Buscar un contacto por su nombre")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar un contacto")
    print("5. Salir")
    
    option = input("Seleccione una opción: ").lower()

    match option:
        case "1" | "uno" | "primero" | "primera":
            nombre = input("Ingrese el nombre: ").strip().lower()
            if not nombre:
                print(" El nombre no puede estar vacío.")
                continue

            if nombre in agent:
                print(" Este contacto ya existe.")
                continue

            numero = input("Ingrese el número: ").strip()
            if not numero.isdigit():
                print(" El número debe contener solo dígitos.")
                continue

            agent[nombre] = numero
            print(f" Contacto '{nombre}' agregado.")

        case "2" | "dos" | "segundo" | "segunda":
            buscar = input("Ingrese nombre: ").strip().lower()
            if buscar in agent:
                print(f" {buscar}: {agent[buscar]}")
            else:
                print(" Contacto no encontrado.")

        case "3" | "tres" | "tercero" | "tercera":
            if not agent:
                print(" La agenda está vacía.")
            else:
                print("\n Contactos:")
                for nombre, numero in agent.items():
                    print(f"- {nombre}: {numero}")

        case "4" | "cuatro" | "cuarto" | "cuarteto":
            elimina = input("Ingrese el nombre del contacto que desea eliminar: ").strip().lower()
            if elimina in agent:
                del agent[elimina]
                print(f" Contacto '{elimina}' eliminado.")
            else:
                print(" Ese contacto no está en la agenda.")

        case "5":
            print(" El programa ha terminado.")
            break

        case _:
            print(" Opción inválida. Intente de nuevo.")

