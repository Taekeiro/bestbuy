from products import Product

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))  # Expected output: 12500.0
    print(mac.buy(100))  # Expected output: 145000.0
    print(mac.is_active())  # Expected output: False, because quantity reached 0

    print(bose.show())  # Expected output: "Bose QuietComfort Earbuds, Price: $250, Quantity: 450"
    print(mac.show())   # Expected output: "MacBook Air M2, Price: $1450, Quantity: 0"

    bose.set_quantity(1000)
    print(bose.show())  # Expected output: "Bose QuietComfort Earbuds, Price: $250, Quantity: 1000"

if __name__ == "__main__":
    main()