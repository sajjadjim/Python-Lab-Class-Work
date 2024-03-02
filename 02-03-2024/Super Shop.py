def add_item_on_cart(cart, name_item , price_item , quantity_item):
    cart.append({'name': name_item, 'price': price_item, 'quantity': quantity_item})


def  calculate_the_Price(cart):
    totall_price= sum(product['price'] * product['quantity']  for product in cart )
    return totall_price

def remove_cart(cart):
    if cart:
        return cart.pop()
    else:
        print("No product on your Cart !!!!")
        return None

def print_items(cart):
    for item in cart :
        print("Name of item -" ,item['name'] ," Price -" ,item['price']  ," Quantity -",item['quantity'])


cart = []
add_item_on_cart(cart,"Apple", 100 , 2 )
add_item_on_cart(cart, "Chips" ,50 , 1 )
add_item_on_cart(cart ,"Bananna" , 7 , 15 )
add_item_on_cart(cart , "Pineapple" , 45 , 3)
add_item_on_cart(cart , "Oil" ,180 ,5)

totall_price =calculate_the_Price(cart)

print_items(cart)
print("\nShopping Totall Bill :",totall_price)

remove_item =remove_cart(cart)
print("Remove item Name -",remove_item['name'])


### AFter Remove Item Print
print("\n")
print_items(cart)
















