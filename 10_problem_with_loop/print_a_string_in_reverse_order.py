# This code snippet in Python prompts the user to enter a string and stores the input in the variable `input_string`. It then calculates and prints the length of the input string. After that, it iterates over the characters of the input string in reverse order and prints each character separated by a space.
# input_string=input("Enter a string: ")
input_string="Abdullah"

print("Lenght = ",len(input_string),"\n")

# for x in range(1,len(input_string)+1):
#     print(input_string[-x],end=(""))

for x in range(len(input_string)-1,-1,-1):
    print(input_string[x],end=(''))
    