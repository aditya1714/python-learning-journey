'''Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.'''

f = open("Chapter 9 Practice set/poem.txt")
data = f.read()
if("twinkle" in data):
    print("it's present")
else:
    print("it is not present")