'''Write a program using functions to find greatest of three numbers.'''

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    if (c>a and c>b):
        return c
a = int(input("enter your 1st number : "))
b = int(input("enter your 2nd number : "))
c = int(input("enter your 3rd number : "))
print(f"the greatest number is : {greatest(a, b, c)}")