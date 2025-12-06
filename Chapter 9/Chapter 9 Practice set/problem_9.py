'''Write a program to find out whether a file is identical & matches the content of
another file.'''

with open("Chapter 9 Practice set/this.txt")as f :
    data = f.read()

with open("Chapter 9 Practice set/this1.txt")as f :
    data1 = f.read()

if (data==data1):
    print("these are identical")
else:
    print("these are not identical")