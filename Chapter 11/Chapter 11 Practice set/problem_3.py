'''Create a class ‘Employee’ and add salary and increment properties to it.'''

class Employee:
    def show(self):
        print(f"the salary of the employee is {self.salary}")

a = Employee()
a.salary = 1200000
a.increment = 20