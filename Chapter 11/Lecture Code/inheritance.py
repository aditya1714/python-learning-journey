class intern:
    company = "Apple"
    def show(self):
        print(f"hello {self.name}, welcome to {self.company}")

# class programmer:
#     company = "Apple INC"
#     def show(self):
#         print(f"name the of the intern is {self.name} and his salary is {self.salary}")

#     def showLang(self):
#         print(f"the intern is a master of {self.lang}")

# INSTEAD OF WRITING THIS LONG CODE WE CAN SIMPLY USE:

class programmer(intern):
    company = "Apple INC"
    def showLang(self):
        print(f"the intern is a master of {self.lang}")

a = intern
b = programmer

print(a.company, b.company)