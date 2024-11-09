n=int(input("Enter the number of element : "))
    # """
    # The function `sum_of_all_elements` returns a list of unique elements from the input list.
    
    # :param items: The `items` variable is a list that stores the elements inputted by the user. The function `sum_of_all_elements(items)` is designed to return a list containing unique elements from the input list `items`
    # :return: The function `sum_of_all_elements` is returning a list containing only the unique elements from the input list `items`.
    # """

items=[]

for _ in range(n):
    item=int(input())
    items.append(item)
    
    
print(items)

def sum_of_all_elements(items):
    return list(set(items))


print(sum_of_all_elements(items))