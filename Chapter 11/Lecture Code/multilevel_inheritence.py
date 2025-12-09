class intern:
    a = 1

class programmer(intern):
    b = 2

class student(programmer):
    c = 3

o = intern()
print(o.a)
# print(o.b)  # error shown becaouse there is no (b) attribute in intern class

o = programmer()
print(o.a, o.b)
# print(o.a, o.b, o.c)  # error shown becaouse there is no (c) attribute in programmer class

o = student()
print(o.a, o.b, o.c) # everthing showed because student class contain all (a, b, c) attributes.