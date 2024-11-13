# File: store.py
from typing import List, Tuple
from products import Product

class Store:
    def __init__(self, products: List[Product] = None):
        # Initialize with a list of products or an empty list if none provided
        self.products = products if products else []

    def add_product(self, product: Product):
        # Add a new product to the store's product list
        self.products.append(product)

    def remove_product(self, product: Product):
        # Remove a product from the store's product list
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        # Calculate the total quantity of all products in the store
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        # Return a list of all active products in the store
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        # Process an order based on a shopping list of (Product, quantity) tuples
        total_price = 0.0
        for product, quantity in shopping_list:
            if not product.is_active():
                raise Exception(f"{product.name} is not available for purchase.")
            try:
                total_price += product.buy(quantity)
            except Exception as e:
                # If there's an error (e.g., not enough stock), raise the exception
                raise Exception(f"Error processing order for {product.name}: {str(e)}")
        return total_price
