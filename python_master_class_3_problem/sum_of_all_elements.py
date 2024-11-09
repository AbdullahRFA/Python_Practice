n=int(input("Enter the number of element : "))
    # """
    # The function calculates the sum of all elements in a list.
    
    # :param items: The `items` parameter in the code refers to a list that stores the elements inputted by the user. The elements are added to this list using a loop that iterates `n` times, where `n` is the number of elements specified by the user. The function `sum_of_all
    # :return: The function `sum_of_all_elements(items)` is returning the sum of all the elements in the `items` list.
    # """

items=[]

for _ in range(n):
    item=int(input())
    items.append(item)
    
    
print(items)

def sum_of_all_elements(items):
    return sum(items)


print(sum_of_all_elements(items))