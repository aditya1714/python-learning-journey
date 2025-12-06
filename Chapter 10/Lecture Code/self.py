class employee: # this is a class attribute
    name = "Aditya"
    lang = "Python"
    salary = 120000

    def getinfo(self):
        print(f"{self.name} your salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning,")
Aditya = employee()  
# Aditya.name = "Vikram Aditya" # this is a instance attribute
Aditya.getinfo()
Aditya.greet()
