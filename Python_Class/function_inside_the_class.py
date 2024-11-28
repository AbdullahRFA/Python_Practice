class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greatin(self):
        print(f"Hello Eveybody\nThis is {self.name} {self.age} years old")
        
        
p1=person('Abdullah Nazmus Sakib',25)
p1.greatin()
# modify object property
p1.age=24
p1.greatin()

# can delete object property using del
# del p1
# p1.greatin()
