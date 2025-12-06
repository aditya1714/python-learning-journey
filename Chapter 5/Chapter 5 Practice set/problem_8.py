'''If languages of two friends are same; what will happen to the program in problem 6? '''

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

# nothing will happen it will show the same language for 2 friends 
# because name is using as a identifer thats why only value can be change because of the   .update method