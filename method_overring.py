class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("This is parent class")
    
class student(person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def display(self):
        print("This is child class")
        
        
p1=person('Abdullah',25)
c1=student('Nazmus',24)

p1.display()
c1.display()