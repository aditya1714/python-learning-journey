'''Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?'''

class Demo:
    a = 5

object = Demo() 
print(object.a) # Prints class attribute because instance attribute is not present.
object.a = 0 # Instance attribute is present.
print(object.a)# Prints instance attribute because instance attribute is present.
print(Demo.a) # Prints class atribute.