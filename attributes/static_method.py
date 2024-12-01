class person:
    counter=0 #Class variable/attributes
    def __init__(self,name,dept):
        self.name=name #instance attributes
        self.dept = dept #instance attributes
        person.counter+=1 #class attributes increase by 1
        self.count = person.counter #instance attributes
    def display(self):
        print(f"Name : {self.name}")
        print(f"Department : {self.dept}")
        print(f"Employee NO : {self.count}")
    # static method that does not need instance to be called
    @staticmethod
    def show_employee():
        print(f"\nNumber of employee : {person.counter}")
        
        
p1=person('Abdullah','CSE')
p2=person('Nazmus','IIT')
p3=person('Sakib','Robotics')

p1.display()
print()
p2.display()
print()
p3.display()

person.show_employee()


