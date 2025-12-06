name = "aditya"

print(name[0:4])
print(name[-5: -1])
print(name[1: 5])

print(name[:4]) # if the start index has given no value it will be considered as 0 [0:4]
print(name[1:]) # if the end index has given no value it will be considered as its full length [1:6]
print(name[1:6])

#skiping slice

print(name[0:5:3]) 