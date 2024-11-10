students={'name':'Abdullah','Roll':383,'dept':'CSE'}
    # """
    # The code snippet defines a function to calculate the sum of input values and demonstrates dictionary operations, including iteration, updating, and comprehension.
    # :return: The function SUM(*take) is returning a tuple containing the values (1, 2, 3, 4, 5) when called with those arguments.
    # """

for key in students:
    print(key,end=(' '))
    
print(' \n\n')
    
for value in students.values():
    print(value,end=(' '))
    
print(' \n\n')
 
for key, value in students.items():
     print(key, ' : ',value)   


student_info={'name':'Alamin', 'age':'24','roll':382}
student_info2={'Blood Group':'A+','dept':'CSE'}

print(' \n\n')
print(student_info)
print(' \n\n')
print(student_info2)

print(' \n\n')
student_info.update(student_info2)
print(student_info)

print(' \n\n')
for key,value in student_info.items():
    print(key,' : ',value)
    
students.clear()
for value in students.values():
    print(value,end=(' '))
    
    
square={x:x**2 for x in range(1,5)}
print('\n Squre from 0 to N ]\n')

for key,value in square.items():
    print(key,' : ',value)
    
    
def SUM(*take):
    return (take)

items=SUM(1,2,3,4,5)

print(items)
