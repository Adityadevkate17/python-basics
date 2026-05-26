# Create Employee class with salary attribute. 

class Employee:
    def __init__(self, salary):
        self.salary = salary 

Employee = Employee(50000)
print(Employee.salary)