n=int(input("Enter the number of element : "))
    # """
    # The function calculates the number of even and odd elements in a list.
    
    # :param items: The `items` parameter in the code represents a list of integers. The code prompts the user to enter the number of elements in the list and then proceeds to take input for each element and store them in the `items` list. The `sum_of_all_elements` function calculates the count of even
    # :return: The function `sum_of_all_elements` is returning a tuple containing the count of even numbers and the count of odd numbers in the list `items`.
    # """

items=[]

for _ in range(n):
    item=int(input())
    items.append(item)
    
    
print(items)

def sum_of_all_elements(items):
    even=sum(1 for x in items if x%2==0)
    odd=len(items)-even
    return even, odd

print(sum_of_all_elements(items))