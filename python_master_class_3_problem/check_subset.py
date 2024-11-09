list1=[1,2,3,4,4,5,5,6]
    # """
    # The function checks if all elements of list2 are present in list1.
    
    # :param list1: [1, 2, 3, 4, 4, 5, 5, 6]
    # :param list2: The function `sum_of_all_elements` checks if all elements in `list2` are present in `list1`. It returns `True` if all elements in `list2` are present in `list1`, otherwise it returns `False`
    # :return: The function `sum_of_all_elements` is returning a boolean value indicating whether all elements in `list2` are present in `list1`.
    # """
list2=[1,1,1,2,3]

def sum_of_all_elements(list1,list2):
    return set(list2).issubset(set(list1))
    # list1=set(list1)
    # list2=set(list2)
    # print(list1,list2)
    # return list2.issubset(list1)


print(sum_of_all_elements(list1,list2))
