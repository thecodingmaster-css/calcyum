
def Calculator():
    try:
        num1 = float(input("Number 1: "))
        op = input("Operator: ")
        num2 = float(input("Number 2: "))

        if op == "*" or "x":
            res = num1 * num2
        elif op == "/":
            res = num1 / num2
        elif op == "+":
            res = num1 + num2
        elif op == "-":
            res = num1 - num2
        else:
            print("Please Enter A Valid Operator.")
        return res
    except ValueError:
        print("Please enter a float value (Number value)")
