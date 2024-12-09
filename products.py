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

class NonStockedProduct(Product):
    """Represents a product that does not require stock tracking."""

    def __init__(self, name: str, price: float):
        """Initialize non-stocked product with a name and price."""
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        """Override set_quantity to always keep quantity at zero."""
        pass

    def buy(self, quantity: int) -> float:
        """Allow unlimited purchases since stock is not tracked."""
        if quantity <= 0:
            raise ValueError("Invalid purchase quantity")
        return self.price * quantity

    def show(self) -> str:
        """Return a string representation indicating it is non-stocked."""
        return f"{self.name} (Non-Stocked), Price: {self.price}"


class LimitedProduct(Product):
    """Represents a product with a maximum purchase limit per order."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """Initialize limited product with a maximum purchase limit."""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """Override buy to enforce the maximum purchase limit."""
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of {self.name}")
        return super().buy(quantity)

    def show(self) -> str:
        """Return a string representation including the maximum limit."""
        return f"{self.name} (Limited, Max: {self.maximum}), Price: {self.price}, Quantity: {self.quantity}"