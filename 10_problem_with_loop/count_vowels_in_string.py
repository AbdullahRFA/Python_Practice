# This code snippet is counting the number of vowels in the string 'education'. It first converts the string to lowercase, then iterates through each character in the string. If the character is a vowel (a, e, i, o, u), it increments the count and prints the vowel. Finally, it prints the total count of vowels found in the string.
 # input_string=input("Enter the string : ")
# input_strin='education'
# input_strin=input_strin.lower()
# count=0
# vowels=['a','e','i','o','u']
# for x in range(0,len(input_strin)):
#     if input_strin[x] in vowels:
#         count+=1
#         print(input_strin[x],end=(' '))

# print("vowels : ",count)


# This code snippet is counting the number of vowels in the string 'education'. 
# 1. It first converts the string to lowercase using the `lower()` method.
# 2. It then iterates through each character in the string.
# 3. If the character is a vowel (a, e, i, o, u), it increments the count and prints the vowel.
# 4. Finally, it prints the total count of vowels found in the string.
name='education'
name=name.lower()

vowels='aeiou'
count=0
for x in name:
    if x in vowels:
        count+=1
        print(x,end=(' ,'))

print(" vawels = ",count) 