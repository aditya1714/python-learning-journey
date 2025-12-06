''' Write a python program to rename a file to “renamed_by_ python.txt.'''

with open("Chapter 9 Practice set/zzen.txt") as f:
    data = f.read()

with open("Chapter 9 Practice set/renamed_by_ python.txt", "a") as f:
    f.write(data)