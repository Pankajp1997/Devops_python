# by using the Special mthods we will be able to change some of the built-in behaviour and the operations
#These Special Methods are always surrounded by the Double Underscrore(__)
# You may heard Dunder init then tey mean __init__
# These 2 methods (str and repr) are allow us to change how our objects are printed and dispalyed now 

class Employee:
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self): # it is an unambigious representation of the object and should be used for the debugging, logging and similar things 
        return "Employee('{}','{}', '{}' )".format(self.first, self.last, self.pay)
    
    def __str__(self): # Meant to be more of a readable representation of an object and to be used as a display to the end user 
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp1 = Employee('Pankaj','Patil', 500000)
emp2 = Employee('Akash','Patil', 100000)

#print(emp1)
#print(repr(emp1))
#print(str(emp1))

#print(emp1.__repr__())
#print(emp2.__str__())

# print(1 + 2) # At the backend it uses __add__ Special method to do th addition
#print(int.__add__(1,2))
#print(str.__add__('a','b'))

#print(len('test')) # this is also usingthe special method as __len__
#print('test'.__len__())
#print(emp1 + emp2)
# emulate Numeric Objects 
# https://docs.python.org/3/reference/datamodel.html
# https://docs.python.org/3/reference/datamodel.html

print(len(emp1))