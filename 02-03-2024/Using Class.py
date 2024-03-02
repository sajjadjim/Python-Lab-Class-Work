class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, name, price, quantity):
        self.cart.append({'name': name, 'price': price, 'quantity': quantity})

    def remove_item(self):
        if self.cart:
            return self.cart.pop()
        else:
            print("The cart is empty.")
            return None

    def calculate_total_price(self):
        total_price = sum(item['price'] * item['quantity'] for item in self.cart)
        return total_price

    def print_cart_product(self):
        for item in self.cart:
            print("Name:", item['name'], " Price:", item['price'], " Quantity:", item['quantity'])

    def apply_discount(self, discount_percentage):
        total_price = self.calculate_total_price()
        discount_amount = total_price * (discount_percentage / 100)
        discounted_price = total_price - discount_amount
        return discounted_price


# Create a ShoppingCart instance
cart = ShoppingCart()

# Add items to the cart
cart.add_item("Apple", 50, 3)
cart.add_item("Banana", 18, 12)
cart.add_item("Milk", 28, 1)
cart.add_item('PineApple', 45, 2)
cart.add_item("
