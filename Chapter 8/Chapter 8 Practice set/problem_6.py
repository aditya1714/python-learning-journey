'''Write a python function which converts inches to cms.'''

def inch_to_cms(n):
    return n * 2.54
n = float(input("enter the inches : "))
x = inch_to_cms(n)
print(f"{round(x, 2)}")