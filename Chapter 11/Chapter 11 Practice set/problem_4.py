'''Write a class ‘Complex’ to represent complex numbers, along with overloaded
operators ‘+’ and ‘*’ which adds and multiplies them.'''

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, C2):
        return Complex(self.r + C2.r, self.i + C2.i)
    
    def __mul__(self, C2):
        real = self.r * C2.r - self.i * C2.i
        imag = self.r * C2.i + self.i * C2.r
        return Complex(real, imag)

    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
C1 = Complex(1, 2)
C2 = Complex(3, 4)
print(C1 + C2)
print(C1 * C2)