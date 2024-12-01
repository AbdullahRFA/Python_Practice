class calculation:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b=0,c=0):
        return a+b+c
    def sum(self, *args):
        return sum(args)
    
cal=calculation()
print(cal.sum(2,4))
print(cal.sum(1,2,3))

print(cal.sum(1,2,3,4,5,6,7,8,9))
