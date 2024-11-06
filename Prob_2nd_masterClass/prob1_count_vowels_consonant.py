# This Python code snippet takes a string input from the user, converts it to lowercase, and then counts the number of vowels and consonants in the input string.
input_string=input("Enter a string: ")
input_string=input_string.lower()
vowels=['a','e','i','o','u']
vowels_count=0
consonant_count=0
for x in input_string:
    if x in vowels:
        vowels_count+=1
    else:
        consonant_count+=1

print("Length of the string: ",len(input_string))
print("Number of vawels: ",vowels_count)
print("NUmber of Consonant: ",consonant_count)
