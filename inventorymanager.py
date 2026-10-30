import json
from product import Product
from inventory import Inventory

# Global constant
INVENTORY_FILE = "data/inventory.json"


# ---------------------------------------------------------------
# File handling
# ---------------------------------------------------------------
def load_inventory():
    """Load products from INVENTORY_FILE into an Inventory object."""
    inventory = Inventory()
    try:
        with open(INVENTORY_FILE, "r") as file:
            data = json.load(file)
        for item in data:
            inventory.add_product(Product.from_dict(item))
        print(INVENTORY_FILE + " found.")
        print("Inventory loaded successfully.")
    except FileNotFoundError:
        print(INVENTORY_FILE + " not found. Starting with an empty inventory.")
    except (json.JSONDecodeError, OSError, KeyError, TypeError):
        print("Could not read " + INVENTORY_FILE + ". Starting with an empty inventory.")
        inventory = Inventory()
    return inventory


def save_inventory(inventory):
    """Write the inventory to INVENTORY_FILE as JSON."""
    print("Saving inventory...")
    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(inventory.to_list(), file, indent=4)
        print("Inventory saved successfully to " + INVENTORY_FILE + ".")
        return True
    except OSError as error:
        print("Error saving inventory: " + str(error))
        return False


# ---------------------------------------------------------------
# Input helpers
# ---------------------------------------------------------------
def get_float(prompt):
    """Keep asking until the user enters a non-negative number."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Invalid input. Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int(prompt):
    """Keep asking until the user enters a non-negative whole number."""
    while True:
        try:
            value = int(float(input(prompt)))  # decimals are truncated
            if value < 0:
                print("Invalid input. Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


# ---------------------------------------------------------------
# Menu handlers
# ---------------------------------------------------------------
def handle_add(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip()
    if product_id == "":
        print("Product ID cannot be empty.")
        return
    name = input("Product Name: ").strip()
    if name == "":
        print("Product name cannot be empty.")
        return
    price = get_float("Price: ")
    stock = get_int("Stock Quantity: ")
    inventory.add_product(Product(product_id, name, price, stock))


def handle_update(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.find_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found:")
    print("Name: " + product.name)
    print("Current Stock: " + str(product.stock))
    new_stock = get_int("New Stock Quantity: ")
    inventory.update_stock(product_id, new_stock)


def handle_search(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()
    inventory.search_product(product_id)


def print_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def load_starter_products(inventory):
    """Seed three starter products when there is no saved inventory."""
    inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
    inventory.add_product(Product("P002", "Mouse", 25.50, 40))
    inventory.add_product(Product("P003", "Keyboard", 45.00, 25))


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()
    if inventory.is_empty():
        load_starter_products(inventory)
        print("Loaded 3 starter products.")

    print_menu()

    while True:
        try:
            option = input("Enter option: ").strip()
        except EOFError:
            option = "6"

        if option == "1":
            inventory.display_all()
        elif option == "2":
            handle_add(inventory)
        elif option == "3":
            handle_update(inventory)
        elif option == "4":
            handle_search(inventory)
        elif option == "5":
            save_inventory(inventory)
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()