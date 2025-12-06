'''If the names of 2 friends are same; what will happen to the program in problem 6?'''

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

#it will update the value as we're using .update method