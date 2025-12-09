class intern:
    a = 3 

    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

e = intern()
e.a = 45 

e.show()