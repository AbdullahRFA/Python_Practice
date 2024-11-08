number = int(input("Enter the number : "))
    # """
    # This Python function determines whether a given number is prime or not.
    
    # :param number: The `number` variable is an integer input by the user. The code then defines a function `prime(number)` that checks if the input number is a prime number or not. The function returns `True` if the number is prime and `False` if it is not prime
    # :return: The function `prime(number)` returns `True` if the input number is a prime number, and `False` if it is not a prime number.
    # """

def prime(number):
    if number<=1:
        return False
    for x in range(2,int(number**0.5)+1):
        if number%x==0:
            return False
    return True


if prime(number):
    print("Prime")
else:
    print('Not Prime')