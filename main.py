# File: main.py

from products import Product
from store import Store

# Setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = Store(product_list)


def start(store):
    while True:
        # Display the menu
        print("\nStore Menu")
        print("---------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        # Get user input
        choice = input("Please choose a number: ")

        if choice == '1':
            # List all products in store
            products = store.get_all_products()
            for idx, product in enumerate(products, 1):
                print(f"{idx}. {product.show()}")

        elif choice == '2':
            # Show total quantity of items in the store
            total_quantity = store.get_total_quantity()
            print(f"Total of {total_quantity} items in store")

        elif choice == '3':
            # Make an order
            make_order(store)

        elif choice == '4':
            # Quit the program
            print("Exiting the store. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def make_order(store):
    # Get a list of all active products
    products = store.get_all_products()
    shopping_list = []

    print("\nWhen you want to finish order, enter empty text.")
    while True:
        # Display available products with indexes for selection
        for idx, product in enumerate(products, 1):
            print(f"{idx}. {product.show()}")

        # Get user choice for product
        product_choice = input("Which product # do you want? ")
        if product_choice == '':
            # Finish the order if input is empty
            break

        try:
            product_index = int(product_choice) - 1
            if product_index < 0 or product_index >= len(products):
                print("Invalid product number.")
                continue

            product = products[product_index]
            quantity_str = input("What amount do you want? ")
            quantity = int(quantity_str)

            # Add to shopping list
            shopping_list.append((product, quantity))
            print("Product added to list!")

        except ValueError:
            print("Invalid input. Please enter a valid product number and quantity.")
        except Exception as e:
            print(f"Error: {e}")

    # Process the order and calculate total cost
    if shopping_list:
        try:
            total_cost = store.order(shopping_list)
            print(f"Order made! Total payment: ${total_cost}")
        except Exception as e:
            print(f"Order failed: {e}")


if __name__ == "__main__":
    start(best_buy)
