number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

# Convert number1 to float if it contains a decimal point, otherwise to int
if '.' in number1:
    number1 = float(number1)
else:
    number1 = int(number1)

# Convert number2 to float if it contains a decimal point, otherwise to int
if '.' in number2:
    number2 = float(number2)
else:
    number2 = int(number2)

operator = input("Enter the operator (+, -, *, /, %): ")
operators = ["+", "-", "*", "/", "%"]

# Validate the operator input
while operator not in operators:
    print("Operator is not valid. Please enter one of (+, -, *, /, %).")
    operator = input("Enter the operator: ")
message="The result is:"
# Handle division by zero for / and % operators
if (operator == "/" or operator == "%") and number2 == 0:
    print("Division or modulus by zero is not allowed.")
else:
    # Perform the operation based on the operator input
    if operator == "+":
        print(message, number1 + number2)
    elif operator == "-":
        print(message, number1 - number2)
    elif operator == "*":
        print(message, number1 * number2)
    elif operator == "/":
        print(message, number1 / number2)
    elif operator == "%":
        print(message, number1 % number2)