# This Python code prompts the user to enter a starting number and an ending number. It then calculates the sum of all numbers from the starting number to the ending number (inclusive) using a for loop and stores the result in the variable `total_sum`. Finally, it prints out the total sum with a message indicating the range of numbers that were summed.
n=int(input("Enter starting number : "))
m=int(input("Enter Ending number : "))


total_sum=0
for x in range(n, m+1):
    total_sum+=x

print(f"Total Sum form {n} to {m} is : ",total_sum)