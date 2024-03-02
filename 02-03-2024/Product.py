product_name =[]
product_price =[]
product_quantity =[]

product_name.append("Bananna")
product_price(10)
product_quantity(2)

x =len(product_name)
sum =0

for i in range(x):
    price =int(product_price.pop())
    quality =float(product_quantity.pop())
    #cal_price =price*(dis/10)
    print(product_name.pop() + "--" +str(price) + "--" +str(quality) +"--")
    sum =sum + price * quality

print(sum)


