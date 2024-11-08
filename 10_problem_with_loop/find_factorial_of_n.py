# This Python code calculates the factorial of a given number. 
# - The user is prompted to enter a number.
# - The code then initializes a variable `result` to 1.
# - It then iterates through a loop from 1 to the entered number (inclusive) and multiplies each number to the `result` variable.
# - Finally, it prints out the factorial of the entered number.
n=int(input("Enter the number: "))
result=1
for i in range(1,n+1):
    result*=i
    
print("Factorial of ",n," is = ",result)