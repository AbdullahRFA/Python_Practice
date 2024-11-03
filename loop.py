# 	1.	Iterating over a list:
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
    
print("\n")

# 2.	Using range() with for:
for i in range(5):  # This will run from 0 to 4
    print(i)

print("\n")
# 3. Using for with a dictionary:
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(key, ":", value)
    
print("\n")
# 1.	Basic while loop:
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count

print("\n")
# 	2.	Using while with user input:
# while True:
#     answer = input("Type 'exit' to stop: ")
#     if answer == "exit":
#         break

print("\n")
# 1.	break Statement:
# •	Exits the loop prematurely when a condition is met.
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

print("\n")
	# 2.	continue Statement:
	# •	Skips the current iteration and moves to the next one.
for i in range(5):
     if i == 3:
        continue  # Skip this iteration when i is 3
     print(i)
 
print("\n")
# 3.	else with Loops:
# •	An else block in a loop executes after the loop completes normally (without break).
for i in range(3):
    print(i)
else:
    print("Loop finished without break")

print("\n")

squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, ..., 81]
print("\n")

# 5. While Loop with else

# Similar to for loops, while loops can also have an else block.
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop finished without a break.")