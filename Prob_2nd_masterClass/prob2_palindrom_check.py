# # This Python code snippet checks if a given input string is a palindrome or not. Here's a breakdown of what the code does:
# input_string=input("Enter The String: ")
# input_string=input_string.lower()
# # reverse the string
# plm_string=input_string[::-1]
# # print(plm_string)

# if(plm_string==input_string):
#     # print("{} is palindrom".format(input_string))
#     print(f"{input_string} is palindrom")
# else:
#     print(f"{input_string} is not palindrom")


input_string=input("Enter the string: ")


def is_palindrom(str):
    return input_string==str[::-1]

if is_palindrom(input_string):
    print(f"{input_string} is palindrom")
else:
    print(f"{input_string} is not palindrom")
