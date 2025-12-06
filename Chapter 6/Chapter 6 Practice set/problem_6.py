'''Write a program to calculate the grade of a student from his marks from the
following scheme:'''

'''     90 – 100 => Ex
        80 – 90 => A
        70 – 80 => B
        60 – 70 =>C
        50 – 60 => D
        <50 => F        '''


a = int(input("enter your marks : "))

if(a<=100 and a>90):
    grade = "Ex"
if(a<=90 and a>80):
    grade = "A"
if(a<=80 and a>70):
    grade = "B"
if(a<=70 and a>60):
    grade = "C"
if(a<=60 and a>50):
    grade = "D"
if(a<50):
    grade = "F"

print("Your Grade is : ", grade)