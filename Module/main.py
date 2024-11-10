# This code snippet is importing a module named `mathe_operations` using the alias `math_op`. The module likely contains functions for mathematical operations such as Summation, Subtraction, Multiplication, Division, and Remainder.
import mathe_operations as math_op

a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))

print(f'Sum of {a} and {b} = ',math_op.Summation(a,b))
print(f'Substruction of {a} and {b} = ',math_op.Subtruction(a,b))
print(f'Multiplication of {a} and {b} = ',math_op.Multiplication(a,b))
print(f'Division of {a} and {b} = ',math_op.Division(a,b))
print(f'Remainder of {a} and {b} = ',math_op.Remainder(a,b))