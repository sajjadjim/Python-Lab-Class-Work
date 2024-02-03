def calculator(num1 , num2, op):
    if op== '+':
        result = num1+num2
    elif op== '-':
        result =num1 -num2
    elif op== '*':
        result =num1  * num2
    elif op == '/':
        result = num1 / num2
    else:
        print("Invalid Operation !!..........")
    return result

c = True
while c is True:
    operator =input("Select the operator which you want (+ , - , * , / ) :")
    num1 = float(input("Input your first number :"))
    num2 = float(input("Input your second number :"))

    result =calculator(num1, num2, operator)
    print(num1 , operator , num2 , "=" , result)

    condition = input("Yes or No :")
    if condition =='No':
        c = False