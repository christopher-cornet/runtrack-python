def calcule(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
        print(result)
    elif operator == "-":
        result = num1 - num2
        print(result)
    elif operator == "*":
        result = num1 * num2
        print(result)
    elif operator == "/":
        result = num1 / num2
        print(result)
    elif operator == "%":
        result = num1 % num2
        print(result)
    else:
        print("Choisir un opérateur valable.")

calcule(2, "*", 5)