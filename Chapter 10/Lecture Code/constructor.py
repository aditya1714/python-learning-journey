class employee: # this is a class attribute
    name = "Aditya"
    lang = "Python"
    salary = 120000

    def __init__(self, name, salary, lang): # it is a dunder which is automatically called
        self.name = name
        self.salary = salary
        self.lang = lang
        print("i am creating an object")

    def getinfo(self):
        print(f"{self.name} your salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning,")

Aditya = employee("Vikram Aditya", 1200000, "C++")  
# Aditya.name = "Vikram Aditya"
print(Aditya.name, Aditya.salary, Aditya.lang)
