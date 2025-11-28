def calculate(num1, num2, operator):
    """Return the calculated value based on the operator."""
    
    if operator == "+":
        return round(num1 + num2, 3)
    elif operator == "-":
        return round(num1 - num2, 3)
    elif operator == "*":
        return round(num1 * num2, 3)
    elif operator == "/":
        return round(num1 / num2, 3)
    else:
        return None  # Invalid operator


def main():
    operator = input("Enter an operator (+ - * /): ")
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

    result = calculate(num1, num2, operator)

    if result is None:
        print(f"{operator} is not a valid operator")
    else:
        print(result)


main()
