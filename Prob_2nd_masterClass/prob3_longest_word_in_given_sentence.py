input_string=input("Enter the sentence : ")
    # """
    # The function `max_length_word` takes a sentence as input and returns the longest word in the sentence.
    
    # :param input_string: The `input_string` is the sentence that the user will input when prompted. The function `max_lenth_word` takes this input string, splits it into individual words, and then returns the longest word in the sentence. Finally, the program prints out the longest word found in the sentence entered by
    # :return: The function `max_length_word(input_string)` returns the longest word in the input sentence provided by the user.
    # """

def max_lenth_word(input_string):
    words=input_string.split()
    return max(words,key=len)

answer=max_lenth_word(input_string)
print(f"{answer} is the longest word")


