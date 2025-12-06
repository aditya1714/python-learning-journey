"""Write a program to fill in a letter template given below with name and date."""


letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''

Name = input("Enter your name : ")
print(letter.replace("<|Name|>", Name ).replace("<|Date|>", "22/11/2025") )