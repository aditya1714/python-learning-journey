class intern:
    company = "Apple"
    name = "Vikram Aditya"
    def show(self):
        print(f"hello {self.name}, welcome to {self.company}")

class Coder :
    Lang = "Pyhton"
    def printLang(self):
        print(f"your programming language is {self.Lang}")


class programmer(intern, Coder ):
    company = "Apple INC"
    def showLang(self):
        print(f"the intern is a master of {self.Lang}")

a = intern()
b = programmer()

b.show()
b.showLang()
b.printLang()