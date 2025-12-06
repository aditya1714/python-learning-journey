class employee: # this is a class attribute
    name = "Aditya"
    lang = "Python"
    salary = 120000

Aditya = employee()  
Aditya.name = "Vikram Aditya" # this is a instance attribute
print(Aditya.name, Aditya.lang, Aditya.salary)

# using instance attribute will overwrite the class attribute when you run the code here in class name = "Aditya" and in instance in becomes "Vikram Aditya".