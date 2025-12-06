'''What will be the length of following set s:'''
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

#output will be 2 because 20.0 is equal to 20

print(len(s))