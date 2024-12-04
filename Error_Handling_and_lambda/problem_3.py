'''
This Python script demonstrates the use of functional programming techniques like map(), filter(), 
and sorted() with lambda functions to manipulate a list of integers. The script solves three specific tasks on a predefined list of numbers.

Key Components
1. List Initialization
Creates a list numbers containing both positive and negative integers
Contains 10 elements ranging from -10 to 9
2. Square of Elements
Uses map() with a lambda function to square each element
Transforms the original list by applying x ** 2 to each number
Stores result in square_all_elements
3. Positive Number Filtering
Employs filter() with a lambda function to extract positive numbers
Selects only elements greater than zero
Stores result in positive_number
4. Absolute Value Sorting
Utilizes sorted() with a lambda function as the key
Sorts the list based on the absolute value of each number
Stores result in sorted_list
Purpose
The script serves as a practical demonstration of lambda functions and functional programming techniques in Python, showing how to:

Transform lists
Filter list elements
Sort lists using custom criteria
'''


# Given List
numbers = [1,-2,3,-4,5,-6,7,-8,9,-10]
#  Q-1
square_all_elements = list(map(lambda x:x ** 2,numbers))
print("Square of all elements = ",square_all_elements)

# Q-2
positive_number = list(filter(lambda x: x > 0,numbers))
print("All positive number = ",positive_number)

#  Q-3
sorted_list = list(sorted(numbers, key=lambda x: abs(x)))
print("Sorted List based on their abs value = ",sorted_list)