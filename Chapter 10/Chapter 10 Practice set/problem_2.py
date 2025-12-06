'''Write a class “Calculator” capable of finding square, cube and square root of a number.'''

n = int(input("enter your number : "))

class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {n} = {self.n*self.n}")

    def square_root(self):
        print(f"The square root of {n} = {self.n**0.5}")

    def cube(self):
        print(f"The cube of {n} = {self.n*self.n*self.n}")

a = calculator(n)
a.square()
a.square_root()
a.cube()