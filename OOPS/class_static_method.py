class Employee: # initiating the class 
    raise_amount = 1.04 # applying the class variable here 
    num_of_emps = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1 
    def fullname(self):  # A method is created for the Fullname 
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount )

emp1 = Employee('pankaj','patil',100000)
emp2 = Employee('Akash','patil',200000)

#print(emp1.pay)
#emp1.apply_raise()
#print(emp1.pay)

#print(emp1.__dict__) # shows the values it will return 
#print(Employee.__dict__) # shows the Values It will gives 

#print(Employee.raise_amount)
#print(emp1.raise_amount)
#print(emp2.raise_amount)

#emp1.raise_amount = 1.05

#print(emp1.__dict__)
#print(Employee.__dict__)

# See above Only the emp1 attribute is changed but all the attributes from Employee is remain unchanged 

print(Employee.num_of_emps)
