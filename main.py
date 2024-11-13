# File: main.py
from products import Product
from store import Store

def main():
    # Create a list of products
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Initialize the store with the product list
    store = Store(product_list)

    # Fetch all active products in the store
    products = store.get_all_products()

    # Display the total quantity of all products in the store
    print(store.get_total_quantity())  # Expected output: 850

    # Place an order for multiple products and display the total cost
    print(store.order([(products[0], 1), (products[1], 2)]))  # Expected output: 1950.0

if __name__ == "__main__":
    main()
