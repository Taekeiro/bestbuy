# File: main.py

from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree
from store import Store

# Setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    NonStockedProduct("Windows License", price=125),
    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

# Create promotion catalog
second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = Store(product_list)


def start(store):
    """Main function to interact with the store, displaying options for the user."""
    while True:
        print("\nStore Menu")
        print("---------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == '1':
            products = store.get_all_products()
            for idx, product in enumerate(products, 1):
                print(f"{idx}. {product.show()}")

        elif choice == '2':
            total_quantity = store.get_total_quantity()
            print(f"Total of {total_quantity} items in store")

        elif choice == '3':
            make_order(store)

        elif choice == '4':
            print("Exiting the store. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def make_order(store):
    """Handles the process of making an order from the available products in the store."""
    products = store.get_all_products()
    shopping_list = []

    print("\nWhen you want to finish order, enter empty text.")
    while True:
        for idx, product in enumerate(products, 1):
            print(f"{idx}. {product.show()}")

        product_choice = input("Which product # do you want? ")
        if product_choice == '':
            break

        try:
            product_index = int(product_choice) - 1
            if product_index < 0 or product_index >= len(products):
                print("Invalid product number.")
                continue

            product = products[product_index]
            quantity_str = input("What amount do you want? ")
            quantity = int(quantity_str)

            shopping_list.append((product, quantity))
            print("Product added to list!")

        except ValueError:
            print("Invalid input. Please enter a valid product number and quantity.")
        except Exception as error:
            print(f"Error: {error}")

    if shopping_list:
        try:
            total_cost = store.order(shopping_list)
            print(f"Order made! Total payment: ${total_cost}")
        except Exception as error:
            print(f"Order failed: {error}")


if __name__ == "__main__":
    start(best_buy)
