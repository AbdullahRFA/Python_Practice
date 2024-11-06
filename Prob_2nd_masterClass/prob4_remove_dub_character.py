input_string=input("Enter the string : ")
    # """
    # The function `remove_dub_char` takes a string input and returns a new string with duplicate characters removed.
    
    # :param input_string: The code you provided defines a function called `remove_dub_char` that takes a string input and removes duplicate characters from it. The function iterates over each character in the input string and only adds it to the answer if it's not already present in the answer string
    # :return: The function `remove_dub_char` returns a new string where duplicate characters from the input string are removed.
    # """

def remove_dub_char(input_string):
    answer=""
    for x in input_string:
        # print(x)
        if x not in answer:
            answer+=x
    return answer

print("Resulting string is ",remove_dub_char(input_string))