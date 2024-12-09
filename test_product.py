import pytest
from products import Product


def test_creating_prod():
    """Test that creating a product with valid details works."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True


def test_create_product_invalid_details():
    """Test that creating a product with invalid details raises an exception."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)  # Empty name

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)  # Negative price

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=1450, quantity=-5)  # Negative quantity


def test_product_becomes_inactive():
    """Test that when a product reaches zero quantity, it becomes inactive."""
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.set_quantity(0)
    assert product.is_active() is False


def test_buy_modifies_quantity():
    """Test that purchasing a product modifies its quantity and returns the correct total price."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_cost = product.buy(10)  # Buy 10 units
    assert total_cost == 14500  # 10 * 1450
    assert product.quantity == 90  # Quantity reduced to 90
    assert product.is_active() is True


def test_buy_too_much():
    """Test that buying more than available quantity raises an exception."""
    product = Product("MacBook Air M2", price=1450, quantity=5)
    with pytest.raises(ValueError):
        product.buy(10)  # Attempt to buy 10 units when only 5 are available
