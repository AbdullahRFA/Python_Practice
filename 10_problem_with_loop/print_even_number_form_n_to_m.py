# This Python code prompts the user to enter a starting number and an ending number. It then iterates through a range of numbers starting from the starting number up to and including the ending number. For each number in this range, it checks if the number is even (divisible by 2) using the modulo operator `%`. If the number is even, it prints the number. This code essentially prints all even numbers between the starting and ending numbers provided by the user.
n=int(input("Enter starting number : "))
m=int(input("Enter Ending number : "))

for x in range(n,m+1):
    if x%2 == 0:
        print(x,end=(" "))