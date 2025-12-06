'''Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.'''

p = int(input("enter your marks of Physics : "))
c = int(input("enter your marks of Chemistry : "))
m = int(input("enter your marks of Maths : "))
total_percentage = (100*(p+c+m))/300

if(total_percentage>=40 and m>33%100 and c>33%100 and p>33%100 ):
    print("Excellent, you have passed the exam", total_percentage)
else:
    print("Oops, you have failed the examination", total_percentage)