marks = {
    "Aditya" : 78,
    "Yash": 90,
    "John": 60
}

# print(marks,  type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Aditya": 90, "Steve": 100})
print(marks)

print(marks.get("Aditya"))
print(marks.get("aditya")) # prints none
print(marks.get["aditya"]) # returns, an error