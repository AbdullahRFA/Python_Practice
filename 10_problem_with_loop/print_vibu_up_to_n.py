# This Python code is generating the Fibonacci sequence up to the nth term specified by the user.

n=int(input('Enter the nth term : '))

a=0
b=1
for _ in range(n):
    print(a,end=(' '))
    a,b=b,a+b
    
   