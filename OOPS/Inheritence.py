# Inheritence allows us to inherite the attributes and the Methods from a parent class 
#  we can create a subclass and modify it without affecting the parent class.

class Employee:
    raise_amt = 1.04 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee): # Developer subClass have all the attributes and the Methods 
    raise_amt = 1.10 
# The raise_amt is a Class variable and we customized it according our way 
# sometimes we wanted subclasses to have more information than parent class can handle,IF we also wanted to pass language Dev Knows , we can 
# give it a Special __init__ method 

    def __init__(self, first, last, pay, prog_lang):
        # We want first, last and Pay should be handlled by the Employee class and Only the Prog_lang by developer we can use below 
        super().__init__(first, last, pay) # pass the inofrmation to the Employee Class
        #Employee.__init__(self,first,last,pay) # we can do in this way as well
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('--->',emp.fullname())

dev_1 = Developer('Pankaj','Patil',100000,'Python')
dev_2 = Developer('Tejasvi','Sul',200000,'java')

#print(help(Developer)) # Shows the All information about the Class from where it is inherited and all  

#print(dev_1.email)
#print(dev_1.prog_lang)
#dev_2.apply_raise()
#print(dev_2.pay)

mgr_1 = Manager('sue','Smith',90000,[dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_1)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()

# pythin has a two Attributes isinstance and isclass 
# isinstance() will tell us if an object is an instance of a class 
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,Developer))

# issubclass will tell us if a class is a subclass of another 
print(issubclass(Manager,Employee)) 
print(issubclass(Manager,Developer)) 



