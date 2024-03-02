def add_item(cart, name, price, quantity):
    cart.append({'name': name, 'price': price, 'quantity': quantity})


def remove_item(cart):
    if cart:
        return cart.pop()
    else:
        print("The cart is empty.")
        return None


def calculate_total_price(cart):
    total_price = sum(item['price'] * item['quantity'] for item in cart)
    return total_price


def print_cart_product(cart):
    for item in cart:
        print("Name:", item['name'], " Price:", item['price'], " Quantity:", item['quantity'])


cart = []

add_item(cart, "Apple", 50, 3)
add_item(cart, "Banana", 18, 12)
add_item(cart, "Milk", 28, 1)
add_item(cart, 'PineApple', 45, 2)
add_item(cart, "Chips", 25, 1)

print_cart_product(cart)

# Calculate and print total price
total_price = calculate_total_price(cart)
print("\nTotal price: ", total_price)

# Remove an item from the cart
removed_item = remove_item(cart)
if removed_item:
    print("Removed item: ", removed_item['name'])

# Print the cart after removing an item
print("\nAfter removing an item:")
print_cart_product(cart)


