class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(f'First Name : {self.fname}')
        print(f'Last Name : {self.lname}')
    
# The class `student` is defined as a subclass of `person` in Python.
class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationYear=2026
        
    def welcome(self):
        print(f"Welcome {self.fname}{self.lname} graduation year {self.graduationYear}")

fname=input("Enter First Name : ")
lname=input("Enter Last Name : ")
st=student(fname,lname)

# print(st.display())
# print(st.welcome())
st.display()
st.welcome()
        