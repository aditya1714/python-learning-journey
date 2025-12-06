with open ("Chapter 9 Practice set/log.html") as f:
    data = f.read()

if("python" in data):
    print("it is present")
else:
    print("it is not present")