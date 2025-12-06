''' Write a program to find out the line number where python is present from ques 6.'''

with open (r"Chapter 9 Practice set/log.html") as f:
    lines = f.readlines()
lineNo = 1
for i in lines:
    if("python" in i):
        print(f"the line number is : {lineNo}")
        break
    lineNo += 1
else:
    print("it is not present")