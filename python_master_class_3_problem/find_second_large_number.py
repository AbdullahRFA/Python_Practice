n=int(input("Enter the number of element : "))
    # """
    # The function `sum_of_all_elements` takes a list of integers, removes duplicates, sorts the unique elements, and returns the second largest element if it exists.
    
    # :param items: The code you provided takes input from the user to create a list of elements, then defines a function `sum_of_all_elements` that sorts the unique elements in the list and returns the second largest element if it exists
    # :return: The function `sum_of_all_elements` is returning the second largest element from the list of items. If the list has at least two elements, it will return the second largest element. If the list has less than two elements, it will return `None`.
    # """

items=[]

for _ in range(n):
    item=int(input())
    items.append(item)
    
    
print(items)

def sum_of_all_elements(items):
    items=sorted(set(items))
    print(items)
    return items[-2] if len(items)>=2 else None


print(sum_of_all_elements(items))