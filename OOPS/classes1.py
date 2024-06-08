class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1 = Employee('pankaj','patil',100000)
emp2 = Employee('Akash','patil',200000)
