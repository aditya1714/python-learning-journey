'''Write a program to find out whether a given post is talking about “Harry” or not.'''

post = input("enter your post : ")

if("Harry" in post.lower()):
    print("harry is in there")
else:
    print("harry not found")