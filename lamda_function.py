add = lambda x,y: x+y

print(add(2,4))


multi = lambda x,y : x*y

print(multi(4,5))

square = [(lambda x : x**2)(i) for i in range(1,6)]

print(square)
