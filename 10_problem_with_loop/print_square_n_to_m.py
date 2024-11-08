# This Python code prompts the user to enter a starting number and an ending number. It then iterates through a range of numbers starting from the starting number up to and including the ending number. For each number in this range, it calculates the square of the number using the exponentiation operator `**` and prints the result with a space as the separator.
n=int(input("Enter starting number : "))
m=int(input("Enter Ending number : "))

for x in range(n,m+1):
    # print(x*x, end=(" "))
    print(x**2, end=(" "))