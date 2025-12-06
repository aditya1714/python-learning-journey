'''Create a class “Programmer” for storing information of few programmers
working at Microsoft.'''

class Programmers():
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin  = pin

P = Programmers("Aditya", 12000000, "171360")
print(P.name, P.salary, P.pin, P.company)
R = Programmers("Yash", 13000000, "14546")
print(R.name, R.salary, R.pin, R.company)