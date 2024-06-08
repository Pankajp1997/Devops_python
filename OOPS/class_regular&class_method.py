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
# Class Methods, Regular methods and Static Methods 
# Regular methods in class automatically takes the instance as the first argument and by convention we are calling it self. 
# In order to change that means taking the class as first argument, to do this we will use the class methods and to turn a regular method into a class methods is easy to add decorators 


    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount 


    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod   # static method usually been used when we did not use the argement anywhere in the code 
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

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

#print(Employee.num_of_emps)

#Employee.set_raise_amt(1.05)
#print(Employee.raise_amount)
#print(emp1.raise_amount)
#print(emp2.raise_amount)

# Please check the output 

emp_str_1 = 'john-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
# it can also be printed using the alternative contructor above from_string 
#first, last, pay = emp_str_1.split('-')
#new_emp_1 = Employee(first,last,pay)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# static methods dont pass anything automatically, they just ben=have as Regular methods 
import datetime 
my_date = datetime.date(year=2024,month=6,day=8)

print(Employee.is_workday(my_date))



