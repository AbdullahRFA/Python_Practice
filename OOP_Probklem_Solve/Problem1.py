import math

"""
Class representing a circle with a given radius.

This class provides methods to calculate the area and perimeter of the circle. 
The area and perimeter are printed in a formatted manner.

Attributes:
    radius (float): The radius of the circle.

Methods:
    area():
        Calculates and prints the area of the circle.
    
    perimeter():
        Calculates and prints the perimeter of the circle.
"""
class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        area_of_circle = math.pi * self.radius
        print(f"Area of the circle : {area_of_circle:.6}")
    def perimeter(self):
        perimeter_of_circle = 2 * math.pi * self.radius
        print(f"Perimeter of the cicle : {perimeter_of_circle:.6}")

circle = Circle(10)
circle.area()    
circle.perimeter()
    