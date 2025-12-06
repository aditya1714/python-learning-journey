f = open("Lecture Code/file.txt")
data = f.read()
print(data)
f.close()

# this same can be written using with statement,

with open("Lecture Code/file.txt")as f :
    print(f.read())

# now you don't have to use .close() .