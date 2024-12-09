from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """Calculate the price after applying the promotion."""
        pass


class PercentDiscount(Promotion):
    """Promotion: Apply a percentage discount."""

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """Promotion: Second item at half price."""

    def apply_promotion(self, product, quantity: int) -> float:
        # Calculate pairs and remaining items
        pairs = quantity // 2
        remaining = quantity % 2
        return product.price * (pairs * 1.5 + remaining)


class ThirdOneFree(Promotion):
    """Promotion: Buy 2, get 1 free."""

    def apply_promotion(self, product, quantity: int) -> float:
        # Calculate groups of three and remaining items
        groups_of_three = quantity // 3
        remaining = quantity % 3
        return product.price * (groups_of_three * 2 + remaining)
