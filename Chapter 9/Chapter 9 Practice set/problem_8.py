'''Write a program to make a copy of a text file “this. txt”
'''

with open("Chapter 9 Practice set/this.txt") as f:
    data = f.read()

with open("Chapter 9 Practice set/this1.txt", "a") as f:
    f.write(data)