input_string=input("Enter the string : ")
    # """
    # The function `count_occurance` takes a string as input, counts the occurrences of each word (case-insensitive), and returns a dictionary with the word frequencies.
    
    # :param input_string: The code you provided prompts the user to enter a string, then it defines a function `count_occurance` that takes the input string, converts it to lowercase, splits it into words, and counts the occurrences of each word in a dictionary. Finally, it prints out the dictionary with word frequencies
    # :return: The function `count_occurance` returns a dictionary where the keys are the unique words in the input string (case-insensitive) and the values are the number of times each word appears in the string.
    # """

def count_occurance(input_string):
    input_string=input_string.lower()
    temp_string=input_string.split()
    track={}
    
    for x in temp_string:
        if x in track:
            track[x] +=1
        else:
            track[x]=1
            
    return track

answer=count_occurance(input_string)

print(answer)