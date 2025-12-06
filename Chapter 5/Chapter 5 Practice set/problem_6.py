'''Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.'''

s = {}
name = input("enter your name : ")
lang = input("enter your language name : ")
s.update({name : lang})
name = input("enter your name : ")
lang = input("enter your language name : ")
s.update({name : lang})
name = input("enter your name : ")
lang = input("enter your language name : ")
s.update({name : lang})
name = input("enter your name : ")
lang = input("enter your language name : ")
s.update({name : lang})

print(s)