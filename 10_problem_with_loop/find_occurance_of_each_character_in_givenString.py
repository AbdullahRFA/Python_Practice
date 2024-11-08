input_string=input("Enter the string: ")
    # """
    # The function `find_occurance` takes a string input and counts the occurrences of each character in the string, storing the results in a dictionary.
    
    # :param input_string: The code you provided takes a string input from the user and then counts the occurrences of each character in the string. It stores the character counts in a dictionary called `temp` and then prints out the dictionary
    # """

temp={}
def find_occurance(input_string):
    for x in input_string:
        if x in temp:
            temp[x]+=1
        else:
            temp[x]=1


find_occurance(input_string)
print(temp)