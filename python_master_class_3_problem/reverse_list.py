n=int(input("Enter the number of element : "))
    # """
    # The function takes a list of numbers as input, reverses the list, and returns the sum of all elements in the list.
    
    # :param items: The 'items' list contains the elements inputted by the user. The 'reverse_list' is an empty list that will store the elements of 'items' list in reverse order. The function 'sum_of_all_elements' is intended to reverse the elements of the 'items' list and store them
    # """

items=[]

for _ in range(n):
    item=int(input())
    items.append(item)
    
reverse_list=[]
print(items)

def sum_of_all_elements(items):
    for x in items:
        reverse_list.insert(0,x)  


print(sum_of_all_elements(items))
print(reverse_list)