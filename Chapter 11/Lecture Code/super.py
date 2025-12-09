class intern:
    def __init__(self):
        print("constructor of intern")
    a = 1

class programmer(intern):
    def __init__(self):
        print("constructor of programmer")
    b = 2

class student(programmer):
    def __init__(self):
        super().__init__() # this will the run the parent construtor which is the "constructor of programmer"
        print("constructor of student")
    c = 3

# o = intern()
# print(o.a)

# o = programmer()
# print(o.a, o.b)

o = student()
print(o.a, o.b, o.c)