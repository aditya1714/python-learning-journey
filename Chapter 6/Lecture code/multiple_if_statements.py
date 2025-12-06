a = int(input("enter your age : "))

#if statement no -1.
if(a%2== 0):
    print("a is even")
# end of if statement no -1.

#if statement no -2.
if(a>=18):       
    print("You are allowed")

elif(a<0):
    print("Are you stupid ? ")

elif(a==0):
    print("Invalid age")

else:
    print("Go and watch cartoon kid")

# end of if statement no -2.


# only if can be used alone.
# "elif" and "else" can't be used alone they need "if" to functin without "if" it will show error.