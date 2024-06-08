# classes allow us to logically group our data and functions in a way that's easy
# to reuse and also easy to build upon if need be. 
# date and functions we call it here as Attributes and methods 
# method ==> Function associated with the class 

# Class and instance of class 
# class is basically a blueprint for creating the instances
'''
class Employee:
    pass
emp1 = Employee() # These are the Instances of the class 
emp2 = Employee() # Instance of the class Employee
print(emp1)  # both are having different space at memory 
print(emp2)

# Instance varibale and Class Variable 
# Instance variable contain Data that is unique to each instance 

emp1.first = 'Pankaj'
emp1.last = 'Patil'
emp1.email = 'Pankaj.patil@company.com'
emp1.pay = 100000

emp2.first = 'Test'
emp2.last = 'User'
emp2.email = 'Test.user@company.com'
emp2.pay = 200000

print(emp1.email)
print(emp2.email)

# if we create the Instance variables in this way we will not get any benefit of using classes Instead we will use the special 
# init method. 

class Employee:
    def __init__(self,first,last,pay):
        self.first = first  # emp1/emp2.first = first 
        self.first = first
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'

emp1 = Employee('pankaj','patil',100000)
emp2 = Employee('Akash','patil',200000)
# here self is pushed automatically self = emp1 and emp2 

'''

class Employee: # initiating the class 
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'

    def fullname(self):  # A method is created for the Fullname 
        return '{} {}'.format(self.first,self.last)

emp1 = Employee('pankaj','patil',100000)
emp2 = Employee('Akash','patil',200000)
#print(emp1.email)
#print(emp2.email)
print(emp1.fullname())
print(emp2.fullname()) # put the () Parentehesis on becoz its a method not an instance of the class

print(emp1.fullname())
print(Employee.fullname(emp1)) # it is same as Above but it runs in backend as it is. 

