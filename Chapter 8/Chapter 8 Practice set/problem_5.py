'''

Write a python function to print first n lines of the following pattern:
***
**  - for n = 3
*

'''

def star(n):
    if(n==0):
        return "no stars"
    print(n * "*")
    (star(n-1))
n = int(input("enter your number : "))
star(n)