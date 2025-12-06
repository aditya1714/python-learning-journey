'''
Write a recursive function to calculate the sum of first n natural numbers.
'''

def naturalNum(n):
    if(n==0):
        return 0
    return n + naturalNum(n-1)

n = int(input("enter your number : "))
print(f"the sum of {n} natural number is : {naturalNum(n)}")