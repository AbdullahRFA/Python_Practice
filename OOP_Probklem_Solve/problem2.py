import math
class shape:
    def __init__(self):
        pass
    def area(self):
        pass
    def perimeter(self):
        pass
    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area_of_circle = math.pi * self.radius ** 2
        print(f"Area of the circle : {area_of_circle:.6f}")
    def perimeter(self):
        perimeter_of_circle = 2 * math.pi * self.radius
        print(f"Perimeter of the circle : {perimeter_of_circle:.6f}")

class triangle(shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a +  self.b + self.c)/2
        area_of_the_triangle = math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))
        print(f"Area of the triangle : {area_of_the_triangle:.6f}")
        
    def perimeter(self):
        perimeter_of_the_triangle =  self.a +  self.b + self.c
        print(f"Perimeter of the triangle : {perimeter_of_the_triangle:.6f}")       
        
class square(shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        
        area_of_the_squre = self.side ** 2
        print(f"Area of the square : {area_of_the_squre:.6f}")
        
    def perimeter(self):
        perimeter_of_the_squre =  self.side * 4
        print(f"Perimeter of the square : {perimeter_of_the_squre:.6f}")       
        
        
c1 = circle(10)
c1.area()
c1.perimeter()
print()
t1=triangle(2,3,4)
t1.area()
t1.perimeter()
print()
sq=square(10)
sq.area()
sq.perimeter()