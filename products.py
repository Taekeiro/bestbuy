# File: products.py

class Product:
    """Represents a product with a name, price, quantity, and active status."""

    def __init__(self, name: str, price: float, quantity: int):
        """Initialize product with name, price, quantity, and active status."""
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid values for name, price, or quantity")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Set the quantity of the product, deactivating if quantity reaches zero."""
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """Buy a specified quantity of the product and return the total cost."""
        if not self.active or quantity > self.quantity or quantity <= 0:
            raise ValueError("Invalid purchase quantity")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity
