input_string=input("Enter the string : ")
    # """
    # The function `extract_file_name` takes a string input containing a file path and returns the file name extracted from the path.
    
    # :param input_string: The `input_string` is the string that the user enters when prompted. This string can contain a file path with directories separated by slashes ("/"). The function `extract_file_name` takes this input string and extracts the file name from the end of the path
    # :return: The function `extract_file_name` is returning the file name extracted from the input string.
    # """

def extract_file_name(input_string):
    temp=input_string.split('/')
    # print(temp)
    return temp[-1]
    
    
    

print("File name is ",extract_file_name(input_string))