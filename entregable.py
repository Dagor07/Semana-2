inventory = []

def num_positive(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print("The number is not positive")
        except ValueError:
            print("the number is invalid")

def num_integer_positive(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            else:
                print("The number is not positive")
        except ValueError:
            print("the number is invalid")

def add_product():
    product_name = input("Product: ")
    price = num_positive("Price: ")
    Quantuty = num_integer_positive("Quantity available: ")
    product = {
        'Name': product_name,
        'Price': price,
        'quantity available': Quantuty
    }
    inventory.append(product)
    print("product added:", product)

def get_product():
    name= input("Name of the product to be updated: ")
    price = num_positive("New price: ")
    product = {
        'Name': name,
        'Price': price
    }
    return product

def consult_product():
    if not inventory:
        print("The inventory is empty")
    else:
        print("Consult product")
        for product in inventory:
            print(product)

def update_price():
    update_product = get_product()
    found = False
    for product in inventory:
        if product['Name'] == update_product['Name']:
            product['Price'] = update_product['Price']
            found = True
            print("Price update:", product)
            break
    if not found:
        print("This function is not in the inventory")

def eliminar_productos():
    nombre_producto = input("Producto a eliminar: ")
    for producto in inventory:
        if producto['Nombre'] == nombre_producto:
            inventory.remove(producto)
            print("Producto eliminado")
            return
    print("Producto no encontrado")

def calcular_valor_total_inventario():
    total = 0
    for producto in inventory:
        total += producto['Precio'] * producto['Cantidad Disponible']
    print(f"Valor total del inventario: ${total:.2f}")

def menu_principal():
    while True:
        print('-----------------------------------------------')
        print("1. Agregar productos")
        print("2. Consultar productos")
        print("3. Actualizar precios")
        print("4. Eliminar productos")
        print("5. Valor total del inventario")
        print("6. Salir")
        print('-----------------------------------------------')
        opcion = input('Elige lo que deseas realizar: ')
        print('-----------------------------------------------')
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            consultar_productos()
        elif opcion == '3':
            actualizar_precios()
        elif opcion == '4':
            eliminar_productos()
        elif opcion == '5':
            calcular_valor_total_inventario()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print('Número inválido')

menu_principal()