# File: store.py

from typing import List, Tuple
from products import Product

class Store:
    """Represents a store containing a collection of products."""

    def __init__(self, products: List[Product]):
        """Initialize the store with a list of products."""
        self.products = products

    def add_product(self, product: Product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products if product.is_active())

    def get_all_products(self) -> List[Product]:
        """Return a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Process an order for multiple products and return the total price."""
        total_price = 0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except ValueError as error:
                raise ValueError(f"Failed to order {product.name}: {error}")
        return total_price
