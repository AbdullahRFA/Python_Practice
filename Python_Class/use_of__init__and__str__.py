class person:
    def __init__(self,name,age):
        """
        The above function is a Python constructor that initializes an object with a name and age attribute.
        
        :param name: The `__init__` method you provided is a constructor for a class that takes in two parameters, `name` and `age`, and assigns them to the instance variables `self.name` and `self.age`, respectively
        :param age: The `age` parameter in the `__init__` method is used to initialize the age attribute of an object when an instance of the class is created. It allows you to set the age of the object to a specific value when the object is instantiated
        """
        self.name=name
        self.age=age
    def __str__(self):
        """
        The `__str__` function returns a string representation of an object with its name and age attributes.
        :return: The `__str__` method is returning a string that includes the `name` and `age` attributes of the object, formatted as "{name} {age}".
        """
        return f'{self.name} {self.age}'
        
        
        
# The code snippet you provided is creating instances of the `person` class, initializing them with specific name and age attributes, and then printing out the name and age of each instance.
p1=person("Abdullah",25)
print(f'Name : {p1.name}')
print(f'Age : {p1.age}')

p2=person("Nazmus",26)
print(f'Name : {p2.name}')
print(f'Age : {p2.age}')

print(p1)
print(p2)
