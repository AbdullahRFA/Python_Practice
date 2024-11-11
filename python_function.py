# def myfunction(name):
#     print("Your name is : ",name)

# name = input("Enter Your name : ")
# myfunction("ABDULLAH NAZMUS_SAKIB")

# def sum(a,b):
#     return a+b


# a=int(input("Enter first number : " ))
# b=int(input("Enter second number : "))
    
# print(sum(a,b))
    
    
# when you dont know how many parameters you want to pass
# def touple(*khan):
#     for ab in khan:
#         print(ab)


# touple("Abdullah","Namzus","Sakib")

# default parameter
# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


# passing list as arguments

# def arg_fun(fr_name):
#     for name in fr_name:
#         print(name)
        
# fruits_name=["Apple","Banana","Orange","licci"]

# arg_fun(fruits_name)


# a function that will return a number multipling by 5

# def mulFun(n):
#     return n*5
# for i in range(10):
#     print(i,"* 5 =",mulFun(i))
# print("\n")
# for i in range(1,10,2):
#     print(i,"* 5 =",mulFun(i))
    
# def my_function(x, /):
#   print(x)

# my_function(3)





# def recursion(n):
#     return 1 if n==0 else n*recursion(n-1)
# print(recursion(5))

def myfunc(n):
    # """
    # The function sorts a list of numbers based on their distance from the number 50.
    
    # :param n: In the given code snippet, the function `myfunc(n)` calculates the absolute difference between the input `n` and the number 50. The list `thislist` contains some numbers, and it is sorted based on the key function `myfunc`, which means the numbers in the list will
    # :return: The `thislist` is being sorted based on the absolute difference between each element and the number 50. The sorted list will be `[50, 65, 23, 82, 100]`.
    # """
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) 

    
