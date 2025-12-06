'''Write a program which finds out whether a given name is present in a list or not.'''

a = {"aditya", "yash", "kishu", "Siwani", "Ananya", "Muskan", "Piyush", "Keshav"}

name = input("enter the name : ")
if name in a:
    print("welcome")
else:
    print("username do not exist")