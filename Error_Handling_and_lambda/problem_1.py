'''
Overview
This Python script implements a robust division function with comprehensive error handling, 
designed to safely perform division operations while gracefully managing potential input and mathematical errors.

Key Components
division() Function
Handles user input for two numbers
Performs division with multiple error handling mechanisms
Catches and manages two specific exceptions:
ZeroDivisionError: Prevents division by zero
ValueError: Ensures only integer inputs are accepted
Error Handling Strategy
Uses try/except/else block for structured exception management
Provides user-friendly error messages for different input scenarios
Allows continuous operation through an infinite while loop
Key Features
Interactive input for division operation
Safe integer conversion
Graceful error reporting
Continuous execution until manually stopped
The script demonstrates defensive programming techniques by anticipating and handling potential runtime errors during a simple division operation.

'''

def division():
    
    try:
        first = int(input("Enter First Number : "))
        second = int (input("Enter Second Number : "))
        result = first / second
        print(f"Result = {result}")
    except ZeroDivisionError:
        print("Something divided ZERO is not allow")
    except ValueError:
        print("Only integer value is allowd")
    else:
        print("Programe closed Successfully")
        
        
while True:
    check=division()
        