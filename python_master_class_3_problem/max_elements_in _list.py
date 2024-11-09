n=int(input("Enter the number of element : "))
    # """
    # The function finds and returns the maximum value from a list of elements.
    
    # :param items: The `items` list contains the elements inputted by the user. The `sum_of_all_elements` function is designed to return the maximum value in the `items` list
    # :return: The function `sum_of_all_elements(items)` is returning the maximum value from the list of items.
    # """

items=[]

for _ in range(n):
    item=int(input())
    items.append(item)
    
    
print(items)

def sum_of_all_elements(items):
    return max(items)


print(sum_of_all_elements(items))