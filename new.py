# This Python code snippet is demonstrating how to create two new lists (`temp_list1` and `temp_list2`) by adding 1 to each element in the original list `numbers=[1,2,3,4,5]`.
numbers=[1,2,3,4,5]

temp_list1=[]
temp_list2=[]

# using for loop
for x in numbers:
    temp_list1.append(x+1)

print(temp_list1)


# using while loop
i=0
while i<len(numbers):
    temp_list2.append(numbers[i]+1)
    i+=1

print(temp_list2)