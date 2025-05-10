# Inventory is a list of dictionaries. Each product is stored as: {'ProductName': (price, quantity)}
inventory = []

# Gets a positive float from user
def num_positive(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print("The number is not positive.")
        except ValueError:
            print("Invalid number.")

# Gets a positive integer from user
def num_integer_positive(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            else:
                print("The number is not positive.")
        except ValueError:
            print("Invalid number.")

# Adds a new product to the inventory
def add_product():
    product_name = input("Product name: ")
    # Check if the product already exists
    for product in inventory:
        if product_name in product:
            print("Product already exists.")
            return
    price = num_positive("Price: ")
    quantity = num_integer_positive("Available quantity: ")
    inventory.append({product_name: (price, quantity)})
    print(f"Product added: {product_name} - Price: ${price:.2f}, Quantity: {quantity}")

# Searches for a product by name
def search_product_by_name():
    name = input("Enter product name to search: ")
    for product in inventory:
        if name in product:
            price, quantity = product[name]
            print(f"Found: {name} - Price: ${price:.2f}, Quantity: {quantity}")
            return
    print("Product not found.")

# Updates the price of an existing product
def update_price():
    name = input("Enter product name to update price: ")
    for product in inventory:
        if name in product:
            new_price = num_positive("New price: ")
            _, quantity = product[name]
            # Replace the old tuple with a new one (tuples are immutable)
            product[name] = (new_price, quantity)
            print(f"Updated: {name} - New Price: ${new_price:.2f}, Quantity: {quantity}")
            return
    print("Product not found.")

# Deletes a product by name
def delete_product():
    name = input("Enter product name to delete: ")
    for product in inventory:
        if name in product:
            inventory.remove(product)
            print("Product deleted.")
            return
    print("Product not found.")

# Calculates the total value of all products in inventory
def calculate_total_inventory_value():
    total = 0
    for product in inventory:
        for price, quantity in product.values():
            total += price * quantity
    print(f"Total inventory value: ${total:.2f}")

# Main menu that controls the program flow
def main_menu():
    while True:
        print('-----------------------------------------------')
        print("1. Add product")
        print("2. Search product by name")
        print("3. Update product price")
        print("4. Delete product")
        print("5. Calculate total inventory value")
        print("6. Exit")
        print('-----------------------------------------------')
        choice = input("Choose an option: ")
        print('-----------------------------------------------')
        if choice == '1':
            add_product()
        elif choice == '2':
            search_product_by_name()
        elif choice == '3':
            update_price()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            calculate_total_inventory_value()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid option.")

# Run the program
main_menu()
