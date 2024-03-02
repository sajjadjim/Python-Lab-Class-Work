import tkinter as  tk

product_name =[]
product_price =[]
product_quantity =[]
product_discount=[]

product_name.append("Bananna")
product_price.append(10)
product_quantity.append(2)
product_discount.append(10)

product_name.append("Milkshake")
product_price.append(28)
product_quantity.append(2)
product_discount.append(3)

product_name.append("Kitkat")
product_price.append(70)
product_quantity.append(2)
product_discount.append(1)

product_name.append("Flower")
product_price.append(150)
product_quantity.append(2)
product_discount.append(3)

x =len(product_name)
sum =0

for i in range(x):
    price =int(product_price.pop())
    quality =float(product_quantity.pop())
    dis =int(product_discount.pop())
    cal_price =price*(dis/10)
    print(product_name.pop() + "--" +str(price) + "--" +str(quality) +"--")
    sum =sum + price * quality

print("----------!!!! Totall Price !!!!---------------")
print(sum)

